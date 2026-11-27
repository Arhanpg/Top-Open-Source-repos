# aws-actions/handle-non-labeled-issues

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/handle-non-labeled-issues
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:18:52+00:00

## Project purpose

Issues created through the GitHub web interface can have templates applied to them, which allows maintainers to set a label on new issue creation. But there's no way to enforce that a label is applied to an issue when it is created through the API or gh CLI. LLM agents especially prefer to use the API to create issues, which can lead to unlabeled issues being created.

## Why this project is used

Issues created through the GitHub web interface can have templates applied to them, which allows maintainers to set a label on new issue creation. But there's no way to enforce that a label is applied to an issue when it is created through the API or gh CLI. LLM agents especially prefer to use the API to create issues, which can lead to unlabeled issues being created.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @actions/github, @biomejs/biome, @types/node, @vitest/coverage-v8, esbuild, generate-license-file, markdownlint-cli, typescript, vitest
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/index.ts, src/main.ts

## Setup and usage

- Usage: Use this example workflow file:
- Usage: name: Handle Non-labeled Issues
- Usage: handle_non_labeled_issues:
- Usage: runs-on: ubuntu-latest
- Usage: - uses: aws-actions/handle-non-labeled-issues@v1
- Usage: Hi! This issue was created via the API, so it didn't have a label
- Usage: and may be missing some information. Please use the issue template
- Usage: through the GitHub web interface next time to ensure that we have

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-actions/handle-non-labeled-issues/blob/main/README.md
- README SHA: ed6bac5b550784215000a06953a01066f8d595f9
- Manifests: package.json
- Sampled source files: src/index.ts, src/main.ts
- Git tree state: captured
- Evidence fingerprint: 0d1fb1b9001f7de45dc51d2f74d6b7c06f04c04992a86569d19ac20e1ecf9e21

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
