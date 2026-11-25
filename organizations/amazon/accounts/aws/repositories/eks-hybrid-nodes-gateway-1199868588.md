# aws/eks-hybrid-nodes-gateway

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/eks-hybrid-nodes-gateway](https://github.com/aws/eks-hybrid-nodes-gateway)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/eks-hybrid-nodes-gateway/blob/main/README.md)
- README blob SHA: 8139db1f95919f4a92e7215962105b265e3c2aab
- README bytes captured: 11779
- README truncated at capture limit: False
- Repository ID: 1199868588
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Automate networking between your Amazon EKS cluster VPC and Kubernetes pods running on Amazon EKS Hybrid Nodes

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:49:22+00:00

### Short excerpt (up to 300 words)

> Label 2 nodes for ┌─── AWS VPC ───────────────────────────────────┐ EKS cluster with Cilium See CONTRIBUTING for more

### README headings

- EKS Hybrid Nodes Gateway
- Architecture
- Prerequisites
- Build
- Build for both architectures
- Run unit tests
- Deploy
- 1. Build and Push the Image
- 2. Install with Helm
- Package and Push the Chart
- Package chart to .tgz
- Push to OCI registry
- Uninstall
- Configuration
- Leader Election & Failover
- Node Reconciler
- Monitoring
- Project Structure
- Connectivity Conformance Tests
- Run default tests (all except LoadBalancer)
- Run specific tests
- Include LoadBalancer test (adds ~3-5 min for NLB provisioning)
- Skip cleanup for debugging
- Verbose output
- End-to-End Tests
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: 2. Install with Helm

> Label 2 nodes for

### Architecture and design: Architecture

> ┌─── AWS VPC ───────────────────────────────────┐

### Technology and requirements: Prerequisites

> EKS cluster with Cilium

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 147,095 |
| Shell | 42,212 |
| Makefile | 4,996 |
| Go Template | 2,043 |
| Dockerfile | 290 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: dario.cat/mergo, github.com/Azure/go-ansiterm, github.com/BurntSushi/toml, github.com/MakeNowJust/heredoc, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/Masterminds/squirrel, github.com/ProtonMail/go-crypto, github.com/ProtonMail/gopenpgp/v3, github.com/asaskevich/govalidator, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/internal/v4a
- Makefile (capture: captured)
- charts/eks-hybrid-nodes-gateway/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 18
- Forks at capture: 8
- Last updated: 2026-10-22T03:23:19Z
- Last pushed: 2026-11-14T02:06:17Z
- Topics: aws, eks, helm, hybrid, hybrid-cloud, kubernetes, kubernetes-deployment

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/eks-hybrid-nodes-gateway)
- [README](https://github.com/aws/eks-hybrid-nodes-gateway/blob/main/README.md)
- [Issues](https://github.com/aws/eks-hybrid-nodes-gateway/issues)
- [Releases](https://github.com/aws/eks-hybrid-nodes-gateway/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
