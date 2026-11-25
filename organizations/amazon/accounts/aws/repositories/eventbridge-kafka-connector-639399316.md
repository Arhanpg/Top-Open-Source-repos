# aws/eventbridge-kafka-connector

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/eventbridge-kafka-connector](https://github.com/aws/eventbridge-kafka-connector)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/eventbridge-kafka-connector/blob/main/README.md)
- README blob SHA: 5085df5fc7b41a590f3edff0207a6e05ba2766f0
- README bytes captured: 73552
- README truncated at capture limit: False
- Repository ID: 639399316
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Kafka sink connector for Amazon EventBridge to send events (records) from Kafka topic(s) to the specified EventBridge event bus

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T22:09:22+00:00

### Short excerpt (up to 300 words)

> Assuming offloading is enabled The JsonPathDetailTypeMapper works as See CONTRIBUTING for more

### README headings

- Kafka Connector for Amazon EventBridge
- Getting Help
- Installation
- Amazon Managed Streaming for Apache Kafka (MSK)
- Confluent Connector Hub
- Java Archive (JAR)
- From Source
- From Source (Docker)
- clone repo
- Configuration
- Custom Event Bus (v2)
- Example: raw pass-through to a Custom Event Bus
- v2 behavior differences
- Records without a key under record-key grouping
- v2 IAM permissions
- Examples
- JSON Encoding
- JSON Encoding with Dead-Letter Queue
- Avro Encoding with multiple Topics, IAM Role and custom Retries
- Topic to `detail-type` Mapping
- Using the custom `JsonPathDetailTypeMapper`
- How it works
- Restrictions and Fallback Behavior
- Offloading large events (payloads) to S3
- Configure Offloading
- Examples
- Records with `null` Keys and Tombstone Handling
- Example EventBridge Rule Filtering Patterns
- Retry Behavior
- Authentication and Permissions

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Examples

> Assuming offloading is enabled

### Architecture and design: How it works

> The JsonPathDetailTypeMapper works as

### Limitations and security: Contributing and Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 384,967 |
| JavaScript | 313 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: apache-client, assertj-core, auth-crt, awaitility, aws-crt-client, bom, cloudevents-core, cloudevents-json-jackson, commons-codec, commons-lang3, commons-logging, connect-api, connect-json, equalsverifier, eventbridge, eventbridgev2, fmt-maven-plugin, git-commit-id-maven-plugin, google-java-format, hamcrest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 78
- Forks at capture: 10
- Last updated: 2026-10-29T16:30:47Z
- Last pushed: 2026-11-23T17:42:14Z
- Topics: event-driven-architecture, eventbridge, kafka, kafka-connect

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/eventbridge-kafka-connector)
- [README](https://github.com/aws/eventbridge-kafka-connector/blob/main/README.md)
- [Issues](https://github.com/aws/eventbridge-kafka-connector/issues)
- [Releases](https://github.com/aws/eventbridge-kafka-connector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
