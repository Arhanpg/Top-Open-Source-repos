# microsoft/amplifier-app-wiki-weaver

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-app-wiki-weaver](https://github.com/microsoft/amplifier-app-wiki-weaver)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-app-wiki-weaver/blob/main/README.md)
- README blob SHA: 1dbc9fd4d6919dd09222895b941c589a6d217a6b
- README bytes captured: 20349
- README truncated at capture limit: False
- Repository ID: 1274820014
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Wiki Weaver LLM-WIKI bundle for the Amplifier project

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T22:42:10+00:00

### Short excerpt (up to 300 words)

> wiki-weaver init mywiki \ Install the wiki-weaver command Code-first, with agents where Python 3.11+ An Amplifier

### README headings

- Wiki-Weaver
- The idea
- Quick start
- Keeping wiki-weaver current
- Check for drift (ls-remote each @main source; no changes made):
- Apply updates:
- Layer 1 — reinstall wiki-weaver + wheel deps (amplifier-foundation, unified-llm-client)
- Layer 2 — re-clone engine bundles in ~/.amplifier/cache/bundles
- Confirm what you're running after update:
- 0. Preflight — verifies the runtime, provider key, network, and validator are all present.
- 1. Create a wiki and design a schema for YOUR purpose (one LLM call, ~30–60s).
- The --purpose text should describe the intended use and the outcomes you want.
- 2. Drop source material (markdown/plain text) into the wiki's inbox.
- 3. Weave the sources in. Re-run any time you add more to _inbox/ — it picks up where
- it left off (already-ingested sources are deduped by content hash).
- 4. Ask questions — answered by reading the compiled wiki, with citations.
- 5. Structurally validate the wiki (exit 0 = PASS).
- Commands
- Ingest exit codes + result.json (headless callers)
- Corpus structure
- Migrating an existing corpus
- Dashboard
- Theming
- Three ways to use it
- ... drop sources into mywiki/_inbox/ ...
- Sharing / publishing your wiki
- Architecture
- Configuration
- Requirements
- Contributing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: The --purpose text should describe the intended use and the outcomes you want.

> wiki-weaver init mywiki \

### Getting started and usage: Quick start

> Install the wiki-weaver command

### Architecture and design: Architecture

> Code-first, with agents where

### Technology and requirements: Requirements

> Python 3.11+ An Amplifier

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,542,719 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: amplifier-dot-runner, amplifier-foundation, amplifier-unified-llm-client, markdown, tinycss2
- modules/hook-run-events/pyproject.toml (capture: captured)
- modules/tool-wiki-weaver/pyproject.toml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 2
- Forks at capture: 2
- Last updated: 2026-10-29T21:42:34Z
- Last pushed: 2026-11-11T10:22:16Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-app-wiki-weaver)
- [README](https://github.com/microsoft/amplifier-app-wiki-weaver/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-app-wiki-weaver/issues)
- [Releases](https://github.com/microsoft/amplifier-app-wiki-weaver/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
