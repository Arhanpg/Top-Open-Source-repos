# cdklabs/cdk-docker-image-deployment

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-docker-image-deployment](https://github.com/cdklabs/cdk-docker-image-deployment)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-docker-image-deployment/blob/main/README.md)
- README blob SHA: 5bbba336311c537f8d5dd54410549260d0416af8
- Repository ID: 521384946
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:45:38+00:00

### Short excerpt (up to 100 words)

> This module allows you to copy docker image assets to a repository you control. This can be necessary if you want to build a Docker image in one CDK app and consume it in a different app or outside the CDK, or if you want to apply a lifecycle policy to all images of a part of your application. Below is a basic example for how to use the `DockerImageDeployment` API: import * as ecr from 'aws-cdk-lib/aws-ecr'; import * as imagedeploy from 'cdk-docker-image-deployment'; const repo = ecr.Repository.fromRepositoryName(this, 'MyRepository', 'myrepository'); new imagedeploy.DockerImageDeployment(this, 'ExampleImageDeploymentWithTag', { source: imagedeploy.Source.directory('path/to/directory'), destination: imagedeploy.Destination.ecr(repo, { tag: 'myspecialtag',

### README headings

- CDK Docker Image Deployment
- Getting Started
- Currently Supported Sources
- Currently Supported Destinations
- Under the Hood
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 32,565 |
| Dockerfile | 154 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @stylistic/eslint-plugin, @types/aws-lambda, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, aws-sdk, commit-and-tag-version, constructs, esbuild, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-diff, jsii-docgen, jsii-pacmak
- test/assets/test1/Dockerfile (capture: captured)
- test/assets/test2/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 87
- Forks at capture: 16
- Last updated: 2026-11-09T00:17:30Z
- Last pushed: 2026-11-23T00:22:57Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-docker-image-deployment)
- [README](https://github.com/cdklabs/cdk-docker-image-deployment/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-docker-image-deployment/issues)
- [Releases](https://github.com/cdklabs/cdk-docker-image-deployment/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
