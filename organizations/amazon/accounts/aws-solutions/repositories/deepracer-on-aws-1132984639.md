# aws-solutions/deepracer-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/deepracer-on-aws](https://github.com/aws-solutions/deepracer-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/deepracer-on-aws/blob/main/README.md)
- README blob SHA: c517623a3e92e32f5859e2ea3e0557776bbd76ff
- Repository ID: 1132984639
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

DeepRacer on AWS is the latest evolution of AWS DeepRacer, delivering a self-hosted reinforcement learning solution you can deploy to your AWS account to train and evaluate autonomous-driving models in a 3D simulated environment.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:12:41+00:00

### Short excerpt (up to 100 words)

> DeepRacer on AWS is a solution that allows you to train and evaluate reinforcement learning models in a three-dimensional simulated autonomous-driving environment. The trained model can then be downloaded to a AWS DeepRacer vehicle (a 1/18th scale RC car capable of running inference on a trained AWS DeepRacer model for autonomous driving) so it can drive in a physical environment. You can also submit your model to a virtual race and have its performance ranked against other models in a virtual leaderboard. Deploying this solution with the default parameters deploys the following components in your AWS account. The diagram groups

### README headings

- DeepRacer on AWS
- Overview
- Architecture
- Components
- Package layout
- Repository structure
- Deployment
- Creating a custom build
- Prerequisites
- Install Java
- Install Node
- Install nvm
- Install Node v22
- Install pnpm
- Install Nx globally (optional)
- Download or clone this repo
- Install dependencies
- After introducing changes, run the unit tests to make sure the customizations don't break existing functionality
- Build and deploy the solution using the accompanying build scripts
- Launch the CloudFormation template
- Build and deploy the solution using CDK deploy
- Set environment variables
- Configuration
- Bootstrap CDK (if not already done)
- Build
- Deploy
- Collection of Operational Metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 6,822,690 |
| Python | 170,377 |
| Smithy | 100,882 |
| Shell | 54,950 |
| JavaScript | 50,475 |
| CSS | 24,778 |
| Dockerfile | 2,066 |
| HTML | 488 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/package.json (capture: captured) — dependency clues: @aws-lambda-powertools/logger, @aws-lambda-powertools/metrics, @aws-lambda-powertools/tracer, @aws-sdk/client-appconfig, @aws-sdk/client-appconfigdata, @aws-sdk/client-cloudwatch-logs, @aws-sdk/client-kinesis-video, @aws-sdk/client-kinesis-video-archived-media, @aws-sdk/client-kinesis-video-media, @aws-sdk/client-lambda, @aws-sdk/client-s3, @aws-sdk/client-sagemaker, @aws-sdk/client-service-quotas, @aws-sdk/client-sfn, @aws-sdk/client-sqs, @aws-sdk/client-ssm, @aws-sdk/client-sts, @nx/eslint, @nx/eslint-plugin, @nx/js
- deployment/cdk-solution-helper/package.json (capture: captured)
- source/apps/infra/package.json (capture: captured) — dependency clues: @aws-smithy/server-apigateway, @aws-smithy/server-common, @aws-solutions-constructs/aws-cloudfront-s3, @aws-solutions-constructs/aws-wafwebacl-apigateway, @deepracer-indy/config, @deepracer-indy/database, @deepracer-indy/typescript-server-client, @types/aws-lambda, @types/js-yaml, aws-cdk, aws-cdk-lib, constructs, esbuild, js-yaml, uuid, vitest
- source/apps/website/package.json (capture: captured) — dependency clues: @aws-amplify/ui-react, @aws-crypto/sha256-browser, @aws-sdk/lib-storage, @aws-sdk/signature-v4, @cloudscape-design/board-components, @cloudscape-design/code-view, @cloudscape-design/collection-hooks, @cloudscape-design/components, @cloudscape-design/design-tokens, @cloudscape-design/global-styles, @deepracer-indy/config, @deepracer-indy/typescript-client, @hookform/devtools, @hookform/resolvers, @react-three/drei, @react-three/fiber, @reduxjs/toolkit, @storybook/addon-actions, @storybook/addon-console, @storybook/addon-essentials
- source/libs/config/package.json (capture: captured)
- source/libs/database/package.json (capture: captured) — dependency clues: @aws-sdk/client-dynamodb, @aws-sdk/lib-dynamodb, @aws-sdk/util-dynamodb, @deepracer-indy/config, @deepracer-indy/typescript-server-client, @deepracer-indy/utils, electrodb, fractional-indexing, nanoid, vitest-dynamodb-lite

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 29
- Forks at capture: 8
- Last updated: 2026-11-10T15:16:44Z
- Last pushed: 2026-11-19T16:32:50Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/deepracer-on-aws)
- [README](https://github.com/aws-solutions/deepracer-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/deepracer-on-aws/issues)
- [Releases](https://github.com/aws-solutions/deepracer-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
