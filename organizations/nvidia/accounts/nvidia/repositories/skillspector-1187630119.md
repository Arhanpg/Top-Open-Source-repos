# NVIDIA/SkillSpector

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/SkillSpector/blob/main/README.md)
- README blob SHA: febba042e0fa81ab905494ea64de9f25161c1d30
- README bytes captured: 76689
- README truncated at capture limit: False
- Repository ID: 1187630119
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills before you install them.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T22:02:39+00:00

### Short excerpt (up to 300 words)

> AI agent skills (used **Multi-format input**: Scan Git Use **Python 3.12 or SkillSpector uses a two-stage export SKILLSPECTOR_PROVIDER=openai export OPENAI_API_KEY="YOUR_GEMINI_API_KEY"

### README headings

- SkillSpector
- Overview
- Documentation
- Features
- Quick Start
- Installation
- To include the optional MCP server:
- Update later: uv tool update skillspector
- Clone the repository
- Create and activate virtual environment
- or: python3.13 -m venv .venv && source .venv/bin/activate
- Install for production use
- Python installation notes
- Docker (no Python required)
- or: docker build -t skillspector .
- Basic Usage
- Scan a local skill directory
- Scan a single SKILL.md file
- Scan a Git repository
- Scan a zip file
- Size limits
- Output Formats
- Terminal output (default) - pretty formatted
- JSON output - machine readable
- Markdown output - for documentation
- SARIF output - for CI/CD integration and IDE tooling
- Recursive Collection Scanning
- Batch Scanning
- Comparing MCP Registry snapshots
- Suppressing False Positives (baseline)

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> AI agent skills (used

### Features and capabilities: Features

> **Multi-format input**: Scan Git

### Getting started and usage: Installation

> Use **Python 3.12 or

### Architecture and design: How It Works

> SkillSpector uses a two-stage

### Limitations and security: Gemini (via OpenAI compatibility layer)

> export SKILLSPECTOR_PROVIDER=openai export OPENAI_API_KEY="YOUR_GEMINI_API_KEY"

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 12,025,930 |
| TypeScript | 62,788 |
| JavaScript | 22,248 |
| YARA | 19,550 |
| Makefile | 5,977 |
| Shell | 2,248 |
| Dockerfile | 596 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- Makefile (capture: captured)
- package.json (capture: captured) — dependency clues: @earendil-works/pi-ai, @earendil-works/pi-coding-agent, typebox
- pyproject.toml (capture: captured) — dependency clues: boto3, build, google-auth, hatchling, httpx, langchain-anthropic, langchain-aws, langchain-core, langchain-openai, langgraph, langgraph-cli, langsmith, mcp, mypy, openai, packaging, poetry, pydantic, pytest, pytest-asyncio

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 27413
- Forks at capture: 2442
- Last updated: 2026-11-23T19:25:09Z
- Last pushed: 2026-11-22T18:53:50Z
- Topics: agent-security, agent-skills, agentic-ai, ai-security, claude-code, mcp, prompt-injection, security-scanner, security-tools, security-workflow, supply-chain-security

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/SkillSpector)
- [README](https://github.com/NVIDIA/SkillSpector/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/SkillSpector/issues)
- [Releases](https://github.com/NVIDIA/SkillSpector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
