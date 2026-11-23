# aws-observability/log-ia-checker

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/log-ia-checker](https://github.com/aws-observability/log-ia-checker)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/log-ia-checker/blob/main/README.md)
- README blob SHA: 53cd4d043f4bc168d0d468abd8f6026bbe9b89a0
- Repository ID: 936235783
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:30:29+00:00

### Short excerpt (up to 100 words)

> This project retrieves and filters CloudWatch log groups based on a list of conditions. It outputs a list of log groups that are good candidates for re-creation as an Infrequent Access (IA) log group. CloudWatch logs has a log class called Infrequent Access. This Log class is 50% cheaper on ingestion but it does not contain call the capabilities of a standard log group. Using this command line utility, we can check all logs in a region to see if they would be good candidates for transition to IA. At this time it is not possible to programmatically convert a

### README headings

- Infrequent Access Check for CloudWatch Log Group
- Why?
- Prerequisites
- 1. Go (Golang)
- 2. AWS CLI Credentials
- Installation
- Option 1: Install directly with Go (Recommended)
- Option 2: Manual Setup
- If installed via go install
- If running from cloned repository
- Using installed binary - specify both region and output file
- Using installed binary - use AWS_REGION environment variable and default output file
- Using installed binary - specify region but use default output file
- If running from cloned repository, replace 'log-ia-checker' with 'go run .' in the examples above
- Notes
- Testing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 38,753 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/cloudtrail, github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 12
- Forks at capture: 1
- Last updated: 2026-10-22T12:54:15Z
- Last pushed: 2026-04-15T19:29:11Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/log-ia-checker)
- [README](https://github.com/aws-observability/log-ia-checker/blob/main/README.md)
- [Issues](https://github.com/aws-observability/log-ia-checker/issues)
- [Releases](https://github.com/aws-observability/log-ia-checker/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
