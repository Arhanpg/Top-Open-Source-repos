# firecracker-microvm/firecracker-go-sdk

- Company: Amazon
- GitHub account: [https://github.com/firecracker-microvm](https://github.com/firecracker-microvm)
- Mapping status: official-directory-listed
- Repository: [firecracker-microvm/firecracker-go-sdk](https://github.com/firecracker-microvm/firecracker-go-sdk)
- Default branch: main
- README: [Open upstream README](https://github.com/firecracker-microvm/firecracker-go-sdk/blob/main/README.md)
- README blob SHA: 749dd629ae36016f0b8bd4e314f2e4387a810ae9
- Repository ID: 156933116
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An SDK in Go for the Firecracker microVM API

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:36:21+00:00

### Short excerpt (up to 100 words)

> We have made the decision to deprecate firecracker-go-sdk. The original intention for this project revolved around firecracker-containerd. As that project is being sunsetted, and most of the work in firecracker-go-sdk revolved around firecracker-containerd, it made sense to also deprecate the Go SDK which itself has been in a state of partial maintenance for a while. If you are interested in continuing to develop this project, you can fork it and continue to maintain it yourself, provided the original LICENSE continues to be followed. There are no alternative solutions to this project due to its specificity of use-case and connection to

### README headings

- As of November 10 2026, this project is no longer maintained.
- CNI
- Example
- Network Setup Limitations

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 322,317 |
| Go Template | 9,119 |
| Makefile | 5,855 |
| Shell | 150 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/asaskevich/govalidator, github.com/containerd/fifo, github.com/containernetworking/cni, github.com/containernetworking/plugins, github.com/davecgh/go-spew, github.com/go-openapi/analysis, github.com/go-openapi/errors, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/loads, github.com/go-openapi/runtime, github.com/go-openapi/spec, github.com/go-openapi/strfmt, github.com/go-openapi/swag, github.com/go-openapi/validate, github.com/go-ping/ping, github.com/google/uuid, github.com/hashicorp/errwrap, github.com/hashicorp/go-multierror, github.com/josharian/intern
- Makefile (capture: captured)
- .hack/go.mod (capture: captured) — dependency clues: github.com/awslabs/tc-redirect-tap, github.com/containernetworking/plugins, github.com/kunalkushwaha/ltag
- examples/cmd/snapshotting/go.mod (capture: captured) — dependency clues: github.com/asaskevich/govalidator, github.com/containerd/fifo, github.com/containernetworking/cni, github.com/containernetworking/plugins, github.com/firecracker-microvm/firecracker-go-sdk, github.com/go-openapi/analysis, github.com/go-openapi/errors, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/loads, github.com/go-openapi/runtime, github.com/go-openapi/spec, github.com/go-openapi/strfmt, github.com/go-openapi/swag, github.com/go-openapi/validate, github.com/google/uuid, github.com/hashicorp/errwrap, github.com/hashicorp/go-multierror, github.com/josharian/intern, github.com/mailru/easyjson
- examples/cmd/snapshotting/Makefile (capture: captured)
- examples/cmd/snapshotting/.hack/go.mod (capture: captured) — dependency clues: github.com/awslabs/tc-redirect-tap, github.com/containernetworking/plugins

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 679
- Forks at capture: 170
- Last updated: 2026-11-16T00:02:01Z
- Last pushed: 2026-11-10T19:54:19Z
- Topics: firecracker, firecracker-api, firecracker-vm, golang-library, sdk, virtual-machine

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/firecracker-microvm/firecracker-go-sdk)
- [README](https://github.com/firecracker-microvm/firecracker-go-sdk/blob/main/README.md)
- [Issues](https://github.com/firecracker-microvm/firecracker-go-sdk/issues)
- [Releases](https://github.com/firecracker-microvm/firecracker-go-sdk/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
