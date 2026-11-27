# awslabs/runner-dbt-aws-airflow

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/runner-dbt-aws-airflow](https://github.com/awslabs/runner-dbt-aws-airflow)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/runner-dbt-aws-airflow/blob/main/README.md)
- README blob SHA: fe612620966b88c6806dc4818462c2a49ee7d591
- README bytes captured: 19014
- README truncated at capture limit: False
- Repository ID: 1334444854
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Run dbt projects on AWS Glue (Spark Job, Interactive Session, Python Shell) and EMR (Serverless, on-EC2) from Apache Airflow. Declarative YAML routing, task-collapse, OpenLineage.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T18:44:55+00:00

### Short excerpt (up to 300 words)

> **Five runner shapes** — End-to-end setup, no library-specific An AWS account with If you discover a

### README headings

- runner-dbt-aws-airflow
- Table of Contents
- Why runner-dbt-aws-airflow
- Install (PyPI)
- Latest release
- With Airflow + dev extras
- With OpenLineage emission
- Quickstart — MWAA 3.2.1 + Glue Spark
- 1. Prerequisites
- 2. Sample dbt project
- 3. `runners.yml`
- runners.yml -- runner-dbt-aws-airflow config
- 4. Airflow DAG
- 1. Build + upload the project archive at DAG-parse time. Content-
- fingerprinted -- re-uploads only when files change.
- 2. Load the runner config once.
- 3. Build the DAG. ``config=cfg`` auto-wires every routing field.
- 5. MWAA `requirements.txt`
- 6. Deploy to MWAA
- Sync DAGs + config to MWAA's S3 bucket
- Update MWAA to pick up the new requirements
- Features
- Documentation
- Repo layout
- Development
- Install everything (creates .venv with dev + docs + runtime deps)
- Lint + type-check
- Build the wheel
- Run all commit-time hooks
- Status

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Features

> **Five runner shapes** —

### Getting started and usage: Quickstart — MWAA 3.2.1 + Glue Spark

> End-to-end setup, no library-specific

### Technology and requirements: 1. Prerequisites

> An AWS account with

### Limitations and security: Security

> If you discover a

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 634,710 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: apache-airflow, apache-airflow-providers-amazon, apache-airflow-providers-standard, boto3, openlineage-dbt, openlineage-python, pyyaml

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3
- Forks at capture: 0
- Last updated: 2026-09-25T09:27:31Z
- Last pushed: 2026-11-13T20:32:32Z
- Topics: airflow, apache-airflow, aws, aws-emr, aws-glue, data-engineering, dbt, dbt-core, mwaa, openlineage

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/runner-dbt-aws-airflow)
- [README](https://github.com/awslabs/runner-dbt-aws-airflow/blob/main/README.md)
- [Issues](https://github.com/awslabs/runner-dbt-aws-airflow/issues)
- [Releases](https://github.com/awslabs/runner-dbt-aws-airflow/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
