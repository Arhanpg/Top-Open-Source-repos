# awslabs/aws-glue-schema-registry

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-glue-schema-registry](https://github.com/awslabs/aws-glue-schema-registry)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/aws-glue-schema-registry/blob/master/README.md)
- README blob SHA: db436b5934789e1eb192052f34df2f0e8486f747
- README bytes captured: 34374
- README truncated at capture limit: False
- Repository ID: 246133980
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Glue Schema Registry Client library provides serializers / de-serializers for applications to integrate with AWS Glue Schema Registry Service. The library currently supports Avro, JSON and Protobuf data formats. See https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html to get started.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T07:21:21+00:00

### Short excerpt (up to 300 words)

> Registry Description can be 1. Messages/records are serialized 1. **Sign up for Registry Description can be

### README headings

- AWS Glue Schema Registry Library
- Getting Started
- Features
- Building from Source
- Testing
- Using the AWS Glue Schema Registry Library Serializer / Deserializer
- Maven Dependency
- Code Example
- Producer for Kafka with AVRO format
- Consumer for Kafka with AVRO format
- Producer for Kafka with JSON format
- Consumer for Kafka with JSON format
- Producer for Kafka with PROTOBUF format
- Consumer for Kafka with PROTOBUF format
- Dealing with Specific Record (JAVA POJO) for JSON
- Deserializing JSON into a Java POJO (className resolution)
- Using AWS Glue Schema Registry with Kinesis Data Streams
- Using Auto-Registration
- Providing Registry Name
- Providing Schema Name
- Providing Registry Description
- Providing Compatibility Setting for Schema
- Using Compression
- In-Memory Cache settings
- Using a custom HTTP client (e.g. IRSA on EKS)
- Migrating from a third party Schema Registry
- Using Kafka Connect with AWS Glue Schema Registry
- Using Kafka Streams with AWS Glue Schema Registry
- Maven Dependency
- Using the AWS Glue Schema Registry Flink Connector

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Providing Registry Description

> Registry Description can be

### Features and capabilities: Features

> 1. Messages/records are serialized

### Getting started and usage: Getting Started

> 1. **Sign up for

### Limitations and security: Providing Compatibility Setting for Schema

> Registry Description can be

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 2,137,833 |
| C# | 349,753 |
| C | 93,488 |
| CMake | 25,202 |
| Shell | 18,087 |
| Python | 11,004 |
| SWIG | 8,776 |
| Dockerfile | 2,167 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: amazon-kinesis-client, amazon-kinesis-producer, avro, avro-compiler, avro-ipc, avro-maven-plugin, awaitility, bom, central-publishing-maven-plugin, classgraph, commons-cli, commons-compress, commons-lang3, connect-api, connect-json, everit-json-schema, glue, guava, hamcrest-all, ion-java
- avro-flink-serde/pom.xml (capture: captured) — dependency clues: central-publishing-maven-plugin, commons-compress, flink-avro, flink-streaming-java_2.11, hamcrest, jacoco-maven-plugin, junit, junit-jupiter-api, junit-jupiter-engine, junit-jupiter-params, junit-platform-commons, lombok, lz4-java, maven-compiler-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-source-plugin, maven-surefire-plugin, mockito-core, mockito-junit-jupiter
- avro-kafkaconnect-converter/pom.xml (capture: captured) — dependency clues: avro-maven-plugin, central-publishing-maven-plugin, connect-api, junit, junit-jupiter-api, junit-jupiter-engine, junit-jupiter-params, junit-platform-commons, lombok, maven-gpg-plugin, maven-shade-plugin, mockito-core, mockito-junit-jupiter, podam, powermock-reflect, schema-registry-kafkaconnect-converter, schema-registry-parent, schema-registry-serde
- build-tools/pom.xml (capture: captured) — dependency clues: central-publishing-maven-plugin, jacoco-maven-plugin, maven-gpg-plugin, maven-javadoc-plugin, schema-registry-build-tools, schema-registry-parent
- common/pom.xml (capture: captured) — dependency clues: apache-client, avro, aws-json-protocol, central-publishing-maven-plugin, commons-compress, commons-lang3, glue, guava, jackson-core, jackson-databind, junit-jupiter-api, junit-jupiter-engine, junit-jupiter-params, junit-platform-commons, lombok, maven-gpg-plugin, maven-resources-plugin, mockito-core, mockito-junit-jupiter, schema-registry-build-tools
- examples/pom.xml (capture: captured) — dependency clues: central-publishing-maven-plugin, commons-cli, jackson-dataformat-cbor, kinesis, lombok, maven-gpg-plugin, schema-registry-examples, schema-registry-parent, schema-registry-serde

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 152
- Forks at capture: 132
- Last updated: 2026-11-20T04:45:49Z
- Last pushed: 2026-11-20T20:31:11Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-glue-schema-registry)
- [README](https://github.com/awslabs/aws-glue-schema-registry/blob/master/README.md)
- [Issues](https://github.com/awslabs/aws-glue-schema-registry/issues)
- [Releases](https://github.com/awslabs/aws-glue-schema-registry/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
