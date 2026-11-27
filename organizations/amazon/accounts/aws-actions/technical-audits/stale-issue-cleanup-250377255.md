# aws-actions/stale-issue-cleanup

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/stale-issue-cleanup
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:24:57+00:00

## Project purpose

This GitHub action warns and then closes issues and PRs without activity after a specified amount of time. It improves upon [GitHub's original stale action](https://github.com/actions/stale) by allowing the action to run only on issues that contain a specified label, and removing labels once the issue sees new activity.

## Why this project is used

Clean up stale issues in your repository with GitHub Actions!

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @actions/github, @biomejs/biome, @fetch-mock/vitest, @octokit/plugin-rest-endpoint-methods, @types/dateformat, @types/node, @vercel/ncc, @vitest/coverage-v8, dateformat, dotenv, typescript, vitest
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/entrypoint.ts, src/github.ts, src/utils.ts, vitest.config.ts

## Setup and usage

- Usage: You need to add a workflow file into your repository under
- Usage: .github/workflows, just like any other Github Action.
- Usage: This workflow file follows the standard workflow syntax for Github Actions..
- Usage: A sample workflow file for you to use as a drop-in is in sample_workflow.yml.
- Usage: For a list of options and their description, see action.yml.
- Usage: Here's an abbreviated example with just the step for this action:
- Usage: - uses: aws-actions/stale-issue-cleanup@v7.1.0
- Usage: # Types of issues that will be processed

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-actions/stale-issue-cleanup/blob/main/README.md
- README SHA: b003303161ee01ae4d55b776a4b726fc970adb0e
- Manifests: package.json
- Sampled source files: src/entrypoint.ts, src/github.ts, src/utils.ts, vitest.config.ts
- Git tree state: captured
- Evidence fingerprint: c4d0317b63f87bb06ed668d4eba8b12790c8210589b1dc538d3d615d9ddc2e69

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
