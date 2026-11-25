# aws-samples/amazon-connect-agentless-outbound-campaign

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-connect-agentless-outbound-campaign](https://github.com/aws-samples/amazon-connect-agentless-outbound-campaign)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-connect-agentless-outbound-campaign/blob/main/README.md)
- README blob SHA: 5f8417b26a7621109c1aa474693b0b7811772145
- README bytes captured: 9475
- README truncated at capture limit: False
- Repository ID: 673844204
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Create Amazon Connect Agentless Outbound Campaign using AWS Step Functions.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T19:45:56+00:00

### Short excerpt (up to 300 words)

> Using Amazon Connect Outbound Clone the repository and Below are the services

### README headings

- amazon-connect-agentless-outbound-campaign
- Overview
- Architecture
- Deploy using AWS CDK
- Installation
- Build
- Deployment
- Intake Process
- Step 1: Upload Contact List to S3 Bucket
- Step 2: Confirm the DynamoDB Tables created by CDK
- Step 2: Execute the AWS Step Function for Intake Process
- Step 3: Execute the AWS Step Function for Outreach Process
- Step 4 [Optional] : Create an EventBridge Rule for triggering the Step Function Intake Process when a new file is uploaded to the S3 bucket
- Step 5 [Optional] : Create an EventBridge Schedule for triggering the Step Function Outreach Process at regular intervals
- Cleanup

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> Using Amazon Connect Outbound

### Getting started and usage: Installation

> Clone the repository and

### Architecture and design: Architecture

> Below are the services

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 21,151 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: amazon-connect-agentless-outbound-campaign, commons-beanutils, commons-codec, guava, license-maven-plugin
- Infra/pom.xml (capture: captured) — dependency clues: aws-cdk-lib, cdknag, constructs, exec-maven-plugin, infra, junit-jupiter, maven-compiler-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 8
- Forks at capture: 2
- Last updated: 2026-06-04T14:15:29Z
- Last pushed: 2026-07-28T13:16:11Z
- Topics: amazon-connect, amazon-dynamodb, amazon-eventbridge, amazon-s3, aws, aws-step-functions, cdk-examples, java

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-connect-agentless-outbound-campaign)
- [README](https://github.com/aws-samples/amazon-connect-agentless-outbound-campaign/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-connect-agentless-outbound-campaign/issues)
- [Releases](https://github.com/aws-samples/amazon-connect-agentless-outbound-campaign/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
