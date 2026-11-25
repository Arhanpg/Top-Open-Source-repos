# cdklabs/aws-delivlib

- Company: Amazon
- Account: cdklabs
- Repository: https://github.com/cdklabs/aws-delivlib
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:05:58+00:00

## Project purpose

**aws-delivlib** is a fabulous library for defining continuous pipelines for building, testing and publishing code libraries through AWS CodeBuild and AWS CodePipeline.

## Why this project is used

setup and manage continuous delivery pipelines for code libraries in multiple languages

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, Shell, JavaScript, PowerShell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-sdk/client-cloudwatch, @aws-sdk/client-codepipeline, @aws-sdk/client-s3, @aws-sdk/client-secrets-manager, @aws-sdk/client-ssm, @babel/plugin-transform-modules-commonjs, @stylistic/eslint-plugin, @types/adm-zip, @types/aws-lambda, @types/changelog-parser, @types/follow-redirects, @types/fs-extra, @types/jest, @types/node, @types/tar, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, JSONStream, adm-zip, aws-cdk, aws-cdk-lib, cdklabs-projen-project-types, changelog-parser, commit-and-tag-version, constructs, esbuild, eslint, eslint-import-resolver-typescript, eslint-plugin-import, follow-redirects, fs-extra, jest, jest-junit, minipass, node-ical, octokit, projen, rrule, standard-version, tar, ts-jest, ts-node, typescript
- Build/package tools: Docker build configuration, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lib/change-control-lambda/index.ts, lib/chime-notifier/index.ts, lib/code-signing/index.ts, lib/index.ts

## Setup and usage

- Installation: To install, use npm / yarn:
- Installation: $ yarn add aws-delivlib
- Installation: and import the library to your project:
- Installation: import delivlib = require('aws-delivlib');
- Installation: The next step is to add a pipeline to your app. When you define a pipeline, the
- Installation: minimum requirement is to specify the source repository. All other settings are
- Installation: const pipeline = new delivlib.Pipeline(this, 'MyPipeline', {
- Installation: The following sections will describe the various options available in your

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/cdklabs/aws-delivlib/blob/main/README.md
- README SHA: 4b3c3e5f8a7c8e1de25cb0cedccbec91b908e227
- Manifests: package.json, lib/custom-resource-handlers/Dockerfile, lib/publishing/github/package.json, lib/__tests__/registry-sync/docker-asset/Dockerfile, lib/__tests__/package-integrity/handler/__fixtures__/non-projen-project/package.json
- Sampled source files: lib/change-control-lambda/index.ts, lib/chime-notifier/index.ts, lib/code-signing/index.ts, lib/index.ts
- Git tree state: captured
- Evidence fingerprint: e6f8575c80303111ea1d0cee71e9fc9b781b629c30149f6476d8a28b0bc57f06

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
