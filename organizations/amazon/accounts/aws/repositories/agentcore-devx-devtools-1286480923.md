# aws/agentcore-devx-devtools

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/agentcore-devx-devtools](https://github.com/aws/agentcore-devx-devtools)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/agentcore-devx-devtools/blob/main/README.md)
- README blob SHA: c4dacd10bd0a62771ed7664819c64a2e4ff2ca84
- Repository ID: 1286480923
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:26:51+00:00

### Short excerpt (up to 100 words)

> Shared developer tools for the AgentCore repositories: agentcore-cli, bedrock-agentcore-sdk-python, bedrock-agentcore-sdk-typescript. This repo is the home for all reusable GitHub Actions workflows and composite actions. The `.github/workflows/` directory contains reusable workflows. Each is invoked via `workflow_call` from a caller workflow in a consuming repo. `reusable-pr-ai-review.yml` centralizes AgentCore Harness review mechanics while callers retain their event triggers and repository-specific prompts. `workflow-metrics.yml` emits `WorkflowRunDuration` for a completed `workflow_run`, with `WorkflowName`, `Branch`, `Result`, and `OS` dimensions. Callers provide the namespace, OS, and writer-role secret name, grant `id-token: write`, and pass `WORKFLOW_SECRETS_READER_ROLE_ARN`. Pin the workflow to a full commit SHA. The writer role needs `cloudwatch:PutMetricData`.

### README headings

- AgentCore DevX DevTools
- Reusable workflows
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Unknown | Not captured |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 5
- Forks at capture: 3
- Last updated: 2026-11-11T18:20:50Z
- Last pushed: 2026-11-23T19:14:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/agentcore-devx-devtools)
- [README](https://github.com/aws/agentcore-devx-devtools/blob/main/README.md)
- [Issues](https://github.com/aws/agentcore-devx-devtools/issues)
- [Releases](https://github.com/aws/agentcore-devx-devtools/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
