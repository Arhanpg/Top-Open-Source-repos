# NVIDIA/storage-lender

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/storage-lender](https://github.com/NVIDIA/storage-lender)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/storage-lender/blob/main/README.md)
- README blob SHA: 1440033f6fa57ab4e91ff84b4a2400f10b498b0b
- README bytes captured: 30247
- README truncated at capture limit: False
- Repository ID: 1306886176
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A service that lends NVMe I/O queues to unprivileged clients over a Unix domain socket.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T03:13:42+00:00

### Short excerpt (up to 300 words)

> Storage Lender separates NVMe The required Linux and

### README headings

- storage-lender
- How it works
- Dependencies
- Building
- Development checks
- Packaging
- Open-source notice bundle
- Running
- Bind the NVMe device to vfio-pci first, e.g.:
- When systemd is not starting the daemon, create the configured parent first:
- Start the server with the repository configuration:
- Socket troubleshooting
- Management ctl
- Logging policy
- Device policy
- Resource governance
- Wire protocol
- API
- Buffer lifecycle
- Device lifecycle
- Queue lifecycle
- Client library
- or
- Testing
- Continuous integration
- Coverage report
- Documentation
- License
- Project layout

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: How it works

> Storage Lender separates NVMe

### Technology and requirements: Dependencies

> The required Linux and

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 681,481 |
| CMake | 34,597 |
| Shell | 17,890 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- client/CMakeLists.txt (capture: captured)
- ctl/CMakeLists.txt (capture: captured)
- examples/CMakeLists.txt (capture: captured)
- proto/CMakeLists.txt (capture: captured)
- server/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9
- Forks at capture: 5
- Last updated: 2026-11-06T07:40:54Z
- Last pushed: 2026-10-15T18:53:29Z
- Topics: cpp, linux, nvme, spdk, storage, vfio

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/storage-lender)
- [README](https://github.com/NVIDIA/storage-lender/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/storage-lender/issues)
- [Releases](https://github.com/NVIDIA/storage-lender/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
