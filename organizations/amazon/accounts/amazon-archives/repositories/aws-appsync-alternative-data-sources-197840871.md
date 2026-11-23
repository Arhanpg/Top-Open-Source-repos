# amazon-archives/aws-appsync-alternative-data-sources

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/aws-appsync-alternative-data-sources](https://github.com/amazon-archives/aws-appsync-alternative-data-sources)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/aws-appsync-alternative-data-sources/blob/master/README.md)
- README blob SHA: 93651832bc1cf6eb09739866bd81a1cb02475a77
- Repository ID: 197840871
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Exploring how AWS AppSync can utilize AWS Lambda to integrate with alternative data sources, including Amazon ElastiCache and Amazon Neptune.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:44:25+00:00

### Short excerpt (up to 100 words)

> As CTO and VP of Amazon.com, Werner Vogels, has pointed out “Seldom can one database fit the needs of multiple distinct use cases. The days of the one-size-fits-all monolithic database are behind us, and developers are now building highly distributed applications using a multitude of purpose-built databases.” AWS now offers a number purpose-built databases, including those mentioned including document, graph, and in-memory. In this project, we explore how AWS AppSync can utilize AWS Lambda to integrate with alternative data sources, those not supported out-of-the-box by AppSync. In specific, we will focus on Amazon ElastiCache (in-memory database) and Amazon Neptune (graph

### README headings

- Enabling alternative data sources with AWS AppSync
- Getting Started
- Prerequisites
- Deployment
- install node modules
- select a unique bucket name
- package for deployment
- deploy cloud resources
- Sample Data
- 1. get the ARN of the State Machine
- 2. start execution
- Test Run
- DNS Name
- API Key
- Cleaning Up
- License Summary

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 11,367 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- elasticache/package.json (capture: captured) — dependency clues: ioredis
- neptune/package.json (capture: captured) — dependency clues: gremlin
- setup/package.json (capture: captured) — dependency clues: aws-sdk, gremlin
- stream/package.json (capture: captured) — dependency clues: ioredis

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 14
- Forks at capture: 5
- Last updated: 2026-01-06T21:17:58Z
- Last pushed: 2019-08-22T15:33:23Z
- Topics: aws-appsync, aws-elasticache, aws-lambda, aws-neptune

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/aws-appsync-alternative-data-sources)
- [README](https://github.com/amazon-archives/aws-appsync-alternative-data-sources/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/aws-appsync-alternative-data-sources/issues)
- [Releases](https://github.com/amazon-archives/aws-appsync-alternative-data-sources/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
