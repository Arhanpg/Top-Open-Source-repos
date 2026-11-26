# NVIDIA/Nvidia-Comms-Perf-Suite

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/Nvidia-Comms-Perf-Suite](https://github.com/NVIDIA/Nvidia-Comms-Perf-Suite)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/Nvidia-Comms-Perf-Suite/blob/main/README.md)
- README blob SHA: 07182acf22c54a17aec17bad57d5be6d9a67bac7
- README bytes captured: 13968
- README truncated at capture limit: False
- Repository ID: 1059593972
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A comprehensive toolkit for GPU Communications Libraries performance testing and data analysis.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:45:11+00:00

### Short excerpt (up to 300 words)

> Nvidia Comms Perf Suite Usage: nvcomms-perf [OPTIONS] COMMAND

### README headings

- Nvidia Comms Perf Suite
- Overview
- Installation
- Virtual Environment (Recommended)
- Create a virtual environment
- Activate the virtual environment
- Build the package with uv
- From the repo root
- Artifacts will be created under dist/
- PostgreSQL URL Format
- Quick Start
- CLI usage
- Workflow
- Step 1: Test Generation
- Generate a job script and print to stdout
- Generate a job script and save to file
- Generate with test report
- Step 2: Run Tests
- Submit the job
- The job will produce test output files (logs, tarballs, etc.)
- Step 3: Process Results
- Option A: Convert to Local File
- Convert a single NCCL test output to a local CSV file
- Convert test results from multiple tarballs to a single local CSV file
- Convert with explicit output format (CSV) and save to local file
- Convert tarball to local CSV file without progress bar
- Convert and stop on first error (instead of continuing)
- Convert using custom number of parallel workers for faster processing
- Option B: Upload to Database/S3
- Upload to PostgreSQL database

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> Nvidia Comms Perf Suite

### Getting started and usage: CLI usage

> Usage: nvcomms-perf [OPTIONS] COMMAND

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 915,281 |
| Jinja | 16,963 |
| Makefile | 2,932 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: boto3, colorlog, hatch, jinja2, marshmallow-dataclass, matplotlib, numpy, openpyxl, orjson, pandas, polars, psycopg, pydantic, pyright, pytest, pytest-cov, pyyaml, requests, rich, ruff
- docs/Makefile (capture: captured)
- examples/example_plugin/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 10
- Forks at capture: 5
- Last updated: 2026-11-01T21:38:42Z
- Last pushed: 2026-11-09T16:07:42Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/Nvidia-Comms-Perf-Suite)
- [README](https://github.com/NVIDIA/Nvidia-Comms-Perf-Suite/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/Nvidia-Comms-Perf-Suite/issues)
- [Releases](https://github.com/NVIDIA/Nvidia-Comms-Perf-Suite/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
