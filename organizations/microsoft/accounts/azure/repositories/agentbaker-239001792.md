# Azure/AgentBaker

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/AgentBaker](https://github.com/Azure/AgentBaker)
- Default branch: dev
- README: [Open upstream README](https://github.com/Azure/AgentBaker/blob/dev/README.md)
- README blob SHA: 1e44a1837aa835fbb6e0fc797f8c28c90068aaf4
- README bytes captured: 3361
- README truncated at capture limit: False
- Repository ID: 239001792
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Agent Baker is aiming to provide a centralized, portable k8s agent node provisioning lib as well as rich support on different OS image with optimized k8s binaries.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T07:51:28+00:00

### Short excerpt (up to 300 words)

> AgentBaker provides components that build VM images and provision Kubernetes nodes in Azure. AgentBaker includes: A VHD builder that creates Linux and Windows node images.

### README headings

- AgentBaker
- Style
- Tests
- Ubuntu GRID driver branches
- Shell scripts
- E2E
- Contributor License Agreement (CLA)
- CGManifest File

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: AgentBaker

> AgentBaker provides components that build VM images and provision Kubernetes nodes in Azure. AgentBaker includes: A VHD builder that creates Linux and Windows node images.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 3,337,441 |
| Shell | 2,792,006 |
| PowerShell | 1,275,077 |
| Python | 132,519 |
| Groovy | 24,210 |
| Makefile | 19,330 |
| Roff | 8,399 |
| CUE | 7,669 |
| Dockerfile | 5,890 |
| C# | 1,678 |
| Batchfile | 1,627 |
| HCL | 127 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/Azure/go-autorest, github.com/Azure/go-autorest/autorest/to, github.com/Masterminds/semver/v3, github.com/aws/aws-sdk-go-v2, github.com/barkimedes/go-deepcopy, github.com/clarketm/json, github.com/coreos/butane, github.com/coreos/go-json, github.com/coreos/go-semver, github.com/coreos/go-systemd/v22, github.com/coreos/ignition/v2, github.com/coreos/vcontext, github.com/felixge/httpsnoop, github.com/fsnotify/fsnotify, github.com/google/go-cmp, github.com/gorilla/handlers, github.com/gorilla/mux, github.com/inconshreveable/mousetrap, github.com/nxadm/tail, github.com/onsi/ginkgo
- Makefile (capture: captured)
- aks-live-patching/go.mod (capture: captured) — dependency clues: golang.org/x/net, golang.org/x/sys, golang.org/x/text, google.golang.org/genproto/googleapis/rpc, google.golang.org/grpc, google.golang.org/protobuf
- aks-live-patching/Makefile (capture: captured)
- aks-node-controller/go.mod (capture: captured) — dependency clues: github.com/Azure/agentbaker/aks-live-patching, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Masterminds/semver/v3, github.com/fsnotify/fsnotify, github.com/google/go-cmp, github.com/kr/pretty, github.com/rogpeppe/go-internal, github.com/stretchr/testify, github.com/urfave/cli/v3, go.yaml.in/yaml/v3, golang.org/x/net, golang.org/x/sys, golang.org/x/text, google.golang.org/genproto/googleapis/rpc, google.golang.org/grpc, google.golang.org/protobuf, gopkg.in/check.v1, gopkg.in/yaml.v3
- aks-node-controller/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 161
- Forks at capture: 285
- Last updated: 2026-11-12T01:50:50Z
- Last pushed: 2026-11-23T19:22:19Z
- Topics: agent, cloud-init, k8s, os, vhd

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/AgentBaker)
- [README](https://github.com/Azure/AgentBaker/blob/dev/README.md)
- [Issues](https://github.com/Azure/AgentBaker/issues)
- [Releases](https://github.com/Azure/AgentBaker/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
