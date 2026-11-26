# microsoft/amplifier-browser-bridge

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-browser-bridge](https://github.com/microsoft/amplifier-browser-bridge)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-browser-bridge/blob/main/README.md)
- README blob SHA: 5bfb3630286e40dab0ab6aa726e231b81f1a0a68
- README bytes captured: 65543
- README truncated at capture limit: False
- Repository ID: 1329277466
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Browser Bridge for the Amplifier project

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T02:56:46+00:00

### Short excerpt (up to 300 words)

> If you're already running This software controls a

### README headings

- Amplifier Browser Bridge
- Status
- Security posture
- Quickstart
- Why the setup is this long
- Recommended: install via the Amplifier bundle
- CLI / power-user path
- 1. Install straight from GitHub (public repo, no credentials needed, no local clone
- required). Verified working 2026-08-08 -- see "Verified clean-room install" below.
- Once this package is published to PyPI, `uv tool install amplifier-browser-bridge`
- (no `git+`, no URL) will work too and this collapses to that one command.
- 2. This is the ONLY other command you need to run. From a real terminal it walks
- you through everything else -- installing the hub, then pairing the extension.
- `init` is the one command -- it walks you through the rest
- The "started debugging this browser" banner is the system working
- Where the token lives, and why
- Enabling auth
- Running the hub as a service
- (expected -- no browser was attached in this test; every prior check passed)
- Verified clean-room install
- Verified interactive `init` end-to-end (guided flow, auto-advance)
- Update survives configuration (verified)
- Recovering a connection after reboot
- Connectivity tiers
- Consent model
- Platform support
- Repository layout
- Agent surfaces
- Testing
- Run from the repo root. No venv activation, no manual install step: `pyproject.toml`'s

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Recommended: install via the Amplifier bundle

> If you're already running

### Limitations and security: Security posture

> This software controls a

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,794,306 |
| JavaScript | 400,317 |
| HTML | 30,913 |
| Shell | 26,690 |
| CSS | 7,463 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: aiohttp, click, html2text, mcp, trafilatura, websockets
- extension/package.json (capture: captured)
- modules/tool-browser-bridge/pyproject.toml (capture: captured) — dependency clues: amplifier-browser-bridge
- src/amplifier_browser_bridge/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 2
- Forks at capture: 1
- Last updated: 2026-10-29T21:39:22Z
- Last pushed: 2026-10-29T21:39:20Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-browser-bridge)
- [README](https://github.com/microsoft/amplifier-browser-bridge/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-browser-bridge/issues)
- [Releases](https://github.com/microsoft/amplifier-browser-bridge/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
