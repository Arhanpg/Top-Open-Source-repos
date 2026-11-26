# mindsphere/mindconnect-nodejs

- Company: Siemens
- Account: mindsphere
- Repository: https://github.com/mindsphere/mindconnect-nodejs
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:44:29+00:00

## Project purpose

> [!WARNING] > ### Breaking change starting with version 4.0.0 > > Insights Hub URLs are migrating from the mindsphere.io domain to the new siemens.app scheme. **Version 4.0.0 and above only work with the new siemens.app URLs** and are **not compatible** with tenants/gateways still using the old mindsphere.io URLs. > > - If your tenant/gateway already uses the new siemens.app URLs, install @mindconnect/mindconnect-nodejs@^4.0.0. > - If your tenant/gateway still uses the old mindsphere.io URLs, keep using @mindconnect/mindconnect-nodejs@^3.0.0 (the 3.x line will continue to work with the old URL scheme). > > **4.0.0 is best-effort compatible with the new Xcelerator gateway** - it has been tested against the current public-cloud regions, but the migration is still in progress and some backend behavior (see below) is known to differ across deployments. **For on-premise/private-cloud install

## Why this project is used

NodeJS Library for Industrial IoT Connectivity - TypeScript SDK for Industrial IoT - Command Line Interface - Development Proxy - typescript-sdk is waiting for your contributions!

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, HTML, JavaScript, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: @compodoc/compodoc, @rollup/plugin-commonjs, @rollup/plugin-json, @rollup/plugin-node-resolve, @types/async-lock, @types/chai, @types/csvtojson, @types/debug, @types/jsonwebtoken, @types/lodash, @types/mocha, @types/node, @types/uuid, ajv, ajv-formats, ajv-keywords, async-lock, chai, chalk, commander, concurrently, copyfiles, cross-env, cross-fetch, csvtojson, date-fns, debug, https-proxy-agent, json-groupby, jsonwebtoken, license-checker, lodash, mime-types, mocha, mocha-jenkins-reporter, nock, ora-classic, performant-array-to-tree, pkg, rimraf, rollup, rollup-plugin-node-polyfills, rollup-plugin-terser, rsa-pem-to-jwk, ts-node, tslib, tslint, typescript, typescript-tslint-plugin, update-notifier-cjs, url-search-params-polyfill, uuid
- Build/package tools: Docker build configuration, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/api/sdk/index.ts, src/index.ts, src/api/agent-auth.ts, src/api/auth-base.ts

## Setup and usage

- Getting started: [](https://developer.siemens.com/industrial-iot-open-source/mindconnect-nodejs/cli/index.html)
- Getting started: The easiest way to start is to use the provided command line interface to create a starter project:

## Limitations and caveats

- Platform Core APIs: | Name |SDK - Client | Command |
- Platform Core APIs: | Identity Management | :heavy_check_mark: | :heavy_check_mark: |
- Platform Core APIs: | Resource Access Management 1 | :heavy_check_mark: | :heavy_check_mark: |
- Platform Core APIs: | Oauth Authorization | :heavy_check_mark: | :heavy_check_mark: |
- Platform Core APIs: | Tenant Management | :heavy_check_mark: | :heavy_check_mark: |
- Platform Core APIs: | Token Management | :heavy_check_mark: | :heavy_check_mark: |
- Platform Core APIs: | Message Broker 2 (preview) | :heavy_check_mark: | :heavy_check_mark: |
- Platform Core APIs: | Usage Transparency | :heavy_check_mark: | |

## Evidence and provenance

- README: https://github.com/mindsphere/mindconnect-nodejs/blob/master/README.md
- README SHA: 53cd9842af0ac90c3e416c930a9ba8be8e3e00dd
- Manifests: Dockerfile, package.json
- Sampled source files: src/api/sdk/index.ts, src/index.ts, src/api/agent-auth.ts, src/api/auth-base.ts
- Git tree state: captured
- Evidence fingerprint: ac9132793262d3437a168757da89d35db96123511a59b5e236e94b4153da2fed

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
