# aws-samples/amazon-kinesis-timestream-grafana

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-kinesis-timestream-grafana](https://github.com/aws-samples/amazon-kinesis-timestream-grafana)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-kinesis-timestream-grafana/blob/main/README.md)
- README blob SHA: fc3f9ba99038f3a02ec7af9cf8af021d2ac777a6
- README bytes captured: 11179
- README truncated at capture limit: False
- Repository ID: 327882563
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Sample serverless application that reads events from Amazon Kinesis Data Streams and batches records to Amazon Timestream via Apache Flink app, visualizing results via Grafana.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T04:50:06+00:00

### Short excerpt (up to 300 words)

> The overall serverless architecture See CONTRIBUTING for more

### README headings

- Amazon Timestream with Amazon Kinesis and Grafana Demo
- Overall architecture
- Getting started
- 1. Building and packaging Amazon Kinesis Data Analytics for Apache Flink application
- 2. Deploy infrastructure
- Check deployed resource and kick-off pipeline
- 3. Visualizing Amazon Timestream values through Grafana
- Clean up
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Overall architecture

> The overall serverless architecture

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 27,883 |
| Java | 23,532 |
| Kotlin | 20,725 |
| Shell | 4,661 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- analytics-kotlin/build.gradle.kts (capture: captured)
- analytics/pom.xml (capture: captured) — dependency clues: analytics-timestream-java-sample, aws-java-sdk-bom, aws-java-sdk-timestreamwrite, aws-kinesisanalytics-runtime, flink-clients_${scala.binary.version}, flink-connector-kinesis_${scala.binary.version}, flink-java, flink-streaming-java_${scala.binary.version}, gson, lifecycle-mapping, maven-compiler-plugin, maven-shade-plugin, slf4j-simple
- cdk/requirements.txt (capture: captured) — dependency clues: aws-cdk-aws_lambda_python, aws-cdk.aws-ecs-patterns, aws-cdk.aws-events-targets, aws-cdk.aws-timestream, aws-cdk.aws_kinesis, aws-cdk.core, aws_cdk.aws_events, aws_cdk.aws_iam, aws_cdk.aws_kinesis, aws_cdk.aws_kinesisanalytics, aws_cdk.aws_s3
- cdk/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 29
- Forks at capture: 7
- Last updated: 2025-06-09T14:36:28Z
- Last pushed: 2021-12-14T13:28:59Z
- Topics: amazon-kinesis, amazon-kinesis-data-analytics-flink, amazon-kinesis-streams, amazon-timestream, amazon-web-services, analytics, aws, aws-cdk, aws-lambda, gradle, grafa, java, java-11, kotlin

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-kinesis-timestream-grafana)
- [README](https://github.com/aws-samples/amazon-kinesis-timestream-grafana/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-kinesis-timestream-grafana/issues)
- [Releases](https://github.com/aws-samples/amazon-kinesis-timestream-grafana/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
