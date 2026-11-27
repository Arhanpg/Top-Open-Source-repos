# awslabs/synthetically_engineered_evaluation_data

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/synthetically_engineered_evaluation_data](https://github.com/awslabs/synthetically_engineered_evaluation_data)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/synthetically_engineered_evaluation_data/blob/main/README.md)
- README blob SHA: 67e482624b7ffd1feb4f96db527f236726b760ac
- README bytes captured: 32108
- README truncated at capture limit: False
- Repository ID: 1296703908
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Create synthetic Document data using Agentic AI

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T20:42:31+00:00

### Short excerpt (up to 300 words)

> Install from PyPI (the The base install is seed-data runs AI agents

### README headings

- Synthetically Engineered Evaluation Data (SEED)
- Quick Start
- Configure AWS credentials with Bedrock access
- Copy the built-in schema library into a local, editable folder
- Generate a single document (PDF + ground-truth JSON) into ./output
- Install (creates the venv and installs from uv.lock)
- Generate a single FCC invoice
- Generate a diverse batch of 4 invoices with augmentation (needs the [augment] extra;
- `uv sync` installs it via the dev group)
- Two ways to use it
- Structured Data Generation
- 1. Plan a schema from anything
- 2. Generate tables from that schema
- ...or generate documents from the very same schema
- Architecture
- Shared front door, two modalities
- Single-document pipeline
- Batch (concurrent fan-out)
- Generic — less diverse
- Specific — much more diverse
- Packet (coordinated multi-document)
- Agent Descriptions
- Setup
- Install uv (see https://docs.astral.sh/uv/getting-started/installation/)
- Create the virtual environment and install all dependencies from uv.lock,
- including the dev group (pytest, ruff, docs). Requires Python 3.12+.
- Run any command inside the managed environment with `uv run`, e.g.
- pip (add the [dev] extra for pytest/ruff/docs tooling)
- or conda for the environment, then pip for the package
- Optional dependencies (extras)

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Quick Start

> Install from PyPI (the

### Technology and requirements: Optional dependencies (extras)

> The base install is

### Limitations and security: Security

> seed-data runs AI agents

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 925,738 |
| Jinja | 41,137 |
| Makefile | 2,253 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: augraphy, boto3, jinja2, mkdocs, mkdocs-awesome-nav, mkdocs-material, mkdocstrings-python, numpy, opencv-python, openpyxl, pandas, pillow, pyarrow, pydantic, pymdown-extensions, pypdf, pypdfium2, pytest, python-dotenv, pyyaml
- docs/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 11
- Forks at capture: 1
- Last updated: 2026-11-11T00:29:34Z
- Last pushed: 2026-11-21T00:05:46Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/synthetically_engineered_evaluation_data)
- [README](https://github.com/awslabs/synthetically_engineered_evaluation_data/blob/main/README.md)
- [Issues](https://github.com/awslabs/synthetically_engineered_evaluation_data/issues)
- [Releases](https://github.com/awslabs/synthetically_engineered_evaluation_data/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
