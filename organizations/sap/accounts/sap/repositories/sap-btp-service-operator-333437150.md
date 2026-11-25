# SAP/sap-btp-service-operator

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/sap-btp-service-operator](https://github.com/SAP/sap-btp-service-operator)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/sap-btp-service-operator/blob/main/README.md)
- README blob SHA: aed3ceb9b2cfdd3ff19c2cb6624320c0273b904a
- README bytes captured: 55729
- README truncated at capture limit: False
- Repository ID: 333437150
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

SAP BTP service operator enables developers to connect Kubernetes clusters to SAP BTP accounts and to consume SAP BTP services within the clusters by using Kubernetes native tools.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T04:38:06+00:00

### Short excerpt (up to 300 words)

> The SAP BTP Service To deploy the SAP The SAP BTP Service With the SAP BTP Automatic credential rotation cannot

### README headings

- SAP Business Technology Platform (SAP BTP) Service Operator for Kubernetes
- Table of Contents
- Overview and Architecture
- Prerequisites for Deployment
- Installation and Setup
- Default Access Credentials
- mTLS Access Credentials
- Using Custom Certificate Authorities
- Configuration
- Managing Access Permissions
- Limited Cache Mode
- How It Works
- Enabling Limited Cache Mode
- Configuring Multiple Subaccounts
- Subaccount for a Namespace
- Default Access Credentials
- mTLS Access Credentials
- Subaccount for a ServiceInstance Resource
- Define a new secret
- Default Access Credentials
- mTLS Access Credentials
- Configure the secret name in the `ServiceInstance` resource within the property `btpAccessCredentialsSecret`:
- Secrets Precedence
- Using the SAP BTP Service Operator
- Creating Service Instances
- Managing Service Bindings
- Structure of the ServiceBinding Custom Resource
- Procedure
- Creating a Service Binding for a Service Instance in a Different Namespace
- Service Binding Secret Formats

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview and Architecture

> The SAP BTP Service

### Getting started and usage: Installation and Setup

> To deploy the SAP

### Architecture and design: Overview and Architecture

> The SAP BTP Service

### Technology and requirements: SAP Business Technology Platform (SAP BTP) Service Operator for Kubernetes

> With the SAP BTP

### Limitations and security: Limitations

> Automatic credential rotation cannot

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 545,521 |
| Shell | 6,777 |
| Makefile | 3,248 |
| Dockerfile | 776 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: dario.cat/mergo, github.com/Masterminds/semver/v3, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading, github.com/go-openapi/swag/mangling
- Makefile (capture: captured)
- sapbtp-operator-charts/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 143
- Forks at capture: 61
- Last updated: 2026-11-06T04:58:06Z
- Last pushed: 2026-11-19T12:06:45Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/sap-btp-service-operator)
- [README](https://github.com/SAP/sap-btp-service-operator/blob/main/README.md)
- [Issues](https://github.com/SAP/sap-btp-service-operator/issues)
- [Releases](https://github.com/SAP/sap-btp-service-operator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
