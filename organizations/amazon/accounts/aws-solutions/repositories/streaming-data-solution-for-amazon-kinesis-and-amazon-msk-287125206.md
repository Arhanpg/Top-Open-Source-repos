# aws-solutions/streaming-data-solution-for-amazon-kinesis-and-amazon-msk

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/streaming-data-solution-for-amazon-kinesis-and-amazon-msk](https://github.com/aws-solutions/streaming-data-solution-for-amazon-kinesis-and-amazon-msk)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/streaming-data-solution-for-amazon-kinesis-and-amazon-msk/blob/main/README.md)
- README blob SHA: 1dbf78ffe5a0f0b10bf8d13cc3ae0e672efc4e37
- README bytes captured: 9922
- README truncated at capture limit: False
- Repository ID: 287125206
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A solutions that automatically configures the AWS services necessary to easily capture, store, process, and deliver streaming data. This solution helps you solve for real-time streaming use cases like capturing high volume application logs, analyzing clickstream data, continuously delivering to a data lake, and more.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T05:02:02+00:00

### Short excerpt (up to 300 words)

> cd ./deployment chmod +x AWS Command Line Interface For the options that

### README headings

- Streaming Data Solution for Amazon Kinesis and Streaming Data Solution for Amazon MSK
- Table of contents
- AWS CDK Constructs
- Project structure
- Deployment
- Creating a custom build
- Prerequisites
- 1. Download or clone this repo
- 2. After introducing changes, run the unit tests to make sure the customizations don't break existing functionality
- 3. Build the solution for deployment
- 4. Upload deployment assets to your Amazon S3 buckets
- 5. Launch the CloudFormation template
- Collection of operational metrics
- Known issues
- Additional Resources
- Services
- Other

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: 2. After introducing changes, run the unit tests to make sure the customizations don't break existing functionality

> cd ./deployment chmod +x

### Technology and requirements: Prerequisites

> AWS Command Line Interface

### Limitations and security: Known issues

> For the options that

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 293,647 |
| Python | 78,380 |
| JavaScript | 37,006 |
| Java | 34,940 |
| Shell | 12,611 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/package.json (capture: captured) — dependency clues: @aws-cdk/aws-servicecatalogappregistry-alpha, @aws-solutions-constructs/aws-apigateway-kinesisstreams, @aws-solutions-constructs/aws-apigateway-lambda, @aws-solutions-constructs/aws-kinesisfirehose-s3, @aws-solutions-constructs/aws-kinesisstreams-lambda, @types/babel__traverse, @types/jest, @types/node, @types/prettier, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, cdk-nag, eslint-config-prettier, eslint-plugin-prettier, jest, prettier, source-map-support, ts-jest
- deployment/cdk-solution-helper/package.json (capture: captured) — dependency clues: fs
- source/kinesis/kda-flink-ml/pom.xml (capture: captured) — dependency clues: auth, aws-kda-flink-ml, aws-kinesisanalytics-runtime, commons-compress, flink-connector-kinesis, flink-java, flink-json, flink-streaming-java, gson, guava, maven-compiler-plugin, maven-shade-plugin, netty-nio-client, slf4j-reload4j, snappy-java
- source/kinesis/kpl-demo/pom.xml (capture: captured) — dependency clues: amazon-kinesis-client, amazon-kinesis-producer, avro, aws-java-sdk-core, aws-kpl-demo, commons-compress, commons-io, guava, json, kafka-clients, maven-compiler-plugin, maven-shade-plugin, netty-nio-client, protobuf-java, schema-registry-serde, slf4j-simple
- source/lambda/cloud9-setup/requirements.txt (capture: captured) — dependency clues: crhelper
- source/lambda/kda-vpc-config/requirements.txt (capture: captured) — dependency clues: crhelper

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 95
- Forks at capture: 32
- Last updated: 2026-07-04T05:45:15Z
- Last pushed: 2025-02-03T15:23:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/streaming-data-solution-for-amazon-kinesis-and-amazon-msk)
- [README](https://github.com/aws-solutions/streaming-data-solution-for-amazon-kinesis-and-amazon-msk/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/streaming-data-solution-for-amazon-kinesis-and-amazon-msk/issues)
- [Releases](https://github.com/aws-solutions/streaming-data-solution-for-amazon-kinesis-and-amazon-msk/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
