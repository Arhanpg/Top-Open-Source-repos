# mindsphere/node-red-contrib-mindconnect

- Company: Siemens
- Account: mindsphere
- Repository: https://github.com/mindsphere/node-red-contrib-mindconnect
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:54:48+00:00

## Project purpose

> [!WARNING] > **v4: migrated Insights Hub tenants only.** > Version 4 supports tenants migrated to the *.siemens.app application URL scheme. > **If your tenant still uses *.mindsphere.io application URLs, stay on v3. Do not upgrade to v4.** > This is v4 - verified against a migrated (*.siemens.app) tenant. If your tenant is still on > *.mindsphere.io, install the v3 release instead (npm install @mindconnect/node-red-contrib-mindconnect@3).

## Why this project is used

Node-RED Agent for the Siemens Insights Hub MindConnect API

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: HTML, TypeScript, CSS, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: @compodoc/compodoc, @mindconnect/mindconnect-nodejs, @types/ajv, @types/chai, @types/mocha, @types/node, @types/node-fetch, ajv, ajv-formats, chai, concurrently, cross-env, debug, license-checker, mocha, mocha-jenkins-reporter, node-fetch, node-red, node-red-node-test-helper, nodemon, nyc, tslint, typescript, typescript-tslint-plugin
- Build/package tools: Docker build configuration, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/http-handlers.ts, src/mindconnect-ops.ts, src/mindconnect-schema.ts, src/mindconnect-utils.ts

## Setup and usage

- Node-RED - Manage Palette Installation: You can install the node also via the Manage palette feature in the Node-RED administration UI.
- Node-RED - Manage Palette Installation: **Legacy tenants must keep v3 installed and must not accept a v4 upgrade.**
- Node-RED - Manage Palette Installation: If the palette does not offer a version choice, use the explicit v3 installation command above.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/mindsphere/node-red-contrib-mindconnect/blob/master/README.md
- README SHA: 9ea4c19b98daf1224e4c6048d486d9f177c6fdf3
- Manifests: Dockerfile, package.json
- Sampled source files: src/http-handlers.ts, src/mindconnect-ops.ts, src/mindconnect-schema.ts, src/mindconnect-utils.ts
- Git tree state: captured
- Evidence fingerprint: a13e0f8b8cddd6e095e59e2b4249e6252cd5a5222f9186ce8e1a0de22e11b562

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
