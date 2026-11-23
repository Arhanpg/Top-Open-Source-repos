# aws-solutions/amazon-virtual-andon

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/amazon-virtual-andon](https://github.com/aws-solutions/amazon-virtual-andon)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/amazon-virtual-andon/blob/main/README.md)
- README blob SHA: 7267f973668e56499b8af84be359a3fb58356ef0
- Repository ID: 219601798
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Deploy a solution that provides a scalable Andon system to help optimize processes, support the transition to predictive maintenance, and prevent issues. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:32:56+00:00

### Short excerpt (up to 100 words)

> Amazon Virtual Andon is a self-service, cloud based andon system that makes it easy for any business to deploy andon in their factory. It is based on the same technology used by the Amazon Fulfillment centers built on AWS. The events occurring on the factory floor are captured either using a web-interface or connecting the machines to AWS IoT core that publish the events to a topic. These events are then stored in DynamoDB. Using the IoT Rule Engine, the events are integrated with other AWS services such as SNS to send notifications about the events. The solution comes with

### README headings

- Amazon Virtual Andon
- Architecture Overview
- Running unit tests for customization
- Building distributable for customization
- Deploying using cloudformation command
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 792,136 |
| Velocity Template Language | 105,080 |
| JavaScript | 15,941 |
| Python | 11,291 |
| Shell | 6,630 |
| SCSS | 5,435 |
| HTML | 1,247 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/appsync-lambda-resolver/package.json (capture: captured) — dependency clues: @types/jest, @types/node, @types/uuid, aws-sdk, jest, moment, ts-jest, ts-node, typescript
- source/ava-issue-handler/package.json (capture: captured) — dependency clues: @types/jest, @types/node, aws-appsync, aws-sdk, es6-promise, graphql, graphql-tag, isomorphic-fetch, jest, ts-jest, ts-node, typescript
- source/cdk-infrastructure/package.json (capture: captured) — dependency clues: @aws-cdk/aws-glue-alpha, @aws-cdk/aws-servicecatalogappregistry-alpha, @aws-solutions-constructs/aws-cloudfront-s3, @aws-solutions-constructs/aws-iot-lambda, @types/jest, @types/node, aws-cdk, aws-cdk-lib, cdk-nag, constructs, jest, ts-jest, ts-node, typescript
- source/cognito-trigger/package.json (capture: captured) — dependency clues: @types/jest, @types/node, jest, ts-jest, ts-node, typescript
- source/console/package.json (capture: captured) — dependency clues: @aws-amplify/pubsub, @aws-amplify/ui-react, @types/react, @types/react-csv, @types/react-dom, @types/react-notification-system, @types/react-router-bootstrap, @types/react-router-dom, @types/uuid, aws-amplify, aws-sdk, axios, bootstrap, buffer, moment, react, react-bootstrap, react-cookie, react-csv, react-dom
- source/external-integrations-handler/package.json (capture: captured) — dependency clues: @types/jest, @types/node, aws-sdk, jest, ts-jest, ts-node, typescript, uuid

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 15
- Forks at capture: 9
- Last updated: 2025-05-14T02:37:39Z
- Last pushed: 2024-02-05T15:48:05Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/amazon-virtual-andon)
- [README](https://github.com/aws-solutions/amazon-virtual-andon/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/amazon-virtual-andon/issues)
- [Releases](https://github.com/aws-solutions/amazon-virtual-andon/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
