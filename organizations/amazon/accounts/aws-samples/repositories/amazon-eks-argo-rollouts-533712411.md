# aws-samples/amazon-eks-argo-rollouts

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-eks-argo-rollouts](https://github.com/aws-samples/amazon-eks-argo-rollouts)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-eks-argo-rollouts/blob/main/README.md)
- README blob SHA: 968f0554d09d565b1e8d76a0c4cd992564adb14d
- README bytes captured: 4082
- README truncated at capture limit: False
- Repository ID: 533712411
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Sample code for blue/green and canary deployments on Amazon EKS using AWS App Mesh/Istio and Argo Rollouts

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:46:12+00:00

### Short excerpt (up to 300 words)

> helm repo add eks An active AWS account. See CONTRIBUTING for more

### README headings

- Progressive Delivery in Amazon EKS using Argo Rollouts
- Prerequisites
- Setup
- Create EKS Cluster and its dependencies (VPC etc)
- Set your local environment variables
- Create the App Mesh and namespace
- Create the virtual gateway expose the API endpoint outside the cluster
- Install Appmesh Prometheus
- Setup Grafana
- Build Docker image and push to ECR
- Blue/Green Deployment
- Canary Deployment
- Clean up
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install Appmesh Prometheus

> helm repo add eks

### Technology and requirements: Prerequisites

> An active AWS account.

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 7,219 |
| Python | 4,964 |
| Dockerfile | 1,569 |
| Shell | 111 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- app/v1/demo-app/Dockerfile (capture: captured)
- app/v1/demo-app/requirements.txt (capture: captured) — dependency clues: Flask-API, flask
- app/v2-fix/demo-app/Dockerfile (capture: captured)
- app/v2-fix/demo-app/requirements.txt (capture: captured) — dependency clues: Flask-API, flask
- app/v2/demo-app/Dockerfile (capture: captured)
- app/v2/demo-app/requirements.txt (capture: captured) — dependency clues: Flask-API, flask

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 10
- Forks at capture: 2
- Last updated: 2025-07-04T03:05:35Z
- Last pushed: 2023-05-12T05:28:17Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-eks-argo-rollouts)
- [README](https://github.com/aws-samples/amazon-eks-argo-rollouts/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-eks-argo-rollouts/issues)
- [Releases](https://github.com/aws-samples/amazon-eks-argo-rollouts/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
