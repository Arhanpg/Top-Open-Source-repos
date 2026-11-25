# SAP/leanix-self-built-software-agent

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/leanix-self-built-software-agent](https://github.com/SAP/leanix-self-built-software-agent)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/leanix-self-built-software-agent/blob/main/README.md)
- README blob SHA: f19d94afdd0071cf9244460545874faa1ab4e732
- README bytes captured: 10084
- README truncated at capture limit: False
- Repository ID: 1145181889
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This is an automated software discovery system that uses AI agents to analyze GitHub repositories and identify self-built software running in production environments. Core Purpose The project aims to discover and catalog self-built software without human intervention by: Automatically analyzing GitHub repositories in an organization Classifying ...

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T00:27:53+00:00

### Short excerpt (up to 300 words)

> A CLI tool and Generates comprehensive software catalogs curl -LsSf https://astral.sh/uv/install.sh | The tool automatically looks Backend: Python FastAPI, Go If you find any

### README headings

- SAP LeanIX Self Built Software Agent
- About this project
- Table of Contents
- Introduction
- Features
- Installation
- Recommended
- Install uv package manager
- Clone and setup
- Homebrew
- Install uv
- Clone and setup
- Python Version
- Getting Started
- Configuration
- Edit .env with your API keys and credentials
- Required Variables
- Or for PostgreSQL:
- export DATABASE_URL="postgresql://user:password@localhost:5432/database"
- Discover Repositories
- Discover all repositories in an organization
- Discover a single repository
- Use a specific LLM model
- Dry run without saving to database
- Save results to JSON file
- Limit number of repositories
- User-Provided Context
- How It Works
- Example Usage
- Auto-detect context files from standard locations

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: About this project

> A CLI tool and

### Features and capabilities: Features

> Generates comprehensive software catalogs

### Getting started and usage: Install uv package manager

> curl -LsSf https://astral.sh/uv/install.sh |

### Architecture and design: How It Works

> The tool automatically looks

### Technology and requirements: Tech Stack

> Backend: Python FastAPI, Go

### Limitations and security: Security / Disclosure

> If you find any

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 308,646 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: asyncpg, click, databases, dotenv, init-llm, langchain, langchain-anthropic, langchain-community, langchain-openai, langgraph, mypy, psycopg2-binary, pygithub, requests, rich, ruff, sap-ai-sdk-gen, sqlalchemy, structlog

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9
- Forks at capture: 3
- Last updated: 2026-09-23T15:42:37Z
- Last pushed: 2026-05-28T08:23:40Z
- Topics: ai, gen-ai, llm, python, sap-ai-core

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/leanix-self-built-software-agent)
- [README](https://github.com/SAP/leanix-self-built-software-agent/blob/main/README.md)
- [Issues](https://github.com/SAP/leanix-self-built-software-agent/issues)
- [Releases](https://github.com/SAP/leanix-self-built-software-agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
