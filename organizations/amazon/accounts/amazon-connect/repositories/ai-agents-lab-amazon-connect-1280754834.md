# amazon-connect/ai-agents-lab-amazon-connect

- Company: Amazon
- GitHub account: [https://github.com/amazon-connect](https://github.com/amazon-connect)
- Mapping status: official-directory-listed
- Repository: [amazon-connect/ai-agents-lab-amazon-connect](https://github.com/amazon-connect/ai-agents-lab-amazon-connect)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-connect/ai-agents-lab-amazon-connect/blob/main/README.md)
- README blob SHA: c54b9843c778b2e787d95d62870ac89109bc6d8b
- Repository ID: 1280754834
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:38:27+00:00

### Short excerpt (up to 100 words)

> A browser-based tool for inspecting Amazon Connect AI agent execution traces, testing agents at scale, and evaluating response quality. No backend — the React SPA calls AWS APIs directly using temporary credentials obtained via IAM Identity Center OIDC. Browse contacts by time range, resolve their Amazon Connect AI Agents sessions, and view the full execution trace as a waterfall timeline. - Parent-child span relationships rendered as a Gantt chart - Color-coded by type: `invoke_agent`, `inference`, `execute_tool` - **Inference spans**: model ID, token usage (input/output/cache read/write), time to first token, temperature, finish reason, system prompt, input/output messages - **Tool spans**: tool

### README headings

- AI Agents Lab for Amazon Connect
- Features
- Span Waterfall Visualisation
- AI Agent Test Harness
- Chat Testing
- Voice Testing (WebRTC)
- YAML Test Script Format
- Batch Variation Generation
- Batch Test Execution
- Evaluations
- Settings
- Workspace Selection
- Prerequisites
- IAM Identity Center Requirement
- Deployment
- Quick Start (full deploy)
- Deploy Parameters
- Deploy Commands
- Examples
- Deploy with IDC in a different region
- Use an existing OIDC client (skip client registration)
- Deployer Permissions
- End-User Permissions
- Core (required)
- Testing — Chat
- Testing — Voice
- Testing — Infrastructure Setup (one-time)
- Batch Test Execution — Variation Generation
- Evaluations
- Permissions Checker

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 990,424 |
| Shell | 5,038 |
| HTML | 381 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-sdk/client-bedrock-runtime, @aws-sdk/client-connect, @aws-sdk/client-connectparticipant, @aws-sdk/client-iam, @aws-sdk/client-lex-models-v2, @aws-sdk/client-polly, @aws-sdk/client-qconnect, @aws-sdk/client-s3, @aws-sdk/client-sso, @aws-sdk/client-sso-oidc, @aws-sdk/client-sts, @aws-sdk/credential-providers, @cloudscape-design/code-view, @cloudscape-design/components, @cloudscape-design/design-tokens, @cloudscape-design/global-styles, @playwright/test, @testing-library/jest-dom, @testing-library/react, @types/react
- infra/package.json (capture: captured) — dependency clues: @types/jest, @types/node, aws-cdk-lib, constructs, jest, ts-jest, ts-node, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 0
- Last updated: 2026-10-28T23:55:01Z
- Last pushed: 2026-10-03T14:58:54Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-connect/ai-agents-lab-amazon-connect)
- [README](https://github.com/amazon-connect/ai-agents-lab-amazon-connect/blob/main/README.md)
- [Issues](https://github.com/amazon-connect/ai-agents-lab-amazon-connect/issues)
- [Releases](https://github.com/amazon-connect/ai-agents-lab-amazon-connect/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
