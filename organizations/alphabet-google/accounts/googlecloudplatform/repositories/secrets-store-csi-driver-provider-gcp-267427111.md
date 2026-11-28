# GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp/blob/main/README.md)
- README blob SHA: 2bcde5351182612e18b1af44f7935426ac2db067
- README bytes captured: 7021
- README truncated at capture limit: False
- Repository ID: 267427111
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Google Secret Manager provider for the Secret Store CSI Driver.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T06:30:31+00:00

### Short excerpt (up to 300 words)

> Create a new GKE This plugin is built

### README headings

- Google Secret Manager Provider for Secret Store CSI Driver
- Install
- if you want to use helm
- helm upgrade --install secrets-store-csi-driver-provider-gcp charts/secrets-store-csi-driver-provider-gcp
- Usage
- Secret Manager
- Create a secret with 1 active version
- grant the new service account permission to access the secret
- Parameter Manager
- set the  location
- grant the new service account permission to access the secret
- wait for pod to be in running state
- Security Considerations
- Contributing
- Support

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install

> Create a new GKE

### Limitations and security: Security Considerations

> This plugin is built

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 236,740 |
| Go Template | 43,944 |
| Shell | 16,958 |
| Makefile | 2,791 |
| Dockerfile | 2,309 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/parametermanager, cloud.google.com/go/secretmanager, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/felixge/httpsnoop, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils
- Makefile (capture: captured)
- tools/go.mod (capture: captured) — dependency clues: cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/compute/metadata, github.com/BurntSushi/toml, github.com/Microsoft/go-winio, github.com/anthropics/anthropic-sdk-go, github.com/ccojocar/zxcvbn-go, github.com/cespare/xxhash/v2, github.com/client9/misspell, github.com/emirpasic/gods, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/golang/groupcache, github.com/google/go-cmp, github.com/google/go-licenses, github.com/google/licenseclassifier, github.com/google/s2a-go, github.com/google/uuid, github.com/googleapis/enterprise-certificate-proxy
- charts/secrets-store-csi-driver-provider-gcp/Chart.yaml (capture: captured)
- test/e2e/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 266
- Forks at capture: 71
- Last updated: 2026-10-26T09:02:37Z
- Last pushed: 2026-11-20T11:57:17Z
- Topics: csi, gcp, gcp-secret-manager, google-cloud-platform, kubernetes, secrets

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp)
- [README](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp/issues)
- [Releases](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
