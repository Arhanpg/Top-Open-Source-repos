# kyma-project/docker-registry

- Company: SAP
- GitHub account: [https://github.com/kyma-project](https://github.com/kyma-project)
- Mapping status: official-directory-listed
- Repository: [kyma-project/docker-registry](https://github.com/kyma-project/docker-registry)
- Default branch: main
- README: [Open upstream README](https://github.com/kyma-project/docker-registry/blob/main/README.md)
- README blob SHA: 66e907c01ecdea2cc652df1fa6e23a286d3a3295
- Repository ID: 788884886
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:41:43+00:00

### Short excerpt (up to 100 words)

> The Docker Registry module provides a lightweight, open-source Docker registry for storing and distributing container images in the Kubernetes environment. You can use it in self-contained development clusters or testing environments, so you can test deployments in an isolated system. The Docker Registry module comes with a dedicated Kubernetes operator for effortless installation and upgrades. It manages the lifecycle of the Docker Registry resources according to the desired specification expressed through a dedicated `Dockerregistry` custom resource (CR). Read more about configuration options in the user documentation. 1. Create the `docker-registry` namespace: kubectl create namespace docker-registry 2. Apply the following script

### README headings

- Docker Registry
- Status
- Overview
- Install
- Usage
- Development
- Prerequisites
- Installation in the k3d Cluster Using Make Targets
- Using Docker Registry Operator
- Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 280,379 |
| Makefile | 20,028 |
| Shell | 6,410 |
| Mustache | 2,577 |
| JavaScript | 1,710 |
| Dockerfile | 1,277 |
| Go Template | 292 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: dario.cat/mergo, github.com/Azure/go-ansiterm, github.com/BurntSushi/toml, github.com/MakeNowJust/heredoc, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/Masterminds/squirrel, github.com/asaskevich/govalidator, github.com/avast/retry-go, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cespare/xxhash/v2, github.com/chai2010/gettext-go, github.com/containerd/containerd, github.com/containerd/errdefs, github.com/containerd/log, github.com/containerd/platforms, github.com/cyphar/filepath-securejoin, github.com/davecgh/go-spew
- Makefile (capture: captured)
- hack/Makefile (capture: captured)
- components/operator/Dockerfile (capture: captured)
- components/operator/Makefile (capture: captured)
- components/registry-init/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3
- Forks at capture: 15
- Last updated: 2026-10-12T12:04:06Z
- Last pushed: 2026-11-17T08:12:57Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/kyma-project/docker-registry)
- [README](https://github.com/kyma-project/docker-registry/blob/main/README.md)
- [Issues](https://github.com/kyma-project/docker-registry/issues)
- [Releases](https://github.com/kyma-project/docker-registry/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
