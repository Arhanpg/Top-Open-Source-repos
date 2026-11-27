# SAP/ai-assisted-github-actions

- Company: SAP
- Account: SAP
- Repository: https://github.com/SAP/ai-assisted-github-actions
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:22:41+00:00

## Project purpose

_Automate your PR workflow with GitHub Actions powered by SAP AI Core. Get instant summaries and reviews—no more manual grunt work._

## Why this project is used

Automate your PR workflow with GitHub Actions powered by SAP AI Core. Get instant summaries and reviews—no more manual grunt work.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @actions/github, @eslint/js, @octokit/action, @octokit/plugin-retry, @octokit/plugin-throttling, @octokit/webhooks, @sap-ai-sdk/ai-api, @sap-ai-sdk/orchestration, @types/node, @vercel/ncc, axios, eslint, eslint-plugin-import, eslint-plugin-sonarjs, eslint-plugin-unicorn, minimatch, mollitia, octokit, parse-diff, prettier, tsx, typescript, typescript-eslint, yaml, zod
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: pr-review/src/index.ts, pr-summary/src/index.ts, pr-review/src/ai-core-client.ts, pr-review/src/config.ts

## Setup and usage

- Usage: Create a GitHub Actions workflow file e.g., .github/workflows/ai-assistance.yml, with the following content:
- Usage: types: [ready_for_review]
- Usage: runs-on: [ubuntu-latest]
- Usage: - uses: SAP/ai-assisted-github-actions/pr-summary@v3
- Usage: aicore-service-key: ${{ secrets.AICORE_SERVICE_KEY }}
- Usage: exclude-files: package-lock.json
- Usage: runs-on: [ubuntu-latest]
- Usage: - uses: SAP/ai-assisted-github-actions/pr-review@v3

## Limitations and caveats

- Security / Disclosure: If you find any bug that may be a security problem, please follow our instructions at in our security policy on how to report it. Please do not create GitHub issues for security-related doubts or problems.

## Evidence and provenance

- README: https://github.com/SAP/ai-assisted-github-actions/blob/main/README.md
- README SHA: 5e87eb6f165da241904fc9b8e1e42ec0da5b8ad4
- Manifests: pr-review/package.json, pr-summary/package.json
- Sampled source files: pr-review/src/index.ts, pr-summary/src/index.ts, pr-review/src/ai-core-client.ts, pr-review/src/config.ts
- Git tree state: captured
- Evidence fingerprint: 61e6fe4370adf613a403cb608570e9519e3bdd6bfa657e97aeedffd0917d697c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
