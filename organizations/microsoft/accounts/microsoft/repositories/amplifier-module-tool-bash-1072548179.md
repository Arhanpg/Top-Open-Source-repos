# microsoft/amplifier-module-tool-bash

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-module-tool-bash](https://github.com/microsoft/amplifier-module-tool-bash)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-module-tool-bash/blob/main/README.md)
- README blob SHA: 282c5ec5a8be67d468a6258d98bfb9efdc0780d1
- README bytes captured: 18579
- README truncated at capture limit: False
- Repository ID: 1072548179
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Reference implementation for a bash tool module for the Amplifier project

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T06:38:11+00:00

### Short excerpt (up to 300 words)

> Enables agents to execute A host can register **Python 3.11+** **UV** - **IMPORTANT**: Bash execution can

### README headings

- Amplifier Bash Tool Module
- Prerequisites
- Installing UV
- macOS/Linux/WSL
- Windows
- Purpose
- Contract
- Tools Provided
- `bash`
- Configuration
- Optional managed process sessions
- All actions must use the host's ordinary tool dispatcher and approval hooks.
- Safety Profiles
- Available Profiles
- Smart Pattern Matching
- ✅ ALLOWED - "sudo" is in a quoted string, not a command
- ✅ ALLOWED - path contains /dev/ but isn't a device redirect
- ❌ BLOCKED - actual sudo command
- ❌ BLOCKED - actual device redirect
- Overriding Safety Rules
- Allow sudo for container/VM environments
- Allow specific sudo commands only
- Full access for dedicated hardware
- Security
- Usage Example
- Agent uses bash tool
- Dependencies
- Contributing
- Trademarks
- Optional operation observer capability

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Purpose

> Enables agents to execute

### Features and capabilities: Optional operation observer capability

> A host can register

### Technology and requirements: Prerequisites

> **Python 3.11+** **UV** -

### Limitations and security: Security

> **IMPORTANT**: Bash execution can

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 387,200 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: tree-sitter, tree-sitter-bash

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 2
- Forks at capture: 5
- Last updated: 2026-10-22T11:37:08Z
- Last pushed: 2026-10-28T17:05:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-module-tool-bash)
- [README](https://github.com/microsoft/amplifier-module-tool-bash/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-module-tool-bash/issues)
- [Releases](https://github.com/microsoft/amplifier-module-tool-bash/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
