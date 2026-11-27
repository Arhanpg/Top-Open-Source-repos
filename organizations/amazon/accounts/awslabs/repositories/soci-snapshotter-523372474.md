# awslabs/soci-snapshotter

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/soci-snapshotter](https://github.com/awslabs/soci-snapshotter)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/soci-snapshotter/blob/main/README.md)
- README blob SHA: de2cbbedb2ad983cf83bcbd6ca0c5a05e5ea5665
- README bytes captured: 4838
- README truncated at capture limit: False
- Repository ID: 523372474
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A containerd snapshotter plugin which enables standard OCI images to be lazily loaded without requiring a build-time conversion step.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T20:00:31+00:00

### Short excerpt (up to 300 words)

> SOCI Snapshotter is a containerd snapshotter plugin. It enables standard OCI images to be lazily loaded without requiring a build-time conversion step. "SOCI" is short

### README headings

- SOCI Snapshotter
- Design considerations
- No image conversion
- Workload-specific load order optimization
- Documentation
- Integration-specific documentation
- Project Origin

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: SOCI Snapshotter

> SOCI Snapshotter is a containerd snapshotter plugin. It enables standard OCI images to be lazily loaded without requiring a build-time conversion step. "SOCI" is short

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 1,539,171 |
| Shell | 35,584 |
| C | 28,752 |
| Makefile | 8,093 |
| Dockerfile | 5,378 |
| Go Template | 358 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/containerd/cgroups/v3, github.com/containerd/containerd/api, github.com/containerd/containerd/v2, github.com/containerd/continuity, github.com/containerd/errdefs, github.com/containerd/errdefs/pkg, github.com/containerd/fifo, github.com/containerd/log, github.com/containerd/platforms, github.com/containerd/plugin, github.com/containerd/ttrpc, github.com/containerd/typeurl/v2, github.com/davecgh/go-spew, github.com/distribution/reference, github.com/docker/cli, github.com/docker/docker-credential-helpers
- Makefile (capture: captured)
- cmd/go.mod (capture: captured) — dependency clues: github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/awslabs/soci-snapshotter, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/containerd/cgroups/v3, github.com/containerd/containerd/api, github.com/containerd/containerd/v2, github.com/containerd/continuity, github.com/containerd/errdefs, github.com/containerd/errdefs/pkg, github.com/containerd/fifo, github.com/containerd/log, github.com/containerd/platforms, github.com/containerd/plugin, github.com/containerd/ttrpc, github.com/containerd/typeurl/v2, github.com/coreos/go-systemd/v22, github.com/davecgh/go-spew, github.com/distribution/reference

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 796
- Forks at capture: 100
- Last updated: 2026-11-19T21:43:26Z
- Last pushed: 2026-11-19T21:22:45Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/soci-snapshotter)
- [README](https://github.com/awslabs/soci-snapshotter/blob/main/README.md)
- [Issues](https://github.com/awslabs/soci-snapshotter/issues)
- [Releases](https://github.com/awslabs/soci-snapshotter/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
