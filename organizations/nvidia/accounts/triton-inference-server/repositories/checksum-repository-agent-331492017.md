# triton-inference-server/checksum_repository_agent

- Company: NVIDIA
- GitHub account: [https://github.com/triton-inference-server](https://github.com/triton-inference-server)
- Mapping status: official-project-linked
- Repository: [triton-inference-server/checksum_repository_agent](https://github.com/triton-inference-server/checksum_repository_agent)
- Default branch: main
- README: [Open upstream README](https://github.com/triton-inference-server/checksum_repository_agent/blob/main/README.md)
- README blob SHA: 7952dc9cf42cd9cf6df820ae205faccefe2fab98
- Repository ID: 331492017
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Triton repository agent that verifies model checksums.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:17:03+00:00

### Short excerpt (up to 100 words)

> --> This repo contains an example [repository agent](https://github.com/triton-inference-server/server/blob/master/docs/repository_agents.md) for verifying file checksums before loading the model. Ask questions or report problems in the main Triton [issues page](https://github.com/triton-inference-server/server/issues). Use a recent cmake to build. First install the required dependencies. $ apt-get install openssl-dev To build the repository agent: $ mkdir build $ cd build $ cmake -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/install .. $ make install The following required Triton repositories will be pulled and used in the build. By default the "main" branch/tag will be used for each repo but the following CMake arguments can be used to override. * triton-inference-server/core: -DTRITON_CORE_REPO_TAG=[tag] * triton-inference-server/common: -DTRITON_COMMON_REPO_TAG=[tag]

### README headings

- Copyright (c) 2021, NVIDIA CORPORATION. All rights reserved.
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
- Triton Checksum Repository Agent
- Build the Checksum Repository Agent
- Using the Checksum Repository Agent

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 8,366 |
| CMake | 7,240 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- pyproject.toml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: BSD-3-Clause
- Stars at capture: 14
- Forks at capture: 13
- Last updated: 2026-10-06T21:47:44Z
- Last pushed: 2026-11-02T23:26:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/triton-inference-server/checksum_repository_agent)
- [README](https://github.com/triton-inference-server/checksum_repository_agent/blob/main/README.md)
- [Issues](https://github.com/triton-inference-server/checksum_repository_agent/issues)
- [Releases](https://github.com/triton-inference-server/checksum_repository_agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
