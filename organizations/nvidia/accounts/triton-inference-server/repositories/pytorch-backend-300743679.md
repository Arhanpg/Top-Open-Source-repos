# triton-inference-server/pytorch_backend

- Company: NVIDIA
- GitHub account: [https://github.com/triton-inference-server](https://github.com/triton-inference-server)
- Mapping status: official-project-linked
- Repository: [triton-inference-server/pytorch_backend](https://github.com/triton-inference-server/pytorch_backend)
- Default branch: main
- README: [Open upstream README](https://github.com/triton-inference-server/pytorch_backend/blob/main/README.md)
- README blob SHA: e832f922322e7b06ccd6baba90b6876fe109b5e5
- Repository ID: 300743679
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Triton backend for the PyTorch TorchScript models.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:46:31+00:00

### Short excerpt (up to 100 words)

> --> The Triton backend for is designed to run models using the PyTorch C++ API. All models created in PyTorch using the python API must be traced/scripted to produce a TorchScript model. You can learn more about Triton backends in the repository. Ask questions or report problems using Be sure to read all the information below as well as the available in the Triton Server repository. Use a recent cmake to build. First install the required dependencies. apt-get install rapidjson-dev python3-dev python3-pip pip3 install patchelf==0.18.0 An appropriate PyTorch container from NVIDIA NGC Catalog must be used. For example, to build

### README headings

- Copyright 2020-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
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
- PyTorch (LibTorch) Backend
- Build the PyTorch Backend
- Build the PyTorch Backend With Custom PyTorch
- Using the PyTorch Backend
- AOT Inductor Support
- Model Configuration
- Ordinal Base I/O Names

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 326,973 |
| CMake | 26,881 |
| Python | 12,350 |
| Shell | 2,540 |

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
- Stars at capture: 184
- Forks at capture: 82
- Last updated: 2026-10-22T16:18:53Z
- Last pushed: 2026-11-19T17:49:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/triton-inference-server/pytorch_backend)
- [README](https://github.com/triton-inference-server/pytorch_backend/blob/main/README.md)
- [Issues](https://github.com/triton-inference-server/pytorch_backend/issues)
- [Releases](https://github.com/triton-inference-server/pytorch_backend/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
