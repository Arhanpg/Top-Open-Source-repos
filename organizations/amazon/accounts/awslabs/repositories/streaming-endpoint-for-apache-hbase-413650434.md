# awslabs/streaming-endpoint-for-apache-hbase

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/streaming-endpoint-for-apache-hbase](https://github.com/awslabs/streaming-endpoint-for-apache-hbase)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/streaming-endpoint-for-apache-hbase/blob/main/README.md)
- README blob SHA: 8717be2342ce6dc62e03758f92b9d38be236d4d2
- README bytes captured: 13309
- README truncated at capture limit: False
- Repository ID: 413650434
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This is a custom Apache HBase replication endpoint, to stream records into Apache Kafka, Amazon Kinesis, etc.   

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T20:26:55+00:00

### Short excerpt (up to 300 words)

> Since HBase 0.98.9 we

### README headings

- HBase Custom Replication Endpoint for Amazon Kinesis and Apache Kafka
- Overview
- Usage
- Cluster
- Unit Tests
- Supported HBase configuration properties
- Sample replicated records
- BulkLoad replication
- Put
- deleteall
- delete
- Sample EMR application configration for AWS MSK:
- Sample EMR application configration for AWS Kinesis Streaming:
- References

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> Since HBase 0.98.9 we

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 146,064 |
| Shell | 1,020 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: hbase-custom-replication-endpoint, jackson-databind, maven-compiler-plugin
- hbase-endpoint/pom.xml (capture: captured) — dependency clues: build-helper-maven-plugin, commons-cli, confluex-mock-http, hbase-custom-replication-endpoint, hbase-endpoint, hbase-server, hbase-testing-util, maven-shade-plugin, mockito-core
- kafka-sink/pom.xml (capture: captured) — dependency clues: aws-java-sdk-kafka, confluex-mock-http, hbase-custom-replication-endpoint, hbase-endpoint, hbase-server, hbase-testing-util, kafka-clients, kafka-sink, kafka_2.12, maven-shade-plugin, mockito-core, servlet-api, zookeeper
- kinesis-sink/pom.xml (capture: captured) — dependency clues: amazon-kinesis-producer, confluex-mock-http, hbase-custom-replication-endpoint, hbase-endpoint, hbase-server, hbase-testing-util, kinesis-sink, maven-shade-plugin, mockito-core
- lambda-kafka-function/pom.xml (capture: captured) — dependency clues: *, aws-java-sdk-emr, aws-lambda-java-core, aws-lambda-java-events, aws-lambda-java-log4j2, hbase-client, hbase-custom-replication-endpoint, hbase-endpoint, lambda-kafka-function, maven-shade-plugin
- lambda-kinesis-function/pom.xml (capture: captured) — dependency clues: *, avro, aws-java-sdk-emr, aws-java-sdk-kinesis, aws-lambda-java-core, aws-lambda-java-events, aws-lambda-java-log4j2, confluex-mock-http, hbase-client, hbase-custom-replication-endpoint, hbase-endpoint, lambda-kinesis-function, maven-shade-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 13
- Forks at capture: 11
- Last updated: 2025-12-06T12:04:13Z
- Last pushed: 2023-10-11T21:06:16Z
- Topics: cdc, hbase, kafka, kinesis, replication

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/streaming-endpoint-for-apache-hbase)
- [README](https://github.com/awslabs/streaming-endpoint-for-apache-hbase/blob/main/README.md)
- [Issues](https://github.com/awslabs/streaming-endpoint-for-apache-hbase/issues)
- [Releases](https://github.com/awslabs/streaming-endpoint-for-apache-hbase/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
