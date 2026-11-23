# aws/agentcore-cli

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/agentcore-cli](https://github.com/aws/agentcore-cli)
- Default branch: v1.x
- README: [Open upstream README](https://github.com/aws/agentcore-cli/blob/v1.x/README.md)
- README blob SHA: 6a3dba7b7ed18a2ef775826699c2d26518c5fc52
- Repository ID: 1142733186
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The terminal experience for AgentCore!

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:26:49+00:00

### Short excerpt (up to 100 words)

> `agentcore` is a command-line tool and interactive terminal UI (TUI) for **Amazon Bedrock AgentCore**, the platform for building and running production AI agents (documentation). It gives you two ways to work, from the same package: - **A scriptable CLI** — flag-driven commands with JSON output (`--json`) for coding agents, scripts, and CI. - **An interactive TUI** — guided flows for creating projects, browsing resources, and chatting with agents. agentcore # launch the interactive TUI agentcore status --json # scriptable, machine-readable output Using the AgentCore APIs directly means calling several services, setting up execution roles, and handling streamed responses. `agentcore` takes

### README headings

- AgentCore CLI
- Installation
- Quick Start
- Projects
- Commands
- Extending the CDK app
- Documentation

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 6,862,166 |
| Python | 134,671 |
| JavaScript | 10,192 |
| Dockerfile | 1,380 |
| Makefile | 617 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- package.json (capture: captured) — dependency clues: @aws-cdk/cloudformation-diff, @aws-cdk/toolkit-lib, @aws-sdk/client-application-signals, @aws-sdk/client-bedrock-agent, @aws-sdk/client-bedrock-agentcore, @aws-sdk/client-bedrock-agentcore-control, @aws-sdk/client-cloudformation, @aws-sdk/client-cloudwatch-logs, @aws-sdk/client-iam, @aws-sdk/client-s3, @aws-sdk/client-sts, @aws-sdk/client-xray, @aws-sdk/util-endpoints, @aws/agent-inspector, @napi-rs/keyring, @opentelemetry/api, @opentelemetry/exporter-metrics-otlp-http, @opentelemetry/otlp-transformer, @opentelemetry/resources, @opentelemetry/sdk-metrics
- .github/harness/Dockerfile (capture: captured)
- src/assets/cdk/package.json (capture: captured) — dependency clues: @aws/agentcore-cdk, @types/node, aws-cdk, aws-cdk-lib, constructs, typescript
- src/assets/evaluators/python-lambda/pyproject.toml (capture: captured) — dependency clues: bedrock-agentcore
- src/assets/templates/a2a-python-strands/pyproject.toml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 337
- Forks at capture: 126
- Last updated: 2026-11-21T10:44:36Z
- Last pushed: 2026-11-23T19:19:36Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/agentcore-cli)
- [README](https://github.com/aws/agentcore-cli/blob/v1.x/README.md)
- [Issues](https://github.com/aws/agentcore-cli/issues)
- [Releases](https://github.com/aws/agentcore-cli/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
