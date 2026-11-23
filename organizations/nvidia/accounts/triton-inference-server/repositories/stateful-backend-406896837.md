# triton-inference-server/stateful_backend

- Company: NVIDIA
- GitHub account: [https://github.com/triton-inference-server](https://github.com/triton-inference-server)
- Mapping status: official-project-linked
- Repository: [triton-inference-server/stateful_backend](https://github.com/triton-inference-server/stateful_backend)
- Default branch: main
- README: [Open upstream README](https://github.com/triton-inference-server/stateful_backend/blob/main/README.md)
- README blob SHA: 553607c6a13314bfd410096837dac1ee78070e14
- Repository ID: 406896837
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Triton backend for managing the model state tensors automatically in sequence batcher

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:46:41+00:00

### Short excerpt (up to 100 words)

> This repository contains the Stateful Backend for Triton Inference Server. You can learn more about backends in the backend repo. Ask questions or report problems in the main Triton issues page. The backend code automatically manages the input and output states of a model. The states are associated with a sequence id and need to be tracked for inference requests associated with the sequence id. The backend currently handles ONNX models, however, it can be extended to other model types. The example stateful model above has matching input and output tensors representing the model states. An output state tensor for

### README headings

- Triton Stateful Backend
- Building the backend
- Using the backend with Triton
- Testing the backend
- Example Triton model
- Additional features
- Limitations

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 196,869 |
| Python | 47,824 |
| Cuda | 8,574 |
| CMake | 8,296 |
| Shell | 1,244 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- client/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 17
- Forks at capture: 7
- Last updated: 2026-04-22T08:08:03Z
- Last pushed: 2024-02-12T16:39:27Z
- Topics: backend, stateful, triton

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/triton-inference-server/stateful_backend)
- [README](https://github.com/triton-inference-server/stateful_backend/blob/main/README.md)
- [Issues](https://github.com/triton-inference-server/stateful_backend/issues)
- [Releases](https://github.com/triton-inference-server/stateful_backend/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
