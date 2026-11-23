# firecracker-microvm/firecracker-containerd

- Company: Amazon
- GitHub account: [https://github.com/firecracker-microvm](https://github.com/firecracker-microvm)
- Mapping status: official-directory-listed
- Repository: [firecracker-microvm/firecracker-containerd](https://github.com/firecracker-microvm/firecracker-containerd)
- Default branch: main
- README: [Open upstream README](https://github.com/firecracker-microvm/firecracker-containerd/blob/main/README.md)
- README blob SHA: 7141c0169851b797daf05d23f7fdbdb868f587fb
- Repository ID: 157781317
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

firecracker-containerd enables containerd to manage containers as Firecracker microVMs

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:36:17+00:00

### Short excerpt (up to 100 words)

> We have made the decision to deprecate firecracker-containerd. firecracker-containerd was created to combine the lightweight, friendly interface of containers with the security of kernel-level isolation. When the project started, this was a novel approach. Since then, the ecosystem has matured: several projects now deliver the same model with more robust implementations and active investment behind them. Amazon has done the same via Nitro Sandboxes, which leverages Nitro Enclaves to achieve hardware-backed isolation for your container workloads. Given those alternatives, we have archived firecracker-containerd rather than continue partial maintenance. The repository will remain available in read-only form for reference. If you

### README headings

- As of November 10 2026, this project is no longer maintained.
- TL;DR firecracker-containerd is no longer maintained. Please see [alternatives](#alternatives) for migrating workloads to more modern, secure alternatives.
- Alternatives
- firecracker-containerd
- Roadmap
- Usage
- Questions?
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 653,511 |
| Makefile | 38,923 |
| Shell | 17,527 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cyphar.com/go-pathrs, dario.cat/mergo, github.com/AdaLogics/go-fuzz-headers, github.com/AdamKorcz/go-118-fuzz-build, github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/StackExchange/wmi, github.com/asaskevich/govalidator, github.com/awslabs/tc-redirect-tap, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cespare/xxhash/v2, github.com/cilium/ebpf, github.com/containerd/cgroups, github.com/containerd/cgroups/v3, github.com/containerd/console, github.com/containerd/containerd, github.com/containerd/containerd/api, github.com/containerd/continuity, github.com/containerd/errdefs
- Makefile (capture: captured)
- agent/Makefile (capture: captured)
- docker-credential-mmds/go.mod (capture: captured) — dependency clues: github.com/davecgh/go-spew, github.com/docker/docker-credential-helpers, github.com/pmezard/go-difflib, github.com/stretchr/testify, gopkg.in/yaml.v3
- docker-credential-mmds/Makefile (capture: captured)
- examples/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2984
- Forks at capture: 252
- Last updated: 2026-11-19T03:42:11Z
- Last pushed: 2026-11-10T19:55:59Z
- Topics: aws, containerd, containers, firecracker, firecracker-containerd, firecracker-microvms, oci, virtualization

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/firecracker-microvm/firecracker-containerd)
- [README](https://github.com/firecracker-microvm/firecracker-containerd/blob/main/README.md)
- [Issues](https://github.com/firecracker-microvm/firecracker-containerd/issues)
- [Releases](https://github.com/firecracker-microvm/firecracker-containerd/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
