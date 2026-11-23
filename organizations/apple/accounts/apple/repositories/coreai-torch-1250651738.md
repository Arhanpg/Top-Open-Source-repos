# apple/coreai-torch

- Company: Apple
- GitHub account: [https://github.com/apple](https://github.com/apple)
- Mapping status: verified
- Repository: [apple/coreai-torch](https://github.com/apple/coreai-torch)
- Default branch: main
- README: [Open upstream README](https://github.com/apple/coreai-torch/blob/main/README.md)
- README blob SHA: c3181488f67eb31a14207199b2baff1c0f62f01c
- Repository ID: 1250651738
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Bridges PyTorch and Core AI. Convert existing models to Core AI IR, or author new ones from PyTorch via composite ops, custom op lowerings, and inline Metal GPU kernels.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:23:51+00:00

### Short excerpt (up to 100 words)

> Core AI PyTorch Extensions (`coreai-torch`) is a Python package that bridges PyTorch and Core AI. Use it to bring up an existing PyTorch model into Core AI IR, or to author Core AI models directly from PyTorch by composing the built-in composite op library (`coreai_torch.composite_ops`), authoring new ops via `register_torch_lowering`, and authoring inline Metal GPU kernels via `TorchMetalKernel`. The resulting IR can be compiled and executed efficiently by the Core AI inference stack. 🔗 Jump to: Getting started · Documentation · Contributing · Support · License `coreai-torch` traverses a `torch.export.ExportedProgram` and produces Core AI IR — the same IR consumed

### README headings

- Core AI PyTorch Extensions (coreai-torch)
- Overview
- Getting started
- Installation
- Usage
- From an ExportedProgram
- Export and decompose — this is your responsibility
- Convert to Core AI IR — the returned program is already optimized
- From an nn.Module
- Documentation
- Building docs locally
- Development
- Setting up pre-commit hooks
- Running tests
- Testing notebooks
- Contributing
- Support
- Security and code of conduct
- License
- Related projects

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 3,150,560 |
| Shell | 14,940 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: coreai-core, coremltools, deptry, filecheck, ghp-import, ml-dtypes, mlx, mlx_lm, myst-nb, nbmake, nbstripout, nest-asyncio, networkx, numpy, packaging, pillow, pre-commit, pytest, pytest-asyncio, pytest-randomly

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: BSD-3-Clause
- Stars at capture: 186
- Forks at capture: 60
- Last updated: 2026-11-20T04:54:06Z
- Last pushed: 2026-11-18T20:57:30Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/apple/coreai-torch)
- [README](https://github.com/apple/coreai-torch/blob/main/README.md)
- [Issues](https://github.com/apple/coreai-torch/issues)
- [Releases](https://github.com/apple/coreai-torch/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
