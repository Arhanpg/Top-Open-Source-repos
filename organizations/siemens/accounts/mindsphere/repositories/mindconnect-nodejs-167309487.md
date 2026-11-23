# mindsphere/mindconnect-nodejs

- Company: Siemens
- GitHub account: [https://github.com/mindsphere](https://github.com/mindsphere)
- Mapping status: official-project-linked
- Repository: [mindsphere/mindconnect-nodejs](https://github.com/mindsphere/mindconnect-nodejs)
- Default branch: master
- README: [Open upstream README](https://github.com/mindsphere/mindconnect-nodejs/blob/master/README.md)
- README blob SHA: 53cd9842af0ac90c3e416c930a9ba8be8e3e00dd
- Repository ID: 167309487
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NodeJS Library for Industrial IoT Connectivity - TypeScript SDK for Industrial IoT - Command Line Interface - Development Proxy - typescript-sdk is waiting for your contributions!

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:50:20+00:00

### Short excerpt (up to 100 words)

> Version 4.0.0 talks to the new Xcelerator gateway (`siemens.app`) instead of the classic Insights Hub gateway (`mindsphere.io`). A few things changed as a consequence, and a couple of rough edges (outside this library's control) are worth knowing about: - **Tenant name vs. tenant/identity-zone id (CLI/SDK credentials only)**: Xcelerator distinguishes between the tenant **name** (used in asset-model qualified names, e.g. `mytenant.MyAspectType`) and a numeric **identity-zone/customer tenant id** (required by the OAuth token endpoint). This only concerns `mc service-credentials` (APP/SERVICE credentials used by CLI/SDK commands like `mc aspects`/`mc assets`) - it has no effect on agent onboarding/`mc agent-token`, which derives its tenant

### README headings

- Migrating to the Xcelerator gateway (4.0.0)
- Full documentation
- Installing the library
- install the latest stable library from the npm registry (v4+, requires the new siemens.app URL scheme)
- install the latest alpha library from the npm registry
- if your tenant/gateway still uses the old mindsphere.io URLs, install the 3.x line instead
- Getting started
- for typescript nodejs project run
- for javascript nodejs project run
- How to create a nodejs Insights Hub agent
- Step 0: Create an asset type and aspect types
- Step 1: Create an asset
- Step 2: Create an agent of type MindConnectLib in Insights Hub
- Step 3 : Create an agent
- Step 4: Onboard the agent
- Step 5: Configure the data model and data mappings to asset variables. (via code)
- Step 6 After this you can send the data in the code
- Step 6.1 using bulk upload
- Events
- File Upload
- Full Agent
- Making sure that the data arrives also with flaky internet connection
- Proxy support
- set http proxy environment variable if you are using e.g. fiddler on the localhost.
- Insights Hub TypeScript SDK
- Platform Core APIs
- IoT and Storage
- Connectivity
- Advanced Services
- Analytics Services

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 2,139,104 |
| HTML | 20,808 |
| JavaScript | 7,529 |
| Dockerfile | 180 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- package.json (capture: captured) — dependency clues: @compodoc/compodoc, @rollup/plugin-commonjs, @rollup/plugin-json, @rollup/plugin-node-resolve, @types/async-lock, @types/chai, @types/csvtojson, @types/debug, @types/jsonwebtoken, @types/lodash, @types/mocha, @types/node, @types/uuid, ajv, ajv-formats, ajv-keywords, async-lock, chai, chalk, commander

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 71
- Forks at capture: 24
- Last updated: 2026-09-18T22:27:46Z
- Last pushed: 2026-10-31T04:20:08Z
- Topics: industrial-iot, industrial-operations-x, insights-hub, insightshub, javascript, mindconnect, mindconnect-api, mindconnect-nodejs, mindsphere-cli, mindsphere-sdk, nodejs, nodejs-library, sdk, siemens, siemens-xcelerator, typescript, typescript-sdk

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/mindsphere/mindconnect-nodejs)
- [README](https://github.com/mindsphere/mindconnect-nodejs/blob/master/README.md)
- [Issues](https://github.com/mindsphere/mindconnect-nodejs/issues)
- [Releases](https://github.com/mindsphere/mindconnect-nodejs/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
