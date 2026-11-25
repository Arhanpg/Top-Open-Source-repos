# aws-ia/addons-transformer-for-amazon-eks

- Company: Amazon
- Account: aws-ia
- Repository: https://github.com/aws-ia/addons-transformer-for-amazon-eks
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:54:35+00:00

## Project purpose

Addons Transformer CLI for Amazon EKS =====================================

## Why this project is used

Addons Transformer to transform ISV Softwares to EKS Marketplace

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, Shell, Makefile, JavaScript, Batchfile
- Frameworks/libraries: Unknown / not established
- Dependency names: @inquirer/prompts, @inquirer/select, @oclif/core, @oclif/plugin-help, @oclif/prettier-config, @oclif/test, @octokit/core, @types/ajv, @types/chai, @types/fs-extra, @types/inquirer, @types/js-yaml, @types/mocha, @types/node, ajv, chai, eslint, eslint-config-oclif, eslint-config-oclif-typescript, eslint-config-prettier, js-yaml, json-schema, mocha, oclif, shx, ts-node, typescript
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/index.ts, src/commandOpts/create-issue.ts, src/commandOpts/validate.ts, src/commands/create-issue.ts

## Setup and usage

- Cloud Shell Installation: To quickly get started with this transformer, you can leverage CloudShell in the AWS Console. Some prerequisites you need:
- Cloud Shell Installation: * Access to the helm chart to pull it
- Cloud Shell Installation: * Install the Helm CLI in CloudShell using the following commands:
- Cloud Shell Installation: $ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
- Cloud Shell Installation: $ chmod 700 get_helm.sh
- Cloud Shell Installation: * A GitHub token as required by The GitHub Service
- Cloud Shell Installation: To use this CLI in CloudShell,
- Cloud Shell Installation: * Log into the AWS Console with a role that has access to the location of the helm chart

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-ia/addons-transformer-for-amazon-eks/blob/main/README.md
- README SHA: 0f4dbf9cbb32fc6782740ef2e07ec2154c69ecf7
- Manifests: Makefile, package.json
- Sampled source files: src/index.ts, src/commandOpts/create-issue.ts, src/commandOpts/validate.ts, src/commands/create-issue.ts
- Git tree state: captured
- Evidence fingerprint: 88fb2364603ffb96180985b0d0a6e90f31081aee588a9e11ebb6c8f2baac348f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
