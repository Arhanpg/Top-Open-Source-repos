# cdklabs/cdk-appflow

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-appflow](https://github.com/cdklabs/cdk-appflow)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-appflow/blob/main/README.md)
- README blob SHA: ee75c515e6efea37478d0c367054db3261dc1c13
- Repository ID: 653596623
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repository contains L2 AWS CDK constructs for Amazon AppFlow

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:15:00+00:00

### Short excerpt (up to 100 words)

> Amazon AppFlow is a service that enables creating managed, bi-directional data transfer integrations between various SaaS applications and AWS services. For more information, see the Amazon AppFlow User Guide. This library provides L2 constructs for the following applications and services: - Amazon RDS for PostgreSQL (destination) - Asana (source) - EventBridge (destination) - GitHub (source) - Google Ads (source) - Google Analytics 4 (source) - Google BigQuery (source) - HubSpot (source, destination) - Mailchimp (source) - Marketo (source) - Microsoft Dynamics 365 (source) - Microsoft SharePoint Online (source) - Redshift (destination) - S3 (source, destination) - Salesforce (source, destination) -

### README headings

- Amazon AppFlow Construct Library
- Introduction
- Supported Applications
- Example
- Concepts
- Types of Flows
- Tasks
- Monitoring
- Metrics
- EventBridge notifications
- Notable distinctions from CloudFormation specification
- `OnScheduleFlow` and `incrementalPullConfig`
- `S3Destination` and Glue Catalog
- Security considerations
- Confidential information
- An approach to managing permissions
- Confused Deputy Problem
- Upgrading and breaking changes

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 438,466 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/aws-glue-alpha, @aws-cdk/aws-redshift-alpha, @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @types/aws-lambda, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, esbuild, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 14
- Forks at capture: 6
- Last updated: 2026-11-02T22:22:59Z
- Last pushed: 2026-11-20T08:34:19Z
- Topics: appflow, aws

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-appflow)
- [README](https://github.com/cdklabs/cdk-appflow/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-appflow/issues)
- [Releases](https://github.com/cdklabs/cdk-appflow/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
