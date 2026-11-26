# NVIDIA/nvidia-mnccd

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/nvidia-mnccd](https://github.com/NVIDIA/nvidia-mnccd)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/nvidia-mnccd/blob/main/README.md)
- README blob SHA: 329707bd05585e057400f6776d3ba02fe14b6dfb
- README bytes captured: 15402
- README truncated at capture limit: False
- Repository ID: 1340731705
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A usermode daemon responsible for key/iv management across nodes and multi-node discovery.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:17:11+00:00

### Short excerpt (up to 300 words)

> /path/to/nvidia-mnccd --help NVML_HEADER_DIR=/usr/local/cuda-13.5/include cargo build **Debug

### README headings

- nvidia-mnccd
- Building nvidia-mnccd
- Example: CUDA 13.5 installed at /usr/local/cuda-13.5
- Running nvidia-mnccd
- Usage summary
- From the repo (Cargo sets CARGO_MANIFEST_DIR; uses ./mnccd_config.toml)
- Default: TLS-PSK when [tls].mode is omitted; psk_identity and psk_key are still required
- Installed or copied binary: set config directory
- Skip NVLE setup on the leader
- Plain gRPC (no TLS)—must be set on every node in the cluster
- Manual background run (logs under /tmp; not for systemd)
- Privileges
- Production deployment
- Run package
- Starting the service
- Logging
- Only warnings and errors from MNCCD
- API documentation
- Contributions

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Usage summary

> /path/to/nvidia-mnccd --help

### Getting started and usage: Example: CUDA 13.5 installed at /usr/local/cuda-13.5

> NVML_HEADER_DIR=/usr/local/cuda-13.5/include cargo build **Debug

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 210,130 |
| Shell | 9,308 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured) — dependency clues: bindgen, clap, daemonize, futures, getrandom, hkdf, libc, libloading, local-ip-address, once_cell, openssl, prost, protox, serde, sha2, thiserror, tokio, tokio-retry, toml, tonic

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 2
- Last updated: 2026-10-16T06:03:07Z
- Last pushed: 2026-10-13T04:03:18Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/nvidia-mnccd)
- [README](https://github.com/NVIDIA/nvidia-mnccd/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/nvidia-mnccd/issues)
- [Releases](https://github.com/NVIDIA/nvidia-mnccd/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
