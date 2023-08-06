// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

use std::sync::Arc;

use async_trait::async_trait;
use bytes::Buf;
use bytes::Bytes;
use http::StatusCode;

use super::core::*;
use super::error::parse_error;
use crate::raw::*;
use crate::*;

pub struct ObsWriter {
    core: Arc<ObsCore>,

    op: OpWrite,
    path: String,
    upload_id: Option<String>,

    parts: Vec<CompleteMultipartUploadRequestPart>,
    buffer: oio::VectorCursor,
    buffer_size: usize,
}

impl ObsWriter {
    pub fn new(core: Arc<ObsCore>, path: &str, op: OpWrite) -> Self {
        let buffer_size = core.write_min_size;
        ObsWriter {
            core,
            path: path.to_string(),
            op,

            upload_id: None,
            parts: vec![],
            buffer: oio::VectorCursor::new(),
            buffer_size,
        }
    }

    async fn write_oneshot(&self, size: u64, body: AsyncBody) -> Result<()> {
        let mut req = self.core.obs_put_object_request(
            &self.path,
            Some(size),
            self.op.content_type(),
            self.op.cache_control(),
            body,
        )?;

        self.core.sign(&mut req).await?;

        let resp = self.core.send(req).await?;

        let status = resp.status();

        match status {
            StatusCode::CREATED | StatusCode::OK => {
                resp.into_body().consume().await?;
                Ok(())
            }
            _ => Err(parse_error(resp).await?),
        }
    }

    async fn initiate_upload(&self) -> Result<String> {
        let resp = self
            .core
            .obs_initiate_multipart_upload(&self.path, self.op.content_type())
            .await?;

        let status = resp.status();

        match status {
            StatusCode::OK => {
                let bs = resp.into_body().bytes().await?;

                let result: InitiateMultipartUploadResult =
                    quick_xml::de::from_reader(bs.reader()).map_err(new_xml_deserialize_error)?;

                Ok(result.upload_id)
            }
            _ => Err(parse_error(resp).await?),
        }
    }

    async fn write_part(
        &self,
        upload_id: &str,
        bs: Bytes,
    ) -> Result<CompleteMultipartUploadRequestPart> {
        // Obs service requires part number must between [1..=10000]
        let part_number = self.parts.len() + 1;

        let resp = self
            .core
            .obs_upload_part_request(
                &self.path,
                upload_id,
                part_number,
                Some(bs.len() as u64),
                AsyncBody::Bytes(bs),
            )
            .await?;

        let status = resp.status();

        match status {
            StatusCode::OK => {
                let etag = parse_etag(resp.headers())?
                    .ok_or_else(|| {
                        Error::new(
                            ErrorKind::Unexpected,
                            "ETag not present in returning response",
                        )
                    })?
                    .to_string();

                resp.into_body().consume().await?;

                Ok(CompleteMultipartUploadRequestPart { part_number, etag })
            }
            _ => Err(parse_error(resp).await?),
        }
    }
}

#[async_trait]
impl oio::Write for ObsWriter {
    async fn write(&mut self, bs: Bytes) -> Result<()> {
        let upload_id = match &self.upload_id {
            Some(upload_id) => upload_id,
            None => {
                if self.op.content_length().unwrap_or_default() == bs.len() as u64 {
                    return self
                        .write_oneshot(bs.len() as u64, AsyncBody::Bytes(bs))
                        .await;
                } else {
                    let upload_id = self.initiate_upload().await?;
                    self.upload_id = Some(upload_id);
                    self.upload_id.as_deref().unwrap()
                }
            }
        };

        // Ignore empty bytes
        if bs.is_empty() {
            return Ok(());
        }

        self.buffer.push(bs);
        // Return directly if the buffer is not full
        if self.buffer.len() <= self.buffer_size {
            return Ok(());
        }

        let bs = self.buffer.peak_at_least(self.buffer_size);
        let size = bs.len();

        match self.write_part(upload_id, bs).await {
            Ok(part) => {
                self.buffer.take(size);
                self.parts.push(part);
                Ok(())
            }
            Err(e) => {
                // If the upload fails, we should pop the given bs to make sure
                // write is re-enter safe.
                self.buffer.pop();
                Err(e)
            }
        }
    }

    async fn sink(&mut self, size: u64, s: oio::Streamer) -> Result<()> {
        if self.op.content_length().unwrap_or_default() == size {
            return self.write_oneshot(size, AsyncBody::Stream(s)).await;
        } else {
            return Err(Error::new(
                ErrorKind::Unsupported,
                "Obs does not support streaming multipart upload",
            ));
        }
    }

    async fn abort(&mut self) -> Result<()> {
        let upload_id = if let Some(upload_id) = &self.upload_id {
            upload_id
        } else {
            return Ok(());
        };

        let resp = self
            .core
            .obs_abort_multipart_upload(&self.path, upload_id)
            .await?;
        match resp.status() {
            // Obs returns code 204 No Content if abort succeeds.
            // Reference: https://support.huaweicloud.com/intl/en-us/api-obs/obs_04_0103.html
            StatusCode::NO_CONTENT => {
                resp.into_body().consume().await?;
                Ok(())
            }
            _ => Err(parse_error(resp).await?),
        }
    }

    async fn close(&mut self) -> Result<()> {
        let upload_id = if let Some(upload_id) = &self.upload_id {
            upload_id
        } else {
            return Ok(());
        };

        // Make sure internal buffer has been flushed.
        if !self.buffer.is_empty() {
            let bs = self.buffer.peak_exact(self.buffer.len());

            match self.write_part(upload_id, bs).await {
                Ok(part) => {
                    self.buffer.clear();
                    self.parts.push(part);
                }
                Err(e) => {
                    return Err(e);
                }
            }
        }

        let resp = self
            .core
            .obs_complete_multipart_upload(&self.path, upload_id, &self.parts)
            .await?;

        let status = resp.status();

        match status {
            StatusCode::OK => {
                resp.into_body().consume().await?;

                Ok(())
            }
            _ => Err(parse_error(resp).await?),
        }
    }
}
