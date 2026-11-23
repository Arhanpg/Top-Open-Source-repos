# SAP/admission-webhook-runtime

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/admission-webhook-runtime](https://github.com/SAP/admission-webhook-runtime)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/admission-webhook-runtime/blob/main/README.md)
- README blob SHA: c41e3229b1ad39de2bc2aed79d168c40d9d7c489
- Repository ID: 631988239
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A generic Kubernetes admission webhook implementation framework

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:41:51+00:00

### Short excerpt (up to 100 words)

> This repository contains a generic Kubernetes admission webhook implementation framework. Consumers implement one or all of the following parameterized interfaces: // Validating webhook interface. type ValidatingWebhook[T runtime.Object] interface { ValidateCreate(ctx context.Context, obj T) error ValidateUpdate(ctx context.Context, oldObj T, newObj T) error ValidateDelete(ctx context.Context, obj T) error } // Mutating webhook interface. type MutatingWebhook[T runtime.Object] interface { MutateCreate(ctx context.Context, obj T) error MutateUpdate(ctx context.Context, oldObj T, newObj T) error } Two sorts of webhooks are supported: - **Specific (typed) webhooks** A specific webhook is one which handles exactly one resource type (such as `corev1.Pod`). Using go's new generics concept allows the

### README headings

- Kubernetes Admission Webhook Runtime
- About this project
- Documentation
- Support, Feedback, Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 38,023 |
| Makefile | 1,495 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/Masterminds/semver/v3, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading, github.com/go-openapi/swag/mangling, github.com/go-openapi/swag/netutils, github.com/go-openapi/swag/pools
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 2
- Last updated: 2026-11-10T22:33:10Z
- Last pushed: 2026-11-23T07:18:25Z
- Topics: sap-cns, sap-cs-devops

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/admission-webhook-runtime)
- [README](https://github.com/SAP/admission-webhook-runtime/blob/main/README.md)
- [Issues](https://github.com/SAP/admission-webhook-runtime/issues)
- [Releases](https://github.com/SAP/admission-webhook-runtime/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
