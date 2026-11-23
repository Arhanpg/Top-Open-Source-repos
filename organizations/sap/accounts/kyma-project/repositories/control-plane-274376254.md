# kyma-project/control-plane

- Company: SAP
- GitHub account: [https://github.com/kyma-project](https://github.com/kyma-project)
- Mapping status: official-directory-listed
- Repository: [kyma-project/control-plane](https://github.com/kyma-project/control-plane)
- Default branch: main
- README: [Open upstream README](https://github.com/kyma-project/control-plane/blob/main/README.md)
- README blob SHA: 4b569154646f8111167b539a03173da9c938c0b9
- Repository ID: 274376254
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A flexible and easy way to manage Kyma Runtimes

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:48:56+00:00

### Short excerpt (up to 100 words)

> This repository has been deprecated and archived on Feb 11th, 2025. For available replacements, see the following: * Kyma Environment Broker (KEB): https://github.com/kyma-project/kyma-environment-broker * Kyma Infrastructure Manager (KIM): https://github.com/kyma-project/infrastructure-manager Kyma Control Plane (KCP) is a central system to manage Kyma Runtimes. For more information on KCP and its components, read the KCP documentation. - Docker - Minikube 1.6.2 - kubectl 1.16.3 - Kyma CLI stable Kyma Control Plane depends on Kyma and Compass. If you want to deploy only the Reconciler for testing purposes, run: cd tools/reconciler make deploy-reconciler See the Contributing Rules. See the Code of Conduct document. See

### README headings

- :warning: **Archived**
- Kyma Control Plane
- Overview
- Prerequisites
- Dependencies
- Reconciler
- Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 673,674 |
| Shell | 19,578 |
| Makefile | 12,993 |
| Mustache | 12,215 |
| PLpgSQL | 6,466 |
| Dockerfile | 2,088 |
| Smarty | 1,925 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- components/provisioner/Dockerfile (capture: captured)
- components/provisioner/go.mod (capture: captured) — dependency clues: github.com/99designs/gqlgen, github.com/Azure/go-ansiterm, github.com/Masterminds/semver, github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/agnivade/levenshtein, github.com/avast/retry-go, github.com/beorn7/perks, github.com/cenkalti/backoff/v4, github.com/cespare/xxhash/v2, github.com/containerd/cgroups, github.com/containerd/containerd, github.com/cpuguy83/go-md2man/v2, github.com/davecgh/go-spew, github.com/docker/distribution, github.com/docker/docker, github.com/docker/go-connections, github.com/docker/go-units, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch
- components/provisioner/Makefile (capture: captured)
- components/reconciler/go.mod (capture: captured) — dependency clues: github.com/deepmap/oapi-codegen, github.com/golang/mock, github.com/pkg/errors, github.com/stretchr/testify
- components/reconciler/makefile (capture: captured)
- components/schema-migrator/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 16
- Forks at capture: 111
- Last updated: 2026-02-08T22:02:19Z
- Last pushed: 2025-02-11T13:59:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/kyma-project/control-plane)
- [README](https://github.com/kyma-project/control-plane/blob/main/README.md)
- [Issues](https://github.com/kyma-project/control-plane/issues)
- [Releases](https://github.com/kyma-project/control-plane/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
