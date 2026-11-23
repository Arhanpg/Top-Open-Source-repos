# aws/amazon-ec2-spot-interrupter

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-ec2-spot-interrupter](https://github.com/aws/amazon-ec2-spot-interrupter)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-ec2-spot-interrupter/blob/main/README.md)
- README blob SHA: f8cef0b24cce0814d3b0609e327757878527a034
- Repository ID: 469878284
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The ec2-spot-interrupter is a simple CLI tool that triggers Amazon EC2 Spot Interruption Notifications and Rebalance Recommendations.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:11:15+00:00

### Short excerpt (up to 100 words)

> The `ec2-spot-interrupter` is a simple CLI tool that triggers Amazon EC2 Spot Interruption Notifications and Rebalance Recommendations. brew tap aws/tap brew install ec2-spot-interrupter Spot instances are regular EC2 capacity that can be reclaimed by AWS with a 2-minute notification called the Interruption Notification. Applications that are able to gracefully handle this notification and respond by check pointing or draining work can leverage Spot for deeply discounted compute resources! In addition to Interruption Notifications, Rebalance Recommendation Events are sent to spot instances that are at higher risk of being interrupted. Handling Rebalance Recommendations can potentially give your application even more time

### README headings

- Amazon EC2 Spot Interrupter
- Installation
- About
- Usage
- Communication
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 48,258 |
| Makefile | 972 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/atotto/clipboard, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/fis, github.com/aws/aws-sdk-go-v2/service/iam, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/aymanbagabas/go-osc52/v2, github.com/charmbracelet/bubbles
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 108
- Forks at capture: 15
- Last updated: 2026-11-02T21:27:35Z
- Last pushed: 2026-03-02T16:44:29Z
- Topics: chaos, ec2, fault-injection, spot

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-ec2-spot-interrupter)
- [README](https://github.com/aws/amazon-ec2-spot-interrupter/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-ec2-spot-interrupter/issues)
- [Releases](https://github.com/aws/amazon-ec2-spot-interrupter/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
