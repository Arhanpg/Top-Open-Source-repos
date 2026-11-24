# cdklabs/cdk-enterprise-iac

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-enterprise-iac](https://github.com/cdklabs/cdk-enterprise-iac)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-enterprise-iac/blob/main/README.md)
- README blob SHA: 45002ac69ddd9381a6ebe2d2c12d5f88c3da9dbe
- Repository ID: 522550800
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Utilities for using CDK within enterprise constraints

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:06+00:00

### Short excerpt (up to 100 words)

> Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: Apache-2.0 --> Utilities for using CDK within enterprise constraints. Typescript npm install @cdklabs/cdk-enterprise-iac Python pip install cdklabs.cdk-enterprise-iac Within large enterprises, builders can come up against enterprise imposed constraints when deploying on AWS. This could be simple things such as "All IAM roles must have a specific Permissions Boundary attached". This could also be more restrictive such as strict separation of duties, only allowing certain teams the ability to deploy specific AWS resources (e.g. Networking team can deploy VPCs, Subnets, and route tables. Security team can deploy IAM resources. Developers can

### README headings

- CDK Enterprise IaC
- Install
- Who this project is for
- Usage
- Adding permissions boundaries to all generated IAM roles
- Resource extraction
- Value Sharing methods
- `CFN_OUTPUT`
- `SSM_PARAMETER`
- `API_LOOKUP`
- Resource Partials
- Generated API.md
- CDK Enterprise IaC
- Install
- Who this project is for
- Usage
- Adding permissions boundaries to all generated IAM roles
- Resource extraction
- Value Sharing methods
- `CFN_OUTPUT`
- `SSM_PARAMETER`
- `API_LOOKUP`
- Resource Partials
- Generated API.md
- API Reference <a name="API Reference" id="api-reference"></a>
- Constructs <a name="Constructs" id="Constructs"></a>
- EcsIsoServiceAutoscaler <a name="EcsIsoServiceAutoscaler" id="@cdklabs/cdk-enterprise-iac.EcsIsoServiceAutoscaler"></a>
- Initializers <a name="Initializers" id="@cdklabs/cdk-enterprise-iac.EcsIsoServiceAutoscaler.Initializer"></a>
- `scope`<sup>Required</sup> <a name="scope" id="@cdklabs/cdk-enterprise-iac.EcsIsoServiceAutoscaler.Initializer.parameter.scope"></a>
- `id`<sup>Required</sup> <a name="id" id="@cdklabs/cdk-enterprise-iac.EcsIsoServiceAutoscaler.Initializer.parameter.id"></a>

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 186,741 |
| Python | 25,654 |
| Shell | 1,648 |
| Dockerfile | 311 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @aws-sdk/client-cloudformation, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier, eslint-plugin-security, jest, jest-junit, jsii
- test/constructs/ecsIsoServiceAutoscaler/resources/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 37
- Forks at capture: 8
- Last updated: 2026-09-17T14:22:59Z
- Last pushed: 2026-11-23T18:12:40Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-enterprise-iac)
- [README](https://github.com/cdklabs/cdk-enterprise-iac/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-enterprise-iac/issues)
- [Releases](https://github.com/cdklabs/cdk-enterprise-iac/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
