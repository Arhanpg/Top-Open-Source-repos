# ai-dynamo/frontend-crates

- Company: NVIDIA
- GitHub account: [https://github.com/ai-dynamo](https://github.com/ai-dynamo)
- Mapping status: official-project-linked
- Repository: [ai-dynamo/frontend-crates](https://github.com/ai-dynamo/frontend-crates)
- Default branch: main
- README: [Open upstream README](https://github.com/ai-dynamo/frontend-crates/blob/main/README.md)
- README blob SHA: 2abdbff2d4a6344ccd0988dd17ed1fb939e3b803
- Repository ID: 1237159425
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:32:52+00:00

### Short excerpt (up to 100 words)

> Standalone Rust crates for building OpenAI/Anthropic-compatible inference servers, plus a small demo wiring them together. Each library listed above is independently published to crates.io and can be adopted on its own. `dynamo-renderer` depends on `dynamo-protocols` and re-exports `dynamo-tokenizers`. `dynamo-parsers` depends on `dynamo-protocols` and `dynamo-structural-tag`; `dynamo-parsers-v2` depends on `dynamo-structural-tag` and owns its batch conversion helpers under `tool_calling/v1core`, without depending on the v1 parser crate. The repository itself is a Cargo workspace so shared dependency versions, CI checks, and the demo build stay consistent. For new streaming integrations, start with the Unified lifecycle example; existing batch callers can use v1. Dynamo uses

### README headings

- frontend-crates
- Layout
- Building

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 9,373,977 |
| HTML | 8,863,535 |
| Python | 2,946,155 |
| JavaScript | 751,010 |
| CSS | 98,635 |
| Shell | 15,181 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- conformance/Cargo.toml (capture: captured) — dependency clues: anyhow, dynamo-parsers, dynamo-parsers-v2, dynamo-protocols, dynamo-renderer, futures, serde, serde_json, serde_yaml, tokio
- decisions/Cargo.toml (capture: captured) — dependency clues: dynamo-protocols, serde, serde_json, thiserror
- multimodal/Cargo.toml (capture: captured) — dependency clues: base64, blake3, gif, image, ipnet, matroska-demuxer, png, rayon, reqwest, rubato, rustfft, serde, serde_json, sha2, symphonia, tokio, turbojpeg, url, xxhash-rust
- protocols/Cargo.toml (capture: captured) — dependency clues: async-openai, derive_builder, futures, indexmap, jsonschema, serde, serde_json, thiserror, tokio, tokio-test, tracing, url, utoipa, uuid
- renderer/Cargo.toml (capture: captured) — dependency clues: aho-corasick, anyhow, chrono, dynamo-parsers-v2, dynamo-protocols, dynamo-tokenizers, either, memchr, minijinja, minijinja-contrib, serde, serde_json, tempfile, tracing

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 31
- Forks at capture: 95
- Last updated: 2026-11-19T20:50:36Z
- Last pushed: 2026-11-23T18:30:19Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/ai-dynamo/frontend-crates)
- [README](https://github.com/ai-dynamo/frontend-crates/blob/main/README.md)
- [Issues](https://github.com/ai-dynamo/frontend-crates/issues)
- [Releases](https://github.com/ai-dynamo/frontend-crates/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
