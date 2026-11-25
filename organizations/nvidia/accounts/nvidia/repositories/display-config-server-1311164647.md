# NVIDIA/display-config-server

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/display-config-server](https://github.com/NVIDIA/display-config-server)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/display-config-server/blob/main/README.md)
- README blob SHA: 644dae4b05b661f4bef3fbffd4aca28373250c95
- README bytes captured: 9906
- README truncated at capture limit: False
- Repository ID: 1311164647
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Configuration and persistence server for workstation display features

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T01:04:17+00:00

### Short excerpt (up to 300 words)

> Instead of using MOSAIC The examples below assume DCS uses Smithay as

### README headings

- Display Config Server
- Background
- System overview
- Design
- Multi-output and multi-GPU
- Splash screen
- Building
- Running
- Usage examples
- Starting DCS
- Showing the current configuration
- Applying a mode to a single display
- Configuring multiple displays
- /etc/dcs/wall.yaml
- RTX Pro Sync across two systems
- Machine A — /etc/dcs/sync-server.yaml
- Machine B — /etc/dcs/sync-client.yaml
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: System overview

> Instead of using MOSAIC

### Getting started and usage: Usage examples

> The examples below assume

### Architecture and design: Design

> DCS uses Smithay as

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 237,288 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured) — dependency clues: anyhow, clap, drm, drm-fourcc, gbm, libc, png, smithay, tracing, tracing-subscriber, wayland-scanner, wayland-server
- dcs-client/Cargo.toml (capture: captured) — dependency clues: anyhow, serde, serde_yaml, wayland-client, wayland-scanner
- dcs-test/Cargo.toml (capture: captured) — dependency clues: ash, clap, dcs-client, libc, wayland-protocols
- dcs-tool/Cargo.toml (capture: captured) — dependency clues: anyhow, clap, dcs-client, serde, serde_yaml

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3
- Forks at capture: 1
- Last updated: 2026-10-05T19:57:34Z
- Last pushed: 2026-09-29T21:04:52Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/display-config-server)
- [README](https://github.com/NVIDIA/display-config-server/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/display-config-server/issues)
- [Releases](https://github.com/NVIDIA/display-config-server/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
