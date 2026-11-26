# NVIDIA/nvalchemi-toolkit

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/nvalchemi-toolkit](https://github.com/NVIDIA/nvalchemi-toolkit)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/nvalchemi-toolkit/blob/main/README.md)
- README blob SHA: a0c0075ccc780beaf77ecebe54f7d094f837f0dd
- README bytes captured: 11382
- README truncated at capture limit: False
- Repository ID: 1167966684
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ALCHEMI Toolkit is a developer toolkit for accelerating training and inference for AI in chemistry and material science.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:05:11+00:00

### Short excerpt (up to 300 words)

> **Batched GPU simulation**: run The quickest way to

### README headings

- NVIDIA ALCHEMI Toolkit
- High-throughput AI atomic simulation on NVIDIA GPUs
- Key Features
- Using with AI coding agents
- Example Snippets
- Create two molecules
- Batch for GPU-efficient inference
- Wrap a model and run
- Dynamics reads and writes these per-step buffers, so allocate them up front.
- + fuses stages: one forward pass, masked updates per sub-stage
- Launch with: torchrun --nproc_per_node=2 my_pipeline.py
- | distributes stages: one dynamics per GPU rank
- Assumes `model` is a BaseModelMixin wrapper and `train_loader` /
- `val_loader` are nvalchemi DataLoaders (see the data pipeline guide).
- Compose an objective: weighted energy + force terms
- Launch with: torchrun --nproc_per_node=2 my_dd_run.py
- The wrapper and the integrator are the same objects you would use on a
- single GPU; `batch` is the full system, built on rank 0 only.
- One DomainConfig + one wrap is the entire user-facing addition. Atoms are
- partitioned spatially; halo exchange and cross-rank reductions are automatic.
- Installation
- Roadmap
- Contributions & Disclaimers
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Key Features

> **Batched GPU simulation**: run

### Getting started and usage: Installation

> The quickest way to

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 13,444,453 |
| Standard ML | 15,021 |
| Shell | 12,219 |
| Makefile | 7,976 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: aimnet, ase, click, cuequivariance-ops-torch-cu12, cuequivariance-ops-torch-cu13, cuequivariance-torch, fairchem-core, jaxtyping, loguru, mace-torch, numpy, nvalchemi-toolkit-ops, nvidia-physicsnemo, periodictable, plotext, plum-dispatch, pydantic, pymatgen, rdkit, rich
- docs/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 244
- Forks at capture: 51
- Last updated: 2026-11-18T23:24:17Z
- Last pushed: 2026-11-23T18:33:54Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/nvalchemi-toolkit)
- [README](https://github.com/NVIDIA/nvalchemi-toolkit/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/nvalchemi-toolkit/issues)
- [Releases](https://github.com/NVIDIA/nvalchemi-toolkit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
