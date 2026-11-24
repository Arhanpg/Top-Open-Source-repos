# NVIDIA/cuEquivariance

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/cuEquivariance](https://github.com/NVIDIA/cuEquivariance)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/cuEquivariance/blob/main/README.md)
- README blob SHA: c2b132aa3d2dfbf9e9063ff17cab3a0a1f737935
- README bytes captured: 2321
- README truncated at capture limit: False
- Repository ID: 876809949
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

cuEquivariance is a math library that is a collective of low-level primitives and tensor ops to accelerate widely-used models, like DiffDock, MACE, Allegro and NEQUIP, based on equivariant neural networks. Also includes kernels for accelerated structure prediction.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T22:00:14+00:00

### Short excerpt (up to 300 words)

> cuEquivariance is an NVIDIA Python library designed to facilitate the construction of high-performance geometric neural networks using segmented polynomials and triangular operations. cuEquivariance provides a

### README headings

- cuEquivariance
- Documentation
- Installation
- Choose the frontend you want to use
- CUDA kernels
- Agent skills
- License
- Disclaimer

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: cuEquivariance

> cuEquivariance is an NVIDIA Python library designed to facilitate the construction of high-performance geometric neural networks using segmented polynomials and triangular operations. cuEquivariance provides a

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,317,247 |
| Standard ML | 20,907 |
| Shell | 3,070 |
| Dockerfile | 648 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- cuequivariance/pyproject.toml (capture: captured) — dependency clues: graphviz, networkx, numpy, opt_einsum, pytest, scipy, sympy
- cuequivariance_jax/pyproject.toml (capture: captured) — dependency clues: cuequivariance, einops, jax, packaging
- cuequivariance_torch/pyproject.toml (capture: captured) — dependency clues: cuequivariance
- docs/requirements.txt (capture: captured) — dependency clues: autodocsumm, e3nn, flax, graphviz, ipykernel, jax, jupyter-sphinx, matplotlib, myst-parser, nvidia-sphinx-theme, sphinx, sphinx-design, torch
- skills/cuequivariance-jax/scripts/requirements.txt (capture: captured) — dependency clues: cuequivariance, cuequivariance-jax, flax, jax
- skills/cuequivariance-torch/scripts/requirements.txt (capture: captured) — dependency clues: cuequivariance, cuequivariance-torch, torch

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 452
- Forks at capture: 52
- Last updated: 2026-11-17T09:31:56Z
- Last pushed: 2026-11-21T01:36:00Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/cuEquivariance)
- [README](https://github.com/NVIDIA/cuEquivariance/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/cuEquivariance/issues)
- [Releases](https://github.com/NVIDIA/cuEquivariance/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
