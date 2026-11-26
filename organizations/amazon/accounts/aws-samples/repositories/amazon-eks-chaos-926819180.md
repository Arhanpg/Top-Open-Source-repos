# aws-samples/amazon-eks-chaos

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-eks-chaos](https://github.com/aws-samples/amazon-eks-chaos)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-eks-chaos/blob/main/README.md)
- README blob SHA: 650de812f7a9957065a9319741f8e61279be1fc2
- README bytes captured: 25755
- README truncated at capture limit: False
- Repository ID: 926819180
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:56:11+00:00

### Short excerpt (up to 300 words)

> We will deploy sample A local machine which See CONTRIBUTING for more

### README headings

- Running chaos experiments on microservices in Amazon EKS using AWS Fault Injection Simulator with ChaosMesh and LitmusChaos
- Prerequisites
- Instructions
- Step 1 - Deploy EKS Cluster
- 1.1 - Clone this Github to Local
- 1.2 - Create the VPC and EKS Cluster with ArgoCD
- Step 2 - Install application
- Step 3 - Install Chaos Mesh
- 3.1 - Add chaos mesh repo to helm
- 3.2 - Install Chaos Mesh with containerd runtime
- 3.3 - Verify the installations
- Step 4 - Install  Litmus Chaos
- 4.1 - Add Litmus helm repo
- 4.2 - Install Litmus Mesh
- 4.3 - Verify the installations, it takes a few mins for pod set up
- Step 4.4 - Install LitmusChaos Operator where it installs all the CRDs required for litmus
- Step 5 - Set Up AWS Fault injection Service (FIS)
- 5.1 - Create FIS role
- 5.2 - Create CloudWatch Log group for storing fault injection experiment logs
- 5.3 - Grant FIS role EKS RBAC access
- This cluster role binding allows anyone in the "manager" group to read secrets in any namespace.
- This cluster role binding allows anyone in the "manager" group to read secrets in any namespace.
- 5.4 - Create EKS Cluster Access entry for fis-role:
- Step 6 - Create FIS experiment template - Litmus Chaos
- 6.1 - Create pod-http-reset-peer experiment resource in the namespace where application is deployed.
- 6.2 - Grant pod-http-reset-peer chaos minimal RBAC permission
- 6.3 - Create FIS experiment template
- 6.4 - Run FIS fault injections
- Step 7 - Create FIS experiment template - Chaos-Mesh
- 7.1 - Get application pod label and container name

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Step 2 - Install application

> We will deploy sample

### Technology and requirements: Prerequisites

> A local machine which

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 24,159 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 9
- Forks at capture: 3
- Last updated: 2026-06-25T06:19:45Z
- Last pushed: 2026-03-03T10:07:37Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-eks-chaos)
- [README](https://github.com/aws-samples/amazon-eks-chaos/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-eks-chaos/issues)
- [Releases](https://github.com/aws-samples/amazon-eks-chaos/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
