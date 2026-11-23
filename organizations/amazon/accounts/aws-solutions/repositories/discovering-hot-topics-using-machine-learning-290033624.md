# aws-solutions/discovering-hot-topics-using-machine-learning

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/discovering-hot-topics-using-machine-learning](https://github.com/aws-solutions/discovering-hot-topics-using-machine-learning)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/discovering-hot-topics-using-machine-learning/blob/main/README.md)
- README blob SHA: cc3ea349d204aad55a5233354cdb869cc6a52d63
- Repository ID: 290033624
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Discovering Hot Topics Using Machine Learning solution helps brand-conscious customers understand the most popular topics being actively discussed by ingesting digital assets and performing near real-time inferences and analytics

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:12:45+00:00

### Short excerpt (up to 100 words)

> As of 12/20/2024, The Discovering Hot Topics Using Machine Learning solution has been deprecated and will not be receiving any additional features or updates. You can explore other Solutions in the AWS Solutions Library. The Discovering Hot Topics Using Machine Learning solution identifies the most dominant topics associated with your products, policies, events, and brands. This enables you to react quickly to new growth opportunities, address negative brand associations, and deliver a higher level of customer satisfaction for your business. In addition to helping you understand what your customers are saying about your brand, this solution gives you insights into

### README headings

- Deprecation Notice
- Discovering Hot Topics using Machine Learning
- On this Page
- Architecture Overview
- AWS CDK Constructs
- Deployment
- Source Code
- Project directory structure
- Creating a custom build
- 1. Clone the repository
- 2. Build the solution for deployment
- 3. Upload deployment assets to your Amazon S3 buckets
- 4. Launch the CloudFormation template
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 574,900 |
| Python | 410,276 |
| TypeScript | 162,506 |
| Shell | 17,477 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/package.json (capture: captured) — dependency clues: @aws-cdk/aws-glue-alpha, @aws-cdk/aws-lambda-python-alpha, @aws-cdk/aws-servicecatalogappregistry-alpha, @aws-solutions-constructs/aws-eventbridge-lambda, @aws-solutions-constructs/aws-kinesisfirehose-s3, @aws-solutions-constructs/aws-kinesisstreams-lambda, @aws-solutions-constructs/aws-lambda-dynamodb, @aws-solutions-constructs/aws-lambda-s3, @aws-solutions-constructs/aws-lambda-stepfunctions, @aws-solutions-constructs/aws-sqs-lambda, @aws-solutions-constructs/core, @types/jest, @types/node, @types/sinon, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, cdk-nag, constructs
- deployment/cdk-solution-helper/package.json (capture: captured) — dependency clues: fs
- source/lambda/capture_news_feed/requirements.txt (capture: captured) — dependency clues: feedparser, tldextract, urllib3
- source/lambda/firehose-text-proxy/package.json (capture: captured) — dependency clues: @aws-sdk/client-firehose, aws-sdk-client-mock, chai, jest, moment, sinon
- source/lambda/firehose_topic_proxy/requirements.txt (capture: content_not_returned)
- source/lambda/ingestion-consumer/package.json (capture: captured) — dependency clues: @aws-sdk/client-sfn, aws-sdk-client-mock, chai, jest, sinon

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 70
- Forks at capture: 22
- Last updated: 2026-08-19T21:40:25Z
- Last pushed: 2024-12-30T18:25:04Z
- Topics: amazon-quicksight-dashboard, architecture-overview, artificial-intelligence, aws-cloud, machine-learning, quicksight

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/discovering-hot-topics-using-machine-learning)
- [README](https://github.com/aws-solutions/discovering-hot-topics-using-machine-learning/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/discovering-hot-topics-using-machine-learning/issues)
- [Releases](https://github.com/aws-solutions/discovering-hot-topics-using-machine-learning/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
