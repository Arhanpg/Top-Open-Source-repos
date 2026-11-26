# amazon-science/thermal-forge

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/thermal-forge](https://github.com/amazon-science/thermal-forge)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/thermal-forge/blob/main/README.md)
- README blob SHA: 25870fe8eee0705a0999a95a1461369395167b60
- README bytes captured: 18642
- README truncated at capture limit: False
- Repository ID: 1218355666
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:15:47+00:00

### Short excerpt (up to 300 words)

> Requires Python ≥ 3.12. ThermalForge runs a two-phase

### README headings

- ThermalForge
- How It Works
- Installation
- Option 1: conda + pip
- Option 2: venv + pip
- Option 3: uv
- AWS Setup Prerequisites
- AWS Account Setup
- SageMaker Execution Role
- S3 Bucket Creation
- Docker Image
- Configure the Dockerfile (prompts for region and DLC account ID)
- Or specify explicitly (DLC_ACCOUNT is the registry account for your region,
- found at https://docs.aws.amazon.com/sagemaker/latest/dg-ecr-paths/sagemaker-algo-docker-registry-paths.html)
- Authenticate Docker to the DLC ECR registry (use the same DLC_ACCOUNT and REGION from above)
- Build the image
- Authenticate Docker to your account's ECR registry
- Create the repository (first time only)
- Tag and push
- Data
- Data Preparation
- If using pip/conda
- If using uv
- Quick Start
- Local (single home)
- At Scale (SageMaker)
- Launch jobs (config and seed are passed to each training job)
- Evaluating resulting models
- Configuration
- Configuration Priority

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> Requires Python ≥ 3.12.

### Architecture and design: How It Works

> ThermalForge runs a two-phase

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 92,856 |
| Jupyter Notebook | 9,650 |
| Dockerfile | 612 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: boto3, langchain-aws, langgraph, matplotlib, mdextractor, netCDF4, numpy, pandas, pyyaml, sagemaker, scipy, torch, transformers
- docker/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 13
- Forks at capture: 1
- Last updated: 2026-11-14T15:17:45Z
- Last pushed: 2026-09-02T04:00:58Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/thermal-forge)
- [README](https://github.com/amazon-science/thermal-forge/blob/main/README.md)
- [Issues](https://github.com/amazon-science/thermal-forge/issues)
- [Releases](https://github.com/amazon-science/thermal-forge/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
