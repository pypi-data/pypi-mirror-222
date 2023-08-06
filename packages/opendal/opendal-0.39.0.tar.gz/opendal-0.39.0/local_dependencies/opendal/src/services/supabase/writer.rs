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
use bytes::Bytes;
use http::StatusCode;

use super::core::*;
use super::error::parse_error;
use crate::raw::*;
use crate::*;

pub struct SupabaseWriter {
    core: Arc<SupabaseCore>,

    op: OpWrite,
    path: String,
}

impl SupabaseWriter {
    pub fn new(core: Arc<SupabaseCore>, path: &str, op: OpWrite) -> Self {
        SupabaseWriter {
            core,
            op,
            path: path.to_string(),
        }
    }

    pub async fn upload(&self, bytes: Bytes) -> Result<()> {
        let size = bytes.len();
        let mut req = self.core.supabase_upload_object_request(
            &self.path,
            Some(size),
            self.op.content_type(),
            AsyncBody::Bytes(bytes),
        )?;

        self.core.sign(&mut req)?;

        let resp = self.core.send(req).await?;

        match resp.status() {
            StatusCode::OK => {
                resp.into_body().consume().await?;
                Ok(())
            }
            _ => Err(parse_error(resp).await?),
        }
    }
}

#[async_trait]
impl oio::Write for SupabaseWriter {
    async fn write(&mut self, bs: Bytes) -> Result<()> {
        if bs.is_empty() {
            return Ok(());
        }

        self.upload(bs).await
    }

    async fn sink(&mut self, _size: u64, _s: oio::Streamer) -> Result<()> {
        Err(Error::new(
            ErrorKind::Unsupported,
            "Write::sink is not supported",
        ))
    }

    async fn abort(&mut self) -> Result<()> {
        Err(Error::new(
            ErrorKind::Unsupported,
            "The abort operation is not yet supported for Supabase backend",
        ))
    }

    async fn close(&mut self) -> Result<()> {
        Ok(())
    }
}
