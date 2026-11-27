# aws-samples/amazon-s3-contentmetadata

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-s3-contentmetadata](https://github.com/aws-samples/amazon-s3-contentmetadata)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-s3-contentmetadata/blob/main/README.md)
- README blob SHA: e05428074a8541792b123ed89f1caf46d3782649
- README bytes captured: 22139
- README truncated at capture limit: False
- Repository ID: 895125979
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T22:09:07+00:00

### Short excerpt (up to 300 words)

> This package provides an sudo yum install npm $ npm i cdk-nag An AWS account &

### README headings

- Example of building an Iceberg table containing metadata about S3 Objects' content
- Sample code notes
- Overview
- Metadata Extraction
- Event Ordering
- Iceberg Writing
- Joining With S3 Metadata
- Accessing other extracted metadata
- Considerations when joining with the S3 Metadata table
- Latent events
- Event Sequence & Content Validation
- Versioned Buckets
- Extending the Sample
- Adding a new type of Metadata extraction
- Adding new columns to the table
- Deploying and Exercising the Sample
- Prerequisites
- Example steps for Amazon Linux 2023 for npm, maven, java & aws-cdk install
- Install npm
- Install Maven, java  & aws-cdk
- Create S3 Table Bucket
- Build the Iceberg processing component
- Deploy the sample architecture
- Start the Flink Application
- Enable S3 Metadata for the Input Bucket
- Run the sample image upload/modification script
- Tearing down and Cleaning up
- Ensure the input bucket is empty:
- Destroy the Application stack
- Delete the S3 Table, Namespace & Table Bucket

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Example of building an Iceberg table containing metadata about S3 Objects' content

> This package provides an

### Getting started and usage: Install npm

> sudo yum install npm

### Architecture and design: Deploy the sample architecture

> $ npm i cdk-nag

### Technology and requirements: Prerequisites

> An AWS account &

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 62,176 |
| Python | 28,953 |
| TypeScript | 9,809 |
| Shell | 3,703 |
| JavaScript | 2,453 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/aws-kinesisanalytics-flink-alpha, @aws-cdk/aws-lambda-python-alpha, @types/jest, @types/node, aws-cdk, aws-cdk-lib, cdk-nag, constructs, jest, source-map-support, ts-jest, ts-node, typescript
- IcebergProcessor/pom.xml (capture: captured) — dependency clues: IcebergProcessor, aws-kinesisanalytics-runtime, bom, flink-clients, flink-connector-base, flink-connector-datagen, flink-connector-dynamodb, flink-connector-files, flink-connector-kinesis, flink-runtime-web, flink-s3-fs-hadoop, flink-streaming-java, flink-table-api-java-bridge, flink-table-planner_${scala.binary.version}, gson, iceberg-flink-runtime-${flink.major.version}, json-path, junit-jupiter, log4j-api, log4j-core
- metadata/requirements.txt (capture: captured) — dependency clues: boto3, botocore, pillow

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 5
- Forks at capture: 0
- Last updated: 2026-11-08T23:41:32Z
- Last pushed: 2025-04-01T01:48:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-s3-contentmetadata)
- [README](https://github.com/aws-samples/amazon-s3-contentmetadata/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-s3-contentmetadata/issues)
- [Releases](https://github.com/aws-samples/amazon-s3-contentmetadata/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
