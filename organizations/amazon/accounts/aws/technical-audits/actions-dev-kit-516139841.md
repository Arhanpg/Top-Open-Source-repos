# aws/actions-dev-kit

- Company: Amazon
- Account: aws
- Repository: https://github.com/aws/actions-dev-kit
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:45:41+00:00

## Project purpose

Amazon CodeCatalyst provides software development teams one place to plan work, collaborate on code, and build, test, and deploy applications with continuous integration/continuous delivery (CI/CD) tools. For more information, see What is Amazon CodeCatalyst?

## Why this project is used

Amazon CodeCatalyst provides software development teams one place to plan work, collaborate on code, and build, test, and deploy applications with continuous integration/continuous delivery (CI/CD) tools. For more information, see What is Amazon CodeCatalyst?

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: HTML, TypeScript, CSS, JavaScript, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws/codecatalyst-adk-core, @aws/codecatalyst-adk-model-parser, @aws/codecatalyst-adk-utils, @nestjs/common, @nestjs/core, @tsconfig/node12, @types/jest, @types/js-yaml, @types/jsonwebtoken, @types/node, @types/shelljs, @types/yargs, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, chalk, eslint, eslint-plugin-import, eslint-plugin-jest, fs-extra, graceful-fs, jest, jest-junit, js-yaml, jsii, jsii-diff, jsii-docgen, jsii-pacmak, jsii-rosetta, json5, jsonschema, jsonwebtoken, reflect-metadata, rxjs, shelljs, ts-node, tsconfig-paths, typedoc, typescript, yargs
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: packages/adk-model-parser/lib/index.ts, packages/adk-utils/lib/index.ts, packages/adk/lib/index.ts, packages/adk/templates/action/typescript/lib/index.ts

## Setup and usage

- Sample Usage: import * as core from '@aws/codecatalyst-adk-core';
- Sample Usage: import * as project from '@aws/codecatalyst-project';
- Sample Usage: import { RunSummaryLevel, RunSummaries } from '@aws/codecatalyst-run-summaries';
- Sample Usage: import * as space from '@aws/codecatalyst-space';
- Sample Usage: const destinationBucket = core.getInput('DestinationBucketName')
- Sample Usage: # => Maps to the destination bucket configuration in CodeCatalyst workflow definition
- Sample Usage: const srcDir = core.getInput('SourcePath')
- Sample Usage: # => Maps to the src dir configuration in CodeCatalyst workflow definition

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws/actions-dev-kit/blob/main/README.md
- README SHA: 7f396830645153db115c72d30dc7bd058883e11f
- Manifests: package.json, packages/adk-core/package.json, packages/adk-model-parser/package.json, packages/adk-utils/package.json, packages/adk/package.json, packages/codecatalyst-entities/project/package.json
- Sampled source files: packages/adk-model-parser/lib/index.ts, packages/adk-utils/lib/index.ts, packages/adk/lib/index.ts, packages/adk/templates/action/typescript/lib/index.ts
- Git tree state: captured
- Evidence fingerprint: b7017f28ff1de9e32d9a4941d08e289e214d59b51756e0a5aff66ad01f9182c5

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
