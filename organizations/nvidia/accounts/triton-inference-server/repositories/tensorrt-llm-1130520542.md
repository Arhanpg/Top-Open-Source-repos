# triton-inference-server/TensorRT-LLM

- Company: NVIDIA
- GitHub account: [https://github.com/triton-inference-server](https://github.com/triton-inference-server)
- Mapping status: official-project-linked
- Repository: [triton-inference-server/TensorRT-LLM](https://github.com/triton-inference-server/TensorRT-LLM)
- Default branch: main
- README: [Open upstream README](https://github.com/triton-inference-server/TensorRT-LLM/blob/main/README.md)
- README blob SHA: 4414e19fc01a00d74a245d8948aec6db7d279778
- Repository ID: 1130520542
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:46:45+00:00

### Short excerpt (up to 100 words)

> TensorRT LLM =========================== * [11/17] NVFP4 MLA: Unified 4-bit KV Cache Storage and Attention Compute in TensorRT LLM ✨ ➡️ link * [11/11] Dense DWDP: Extending Distributed Weight Data Parallelism to Dense Weights on Vera Rubin NVL72 ✨ ➡️ link * [11/03] ISER-MoE: In-Switch Expert Replication for Load-Balanced MoE Prefill ✨ ➡️ link * [10/14] KV Cache Compression in TensorRT LLM ✨ ➡️ link * [09/22] GVR V2: Self-Sampling and Multi-Thresholding for Faster Exact Top-K ✨ ➡️ link * [09/02] Accelerating Video Generation with GEMM Quantization, Attention Quantization and Skip Softmax Attention in TensorRT-LLM ✨ ➡️ link * [08/20] Evaluating

### README headings

- Tech Blogs
- Latest News
- TensorRT LLM Overview
- Getting Started
- Deprecation Policy
- Telemetry Data Collection
- Opting Out of Telemetry Data Collection
- Useful Links

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 162,126,140 |
| C++ | 33,165,726 |
| Cuda | 13,551,592 |
| Groovy | 918,464 |
| Shell | 403,977 |
| CMake | 392,131 |
| Jinja | 73,453 |
| C | 66,929 |
| Makefile | 35,892 |
| JavaScript | 12,173 |
| Standard ML | 11,101 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)
- requirements.txt (capture: captured) — dependency clues: PyNvVideoCodec, StrEnum, accelerate, aenum, apache-tvm-ffi, backoff, blake3, blobfile, build, cache-dit, click, click_option_group, colored, cuda-core, cuda-python, cuda-tile, datasets, diffusers, einops, etcd-sdk-python
- setup.py (capture: captured)
- 3rdparty/CMakeLists.txt (capture: captured)
- agent-flow/pyproject.toml (capture: captured) — dependency clues: anyio, claude-agent-sdk, jinja2, openai-codex, pytest, pytest-asyncio, pyyaml, rich
- cpp/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: True
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 8
- Forks at capture: 1
- Last updated: 2026-11-12T15:07:06Z
- Last pushed: 2026-11-23T20:06:49Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/triton-inference-server/TensorRT-LLM)
- [README](https://github.com/triton-inference-server/TensorRT-LLM/blob/main/README.md)
- [Issues](https://github.com/triton-inference-server/TensorRT-LLM/issues)
- [Releases](https://github.com/triton-inference-server/TensorRT-LLM/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
