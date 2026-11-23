# aws-controllers-k8s/eks-controller

- Company: Amazon
- GitHub account: [https://github.com/aws-controllers-k8s](https://github.com/aws-controllers-k8s)
- Mapping status: official-directory-listed
- Repository: [aws-controllers-k8s/eks-controller](https://github.com/aws-controllers-k8s/eks-controller)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-controllers-k8s/eks-controller/blob/main/README.md)
- README blob SHA: 916472e0bef5319f7fb9ef59c5cec82251317548
- Repository ID: 384186632
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ACK service controller for Amazon Elastic Kubernetes Service (EKS)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:44:56+00:00

### Short excerpt (up to 100 words)

> This repository contains source code for the AWS Controllers for Kubernetes (ACK) service controller for Amazon EKS. Please [log issues][ack-issues] and feedback on the main AWS Controllers for Kubernetes Github project. To install the `eks-controller` on your cluster, follow the the Currently, the `eks-controller` is GA and supports the following resources: - `Cluster` - `Nodegroup` - `FargateProfile` - `Addon` - `PodIdentityAssociation` - `AccessEntry` A detailed list of the resources supported specifications can be found in the For some resources, the `eks-controller` supports annotations to customize the behavior of the controller. The following annotations are supported: - **Nodegroup** - `eks.services.k8s.aws/desired-size-managed-by`: used

### README headings

- ACK service controller for Amazon Elastic Kubernetes Service (EKS)
- Getting started
- Annotations
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 185,692 |
| Python | 132,587 |
| Go Template | 9,285 |
| Smarty | 7,968 |
| Makefile | 857 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws-controllers-k8s/ec2-controller, github.com/aws-controllers-k8s/iam-controller, github.com/aws-controllers-k8s/kms-controller, github.com/aws-controllers-k8s/runtime, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/eks, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/beorn7/perks, github.com/cenkalti/backoff/v4
- Makefile (capture: captured)
- helm/Chart.yaml (capture: captured)
- test/e2e/requirements.txt (capture: captured) — dependency clues: acktest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 48
- Forks at capture: 61
- Last updated: 2026-11-10T22:44:27Z
- Last pushed: 2026-11-10T21:44:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-controllers-k8s/eks-controller)
- [README](https://github.com/aws-controllers-k8s/eks-controller/blob/main/README.md)
- [Issues](https://github.com/aws-controllers-k8s/eks-controller/issues)
- [Releases](https://github.com/aws-controllers-k8s/eks-controller/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
