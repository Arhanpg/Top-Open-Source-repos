# bottlerocket-os/bottlerocket-core-kit

- Company: Amazon
- GitHub account: [https://github.com/bottlerocket-os](https://github.com/bottlerocket-os)
- Mapping status: official-directory-listed
- Repository: [bottlerocket-os/bottlerocket-core-kit](https://github.com/bottlerocket-os/bottlerocket-core-kit)
- Default branch: develop
- README: [Open upstream README](https://github.com/bottlerocket-os/bottlerocket-core-kit/blob/develop/README.md)
- README blob SHA: 1f3ef5b98b6c7c69069deb0adfdf68be41da4616
- Repository ID: 810418424
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A kit with core software packaged for Bottlerocket

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:36:00+00:00

### Short excerpt (up to 100 words)

> This is the core kit for Bottlerocket. It includes many common dependencies for downstream package and variant builds. The core kit includes: * Shared libraries such as glibc and libz * Management daemons such as systemd and dbus-broker * Agents for settings API and in-place updates The Bottlerocket core kit is available through Amazon ECR Public. The core kit can be built on either an **x86_64** or an **aarch64** host. To do this you can use the following commands. make OR make ARCH=<aarch64, x86_64> See the BUILDING guide for more details.

### README headings

- Bottlerocket Core Kit
- Contents
- Availability
- Development

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 2,387,713 |
| Go | 72,492 |
| Shell | 17,581 |
| Makefile | 1,924 |
| JavaScript | 1,893 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- Makefile (capture: captured)
- sources/Cargo.toml (capture: captured)
- kits/bottlerocket-core-kit/Cargo.toml (capture: captured) — dependency clues: amazon-ecs-cni-plugins, amazon-ssm-agent, amazon-vpc-cni-plugins, aws-iam-authenticator, aws-otel-collector, aws-signer-notation-plugin, aws-signing-helper, bash, binutils, chrony, cni, cni-plugins, conntrack-tools, containerd-1_7, containerd-2_2, containerd-2_3, coreutils, cri-tools, dbus-broker, docker-cli-25
- packages/amazon-ecs-cni-plugins/Cargo.toml (capture: captured) — dependency clues: glibc
- packages/amazon-ssm-agent/Cargo.toml (capture: captured) — dependency clues: glibc

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 36
- Forks at capture: 87
- Last updated: 2026-11-11T20:26:00Z
- Last pushed: 2026-11-23T19:35:22Z
- Topics: bottlerocket

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/bottlerocket-os/bottlerocket-core-kit)
- [README](https://github.com/bottlerocket-os/bottlerocket-core-kit/blob/develop/README.md)
- [Issues](https://github.com/bottlerocket-os/bottlerocket-core-kit/issues)
- [Releases](https://github.com/bottlerocket-os/bottlerocket-core-kit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
