# aws-solutions/aws-devops-monitoring-dashboard

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/aws-devops-monitoring-dashboard](https://github.com/aws-solutions/aws-devops-monitoring-dashboard)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/aws-devops-monitoring-dashboard/blob/main/README.md)
- README blob SHA: 77384560857596063c0456d14412019e1565a15a
- Repository ID: 348777695
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The DevOps Monitoring Dashboard on AWS solution is a reference implementation that automates the process for monitoring and visualizing performance and operational metrics in continuous integration/continuous delivery (CI/CD) pipeline following AWS best practices. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:04:00+00:00

### Short excerpt (up to 100 words)

> ⚠️ __Important: DevOps Monitoring Dashboard on AWS will no longer be supported starting December 3, 2024. You can find other AWS Solutions in the AWS Solutions Library__ ⚠️ **🚀 Solution Landing Page** | **🚧 Feature request** | **🐛 Bug Report** Note: If you want to use the solution without building from source, navigate to Solution Landing Page - Solution Overview - Architecture Diagram - AWS CDK Constructs - Customizing the Solution - Prerequisites for Customization - Build - Unit Test - Deploy - File Structure - License The DevOps Monitoring Dashboard on AWS solution is a reference implementation that automates

### README headings

- Table of contents
- Solution Overview
- Architecture Diagram
- AWS Solutions Constructs
- Customizing the Solution
- Prerequisites for Customization
- Build
- 1. Clone the repository
- 2. Unit test
- 3. Create S3 buckets for storing deployment assets
- 4. Declare environment variables
- The namespace in QuickSight account ARN. Ex. "default"
- 5. Build the solution
- Upload Deployment Assets
- Create QuickSight Template
- Deploy
- File structure
- Collection of operational metrics
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 303,752 |
| TypeScript | 112,440 |
| Python | 96,212 |
| Shell | 15,677 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-glue-alpha, @aws-cdk/aws-servicecatalogappregistry-alpha, @aws-solutions-constructs/aws-eventbridge-kinesisfirehose-s3, @aws-solutions-constructs/aws-eventbridge-lambda, @aws-solutions-constructs/aws-kinesisfirehose-s3, @aws-solutions-constructs/core, @types/jest, @types/node, aws-cdk, aws-cdk-lib, cdk-nag, constructs, eslint, eslint-config-prettier, eslint-config-react-app, eslint-plugin-header, eslint-plugin-import, eslint-plugin-node, eslint-plugin-prettier
- deployment/cdk-solution-helper/package.json (capture: captured)
- source/lambda/event_parser/package.json (capture: captured) — dependency clues: @aws-sdk/client-secrets-manager, async, aws-sdk-mock, chai, jest, mocha, npm-run-all, nyc, sinon, sinon-chai, uuid
- source/lambda/multi_account_custom_resources/package.json (capture: captured) — dependency clues: @aws-sdk/client-eventbridge, @aws-sdk/client-s3, async, aws-sdk-mock, axios, axios-mock-adapter, chai, jest, mocha, npm-run-all, nyc, sinon, sinon-chai, uuid
- source/lambda/query_runner/package.json (capture: captured) — dependency clues: @aws-sdk/client-athena, @aws-sdk/client-cloudwatch, @aws-sdk/client-glue, async, aws-sdk-mock, axios, axios-mock-adapter, chai, jest, mocha, npm-run-all, nyc, sinon, sinon-chai, uuid
- source/lambda/quicksight-custom-resources/pyproject.toml (capture: captured) — dependency clues: PyYAML, boto3, botocore, crhelper, mock, moto, pytest, pytest-cov, pytest-env, requests, tenacity, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 75
- Forks at capture: 42
- Last updated: 2026-10-12T01:51:11Z
- Last pushed: 2024-12-09T18:14:07Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/aws-devops-monitoring-dashboard)
- [README](https://github.com/aws-solutions/aws-devops-monitoring-dashboard/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/aws-devops-monitoring-dashboard/issues)
- [Releases](https://github.com/aws-solutions/aws-devops-monitoring-dashboard/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
