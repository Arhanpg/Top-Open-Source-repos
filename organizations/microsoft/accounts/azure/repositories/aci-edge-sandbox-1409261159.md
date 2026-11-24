# Azure/aci-edge-sandbox

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/aci-edge-sandbox](https://github.com/Azure/aci-edge-sandbox)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/aci-edge-sandbox/blob/main/README.md)
- README blob SHA: c25b0bfe17687470cf398442ce28a3d0af3dd177
- Repository ID: 1409261159
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ACI SDK for Creating Hyper-V isolated Sandboxes on Edge devices.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:40:37+00:00

### Short excerpt (up to 100 words)

> ACI Edge Sandbox enables containerized applications to run in lightweight, Hyper-V isolated environments on edge devices and on-premises infrastructure, without requiring the Azure control plane, giving you guarantees that your application is as isolated in a container as it would be in a VM. ACI Edge Sandbox can use traditional Hyper-V-isolated ACI backends, as well as nvx, a novel cross-platform, OpenVMM-based micro-VM sandbox specialized for agentic workloads. The current bundle includes only nvx as its micro-VM sandbox backend. Additional backends will be added in the future. The SDK is the `aci_edge_sandboxes` Rust crate in `aci-edge-sandbox/`. Its Building it needs Rust

### README headings

- ACI Edge Sandbox
- Getting started
- Code of Conduct
- Security
- Trademarks

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 654,271 |
| PowerShell | 84,348 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- aci-edge-sandbox/Cargo.toml (capture: captured) — dependency clues: aci_edge_sandboxes_model, libloading, nvx, serde, serde_json, sha2, static_assertions, tempfile, tokio
- aci-edge-sandbox/model/Cargo.toml (capture: captured) — dependency clues: getrandom, humantime, nvx, serde, serde_json, thiserror

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 0
- Forks at capture: 2
- Last updated: 2026-11-07T06:45:11Z
- Last pushed: 2026-11-14T06:50:42Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/aci-edge-sandbox)
- [README](https://github.com/Azure/aci-edge-sandbox/blob/main/README.md)
- [Issues](https://github.com/Azure/aci-edge-sandbox/issues)
- [Releases](https://github.com/Azure/aci-edge-sandbox/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
