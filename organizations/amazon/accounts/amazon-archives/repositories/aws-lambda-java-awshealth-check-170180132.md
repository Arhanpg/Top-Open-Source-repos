# amazon-archives/aws-lambda-java-AWSHealth-check

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/aws-lambda-java-AWSHealth-check](https://github.com/amazon-archives/aws-lambda-java-AWSHealth-check)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/aws-lambda-java-AWSHealth-check/blob/master/README.md)
- README blob SHA: 455b950c0d09835f9877e162b7b079525d203061
- README bytes captured: 3789
- README truncated at capture limit: False
- Repository ID: 170180132
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Java SAM Lambda module for periodically checking AWS Health API for both general AWS Service issues and customer specific system maintenance events and notify via SES if updates are found.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T06:10:15+00:00

### Short excerpt (up to 300 words)

> This sample code is awscli - https://aws.amazon.com/cli/ configure

### README headings

- AWS Lambda Java module for periodic checking of new AWS Health events
- License Summary
- AWS Costs
- Prerequisites
- Building
- Deploying (SAM / Script)
- Deploy Manually (Lambda Console)
- Manually Running / Testing
- Customize the settings
- Refer to https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html for limitations of filter
- Regions to check for the AWSHealth API data (cannot exceed 10)
- - "ap-northeast-3"
- - "ap-south-1"
- - "ap-southeast-1"
- - "ap-southeast-2"
- - "ca-central-1"
- - "eu-central-1"
- - "eu-west-2"
- - "eu-west-3"
- - "sa-east-1"
- Category to check for the AWSHealth API data
- Status codes to check for for the AWSHealth API data
- - "closed"
- Resource tags to filter for for the AWSHealth API data
- - {"key": "value"}
- - {"key2": "value"}
- SES settings
- Email template for sending blocked IP found notification.

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: License Summary

> This sample code is

### Technology and requirements: Prerequisites

> awscli - https://aws.amazon.com/cli/ configure

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 41,666 |
| Shell | 1,245 |
| Dockerfile | 438 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- pom.xml (capture: captured) — dependency clues: AWSHealthCheck, aws-java-sdk-bom, aws-java-sdk-cloudwatch, aws-java-sdk-core, aws-java-sdk-health, aws-java-sdk-lambda, aws-java-sdk-logs, aws-java-sdk-organizations, aws-java-sdk-s3, aws-java-sdk-ses, aws-java-sdk-sts, aws-lambda-java-core, aws-lambda-java-log4j2, commons-io, javax.mail, javax.mail-api, log4j-api, log4j-core, maven-shade-plugin, maven-shade-plugin.log4j2-cachefile-transformer

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 11
- Forks at capture: 13
- Last updated: 2023-08-14T12:04:55Z
- Last pushed: 2020-07-01T18:43:50Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/aws-lambda-java-AWSHealth-check)
- [README](https://github.com/amazon-archives/aws-lambda-java-AWSHealth-check/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/aws-lambda-java-AWSHealth-check/issues)
- [Releases](https://github.com/amazon-archives/aws-lambda-java-AWSHealth-check/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
