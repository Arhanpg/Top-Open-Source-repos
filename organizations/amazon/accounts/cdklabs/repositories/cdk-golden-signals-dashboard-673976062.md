# cdklabs/cdk-golden-signals-dashboard

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-golden-signals-dashboard](https://github.com/cdklabs/cdk-golden-signals-dashboard)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-golden-signals-dashboard/blob/main/README.md)
- README blob SHA: 7f9f6afc8136ae513589d008545fe1d829e8193c
- Repository ID: 673976062
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:12+00:00

### Short excerpt (up to 100 words)

> Create Amazon CloudWatch Dashboards for monitoring CloudWatch Metrics of AWS Resources partitioned in golden signals. *Latency, Traffic, Errors, Saturation* You can create tag based CloudWatch dashbord solution out of the box using this construct! Here are some screen captures of CloudWatch dashboards created using this cdk construct. * AWS::DynamoDB::Table * AWS::Lambda::Function * AWS::RDS::DBInstance * AWS::SNS::Topic * AWS::AutoScaling::AutoScalingGroup import { App, StackProps } from 'aws-cdk-lib'; import { GoldenSignalDashboard } from 'cdk-golden-signals-dashboard'; class MyStack extends Stack { constructor(scope: Construct, id: string, props: StackProps = {}) { super(scope, id, props); new GoldenSignalDashboard(this, 'dynamodbDashboard', { resourceType: 'AWS::DynamoDB::Table', dashboardName: 'myGSDashboard', resourceDimensions: [{resourceRegion : 'us-east-1', resources:

### README headings

- CloudWatch Golden Signals Dashboard AWS CDK Construct
- Supported Resource Types
- Usage
- Contributing
- License Summary

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 105,312 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier, eslint-plugin-security, jest, jest-junit, jsii, jsii-diff

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 12
- Forks at capture: 0
- Last updated: 2026-02-20T11:13:24Z
- Last pushed: 2026-02-17T12:01:39Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-golden-signals-dashboard)
- [README](https://github.com/cdklabs/cdk-golden-signals-dashboard/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-golden-signals-dashboard/issues)
- [Releases](https://github.com/cdklabs/cdk-golden-signals-dashboard/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
