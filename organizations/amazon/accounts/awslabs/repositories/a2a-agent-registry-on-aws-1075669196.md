# awslabs/a2a-agent-registry-on-aws

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/a2a-agent-registry-on-aws](https://github.com/awslabs/a2a-agent-registry-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/a2a-agent-registry-on-aws/blob/main/README.md)
- README blob SHA: ea9279070de9523ac3469c4a28882b11fef43435
- Repository ID: 1075669196
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Scalable agent registry for AI agents using A2A protocol AgentCard with semantic search. AWS serverless (Lambda, S3 Vectors, Bedrock). Python SDK & React Web UI.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:31:20+00:00

### Short excerpt (up to 100 words)

> The A2A Agent Registry is a **centralized service for registering, discovering, and managing AI agents** in multi-agent systems. It stores AgentCards — the standard metadata format that describes an agent's identity, capabilities, and endpoint. It implements Google's Agent-to-Agent (A2A) protocol to enable seamless agent-to-agent communication and discovery. Build your own **agent marketplace**, **agentic AI platform**, or **LLM agent orchestration layer** with: - **Semantic search** — Find agents using natural language queries (not just keyword matching) - **Skill-based filtering** — Query agents by capabilities using metadata filters - **Serverless architecture** — Pay only for what you use with AWS Lambda and

### README headings

- What is the A2A Agent Registry?
- 🎯 Use Cases
- 🔖 Features
- 🎬 Web UI Demo
- 🏗️ Architecture
- 🚀 Quick Start
- Prerequisites
- Deploy the Agent Registry
- Build the Web UI first (required for deployment)
- Deploy the infrastructure
- Deploy Web UI (Optional)
- Use the Python SDK
- Register an agent
- Search for agents using natural language
- Search by skills
- Combined semantic + skill search
- 🔒 Security Model
- 📚 Documentation
- 💰 Cost Estimate
- ❓ FAQ
- 🤝 Contributing
- 📄 License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 373,804 |
| TypeScript | 165,341 |
| Dockerfile | 2,042 |
| Shell | 1,934 |
| HTML | 600 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- client/pyproject.toml (capture: captured) — dependency clues: a2a-sdk, black, boto3, flake8, isort, moto, mypy, pytest, pytest-cov, pytest-mock, requests, requests-aws4auth
- infrastructure/package.json (capture: captured) — dependency clues: @aws-cdk/aws-lambda-python-alpha, @cdklabs/generative-ai-cdk-constructs, @types/jest, @types/node, aws-cdk, aws-cdk-lib, cdk-nag, constructs, jest, source-map-support, ts-jest, ts-node, typescript
- integration_test/pyproject.toml (capture: captured) — dependency clues: boto3, requests, requests-aws4auth
- lambda/requirements.txt (capture: captured) — dependency clues: a2a-sdk, boto3
- web-ui/Dockerfile (capture: captured)
- web-ui/package.json (capture: captured) — dependency clues: @a2a-js/sdk, @anthropic-ai/sdk, @aws-amplify/auth, @aws-amplify/core, @aws-crypto/sha256-js, @aws-sdk/client-apigatewaymanagementapi, @aws-sdk/credential-providers, @aws-sdk/protocol-http, @aws-sdk/signature-v4, @cloudscape-design/components, @cloudscape-design/global-styles, @testing-library/jest-dom, @testing-library/react, @testing-library/user-event, @types/jest, @types/node, @types/react, @types/react-dom, @typescript-eslint/eslint-plugin, @typescript-eslint/parser

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 30
- Forks at capture: 4
- Last updated: 2026-11-02T09:44:22Z
- Last pushed: 2026-10-19T11:21:58Z
- Topics: a2a-protocol, agent-registry, ai-agents, aws-bedrock, aws-cdk, aws-serverless, multi-agent-systems, python, react, sementic-search

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/a2a-agent-registry-on-aws)
- [README](https://github.com/awslabs/a2a-agent-registry-on-aws/blob/main/README.md)
- [Issues](https://github.com/awslabs/a2a-agent-registry-on-aws/issues)
- [Releases](https://github.com/awslabs/a2a-agent-registry-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
