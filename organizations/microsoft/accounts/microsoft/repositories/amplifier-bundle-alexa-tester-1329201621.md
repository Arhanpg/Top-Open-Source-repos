# microsoft/amplifier-bundle-alexa-tester

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-bundle-alexa-tester](https://github.com/microsoft/amplifier-bundle-alexa-tester)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-bundle-alexa-tester/blob/main/README.md)
- README blob SHA: a0ca00df56d0d5f13665e02404e794d20c23f023
- README bytes captured: 17046
- README truncated at capture limit: False
- Repository ID: 1329201621
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Test and validate Alexa custom skills — signed envelope generation, response conformance, and routing verification against Amazon's real NLU

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:00:45+00:00

### Short excerpt (up to 300 words)

> Checks cover: endpoint reachability **Add as an app A single alexa_inspector tool **Start by asking the

### README headings

- amplifier-bundle-alexa-tester
- The Load-Bearing Rule
- How It Works
- ⚠️ `live_simulate` Is Implemented, Credential-Gated, and Never Verified End-to-End
- Quick Start
- Installation
- Prerequisites
- report["ready"]    — false if any check failed
- report["checks"]   — [{name, status: ok|warn|fail, message, ...}, ...]
- report["summary"]  — "N checks: N failing, N warning, N ok."
- ca["serve_url"]   — point your endpoint's test-mode trust anchor at this
- ca["cert_url_check"]["passes_real_host_check"]  — ALWAYS false; a local origin
- can never satisfy Amazon's real s3.amazonaws.com requirement, and this is
- reported honestly, not hidden
- Basic Usage
- Direct handler check, no NLU involved at all -- you already know the intent
- Multi-turn dialog with session continuity carried automatically
- dialog["transcript"] -- one entry per turn; sessionAttributes carried forward automatically
- The ONE operation that actually proves Alexa would route an utterance correctly
- sim["note"] confirms this came from real Amazon simulate-skill, not local NLU
- Agents
- `alexa-operator` (primary) — `[coding, general]`
- `alexa-voice-tester` — `[critique, creative, general]`
- `alexa-debugger` — `[coding, reasoning, general]`
- Tool Operations Reference
- Key Design Decisions
- Why a tool module instead of a CLI wrapper
- Why local NLU is marked so aggressively
- Why every limit traces to an explicit citation
- Why `make_test_ca` reports its own host-check failure honestly

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: report["summary"]  — "N checks: N failing, N warning, N ok."

> Checks cover: endpoint reachability

### Getting started and usage: Installation

> **Add as an app

### Architecture and design: How It Works

> A single alexa_inspector tool

### Technology and requirements: Prerequisites

> **Start by asking the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 429,674 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- modules/tool-alexa-inspector/pyproject.toml (capture: captured) — dependency clues: cryptography, pytest, pytest-asyncio

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 1
- Forks at capture: 1
- Last updated: 2026-08-27T10:57:55Z
- Last pushed: 2026-08-09T22:04:45Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-bundle-alexa-tester)
- [README](https://github.com/microsoft/amplifier-bundle-alexa-tester/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-bundle-alexa-tester/issues)
- [Releases](https://github.com/microsoft/amplifier-bundle-alexa-tester/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
