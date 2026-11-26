# microsoft/amplifier-bundle-ios-tester

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-bundle-ios-tester](https://github.com/microsoft/amplifier-bundle-ios-tester)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-bundle-ios-tester/blob/main/README.md)
- README blob SHA: cf402d3f73a0b41da21740a05dacc3a8f157c085
- README bytes captured: 19851
- README truncated at capture limit: False
- Repository ID: 1327207331
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

iOS tester bundle for the Amplifier project

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:44:47+00:00

### Short excerpt (up to 300 words)

> It checks Xcode / **Add as an app A single ios_inspector tool **Start by asking the Enabling Developer Mode on

### README headings

- amplifier-bundle-ios-tester
- Context loading
- The Load-Bearing Rule
- The iOS-Only Trap: Points vs Pixels
- Three Tiers, Honestly Labeled
- What Was Proven, and How
- How It Works
- Quick Start
- Installation
- Prerequisites
- report["ready"]   — false if any check failed
- report["checks"]  — [{name, status: ok|warn|fail, detail, remediation}, ...]
- report["summary"] — what to fix first
- Basic Usage
- Boot — measured 2.7s to Booted, headless, over bare SSH
- Gate on state, never on time — "Booted" is the device, not your app
- Coordinates come from the tree — this resolves, taps, re-dumps, reports what changed
- The verified field write: focus assertion + readback
- Screenshot for judgment — never for coordinates
- Agents
- `ios-operator` (primary) — `[coding, general]`
- `ios-visual-tester` — `[vision, critique, general]`
- `ios-debugger` — `[coding, reasoning, general]`
- Tool Operations Reference
- Selector Syntax
- Key Design Decisions
- Why `ios-tester` and not `iphone-tester`
- Why the accessibility tree and not vision
- Why the tool owns points↔pixels
- Why `axe` and not `idb`

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: report["summary"] — what to fix first

> It checks Xcode /

### Getting started and usage: Installation

> **Add as an app

### Architecture and design: How It Works

> A single ios_inspector tool

### Technology and requirements: Prerequisites

> **Start by asking the

### Limitations and security: A Note on Security Prompts

> Enabling Developer Mode on

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 268,096 |
| Shell | 1,403 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- modules/tool-ios-inspector/pyproject.toml (capture: captured) — dependency clues: pytest, pytest-asyncio

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 1
- Forks at capture: 1
- Last updated: 2026-11-06T19:42:04Z
- Last pushed: 2026-11-06T19:41:58Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-bundle-ios-tester)
- [README](https://github.com/microsoft/amplifier-bundle-ios-tester/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-bundle-ios-tester/issues)
- [Releases](https://github.com/microsoft/amplifier-bundle-ios-tester/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
