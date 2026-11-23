# apple/containerization

- Company: Apple
- GitHub account: [https://github.com/apple](https://github.com/apple)
- Mapping status: verified
- Repository: [apple/containerization](https://github.com/apple/containerization)
- Default branch: main
- README: [Open upstream README](https://github.com/apple/containerization/blob/main/README.md)
- README blob SHA: f658b08ddadf787997ad24b6b6cd4b05ca476f8a
- Repository ID: 992765044
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Containerization is a Swift package for running Linux containers on macOS.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:10:13+00:00

### Short excerpt (up to 100 words)

> &nbsp;Containerization The Containerization package allows applications to use Linux containers. Containerization is written in Swift and uses Virtualization.framework on Apple silicon. Containerization provides APIs to: - Manage OCI images. - Interact with remote registries. - Create and populate ext4 file systems. - Interact with the Netlink socket family. - Create an optimized Linux kernel for fast boot times. - Spawn lightweight virtual machines and manage the runtime environment. - Spawn and interact with containerized processes. - Use Rosetta 2 for running linux/amd64 containers on Apple silicon. Please view the API documentation for information on the Swift packages that Containerization provides.

### README headings

- Design
- Backends
- Requirements
- Example Usage
- Linux kernel
- Kernel Support
- Pre-built Kernel
- Prepare to build package
- Install per https://github.com/apple/container, then verify it is on PATH:
- Build the package
- Test the package
- Protobufs
- Building a kernel
- Pre-commit hook
- Documentation
- Contributing
- Project Status

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Swift | 4,273,945 |
| C | 123,215 |
| Shell | 39,102 |
| Makefile | 33,307 |
| Dockerfile | 7,471 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- kernel/Makefile (capture: captured)
- vminitd/Makefile (capture: captured)
- images/linux-dev/Dockerfile (capture: captured)
- kernel/image/Dockerfile (capture: captured)
- vminitd/.devcontainer/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9029
- Forks at capture: 419
- Last updated: 2026-11-23T02:24:48Z
- Last pushed: 2026-11-18T17:02:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/apple/containerization)
- [README](https://github.com/apple/containerization/blob/main/README.md)
- [Issues](https://github.com/apple/containerization/issues)
- [Releases](https://github.com/apple/containerization/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
