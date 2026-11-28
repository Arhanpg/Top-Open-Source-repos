# microsoft/babylon-native-rs

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/babylon-native-rs](https://github.com/microsoft/babylon-native-rs)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/babylon-native-rs/blob/main/README.md)
- README blob SHA: 04af68cafd88ff1f232670645698eb09bb0c623a
- README bytes captured: 20024
- README truncated at capture limit: False
- Repository ID: 1311276325
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Rust bindings for Babylon Native

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T05:57:06+00:00

### Short excerpt (up to 300 words)

> **Shim-first with cxx for

### README headings

- babylon-native-rs
- Goal
- Current state
- Known gaps & resolved binding challenges
- API surface
- Graphics / lifecycle
- Runtime / scripting
- Polyfills
- Plugins
- N-API bridge
- The napi boundary (key strategy)
- Workback plan
- Phase 0 — Foundation & build hardening
- Phase 1 — Retarget bindings to the à-la-carte API (cxx shim)
- Phase 2 — Device & frame loop
- Phase 3 — Runtime, scripts & polyfills/plugins
- Phase 4 — N-API bridge (C ABI)
- Phase 5 — Polish & release
- Design decisions
- Layout

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Design decisions

> **Shim-first with cxx for

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 134,035 |
| C++ | 20,928 |
| PowerShell | 3,898 |
| JavaScript | 1,794 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- babylon_native/Cargo.toml (capture: captured) — dependency clues: babylon_native_sys, cxx, windows
- babylon_native_sys/Cargo.toml (capture: captured) — dependency clues: cc, cxx, cxx-build, git2, windows-sys
- babylon_native/examples/package.json (capture: captured) — dependency clues: babylonjs

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 0
- Forks at capture: 2
- Last updated: 2026-08-07T18:08:00Z
- Last pushed: 2026-07-24T21:54:27Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/babylon-native-rs)
- [README](https://github.com/microsoft/babylon-native-rs/blob/main/README.md)
- [Issues](https://github.com/microsoft/babylon-native-rs/issues)
- [Releases](https://github.com/microsoft/babylon-native-rs/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
