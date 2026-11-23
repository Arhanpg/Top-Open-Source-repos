# NVIDIA/agent-policy-fabric

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/agent-policy-fabric](https://github.com/NVIDIA/agent-policy-fabric)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/agent-policy-fabric/blob/main/README.md)
- README blob SHA: 4fd4028b37f12a0e305713f5e27022fc9e886391
- Repository ID: 1409483917
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

APF is the enterprise policy layer for agentic workloads: one signed policy, enforced at admission and on every request.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:01:38+00:00

### Short excerpt (up to 100 words)

> APF governs what agentic workloads are allowed to do. Policy is authored and signed once, independent of any execution environment, letting the enterprise — not the developer or the agent itself — set the rules every decision is evaluated against, rather than each agent or host carrying its own hand-built version of "what's allowed." Every agent follows one governed path: admitted once under signed policy, then gated at every layer on every action. Every layer has to agree before a call proceeds: - **Sandbox containment and admission** (OpenShell) — what a sandbox can even attempt, and which tools it may

### README headings

- APF — Agent Policy Fabric
- How it works
- Documentation
- Contributing
- License
- Upstream license copies
- Notice and disclaimer

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 2,006,521 |
| Shell | 142,043 |
| Python | 47,838 |
| Dockerfile | 4,607 |
| Go Template | 3,282 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- xtask/Cargo.toml (capture: captured) — dependency clues: serde, serde_json, toml
- crates/apf-audit/Cargo.toml (capture: captured) — dependency clues: jsonschema, nix, serde, serde_json, thiserror, time, tracing, tracing-subscriber, uuid
- crates/apf-bundle/Cargo.toml (capture: captured) — dependency clues: apf-types, base64, chrono, ed25519-dalek, getrandom, hex, p256, semver, serde, serde_yaml, sha2, tempfile, thiserror, yaml-sigil-core, yaml-sigil-signing, yaml-sigil-traits, yaml-sigil-verification
- crates/apf-compile/Cargo.toml (capture: captured) — dependency clues: anyhow, apf-bundle, apf-compiler, apf-types, base64, clap, ed25519-dalek, hex, rand, serde_yaml, sha2, yaml-sigil-signing, yaml-sigil-traits
- crates/apf-compiler/Cargo.toml (capture: captured) — dependency clues: apf-bundle, apf-policy-eval, apf-proto, prost, prost-types, serde, serde_json, serde_yaml, thiserror

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 11
- Forks at capture: 2
- Last updated: 2026-11-16T01:12:13Z
- Last pushed: 2026-11-03T17:45:13Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/agent-policy-fabric)
- [README](https://github.com/NVIDIA/agent-policy-fabric/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/agent-policy-fabric/issues)
- [Releases](https://github.com/NVIDIA/agent-policy-fabric/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
