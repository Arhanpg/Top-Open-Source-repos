# awslabs/amazon-eks-ami

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-eks-ami](https://github.com/awslabs/amazon-eks-ami)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/amazon-eks-ami/blob/main/README.md)
- README blob SHA: e21e2557e491a6b66ddf0aebce35b51bfd0b063f
- Repository ID: 136244218
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Packer configuration for building a custom EKS AMI

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:36:43+00:00

### Short excerpt (up to 100 words)

> This repository contains resources and configuration scripts for building a custom Amazon EKS AMI with HashiCorp Packer. This is the same configuration that Amazon EKS uses to create the official Amazon EKS-optimized AMI. **Check out the 📖 documentation to learn more.** If you are new to Amazon EKS, we recommend that you follow our Getting Started chapter in the Amazon EKS User Guide. If you already have a cluster, and you want to launch a node group with your new AMI, see [Launching Amazon EKS Worker Nodes](https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html). You must have Packer version 1.8.0 or later installed on your local system.

### README headings

- Amazon EKS AMI Build Specification
- 🚀 Getting started
- 🔢 Pre-requisites
- 👷 Building the AMI
- build an AMI with a specific Kubernetes version
- check default value and options in help doc
- 🔒 Security
- ⚖️ License Summary

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 313,177 |
| Shell | 246,076 |
| HCL | 31,495 |
| PowerShell | 15,797 |
| Makefile | 10,231 |
| Python | 3,882 |
| Dockerfile | 3,382 |
| Go Template | 1,471 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- nodeadm/go.mod (capture: captured) — dependency clues: cel.dev/cel-go, cel.dev/expr, dario.cat/mergo, github.com/antlr4-go/antlr/v4, github.com/avast/retry-go/v5, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go
- nodeadm/Makefile (capture: captured)
- .github/actions/bot/package.json (capture: captured) — dependency clues: @actions/core, @actions/github
- nodeadm/test/e2e/infra/Dockerfile (capture: captured)
- nodeadm/test/e2e/infra/requirements.txt (capture: captured) — dependency clues: mitmproxy, moto

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 2684
- Forks at capture: 1205
- Last updated: 2026-11-23T03:29:45Z
- Last pushed: 2026-11-23T02:23:03Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-eks-ami)
- [README](https://github.com/awslabs/amazon-eks-ami/blob/main/README.md)
- [Issues](https://github.com/awslabs/amazon-eks-ami/issues)
- [Releases](https://github.com/awslabs/amazon-eks-ami/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
