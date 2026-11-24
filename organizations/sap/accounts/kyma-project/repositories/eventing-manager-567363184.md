# kyma-project/eventing-manager

- Company: SAP
- GitHub account: [https://github.com/kyma-project](https://github.com/kyma-project)
- Mapping status: official-directory-listed
- Repository: [kyma-project/eventing-manager](https://github.com/kyma-project/eventing-manager)
- Default branch: main
- README: [Open upstream README](https://github.com/kyma-project/eventing-manager/blob/main/README.md)
- README blob SHA: 382b76d7a3fd7cb9b046aaab14647f67ad4d261d
- Repository ID: 567363184
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Eventing Operator installs Eventing as Kyma module

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:41:48+00:00

### Short excerpt (up to 100 words)

> Eventing Manager is a standard Kubernetes operator that observes the state of Eventing resources and reconciles their state according to the desired state. It uses Controllers, which provide a reconcile function responsible for synchronizing resources until the desired state is reached in the cluster. This project is scaffolded using Kubebuilder. You need a Kubernetes cluster to run against. You can use k3d to get a local cluster for testing, or run against a remote cluster. 1. To install the latest version of the Eventing Manager in your cluster, run: kubectl apply -f https://github.com/kyma-project/eventing-manager/releases/latest/download/eventing-manager.yaml 2. To install the latest version of

### README headings

- Eventing Manager
- Status
- Overview
- Get Started
- Install
- Development
- Prerequisites
- Run Eventing Manager Locally
- Run Tests
- Linting
- Modify the API Definitions
- Build Container Images
- Deployment
- Deploy in the Cluster
- Undeploy Eventing Manager
- Uninstall CRDs
- End-to-End Tests
- Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 1,406,239 |
| Shell | 41,052 |
| Makefile | 23,206 |
| Dockerfile | 2,811 |
| JavaScript | 1,707 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/antithesishq/antithesis-sdk-go, github.com/avast/retry-go/v3, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cespare/xxhash/v2, github.com/chigopher/pathlib, github.com/cloudevents/sdk-go/protocol/nats/v2, github.com/cloudevents/sdk-go/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/gogo/protobuf, github.com/golang/protobuf
- Makefile (capture: captured)
- hack/ci/Makefile (capture: captured)
- hack/e2e/sink/Dockerfile (capture: captured)
- hack/e2e/sink/go.mod (capture: captured) — dependency clues: github.com/cloudevents/sdk-go/v2, github.com/gorilla/mux, github.com/json-iterator/go, github.com/modern-go/concurrent, github.com/modern-go/reflect2, go.uber.org/atomic, go.uber.org/multierr, go.uber.org/zap

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 21
- Last updated: 2026-11-06T09:20:34Z
- Last pushed: 2026-11-16T07:08:52Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/kyma-project/eventing-manager)
- [README](https://github.com/kyma-project/eventing-manager/blob/main/README.md)
- [Issues](https://github.com/kyma-project/eventing-manager/issues)
- [Releases](https://github.com/kyma-project/eventing-manager/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
