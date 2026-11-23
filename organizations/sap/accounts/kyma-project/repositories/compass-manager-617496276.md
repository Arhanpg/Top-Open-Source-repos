# kyma-project/compass-manager

- Company: SAP
- GitHub account: [https://github.com/kyma-project](https://github.com/kyma-project)
- Mapping status: official-directory-listed
- Repository: [kyma-project/compass-manager](https://github.com/kyma-project/compass-manager)
- Default branch: main
- README: [Open upstream README](https://github.com/kyma-project/compass-manager/blob/main/README.md)
- README blob SHA: 9f4ca5fd8dfb5d91a8f870039a74b5672ee27ce9
- Repository ID: 617496276
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Manager for the compass module

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:48:53+00:00

### Short excerpt (up to 100 words)

> Compass Manager **will be** a new Control Plane component. Build using Kubebuilder framework. It's main responsibilities **will be**: - registering Kyma runtimes in the Compass Director - creating secret on client cluster with the Compass Runtime configuration - Golang - minimum version is 1.20. - Kyma Custom Resource Definition present on cluster. - Access to a k8s cluster. - `kcp-system` namespace on the k8s cluster - k3d to get a local cluster for testing, or run against a remote cluster. - kubectl - kubebuilder 1. Clone the project. git clone https://github.com/kyma-project/compass-manager.git && cd compass-manager/ 2. Set the `compass-manager` image name.

### README headings

- Compass Manager
- Overview
- Prerequisites
- Usage
- Configuration Envs
- Development
- Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 125,940 |
| Makefile | 7,701 |
| Dockerfile | 1,457 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: dario.cat/mergo, github.com/99designs/gqlgen, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/agnivade/levenshtein, github.com/asaskevich/govalidator, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 14
- Last updated: 2026-10-21T04:50:10Z
- Last pushed: 2026-11-18T04:35:29Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/kyma-project/compass-manager)
- [README](https://github.com/kyma-project/compass-manager/blob/main/README.md)
- [Issues](https://github.com/kyma-project/compass-manager/issues)
- [Releases](https://github.com/kyma-project/compass-manager/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
