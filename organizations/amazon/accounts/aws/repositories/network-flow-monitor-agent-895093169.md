# aws/network-flow-monitor-agent

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/network-flow-monitor-agent](https://github.com/aws/network-flow-monitor-agent)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/network-flow-monitor-agent/blob/main/README.md)
- README blob SHA: 334e02db28f11a3d22170ea4078443a9bc2faf62
- README bytes captured: 5812
- README truncated at capture limit: False
- Repository ID: 895093169
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon CloudWatch Network Monitoring - Network Flow Monitor agent repository

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:50:00+00:00

### Short excerpt (up to 300 words)

> This is an on-host agent that passively collects performance statistics related to various communication protocols of interest, beginning with TCP. The statistics can be published

### README headings

- Network Flow Monitor Agent
- Installation
- Building
- Running
- Testing
- Integration Tests
- EC2 Multi-Distro (`integration-tests-ec2.yml`)
- Kubernetes (`integration-tests-k8s.yml`)
- Known Incompatible Distributions
- Distributions
- Versioning
- Release Tags
- Bumping the Version
- Version Sync
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Network Flow Monitor Agent

> This is an on-host agent that passively collects performance statistics related to various communication protocols of interest, beginning with TCP. The statistics can be published

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 841,571 |
| Shell | 125,040 |
| Python | 32,648 |
| Makefile | 1,732 |
| Go Template | 1,569 |
| Dockerfile | 406 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- nfm-bpf/Cargo.toml (capture: captured) — dependency clues: aya-ebpf, aya-log-common, nfm-common
- nfm-common/Cargo.toml (capture: captured) — dependency clues: aya, aya-ebpf, bitflags, libc, serde
- nfm-controller/Cargo.toml (capture: captured) — dependency clues: anyhow, assert_approx_eq, aws-config, aws-credential-types, aws-sign-v4, aya, aya-obj, caps, cargo_metadata, chrono, clap, criterion, dhat, env_logger, flate2, futures, getifaddrs, hashbrown, hex, hyper
- charts/amazon-network-flow-monitor-agent/Chart.yaml (capture: captured)
- charts/amazon-network-flow-monitor-agent/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 32
- Forks at capture: 17
- Last updated: 2026-11-13T12:40:40Z
- Last pushed: 2026-11-23T17:44:32Z
- Topics: agent, aws, flow, monitor, network

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/network-flow-monitor-agent)
- [README](https://github.com/aws/network-flow-monitor-agent/blob/main/README.md)
- [Issues](https://github.com/aws/network-flow-monitor-agent/issues)
- [Releases](https://github.com/aws/network-flow-monitor-agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
