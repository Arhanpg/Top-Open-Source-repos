# microsoft/amplifier-module-provider-vllm

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-module-provider-vllm](https://github.com/microsoft/amplifier-module-provider-vllm)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-module-provider-vllm/blob/main/README.md)
- README blob SHA: 3ae05c500323203663411aabb7484e961123411c
- README bytes captured: 26347
- README truncated at capture limit: False
- Repository ID: 1101815472
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Reference implementation of a vLLM provider module for the Amplifier project

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T06:34:35+00:00

### Short excerpt (up to 300 words)

> This provider module integrates **For GPT-OSS models**: Token This provider uses the

### README headings

- amplifier-module-provider-vllm
- Overview
- Installation
- Via uv (recommended)
- For development
- vLLM Server Setup
- Start vLLM server (basic)
- For production (recommended - full config in /etc/vllm/model.env)
- Configuration
- Model listing
- Minimal Configuration
- Full Configuration
- Image inputs (endpoint-dependent)
- Stream idle timeout
- Context limits
- Truncation
- Local vs remote — single source of truth
- Mixed local + remote (multi-instance)
- Default LOCAL instance — keeps the natural mount name "vllm"
- Second instance — explicit `instance_id` makes it addressable as "vllm-remote"
- Usage Examples
- Basic Chat
- With Reasoning
- With Tool Calling
- Architecture
- Responses API Details
- Debugging
- Find recent session
- View raw requests
- View raw responses

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> This provider module integrates

### Getting started and usage: Token usage shows zeros

> **For GPT-OSS models**: Token

### Architecture and design: Architecture

> This provider uses the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 464,391 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: openai, openai-harmony

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 6
- Forks at capture: 8
- Last updated: 2026-11-07T04:51:02Z
- Last pushed: 2026-11-21T14:22:46Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-module-provider-vllm)
- [README](https://github.com/microsoft/amplifier-module-provider-vllm/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-module-provider-vllm/issues)
- [Releases](https://github.com/microsoft/amplifier-module-provider-vllm/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
