# kyma-project/gardener-syncer

- Company: SAP
- GitHub account: [https://github.com/kyma-project](https://github.com/kyma-project)
- Mapping status: official-directory-listed
- Repository: [kyma-project/gardener-syncer](https://github.com/kyma-project/gardener-syncer)
- Default branch: main
- README: [Open upstream README](https://github.com/kyma-project/gardener-syncer/blob/main/README.md)
- README blob SHA: a7083a42ae1af7b85a3621fa79a10521dec51b58
- Repository ID: 987494688
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:41:56+00:00

### Short excerpt (up to 100 words)

> Gardener Syncer Job is a Cronjob that regularly synchronizes the Seed data from Gardener System to Kyma Control Plane (KCP). The fetched Gardener Seed data for available cloud providers regions is stored inside a ConfigMap. For more information, see architectural docs. - Gardener Syncer Job is running on KCP. - Gardener Syncer Job is configured to connect to the Gardener System with kubeconfig file. The Gardener Syncer Job is installed and run as an ArgoCD application on KCP. For more information about the Gardener Syncer Job installation and configuration, see the installation and configuration documentation. The Gardener Syncer Job runs

### README headings

- Gardener Syncer Job
- Overview
- Prerequisites
- Installation and Configuration
- Usage
- Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 39,534 |
| Dockerfile | 1,364 |
| Makefile | 153 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/Masterminds/semver/v3, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/elliotchance/orderedmap/v3, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/fxamacker/cbor/v2, github.com/gardener/gardener, github.com/gardener/gardener/pkg/apis, github.com/gardener/oidc-webhook-authenticator, github.com/go-logr/logr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 10
- Last updated: 2026-10-21T12:38:17Z
- Last pushed: 2026-11-20T21:32:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/kyma-project/gardener-syncer)
- [README](https://github.com/kyma-project/gardener-syncer/blob/main/README.md)
- [Issues](https://github.com/kyma-project/gardener-syncer/issues)
- [Releases](https://github.com/kyma-project/gardener-syncer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
