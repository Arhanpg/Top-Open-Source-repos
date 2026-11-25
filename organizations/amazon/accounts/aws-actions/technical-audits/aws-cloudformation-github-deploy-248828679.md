# aws-actions/aws-cloudformation-github-deploy

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/aws-cloudformation-github-deploy
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:52:08+00:00

## Project purpose

Deploys AWS CloudFormation Stacks.

## Why this project is used

Deploys AWS CloudFormation Stacks

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @aws-sdk/client-cloudformation, @aws-sdk/client-s3, @smithy/node-http-handler, @types/jest, @types/js-yaml, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @vercel/ncc, aws-sdk-client-mock, aws-sdk-client-mock-jest, eslint, eslint-config-prettier, eslint-plugin-github, eslint-plugin-jest, eslint-plugin-prettier, fast-check, https-proxy-agent, husky, jest, jest-circus, js-yaml, lint-staged, prettier, ts-jest, typescript, zod
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/changeset-formatter.ts, src/deploy.ts, src/event-streaming.ts, src/main.ts

## Setup and usage

- Usage: - name: Deploy to AWS CloudFormation
- Usage: uses: aws-actions/aws-cloudformation-github-deploy@v2.0.0
- Usage: template: myStack.yaml
- Usage: parameter-overrides: 'MyParam1=myValue,MyParam2=${{ secrets.MY_SECRET_VALUE }}'
- Usage: The action can be passed a CloudFormation Stack name and a template file. The template file can be a local file existing in the working directory, or a URL to template that exists in an Amazon S3 bucket. It will create the Stack if it does not exist, or create a Change Set to update the Stack. An update fails by default when the Change Set is empty

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-actions/aws-cloudformation-github-deploy/blob/master/README.md
- README SHA: 87ea800e0ff29eec5f65ec95b80e899eb2e13d04
- Manifests: package.json
- Sampled source files: src/changeset-formatter.ts, src/deploy.ts, src/event-streaming.ts, src/main.ts
- Git tree state: captured
- Evidence fingerprint: a3885f3f65df7c1abc19bfc568774c0506077970da5e2a5301da612832f4371b

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
