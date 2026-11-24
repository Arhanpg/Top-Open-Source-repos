# mindsphere/product-edc-fork

- Company: Siemens
- GitHub account: [https://github.com/mindsphere](https://github.com/mindsphere)
- Mapping status: official-project-linked
- Repository: [mindsphere/product-edc-fork](https://github.com/mindsphere/product-edc-fork)
- Default branch: develop
- README: [Open upstream README](https://github.com/mindsphere/product-edc-fork/blob/develop/README.md)
- README blob SHA: c9cf6eb50c2baf2ad4b838b95e68a591d9c66f51
- Repository ID: 504026930
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Repository for Catena-X specific eclipse dataspace connector apps

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:43:06+00:00

### Short excerpt (up to 100 words)

> Container images and deployments of the Eclipse Dataspace Connector open source project. · · The project provides pre-built control- and data-plane docker images and helm charts of the Eclipse DataSpaceConnector Project. The eclipse data space connector is split up into Control-Plane and Data-Plane, whereas the Control-Plane functions as administration layer and has responsibility of resource management, contract negotiation and administer data transfer. The Data-Plane does the heavy lifting of transferring and receiving data streams. Depending on your environment there are different derivatives of the control-plane prepared: * edc-controlplane-memory with dependency onto * Azure Key Vault * edc-controlplane-postgresql with dependency onto

### README headings

- About The Project
- Inventory
- Getting Started
- Build
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 337,468 |
| Smarty | 7,228 |
| Dockerfile | 6,523 |
| Gherkin | 5,222 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: apache-commons-pool-sql, api-configuration, api-core, asset-api, asset-index-sql, assetindex-cosmos, auth-basic, auth-spi, auth-tokenbased, awaitility, aws-s3, aws-test, azure-eventgrid, azure-eventgrid-config, azure-sdk-bom, azure-test, azure-vault, bcpkix-jdk15on, blob-core, blob-operator
- edc-controlplane/pom.xml (capture: captured) — dependency clues: edc-controlplane, product-edc-parent
- edc-dataplane/pom.xml (capture: captured) — dependency clues: edc-dataplane, product-edc-parent
- edc-extensions/pom.xml (capture: captured) — dependency clues: edc-extensions, product-edc-parent
- edc-tests/pom.xml (capture: captured) — dependency clues: awaitility, business-partner-validation, cucumber-java, cucumber-junit-platform-engine, cx-oauth2, data-encryption, dataplane-selector-configuration, edc-controlplane-base, edc-controlplane-memory, edc-controlplane-postgresql, edc-controlplane-postgresql-hashicorp-vault, edc-dataplane-azure-vault, edc-dataplane-base, edc-dataplane-hashicorp-vault, edc-tests, gson, hashicorp-vault, httpclient, jacoco-maven-plugin, junit-jupiter-api
- charts/edc-controlplane/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: True
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2022-06-28T06:27:39Z
- Last pushed: 2022-09-20T05:32:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/mindsphere/product-edc-fork)
- [README](https://github.com/mindsphere/product-edc-fork/blob/develop/README.md)
- [Issues](https://github.com/mindsphere/product-edc-fork/issues)
- [Releases](https://github.com/mindsphere/product-edc-fork/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
