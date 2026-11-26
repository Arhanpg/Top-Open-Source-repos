# microsoft/amplifier-bundle-shadow

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-bundle-shadow](https://github.com/microsoft/amplifier-bundle-shadow)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-bundle-shadow/blob/main/README.md)
- README blob SHA: bf54bf8864d0445b7a64ec350a7de698a33d73d7
- README bytes captured: 12815
- README truncated at capture limit: False
- Repository ID: 1129345869
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Shadow environment bundle for the Amplifier project

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:22:47+00:00

### Short excerpt (up to 300 words)

> Amplifier Shadow creates isolated **Exact Working Tree Snapshots**: uv tool install git+https://github.com/microsoft/amplifier-bundle-shadow Shadow environments use a **Container Runtime (required):**

### README headings

- Amplifier Shadow
- Overview
- Key Features
- Installation
- Install from source
- Or for development
- Prerequisites
- Docker
- Or Podman (preferred - rootless by default)
- Quick Start
- Create a shadow with your local library changes
- Inside the shadow, install via git URL
- -> my-library uses YOUR LOCAL snapshot
- -> all other dependencies fetch from REAL GitHub
- Run tests
- See what changed
- Open an interactive shell
- Clean up when done
- How It Works
- Architecture
- Exact Working Tree Snapshots
- Selective Git URL Rewriting
- CLI Commands
- Create Options
- Common Patterns
- Test a Single Library
- Testing your library with its dependents
- Clone and test inside shadow
- Test Multi-Repo Changes
- Testing changes across multiple repos

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> Amplifier Shadow creates isolated

### Features and capabilities: Key Features

> **Exact Working Tree Snapshots**:

### Getting started and usage: Install from source

> uv tool install git+https://github.com/microsoft/amplifier-bundle-shadow

### Architecture and design: Architecture

> Shadow environments use a

### Technology and requirements: Prerequisites

> **Container Runtime (required):**

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 252,586 |
| Dockerfile | 6,334 |
| Shell | 3,545 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: click, pytest, pytest-asyncio, rich
- container/Dockerfile (capture: captured)
- modules/tool-shadow/pyproject.toml (capture: captured)
- src/amplifier_bundle_shadow/container/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 2
- Forks at capture: 3
- Last updated: 2026-08-27T10:58:21Z
- Last pushed: 2026-03-04T16:35:13Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-bundle-shadow)
- [README](https://github.com/microsoft/amplifier-bundle-shadow/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-bundle-shadow/issues)
- [Releases](https://github.com/microsoft/amplifier-bundle-shadow/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
