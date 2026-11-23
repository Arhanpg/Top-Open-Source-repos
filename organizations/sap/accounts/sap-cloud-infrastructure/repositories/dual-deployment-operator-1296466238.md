# SAP-cloud-infrastructure/dual-deployment-operator

- Company: SAP
- GitHub account: [https://github.com/SAP-cloud-infrastructure](https://github.com/SAP-cloud-infrastructure)
- Mapping status: official-directory-listed
- Repository: [SAP-cloud-infrastructure/dual-deployment-operator](https://github.com/SAP-cloud-infrastructure/dual-deployment-operator)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-cloud-infrastructure/dual-deployment-operator/blob/main/README.md)
- README blob SHA: b11f8c999fd87e2f9a9ef1ec0898736f7bc14dd4
- Repository ID: 1296466238
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Kubernetes operator that deploys split host/remote helm chart/kustomization in Gardener environments, rendering a Helm chart or kustomize source per operator and applying each half to its target cluster via server-side apply.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:37:50+00:00

### Short excerpt (up to 100 words)

> A Kubernetes operator for **Gardener** environments that deploys a single Helm chart or kustomize source across **two clusters at once** — the seed (in-cluster) and its shoot (remote) — from one `DualDeploymentOperator` custom resource. You point it at a source, tell it which namespace to use on the shoot, and give it credentials to reach the shoot. On every reconcile it renders the source **twice** (once per cluster), applies your transformations, and server-side-applies each render to its target cluster. It tracks per-resource health, drift-corrects on a periodic reconcile, and cleans both clusters up on deletion. Splitting an operator's manifests into

### README headings

- dual-deployment-operator
- Why
- How it works
- Architecture
- Install
- Usage
- Helm source
- Kustomize source
- Transformations (optional)
- Private sources
- Checking status
- Deleting
- Local development
- point at a specific kubeconfig:
- or:
- Documentation
- Status
- Support, Feedback, Contributing
- Security / Disclosure
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 662,987 |
| Makefile | 18,346 |
| Dockerfile | 8,058 |
| Shell | 4,806 |
| Go Template | 2,292 |
| Nix | 442 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: cel.dev/expr, dario.cat/mergo, github.com/Azure/go-ansiterm, github.com/BurntSushi/toml, github.com/MakeNowJust/heredoc, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/Masterminds/squirrel, github.com/Microsoft/go-winio, github.com/ProtonMail/go-crypto, github.com/antlr4-go/antlr/v4, github.com/asaskevich/govalidator, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cenkalti/backoff/v5, github.com/cespare/xxhash/v2, github.com/chai2010/gettext-go, github.com/cloudflare/circl, github.com/cyphar/filepath-securejoin
- Makefile (capture: captured)
- chart/Chart.yaml (capture: captured)
- internal/source/testdata/charts/demo/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 1
- Last updated: 2026-11-11T13:19:46Z
- Last pushed: 2026-11-21T16:09:36Z
- Topics: cloud-native, controller, gardener, go, helm, kubernetes, kubernetes-operator, kustomize, operator, server-side-apply

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-cloud-infrastructure/dual-deployment-operator)
- [README](https://github.com/SAP-cloud-infrastructure/dual-deployment-operator/blob/main/README.md)
- [Issues](https://github.com/SAP-cloud-infrastructure/dual-deployment-operator/issues)
- [Releases](https://github.com/SAP-cloud-infrastructure/dual-deployment-operator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
