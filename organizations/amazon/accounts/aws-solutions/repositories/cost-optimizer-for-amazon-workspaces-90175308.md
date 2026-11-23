# aws-solutions/cost-optimizer-for-amazon-workspaces

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/cost-optimizer-for-amazon-workspaces](https://github.com/aws-solutions/cost-optimizer-for-amazon-workspaces)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/cost-optimizer-for-amazon-workspaces/blob/main/README.md)
- README blob SHA: 2026688cb369939bf1f237484668824fbb640bac
- Repository ID: 90175308
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This solution analyzes all of your Amazon WorkSpaces usage data and automatically converts the WorkSpace to the most cost-effective billing option (hourly or monthly), depending on your individual usage. Use this with a single account, or with AWS Organizations across multiple accounts, to help you monitor your WorkSpace usage and optimize costs.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:12:37+00:00

### Short excerpt (up to 100 words)

> *🚀 Solution Landing Page** | **🚧 Feature request** | **🐛 Bug Report** Note: If you want to use the solution without building from source, navigate to Solution Landing Page. - Solution Overview - Architecture Diagram - Getting Started - Customizing the Solution - Build - Unit Test - Deploy - File Structure - Collection of operational metrics - License Amazon WorkSpaces, a fully managed, secure virtual desktop computing service on the AWS Cloud, eliminates the need for customers to procure, deploy, and manage complex virtual desktop environments. Amazon WorkSpaces offers the flexibility to pay hourly or monthly without any up-front

### README headings

- Table of contents
- Solution Overview
- Architecture Diagram
- Getting Started
- set your preconfigured aws profile in ~/.aws/credentials
- Customizing the Solution
- Build
- NOTE THAT the region is appended to the DIST_BUCKET_NAME (DIST_BUCKET_NAME-REGION) when deployed, so creating a bucket with only Bucket_Name will not work.
- Unit Test
- Deploy
- Note: running bootstrap is only required once, not needed for every subsequent deployment.
- source/cdk.out/{cost-optimizer-for-amazon-workspaces.template.json, cost-optimizer-for-amazon-workspaces-spoke.template.json}
- File structure
- Collection of operational metrics
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 372,496 |
| TypeScript | 107,953 |
| Shell | 10,206 |
| Dockerfile | 626 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/Dockerfile (capture: captured)
- source/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @eslint/js, @types/jest, @types/node, @types/sinon, aws-cdk, aws-cdk-lib, cdk-nag, constructs, eslint, eslint-config-prettier, eslint-plugin-headers, eslint-plugin-prettier, globals, jest, prettier, sinon, ts-jest, ts-node, typescript
- source/pyproject.toml (capture: captured) — dependency clues: attrs, aws-lambda-powertools, boto3, botocore, certifi, charset-normalizer, coverage, freezegun, idna, iniconfig, jmespath, packaging, pluggy, pyparsing, pytest, pytest-cov, pytest-mock, python-dateutil, requests, s3transfer

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 110
- Forks at capture: 52
- Last updated: 2026-10-26T14:14:58Z
- Last pushed: 2026-10-26T14:21:10Z
- Topics: aws, aws-solutions, cost-optimization, device-managment, virtual-desktop-optimization-tool

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/cost-optimizer-for-amazon-workspaces)
- [README](https://github.com/aws-solutions/cost-optimizer-for-amazon-workspaces/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/cost-optimizer-for-amazon-workspaces/issues)
- [Releases](https://github.com/aws-solutions/cost-optimizer-for-amazon-workspaces/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
