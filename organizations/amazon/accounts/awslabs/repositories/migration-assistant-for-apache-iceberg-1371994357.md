# awslabs/migration-assistant-for-apache-iceberg

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/migration-assistant-for-apache-iceberg](https://github.com/awslabs/migration-assistant-for-apache-iceberg)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/migration-assistant-for-apache-iceberg/blob/main/README.md)
- README blob SHA: 1644af60c3881165837b58c2f3bf264660a2c11f
- README bytes captured: 13242
- README truncated at capture limit: False
- Repository ID: 1371994357
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Migration Assistant for converting existing data lake tables into Apache Iceberg lakehouse

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T04:41:54+00:00

### Short excerpt (up to 300 words)

> (cd app/server && uv ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐ AWS CLI v2 configured

### README headings

- Migration Assistant for Apache Iceberg
- Architecture
- How it works
- Conversion Strategies
- Project Structure
- Deploy to AWS
- Prerequisites
- Deployment script
- Optional flag (combine with any build mode above):
- Post-deployment steps (required)
- Quick Start (Local dev)
- Run from IMA_HOME (the repo root)
- Install dependencies
- Start everything
- Estimated Costs
- Infrastructure Costs (Monthly, Steady-State)
- Cost Reduction Options
- Releases
- Contributing
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install dependencies

> (cd app/server && uv

### Architecture and design: Architecture

> ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐

### Technology and requirements: Prerequisites

> AWS CLI v2 configured

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,444,257 |
| TypeScript | 425,264 |
| Shell | 39,956 |
| Dockerfile | 7,733 |
| CSS | 3,115 |
| JavaScript | 726 |
| HTML | 511 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- agent/pyproject.toml (capture: captured) — dependency clues: aws-opentelemetry-distro, bedrock-agentcore, boto3, botocore, fastavro, strands-agents
- app/Dockerfile (capture: captured)
- docs/requirements.txt (capture: captured) — dependency clues: mkdocs, mkdocs-material, pymdown-extensions
- engine/Dockerfile (capture: captured)
- engine/pyproject.toml (capture: captured) — dependency clues: boto3, fastapi, httpx, psycopg2-binary, pyarrow, pyiceberg, pytest, sqlglot, uvicorn
- app/client/package.json (capture: captured) — dependency clues: @eslint/js, @hookform/resolvers, @tailwindcss/vite, @tanstack/react-query, @tanstack/react-router, @types/node, @types/react, @types/react-dom, @vitejs/plugin-react, class-variance-authority, clsx, eslint, eslint-plugin-react-hooks, eslint-plugin-react-refresh, globals, i18next, lucide-react, react, react-dom, react-hook-form

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 0
- Last updated: 2026-11-22T21:24:16Z
- Last pushed: 2026-11-22T21:21:46Z
- Topics: aws, aws-analytics, iceberg, s3tables

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/migration-assistant-for-apache-iceberg)
- [README](https://github.com/awslabs/migration-assistant-for-apache-iceberg/blob/main/README.md)
- [Issues](https://github.com/awslabs/migration-assistant-for-apache-iceberg/issues)
- [Releases](https://github.com/awslabs/migration-assistant-for-apache-iceberg/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
