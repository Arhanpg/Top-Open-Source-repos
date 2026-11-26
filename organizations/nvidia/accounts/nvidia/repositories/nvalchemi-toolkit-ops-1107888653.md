# NVIDIA/nvalchemi-toolkit-ops

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/nvalchemi-toolkit-ops](https://github.com/NVIDIA/nvalchemi-toolkit-ops)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/nvalchemi-toolkit-ops/blob/main/README.md)
- README blob SHA: 640c566476c46e802518fd15135f14a633fb8426
- README bytes captured: 8699
- README truncated at capture limit: False
- Repository ID: 1107888653
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ALCHEMI Toolkit-Ops is a collection of optimized batch kernels to accelerate computational chemistry and material science workflows.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:07:11+00:00

### Short excerpt (up to 300 words)

> **Neighbor lists** Naive, cell-list, uv venv --seed --python

### README headings

- NVIDIA ALCHEMI Toolkit-Ops
- High-performance NVIDIA Warp primitives for computational chemistry
- Key Features
- Use Cases
- Example Snippets
- distribute positions inside the cell
- use padded matrix representation for neighbors, optimal for
- compiled applications that need constant shapes
- ...or pass `return_neighbor_list=True` for the familiar COO
- `edge_index` format. `method` will also automatically determine
- neighbor algorithm based off system size
- the following parameters need to be constructed ahead of time
- construct neighbor matrix
- DFT-D3 parameters need to be provided, which comprises reference C6 parameters.
- Refer to the user documentation to see the expected structure and data source.
- pass everything to the functional interface
- the following parameters need to be constructed ahead of time
- construct neighbor matrix
- call PME, using automatic parameter tuning
- CUDA 13 Support
- Standalone install
- Explicit CUDA 13 PyTorch wheel index
- Contributions & Disclaimers

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Key Features

> **Neighbor lists** Naive, cell-list,

### Getting started and usage: Standalone install

> uv venv --seed --python

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 18,801,736 |
| Shell | 47,798 |
| Makefile | 22,038 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: jax, numpy, torch, warp-lang
- docs/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 255
- Forks at capture: 42
- Last updated: 2026-11-23T14:15:53Z
- Last pushed: 2026-11-23T18:33:25Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/nvalchemi-toolkit-ops)
- [README](https://github.com/NVIDIA/nvalchemi-toolkit-ops/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/nvalchemi-toolkit-ops/issues)
- [Releases](https://github.com/NVIDIA/nvalchemi-toolkit-ops/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
