# awslabs/ec2-spot-jenkins-plugin

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/ec2-spot-jenkins-plugin](https://github.com/awslabs/ec2-spot-jenkins-plugin)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/ec2-spot-jenkins-plugin/blob/master/README.md)
- README blob SHA: 88ae681f760921b6ba8edd52fb028b0da2ae7a1b
- README bytes captured: 9793
- README truncated at capture limit: False
- Repository ID: 49990501
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The EC2 Spot Jenkins plugin launches EC2 Spot instances as worker nodes for Jenkins CI server, automatically scaling the capacity with the load. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T19:58:39+00:00

### Short excerpt (up to 300 words)

> This plugin uses Spot sudo yum install java-1.8.0

### README headings

- ec2-spot-jenkins-plugin
- Overview
- Change Log
- Usage
- Setup
- 1. Get AWS Account
- 2. Create IAM User
- 3. Configure User permissions
- 4. Create EC2 Spot Fleet
- 5. Configure Jenkins
- Scaling
- Groovy
- Preconfigure Slave
- Amazon EC2 AMI
- EC2 instance User Data
- Development
- Releasing
- Jenkins 2 can't connect by SSH
- Install Java 8 on EC2 instance

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> This plugin uses Spot

### Getting started and usage: Install Java 8 on EC2 instance

> sudo yum install java-1.8.0

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 317,193 |
| HTML | 9,961 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: aws-credentials, aws-java-sdk, credentials, ec2-fleet, findbugs-maven-plugin, jackson2-api, objenesis, plugin, powermock-api-mockito2, powermock-module-junit4, ssh-slaves

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 95
- Forks at capture: 26
- Last updated: 2025-08-13T11:14:33Z
- Last pushed: 2024-01-30T21:08:33Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/ec2-spot-jenkins-plugin)
- [README](https://github.com/awslabs/ec2-spot-jenkins-plugin/blob/master/README.md)
- [Issues](https://github.com/awslabs/ec2-spot-jenkins-plugin/issues)
- [Releases](https://github.com/awslabs/ec2-spot-jenkins-plugin/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
