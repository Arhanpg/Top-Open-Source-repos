# NVIDIA/cutile-python

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/cutile-python](https://github.com/NVIDIA/cutile-python)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/cutile-python/blob/main/README.md)
- README blob SHA: 5d3e9a8840c3831463a800d2de461b8d90ef095b
- README bytes captured: 6116
- README truncated at capture limit: False
- Repository ID: 1001718807
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

cuTile is a programming model for writing parallel kernels for NVIDIA GPUs

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T22:50:50+00:00

### Short excerpt (up to 300 words)

> cuTile Python ============= cuTile import cuda.tile as ct

### README headings

- This examples uses CuPy which can be installed via `pip install cupy-cuda13x`
- Make sure cuda toolkit 13.1+ is installed: https://developer.nvidia.com/cuda-downloads
- cuTile kernel for adding two dense vectors. It runs in parallel on the GPU.
- Generate input arrays
- Allocate an output array and launch the kernel
- Verify the results

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> cuTile Python ============= cuTile

### Getting started and usage: Make sure cuda toolkit 13.1+ is installed: https://developer.nvidia.com/cuda-downloads

> import cuda.tile as ct

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 6,312,535 |
| C++ | 870,228 |
| CMake | 12,984 |
| CSS | 5,761 |
| C | 2,202 |
| Shell | 1,917 |
| Makefile | 1,250 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: cuda-toolkit, typing-extensions
- setup.py (capture: captured)
- cext/CMakeLists.txt (capture: captured)
- docs/Makefile (capture: captured)
- docs/requirements.txt (capture: captured) — dependency clues: myst-parser, nvidia-sphinx-theme, pydata-sphinx-theme, sphinx

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 2172
- Forks at capture: 162
- Last updated: 2026-11-20T16:03:27Z
- Last pushed: 2026-11-21T11:06:36Z
- Topics: cutile, gpu, kernel, parallel-kernels, python, tile, tile-based-programming

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/cutile-python)
- [README](https://github.com/NVIDIA/cutile-python/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/cutile-python/issues)
- [Releases](https://github.com/NVIDIA/cutile-python/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
