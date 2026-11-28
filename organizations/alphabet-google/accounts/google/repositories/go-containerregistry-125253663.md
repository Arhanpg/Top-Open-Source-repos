# google/go-containerregistry

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/go-containerregistry](https://github.com/google/go-containerregistry)
- Default branch: main
- README: [Open upstream README](https://github.com/google/go-containerregistry/blob/main/README.md)
- README blob SHA: de70fb7c57349f3dfef0a9297304e4af615a7c15
- README bytes captured: 6377
- README truncated at capture limit: False
- Repository ID: 125253663
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Go library and CLIs for working with container registries

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T03:12:18+00:00

### Short excerpt (up to 300 words)

> This is a golang

### README headings

- go-containerregistry
- Introduction
- Philosophy
- `v1.Image`
- Sources
- Sinks
- `v1.ImageIndex`
- Sources
- Sinks
- `v1.Layer`
- Sources
- Sinks
- Overview
- `mutate`
- `partial`
- `transport`
- Tools
- `crane`
- `gcrane`
- `krane`
- `k8schain`
- Emeritus: [`ko`](https://github.com/google/ko)

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> This is a golang

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 1,478,096 |
| Shell | 17,186 |
| Dockerfile | 118 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cloud.google.com/go/compute/metadata, github.com/Microsoft/go-winio, github.com/cespare/xxhash/v2, github.com/containerd/errdefs, github.com/containerd/errdefs/pkg, github.com/cpuguy83/go-md2man/v2, github.com/distribution/reference, github.com/docker/cli, github.com/docker/docker-credential-helpers, github.com/docker/go-connections, github.com/docker/go-units, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/google/go-cmp, github.com/inconshreveable/mousetrap, github.com/klauspost/compress, github.com/moby/docker-image-spec, github.com/moby/moby/api, github.com/moby/moby/client
- cmd/gcrane/Dockerfile (capture: captured)
- cmd/krane/go.mod (capture: captured) — dependency clues: cloud.google.com/go/compute/metadata, github.com/Azure/azure-sdk-for-go, github.com/Azure/go-autorest, github.com/Azure/go-autorest/autorest, github.com/Azure/go-autorest/autorest/adal, github.com/Azure/go-autorest/autorest/azure/auth, github.com/Azure/go-autorest/autorest/azure/cli, github.com/Azure/go-autorest/autorest/date, github.com/Azure/go-autorest/logger, github.com/Azure/go-autorest/tracing, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/ecr, github.com/aws/aws-sdk-go-v2/service/ecrpublic, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding
- pkg/authn/k8schain/go.mod (capture: captured) — dependency clues: cloud.google.com/go/compute/metadata, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/containers/azcontainerregistry, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/ecr, github.com/aws/aws-sdk-go-v2/service/ecrpublic, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc
- pkg/authn/kubernetes/go.mod (capture: captured) — dependency clues: github.com/davecgh/go-spew, github.com/docker/cli, github.com/docker/docker-credential-helpers, github.com/emicklei/go-restful/v3, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading, github.com/go-openapi/swag/mangling, github.com/go-openapi/swag/netutils, github.com/go-openapi/swag/pools, github.com/go-openapi/swag/stringutils, github.com/go-openapi/swag/typeutils, github.com/go-openapi/swag/yamlutils
- vendor/go.opentelemetry.io/otel/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4144
- Forks at capture: 720
- Last updated: 2026-11-23T18:22:24Z
- Last pushed: 2026-11-18T02:33:54Z
- Topics: container, container-registry, docker, registry

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/go-containerregistry)
- [README](https://github.com/google/go-containerregistry/blob/main/README.md)
- [Issues](https://github.com/google/go-containerregistry/issues)
- [Releases](https://github.com/google/go-containerregistry/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
