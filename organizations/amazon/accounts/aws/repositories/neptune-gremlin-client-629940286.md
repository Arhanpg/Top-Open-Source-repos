# aws/neptune-gremlin-client

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/neptune-gremlin-client](https://github.com/aws/neptune-gremlin-client)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/neptune-gremlin-client/blob/main/README.md)
- README blob SHA: faa29aaf675a7360c60878dd55bc30f25b29bc3e
- README bytes captured: 86916
- README truncated at capture limit: False
- Repository ID: 629940286
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Java Gremlin client for Amazon Neptune that allows you to change the endpoints used by the client as it is running.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:47:59+00:00

### Short excerpt (up to 300 words)

> With the Neptune Gremlin 1. Build the AWS The major version of

### README headings

- Neptune Gremlin Client
- Changes to the build artefacts
- Support for AWS SDK for Java 2.x
- Removing AWS SDK for Java 1.x
- Apache TinkerPop compatibility
- Example
- Dependencies
- Maven
- Table of Contents
- Overview
- Distributing requests across an Amazon Neptune cluster
- Creating a GremlinCluster and GremlinClient
- Configuration
- Using a ClusterEndpointsRefreshAgent
- Using an AWS Lambda proxy to retrieve cluster topology
- Installing the neptune-endpoints-info AWS Lambda function
- Lambda proxy environment variables
- Lambda reserved concurrency
- Suspending endpoints using the AWS Lambda proxy
- Using a ClusterEndpointsRefreshAgent to query the Neptune Management API directly
- ClusterEndpointsRefreshAgent credentials
- Using a ClusterEndpointsRefreshAgent in an AWS Lambda function
- Accessing the Neptune Management API or Lambda proxy across accounts
- EndpointsSelector
- EndpointsType
- Connecting to an IAM auth enabled Neptune database
- Service region
- Connecting via a proxy
- Configuring proxy connections for an IAM auth enabled Neptune database
- Removing the Host header before sending a Sigv4 signed request to a proxy

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> With the Neptune Gremlin

### Getting started and usage: Installing the neptune-endpoints-info AWS Lambda function

> 1. Build the AWS

### Limitations and security: Apache TinkerPop compatibility

> The major version of

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 362,735 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: maven-compiler-plugin, neptune-gremlin-client
- gremlin-client-demo/pom.xml (capture: captured) — dependency clues: airline, aws-lambda-java-core, gremlin-client, gremlin-client-demo, junit, maven-clean-plugin, maven-deploy-plugin, maven-install-plugin, maven-jar-plugin, maven-javadoc-plugin, maven-resources-plugin, maven-shade-plugin, maven-site-plugin, maven-source-plugin, maven-surefire-plugin, slf4j-simple
- gremlin-client/pom.xml (capture: captured) — dependency clues: amazon-neptune-sigv4-signer, aws-core, central-publishing-maven-plugin, git-commit-id-maven-plugin, gremlin-client, gremlin-driver, jackson-databind, junit, lambda, maven-assembly-plugin, maven-compiler-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-source-plugin, mockito-core, neptune, neptunedata, retry4j, sdk-core, utils
- neptune-endpoints-info-lambda/pom.xml (capture: captured) — dependency clues: aws-lambda-java-core, central-publishing-maven-plugin, gremlin-client, junit, maven-clean-plugin, maven-deploy-plugin, maven-gpg-plugin, maven-install-plugin, maven-jar-plugin, maven-javadoc-plugin, maven-resources-plugin, maven-shade-plugin, maven-site-plugin, maven-source-plugin, maven-surefire-plugin, neptune-endpoints-info-lambda

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 11
- Last updated: 2026-08-25T11:20:29Z
- Last pushed: 2026-10-06T00:21:31Z
- Topics: amazon-neptune, aws-neptune, gremlin, tinkerpop

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/neptune-gremlin-client)
- [README](https://github.com/aws/neptune-gremlin-client/blob/main/README.md)
- [Issues](https://github.com/aws/neptune-gremlin-client/issues)
- [Releases](https://github.com/aws/neptune-gremlin-client/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
