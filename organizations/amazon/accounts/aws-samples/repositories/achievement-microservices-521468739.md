# aws-samples/achievement-microservices

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/achievement-microservices](https://github.com/aws-samples/achievement-microservices)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/achievement-microservices/blob/main/README.md)
- README blob SHA: 7b6fdfad2e40d947c3315c1411583487a4669a7a
- Repository ID: 521468739
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:11:28+00:00

### Short excerpt (up to 100 words)

> This CDK project is a sample solution for achievement microservices in games.\ The sample solution contains AWS Lambda Functions, Amazon DynamoDB Tables, Amazon SQS Queues and Amazon API Gateway. - the solution is constructed with only serverless services - the solution handles achievement progress additions asynchronously - a single progress can trigger multiple achievements - for example, progress with winning matches could trigger achievements for 10 wins, 50 wins and 100 wins. - achievement requirements can be appended, and new achievements will be unlocked on the next progress event, as long as the new requirements are after the previous requirements,

### README headings

- Achievement Microservices Sample
- Key features
- Assumptions
- Architecture
- DynamoDB Tables
- Player Table: (1 table, 2 entry types)
- Player Achievement Entries
- Player Progress Entries
- Admin Data Table (1 table, 1 entry type)
- Achievement Data Entries
- Progress Message Table (1 table, 1 entry type)
- Progress Message Entries
- SQS Message Syntax
- In Message
- Out Message
- Prerequisites
- Usage
- Deployment
- Setup Achievement Data
- Send Progress Events
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 14,513 |
| JavaScript | 422 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @types/aws-lambda, @types/jest, @types/node, aigle, aws-cdk, aws-cdk-lib, aws-sdk, constructs, jest, prettier, source-map-support, ts-jest, ts-node, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 1
- Forks at capture: 3
- Last updated: 2025-04-04T06:46:30Z
- Last pushed: 2026-01-22T04:16:50Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/achievement-microservices)
- [README](https://github.com/aws-samples/achievement-microservices/blob/main/README.md)
- [Issues](https://github.com/aws-samples/achievement-microservices/issues)
- [Releases](https://github.com/aws-samples/achievement-microservices/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
