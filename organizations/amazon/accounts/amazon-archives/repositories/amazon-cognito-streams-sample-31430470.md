# amazon-archives/amazon-cognito-streams-sample

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/amazon-cognito-streams-sample](https://github.com/amazon-archives/amazon-cognito-streams-sample)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/amazon-cognito-streams-sample/blob/master/README.md)
- README blob SHA: 7b46fd520fd8ccc560f40a5fce7c0c32c479a2d1
- Repository ID: 31430470
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Sample demonstrating consuming Amazon Cognito Streams

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:04:33+00:00

### Short excerpt (up to 100 words)

> This example application is meant to demonstrate how to consume Amazon Cognito streams and model data in Amazon Redshift. This sample is designed to be built with Maven. All requisite dependencies are captured in the `pom.xml`. Simply use `mvn package` to build the war and deploy to Elastic Beanstalk or directly to EC2. The sample requires the following environment variables be set: * `JDBC_CONNECTION_STRING` - This JDBC connection string for your Amazon Redshift cluster. * `KINESIS_INPUT_STREAM` (or `PARAM1`) - The name of the Kinesis stream to look for Amazon Cognito updates. * `REDSHIFT_USER_NAME` (or `PARAM2`) - The master user name

### README headings

- Amazon Cognito Streams connector for Amazon Redshift
- Building the sample
- Configuring the sample
- Deploying the sample

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 114,466 |
| CSS | 2,016 |
| HTML | 126 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: amazon-cognito-streams-sample, amazon-kinesis-client, aws-java-sdk, commons-collections, commons-io, commons-logging, guava, javatuples, javax.servlet-api, joda-time, maven-compiler-plugin, maven-war-plugin, postgresql

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 10
- Forks at capture: 8
- Last updated: 2025-02-06T00:36:43Z
- Last pushed: 2020-06-15T20:54:05Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/amazon-cognito-streams-sample)
- [README](https://github.com/amazon-archives/amazon-cognito-streams-sample/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/amazon-cognito-streams-sample/issues)
- [Releases](https://github.com/amazon-archives/amazon-cognito-streams-sample/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
