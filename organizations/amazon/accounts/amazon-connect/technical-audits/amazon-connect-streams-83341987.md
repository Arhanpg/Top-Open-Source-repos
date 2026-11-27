# amazon-connect/amazon-connect-streams

- Company: Amazon
- Account: amazon-connect
- Repository: https://github.com/amazon-connect/amazon-connect-streams
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:17:59+00:00

## Project purpose

The Amazon Connect Streams API (Streams) gives you the power to integrate your existing web applications with Amazon Connect. Streams lets you embed the Contact Control Panel (CCP) and Customer Profiles app UI into your page. It also enables you to handle agent and contact state events directly through an object oriented event driven interface. You can use the built in interface or build your own from scratch: Streams gives you the choice.

## Why this project is used

Amazon Connect Streams - a browser-based contact center integration API, typically with CRM systems.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @amazon-connect/activity, @amazon-connect/contact, @amazon-connect/core, @amazon-connect/site, @amazon-connect/site-streams, @amazon-connect/user, @amazon-connect/voice, @babel/eslint-parser, @babel/preset-env, @babel/preset-typescript, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, amazon-chime-sdk-js, babel-jest, babel-loader, babel-plugin-istanbul, chai, eslint, eslint-config-airbnb-base, eslint-config-airbnb-typescript, eslint-config-prettier, eslint-plugin-import, jest, jest-environment-jsdom, prettier, proxyquire, terser-webpack-plugin, typescript, webpack, webpack-cli
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/agent-app/agent-app.js, src/agent-app/app-registry.js, src/client.js, src/event.js

## Setup and usage

- Usage: amazon-connect-streams is available from npmjs.com. If you'd like to download it here, you can use either of the files like release/connect-streams*.
- Usage: Run npm run release to generate new release files. Full instructions for building locally with npm can be found below.
- Usage: In version 1.x, we also support make for legacy builds. This option was removed in version 2.x.
- Usage with TypeScript: amazon-connect-streams is compatible with TypeScript. You'll need to use version 3.0.1 or higher:
- Usage with TypeScript: import "amazon-connect-streams";
- Usage with TypeScript: connect.core.initCCP({ /* ... */ });

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/amazon-connect/amazon-connect-streams/blob/master/README.md
- README SHA: 2d2e62c3887e6037bdb04c9df116ee845a48984f
- Manifests: package.json
- Sampled source files: src/agent-app/agent-app.js, src/agent-app/app-registry.js, src/client.js, src/event.js
- Git tree state: captured
- Evidence fingerprint: 19ef4d119b40c38de4106f02314c9a55404cca38ab1b851c2310b13d7808b49a

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
