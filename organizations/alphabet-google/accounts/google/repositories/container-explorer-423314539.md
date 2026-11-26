# google/container-explorer

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/container-explorer](https://github.com/google/container-explorer)
- Default branch: main
- README: [Open upstream README](https://github.com/google/container-explorer/blob/main/README.md)
- README blob SHA: c7d0d3fa0dad5f97d9eb16a4ef747247ac6d600d
- README bytes captured: 11861
- README truncated at capture limit: False
- Repository ID: 423314539
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:47:23+00:00

### Short excerpt (up to 300 words)

> **Offline Forensics**: Analyze container Container Explorer parses metadata To compile or run Because Container Explorer operates

### README headings

- Container Explorer (`container-explorer`)
- Key Features
- Architecture and Design
- Filesystem & Snapshotter Support
- Installation
- Prerequisites
- Compiling from Source
- Using the Setup Script
- Command Line Interface (CLI) Reference
- Global Flags
- Commands
- 1. `list` (or `ls`)
- Subcommands:
- List all Docker and containerd containers
- List snapshots with full host OverlayFS paths
- Export the list of all containers to a JSON file
- 2. `info` / `inspect`
- Or using the inspect shortcut:
- 3. `mount`
- You can now browse the live merged filesystem of the container under /mnt/container_inspect
- 4. `drift` (or `diff`)
- Print container drift to stdout in JSON format
- Export container drift to a JSON file
- 5. `export`
- Generates a tar archive of the container's filesystem in /tmp/container_exports/
- Limitations & Feature Matrix
- Forensic Investigation Guide
- Investigating a Mounted VM Disk
- Analyze containerd and Docker runtimes under the mounted disk image
- Check for container filesystem drift on the disk image

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Key Features

> **Offline Forensics**: Analyze container

### Architecture and design: Architecture and Design

> Container Explorer parses metadata

### Technology and requirements: Prerequisites

> To compile or run

### Limitations and security: Limitations & Feature Matrix

> Because Container Explorer operates

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 401,626 |
| Shell | 1,737 |
| Dockerfile | 640 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/BurntSushi/toml, github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/containerd/cgroups/v3, github.com/containerd/containerd, github.com/containerd/containerd/api, github.com/containerd/containerd/v2, github.com/containerd/continuity, github.com/containerd/errdefs, github.com/containerd/errdefs/pkg, github.com/containerd/log, github.com/containerd/platforms, github.com/containerd/ttrpc, github.com/containerd/typeurl/v2, github.com/cpuguy83/go-md2man/v2, github.com/docker/go-units, github.com/gogo/protobuf, github.com/golang/groupcache, github.com/google/go-cmp, github.com/klauspost/compress
- dev/docker/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 110
- Forks at capture: 14
- Last updated: 2026-10-26T07:45:58Z
- Last pushed: 2026-11-20T06:56:31Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/container-explorer)
- [README](https://github.com/google/container-explorer/blob/main/README.md)
- [Issues](https://github.com/google/container-explorer/issues)
- [Releases](https://github.com/google/container-explorer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
