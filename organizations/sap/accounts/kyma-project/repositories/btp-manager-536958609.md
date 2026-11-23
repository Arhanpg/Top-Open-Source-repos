# kyma-project/btp-manager

- Company: SAP
- GitHub account: [https://github.com/kyma-project](https://github.com/kyma-project)
- Mapping status: official-directory-listed
- Repository: [kyma-project/btp-manager](https://github.com/kyma-project/btp-manager)
- Default branch: main
- README: [Open upstream README](https://github.com/kyma-project/btp-manager/blob/main/README.md)
- README blob SHA: 940ef642df2b689e9a4c149750b248277abd8064
- Repository ID: 536958609
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

BTP Manager installs SAP BTP Service Operator as a Kyma module

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:37:11+00:00

### Short excerpt (up to 100 words)

> BTP Manager is an operator for the SAP BTP service operator based on the Kubebuilder framework. It extends Kubernetes API by providing BtpOperator CustomResourceDefinition (CRD), which allows you to manage the SAP BTP service operator resource through custom resource (CR). BTP Manager and the SAP BTP service operator constitute the SAP BTP Operator module. To enable the SAP BTP Operator module from the latest release, you must install BTP Manager. For installation instructions, see Install the SAP BTP Operator module. Use SAP BTP Operator to create SAP BTP services in your Kyma cluster. To find out how to do it,

### README headings

- BTP Manager
- Overview
- Installation
- Usage
- Uninstallation
- Read More
- Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 485,179 |
| Shell | 168,065 |
| JavaScript | 11,796 |
| Makefile | 7,808 |
| Python | 4,419 |
| Dockerfile | 2,871 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/Masterminds/semver/v3, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading, github.com/go-openapi/swag/mangling
- Makefile (capture: captured)
- module-chart/chart/Chart.yaml (capture: captured)
- scripts/python/requirements.txt (capture: captured) — dependency clues: pyyaml, requests
- tests/fake-server/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 10
- Forks at capture: 25
- Last updated: 2026-11-12T07:16:14Z
- Last pushed: 2026-11-20T20:22:05Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/kyma-project/btp-manager)
- [README](https://github.com/kyma-project/btp-manager/blob/main/README.md)
- [Issues](https://github.com/kyma-project/btp-manager/issues)
- [Releases](https://github.com/kyma-project/btp-manager/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
