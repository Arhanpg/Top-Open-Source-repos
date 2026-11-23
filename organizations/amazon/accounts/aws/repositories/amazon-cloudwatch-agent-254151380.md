# aws/amazon-cloudwatch-agent

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-cloudwatch-agent](https://github.com/aws/amazon-cloudwatch-agent)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-cloudwatch-agent/blob/main/README.md)
- README blob SHA: 54714cf293dcc928eb8f3ab3454c3dc3d6874602
- Repository ID: 254151380
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

CloudWatch Agent enables you to collect and export host-level metrics and logs on instances running Linux or Windows server.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:01:57+00:00

### Short excerpt (up to 100 words)

> The Amazon CloudWatch Agent is software developed for the CloudWatch Agent The Amazon CloudWatch Agent enables you to do the following: - Collect more system-level metrics from Amazon EC2 instances across operating systems. The metrics can include in-guest metrics, in addition to the metrics for EC2 instances. The additional metrics that can be collected are listed in Metrics Collected by the CloudWatch Agent. - Collect system-level metrics from on-premises servers. These can include servers in a hybrid environment as well as servers not managed by AWS. - Retrieve custom metrics from your applications or services using the StatsD and collectd

### README headings

- Amazon CloudWatch Agent
- Overview
- Setup
- Troubleshooting
- Building and Running from source
- Building and running container
- Make Targets
- Features
- Log Filtering
- Versioning
- Distributions
- Usage data
- Security disclosures
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 5,215,667 |
| Shell | 226,200 |
| Makefile | 26,215 |
| PowerShell | 25,356 |
| Dockerfile | 5,607 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute, cloud.google.com/go/compute/metadata, collectd.org, github.com/Azure/azure-sdk-for-go, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/compute/armcompute/v5, github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/network/armnetwork/v4, github.com/Azure/go-autorest/autorest, github.com/Azure/go-autorest/autorest/adal, github.com/Azure/go-ntlmssp, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/BurntSushi/toml, github.com/Code-Hex/go-generics-cache, github.com/DataDog/datadog-agent/pkg/obfuscate, github.com/DataDog/datadog-go/v5, github.com/DataDog/go-sqllexer
- Makefile (capture: captured)
- amazon-cloudwatch-container-insights/cloudwatch-agent-dockerfile/Dockerfile (capture: captured)
- tool/clean/go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/amp, github.com/aws/aws-sdk-go-v2/service/autoscaling, github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/ecs, github.com/aws/aws-sdk-go-v2/service/efs, github.com/aws/aws-sdk-go-v2/service/eks, github.com/aws/aws-sdk-go-v2/service/iam, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/sso
- amazon-cloudwatch-container-insights/cloudwatch-agent-dockerfile/localal2/Dockerfile (capture: captured)
- amazon-cloudwatch-container-insights/cloudwatch-agent-dockerfile/localbin/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 555
- Forks at capture: 284
- Last updated: 2026-11-23T12:41:25Z
- Last pushed: 2026-11-18T17:57:54Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-cloudwatch-agent)
- [README](https://github.com/aws/amazon-cloudwatch-agent/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-cloudwatch-agent/issues)
- [Releases](https://github.com/aws/amazon-cloudwatch-agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
