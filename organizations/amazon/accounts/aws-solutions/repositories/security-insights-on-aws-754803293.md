# aws-solutions/security-insights-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/security-insights-on-aws](https://github.com/aws-solutions/security-insights-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/security-insights-on-aws/blob/main/README.md)
- README blob SHA: d54f5b1d526fdc6fdb45fadd9af6ca1f79f7fb5b
- README bytes captured: 17180
- README truncated at capture limit: False
- Repository ID: 754803293
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T05:01:19+00:00

### Short excerpt (up to 300 words)

> ⚠️🚨⚠️ Security Insights on If you plan to The default deployment of Before deploying this solution,

### README headings

- Table of contents
- Solution overview
- Architecture overview
- Architecture reference diagram
- Prerequisites
- Installation
- Customizing the solution
- Prerequisites for Customization
- Build
- 1. Clone the repository
- Unit test
- 3. Create S3 buckets for storing deployment assets
- 4. Declare environment variables
- 5. Build the solution
- Upload Deployment Assets
- Upload deployment assets
- Custom QuickSight Template
- Deploy
- CloudFormation deploy
- CDK deploy
- File structure
- Collection of operational metrics
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> ⚠️🚨⚠️ Security Insights on

### Getting started and usage: Installation

> If you plan to

### Architecture and design: Architecture reference diagram

> The default deployment of

### Technology and requirements: Prerequisites

> Before deploying this solution,

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 515,047 |
| Shell | 8,166 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @typescript-eslint/eslint-plugin, eslint, eslint-config-prettier, eslint-config-standard-with-typescript, eslint-import-resolver-typescript, eslint-plugin-header, eslint-plugin-import, eslint-plugin-prettier, eslint-plugin-promise, husky, lint-staged, typescript
- source/resources/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-glue-alpha, @aws-cdk/aws-scheduler-alpha, @aws-cdk/aws-scheduler-targets-alpha, @aws-solutions-constructs/aws-eventbridge-lambda, @aws-solutions-constructs/aws-eventbridge-sns, @types/jest, @types/node, @types/sinon, aws-cdk, aws-cdk-lib, cdk-nag, constructs, jest, sinon, ts-jest, ts-node, typescript
- source/services/createLakeFormationPermissions/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-sdk/client-glue, @aws-sdk/client-lakeformation, @aws-sdk/client-quicksight, @types/aws-lambda, @types/jest, @types/node, aws-cdk-lib, aws-sdk-client-mock, aws-sdk-client-mock-jest, axios, jest, jest-sonar-reporter, ts-jest, ts-node, typescript, winston
- source/services/createQuickSightDataSetRefreshSchedules/package.json (capture: captured) — dependency clues: @aws-sdk/client-quicksight, @types/aws-lambda, @types/jest, @types/node, aws-sdk-client-mock, aws-sdk-client-mock-jest, axios, jest, ts-jest, ts-node, typescript, winston
- source/services/createQuickSightDataSets/package.json (capture: captured) — dependency clues: @aws-sdk/client-quicksight, @aws-sdk/client-securitylake, @aws-sdk/client-ssm, @types/aws-lambda, @types/jest, @types/node, aws-sdk-client-mock, aws-sdk-client-mock-jest, axios, jest, ts-jest, ts-node, typescript, winston
- source/services/createSolutionReleaseNotification/package.json (capture: captured) — dependency clues: @aws-sdk/client-ssm, @aws-sdk/client-sts, @types/aws-lambda, @types/jest, @types/node, aws-sdk-client-mock, aws-sdk-client-mock-jest, axios, jest, ts-jest, ts-node, typescript, uuid, winston

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 10
- Forks at capture: 6
- Last updated: 2026-01-05T20:40:06Z
- Last pushed: 2025-08-11T20:43:28Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/security-insights-on-aws)
- [README](https://github.com/aws-solutions/security-insights-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/security-insights-on-aws/issues)
- [Releases](https://github.com/aws-solutions/security-insights-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
