# microsoft/amplifier-bundle-dot-runner

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-bundle-dot-runner](https://github.com/microsoft/amplifier-bundle-dot-runner)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-bundle-dot-runner/blob/main/README.md)
- README blob SHA: 8dce5b9e6a96e9fcb72d6aafbd5d74988b183e9f
- README bytes captured: 34037
- README truncated at capture limit: False
- Repository ID: 1348025655
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Dot Runner bundle for the Amplifier project

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:32:48+00:00

### Short excerpt (up to 300 words)

> **The attractor command is

### README headings

- amplifier-bundle-dot-runner
- Public agent binding migration
- 0.2.0 -- repair release (breaking changes)
- What's here
- This is a proper bundle
- Who consumes this
- Spec fidelity
- History
- Breaking changes (0.3.0)
- Getting started
- Pattern (a) — root one-liner (recommended)
- Pattern (b) — pip-install a module directly (git + subdirectory, pinned)
- One CLI -- default worker: amplifier-agent (unconditional), `direct` (broken-env fallback only)
- amplifier-agent is always installed at the root: every box node is hosted
- by microsoft/amplifier-agent's Engine, no flags needed
- explicit choice always wins
- Library seam: `run_pipeline()` / `resume_pipeline()` get the SAME default-worker story (fix/library-seam-default-worker)
- Bare call: resolves to amplifier-agent (spawn + real tool loop),
- exactly like `dot-runner run pipeline.dot` with no --worker flag.
- Fails loud (raises `default_worker.WorkerResolutionError`) if that
- install is broken -- never silently falls back to a text-only worker.
- Explicit choice always wins -- same three names as `--worker`, and the
- bare, text-only loop remains fully available, deliberately, by asking
- for it:
- Subscription providers: `github-copilot` / `openai-chatgpt` (spawn workers only)
- github-copilot: set a GitHub token that carries intent (any one of these)
- openai-chatgpt: authenticate once via the provider module's own device-code
- flow, which writes ~/.amplifier/openai-chatgpt-oauth.json
- Dependency conflict fix: amplifier-foundation SHAPE mismatch (resolved)
- The library-seam / module-dist coupling: which install a bare `run_pipeline()` needs (fix/library-seam-default-worker)

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Getting started

> **The attractor command is

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 5,844,014 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: amplifier-module-loop-agent, amplifier-module-loop-amplifier-agent, amplifier-module-pipeline-runner
- modules/hooks-pipeline-observability/pyproject.toml (capture: captured) — dependency clues: amplifier-core
- modules/hooks-pipeline-progress/pyproject.toml (capture: captured) — dependency clues: amplifier-core
- modules/hooks-tool-truncation/pyproject.toml (capture: captured) — dependency clues: amplifier-core
- modules/loop-agent/pyproject.toml (capture: captured) — dependency clues: amplifier-core, amplifier-unified-llm-client
- modules/loop-amplifier-agent/pyproject.toml (capture: captured) — dependency clues: amplifier-agent, amplifier-core

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 2
- Forks at capture: 2
- Last updated: 2026-11-04T04:04:30Z
- Last pushed: 2026-11-19T22:34:57Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-bundle-dot-runner)
- [README](https://github.com/microsoft/amplifier-bundle-dot-runner/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-bundle-dot-runner/issues)
- [Releases](https://github.com/microsoft/amplifier-bundle-dot-runner/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
