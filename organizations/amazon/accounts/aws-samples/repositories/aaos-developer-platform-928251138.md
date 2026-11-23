# aws-samples/aaos-developer-platform

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/aaos-developer-platform](https://github.com/aws-samples/aaos-developer-platform)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/aaos-developer-platform/blob/main/README.md)
- README blob SHA: fb228a04bd007b4a83010992c545ac76ac16a26e
- Repository ID: 928251138
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:30:46+00:00

### Short excerpt (up to 100 words)

> This project aims to provide a solution to build, run and test Android Automotive OS in the Cloud. The project relies on Android Cuttlefish Device to run virtual Android devices. The devices run in a Kubernetes cluster using Karpenter to provide the underlying infrastructure. The project comes with a number of Dockerfiles inside the `ci-images` folder. Those dockerfiles can be used to build the container images needed to run Cuttlefish as a container. * `aws-cli-kubectl-adb` contains a Dockerfile for a container that can be used in a CI/CD pipeline to interact with AWS services, a Kubernetes cluster to provision a

### README headings

- AAOS Developer platform on EKS with Karpenter
- Motivation
- Requirements
- Create an EKS Cluster using Terraform
- Deploy your first Cuttlefish device
- Terraform Cleanup  (Optional)
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 11,708 |
| Dockerfile | 3,453 |
| Shell | 836 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- ci-images/aws-cli-kubectl-adb/Dockerfile (capture: captured)
- ci-images/base-cuttlefish/Dockerfile (capture: captured)
- ci-images/target-cuttlefish/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 16
- Forks at capture: 1
- Last updated: 2026-07-07T21:42:59Z
- Last pushed: 2025-06-16T09:57:22Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/aaos-developer-platform)
- [README](https://github.com/aws-samples/aaos-developer-platform/blob/main/README.md)
- [Issues](https://github.com/aws-samples/aaos-developer-platform/issues)
- [Releases](https://github.com/aws-samples/aaos-developer-platform/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
