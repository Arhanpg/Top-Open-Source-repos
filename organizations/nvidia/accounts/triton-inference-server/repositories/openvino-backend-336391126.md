# triton-inference-server/openvino_backend

- Company: NVIDIA
- GitHub account: [https://github.com/triton-inference-server](https://github.com/triton-inference-server)
- Mapping status: official-project-linked
- Repository: [triton-inference-server/openvino_backend](https://github.com/triton-inference-server/openvino_backend)
- Default branch: main
- README: [Open upstream README](https://github.com/triton-inference-server/openvino_backend/blob/main/README.md)
- README blob SHA: 98211ee86805189528fc20f32259f41b62b822b9
- Repository ID: 336391126
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

OpenVINO backend for Triton.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:33:28+00:00

### Short excerpt (up to 100 words)

> --> **Note: The OpenVINO backend is co-maintained by Nvidia and Intel.** The Triton backend for the can learn more about Triton backends in the [backend repo](https://github.com/triton-inference-server/backend). Ask questions or report problems in the main Triton [issues page](https://github.com/triton-inference-server/server/issues). The backend is designed to run models in Intermediate Representation (IR), TensorFlow saved_model, TensorFlow Lite, ONNX and PaddlePaddle. PyTorch models can be used after converting to IR or ONNX. See here for instruction. The backend is implemented using OpenVINO C++ API. OpenVINO backend in the public docker image version currently supports inference only on Intel CPU devices using OpenVINO CPU plugin. Note the

### README headings

- Copyright 2021-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
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
- OpenVINO Backend
- Supported Devices
- Build the OpenVINO Backend
- Build a complete triton custom image with OpenVINO backend
- Add Intel GPU and NPU dependencies to the image
- Using the OpenVINO Backend
- Parameters

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 74,053 |
| Python | 26,071 |
| CMake | 12,043 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- pyproject.toml (capture: captured)
- tests/requirements.txt (capture: captured) — dependency clues: pytest, requests, tritonclient

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: BSD-3-Clause
- Stars at capture: 39
- Forks at capture: 24
- Last updated: 2026-10-06T22:55:09Z
- Last pushed: 2026-11-04T22:57:07Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/triton-inference-server/openvino_backend)
- [README](https://github.com/triton-inference-server/openvino_backend/blob/main/README.md)
- [Issues](https://github.com/triton-inference-server/openvino_backend/issues)
- [Releases](https://github.com/triton-inference-server/openvino_backend/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
