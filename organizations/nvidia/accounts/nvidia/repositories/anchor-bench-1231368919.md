# NVIDIA/anchor-bench

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/anchor-bench](https://github.com/NVIDIA/anchor-bench)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/anchor-bench/blob/main/README.md)
- README blob SHA: 89626457d918befbfa0640435a8d62e3ffcc4292
- Repository ID: 1231368919
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

DevTech - Physical AI: system identification and neural actuator model tuning library for Newton 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:10:54+00:00

### Short excerpt (up to 100 words)

> Anchor Bench is an early-stage, configuration-driven toolkit for robot actuator workflows. It validates a YAML task, runs the corresponding implementation, and writes reproducible artifacts to a dedicated output directory. The current task types are: Anchor Bench also provides a Parquet dataset loader with revision-pinned Hugging Face sources, a Newton USD adapter, and optional run tracking through the bundled MLflow backend. Anchor Bench requires Python 3.10 or newer and uses uv sync Run the included trajectory example: uv run anchor-bench \ --config examples/trajectory/so101_motion_pack.yaml \ --output outputs/so101_motion_pack The command validates the configuration and writes `config.yaml`, `trajectories.parquet`, and a `.completed` marker under the

### README headings

- Anchor Bench
- Quick start
- Documentation
- Python API
- Development

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 649,655 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: GitPython, PyYAML, cmaes, huggingface-hub, mlflow, newton, numpy, optuna, pandas, protobuf, pyarrow, pydantic, pyright, pytest, pytest-cov, ruff, sqlparse, torch, typing-extensions, usd-core

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 13
- Forks at capture: 4
- Last updated: 2026-11-17T03:45:40Z
- Last pushed: 2026-11-20T01:46:12Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/anchor-bench)
- [README](https://github.com/NVIDIA/anchor-bench/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/anchor-bench/issues)
- [Releases](https://github.com/NVIDIA/anchor-bench/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
