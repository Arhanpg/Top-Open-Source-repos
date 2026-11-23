# aws-solutions/machine-downtime-monitor-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/machine-downtime-monitor-on-aws](https://github.com/aws-solutions/machine-downtime-monitor-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/machine-downtime-monitor-on-aws/blob/main/README.md)
- README blob SHA: caa32109fbda7349df874198ca57c857e43f5465
- Repository ID: 362550984
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Machine Downtime Monitor on AWS is a self-service, cloud solution that customers can utilize to monitor their machines for breakdowns on factory floors. The solution connects to machines on a factory floor via the OPC-DA protocol and provides a near real-time view of machines statuses across lines and factories. The solution deploys Amazon Kinesis stream and provides a flexible model to configure how machine data should be interpreted, based on customers’ needs.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:44:05+00:00

### Short excerpt (up to 100 words)

> **🚀 Solution Landing Page** | **🚧 Feature request** | **🐛 Bug Report** Note: If you want to use the solution without building from source, navigate to Solution Landing Page - Solution Overview - Architecture Diagram - AWS CDK Constructs - Customizing the Solution - Prerequisites for Customization - Build - Unit Test - Deploy - File Structure - Collection of operational metrics - License Machine Downtime Monitor on AWS is a self-service, cloud solution that customers can utilize to monitor their machines for breakdowns on factory floors. The solution connects to machines on a factory floor via the OPC-DA protocol

### README headings

- Table of contents
- Solution Overview
- Architecture Diagram
- Data Processing and Analysis
- Lambda
- DynamoDB
- Dashboard
- AWS Solutions Constructs
- Customizing the Solution
- Running unit tests for customization
- Building distributable for customization
- File structure
- Collection of operational metrics
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 421,228 |
| Python | 20,661 |
| Shell | 8,093 |
| CSS | 3,848 |
| HTML | 1,150 |
| JavaScript | 417 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/cdk-infrastructure/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-appsync, @aws-cdk/aws-glue, @aws-cdk/aws-quicksight, @aws-cdk/core, @aws-solutions-constructs/aws-cloudfront-s3, @aws-solutions-constructs/aws-dynamodb-stream-lambda, @aws-solutions-constructs/aws-kinesisstreams-kinesisfirehose-s3, @aws-solutions-constructs/aws-kinesisstreams-lambda, @aws-solutions-constructs/core, @types/jest, @types/node, aws-cdk, jest, ts-jest, ts-node, typescript
- source/web-ui/package.json (capture: captured) — dependency clues: @aws-amplify/ui-react, @testing-library/jest-dom, @testing-library/react, @testing-library/user-event, @types/chart.js, @types/jest, @types/node, @types/react, @types/react-bootstrap, @types/react-dom, @types/react-router-dom, aws-amplify, bootstrap, bootstrap-icons, chart.js, moment, react, react-bootstrap, react-dom, react-router-dom
- source/lambda/data-sources/package.json (capture: captured) — dependency clues: @types/jest, @types/node, aws-sdk, axios, jest, moment, ts-jest, ts-node, typescript
- source/lambda/filter-kinesis-stream/package.json (capture: captured) — dependency clues: @types/jest, @types/node, aws-appsync, aws-sdk, axios, es6-promise, graphql, graphql-tag, isomorphic-fetch, jest, moment, ts-jest, ts-node, typescript
- source/lambda/solution-helper/package.json (capture: captured) — dependency clues: @types/jest, @types/node, @types/uuid, aws-sdk, axios, axios-mock-adapter, jest, moment, ts-jest, ts-node, typescript, uuid
- source/lambda/update-filter-function/package.json (capture: captured) — dependency clues: @types/jest, @types/node, aws-sdk, axios, jest, moment, ts-jest, ts-node, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 5
- Last updated: 2024-09-14T01:48:22Z
- Last pushed: 2021-11-22T22:44:48Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/machine-downtime-monitor-on-aws)
- [README](https://github.com/aws-solutions/machine-downtime-monitor-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/machine-downtime-monitor-on-aws/issues)
- [Releases](https://github.com/aws-solutions/machine-downtime-monitor-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
