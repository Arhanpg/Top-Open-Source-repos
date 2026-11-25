# SAP/langgraph-checkpoint-sap-agent-memory-service

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/langgraph-checkpoint-sap-agent-memory-service](https://github.com/SAP/langgraph-checkpoint-sap-agent-memory-service)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/langgraph-checkpoint-sap-agent-memory-service/blob/main/README.md)
- README blob SHA: 6d59aca62cd627d980dc7f33267650c3c65cf597
- README bytes captured: 14314
- README truncated at capture limit: False
- Repository ID: 1425773633
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A free, open-source LangGraph's checkpoint saver that uses SAP Agent Memory Service. It enables state persistence backed by SAP Agent Memory Service for durable, long-running workflows and agents.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T00:16:29+00:00

### Short excerpt (up to 300 words)

> This library provides an pip install langgraph-checkpoint-sap-agent-memory-service # Python ≥ 3.10 A If you find any

### README headings

- LangGraph checkpointers for SAP Agent Memory Service
- About this project
- Requirements and Setup
- Installation
- Quick start
- Option 1 — XSUAA (OAuth2 client credentials)
- First run — checkpoints are saved automatically at each node boundary
- Resume after a crash — same thread_id restores the latest checkpoint
- Option 2 — IAS (Bearer token)
- No ias_access_token in config needed — the default is used automatically
- The callable is invoked automatically; no ias_access_token needed in config
- Common usage patterns
- Crash recovery
- Run 1 — crashes after node_2
- Run 2 — resumes from node_3, skips node_1 and node_2
- Human-in-the-loop (HITL)
- Pause — graph.invoke raises NodeInterrupt
- Resume with human input
- Deleting a thread
- IAS saver — pass the Bearer token (or rely on a default source)
- XSUAA saver — pass tenant_id to route to a subscriber tenant (optional)
- Async
- Token refresh
- XSUAA token refresh
- IAS token refresh
- Sync callable
- Async callable
- State history
- All checkpoints for a thread, newest first
- Subgraph support

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: About this project

> This library provides an

### Getting started and usage: Installation

> pip install langgraph-checkpoint-sap-agent-memory-service #

### Technology and requirements: Requirements and Setup

> Python ≥ 3.10 A

### Limitations and security: Security / Disclosure

> If you find any

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 165,070 |
| Makefile | 379 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: httpx, langgraph-checkpoint, langgraph-checkpoint-conformance, pytest, pytest-asyncio, respx, ruff, ty, urllib3, uuid6

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-11-10T04:34:32Z
- Last pushed: 2026-11-23T05:12:07Z
- Topics: hana-cloud, langchain, langchain-python, langgraph

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/langgraph-checkpoint-sap-agent-memory-service)
- [README](https://github.com/SAP/langgraph-checkpoint-sap-agent-memory-service/blob/main/README.md)
- [Issues](https://github.com/SAP/langgraph-checkpoint-sap-agent-memory-service/issues)
- [Releases](https://github.com/SAP/langgraph-checkpoint-sap-agent-memory-service/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
