# Azure/azure-functions-agents-runtime

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/azure-functions-agents-runtime](https://github.com/Azure/azure-functions-agents-runtime)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/azure-functions-agents-runtime/blob/main/README.md)
- README blob SHA: 9995f2fb2533a148df57654a5de9cd5a5bf73870
- README bytes captured: 43800
- README truncated at capture limit: False
- Repository ID: 1220567155
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Agent Runtime for new Event Driven Hosted Skills on the Azure Functions platform

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T19:15:39+00:00

### Short excerpt (up to 300 words)

> **Architecture overview:** see docs/architecture.md The package is published azurefunctions-agents-runtime Connector-backed tools are

### README headings

- azurefunctions-agents-runtime (Preview)
- Installation
- Model Provider Configuration
- Quick Start
- 1. Create the agent file
- 2. Create the function app entry point
- 3. Create `agents.config.yaml`
- Default runtime configuration
- 4. Create `host.json`
- 5. Create `requirements.txt`
- 6. Set the model provider
- 7. Start Azurite (local storage emulator)
- 8. Run locally
- Features
- Built-in endpoints
- Hosted skill bindings
- Agent evaluations (preview)
- Agent configuration
- agents.config.yaml
- Securing endpoints
- Event-driven agents (`<name>.agent.md`)
- Shared capabilities
- Multi-agent delegation (`subagents`)
- Agent File Format (`.agent.md`)
- Optional: system tools (code execution)
- Optional when builtin_endpoints is enabled; required otherwise:
- For HTTP-triggered agents: expected response format
- Multiple functions from markdown
- Trigger type resolution
- HTTP-triggered agents

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Features

> **Architecture overview:** see docs/architecture.md

### Getting started and usage: Installation

> The package is published

### Technology and requirements: 5. Create `requirements.txt`

> azurefunctions-agents-runtime Connector-backed tools are

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 2,784,224 |
| HTML | 98,987 |
| TypeScript | 39,091 |
| JavaScript | 12,365 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: agent-framework-core, agent-framework-foundry, agent-framework-openai, aiohttp, azure-functions, azure-functions-durable, azure-identity, azure-monitor-opentelemetry, azure-storage-blob, azure-storage-queue, azurefunctions-agents-runtime, azurefunctions-extensions-http-fastapi, github-copilot-sdk, jmespath, jsonschema, mcp, mkdocs-material, mypy, pydantic, pytest
- integrations/vally-executor-azure-functions/package.json (capture: captured) — dependency clues: @azure/identity, @microsoft/vally, @microsoft/vally-cli, @types/node, prettier, typescript
- samples/agent-evaluation/src/requirements.txt (capture: captured)
- samples/basic-chat/src/requirements.txt (capture: captured)
- samples/copilot-preview/src/requirements.txt (capture: captured)
- samples/daily-azure-report/src/requirements.txt (capture: captured) — dependency clues: jmespath

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 13
- Forks at capture: 10
- Last updated: 2026-11-03T23:07:57Z
- Last pushed: 2026-11-04T22:55:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/azure-functions-agents-runtime)
- [README](https://github.com/Azure/azure-functions-agents-runtime/blob/main/README.md)
- [Issues](https://github.com/Azure/azure-functions-agents-runtime/issues)
- [Releases](https://github.com/Azure/azure-functions-agents-runtime/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
