# NVIDIA/nv-one-logger

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/nv-one-logger](https://github.com/NVIDIA/nv-one-logger)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/nv-one-logger/blob/main/README.md)
- README blob SHA: eccb1cda570286e40fe2fbf5a6db640cc2c54cc1
- README bytes captured: 5073
- README truncated at capture limit: False
- Repository ID: 1000380521
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

nv-one-logger enables tracking of GPU application progress over time and can help to identify overhead from workload and cluster inefficiencies to provide efficiency metrics.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:55:12+00:00

### Short excerpt (up to 300 words)

> No README excerpt captured. Use the upstream README link.

### README headings

- nv-one-logger repo
- Repo Structure
- Project Folder Hierarchy
- Common Project Structure
- Project Descriptions
- one_logger_core
- Projects that facilitate telemetry in a particular domain
- one_logger_training_telemetry
- Projects that facilitate using different telemetry backends
- one_logger_otel
- one_logger_wandb
- Application layer packages
- one_logger_pytorch_lightning_integration
- Dev Guidance

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

No selected README section excerpts were captured.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,032,204 |
| Makefile | 20,550 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- nv_one_logger/one_logger_core/Makefile (capture: captured)
- nv_one_logger/one_logger_core/pyproject.toml (capture: captured) — dependency clues: StrEnum, annotated-types, black, flake8, flake8-bugbear, flake8-docstrings, flake8-pyproject, isort, mypy, mypy-extensions, overrides, pre-commit, pydantic, pytest, pytest-cov, python-semantic-release, toml, typing-extensions
- nv_one_logger/one_logger_otel/Makefile (capture: captured)
- nv_one_logger/one_logger_otel/pyproject.toml (capture: captured) — dependency clues: StrEnum, annotated-types, black, flake8, flake8-bugbear, flake8-docstrings, flake8-pyproject, isort, mypy, mypy-extensions, nv-one-logger-core, opentelemetry-api, opentelemetry-sdk, overrides, pre-commit, pytest, pytest-cov, python-semantic-release, typing-extensions
- nv_one_logger/one_logger_pytorch_lightning_integration/Makefile (capture: captured)
- nv_one_logger/one_logger_pytorch_lightning_integration/pyproject.toml (capture: captured) — dependency clues: StrEnum, annotated-types, black, flake8, flake8-bugbear, flake8-docstrings, flake8-pyproject, isort, lightning, mypy, mypy-extensions, nv-one-logger-core, nv-one-logger-training-telemetry, overrides, pre-commit, pytest, pytest-cov, python-semantic-release, setuptools, torch

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 26
- Forks at capture: 10
- Last updated: 2026-11-05T00:05:22Z
- Last pushed: 2025-11-06T19:36:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/nv-one-logger)
- [README](https://github.com/NVIDIA/nv-one-logger/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/nv-one-logger/issues)
- [Releases](https://github.com/NVIDIA/nv-one-logger/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
