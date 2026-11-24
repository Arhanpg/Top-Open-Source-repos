# aws/amazon-mwaa-docker-images

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-mwaa-docker-images/blob/main/README.md)
- README blob SHA: 8748339545d023d949239a5372db5ba754c91c6e
- Repository ID: 731811186
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:34:59+00:00

### Short excerpt (up to 100 words)

> This repository contains the Docker Images that [Amazon MWAA](https://aws.amazon.com/managed-workflows-for-apache-airflow/) uses to run Airflow. You can also use it locally if you want to run a MWAA-like environment for testing, experimentation, and development purposes. Currently, Airflow v2.9.2 and above are supported. Future versions in parity with Amazon MWAA will be added as well. _Notice, however, that we do not plan to support previous Airflow versions supported by MWAA._ To experiment with the image using a vanilla Docker setup, follow these steps: 0. _(Prerequisites)_ Ensure you have: - Python 3.11 or later. - Docker and Docker Compose 1. Clone this repository. 2.

### README headings

- aws-mwaa-docker-images
- Overview
- Using the Airflow Image
- Linux / macOS
- Create venvs for all Airflow versions
- Or create venv for a specific version only
- Windows (PowerShell 5.1) [Not supported by AWS MWAA Service Team]
- Prerequisites
- One-time setup
- Create venvs for all Airflow versions
- Or for a specific version only
- Running
- AWS Credentials
- Logging in
- Adding DAGs
- Stopping
- Troubleshooting
- Authentication from version 3.0.1 onward
- Generated Docker Images
- Extra commands
- Requirements
- Package requirements
- Startup script
- Reset database
- Validate DAGs before an Amazon MWAA upgrade
- Build the image once
- Commands
- Exit codes
- Report
- What the check can't catch

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 5,247,557 |
| Shell | 306,569 |
| PowerShell | 134,893 |
| Jinja | 56,828 |
| Dockerfile | 2,402 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: Jinja2, MarkupSafe, diff-cover, nodeenv, pip, psycopg2-binary, pydocstyle, pyright, pytest, pytest-asyncio, pytest-cov, pytest-mock, ruff, setuptools, snowballstemmer, wheel
- images/airflow/2.10.1/requirements.txt (capture: captured) — dependency clues: apache-airflow, apache-airflow-providers-amazon, boto3-stubs, celery, diff-cover, fluent-logger, jinja2, psycopg2, pycurl, pydocstyle, pyright, pytest, pytest-asyncio, pytest-cov, pytest-mock, ruff, sqlalchemy-stubs, watchtower
- images/airflow/2.10.3/requirements.txt (capture: captured) — dependency clues: apache-airflow, apache-airflow-providers-amazon, boto3-stubs, celery, diff-cover, fluent-logger, jinja2, psycopg2, pycurl, pydocstyle, pyright, pytest, pytest-asyncio, pytest-cov, pytest-mock, ruff, sqlalchemy-stubs, watchtower
- images/airflow/2.11.0/requirements.txt (capture: captured) — dependency clues: apache-airflow, apache-airflow-providers-amazon, boto3-stubs, celery, diff-cover, fluent-logger, jinja2, psycopg2, pycurl, pydocstyle, pyright, pytest, pytest-asyncio, pytest-cov, pytest-mock, ruff, sqlalchemy-stubs, watchtower
- images/airflow/2.11.2/requirements.txt (capture: captured) — dependency clues: apache-airflow, apache-airflow-providers-amazon, boto3-stubs, celery, diff-cover, fluent-logger, jinja2, psycopg2, pycurl, pydocstyle, pyright, pytest, pytest-asyncio, pytest-cov, pytest-mock, ruff, sqlalchemy-stubs, watchtower
- images/airflow/2.9.2/requirements.txt (capture: captured) — dependency clues: apache-airflow, apache-airflow-providers-amazon, boto3-stubs, celery, diff-cover, fluent-logger, jinja2, psycopg2, pycurl, pydocstyle, pyright, pytest, pytest-asyncio, pytest-cov, pytest-mock, ruff, sqlalchemy-stubs, watchtower

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 111
- Forks at capture: 74
- Last updated: 2026-11-06T18:54:47Z
- Last pushed: 2026-11-23T02:59:39Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-mwaa-docker-images)
- [README](https://github.com/aws/amazon-mwaa-docker-images/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-mwaa-docker-images/issues)
- [Releases](https://github.com/aws/amazon-mwaa-docker-images/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
