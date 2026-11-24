# amazon-archives/aws-appsync-rds-aurora-sample

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/aws-appsync-rds-aurora-sample](https://github.com/amazon-archives/aws-appsync-rds-aurora-sample)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/aws-appsync-rds-aurora-sample/blob/master/README.md)
- README blob SHA: 3dabcdcd4e20229258912374d06524931da762dc
- Repository ID: 144206078
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An AWS AppSync Serverless resolver for the Amazon Aurora relational database.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:37:56+00:00

### Short excerpt (up to 100 words)

> As of 11/20/2018, AWS AppSync supports Aurora Serverless as a native data source. More information is available here: Relational database data sources This sample application will create all of the AWS resources you need to have an AppSync GraphQL API that fronts an RDS Aurora cluster, doing so via a Lambda function. All resources are created with AWS CloudFormation. Specifically, it will provision the AppSync API (including the schema, data source, and all resolvers), the Cognito user pool used for authorization, an RDS cluster that runs on Amazon Aurora MySQL, and a Lambda function to serve as the go-between. Both

### README headings

- AWS AppSync Using Amazon Aurora as a Data Source via AWS Lambda
- Aurora Serverless Data Sources
- Introduction
- Features
- Setting up the Sample
- Create CloudFormation Stack
- From Here
- From the AppSync Console
- Customize Your Own
- Customizing the Lambda
- Setting Up Authorization
- Client Id
- A Created User
- Authorizing on the AppSync Console
- Using the Sample
- License Summary

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 3,506 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/lamdaresolver/node_modules/mysql/package.json (capture: captured) — dependency clues: after, bignumber.js, eslint, nyc, readable-stream, safe-buffer, seedrandom, sqlstring, timezone-mock, urun, utest
- src/lamdaresolver/node_modules/mysql/node_modules/bignumber.js/package.json (capture: captured)
- src/lamdaresolver/node_modules/mysql/node_modules/readable-stream/package.json (capture: captured) — dependency clues: assert, babel-polyfill, buffer, core-util-is, inherits, isarray, lolex, nyc, process-nextick-args, safe-buffer, string_decoder, tap, tape, util-deprecate
- src/lamdaresolver/node_modules/mysql/node_modules/safe-buffer/package.json (capture: captured) — dependency clues: standard, tape
- src/lamdaresolver/node_modules/mysql/node_modules/sqlstring/package.json (capture: captured) — dependency clues: beautify-benchmark, benchmark, eslint, eslint-plugin-markdown, nyc, urun, utest
- src/lamdaresolver/node_modules/mysql/node_modules/readable-stream/node_modules/core-util-is/package.json (capture: captured) — dependency clues: tap

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 131
- Forks at capture: 32
- Last updated: 2025-07-28T06:03:04Z
- Last pushed: 2020-03-06T20:23:34Z
- Topics: amazon-aurora, amazon-web-services, appsync, appsync-resolvers, aws, aws-lambda, mysql, nodejs, rds

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/aws-appsync-rds-aurora-sample)
- [README](https://github.com/amazon-archives/aws-appsync-rds-aurora-sample/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/aws-appsync-rds-aurora-sample/issues)
- [Releases](https://github.com/amazon-archives/aws-appsync-rds-aurora-sample/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
