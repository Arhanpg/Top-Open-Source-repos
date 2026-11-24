# kyma-project/eventing-publisher-proxy

- Company: SAP
- GitHub account: [https://github.com/kyma-project](https://github.com/kyma-project)
- Mapping status: official-directory-listed
- Repository: [kyma-project/eventing-publisher-proxy](https://github.com/kyma-project/eventing-publisher-proxy)
- Default branch: main
- README: [Open upstream README](https://github.com/kyma-project/eventing-publisher-proxy/blob/main/README.md)
- README blob SHA: 6d527667bdbd18893fbcbc8465f128952065531a
- Repository ID: 730578500
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:41:50+00:00

### Short excerpt (up to 100 words)

> The Eventing Publisher Proxy receives legacy and Cloud Event publishing requests from the cluster workloads (microservice or Serverless functions) and redirects them to the Enterprise Messaging Service Cloud Event Gateway. It also fetches a list of subscriptions for a connected application. - Go - Docker - kubectl - kustomize - Access to a Kubernetes cluster (e.g. k3d / k8s) make build Run the unit and integration tests: make generate-and-test To run the E2E tests, refer to Testing. 1. Fix common lint issues: make imports make fmt make lint-fix Build and push your image to the location specified by `IMG`: make

### README headings

- Eventing Publisher Proxy
- Overview
- Prerequisites
- Development
- Build
- Run Tests
- Linting
- Build Container Images
- Deployment
- Deploy Inside a Cluster
- Usage
- Send Events
- Get a list of subscriptions for a connected application
- Environment Variables
- Flags
- Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 253,903 |
| Makefile | 7,008 |
| Shell | 6,540 |
| Dockerfile | 672 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/antithesishq/antithesis-sdk-go, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/cloudevents/sdk-go/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/golang/groupcache, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/go-tpm, github.com/google/uuid, github.com/gorilla/mux, github.com/josharian/intern, github.com/json-iterator/go
- Makefile (capture: captured)
- hack/ci/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 9
- Last updated: 2026-10-28T12:16:44Z
- Last pushed: 2026-11-16T07:09:00Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/kyma-project/eventing-publisher-proxy)
- [README](https://github.com/kyma-project/eventing-publisher-proxy/blob/main/README.md)
- [Issues](https://github.com/kyma-project/eventing-publisher-proxy/issues)
- [Releases](https://github.com/kyma-project/eventing-publisher-proxy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
