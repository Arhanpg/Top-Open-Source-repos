# SAP/kafka-operator

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/kafka-operator](https://github.com/SAP/kafka-operator)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/kafka-operator/blob/main/README.md)
- README blob SHA: ca844146076a0db06f5c905771c90265d85a5741
- README bytes captured: 12536
- README truncated at capture limit: False
- Repository ID: 1355014307
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Kubernetes operator to manage Kafka resources declaratively

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T23:46:05+00:00

### Short excerpt (up to 300 words)

> A Kubernetes operator to The recommended deployment method If you find any

### README headings

- kafka-operator
- About this project
- Usage
- Topic custom resource
- Spec fields and defaulting
- `spec.name`
- `spec.partitions`
- `spec.replicas`
- `spec.configs`
- `spec.connectionSecretRef`
- Status fields
- `status.state`
- `status.conditions`
- `status.observedGeneration`
- `status.lastObservedAt`
- `status.details`
- Connection secret
- Format
- list of seed brokers, at least one entry is required
- PEM-encoded CA bundle used to verify the broker certificates (optional)
- PEM-encoded client certificate for mTLS (optional)
- PEM-encoded private key belonging to clientCertificate (optional)
- SASL mechanisms (optional)
- Requirements and Setup
- Documentation
- Support, Feedback, Contributing
- Security / Disclosure
- Code of Conduct
- Licensing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: About this project

> A Kubernetes operator to

### Technology and requirements: Requirements and Setup

> The recommended deployment method

### Limitations and security: Security / Disclosure

> If you find any

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 47,628 |
| Makefile | 4,267 |
| Dockerfile | 1,024 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/fatih/color, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading, github.com/go-openapi/swag/mangling
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 1
- Last updated: 2026-11-10T22:10:30Z
- Last pushed: 2026-11-23T07:19:22Z
- Topics: sap-cns, sap-cs-devops

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/kafka-operator)
- [README](https://github.com/SAP/kafka-operator/blob/main/README.md)
- [Issues](https://github.com/SAP/kafka-operator/issues)
- [Releases](https://github.com/SAP/kafka-operator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
