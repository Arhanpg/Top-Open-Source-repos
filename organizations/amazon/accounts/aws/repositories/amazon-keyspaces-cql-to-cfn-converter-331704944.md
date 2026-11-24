# aws/amazon-keyspaces-cql-to-cfn-converter

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-keyspaces-cql-to-cfn-converter](https://github.com/aws/amazon-keyspaces-cql-to-cfn-converter)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-keyspaces-cql-to-cfn-converter/blob/main/README.md)
- README blob SHA: 840d37cc7f3ef5c91942b60b153cf1808feb88be
- Repository ID: 331704944
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Command-line tool for converting Apache Cassandra Query Language (CQL) scripts to AWS CloudFormation (CFN) templates, so Amazon Keyspaces (for Apache Cassandra) schema can be easily managed in AWS CloudFormation stacks.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:34:50+00:00

### Short excerpt (up to 100 words)

> The current version is 1.0.0. Please see the changelog for details on version history. This package implements a command-line tool for converting Apache Cassandra Query Language (CQL) scripts to AWS CloudFormation (CFN) templates, which allows Amazon Keyspaces (for Apache Cassandra) schema to be easily managed in AWS CloudFormation stacks. The tool currently supports the following statements: * `CREATE KEYSPACE` * `CREATE TABLE` * `USE` Given a CQL script named `my_cql_script.cql` CREATE KEYSPACE my_keyspace WITH replication = {'class': 'SingleRegionStrategy'}; USE my_keyspace; CREATE TABLE my_table (pk int PRIMARY KEY); run the tool by executing $ cql2cfn my_cql_script.cql my_cfn_template.json this will produce a

### README headings

- IMPORTANT: Latest Version
- Overview
- Example Usage
- How to build the tool
- Testing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Kotlin | 39,844 |
| GAP | 15,967 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build.gradle.kts (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 5
- Last updated: 2024-08-02T02:22:40Z
- Last pushed: 2023-04-10T09:18:12Z
- Topics: amazon-keyspaces, aws, cassandra, cql, keyspaces

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-keyspaces-cql-to-cfn-converter)
- [README](https://github.com/aws/amazon-keyspaces-cql-to-cfn-converter/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-keyspaces-cql-to-cfn-converter/issues)
- [Releases](https://github.com/aws/amazon-keyspaces-cql-to-cfn-converter/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
