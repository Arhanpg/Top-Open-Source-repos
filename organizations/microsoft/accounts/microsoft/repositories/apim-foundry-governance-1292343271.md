# microsoft/apim-foundry-governance

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/apim-foundry-governance](https://github.com/microsoft/apim-foundry-governance)
- Default branch: english
- README: [Open upstream README](https://github.com/microsoft/apim-foundry-governance/blob/english/README.md)
- README blob SHA: f115862d5b04db8b2b9c4423ad4b5ce7679232a6
- README bytes captured: 13944
- README truncated at capture limit: False
- Repository ID: 1292343271
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Azure AI Gateway client and governance reference

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T20:43:51+00:00

### Short excerpt (up to 300 words)

> **APIM (VNet-injected)** is the An **Azure subscription** with Backends: private endpoints +

### README headings

- Azure AI Gateway
- What it provides
- Demo
- How it works
- Repository layout
- `scripts/` file descriptions
- Prerequisites
- Deployment
- 1. Bootstrap the Terraform state backend (once per subscription)
- 2. Set variables
- Edit infra/terraform.tfvars: prefix, location, owner, cost_center, apim_publisher_*, budget_*.
- Set apim_public = true before the first apply if the APIM gateway must be internet reachable.
- 3. First apply — the gateway core
- If you are moving an existing state from another backend, run `terraform init -migrate-state` instead.
- 4. Build + push the container images
- 5. Second apply — enable the worker + Admin UI
- 6. Seed configuration (from inside the VNet)
- Global allowed models + limits
- Per-model pricing (for cost-based budgeting)
- 7. Use it
- VS Code BYOK example
- Copilot CLI BYOK example
- Cost & cleanup
- Security model

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: How it works

> **APIM (VNet-injected)** is the

### Technology and requirements: Prerequisites

> An **Azure subscription** with

### Limitations and security: Security model

> Backends: private endpoints +

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 139,570 |
| Python | 123,660 |
| TypeScript | 61,848 |
| Shell | 15,290 |
| PowerShell | 2,341 |
| Dockerfile | 928 |
| HTML | 304 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- app/admin-ui/Dockerfile (capture: captured)
- app/config-sync-worker/Dockerfile (capture: captured)
- app/config-sync-worker/requirements.txt (capture: captured) — dependency clues: azure-cosmos, azure-identity, azure-mgmt-apimanagement, azure-monitor-query
- app/admin-ui/bff/requirements.txt (capture: captured) — dependency clues: azure-cosmos, azure-identity, azure-mgmt-apimanagement, azure-monitor-query, fastapi, httpx, pyjwt, uvicorn
- app/admin-ui/spa/package.json (capture: captured) — dependency clues: @azure/msal-browser, @azure/msal-react, @fluentui/react-components, @fluentui/react-icons, @types/react, @types/react-dom, @vitejs/plugin-react, react, react-dom, react-router-dom, typescript, vite

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 4
- Forks at capture: 2
- Last updated: 2026-11-14T05:45:57Z
- Last pushed: 2026-10-18T14:36:18Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/apim-foundry-governance)
- [README](https://github.com/microsoft/apim-foundry-governance/blob/english/README.md)
- [Issues](https://github.com/microsoft/apim-foundry-governance/issues)
- [Releases](https://github.com/microsoft/apim-foundry-governance/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
