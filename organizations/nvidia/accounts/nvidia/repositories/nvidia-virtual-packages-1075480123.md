# NVIDIA/nvidia-virtual-packages

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/nvidia-virtual-packages](https://github.com/NVIDIA/nvidia-virtual-packages)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/nvidia-virtual-packages/blob/main/README.md)
- README blob SHA: 1f78403c13c7f7de0e82e58106f10187467ea93c
- README bytes captured: 5859
- README truncated at capture limit: False
- Repository ID: 1075480123
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A conda plugin which creates NVIDIA-specific virtual packages

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:47:11+00:00

### Short excerpt (up to 300 words)

> If your program benefits

### README headings

- nvidia-virtual-packages
- The `cuda-arch` metapackage
- Implementing a conda-recipe which depends on `__cuda_arch`
- conda_build_config.yaml
- CUDAARCHS is a CMake-specific environment variable
- Just for illustration, the equivalent args for pytorch would be
- These strings define the corresponding compatible compute capabilities
- We should rank the variants in case multiple variants match a user's machine
- Higher numbers are higher priority
- meta.yaml
- What about arch-specific- and family- instructions sets such as 90a and 120f?

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: What about arch-specific- and family- instructions sets such as 90a and 120f?

> If your program benefits

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 6,178 |
| Shell | 374 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: bandit, conda, coverage, invoke, mypy, mypy-extensions, pre-commit, pytest, pytest-bdd, pytest-benchmark, pytest-cov, pytest-html, pytest-mock, pytest-pikachu, pytest-sugar, pytest-timeout, ruff, safety

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 7
- Forks at capture: 2
- Last updated: 2026-07-21T12:42:47Z
- Last pushed: 2025-11-12T16:33:00Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/nvidia-virtual-packages)
- [README](https://github.com/NVIDIA/nvidia-virtual-packages/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/nvidia-virtual-packages/issues)
- [Releases](https://github.com/NVIDIA/nvidia-virtual-packages/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
