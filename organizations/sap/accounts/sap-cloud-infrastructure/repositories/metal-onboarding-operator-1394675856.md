# SAP-cloud-infrastructure/metal-onboarding-operator

- Company: SAP
- GitHub account: [https://github.com/SAP-cloud-infrastructure](https://github.com/SAP-cloud-infrastructure)
- Mapping status: official-directory-listed
- Repository: [SAP-cloud-infrastructure/metal-onboarding-operator](https://github.com/SAP-cloud-infrastructure/metal-onboarding-operator)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-cloud-infrastructure/metal-onboarding-operator/blob/main/README.md)
- README blob SHA: 1f5b075f17c643cb14d209a9d6962827ed35ba94
- Repository ID: 1394675856
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Onboarding operator for the Metal-API

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:38:02+00:00

### Short excerpt (up to 100 words)

> // TODO(user): Add simple overview of use/purpose // TODO(user): An in-depth paragraph about your project and overview of use - go version v1.24.6+ - docker version 17.03+. - kubectl version v1.11.3+. - Access to a Kubernetes v1.11.3+ cluster. **Build and push your image to the location specified by `IMG`:** make docker-build docker-push IMG=<some-registry>/metal-onboarding-operator:tag **NOTE:** This image ought to be published in the personal registry you specified. And it is required to have access to pull the image from the working environment. Make sure you have the proper permission to the registry if the above commands don’t work. **Install the CRDs

### README headings

- metal-onboarding-operator
- Description
- Getting Started
- Prerequisites
- To Deploy on the cluster
- To Uninstall
- Project Distribution
- By providing a bundle with all YAML files
- By providing a Helm Chart
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 96,815 |
| Makefile | 12,519 |
| Shell | 3,432 |
| Starlark | 2,884 |
| Dockerfile | 1,658 |
| Go Template | 1,478 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: cel.dev/expr, github.com/Masterminds/semver/v3, github.com/SAP-cloud-infrastructure/metaldhcp, github.com/antlr4-go/antlr/v4, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cenkalti/backoff/v5, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/felixge/httpsnoop, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag
- Makefile (capture: captured)
- charts/metal-onboarding-operator/Chart.yaml (capture: captured)
- dev/fake-redfish/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 1
- Forks at capture: 0
- Last updated: 2026-11-11T12:47:23Z
- Last pushed: 2026-11-23T12:22:25Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-cloud-infrastructure/metal-onboarding-operator)
- [README](https://github.com/SAP-cloud-infrastructure/metal-onboarding-operator/blob/main/README.md)
- [Issues](https://github.com/SAP-cloud-infrastructure/metal-onboarding-operator/issues)
- [Releases](https://github.com/SAP-cloud-infrastructure/metal-onboarding-operator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
