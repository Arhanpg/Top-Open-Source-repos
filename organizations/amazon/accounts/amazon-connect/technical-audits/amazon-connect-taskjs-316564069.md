# amazon-connect/amazon-connect-taskjs

- Company: Amazon
- Account: amazon-connect
- Repository: https://github.com/amazon-connect/amazon-connect-taskjs
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:24:33+00:00

## Project purpose

The Amazon Connect Task javascript library (TaskJS) gives you the power to handle task contacts when used together with Amazon Connect Streams.

## Why this project is used

Amazon Connect Task JS - a browser-based contact center integration API for Tasks.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @babel/core, @babel/preset-env, babel-loader, copy-webpack-plugin, eslint, eslint-config-prettier, eslint-webpack-plugin, jest, ssri, webpack, webpack-cli
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/index.js, src/constants.js, src/core/agentApis.js, src/core/agentApis.spec.js

## Setup and usage

- Usage:: TaskJS provides a taskSession instance for each task contact. You can access the taskSession by calling the getMediaController method on a taskConnection. getMediaController returns a promise that resolves with a taskSession instance.
- Usage:: taskConnection.getMediaController().then((taskSession) => { /* ... */ });

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/amazon-connect/amazon-connect-taskjs/blob/main/README.md
- README SHA: 66d86c8a5de7cd5469b048441a16f1124ae72df8
- Manifests: package.json
- Sampled source files: src/index.js, src/constants.js, src/core/agentApis.js, src/core/agentApis.spec.js
- Git tree state: captured
- Evidence fingerprint: 7a2e4fd57cede127b39e7ce9ca8f131de1537100cd7e38fc0321e95e0d09f1e6

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
