# amazon-archives/aws-app-mesh-inject

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/aws-app-mesh-inject](https://github.com/amazon-archives/aws-app-mesh-inject)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/aws-app-mesh-inject/blob/master/README.md)
- README blob SHA: 74cae233dcc9ac28025cd780d9949aace58a7863
- Repository ID: 171725089
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS AppMesh sidecar injector for EKS.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:44:23+00:00

### Short excerpt (up to 100 words)

> The AWS App Mesh Kubernetes sidecar injecting Admission Controller. If you think you’ve found a potential security issue, please do not post it in the Issues. Instead, please follow the instructions here or email AWS security directly. Please reference the install instructions. To align our helm repository and this repository we have changed the namespace to appmesh-system and resource names to appmesh-inject. To enable sidecar injection for a namespace, you need to label the namespace with `appmesh.k8s.aws/sidecarInjectorWebhook=enabled` kubectl label namespace appmesh-demo appmesh.k8s.aws/sidecarInjectorWebhook=enabled For namespaces with sidecar injection enabled, pods will be injected if the `appmesh.k8s.aws/sidecarInjectorWebhook` annotation is `enabled` and will

### README headings

- App Mesh Inject
- Security disclosures
- Installation
- Warning
- Under the hood
- Enable Sidecar injection
- Default behavior and how to override
- Troubleshooting
- CA bundle not configured properly

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 69,587 |
| Shell | 7,583 |
| Makefile | 2,905 |
| Dockerfile | 692 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go, github.com/davecgh/go-spew, github.com/evanphx/json-patch, github.com/gogo/protobuf, github.com/golang/protobuf, github.com/google/gofuzz, github.com/googleapis/gnostic, github.com/imdario/mergo, github.com/json-iterator/go, github.com/konsorten/go-windows-terminal-sequences, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/spf13/pflag, golang.org/x/crypto, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sys, golang.org/x/text, golang.org/x/time, google.golang.org/appengine
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 55
- Forks at capture: 40
- Last updated: 2026-11-13T20:11:21Z
- Last pushed: 2020-06-11T17:29:00Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/aws-app-mesh-inject)
- [README](https://github.com/amazon-archives/aws-app-mesh-inject/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/aws-app-mesh-inject/issues)
- [Releases](https://github.com/amazon-archives/aws-app-mesh-inject/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
