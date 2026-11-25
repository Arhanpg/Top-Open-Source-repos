# Azure/application-gateway-kubernetes-ingress

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/application-gateway-kubernetes-ingress](https://github.com/Azure/application-gateway-kubernetes-ingress)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/application-gateway-kubernetes-ingress/blob/master/README.md)
- README blob SHA: abdc970aa656f27c45c8504e2adb79b5a6950ed0
- README bytes captured: 6464
- README truncated at capture limit: False
- Repository ID: 146650795
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This is an ingress controller that can be run on Azure Kubernetes Service (AKS) to allow an Azure Application Gateway to act as the ingress for an AKS cluster.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T05:10:55+00:00

### Short excerpt (up to 300 words)

> Application Gateway Ingress Controller (AGIC) is a Kubernetes application, which makes it possible for Azure Kubernetes Service (AKS) customers to leverage Azure's native Application Gateway

### README headings

- Application Gateway Ingress Controller
- Changelog
- Blogs and talks
- Setup
- Usage
- How-tos
- Troubleshooting
- Frequently asked questions
- Reporting Issues
- Contributing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Application Gateway Ingress Controller

> Application Gateway Ingress Controller (AGIC) is a Kubernetes application, which makes it possible for Azure Kubernetes Service (AKS) customers to leverage Azure's native Application Gateway

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 1,115,302 |
| Shell | 15,393 |
| Makefile | 4,460 |
| CMake | 4,325 |
| Mustache | 3,908 |
| Dockerfile | 745 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/Azure/azure-container-networking, github.com/Azure/azure-sdk-for-go, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/Azure/go-autorest, github.com/Azure/go-autorest/autorest, github.com/Azure/go-autorest/autorest/adal, github.com/Azure/go-autorest/autorest/azure/auth, github.com/Azure/go-autorest/autorest/azure/cli, github.com/Azure/go-autorest/autorest/date, github.com/Azure/go-autorest/autorest/to, github.com/Azure/go-autorest/autorest/validation, github.com/Azure/go-autorest/logger, github.com/Azure/go-autorest/tracing, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/Masterminds/semver/v3, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew
- Makefile (capture: captured)
- helm/ingress-azure/Chart.yaml (capture: captured)
- scripts/e2e/go.mod (capture: captured) — dependency clues: github.com/Azure/application-gateway-kubernetes-ingress, github.com/Azure/azure-sdk-for-go, github.com/Azure/go-autorest, github.com/Azure/go-autorest/autorest, github.com/Azure/go-autorest/autorest/adal, github.com/Azure/go-autorest/autorest/azure/auth, github.com/Azure/go-autorest/autorest/azure/cli, github.com/Azure/go-autorest/autorest/date, github.com/Azure/go-autorest/autorest/to, github.com/Azure/go-autorest/autorest/validation, github.com/Azure/go-autorest/logger, github.com/Azure/go-autorest/tracing, github.com/davecgh/go-spew, github.com/dimchansky/utfbom, github.com/emicklei/go-restful/v3, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 701
- Forks at capture: 451
- Last updated: 2026-11-18T22:22:50Z
- Last pushed: 2026-11-11T14:24:25Z
- Topics: agic, aks, application-gateway, azure, go, ingress, ingress-controller, kubernetes

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/application-gateway-kubernetes-ingress)
- [README](https://github.com/Azure/application-gateway-kubernetes-ingress/blob/master/README.md)
- [Issues](https://github.com/Azure/application-gateway-kubernetes-ingress/issues)
- [Releases](https://github.com/Azure/application-gateway-kubernetes-ingress/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
