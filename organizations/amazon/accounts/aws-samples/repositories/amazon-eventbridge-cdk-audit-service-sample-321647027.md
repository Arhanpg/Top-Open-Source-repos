# aws-samples/amazon-eventbridge-cdk-audit-service-sample

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-eventbridge-cdk-audit-service-sample](https://github.com/aws-samples/amazon-eventbridge-cdk-audit-service-sample)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-eventbridge-cdk-audit-service-sample/blob/main/README.md)
- README blob SHA: a05d1819adebc145a34f18c053fe86849b269383
- README bytes captured: 8628
- README truncated at capture limit: False
- Repository ID: 321647027
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Sample of a decoupled audit service using Amazon EventBridge and AWS Step Functions. Provisioned with AWS CDK.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T19:50:27+00:00

### Short excerpt (up to 300 words)

> npm install -g aws-cdk Custom bus defines three Node v20.16.0 npm 10.8.1 See CONTRIBUTING for more

### README headings

- Audit Service Sample <!-- omit in toc -->
- Architecture
- Schema
- Requirements
- Deployment
- create the required parameters in your AWS account so
- AWS CodePipeline can connect to Github and pull source code
- install aws cdk
- install dependencies
- bootstrap cdk for the target accont and region
- (profile may be different based on your terminal setup)
- CI/CD
- Clean up
- Want to contribute? <!-- omit in toc -->
- Security <!-- omit in toc -->
- License <!-- omit in toc -->

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: install aws cdk

> npm install -g aws-cdk

### Architecture and design: Architecture

> Custom bus defines three

### Technology and requirements: Requirements

> Node v20.16.0 npm 10.8.1

### Limitations and security: Security <!-- omit in toc -->

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 21,365 |
| JavaScript | 8,482 |
| Shell | 1,468 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @types/jest, @types/node, aws-cdk, aws-cdk-lib, constructs, jest, source-map-support, ts-jest, ts-node, typescript
- test/package.json (capture: captured) — dependency clues: @aws-sdk/client-cloudwatch-logs, @aws-sdk/client-dynamodb, @aws-sdk/client-eventbridge, @aws-sdk/client-s3, chai, mocha
- lib/lambda/save-to-s3/package.json (capture: captured) — dependency clues: @aws-sdk/client-s3, @types/aws-lambda, @types/chai, @types/mocha, @types/node, @types/sinon, @types/sinon-chai, chai, mocha, sinon, sinon-chai, ts-node, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 46
- Forks at capture: 13
- Last updated: 2026-10-05T13:35:04Z
- Last pushed: 2026-10-17T11:01:59Z
- Topics: amazon-cloudwatch, amazon-dynamodb, amazon-eventbridge, amazon-s3, amazon-sns, aws-cdk, aws-lambda, aws-step-functions, cicd

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-eventbridge-cdk-audit-service-sample)
- [README](https://github.com/aws-samples/amazon-eventbridge-cdk-audit-service-sample/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-eventbridge-cdk-audit-service-sample/issues)
- [Releases](https://github.com/aws-samples/amazon-eventbridge-cdk-audit-service-sample/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
