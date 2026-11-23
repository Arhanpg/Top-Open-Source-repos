# awslabs/ai-eval-studio

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/ai-eval-studio](https://github.com/awslabs/ai-eval-studio)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/ai-eval-studio/blob/main/README.md)
- README blob SHA: ef719ed5207d2c1c254e597876fe098bc32bc2b0
- Repository ID: 1435220921
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:02:49+00:00

### Short excerpt (up to 100 words)

> An end-to-end LLM evaluation platform. Upload a dataset, describe your goal in chat, and the system runs evaluations across models, optimizes the prompt iteratively against real failures, and hands you back a standalone Python eval harness you can run in CI. Every model call — the agent driving the conversation, the models under test, and the LLM judge — runs on Amazon Bedrock. You talk to a coordinator agent, which walks the project through seven phases: The generated harness is the durable artifact: a self-contained Python project that runs without the platform. See The platform runs in two modes from

### README headings

- AI Eval Studio
- What it does
- Architecture
- Running locally
- Deploying to AWS
- Security scope
- Tests and checks
- Repository layout
- Documentation
- License
- Claude Code
- Reporting a security issue

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 6,165,587 |
| TypeScript | 1,263,466 |
| Shell | 48,497 |
| CSS | 9,865 |
| Dockerfile | 7,877 |
| JavaScript | 6,816 |
| HTML | 366 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- backend/Dockerfile (capture: captured)
- backend/pyproject.toml (capture: captured) — dependency clues: boto3, botocore, certifi, claude-agent-sdk, deepeval, fastapi, httpx, openpyxl, pandas, pyjwt, python-multipart, uvicorn
- frontend/package.json (capture: captured) — dependency clues: @assistant-ui/react, @assistant-ui/react-markdown, @assistant-ui/react-syntax-highlighter, @base-ui/react, @eslint/js, @fontsource-variable/fira-code, @fontsource-variable/geist, @fontsource-variable/inter, @fontsource-variable/jetbrains-mono, @fontsource-variable/oxanium, @fontsource-variable/plus-jakarta-sans, @fontsource/architects-daughter, @monaco-editor/react, @tailwindcss/vite, @tanstack/react-table, @testing-library/jest-dom, @testing-library/react, @types/node, @types/plotly.js, @types/react
- infra/requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, aws-cdk.aws-servicecatalogappregistry-alpha, constructs
- backend/app/templates/harness/pyproject.toml (capture: captured) — dependency clues: awscrt, boto3, certifi, deepeval, httpx, pandas, pytest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 561
- Forks at capture: 5
- Last updated: 2026-11-23T17:25:56Z
- Last pushed: 2026-11-05T04:53:17Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/ai-eval-studio)
- [README](https://github.com/awslabs/ai-eval-studio/blob/main/README.md)
- [Issues](https://github.com/awslabs/ai-eval-studio/issues)
- [Releases](https://github.com/awslabs/ai-eval-studio/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
