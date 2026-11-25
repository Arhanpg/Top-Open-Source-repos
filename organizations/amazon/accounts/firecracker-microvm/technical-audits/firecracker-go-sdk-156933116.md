# firecracker-microvm/firecracker-go-sdk

- Company: Amazon
- Account: firecracker-microvm
- Repository: https://github.com/firecracker-microvm/firecracker-go-sdk
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:14:38+00:00

## Project purpose

We have made the decision to deprecate firecracker-go-sdk.

## Why this project is used

An SDK in Go for the Firecracker microVM API

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Go Template, Makefile, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/asaskevich/govalidator, github.com/awslabs/tc-redirect-tap, github.com/containerd/fifo, github.com/containernetworking/cni, github.com/containernetworking/plugins, github.com/davecgh/go-spew, github.com/firecracker-microvm/firecracker-go-sdk, github.com/go-openapi/analysis, github.com/go-openapi/errors, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/loads, github.com/go-openapi/runtime, github.com/go-openapi/spec, github.com/go-openapi/strfmt, github.com/go-openapi/swag, github.com/go-openapi/validate, github.com/go-ping/ping, github.com/google/uuid, github.com/hashicorp/errwrap, github.com/hashicorp/go-multierror, github.com/josharian/intern, github.com/kunalkushwaha/ltag, github.com/mailru/easyjson, github.com/mdlayher/socket, github.com/mdlayher/vsock, github.com/mitchellh/mapstructure, github.com/oklog/ulid, github.com/opentracing/opentracing-go, github.com/pmezard/go-difflib, github.com/sirupsen/logrus, github.com/stretchr/testify, github.com/vishvananda/netlink, github.com/vishvananda/netns, go.mongodb.org/mongo-driver, golang.org/x/crypto, golang.org/x/net, golang.org/x/sync, golang.org/x/sys, gopkg.in/yaml.v2, gopkg.in/yaml.v3
- Build/package tools: Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: balloon.go, balloon_test.go, benchmark_test.go, client/firecracker_client.go

## Setup and usage

No setup information established.

## Limitations and caveats

- Network Setup Limitations: These limitations are a result of the current implementation and may be lifted in the future:
- Network Setup Limitations: * For a given VM, if a CNI-configured network interface is specified or a static interface
- Network Setup Limitations: that includes IP configuration is specified, the VM can only have a single
- Network Setup Limitations: network interface, not multiple.
- Network Setup Limitations: * Users can specify multiple static interfaces as long as none of them
- Network Setup Limitations: include IP configuration.
- Network Setup Limitations: * DNS nameserver settings will only be effective if the VM's rootfs makes
- Network Setup Limitations: /etc/resolv.conf be a symlink to /proc/net/pnp.

## Evidence and provenance

- README: https://github.com/firecracker-microvm/firecracker-go-sdk/blob/main/README.md
- README SHA: 749dd629ae36016f0b8bd4e314f2e4387a810ae9
- Manifests: go.mod, Makefile, .hack/go.mod, examples/cmd/snapshotting/go.mod, examples/cmd/snapshotting/Makefile, examples/cmd/snapshotting/.hack/go.mod
- Sampled source files: balloon.go, balloon_test.go, benchmark_test.go, client/firecracker_client.go
- Git tree state: captured
- Evidence fingerprint: b81244351f7a0c737fd6a7e7d4eac8e5965dcce6519d70f434e163ac7d60048f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
