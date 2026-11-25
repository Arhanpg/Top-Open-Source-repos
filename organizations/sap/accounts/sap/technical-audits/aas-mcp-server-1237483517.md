# SAP/aas-mcp-server

- Company: SAP
- Account: SAP
- Repository: https://github.com/SAP/aas-mcp-server
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T23:05:46+00:00

## Project purpose

> OpenAPI-to-MCP bridge for Asset Administration Shell (AAS) APIs

## Why this project is used

An AAS MCP adapter that exposes configured Asset Administration Shell APIs as Model Context Protocol tools, enabling LLM agents to interact with any AAS-compliant backend.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Shell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: cryptography, fastmcp, httpx2, mcp, oas-patch, py-key-value-aio, pyyaml
- Build/package tools: Docker build configuration, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/aas_mcp_server/cli.py, src/aas_mcp_server/server.py, src/aas_mcp_server/__init__.py, src/aas_mcp_server/audit.py

## Setup and usage

- Docker Usage: The pre-built image is published to GitHub Container Registry at
- Docker Usage: ghcr.io/sap/aas-mcp-server (multi-arch linux/amd64 + linux/arm64, SBOM
- Docker Usage: and build-provenance attested). The examples below use :latest; pin to a
- Docker Usage: specific version (:0.1.0) or minor line (:0.1) for reproducible deployments.

## Limitations and caveats

- Security / Disclosure: - **Read-only by default** - Write operations disabled unless --enable-writes
- Security / Disclosure: - **Allowlist-based** - Only explicitly allowed operations exposed
- Security / Disclosure: - **Wildcard patterns** - [get, "*"], ["*", /path], ["*", "*"]
- Security / Disclosure: - **Pagination limits** - Max 100 items per request
- Security / Disclosure: If you find any bug that may be a security problem, please follow our instructions at in our security policy on how to report it. Please do not create GitHub issues for security-related doubts or problems.

## Evidence and provenance

- README: https://github.com/SAP/aas-mcp-server/blob/main/README.md
- README SHA: 7019a9976e6e14c05efd11d0bdf71acfdb79bf5c
- Manifests: Dockerfile, pyproject.toml
- Sampled source files: src/aas_mcp_server/cli.py, src/aas_mcp_server/server.py, src/aas_mcp_server/__init__.py, src/aas_mcp_server/audit.py
- Git tree state: captured
- Evidence fingerprint: ff86d4dcbb30fc2b6bb6b9771e4c2425a7be5ceb0d19829b59b6a6a58c4b2a85

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
