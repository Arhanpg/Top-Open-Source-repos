# cdklabs/cdk-aws-sagemaker-role-manager

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-aws-sagemaker-role-manager](https://github.com/cdklabs/cdk-aws-sagemaker-role-manager)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-aws-sagemaker-role-manager/blob/main/README.md)
- README blob SHA: d458f9bf4d6ea87dd2ad90dc7c0486e512eed447
- Repository ID: 633534476
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Create roles and policies for ML Activities and ML Personas

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:31:04+00:00

### Short excerpt (up to 100 words)

> import { Stack } from 'aws-cdk-lib'; import { Activity } from '@cdklabs/cdk-aws-sagemaker-role-manager'; const stack = new Stack(app, 'CdkRoleManagerDemo'); const activity = Activity.manageJobs(stack, 'id1', { rolesToPass: [iam.Role.fromRoleName('Enter Name')], subnets: [ec2.Subnet.fromSubnetId('Enter Id')], securityGroups: [ec2.SecurityGroup.fromSecurityGroupId('Enter Id')], dataKeys: [kms.Key.fromKeyArn('Enter Key Arn')], volumeKeys: [kms.Key.fromKeyArn('Enter Key Arn')], }); activity.createRole(stack, 'role id', 'Enter Name'); import { Stack } from 'aws-cdk-lib'; import { Activity } from '@cdklabs/cdk-aws-sagemaker-role-manager'; const stack = new Stack(app, 'CdkRoleManagerDemo'); const activity = Activity.manageJobs(this, 'id1', { rolesToPass: [iam.Role.fromRoleName('Enter Name')], }); activity.createRole(this, 'role id', 'Enter Name', 'Enter Description'); import { Stack } from 'aws-cdk-lib'; import { Activity, Persona } from '@cdklabs/cdk-aws-sagemaker-role-manager'; const stack = new Stack(app,

### README headings

- cdk-aws-sagemaker-role-manager
- Usage
- Create Role from ML Activity with VPC and KMS conditions
- Create Role from ML Activity without VPC and KMS conditions
- Create Role from Data Scientist ML Persona
- Create Role from Data Scientist ML Persona without vpc and kms global conditions
- Create Role MLOps ML Persona
- Create Role from MLOps ML Persona without vpc and kms global conditions
- Available ML Activities
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 88,668 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, aws-sdk, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-diff, jsii-docgen

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 1
- Last updated: 2026-11-02T22:22:38Z
- Last pushed: 2026-11-20T08:32:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-aws-sagemaker-role-manager)
- [README](https://github.com/cdklabs/cdk-aws-sagemaker-role-manager/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-aws-sagemaker-role-manager/issues)
- [Releases](https://github.com/cdklabs/cdk-aws-sagemaker-role-manager/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
