# aws-samples/amazon-eks-ami-rhel

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-eks-ami-rhel](https://github.com/aws-samples/amazon-eks-ami-rhel)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-eks-ami-rhel/blob/main/README.md)
- README blob SHA: 813a8e36f78d8aaba3ee34eb4eaa983efc49bb3c
- README bytes captured: 7573
- README truncated at capture limit: False
- Repository ID: 635458676
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This is a Red Hat Enterprise Linux specific forked version of the official awslabs amazon-eks-ami repository.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:42:12+00:00

### Short excerpt (up to 300 words)

> This library is licensed If you are new For security issues or

### README headings

- Amazon EKS RHEL AMI Build Specification
- 🚀 Getting started
- 🔢 Pre-requisites
- 🪪 Minimal Packer IAM Permissions
- ⚙️ Installing Packer in CloudShell
- 🗂️ Cloning the Github repository
- 👷 Building the AMI
- Example for building an AMI with the latest Kubernetes version and the latest RHEL 8.9 AMI. This would use all variables stored in the variables-default.json file.
- Example for building an AMI with the latest Kubernetes version and the latest RHEL 8.9 AMI in us-gov-east-1
- Example for building an AMI off of the latest RHEL 9.0.0 AMI in us-east-2 region
- Example for building a customized DISA STIG compliant AMI, owned by a specific AWS Account in AWS GovCloud us-gov-east-1 region, with binaries stored in a private S3 bucket, an IAM instance profile attached, a user data script to install the AWS Systems Manager agent, and using AWS Systems Manager Session Manager for Packer terminal access.
- Check default value and options in help doc
- 🔒 Security
- ⚖️ License Summary
- 📝 Legal Disclaimer

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: ⚖️ License Summary

> This library is licensed

### Getting started and usage: 🚀 Getting started

> If you are new

### Limitations and security: 🔒 Security

> For security issues or

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 235,879 |
| Shell | 140,228 |
| Makefile | 11,223 |
| Python | 3,845 |
| Dockerfile | 2,881 |
| Go Template | 1,471 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- nodeadm/go.mod (capture: captured) — dependency clues: cel.dev/expr, dario.cat/mergo, github.com/antlr4-go/antlr/v4, github.com/avast/retry-go/v5, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/beorn7/perks
- nodeadm/Makefile (capture: captured)
- nodeadm/test/e2e/infra/Dockerfile (capture: captured)
- nodeadm/test/e2e/infra/requirements.txt (capture: captured) — dependency clues: mitmproxy, moto
- nodeadm/vendor/go.uber.org/multierr/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 24
- Forks at capture: 16
- Last updated: 2026-09-22T06:26:56Z
- Last pushed: 2026-03-28T02:45:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-eks-ami-rhel)
- [README](https://github.com/aws-samples/amazon-eks-ami-rhel/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-eks-ami-rhel/issues)
- [Releases](https://github.com/aws-samples/amazon-eks-ami-rhel/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
