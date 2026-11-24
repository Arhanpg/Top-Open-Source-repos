# amazon-archives/cdc-neo4j-msk-neptune

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/cdc-neo4j-msk-neptune](https://github.com/amazon-archives/cdc-neo4j-msk-neptune)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/cdc-neo4j-msk-neptune/blob/master/README.md)
- README blob SHA: c56e274bbcc45ec11434054ac58c67fa0abcf52f
- README bytes captured: 7677
- README truncated at capture limit: False
- Repository ID: 260741469
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

After you migrate from an existing graph database to Amazon Neptune, you might want to capture and process changed data in real time. Continuous replication of databases using the change data capture technique allows you to unlock your data and make it available to other systems for use cases such as distributed data processing, building an enterprise data lake, and modernizing your existing database. In the previous post of this series, we demonstrated with an example solution, how to perform automated migration from Neo4j to Amazon Neptune. If you are looking beyond one-time migration and want to keep both databases in sync you might want to run an ongoing replication using the change data capture technique. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T22:56:26+00:00

### Short excerpt (up to 300 words)

> The following code snippet Install Install Git Install

### README headings

- Architecture
- Prerequisites
- Launching the app
- Download code from GitHub
- Review configuration file
- Deploy
- Detailed architecture
- Post deploy steps
- Execute cypher scripts
- Query architecture
- KAFKA related configuration
- streams
- other
- Cleaning up

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Query architecture

> The following code snippet

### Technology and requirements: Prerequisites

> Install Install Git Install

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 3,922 |
| Shell | 1,727 |
| Dockerfile | 1,435 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- bootstrapper/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-ec2, @aws-cdk/aws-iam, @aws-cdk/aws-msk, @aws-cdk/aws-neptune, @aws-cdk/aws-s3, @aws-cdk/core, aws-cdk, aws-sdk, jest, prompts
- transformation-app/package.json (capture: captured) — dependency clues: gremlin, kafkajs
- docker-files/kafka-topic-service/Dockerfile (capture: captured)
- docker-files/neo4j-service/Dockerfile (capture: captured)
- docker-files/startup-service/Dockerfile (capture: captured)
- docker-files/transformation-service/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 5
- Forks at capture: 2
- Last updated: 2024-04-02T21:03:11Z
- Last pushed: 2020-07-27T16:45:39Z
- Topics: amazon-cdk, amazon-msk, amazon-neptune, change-data-capture, docker, docker-compose, graph-database, kafka, neo4j, neo4j-streams, replication

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/cdc-neo4j-msk-neptune)
- [README](https://github.com/amazon-archives/cdc-neo4j-msk-neptune/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/cdc-neo4j-msk-neptune/issues)
- [Releases](https://github.com/amazon-archives/cdc-neo4j-msk-neptune/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
