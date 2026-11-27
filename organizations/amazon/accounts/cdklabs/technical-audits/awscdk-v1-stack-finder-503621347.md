# cdklabs/awscdk-v1-stack-finder

- Company: Amazon
- Account: cdklabs
- Repository: https://github.com/cdklabs/awscdk-v1-stack-finder
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:07:04+00:00

## Project purpose

Command line tool to identify stacks that were deployed with AWS CDK V1 (as opposed to V2). You can use this to help with the migration process from V1 to V2.

## Why this project is used

Command line tool to identify stacks that were deployed with AWS CDK V1 (as opposed to V2). You can use this to help with the migration process from V1 to V2.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-sdk, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, projen, ts-jest, ts-node, typescript, yaml
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/index.ts, src/cli.ts, .projenrc.ts

## Setup and usage

- Usage: Configure you AWS credentials as normal, and run:
- Usage: npx awscdk-v1-stack-finder
- Usage: To use a profile, run:
- Usage: AWS_SDK_LOAD_CONFIG=1 AWS_PROFILE= npx awscdk-v1-stack-finder
- Usage: By default, this will scan all regions in your account (apart from us-iso-east-1 and us-iso-west-1)
- Usage: and print the stacks that were deployed with AWS CDK V1:
- Usage: ❯ npx awscdk-v1-stack-finder
- Usage: us-east-1: fetching stacks

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/cdklabs/awscdk-v1-stack-finder/blob/main/README.md
- README SHA: 01aa696131e1d3e2388db1783c6ca8a20103f953
- Manifests: package.json
- Sampled source files: src/index.ts, src/cli.ts, .projenrc.ts
- Git tree state: captured
- Evidence fingerprint: 8ec6b56076a32a01be153ef46027e09c7374d89b35ead81c179d5a8cf97d3147

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
