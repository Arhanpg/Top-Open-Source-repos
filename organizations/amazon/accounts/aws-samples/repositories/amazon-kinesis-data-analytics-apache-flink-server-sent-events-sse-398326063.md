# aws-samples/amazon-kinesis-data-analytics-apache-flink-server-sent-events-sse

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-kinesis-data-analytics-apache-flink-server-sent-events-sse](https://github.com/aws-samples/amazon-kinesis-data-analytics-apache-flink-server-sent-events-sse)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-kinesis-data-analytics-apache-flink-server-sent-events-sse/blob/main/README.md)
- README blob SHA: 5620fa1c632022ba44ca33c086f9ee879d9521f0
- README bytes captured: 7741
- README truncated at capture limit: False
- Repository ID: 398326063
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

When dealing with real-time data it is often required to send that data over the internet to various sources. Various technologies have enabled this such as web sockets and long polling. Recently server-sent events (SSE) has become a popular technology to push updates to clients. Ingesting this type of data source into AWS requires a client to be running continuously to receive those events. This sample shows how to connect to an SSE endpoint using an Amazon Kinesis Data Analytics application using Apache Flink. As the events arrive they are published to an Amazon Kinesis Data Streams stream then in this sample we simply store the event data in Amazon S3.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T04:26:18+00:00

### Short excerpt (up to 300 words)

> 1. An Amazon Kinesis 1. Apache Maven 3.5 See CONTRIBUTING for more

### README headings

- Ingest Server-Sent Events (SSE) using Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics)
- Architecture
- Example SSE use cases:
- Requirements To Compile
- Compiling
- Setup
- Running
- SSE Endpoints
- Resource Cleanup
- CloudFormation
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Architecture

> 1. An Amazon Kinesis

### Technology and requirements: Requirements To Compile

> 1. Apache Maven 3.5

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 28,472 |
| JavaScript | 3,571 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: amazon-kinesis-data-analytics-apache-flink-server-sent-events-parent, junit, maven-compiler-plugin
- cdk/pom.xml (capture: captured) — dependency clues: amazon-kinesis-data-analytics-apache-flink-server-sent-events-sse-cdk, assertj-core, aws-cdk-maven-plugin, cloudformation, copy-rename-maven-plugin, core, custom-resources, exec-maven-plugin, junit-jupiter-api, junit-jupiter-engine, kinesis, kinesisanalytics, kinesisanalytics-flink, kinesisfirehose, kinesisfirehose-destinations, maven-compiler-plugin, s3
- kinesis-data-analytics-sse/pom.xml (capture: captured) — dependency clues: amazon-kinesis-data-analytics-apache-flink-server-sent-events, aws-java-sdk-bom, aws-java-sdk-logs, aws-kinesisanalytics-flink, aws-kinesisanalytics-runtime, flink-connector-kinesis_${scala.binary.version}, flink-streaming-java_${scala.binary.version}, junit, maven-compiler-plugin, maven-shade-plugin, okhttp, okhttp-sse, slf4j-api, slf4j-simple

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 4
- Forks at capture: 1
- Last updated: 2023-12-28T16:46:30Z
- Last pushed: 2026-01-26T21:40:04Z
- Topics: flink, kinesis-data-analytics, server-sent-events

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-kinesis-data-analytics-apache-flink-server-sent-events-sse)
- [README](https://github.com/aws-samples/amazon-kinesis-data-analytics-apache-flink-server-sent-events-sse/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-kinesis-data-analytics-apache-flink-server-sent-events-sse/issues)
- [Releases](https://github.com/aws-samples/amazon-kinesis-data-analytics-apache-flink-server-sent-events-sse/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
