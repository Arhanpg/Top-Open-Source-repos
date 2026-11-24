# SAP-samples/btp-a2a-dispute-resolution

- Company: SAP
- GitHub account: [https://github.com/SAP-samples](https://github.com/SAP-samples)
- Mapping status: official-directory-listed
- Repository: [SAP-samples/btp-a2a-dispute-resolution](https://github.com/SAP-samples/btp-a2a-dispute-resolution)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-samples/btp-a2a-dispute-resolution/blob/main/README.md)
- README blob SHA: 10d0e2a8a6b92a41f764b7cb81e1210c4155d29b
- README bytes captured: 5512
- README truncated at capture limit: False
- Repository ID: 990469771
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repository demonstrates an end-to-end scenario where multiple organizations collaborate through domain-specific agents (discovered via ORD and communicating via A2A) to resolve a customer dispute.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T06:15:03+00:00

### Short excerpt (up to 300 words)

> 1. Provision A2A Agents To run this project, No known issues.

### README headings

- Dispute Resolution with Multi-Agent Orchestration
- Architecture
- Scenario
- Scenario Breakdown
- Prerequisites
- Walkthrough & Hands-on Tutorial
- Repository Structure
- [agent-catalog](/agent-catalog/): Agent discovery and routing services
- [agents](/agents/): A2A agents on SAP, GCP and Azure
- Known Issues
- How to obtain support
- Contributing
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Walkthrough & Hands-on Tutorial

> 1. Provision A2A Agents

### Technology and requirements: Prerequisites

> To run this project,

### Limitations and security: Known Issues

> No known issues.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 38,707 |
| TypeScript | 25,453 |
| CAP CDS | 2,319 |
| Dockerfile | 318 |
| JavaScript | 166 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- agent-catalog/package.json (capture: captured) — dependency clues: @a2a-js/sdk, @cap-js/cds-typer, @cap-js/cds-types, @sap/cds, @types/node, cors, express, prettier, typescript, zod, zod-to-json-schema
- agents/azure-ai-foundry-a2a/requirements.txt (capture: captured) — dependency clues: a2a-sdk, click, httpx, langchain, langchain-core, langchain-openai, langgraph, pydantic, python-dotenv, uvicorn
- agents/gcp-adk-a2a/Dockerfile (capture: captured)
- agents/gcp-adk-a2a/requirements.txt (capture: captured) — dependency clues: a2a-sdk, fastapi, google_adk, uvicorn
- agents/sap-agent-builder-a2a/agent-builder-a2a-agent-connector/package.json (capture: captured) — dependency clues: @a2a-js/sdk, @cap-js/cds-typer, @cap-js/cds-types, @cap-js/ord, @sap/cds, @sap/cds-dk, @types/node, axios, bcrypt, express, prettier, tsx, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 27
- Forks at capture: 7
- Last updated: 2026-06-15T11:50:20Z
- Last pushed: 2026-06-15T11:50:15Z
- Topics: a2a, agent-builder, agents, azure, btp, gcp, genai, llm, ord, sap-cap

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-samples/btp-a2a-dispute-resolution)
- [README](https://github.com/SAP-samples/btp-a2a-dispute-resolution/blob/main/README.md)
- [Issues](https://github.com/SAP-samples/btp-a2a-dispute-resolution/issues)
- [Releases](https://github.com/SAP-samples/btp-a2a-dispute-resolution/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
