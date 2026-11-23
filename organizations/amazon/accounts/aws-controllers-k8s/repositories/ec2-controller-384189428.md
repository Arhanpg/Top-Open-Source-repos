# aws-controllers-k8s/ec2-controller

- Company: Amazon
- GitHub account: [https://github.com/aws-controllers-k8s](https://github.com/aws-controllers-k8s)
- Mapping status: official-directory-listed
- Repository: [aws-controllers-k8s/ec2-controller](https://github.com/aws-controllers-k8s/ec2-controller)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-controllers-k8s/ec2-controller/blob/main/README.md)
- README blob SHA: 09a2d6a5cfa33c5256181d518ff740e4c8f7e5d4
- Repository ID: 384189428
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ACK service controller for Amazon Elastic Compute Cloud (EC2)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:29:53+00:00

### Short excerpt (up to 100 words)

> This repository contains source code for the AWS Controllers for Kubernetes (ACK) service controller for Amazon EC2. Please [log issues][ack-issues] and feedback on the main AWS Controllers for Kubernetes Github project. Start with the Install an ACK Controller section to install the controller into a cluster and setup necessary IAM Permissions. *Note: it is recommended and assumed your local terminal has kubectl and AWS credentials configured to use the hosting cluster and AWS account, respectively.* The latest images and Helm Charts can be found in their respective ECR Public repository: * Images * Helm charts * Navigate to test resources

### README headings

- ACK service controller for Amazon Elastic Compute Cloud (EC2)
- Install the Controller
- Release Artifacts
- Create/Delete an ACK Resource
- Uninstall the Controller
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 405,106 |
| Go | 283,583 |
| Go Template | 28,663 |
| Smarty | 28,205 |
| Makefile | 734 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws-controllers-k8s/cloudwatchlogs-controller, github.com/aws-controllers-k8s/elbv2-controller, github.com/aws-controllers-k8s/iam-controller, github.com/aws-controllers-k8s/runtime, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/beorn7/perks, github.com/cenkalti/backoff/v4
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
- Stars at capture: 44
- Forks at capture: 78
- Last updated: 2026-11-11T18:24:45Z
- Last pushed: 2026-11-20T20:30:32Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-controllers-k8s/ec2-controller)
- [README](https://github.com/aws-controllers-k8s/ec2-controller/blob/main/README.md)
- [Issues](https://github.com/aws-controllers-k8s/ec2-controller/issues)
- [Releases](https://github.com/aws-controllers-k8s/ec2-controller/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
