# triton-inference-server/fastertransformer_backend

- Company: NVIDIA
- GitHub account: [https://github.com/triton-inference-server](https://github.com/triton-inference-server)
- Mapping status: official-project-linked
- Repository: [triton-inference-server/fastertransformer_backend](https://github.com/triton-inference-server/fastertransformer_backend)
- Default branch: main
- README: [Open upstream README](https://github.com/triton-inference-server/fastertransformer_backend/blob/main/README.md)
- README blob SHA: f940aa868e0aa744c10336519d0fde1bdaa2c11b
- Repository ID: 354999045
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:21:29+00:00

### Short excerpt (up to 100 words)

> --> **Note: FasterTransformer development has transitioned to TensorRT-LLM. All developers are encouraged to leverage TensorRT-LLM and tensorrtllm_backend to get the latest improvements on LLM Inference. The NVIDIA/FasterTransformer repo will stay up, but will not have further development.** The Triton backend for the FasterTransformer. This repository provides a script and recipe to run the highly optimized transformer-based encoder and decoder component, and it is tested and maintained by NVIDIA. In the FasterTransformer v4.0, it supports multi-gpu inference on GPT-3 model. This backend integrates FasterTransformer into Triton to use giant GPT-3 model serving by Triton. In the below example, we will show

### README headings

- Copyright 2021-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
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
- FasterTransformer Backend
- Table Of Contents
- Support matrix
- Introduction
- Setup
- Prepare docker images
- Create your own Triton container. You can skip this step (done in trtionserver/server)

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 462,451 |
| C++ | 77,548 |
| Shell | 70,509 |
| CMake | 18,270 |
| Dockerfile | 2,855 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- docker/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: BSD-3-Clause
- Stars at capture: 414
- Forks at capture: 137
- Last updated: 2026-08-20T05:59:08Z
- Last pushed: 2023-11-11T00:41:49Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/triton-inference-server/fastertransformer_backend)
- [README](https://github.com/triton-inference-server/fastertransformer_backend/blob/main/README.md)
- [Issues](https://github.com/triton-inference-server/fastertransformer_backend/issues)
- [Releases](https://github.com/triton-inference-server/fastertransformer_backend/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
