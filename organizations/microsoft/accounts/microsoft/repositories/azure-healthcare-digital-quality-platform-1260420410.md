# microsoft/azure-healthcare-digital-quality-platform

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/azure-healthcare-digital-quality-platform](https://github.com/microsoft/azure-healthcare-digital-quality-platform)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/azure-healthcare-digital-quality-platform/blob/main/README.md)
- README blob SHA: 05e397c6d8c9b8fdc860bed10587f98c87e69d1b
- README bytes captured: 39189
- README truncated at capture limit: False
- Repository ID: 1260420410
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T21:10:32+00:00

### Short excerpt (up to 300 words)

> 1. Trigger a submitter-side azd auth login azd Five independently deployable stacks, Azure Subscription with Owner Microsoft Entra ID Workload

### README headings

- Azure Healthcare Digital Quality Platform
- Platform Architecture
- Workflow
- Stack Architecture
- Activator Architecture
- Components
- Orchestrator ([`submitters/orchestrator/`](submitters/orchestrator))
- Backend ([`submitters/backend/`](submitters/backend))
- Frontend ([`submitters/frontend/`](submitters/frontend))
- Repository Layout
- Resource Groups
- Buildtime Architecture
- Deployment
- Prerequisites
- Development Tools
- Azure & Container Tools
- Azure Access Requirements
- Quick Start
- Microsoft Entra ID Setup
- 1. Create the App Registration
- 2. Configure SPA Redirect URIs
- 3. Define App Roles
- 4. Assign users in the Enterprise Application
- 5. Wire the frontend `.env`
- 6. Verify
- Submitter → Receiver API Authentication (OAuth 2.0 Client Credentials)
- 1. Register the Receiver API
- 2. Register the Submitter client
- 3. Configure environment variables
- 4. Multi-tenant (cross-tenant) receivers

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: 4. Test DEQM Summary MeasureReport + FHIR bundle exchange

> 1. Trigger a submitter-side

### Getting started and usage: Quick Start

> azd auth login azd

### Architecture and design: Platform Architecture

> Five independently deployable stacks,

### Technology and requirements: Azure Access Requirements

> Azure Subscription with Owner

### Limitations and security: Identity & Security

> Microsoft Entra ID Workload

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,847,567 |
| TypeScript | 1,465,229 |
| Bicep | 907,260 |
| PowerShell | 69,227 |
| Shell | 55,161 |
| HCL | 24,634 |
| CSS | 22,410 |
| CQL | 17,374 |
| Mermaid | 14,455 |
| Dockerfile | 9,252 |
| TSQL | 5,747 |
| JavaScript | 3,435 |
| HTML | 2,745 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- platform/requirements.txt (capture: captured)
- submitters/requirements.txt (capture: captured)
- consumers/backend/Dockerfile (capture: captured)
- consumers/backend/requirements.txt (capture: captured) — dependency clues: PyJWT, aiohttp, azure-cosmos, azure-identity, azure-monitor-opentelemetry, azure-monitor-opentelemetry-exporter, cryptography, fastapi, opentelemetry-api, opentelemetry-instrumentation, opentelemetry-instrumentation-fastapi, opentelemetry-sdk, prompty, pydantic, python-dotenv, requests, uvicorn
- consumers/frontend/Dockerfile (capture: captured)
- consumers/frontend/package.json (capture: captured) — dependency clues: @azure/msal-browser, @azure/msal-react, @headlessui/react, @heroicons/react, @reduxjs/toolkit, @types/react, @types/react-dom, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @vitejs/plugin-react, autoprefixer, axios, clsx, eslint, eslint-plugin-react-hooks, eslint-plugin-react-refresh, postcss, react, react-dom, react-redux

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 5
- Forks at capture: 4
- Last updated: 2026-10-17T13:23:37Z
- Last pushed: 2026-10-15T19:19:52Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/azure-healthcare-digital-quality-platform)
- [README](https://github.com/microsoft/azure-healthcare-digital-quality-platform/blob/main/README.md)
- [Issues](https://github.com/microsoft/azure-healthcare-digital-quality-platform/issues)
- [Releases](https://github.com/microsoft/azure-healthcare-digital-quality-platform/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
