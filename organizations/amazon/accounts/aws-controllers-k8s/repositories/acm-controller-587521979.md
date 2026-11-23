# aws-controllers-k8s/acm-controller

- Company: Amazon
- GitHub account: [https://github.com/aws-controllers-k8s](https://github.com/aws-controllers-k8s)
- Mapping status: official-directory-listed
- Repository: [aws-controllers-k8s/acm-controller](https://github.com/aws-controllers-k8s/acm-controller)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-controllers-k8s/acm-controller/blob/main/README.md)
- README blob SHA: 7604aedc190a3b5472a1d4742a9ab87e988068ca
- Repository ID: 587521979
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ACK Service controller for AWS Certificate Manager (ACM)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:34:21+00:00

### Short excerpt (up to 100 words)

> This repository contains source code for the AWS Controllers for Kubernetes (ACK) service controller for ACM. Please [log issues][ack-issues] and feedback on the main AWS Controllers for Kubernetes Github project. Learn more about installing ACK service controller for AWS Certificate Manager. The ACK service controller for AWS Certificate Manager is free of charge. If you issue an exportable public certificate with AWS Certificate Manager, there is a charge at certificate issuance and again when the certificate renews. Learn more about AWS Certificate Manager Pricing. The ACK service controller for AWS Certificate Manager uses Kubernetes TLS Secrets to store the certificate

### README headings

- ACK service controller for AWS Certificate Manager
- Getting Started
- Installation Instructions
- Pricing
- Kubernetes Secrets
- Export Certificate
- Exporting an exportable ACM public certificate
- Exporting an ACM private certificate
- Contributing
- License
- ACME Resources
- AcmeEndpoint
- AcmeDomainValidation
- AcmeExternalAccountBinding

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 64,567 |
| Go | 56,954 |
| Go Template | 9,648 |
| Smarty | 7,091 |
| Makefile | 565 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws-controllers-k8s/acmpca-controller, github.com/aws-controllers-k8s/iam-controller, github.com/aws-controllers-k8s/route53-controller, github.com/aws-controllers-k8s/runtime, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/acm, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/beorn7/perks, github.com/cenkalti/backoff/v4
- Makefile (capture: captured)
- helm/Chart.yaml (capture: captured)
- test/e2e/requirements.txt (capture: captured) — dependency clues: acktest, cryptography

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 45
- Forks at capture: 24
- Last updated: 2026-11-10T22:39:26Z
- Last pushed: 2026-11-10T21:39:31Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-controllers-k8s/acm-controller)
- [README](https://github.com/aws-controllers-k8s/acm-controller/blob/main/README.md)
- [Issues](https://github.com/aws-controllers-k8s/acm-controller/issues)
- [Releases](https://github.com/aws-controllers-k8s/acm-controller/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
