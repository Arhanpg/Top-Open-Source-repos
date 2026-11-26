# microsoft/amplifier-bundle-android-tester

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-bundle-android-tester](https://github.com/microsoft/amplifier-bundle-android-tester)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-bundle-android-tester/blob/main/README.md)
- README blob SHA: 0bc9be1be31c3daabb3d61d6fd5691668cd726d7
- README bytes captured: 14293
- README truncated at capture limit: False
- Repository ID: 1325432836
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Android tester bundle for the Amplifier project

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:06:45+00:00

### Short excerpt (up to 300 words)

> Ten checks — host **Add as an app A single android_inspector tool **Start by asking the

### README headings

- amplifier-bundle-android-tester
- Context loading
- The Load-Bearing Rule
- How It Works
- Quick Start
- Installation
- Prerequisites
- report["ready"]   — false if any check failed
- report["checks"]  — [{name, status: ok|warn|fail, detail, remediation}, ...]
- report["summary"] — what to fix first
- Basic Usage
- Boot (applies host workarounds + the two-stage readiness gate)
- Gate on state, never on time
- Coordinates come from the tree — this resolves, taps, re-dumps, reports what changed
- The verified field write: focus assertion + readback
- Screenshot for judgment — never for coordinates
- Agents
- `android-operator` (primary) — `[coding, general]`
- `android-visual-tester` — `[vision, critique, general]`
- `android-debugger` — `[coding, reasoning, general]`
- Tool Operations Reference
- Selector Syntax
- Key Design Decisions
- Why a tool module instead of agent prose
- Why the accessibility tree and not vision
- Why `-no-window` is on by default
- Why setup is a tool call, not a checklist
- Explicitly deferred
- Related Bundles
- Getting Help

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: report["summary"] — what to fix first

> Ten checks — host

### Getting started and usage: Installation

> **Add as an app

### Architecture and design: How It Works

> A single android_inspector tool

### Technology and requirements: Prerequisites

> **Start by asking the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 446,100 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- modules/tool-android-inspector/pyproject.toml (capture: captured) — dependency clues: pytest, pytest-asyncio

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 1
- Forks at capture: 1
- Last updated: 2026-11-06T19:41:57Z
- Last pushed: 2026-11-06T19:41:52Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-bundle-android-tester)
- [README](https://github.com/microsoft/amplifier-bundle-android-tester/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-bundle-android-tester/issues)
- [Releases](https://github.com/microsoft/amplifier-bundle-android-tester/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
