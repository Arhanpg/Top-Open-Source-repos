# triton-inference-server/hugectr_backend

- Company: NVIDIA
- GitHub account: [https://github.com/triton-inference-server](https://github.com/triton-inference-server)
- Mapping status: official-project-linked
- Repository: [triton-inference-server/hugectr_backend](https://github.com/triton-inference-server/hugectr_backend)
- Default branch: main
- README: [Open upstream README](https://github.com/triton-inference-server/hugectr_backend/blob/main/README.md)
- README blob SHA: b0bf8a464e68908c884d313d9f7af9fbc52f4b51
- Repository ID: 332048175
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:33:17+00:00

### Short excerpt (up to 100 words)

> --> The Hierarchical Parameter Server(HPS) Backend is a framework for embedding vectors looking up on large-scale embedding tables that was designed to effectively use GPU memory to accelerate the looking up by decoupling the embedding tables and embedding cache from the end-to-end inference pipeline of the deep recommendation model. The HPS Backend supports executing multiple embedding vector looking-up services concurrently across multiple GPUs by embedding cache that is shared between multiple look_up sessions. For more information, see Hierarchical Parameter Server Architecture. You can build the HPS Backend from scratch and install to the specify path based on your own specific

### README headings

- Copyright (c) 2020, NVIDIA CORPORATION. All rights reserved.
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
- Hierarchical Parameter Server Backend
- Quick Start
- Install the HPS Backend Using NGC Containers
- Build the HPS Backend from Scratch
- Independent Inference Hierarchical Parameter Server Configuration
- Model Repository Extension
- Metrix

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Jupyter Notebook | 215,593 |
| C++ | 139,169 |
| CMake | 9,432 |
| Shell | 1,762 |
| Dockerfile | 1,492 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- hps_backend/CMakeLists.txt (capture: captured)
- hps_backend/samples/hps-triton-ensemble/requirements.txt (capture: captured) — dependency clues: jupyter, onnx, tensorflow, tf2onnx, torch

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: BSD-3-Clause
- Stars at capture: 58
- Forks at capture: 13
- Last updated: 2026-10-30T04:43:47Z
- Last pushed: 2023-10-17T07:00:00Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/triton-inference-server/hugectr_backend)
- [README](https://github.com/triton-inference-server/hugectr_backend/blob/main/README.md)
- [Issues](https://github.com/triton-inference-server/hugectr_backend/issues)
- [Releases](https://github.com/triton-inference-server/hugectr_backend/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
