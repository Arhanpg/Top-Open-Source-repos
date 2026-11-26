# cdklabs/awscdk-change-analyzer

- Company: Amazon
- Account: cdklabs
- Repository: https://github.com/cdklabs/awscdk-change-analyzer
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:22:00+00:00

## Project purpose

The **CDK Change Analyzer** (C2A) is a tool that helps you:

## Why this project is used

A toolkit that analyzes the differences between two cloud infrastructures states.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: HTML, TypeScript, JavaScript, Shell, CSS
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-c2a/engine, @aws-c2a/models, @aws-c2a/presets, @aws-c2a/rules, @aws-c2a/visualizer, @aws-c2a/web-app, @aws-cdk/assert, @aws-cdk/aws-appsync, @aws-cdk/aws-codebuild, @aws-cdk/aws-codepipeline, @aws-cdk/aws-codepipeline-actions, @aws-cdk/aws-ec2, @aws-cdk/aws-iam, @aws-cdk/aws-lambda, @aws-cdk/aws-s3, @aws-cdk/aws-s3-assets, @aws-cdk/aws-secretsmanager, @aws-cdk/aws-sns, @aws-cdk/aws-sqs, @aws-cdk/cfnspec, @aws-cdk/cloud-assembly-schema, @aws-cdk/core, @aws-cdk/cx-api, @aws-cdk/pipelines, @babel/core, @babel/preset-env, @babel/preset-typescript, @types/aws-sdk, @types/graphviz, @types/jest, @types/node, @types/semver, @types/string-similarity, @types/yaml, @types/yargs, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-sdk, babel-jest, babel-plugin-inline-import, colors, constructs, eslint, eslint-plugin-import, fifinet, graphviz, jest, jsii, jsii-pacmak, lerna, minimatch, rimraf, semver, ts-jest, ts-node, tsconfig-paths, typescript, yaml, yargs
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: packages/@aws-c2a/cdk-pipelines-step/lib/index.ts, packages/@aws-c2a/cdk-pipelines-step/lib/private/approve-lambda/index.ts, packages/@aws-c2a/engine/lib/aggregations/component-operation/aggregation-modules/index.ts, packages/@aws-c2a/engine/lib/aggregations/index.ts

## Setup and usage

- Usage: 1. Add a [PerformChangeAnalysis
- Usage: step](https://github.com/cdklabs/awscdk-change-analyzer/tree/main/packages/%40aws-c2a/cdk-pipelines-step) to your CDK pipeline.
- Usage: 2. Create a JSON file to encode your own
- Usage: to save yourself manual reviewing time.

## Limitations and caveats

- Security: See CONTRIBUTING for more

## Evidence and provenance

- README: https://github.com/cdklabs/awscdk-change-analyzer/blob/main/README.md
- README SHA: 2130bc3ca35e6ab8aa84e86fe4e57aeb14a5d694
- Manifests: package.json, packages/aws-c2a/package.json, packages/@aws-c2a/cdk-pipelines-step/package.json, packages/@aws-c2a/engine/package.json, packages/@aws-c2a/models/package.json, packages/@aws-c2a/presets/package.json
- Sampled source files: packages/@aws-c2a/cdk-pipelines-step/lib/index.ts, packages/@aws-c2a/cdk-pipelines-step/lib/private/approve-lambda/index.ts, packages/@aws-c2a/engine/lib/aggregations/component-operation/aggregation-modules/index.ts, packages/@aws-c2a/engine/lib/aggregations/index.ts
- Git tree state: captured
- Evidence fingerprint: eac7ac0d6e8b53da1b0ec8c108c7adb75141ec98e5e2fecfa938fbd3a83f442f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
