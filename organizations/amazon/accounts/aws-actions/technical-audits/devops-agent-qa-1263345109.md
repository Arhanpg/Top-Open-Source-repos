# aws-actions/devops-agent-qa

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/devops-agent-qa
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:12:08+00:00

## Project purpose

A GitHub Action that triggers the AWS DevOps Release Testing Agent after deployment. It automatically runs UI or API tests against your application and reports results as a GitHub Check Run on your commit.

## Why this project is used

A GitHub Action that triggers the AWS DevOps Release Testing Agent after deployment. It automatically runs UI or API tests against your application and reports results as a GitHub Check Run on your commit.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @actions/github, @types/node, @vercel/ncc, typescript
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/index.ts

## Setup and usage

No setup information established.

## Limitations and caveats

- Limitations: - **Guest mode only** — no authenticated testing. If you need login flows, use a test profile.
- Limitations: - **API specs must fit in the webhook payload** — for specs exceeding ~1MB, use a test profile instead.
- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-actions/devops-agent-qa/blob/main/README.md
- README SHA: f954b06f60c3b2f1a9f4424d3c8ecbfbea7fab15
- Manifests: package.json
- Sampled source files: src/index.ts
- Git tree state: captured
- Evidence fingerprint: be20208940b9a91aac6c1b96fa381cba9d6fd645ab8786b8703f71e3eb0fd469

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
