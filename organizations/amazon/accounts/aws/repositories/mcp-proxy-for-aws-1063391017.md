# aws/mcp-proxy-for-aws

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/mcp-proxy-for-aws/blob/main/README.md)
- README blob SHA: 48ba4cbc669cd139ca32fc9f362f339e3492f87d
- README bytes captured: 24824
- README truncated at capture limit: False
- Repository ID: 1063391017
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS MCP Proxy Server

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:35:59+00:00

### Short excerpt (up to 300 words)

> The **MCP Proxy for **Use as a proxy Add the following configuration Install Python 3.11+ Install

### README headings

- MCP Proxy for AWS
- Overview
- When Do You Need This Package?
- How This Package Helps
- Which Feature Should I Use?
- Prerequisites
- MCP Proxy
- Installation
- Using PyPi
- Run the server (pinned CLI distribution)
- Using a local repository
- Using Docker
- Pull the latest image
- Or pull a specific version
- Build the Docker image
- Configuration Parameters
- Optional Environment Variables
- Credentials through profile
- Credentials through parameters
- AWS Region
- Multi-profile switching (alternative to --profile flag, useful for plugin integration)
- Multi-account access
- Via CLI flag (first profile is default, rest are switchable)
- Via environment variable (same behavior, for plugin integration)
- Setup Examples
- Running from local - using uv
- Using Docker
- Programmatic Access
- Injecting Metadata
- Integration Patterns

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> The **MCP Proxy for

### Features and capabilities: Which Feature Should I Use?

> **Use as a proxy

### Getting started and usage: Setup Examples

> Add the following configuration

### Technology and requirements: Prerequisites

> Install Python 3.11+ Install

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 445,539 |
| Shell | 3,888 |
| Dockerfile | 1,598 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: boto3, botocore, fastmcp, httpx2
- packages/proxy/pyproject.toml (capture: captured)
- examples/mcp-client/agent-framework/pyproject.toml (capture: captured) — dependency clues: agent-framework, mcp-proxy-for-aws
- examples/mcp-client/langchain/pyproject.toml (capture: captured) — dependency clues: langchain, langchain-aws, langchain-mcp-adapters, mcp-proxy-for-aws, python-dotenv
- examples/mcp-client/llamaindex/pyproject.toml (capture: captured) — dependency clues: llama-index, llama-index-llms-openai, llama-index-tools-mcp, mcp-proxy-for-aws, python-dotenv

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 374
- Forks at capture: 77
- Last updated: 2026-11-23T03:49:24Z
- Last pushed: 2026-11-23T10:13:37Z
- Topics: aws, mcp, proxy, sigv4

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/mcp-proxy-for-aws)
- [README](https://github.com/aws/mcp-proxy-for-aws/blob/main/README.md)
- [Issues](https://github.com/aws/mcp-proxy-for-aws/issues)
- [Releases](https://github.com/aws/mcp-proxy-for-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
