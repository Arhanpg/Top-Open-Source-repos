# rapidsai/velox-testing

- Company: NVIDIA
- GitHub account: [https://github.com/rapidsai](https://github.com/rapidsai)
- Mapping status: official-project-linked
- Repository: [rapidsai/velox-testing](https://github.com/rapidsai/velox-testing)
- Default branch: main
- README: [Open upstream README](https://github.com/rapidsai/velox-testing/blob/main/README.md)
- README blob SHA: fa08b9987ae0739bba1ca71502976cc7c40fb6f7
- README bytes captured: 22567
- README truncated at capture limit: False
- Repository ID: 1024489913
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T21:38:02+00:00

### Short excerpt (up to 300 words)

> sccache has been integrated When --sccache is passed, The benchmarking infrastructure requires

### README headings

- velox-testing
- CI/CD Workflows
- Velox Testing
- `sccache` Usage
- Setup
- Velox Builds with sccache
- Default: Remote S3 cache + local compilation (recommended)
- Optional: Enable distributed compilation (may cause build differences such as additional warnings)
- Pin a specific sccache version
- Presto Builds with sccache
- GPU native build with sccache
- CPU native build with sccache
- Pin a specific sccache version
- Enable distributed compilation (use with caution)
- How it Works
- Velox Benchmarking
- Prerequisites
- Building for Benchmarks
- Running Benchmarks
- Basic Examples:
- Run all TPC-H queries on both CPU and GPU (using defaults)
- Run TPC-H Q6 on CPU only
- Run TPC-H Q1 and Q6 on both CPU and GPU
- Run TPC-H Q6 on GPU with profiling enabled
- Custom output directory for results
- Run TPC-H Q6 with 5 repetitions
- Use custom data directory
- Results
- Presto Testing
- Running Integration Tests

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: `sccache` Usage

> sccache has been integrated

### Architecture and design: How it Works

> When --sccache is passed,

### Technology and requirements: Prerequisites

> The benchmarking infrastructure requires

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 433,489 |
| Python | 361,593 |
| Dockerfile | 31,839 |
| Jinja | 7,967 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)
- .devcontainer/Dockerfile (capture: captured)
- benchmark_data_tools/requirements.txt (capture: captured) — dependency clues: certifi, charset-normalizer, click, duckdb, httpx, idna, presto-python-client, psutil, pyarrow, pytest, requests, six, urllib3
- benchmark_reporting_tools/requirements.txt (capture: captured) — dependency clues: httpx
- template_rendering/requirements.txt (capture: captured) — dependency clues: Jinja2
- presto/testing/requirements.txt (capture: captured) — dependency clues: Pygments, certifi, charset-normalizer, click, duckdb, idna, iniconfig, packaging, pandas, pluggy, presto-python-client, pyarrow, pytest, requests, simple-term-menu, six, sqlglot, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 13
- Forks at capture: 31
- Last updated: 2026-10-15T19:23:39Z
- Last pushed: 2026-11-20T15:14:00Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/rapidsai/velox-testing)
- [README](https://github.com/rapidsai/velox-testing/blob/main/README.md)
- [Issues](https://github.com/rapidsai/velox-testing/issues)
- [Releases](https://github.com/rapidsai/velox-testing/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
