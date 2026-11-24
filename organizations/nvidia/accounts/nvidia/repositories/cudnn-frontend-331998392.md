# NVIDIA/cudnn-frontend

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/cudnn-frontend](https://github.com/NVIDIA/cudnn-frontend)
- Default branch: develop
- README: [Open upstream README](https://github.com/NVIDIA/cudnn-frontend/blob/develop/README.md)
- README blob SHA: 51bc2b0a620a80fd14a19eb590f8aacb5c149c3e
- README bytes captured: 17703
- README truncated at capture limit: False
- Repository ID: 331998392
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

cuDNN Frontend is NVIDIA's modern, open-source entry point to the cuDNN library and a growing collection of high-performance open-source kernels.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T21:51:26+00:00

### Short excerpt (up to 300 words)

> **Unified Graph API:** Create **Developer Guide:** Official NVIDIA

### README headings

- cuDNN Frontend (FE)
- 🚀 Latest news:
- Tech talks
- 🔥🔥🔥  SOTA Attention Kernels from cudnn backend
- Llama 3.1 style Forward and Bprop with causal masking (GB300)
- Deepseek v3 style Forward and Bprop with causal masking (GB300)
- New OSS Linear Attention Kernels
- GDN Forward and Bprop (GB300)
- KDA Forward and Bprop (GB300)
- GDN-2 Forward and Bprop (GB300)
- GDP Forward and Bprop (GB300)
- Mamba-2 Forward and Bprop (GB300)
- Key Features
- Installation
- 🐍 Python
- ⚙️ C++ (Header Only)
- Building from Source
- Documentation & Examples
- 🤝 Contributing
- Debugging
- Log to stdout
- Log to a file
- Offer the maturing open-source engines (FROST GEMM / SDPA) as plan candidates.
- Where JIT-compiled kernels are cached (default: $XDG_CACHE_HOME/cudnn_gemm/kernel_cache).
- Environment report
- CUDA graph retention
- Overriding the CUDA runtime library
- or an absolute path
- or the full path to the selected CUDA 13 runtime DLL
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Key Features

> **Unified Graph API:** Create

### Getting started and usage: Documentation & Examples

> **Developer Guide:** Official NVIDIA

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Cuda | 91,488,765 |
| Python | 90,002,803 |
| C++ | 3,359,278 |
| C | 87,386 |
| CMake | 22,097 |
| Standard ML | 10,082 |
| Dockerfile | 3,960 |
| Shell | 2,434 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: apache-tvm-ffi, cuda-python, cuda-tile, nvidia-cutlass-dsl, nvshmem4py-cu13, triton
- requirements.txt (capture: captured) — dependency clues: black, clang-format, cuda-python, jupyter, looseversion, nanobind, numpy, pytest, pytest-xdist
- setup.py (capture: captured)
- aot/CMakeLists.txt (capture: captured)
- python/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1011
- Forks at capture: 344
- Last updated: 2026-11-23T08:44:56Z
- Last pushed: 2026-11-23T13:46:20Z
- Topics: attention, blackwell, cuda, cuda-kernels, cuda-toolkit, deep-learning, flash-attention, fp8, gemm, gpu, grouped-gemm, hopper, mixture-of-experts, moe, mxfp8, normalization, nvfp4, nvidia, sdpa, transformer

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/cudnn-frontend)
- [README](https://github.com/NVIDIA/cudnn-frontend/blob/develop/README.md)
- [Issues](https://github.com/NVIDIA/cudnn-frontend/issues)
- [Releases](https://github.com/NVIDIA/cudnn-frontend/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
