# microsoft/amplifier-eval-harness

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-eval-harness](https://github.com/microsoft/amplifier-eval-harness)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-eval-harness/blob/main/README.md)
- README blob SHA: e3148236259dee9d43195b6c9786561f45a67193
- README bytes captured: 10238
- README truncated at capture limit: False
- Repository ID: 1232063212
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Eval harness for exploring configuration of amplifier-app-cli for the Amplifier project

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:34:47+00:00

### Short excerpt (up to 300 words)

> uv tool install --from 1. Read config → **No token / cost

### README headings

- amplifier-eval-harness
- Status
- Quick start
- Prerequisites:
- - amplifier CLI installed (uv tool install git+https://github.com/microsoft/amplifier)
- - amplifier-bundle-gitea (provides amplifier-gitea CLI)
- - amplifier-bundle-digital-twin-universe v0.2.0+ (provides amplifier-digital-twin CLI).
- v0.1.x silently ignores `default_match_mode: boundary`; URL prefix collisions
- with sibling repos can over-match. PR #7 (merged 2026-05-05) fixes it.
- - Docker running (for Gitea container) + Incus (for DTU containers)
- - At least one provider env var set (ANTHROPIC_API_KEY, OPENAI_API_KEY, GOOGLE_API_KEY, GITHUB_TOKEN…)
- Install
- Sanity check (no DTU launches)
- Smoke run (1 bundle × 1 scenario × 1 run, sequential)
- Baseline (foundation + amplifier-dev × 3 runs each, up to 2 in parallel)
- Override parallelism at the CLI without editing the config
- Dry run (just expand and print the matrix)
- Configs
- Scenarios
- Settings overlays
- Gitea instance pinning
- {"id": "gitea-abcd1234", "port": 10111, ...}
- Pin via env var (per-invocation, no config edit required)
- Or pin in the config itself
- Running inside a nested Incus DTU
- Find the harness DTU's eth0 IP (run this inside the DTU):
- e.g. 10.119.176.124
- Set before running the harness:
- Architecture in 60 seconds
- Parallelism

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install

> uv tool install --from

### Architecture and design: Architecture in 60 seconds

> 1. Read config →

### Limitations and security: Limitations (v0.2)

> **No token / cost

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 189,089 |
| Go Template | 6,901 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: click, pyyaml, rich

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 1
- Forks at capture: 1
- Last updated: 2026-08-27T10:58:40Z
- Last pushed: 2026-10-15T03:16:59Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-eval-harness)
- [README](https://github.com/microsoft/amplifier-eval-harness/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-eval-harness/issues)
- [Releases](https://github.com/microsoft/amplifier-eval-harness/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
