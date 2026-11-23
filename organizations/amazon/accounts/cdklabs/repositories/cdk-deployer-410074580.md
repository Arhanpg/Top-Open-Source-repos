# cdklabs/cdk-deployer

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-deployer](https://github.com/cdklabs/cdk-deployer)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-deployer/blob/main/README.md)
- README blob SHA: 981899a35983fadb7677946dfb94471e685fba34
- Repository ID: 410074580
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A CDK construct library for deploying artifacts via CodeDeploy.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:45:36+00:00

### Short excerpt (up to 100 words)

> This is a CDK construct library for deploying artifacts via CodeDeploy. This library currently supports NodeJS and Python. Install with npm $ npm install cdk-deployer Install with pip $ pip install cdk-deployer With `codeDeploy.ServerDeploymentGroup`: import * as cdk from '@aws-cdk/core'; import * as autoscaling from '@aws-cdk/aws-autoscaling'; import * as codedeploy from '@aws-cdk/aws-codedeploy'; import { Ec2Deployer, Code } from 'cdk-deployer'; const asg = new autoscaling.AutoScalingGroup(this, 'Asg', { ... }); const deploymentGroup = new codedeploy.ServerDeploymentGroup(this, 'DeploymentGroup', { autoScalingGroups: [asg] }); const deployer = new Ec2Deployer(this, 'Deployer', { code: Code.fromAsset('path/to/code/directory'), deploymentGroup, }); With `codeDeploy.IServerDeploymentGroup`, also need to specify `instanceRoles`: import * as cdk

### README headings

- Deployer CDK Construct
- Installation
- Usage/Examples
- TypeScript:
- Python:
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 24,976 |
| Python | 2,996 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/assertions, @aws-cdk/aws-autoscaling, @aws-cdk/aws-codedeploy, @aws-cdk/aws-ec2, @aws-cdk/aws-iam, @aws-cdk/aws-lambda, @aws-cdk/aws-s3, @aws-cdk/aws-s3-assets, @aws-cdk/core, @aws-cdk/custom-resources, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, constructs, eslint, eslint-import-resolver-node, eslint-import-resolver-typescript, eslint-plugin-import

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 2
- Last updated: 2026-04-26T12:50:06Z
- Last pushed: 2026-04-03T11:29:28Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-deployer)
- [README](https://github.com/cdklabs/cdk-deployer/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-deployer/issues)
- [Releases](https://github.com/cdklabs/cdk-deployer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
