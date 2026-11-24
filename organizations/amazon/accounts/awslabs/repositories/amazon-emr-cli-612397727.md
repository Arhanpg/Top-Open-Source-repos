# awslabs/amazon-emr-cli

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-emr-cli](https://github.com/awslabs/amazon-emr-cli)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/amazon-emr-cli/blob/main/README.md)
- README blob SHA: 068e89451351c48a9b186e1a3cecc724884fde9d
- Repository ID: 612397727
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A command-line interface for packaging, deploying, and running your EMR Serverless Spark jobs

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:36:48+00:00

### Short excerpt (up to 100 words)

> So we're all working on data pipelines every day, but wouldn't be nice to just hit a button and have our code automatically deployed to staging or test accounts? I thought so, too, thats why I created the EMR CLI (`emr`) that can help you package and deploy your EMR jobs so you don't have to. The EMR CLI supports a wide variety of configuration options to adapt to _your_ data pipeline, not the other way around. 1. Packaging - Ensure a consistent approach to packaging your production Spark jobs. 2. Deployment - Easily deploy your Spark jobs across multiple

### README headings

- EMR CLI
- Quick Start
- EMR CLI Sub-commands
- bootstrap
- EMR Serverless
- init
- package
- deploy
- run
- Support PySpark configurations
- Sample Commands
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 76,395 |
| Dockerfile | 2,763 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: boto3, boto3-stubs, click, importlib-metadata, pyfakefs, pytest, pytest-cov, pyyaml, rich
- requirements.txt (capture: captured) — dependency clues: pandas, pyarrow
- src/emr_cli/templates/poetry/pyproject.toml (capture: captured) — dependency clues: pandas, pyarrow, pyspark, pytest
- src/emr_cli/templates/pyspark/Dockerfile (capture: captured)
- src/emr_cli/templates/pyspark/pyproject.toml (capture: captured) — dependency clues: pandas, pyarrow, pytest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 47
- Forks at capture: 14
- Last updated: 2026-06-24T17:39:08Z
- Last pushed: 2026-06-24T17:39:05Z
- Topics: amazon-emr, apache-spark, aws, emr-serverless

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-emr-cli)
- [README](https://github.com/awslabs/amazon-emr-cli/blob/main/README.md)
- [Issues](https://github.com/awslabs/amazon-emr-cli/issues)
- [Releases](https://github.com/awslabs/amazon-emr-cli/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
