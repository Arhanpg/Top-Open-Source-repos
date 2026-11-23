# bottlerocket-os/bottlerocket-admin-container

- Company: Amazon
- GitHub account: [https://github.com/bottlerocket-os](https://github.com/bottlerocket-os)
- Mapping status: official-directory-listed
- Repository: [bottlerocket-os/bottlerocket-admin-container](https://github.com/bottlerocket-os/bottlerocket-admin-container)
- Default branch: develop
- README: [Open upstream README](https://github.com/bottlerocket-os/bottlerocket-admin-container/blob/develop/README.md)
- README blob SHA: c6f610b6ac2b96eef3a81abe05f2bb13225b3265
- Repository ID: 240619493
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A container for admin access to Bottlerocket

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:35:54+00:00

### Short excerpt (up to 100 words)

> This is the admin container for troubleshooting the Bottlerocket operating system. It runs outside of Bottlerocket's container orchestrator in a separate instance of `containerd`. The container hosts an SSH server to allow public key SSH access, as well as `agetty` services for serial console devices to allow console access. You can also connect to the admin container via the control container by running `enter-admin-container`. Unless otherwise specified through user-data, the default user is **ec2-user**. The admin container is disabled by default in Bottlerocket. For more information about how the admin container fits into the Bottlerocket operating system, please see the

### README headings

- Bottlerocket Admin Container
- Building the Container Image
- Authenticating with the Admin Container
- ex: echo '{"ssh":{"authorized-keys":[]}}' | base64
- NVIDIA GPU Bug Report Script
- Prerequisites
- Usage

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 93,557 |
| Dockerfile | 3,376 |
| Makefile | 1,898 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 67
- Forks at capture: 47
- Last updated: 2026-10-22T00:05:55Z
- Last pushed: 2026-11-13T18:52:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/bottlerocket-os/bottlerocket-admin-container)
- [README](https://github.com/bottlerocket-os/bottlerocket-admin-container/blob/develop/README.md)
- [Issues](https://github.com/bottlerocket-os/bottlerocket-admin-container/issues)
- [Releases](https://github.com/bottlerocket-os/bottlerocket-admin-container/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
