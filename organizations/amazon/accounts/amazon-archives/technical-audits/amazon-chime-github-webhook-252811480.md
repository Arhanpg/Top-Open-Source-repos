# amazon-archives/amazon-chime-github-webhook

- Company: Amazon
- Account: amazon-archives
- Repository: https://github.com/amazon-archives/amazon-chime-github-webhook
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T23:07:29+00:00

## Project purpose

Send message to Amazon Chime chat rooms.

## Why this project is used

Send a message to Amazon Chime chat rooms

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @zeit/ncc, chime, eslint, eslint-config-prettier, eslint-plugin-github, eslint-plugin-jest, eslint-plugin-prettier, husky, jest, jest-circus, js-yaml, prettier, ts-jest, typescript
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/main.ts, __tests__/main.test.ts, jest.config.js

## Setup and usage

- Usage: - name: Send message to Amazon Chime chat room
- Usage: uses: aws-actions/amazon-chime-github-webhook@v1
- Usage: webhook: ${{ secrets.webhook }}
- Usage: The action can be passed a webhook URL and message to be send to a Amazon Chime chat room. webook should be defined as an encrypted secret and not be exposed directly.
- Usage: See action.yml for the full documentation for this action's inputs and outputs.
- Usage: > You can learn more about creating an Amazon Chime Webhook and about Amazon Chime

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/amazon-archives/amazon-chime-github-webhook/blob/master/README.md
- README SHA: fb91690d92121d1b33714a3cf3eb2cd3a272dc35
- Manifests: package.json
- Sampled source files: src/main.ts, __tests__/main.test.ts, jest.config.js
- Git tree state: captured
- Evidence fingerprint: c68d18619c8d801ae5e261efe44644ecd26c557f7517592a0d2c4571323e6929

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
