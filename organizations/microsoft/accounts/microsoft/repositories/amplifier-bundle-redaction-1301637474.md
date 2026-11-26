# microsoft/amplifier-bundle-redaction

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-bundle-redaction](https://github.com/microsoft/amplifier-bundle-redaction)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-bundle-redaction/blob/main/README.md)
- README blob SHA: 907e7570ec1809a27f4bef304f932f57448ee128
- README bytes captured: 14674
- README truncated at capture limit: False
- Repository ID: 1301637474
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amplifier bundle with redaction library and redaction hook

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:16:47+00:00

### Short excerpt (up to 300 words)

> amplifier bundle add "git+https://github.com/microsoft/amplifier-bundle-redaction@main"

### README headings

- amplifier-bundle-redaction
- What's in the box
- Quick Start — install into an app
- Add as a layered behavior (recommended)
- Or install standalone (full root bundle, includes foundation)
- Or compose it from another bundle's `bundle.md`
- Use as a library — programmatic redaction (no Amplifier required)
- pyproject.toml
- Mask a string
- -> "key=[REDACTED:SECRET] contact [REDACTED:PII]"
- Scrub a whole JSON-like structure
- -> {"email": "[REDACTED:PII]", "session_id": "abc-123"}
- Extend the defaults (never replace them)
- `NAME=value` credential assignments
- -> "ACME_STAGING_API_KEY=[REDACTED:SECRET]"
- -> "CONTEXT_INTELLIGENCE_PERSONAL=[REDACTED:SECRET]"
- Library API
- Use by mounting the hook directly
- Hook configuration
- The zero-dependency contract
- Development
- Library tests (zero-dependency core)
- Hook tests — amplifier_core is host-provided at runtime, supplied ad-hoc here
- Full bundle validation (structural + BundleRegistry load + build)
- Relationship to `amplifier-module-hooks-redaction`
- Contributing
- Trademarks

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Or install standalone (full root bundle, includes foundation)

> amplifier bundle add "git+https://github.com/microsoft/amplifier-bundle-redaction@main"

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 234,177 |
| Shell | 2,833 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)
- modules/hook-redaction/pyproject.toml (capture: captured) — dependency clues: amplifier-bundle-redaction

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 1
- Forks at capture: 2
- Last updated: 2026-11-04T23:40:02Z
- Last pushed: 2026-11-11T17:05:42Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-bundle-redaction)
- [README](https://github.com/microsoft/amplifier-bundle-redaction/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-bundle-redaction/issues)
- [Releases](https://github.com/microsoft/amplifier-bundle-redaction/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
