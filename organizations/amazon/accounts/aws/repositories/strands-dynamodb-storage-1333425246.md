# aws/strands-dynamodb-storage

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/strands-dynamodb-storage](https://github.com/aws/strands-dynamodb-storage)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/strands-dynamodb-storage/blob/main/README.md)
- README blob SHA: 06b0100d20b8e0704bbb8da9039ed8f314fd6da0
- README bytes captured: 20530
- README truncated at capture limit: False
- Repository ID: 1333425246
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon DynamoDB storage backend for the Strands Agents SDK (TypeScript and Python): sessions, agent memory, semantic search over DynamoDB vector indexes, and S3 offload behind one Storage interface.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T06:24:47+00:00

### Short excerpt (up to 300 words)

> &nbsp;&nbsp;&nbsp; Strands DynamoDB Storage Both languages ship the Create a table with See CONTRIBUTING for more

### README headings

- Why DynamoDB for agent storage
- Quick Start
- One store for the whole agent
- One backend for the whole agent — subsystems without their own storage inherit it.
- Long-term memory
- Python
- Persist the agent's session to DynamoDB — nothing else to wire.
- TypeScript
- Examples
- Provisioning and permissions
- Features
- Releases
- Development
- Contributing ❤️
- License
- Security

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> &nbsp;&nbsp;&nbsp; Strands DynamoDB Storage

### Features and capabilities: Features

> Both languages ship the

### Getting started and usage: Quick Start

> Create a table with

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 256,168 |
| Python | 237,021 |
| JavaScript | 803 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- python/pyproject.toml (capture: captured) — dependency clues: boto3, moto, mypy, pytest, pytest-asyncio, pytest-cov, ruff, strands-agents
- typescript/package.json (capture: captured) — dependency clues: @aws-sdk/client-bedrock-runtime, @aws-sdk/client-dynamodb, @aws-sdk/client-s3, @aws-sdk/client-sts, @aws-sdk/lib-dynamodb, @aws-sdk/util-dynamodb, @eslint/js, @strands-agents/sdk, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @vitest/coverage-v8, eslint, globals, prettier, typescript, vitest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 18
- Forks at capture: 5
- Last updated: 2026-11-21T16:25:40Z
- Last pushed: 2026-11-19T16:29:22Z
- Topics: agent-memory, ai-agents, amazon-dynamodb, aws, python, semantic-search, storage, strands-agents, typescript, vector-search

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/strands-dynamodb-storage)
- [README](https://github.com/aws/strands-dynamodb-storage/blob/main/README.md)
- [Issues](https://github.com/aws/strands-dynamodb-storage/issues)
- [Releases](https://github.com/aws/strands-dynamodb-storage/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
