# NVIDIA/libnvidia-container

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/libnvidia-container](https://github.com/NVIDIA/libnvidia-container)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/libnvidia-container/blob/main/README.md)
- README blob SHA: 08435ec7721de74b068ad8c1c6ff9bc0e4385409
- README bytes captured: 3850
- README truncated at capture limit: False
- Repository ID: 88311197
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA container runtime library

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T19:58:58+00:00

### Short excerpt (up to 300 words)

> DESTDIR=/path/to/root make install prefix=/usr

### README headings

- libnvidia-container
- Installing the library
- From packages
- From sources
- Generate docker images for a supported <os><version>
- Or generate docker images for all supported distributions in the dist/ directory
- Alternatively in order to customize the installation paths
- Using the library
- Container runtime example
- Command line example
- Setup a new set of namespaces
- Setup a rootfs based on Ubuntu 16.04 inside the new namespaces
- Mount standard filesystems
- Isolate the first GPU device along with basic utilities
- Change into the new rootfs
- Run nvidia-smi from within the container
- Copyright and License
- Issues and Contributing
- Support and Getting Help

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Alternatively in order to customize the installation paths

> DESTDIR=/path/to/root make install prefix=/usr

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 823,837 |
| Makefile | 31,861 |
| Shell | 27,259 |
| Go | 27,185 |
| RPC | 6,189 |
| Dockerfile | 788 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- deployments/devel/Dockerfile (capture: captured)
- deployments/devel/go.mod (capture: captured) — dependency clues: github.com/davecgh/go-spew, github.com/go-logr/logr, github.com/golang/groupcache, github.com/google/go-licenses/v2, github.com/google/licenseclassifier/v2, github.com/inconshreveable/mousetrap, github.com/otiai10/copy, github.com/sergi/go-diff, github.com/spf13/cobra, github.com/spf13/pflag, go.opencensus.io, golang.org/x/mod, golang.org/x/net, golang.org/x/sync, golang.org/x/sys, golang.org/x/text, golang.org/x/tools, k8s.io/klog/v2
- src/nvcgo/go.mod (capture: captured) — dependency clues: github.com/cilium/ebpf, github.com/google/uuid, github.com/opencontainers/runtime-spec, github.com/sirupsen/logrus, golang.org/x/sys, golang.org/x/xerrors
- src/nvcgo/Makefile (capture: captured)
- src/nvcgo/vendor/github.com/cilium/ebpf/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1140
- Forks at capture: 280
- Last updated: 2026-11-23T10:06:43Z
- Last pushed: 2026-11-18T23:49:47Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/libnvidia-container)
- [README](https://github.com/NVIDIA/libnvidia-container/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/libnvidia-container/issues)
- [Releases](https://github.com/NVIDIA/libnvidia-container/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
