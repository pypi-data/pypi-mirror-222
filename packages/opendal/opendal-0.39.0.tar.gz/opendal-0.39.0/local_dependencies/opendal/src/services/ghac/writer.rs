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

use async_trait::async_trait;
use bytes::Bytes;

use super::backend::GhacBackend;
use super::error::parse_error;
use crate::raw::*;
use crate::*;

pub struct GhacWriter {
    backend: GhacBackend,

    cache_id: i64,
    size: u64,
}

impl GhacWriter {
    pub fn new(backend: GhacBackend, cache_id: i64) -> Self {
        GhacWriter {
            backend,
            cache_id,
            size: 0,
        }
    }
}

#[async_trait]
impl oio::Write for GhacWriter {
    async fn write(&mut self, bs: Bytes) -> Result<()> {
        let size = bs.len() as u64;
        let req = self
            .backend
            .ghac_upload(self.cache_id, size, AsyncBody::Bytes(bs))
            .await?;

        let resp = self.backend.client.send(req).await?;

        if resp.status().is_success() {
            resp.into_body().consume().await?;
            self.size += size;
            Ok(())
        } else {
            Err(parse_error(resp)
                .await
                .map(|err| err.with_operation("Backend::ghac_upload"))?)
        }
    }

    async fn sink(&mut self, _size: u64, _s: oio::Streamer) -> Result<()> {
        Err(Error::new(
            ErrorKind::Unsupported,
            "Write::sink is not supported",
        ))
    }

    async fn abort(&mut self) -> Result<()> {
        Ok(())
    }

    async fn close(&mut self) -> Result<()> {
        let req = self.backend.ghac_commit(self.cache_id, self.size).await?;
        let resp = self.backend.client.send(req).await?;

        if resp.status().is_success() {
            resp.into_body().consume().await?;
            Ok(())
        } else {
            Err(parse_error(resp)
                .await
                .map(|err| err.with_operation("Backend::ghac_commit"))?)
        }
    }
}
