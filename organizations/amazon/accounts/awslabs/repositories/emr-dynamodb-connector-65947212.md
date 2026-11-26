# awslabs/emr-dynamodb-connector

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/emr-dynamodb-connector](https://github.com/awslabs/emr-dynamodb-connector)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/emr-dynamodb-connector/blob/master/README.md)
- README blob SHA: 9ae98bf87cee8388ff086e0a11e97ba4001af20e
- README bytes captured: 8655
- README truncated at capture limit: False
- Repository ID: 65947212
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Implementations of open source Apache Hadoop/Hive interfaces which allow for ingesting data from Amazon DynamoDB

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T20:30:39+00:00

### Short excerpt (up to 300 words)

> You can use this java -cp target/emr-dynamodb-tools-4.2.0-SNAPSHOT.jar org.apache.hadoop.dynamodb.tools.DynamoDBExport

### README headings

- emr-dynamodb-connector
- Introduction
- Hive StorageHandler Implementation
- Hadoop InputFormat and OutputFormat Implementation
- Import/Export Tool
- Supported Versions
- How to Build
- Example: Hive StorageHandler
- Example: Input/Output Formats with Spark
- Example: Import/Export Tool
- Export usage
- Import usage
- Additional options
- Maven Dependency
- Hadoop InputFormat/OutputFormats & DynamoDBItemWritable
- Hive SerDes & StorageHandler
- Contributing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> You can use this

### Getting started and usage: Export usage

> java -cp target/emr-dynamodb-tools-4.2.0-SNAPSHOT.jar org.apache.hadoop.dynamodb.tools.DynamoDBExport

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 602,193 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: bom, commons-lang3, emr-dynamodb-connector, git-commit-id-plugin, gson, guava, hadoop-common, hadoop-hdfs, hadoop-mapreduce-client-app, hadoop-mapreduce-client-core, hadoop-mapreduce-client-jobclient, hamcrest-all, hive-exec, hive-metastore, hive-service, httpclient, httpcore, junit, maven-assembly-plugin, maven-checkstyle-plugin
- emr-dynamodb-hadoop/pom.xml (capture: captured) — dependency clues: apache-client, commons-lang3, dynamodb, emr-dynamodb-connector, emr-dynamodb-hadoop, gson, hadoop-common, hadoop-mapreduce-client-app, jackson-databind, joda-time, junit, maven-checkstyle-plugin, maven-shade-plugin, mockito-inline
- emr-dynamodb-hive/pom.xml (capture: captured) — dependency clues: apache-client, commons-lang3, dynamodb, emr-dynamodb-connector, emr-dynamodb-hadoop, emr-dynamodb-hive, hadoop-common, hadoop-hdfs, hadoop-mapreduce-client-hs, hadoop-mapreduce-client-jobclient, hadoop-yarn-server-tests, hive-exec, hive-metastore, hive-service, junit, maven-checkstyle-plugin, maven-jar-plugin, maven-shade-plugin, mockito-inline, shims-common
- emr-dynamodb-tools/pom.xml (capture: captured) — dependency clues: apache-client, dynamodb, emr-dynamodb-connector, emr-dynamodb-hadoop, emr-dynamodb-tools, guava, hadoop-common, hadoop-mapreduce-client-core, hamcrest-all, junit, maven-checkstyle-plugin, mockito-inline
- shims/pom.xml (capture: captured) — dependency clues: emr-dynamodb-connector, shims
- shims/common/pom.xml (capture: captured) — dependency clues: hadoop-common, hive-exec, maven-checkstyle-plugin, shims, shims-common

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 228
- Forks at capture: 138
- Last updated: 2026-04-08T22:12:42Z
- Last pushed: 2026-04-08T22:12:34Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/emr-dynamodb-connector)
- [README](https://github.com/awslabs/emr-dynamodb-connector/blob/master/README.md)
- [Issues](https://github.com/awslabs/emr-dynamodb-connector/issues)
- [Releases](https://github.com/awslabs/emr-dynamodb-connector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
