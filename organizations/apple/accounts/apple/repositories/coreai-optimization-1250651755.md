# apple/coreai-optimization

- Company: Apple
- GitHub account: [https://github.com/apple](https://github.com/apple)
- Mapping status: verified
- Repository: [apple/coreai-optimization](https://github.com/apple/coreai-optimization)
- Default branch: main
- README: [Open upstream README](https://github.com/apple/coreai-optimization/blob/main/README.md)
- README blob SHA: a53e266cb6ca4fd3ab4799d05655e61f3c72730c
- Repository ID: 1250651755
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A library for PyTorch model compression and optimizations for deployment via Core AI on Apple silicon.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:23:49+00:00

### Short excerpt (up to 100 words)

> `coreai-opt` provides implementations of popular model optimizations such as quantization, palettization (codebook-based compression), and pruning, for PyTorch models, customized for deployment on Apple Silicon via Core AI. Jump to: Getting Started · Documentation · Contributing · Support · License · Related projects Install the latest release from PyPI: pip install coreai-opt Or with uv: uv pip install coreai-opt A wheel built from the latest `main` is published to PyPI every night as `coreai-opt-nightly`. It provides the same `coreai_opt` package, so install it in place of `coreai-opt`: pip install --upgrade coreai-opt-nightly uv pip install --upgrade coreai-opt-nightly This project uses uv for

### README headings

- Core AI Optimization
- Getting started
- Installation
- Nightly builds
- pip
- uv
- From source
- Usage
- A simple model and example input.
- Apply INT8 weight-only quantization using a built-in preset.
- Finalize for Core AI export.
- Documentation
- Contributing
- Support
- License
- Related projects

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 3,507,268 |
| Shell | 53,368 |
| Makefile | 20,418 |
| C++ | 11,343 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: coreai-core, coreai-torch, coremltools, flash-kmeans, ninja, numpy, packaging, pydantic, pyyaml, rich, safetensors, scikit-learn, setuptools, torch, torchao, tqdm

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: BSD-3-Clause
- Stars at capture: 160
- Forks at capture: 52
- Last updated: 2026-11-18T12:52:40Z
- Last pushed: 2026-11-20T21:56:42Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/apple/coreai-optimization)
- [README](https://github.com/apple/coreai-optimization/blob/main/README.md)
- [Issues](https://github.com/apple/coreai-optimization/issues)
- [Releases](https://github.com/apple/coreai-optimization/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
