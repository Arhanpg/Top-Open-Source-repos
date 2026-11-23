# triton-inference-server/identity_backend

- Company: NVIDIA
- GitHub account: [https://github.com/triton-inference-server](https://github.com/triton-inference-server)
- Mapping status: official-project-linked
- Repository: [triton-inference-server/identity_backend](https://github.com/triton-inference-server/identity_backend)
- Default branch: main
- README: [Open upstream README](https://github.com/triton-inference-server/identity_backend/blob/main/README.md)
- README blob SHA: 2bcd8e87ba0a261494cb0365d7cd8f47a0c0b65b
- Repository ID: 285115542
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Example Triton backend that demonstrates most of the Triton Backend API.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:33:19+00:00

### Short excerpt (up to 100 words)

> --> A simple Triton backend that copies input tensors to corresponding output tensors. This backend is used primarily for testing. To learn more about writing your own Triton backend including simple examples, see the documentation included in the [backend repo](https://github.com/triton-inference-server/backend). Ask questions or report problems with the Identity backend in the main Triton [issues page](https://github.com/triton-inference-server/server/issues). Use cmake to build and install in a local directory. $ mkdir build $ cd build $ cmake -DTRITON_ENABLE_GPU=ON -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/install .. $ make install The following required Triton repositories will be pulled and used in the build. By default the "main" branch/tag will be used

### README headings

- Copyright 2020-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
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
- Triton Inference Server Identity Backend
- Build
- Custom Metric Example
- HELP input_byte_size_counter Cumulative input byte size of all requests received by the model
- TYPE input_byte_size_counter counter

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 52,855 |
| CMake | 8,076 |

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
- Stars at capture: 6
- Forks at capture: 18
- Last updated: 2026-10-06T21:47:58Z
- Last pushed: 2026-11-02T23:26:25Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/triton-inference-server/identity_backend)
- [README](https://github.com/triton-inference-server/identity_backend/blob/main/README.md)
- [Issues](https://github.com/triton-inference-server/identity_backend/issues)
- [Releases](https://github.com/triton-inference-server/identity_backend/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
