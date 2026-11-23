# cdklabs/awscdk-change-analyzer

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/awscdk-change-analyzer](https://github.com/cdklabs/awscdk-change-analyzer)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/awscdk-change-analyzer/blob/main/README.md)
- README blob SHA: 2130bc3ca35e6ab8aa84e86fe4e57aeb14a5d694
- Repository ID: 361684977
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A toolkit that analyzes the differences between two cloud infrastructures states.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:08:27+00:00

### Short excerpt (up to 100 words)

> The **CDK Change Analyzer** (C2A) is a tool that helps you: * Review the changes that a CDK deployment will introduce to your infrastructure in a visual interface. * Write rules to automatically classify certain changes as "safe" or "unsafe", making sure you only need to review changes if there is something important to review. CDK Change Analyzer can be used independently, or as an integration with [CDK Pipelines](https://github.com/cdklabs/awscdk-change-analyzer/tree/main/packages/%40aws-c2a/cdk-pipelines-step). To use C2A: 1. Add a [PerformChangeAnalysis step](https://github.com/cdklabs/awscdk-change-analyzer/tree/main/packages/%40aws-c2a/cdk-pipelines-step) to your CDK pipeline. 2. Create a JSON file to encode your own to save yourself manual reviewing time. The CDK Change Analyzer

### README headings

- AWS CDK Change Analyzer
- Usage
- Repository Structure
- Developing
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HTML | 5,591,394 |
| TypeScript | 434,702 |
| JavaScript | 15,105 |
| Shell | 802 |
| CSS | 91 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: lerna
- packages/aws-c2a/package.json (capture: captured) — dependency clues: @aws-c2a/engine, @aws-c2a/models, @aws-c2a/presets, @aws-c2a/rules, @aws-c2a/visualizer, @aws-c2a/web-app, @aws-cdk/aws-appsync, @aws-cdk/aws-ec2, @aws-cdk/aws-iam, @aws-cdk/aws-s3, @aws-cdk/aws-sns, @aws-cdk/aws-sqs, @aws-cdk/cfnspec, @aws-cdk/cloud-assembly-schema, @aws-cdk/core, @aws-cdk/cx-api, @babel/core, @babel/preset-env, @babel/preset-typescript, @types/aws-sdk
- packages/@aws-c2a/cdk-pipelines-step/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-codebuild, @aws-cdk/aws-codepipeline, @aws-cdk/aws-codepipeline-actions, @aws-cdk/aws-iam, @aws-cdk/aws-lambda, @aws-cdk/aws-s3, @aws-cdk/aws-s3-assets, @aws-cdk/aws-secretsmanager, @aws-cdk/aws-sns, @aws-cdk/cfnspec, @aws-cdk/core, @aws-cdk/cx-api, @aws-cdk/pipelines, @babel/core, @babel/preset-env, @babel/preset-typescript, @types/jest, @types/node, @types/string-similarity
- packages/@aws-c2a/engine/package.json (capture: captured) — dependency clues: @aws-c2a/models, @aws-c2a/rules, @aws-cdk/cfnspec, @aws-cdk/core, @babel/core, @babel/preset-env, @babel/preset-typescript, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, babel-jest, eslint, eslint-plugin-import, fifinet, graphviz, jest, rimraf, ts-jest, ts-node
- packages/@aws-c2a/models/package.json (capture: captured) — dependency clues: @aws-cdk/cfnspec, @babel/core, @babel/preset-env, @babel/preset-typescript, @types/jest, @types/node, @types/yaml, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, babel-jest, eslint, fifinet, jest, ts-jest, ts-node, typescript
- packages/@aws-c2a/presets/package.json (capture: captured) — dependency clues: @aws-c2a/engine, @aws-c2a/models, @aws-c2a/rules, @aws-cdk/core, @babel/core, @babel/preset-env, @babel/preset-typescript, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, babel-jest, eslint, eslint-plugin-import, fifinet, jest, ts-jest, ts-node, tsconfig-paths, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 13
- Forks at capture: 2
- Last updated: 2023-10-02T14:38:04Z
- Last pushed: 2022-06-29T08:12:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/awscdk-change-analyzer)
- [README](https://github.com/cdklabs/awscdk-change-analyzer/blob/main/README.md)
- [Issues](https://github.com/cdklabs/awscdk-change-analyzer/issues)
- [Releases](https://github.com/cdklabs/awscdk-change-analyzer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
