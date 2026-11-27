# aws-actions/configure-aws-credentials

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/configure-aws-credentials
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:05:20+00:00

## Project purpose

Authenticate to AWS in GitHub Actions (and others)! Works especially well with [AWS Secrets Manager][secretsmanager].

## Why this project is used

Configure AWS credential environment variables for use in other GitHub Actions.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @aws-sdk/client-sts, @aws-sdk/credential-provider-env, @aws-sdk/credential-provider-node, @biomejs/biome, @smithy/node-http-handler, @smithy/property-provider, @types/node, @vitest/coverage-v8, aws-sdk-client-mock, esbuild, generate-license-file, json-schema, markdownlint-cli, memfs, proxy-agent, standard-version, typescript, vitest
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/cleanup/index.ts, src/index.ts, src/assumeRole.ts, src/CredentialsClient.ts

## Setup and usage

- Quick Start (OIDC, recommended): 1. Create an IAM Identity Provider in your AWS account for GitHub OIDC. (See
- Quick Start (OIDC, recommended): OIDC configuration below for details.)
- Quick Start (OIDC, recommended): 2. Create an IAM Role in your AWS account with a trust policy that allows GitHub
- Quick Start (OIDC, recommended): Actions to assume it. (Expand the sections below)
- Quick Start (OIDC, recommended): GitHub OIDC Trust Policy
- Quick Start (OIDC, recommended): "Version": "2012-10-17",
- Quick Start (OIDC, recommended): "Federated": "arn:aws:iam:: :oidc-provider/token.actions.githubusercontent.com"
- Quick Start (OIDC, recommended): "Action": "sts:AssumeRoleWithWebIdentity",

## Limitations and caveats

- Security Recommendations: - Use temporary credentials when possible. OIDC is recommended because it
- Security Recommendations: provides temporary credentials and it's easy to set up.
- Security Recommendations: - Do not store credentials in your repository's code. Consider using
- Security Recommendations: git-secrets to prevent committing
- Security Recommendations: secrets to your repository.
- Security Recommendations: - Grant least privilege
- Security Recommendations: to your workflows. Grant only those permissions that are necessary for the
- Security Recommendations: - Monitor the activity

## Evidence and provenance

- README: https://github.com/aws-actions/configure-aws-credentials/blob/main/README.md
- README SHA: cf509270d5114a0fa95b60a5d037dbe7e4b128ef
- Manifests: package.json
- Sampled source files: src/cleanup/index.ts, src/index.ts, src/assumeRole.ts, src/CredentialsClient.ts
- Git tree state: captured
- Evidence fingerprint: 727f82364b2f2c92f08612f3f54e3176a8d87dcbd01d1de86958b6115da786eb

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
