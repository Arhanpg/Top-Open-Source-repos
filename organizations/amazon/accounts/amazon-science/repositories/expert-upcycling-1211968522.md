# amazon-science/expert-upcycling

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/expert-upcycling](https://github.com/amazon-science/expert-upcycling)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/expert-upcycling/blob/main/README.md)
- README blob SHA: d0dcddf218bb2a2600de9a64f41cd9f6394af581
- README bytes captured: 7571
- README truncated at capture limit: False
- Repository ID: 1211968522
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T23:00:37+00:00

### Short excerpt (up to 300 words)

> pip install -e ".[nemo]" This package treats Megatron-LM

### README headings

- Expert Upcycling
- Installation
- Recommended: NeMo 2.x container
- Inside the container:
- From scratch (no NeMo container)
- Core only (torch + numpy):
- With Megatron-LM integration:
- Full NeMo entrypoint (installs NeMo, Lightning, omegaconf):
- Quick Start
- Option A: NeMo entrypoint (recommended)
- Single GPU
- Multi-GPU (e.g. 8 GPUs with tensor parallelism)
- Option B: Patch existing training script
- Now TEGroupedMLP has .upcycle_experts() and TopKRouter has .upcycle_router()
- Call them during training at the desired transition point.
- Note: model is typically wrapped — unwrap to reach the decoder:
- Option C: Use the model-level API
- Upcycling Strategies
- Expert duplication
- Router expansion
- Architecture
- Running Tests
- CPU tests (no GPU, no Megatron install required)
- GPU test (requires NeMo container + GPU)
- Citation
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Full NeMo entrypoint (installs NeMo, Lightning, omegaconf):

> pip install -e ".[nemo]"

### Architecture and design: Architecture

> This package treats Megatron-LM

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 105,536 |
| Shell | 337 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: dacite, lightning, megatron-core, nemo-toolkit, numpy, omegaconf, pytest, ruff, torch

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 16
- Forks at capture: 2
- Last updated: 2026-09-26T06:59:20Z
- Last pushed: 2026-04-15T23:58:50Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/expert-upcycling)
- [README](https://github.com/amazon-science/expert-upcycling/blob/main/README.md)
- [Issues](https://github.com/amazon-science/expert-upcycling/issues)
- [Releases](https://github.com/amazon-science/expert-upcycling/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
