# aws-solutions/media-insights-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/media-insights-on-aws](https://github.com/aws-solutions/media-insights-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/media-insights-on-aws/blob/main/README.md)
- README blob SHA: 84ac806b299023059e4cdc688cdd83a4aaa8f1cb
- Repository ID: 206171138
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A serverless framework to accelerate the development of applications that discover next-generation insights in your video, audio, text, and image resources by utilizing AWS Machine Learning and Media services.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:44:14+00:00

### Short excerpt (up to 100 words)

> Media Insights on AWS is a development framework for building serverless applications that process video, images, audio, and text on AWS. It takes care of workflow orchestration and data persistence so that you can focus on workflow development. By addressing the concerns of running workflows, Media Insights on AWS empowers you to build applications faster with the benefit of inheriting a pre-built and robust back end. Media Insights on AWS has been successfully used in a variety of scenarios, such as: * Deriving video features for ad placement * Transforming video content with redaction * Indexing videos based on visual

### README headings

- NOTE: This solution is no longer being supported
- Build from scratch:
- Outputs
- Cost
- Approximate monthly cost, excluding all free tiers:
- Limitations
- Architecture Overview
- Architecture components:
- Installation Parameters
- Required parameters
- Optional parameters
- Developers
- Security
- S3 Macie
- Uninstall
- Option 1: Uninstall using the AWS Management Console
- Option 2: Uninstall using AWS Command Line Interface
- Deleting Media Insights on AWS data buckets
- Collection of operational metrics
- Known Issues
- Contributing
- Logo
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,195,873 |
| TypeScript | 201,320 |
| Shell | 61,757 |
| JavaScript | 6,579 |
| Dockerfile | 994 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- docs/Makefile (capture: captured)
- deployment/cdk-solution-helper/package.json (capture: captured)
- deployment/lambda_layer_factory/Dockerfile (capture: captured)
- deployment/lambda_layer_factory/requirements.txt (capture: captured) — dependency clues: aws-xray-sdk, jsonpickle, pymediainfo
- source/anonymized-data-logger/requirements.txt (capture: captured) — dependency clues: requests
- source/cdk/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @types/jest, @types/node, aws-cdk, aws-cdk-lib, cdk-nag, constructs, jest, jest-cdk-snapshot, source-map-support, ts-jest, ts-node, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 256
- Forks at capture: 91
- Last updated: 2026-10-06T08:52:48Z
- Last pushed: 2025-08-29T16:23:40Z
- Topics: aws, machine-learning, serverless-framework, video-processing

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/media-insights-on-aws)
- [README](https://github.com/aws-solutions/media-insights-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/media-insights-on-aws/issues)
- [Releases](https://github.com/aws-solutions/media-insights-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
