# aws/secrets-store-csi-driver-provider-aws

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/secrets-store-csi-driver-provider-aws](https://github.com/aws/secrets-store-csi-driver-provider-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/secrets-store-csi-driver-provider-aws/blob/main/README.md)
- README blob SHA: b30bc1b5163d4e4bc559b7c64250a1fa29071282
- README bytes captured: 32536
- README truncated at capture limit: False
- Repository ID: 358007078
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The AWS provider for the Secrets Store CSI Driver allows you to fetch secrets from AWS Secrets Manager and AWS Systems Manager Parameter Store, and mount them into Kubernetes pods.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T06:04:59+00:00

### Short excerpt (up to 300 words)

> If you install the Amazon Elastic Kubernetes Service The AWS Secrets Manager

### README headings

- AWS Secrets Manager and Config Provider for Secret Store CSI Driver
- Installation
- Requirements
- Installing the AWS Secrets Manager and Config Provider (ASCP)
- Option 1: Using helm
- Option 2: Using kubectl
- Separate CSI Driver Installation
- Usage
- Option 1: Using IAM Roles For Service Accounts (IRSA)
- Option 2: Using EKS Pod Identity
- Troubleshooting
- SecretProviderClass options
- Additional Considerations
- Rotation
- Automated Failover Regions
- Using EKS Pod Identity to Access Cross-Account AWS Resources
- Role-chaining
- 1. The target role
- 2. The base role
- 3. The SecretProviderClass
- Private Builds
- Configure the Underlying Secrets Manager Client to Use FIPS Endpoint
- Client-Side Rate-Limitting to Kubernetes API server
- HTTP timeout for Pod Identity
- Driver Writes Secrets
- Security Considerations
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Separate CSI Driver Installation

> If you install the

### Technology and requirements: Requirements

> Amazon Elastic Kubernetes Service

### Limitations and security: Security Considerations

> The AWS Secrets Manager

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 278,892 |
| Shell | 25,825 |
| Python | 14,843 |
| Makefile | 1,949 |
| Go Template | 1,777 |
| Dockerfile | 1,065 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/secretsmanager, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/ssm, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/fxamacker/cbor/v2, github.com/go-logr/logr
- Makefile (capture: captured)
- charts/secrets-store-csi-driver-provider-aws/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 598
- Forks at capture: 177
- Last updated: 2026-11-21T04:50:57Z
- Last pushed: 2026-11-22T23:04:47Z
- Topics: aws, aws-secrets-manager, csi-driver, golang, kubernetes, secret

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/secrets-store-csi-driver-provider-aws)
- [README](https://github.com/aws/secrets-store-csi-driver-provider-aws/blob/main/README.md)
- [Issues](https://github.com/aws/secrets-store-csi-driver-provider-aws/issues)
- [Releases](https://github.com/aws/secrets-store-csi-driver-provider-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
