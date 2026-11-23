# aws/amazon-cloudwatch-agent-operator

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-cloudwatch-agent-operator](https://github.com/aws/amazon-cloudwatch-agent-operator)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-cloudwatch-agent-operator/blob/main/README.md)
- README blob SHA: 706926de2d5502561b708075bbf375887ef9acc0
- Repository ID: 673479242
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Amazon CloudWatch Agent Operator is software developed to manage the CloudWatch Agent on kubernetes.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:02:00+00:00

### Short excerpt (up to 100 words)

> The Amazon CloudWatch Agent Operator is software developed to manage the CloudWatch Agent on kubernetes. Supported Languages: - Java - Python - .NET - NodeJS This repo is based off of the OpenTelemetry Operator - Image can be built using `make container` - Deploy kubernetes objects to your cluster `make deploy` 1. Have an existing kubernetes cluster, such as minikube 2. Install cert-manager on your cluster kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.0/cert-manager.yaml 1. Set a shortcut for kubectl for the operator namespace kubectl config set-context --current --namespace=amazon-cloudwatch 2. Look at all resources created kubectl get all 3. Look at the manager pod

### README headings

- Amazon CloudWatch Agent Operator
- Build and Deployment
- Pre requisites
- Getting started
- Helpful tools
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 1,866,863 |
| Makefile | 12,764 |
| Shell | 5,651 |
| HCL | 5,648 |
| Dockerfile | 2,253 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, dario.cat/mergo, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/compute/armcompute/v5, github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/network/armnetwork/v4, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/Code-Hex/go-generics-cache, github.com/Microsoft/go-winio, github.com/alecthomas/units, github.com/armon/go-metrics, github.com/asaskevich/govalidator, github.com/aws/aws-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds
- Makefile (capture: captured)
- cmd/amazon-cloudwatch-agent-target-allocator/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 33
- Forks at capture: 45
- Last updated: 2026-11-12T12:42:25Z
- Last pushed: 2026-11-17T14:07:52Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-cloudwatch-agent-operator)
- [README](https://github.com/aws/amazon-cloudwatch-agent-operator/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-cloudwatch-agent-operator/issues)
- [Releases](https://github.com/aws/amazon-cloudwatch-agent-operator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
