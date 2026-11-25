# aws/aws-msk-iam-auth

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-msk-iam-auth](https://github.com/aws/aws-msk-iam-auth)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-msk-iam-auth/blob/main/README.md)
- README blob SHA: d5e4bb04f84bffec3d33fe69fe6d0e9b27ad6e8e
- README bytes captured: 47806
- README truncated at capture limit: False
- Repository ID: 292053394
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Enables developers to use AWS Identity and Access Management (IAM) to connect to their Amazon Managed Streaming for Apache Kafka (Amazon MSK) clusters.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T03:15:33+00:00

### Short excerpt (up to 300 words)

> The Amazon MSK Library Dependency vulnerability scanning is

### README headings

- Amazon MSK Library for AWS Identity and Access Management
- License
- Introduction
- Building from source
- Validating secure dependencies
- Using the Amazon MSK Library for IAM Authentication
- Configuring a Kafka client to use AWS IAM with AWS_MSK_IAM mechanism
- Sets up TLS for encryption and SASL for authN.
- Identifies the SASL mechanism to use.
- Binds SASL client implementation.
- Encapsulates constructing a SigV4 signature based on extracted credentials.
- The SASL client bound by "sasl.jaas.config" invokes this class.
- Configuring a Kafka client to use AWS IAM with SASL OAUTHBEARER mechanism
- Sets up TLS for encryption and SASL for authN.
- Identifies the SASL mechanism to use.
- Binds SASL client implementation. You can add client credential configurations here.
- Encapsulates constructing a SigV4 signature based on extracted credentials.
- The SASL client bound by "sasl.jaas.config" invokes this class.
- This is used during client authentication and reauthentication
- Specifying an alternate credential profile for a client
- Binds SASL client implementation. Uses the specified profile name to look for credentials.
- Specifying a role based credential profile for a client
- Specifying an AWS IAM Role for a client
- Figuring out whether or not to use default credentials
- Retries while getting credentials
- Custom Region Provider
- CnameRegionProvider
- Route53RegionProvider
- LookupDnsRegionProvider
- Shared parameters

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> The Amazon MSK Library

### Technology and requirements: Validating secure dependencies

> Dependency vulnerability scanning is

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 325,933 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build.gradle (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 172
- Forks at capture: 83
- Last updated: 2026-11-10T23:19:42Z
- Last pushed: 2026-11-10T23:38:23Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-msk-iam-auth)
- [README](https://github.com/aws/aws-msk-iam-auth/blob/main/README.md)
- [Issues](https://github.com/aws/aws-msk-iam-auth/issues)
- [Releases](https://github.com/aws/aws-msk-iam-auth/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
