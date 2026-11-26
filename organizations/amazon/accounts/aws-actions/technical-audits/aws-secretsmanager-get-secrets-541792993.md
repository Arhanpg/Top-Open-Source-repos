# aws-actions/aws-secretsmanager-get-secrets

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/aws-secretsmanager-get-secrets
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:31:32+00:00

## Project purpose

To use a secret in a GitHub job, you can use a GitHub action to retrieve secrets from AWS Secrets Manager and add them as masked Environment variables in your GitHub workflow. For more information about GitHub Actions, see Understanding GitHub Actions in the *GitHub Docs*.

## Why this project is used

To use a secret in a GitHub job, you can use a GitHub action to retrieve secrets from AWS Secrets Manager and add them as masked Environment variables in your GitHub workflow. For more information about GitHub Actions, see Understanding GitHub Actions in the *GitHub Docs*.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @aws-sdk/client-secrets-manager, @eslint/eslintrc, @eslint/js, @smithy/node-http-handler, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @vercel/ncc, aws-sdk-client-mock, aws-sdk-client-mock-jest, eslint, generate-license-file, jest, proxy-agent, ts-jest
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/index.ts, src/cleanup.ts, src/constants.ts, src/proxy.ts

## Setup and usage

- Usage: To use the action, add a step to your workflow that uses the following syntax.
- Usage: uses: aws-actions/aws-secretsmanager-get-secrets@v4
- Usage: ENV_VAR_NAME, secretId2
- Usage: name-transformation: (Optional) uppercase|lowercase|none
- Usage: parse-json-secrets: (Optional) true|false
- Usage: auto-select-family-attempt-timeout: (Optional) positive integer
- Usage: http-proxy: (Optional) proxy URL
- Usage: no-proxy: (Optional) comma-separated hosts

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-actions/aws-secretsmanager-get-secrets/blob/main/README.md
- README SHA: fc3144ec3872345e4d87fc3f0b35d2b76cc6973e
- Manifests: package.json
- Sampled source files: src/index.ts, src/cleanup.ts, src/constants.ts, src/proxy.ts
- Git tree state: captured
- Evidence fingerprint: e9fc542cca0adad4a4b993e5659735cb032fc82cfbb91723ae83a656f50aff2f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
