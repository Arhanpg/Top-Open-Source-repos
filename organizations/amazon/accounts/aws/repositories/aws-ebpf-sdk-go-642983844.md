# aws/aws-ebpf-sdk-go

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-ebpf-sdk-go](https://github.com/aws/aws-ebpf-sdk-go)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-ebpf-sdk-go/blob/main/README.md)
- README blob SHA: d44a73cbe098989f65206c408bc18f8c37e19d37
- README bytes captured: 4036
- README truncated at capture limit: False
- Repository ID: 642983844
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Golang based SDK for kernel eBPF operations i.e, load/attach/detach eBPF programs and create/delete/update maps. SDK relies on Unix bpf() system calls.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T22:31:38+00:00

### Short excerpt (up to 300 words)

> See CONTRIBUTING for more

### README headings

- aws-ebpf-sdk-go
- Getting started
- How to build SDK?
- How to build elf file?
- How to use the SDK?
- How to use tail calls (BPF_MAP_TYPE_PROG_ARRAY)?
- Example
- How to debug SDK issues?
- How to run unit-test
- How to run functional tests
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 361,228 |
| C | 38,279 |
| Makefile | 4,185 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/davecgh/go-spew, github.com/golang/mock, github.com/pmezard/go-difflib, github.com/stretchr/testify, github.com/vishvananda/netlink, github.com/vishvananda/netns, go.uber.org/multierr, go.uber.org/zap, golang.org/x/mod, golang.org/x/sync, golang.org/x/sys, golang.org/x/tools, golang.org/x/xerrors, gopkg.in/natefinch/lumberjack.v2, gopkg.in/yaml.v3
- Makefile (capture: captured)
- test/go.mod (capture: captured) — dependency clues: github.com/aws/aws-ebpf-sdk-go, github.com/fatih/color, github.com/mattn/go-colorable, github.com/mattn/go-isatty, github.com/vishvananda/netlink, github.com/vishvananda/netns, go.uber.org/multierr, go.uber.org/zap, golang.org/x/sys, gopkg.in/natefinch/lumberjack.v2
- test/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 86
- Forks at capture: 30
- Last updated: 2026-11-02T18:00:01Z
- Last pushed: 2026-11-20T06:44:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-ebpf-sdk-go)
- [README](https://github.com/aws/aws-ebpf-sdk-go/blob/main/README.md)
- [Issues](https://github.com/aws/aws-ebpf-sdk-go/issues)
- [Releases](https://github.com/aws/aws-ebpf-sdk-go/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
