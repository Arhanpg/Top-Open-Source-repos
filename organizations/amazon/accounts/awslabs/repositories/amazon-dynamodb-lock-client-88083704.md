# awslabs/amazon-dynamodb-lock-client

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-dynamodb-lock-client](https://github.com/awslabs/amazon-dynamodb-lock-client)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/amazon-dynamodb-lock-client/blob/master/README.md)
- README blob SHA: 0083ea382a81de635fa144f47e8c622997a8e626
- Repository ID: 88083704
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The AmazonDynamoDBLockClient is a general purpose distributed locking library built on top of DynamoDB. It supports both coarse-grained and fine-grained locking.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:42:59+00:00

### Short excerpt (up to 100 words)

> The Amazon DynamoDB Lock Client is a general purpose distributed locking library built for DynamoDB. The DynamoDB Lock Client supports both fine-grained and coarse-grained locking as the lock keys can be any arbitrary string, up to a certain length. DynamoDB Lock Client is an open-source project that will be supported by the community. Please create issues in the GitHub repository with questions. A common use case for this lock client is: let's say you have a distributed system that needs to periodically do work on a given campaign (or a given customer, or any other object) and you want to

### README headings

- Amazon DynamoDB Lock Client
- Use cases
- Getting Started
- Permissions
- Selected Features
- Send Automatic Heartbeats
- Acquire lock with timeout
- Acquire lock without blocking the user thread.
- Read the data in a lock without acquiring it
- How we handle clock skew
- Testing the DynamoDB Locking client
- External release to Sonatype

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 441,203 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: annotations, auth, aws-core, byte-buddy, byte-buddy-agent, central-publishing-maven-plugin, commons-codec, commons-logging, docker-maven-plugin, dynamodb, dynamodb-lock-client, hamcrest-core, http-client-spi, httpcore, jacoco-maven-plugin, junit, log4j-core, maven-compiler-plugin, maven-dependency-plugin, maven-enforcer-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 521
- Forks at capture: 93
- Last updated: 2026-11-19T20:25:23Z
- Last pushed: 2026-06-29T10:44:02Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-dynamodb-lock-client)
- [README](https://github.com/awslabs/amazon-dynamodb-lock-client/blob/master/README.md)
- [Issues](https://github.com/awslabs/amazon-dynamodb-lock-client/issues)
- [Releases](https://github.com/awslabs/amazon-dynamodb-lock-client/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
