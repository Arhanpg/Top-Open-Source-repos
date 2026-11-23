# triton-inference-server/redis_cache

- Company: NVIDIA
- GitHub account: [https://github.com/triton-inference-server](https://github.com/triton-inference-server)
- Mapping status: official-project-linked
- Repository: [triton-inference-server/redis_cache](https://github.com/triton-inference-server/redis_cache)
- Default branch: main
- README: [Open upstream README](https://github.com/triton-inference-server/redis_cache/blob/main/README.md)
- README blob SHA: 5ca79e4e24284c50f0048eb69ec5215c0d809046
- Repository ID: 563046915
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

TRITONCACHE implementation of a Redis cache

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:46:34+00:00

### Short excerpt (up to 100 words)

> --> This repo contains an example for caching data with Redis. Ask questions or report problems in the main Triton [issues page](https://github.com/triton-inference-server/server/issues). If you don't have it installed already - install rapidjson-dev: apt install rapidjson-dev Use a recent cmake to build and run the following: $ mkdir build $ cd build $ cmake -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/install .. $ make install The following required Triton repositories will be pulled and used in the build. By default the "main" branch/tag will be used for each repo but the following CMake arguments can be used to override. * triton-inference-server/core: `-D TRITON_CORE_REPO_TAG=[tag]` * triton-inference-server/common: `-D TRITON_COMMON_REPO_TAG=[tag]`

### README headings

- Copyright 2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
- Redistribution and use in source and binary forms, with or without
- modification, are permitted provided that the following conditions
- are met:
- * Redistributions of source code must retain the above copyright
- notice, this list of conditions and the following disclaimer.
- * Redistributions in binary form must reproduce the above copyright
- notice, this list of conditions and the following disclaimer in the
- documentation and/or other materials provided with the distribution.
- * Neither the name of NVIDIA CORPORATION nor the names of its
- contributors may be used to endorse or promote products derived
- from this software without specific prior written permission.
- THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
- EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
- IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
- PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
- CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
- EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
- PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
- PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
- OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
- (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
- OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
- Triton Redis Cache
- Build the Cache
- Using the Cache
- Deploying to Triton
- Configuration
- Available Configuration Options
- Optional Environment Variables for Credentials

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 19,131 |
| CMake | 7,435 |
| Shell | 1,743 |
| Dockerfile | 136 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- Dockerfile (capture: captured)
- pyproject.toml (capture: captured)
- examples/tls/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: BSD-3-Clause
- Stars at capture: 18
- Forks at capture: 9
- Last updated: 2026-10-06T05:32:07Z
- Last pushed: 2026-11-02T23:27:14Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/triton-inference-server/redis_cache)
- [README](https://github.com/triton-inference-server/redis_cache/blob/main/README.md)
- [Issues](https://github.com/triton-inference-server/redis_cache/issues)
- [Releases](https://github.com/triton-inference-server/redis_cache/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
