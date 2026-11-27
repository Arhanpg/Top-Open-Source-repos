# GoogleCloudPlatform/hcls-mcp-servers

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/hcls-mcp-servers](https://github.com/GoogleCloudPlatform/hcls-mcp-servers)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/hcls-mcp-servers/blob/main/README.md)
- README blob SHA: 116f9223a41d9b2c3289f92e969abe94ad6b27ae
- README bytes captured: 18830
- README truncated at capture limit: False
- Repository ID: 1260429035
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T18:38:31+00:00

### Short excerpt (up to 300 words)

> These MCP servers act **IAP support**: Optional Identity-Aware **Prerequisites:** Python 3.10+ Each The servers are designed gcloud CLI installed and The deploy pipeline supports

### README headings

- Google Cloud Healthcare MCP Servers
- Table of Contents
- Overview & Use Cases
- Architecture
- Servers Catalog
- Quick Start (Local)
- Cloud Run Deployment
- Prerequisites
- First-Time Setup
- Continuous Deployment
- Adding a New Server or Modifying Defaults
- Teardown
- Security & Authentication
- Concurrent Public & Private Deployments
- Additional Security Features
- Managing Cloud Run Logs
- Connecting Clients
- Public Mode (`auth_mode=public`)
- IAM Mode (`auth_mode=iam`, Default)
- Example for Antigravity: Add to your mcp_config.json
- Example for Gemini CLI:
- Local Development
- Connect your client to http://localhost:8080/mcp
- Testing
- Test locally (starts each server, runs checks, stops it)
- Test deployed Cloud Run services
- Include UMLS tests (requires free API key from https://uts.nlm.nih.gov/)
- Compliance & Support
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview & Use Cases

> These MCP servers act

### Features and capabilities: Additional Security Features

> **IAP support**: Optional Identity-Aware

### Getting started and usage: Quick Start (Local)

> **Prerequisites:** Python 3.10+ Each

### Architecture and design: Architecture

> The servers are designed

### Technology and requirements: Prerequisites

> gcloud CLI installed and

### Limitations and security: Security & Authentication

> The deploy pipeline supports

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 456,870 |
| Shell | 14,117 |
| HCL | 11,642 |
| Dockerfile | 2,381 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- clinical_trials_mcp/Dockerfile (capture: captured)
- clinical_trials_mcp/requirements.txt (capture: captured) — dependency clues: cachetools, httpx, mcp, pydantic, starlette, uvicorn
- cms_coverage_mcp/Dockerfile (capture: captured)
- cms_coverage_mcp/requirements.txt (capture: captured) — dependency clues: cachetools, httpx, mcp, pydantic, starlette, uvicorn
- drug_data_mcp/Dockerfile (capture: captured)
- drug_data_mcp/requirements.txt (capture: captured) — dependency clues: cachetools, httpx, mcp, pydantic, starlette, uvicorn

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 8
- Forks at capture: 4
- Last updated: 2026-10-23T02:36:34Z
- Last pushed: 2026-07-22T19:08:45Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/hcls-mcp-servers)
- [README](https://github.com/GoogleCloudPlatform/hcls-mcp-servers/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/hcls-mcp-servers/issues)
- [Releases](https://github.com/GoogleCloudPlatform/hcls-mcp-servers/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
