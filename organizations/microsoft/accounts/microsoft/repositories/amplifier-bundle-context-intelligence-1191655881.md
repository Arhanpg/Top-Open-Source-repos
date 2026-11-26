# microsoft/amplifier-bundle-context-intelligence

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-bundle-context-intelligence](https://github.com/microsoft/amplifier-bundle-context-intelligence)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-bundle-context-intelligence/blob/main/README.md)
- README blob SHA: 0aad2d001e47c71c89d65b04504f7ccab2fbb7dd
- README bytes captured: 88840
- README truncated at capture limit: False
- Repository ID: 1191655881
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Context Intelligence bundle for the Amplifier project

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:18:48+00:00

### Short excerpt (up to 300 words)

> Two agents are included **Add to an existing Activate with /context-intelligence (or

### README headings

- amplifier-bundle-context-intelligence
- What it does
- Transcript recall
- Composition — pick the layer you need
- Understanding workspace
- How workspace appears in data
- Resolution priority
- Quick Start
- 1. Install
- 2. (Optional) Forward events to one or more servers
- ~/.amplifier/keys.env  — secrets only, never commit
- ~/.amplifier/settings.yaml
- 3. Verify
- events.jsonl  metadata.json
- Exploration guide
- Troubleshooting
- Configuring via the Amplifier app-cli
- The override pattern
- Embedding in an Amplifier application
- Sending application events without mounting a hook
- Persist this exact envelope in your outbox before dispatching, if needed.
- Mounting the telemetry hook
- Minimal — JSONL only
- ... session runs ...
- Full config dict
- Workspace via coordinator.config
- Accessing resolved values
- Configuration reference
- Server forwarding — `destinations`
- ~/.amplifier/settings.yaml — route different projects to different servers

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: What it does

> Two agents are included

### Getting started and usage: 1. Install

> **Add to an existing

### Architecture and design: Context Intelligence Design Mode

> Activate with /context-intelligence (or

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 3,307,188 |
| Shell | 40,428 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: azure-identity, httpx
- modules/hook-context-intelligence/pyproject.toml (capture: captured) — dependency clues: amplifier-bundle-context-intelligence, httpx, idna, pathspec
- modules/hook-server-data-ops-lockdown/pyproject.toml (capture: captured)
- modules/tool-context-intelligence-prune/pyproject.toml (capture: captured) — dependency clues: PyYAML, amplifier-bundle-context-intelligence, click
- modules/tool-context-intelligence-query/pyproject.toml (capture: captured) — dependency clues: amplifier-bundle-context-intelligence, httpx, idna
- modules/tool-context-intelligence-recover/pyproject.toml (capture: captured) — dependency clues: amplifier-bundle-context-intelligence, amplifier-module-hook-context-intelligence, httpx, pyyaml

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 5
- Forks at capture: 7
- Last updated: 2026-11-06T20:52:27Z
- Last pushed: 2026-11-23T18:24:10Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-bundle-context-intelligence)
- [README](https://github.com/microsoft/amplifier-bundle-context-intelligence/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-bundle-context-intelligence/issues)
- [Releases](https://github.com/microsoft/amplifier-bundle-context-intelligence/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
