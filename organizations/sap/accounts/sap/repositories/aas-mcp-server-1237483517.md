# SAP/aas-mcp-server

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/aas-mcp-server](https://github.com/SAP/aas-mcp-server)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/aas-mcp-server/blob/main/README.md)
- README blob SHA: a5f1645d21cbf958e4b3daf32d232a9b99a2492c
- Repository ID: 1237483517
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An AAS MCP adapter that exposes configured Asset Administration Shell APIs as Model Context Protocol tools, enabling LLM agents to interact with any AAS-compliant backend.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:25:57+00:00

### Short excerpt (up to 100 words)

> An AAS MCP adapter that exposes configured Asset Administration Shell APIs as Model Context Protocol tools, enabling LLM agents to interact with any AAS-compliant backend. 1. **AAS OpenAPI Specifications** - the IDTA Part 2 API specs from the git tags of admin-shell-io/aas-specs-api, bundled into one file per API (needs git, perl and Node.js for `npx`) 2. **AAS Backend Server** - SAP BNAC AAS Server, Eclipse BaSyx, FA³ST Service, etc. 3. **Python 3.12+** OR **Docker** 1. **Get AAS Specifications**: TAG=v3.2.0 SPEC=AssetAdministrationShellRepositoryServiceSpecification/V3.2_SSP-001.yaml git clone -q --depth 1 --branch "$TAG" \ https://github.com/admin-shell-io/aas-specs-api "aas-specs-api-$TAG" find "aas-specs-api-$TAG" -name '*.yaml' -exec perl -pi -e \ 's#https://api\.swaggerhub\.com/domains/Plattform_i40/(Part1-MetaModel-Schemas|Part2-API-Schemas)/V[0-9.]+#../$1/openapi.yaml#g'

### README headings

- AAS MCP Server
- About this project
- Requirements and Setup
- Prerequisites
- Setup
- Configuration
- Basic (Official Spec Only)
- Filtered (Implementation-Specific)
- With Curation (Wildcards Supported)
- MCP Client Configuration
- Claude Desktop
- Claude CLI (Claude Code)
- OpenCode
- Docker Usage
- Basic (stdio — local use, no auth)
- HTTP Transport with OAuth 2.1
- Custom Config Path
- Outbound AAS Request Headers
- Forward selected inbound HTTP headers
- Claude Code HTTP client with a user subscription key
- OAuth 2.1 Authorization
- Environment variables
- How it works
- Audit Logging
- OpenTelemetry Tracing
- Supported Components
- Testing
- Unit tests only
- With integration tests (requires backend on port 8081)
- Support, Feedback, Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 497,509 |
| Shell | 19,599 |
| Dockerfile | 1,704 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: asyncpg, cryptography, fastmcp, httpx2, mcp, oas-patch, opentelemetry-exporter-otlp-proto-http, opentelemetry-sdk, py-key-value-aio, pyyaml, redis

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9
- Forks at capture: 7
- Last updated: 2026-11-11T09:14:17Z
- Last pushed: 2026-11-23T07:46:11Z
- Topics: aas, ai-agent, asset-administration-shell, digital-twin, idta, industry-4-0, llm, mcp, model-context-protocol, openapi, python, sap-bnac

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/aas-mcp-server)
- [README](https://github.com/SAP/aas-mcp-server/blob/main/README.md)
- [Issues](https://github.com/SAP/aas-mcp-server/issues)
- [Releases](https://github.com/SAP/aas-mcp-server/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
