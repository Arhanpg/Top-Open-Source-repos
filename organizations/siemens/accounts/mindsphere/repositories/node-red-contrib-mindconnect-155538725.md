# mindsphere/node-red-contrib-mindconnect

- Company: Siemens
- GitHub account: [https://github.com/mindsphere](https://github.com/mindsphere)
- Mapping status: official-project-linked
- Repository: [mindsphere/node-red-contrib-mindconnect](https://github.com/mindsphere/node-red-contrib-mindconnect)
- Default branch: master
- README: [Open upstream README](https://github.com/mindsphere/node-red-contrib-mindconnect/blob/master/README.md)
- README blob SHA: 9ea4c19b98daf1224e4c6048d486d9f177c6fdf3
- Repository ID: 155538725
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Node-RED Agent for the Siemens Insights Hub MindConnect API

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:43:01+00:00

### Short excerpt (up to 100 words)

> This node enables the Node-RED users to upload timeseries, files and events to Insights Hub. This project has started as a community effort at Siemens AG and is now available for general use. The node is written in typescript/javascript without any native dependencies so it should work beside x86 also on other platforms (e.g. on raspberry pi, IoT2000 etc, you just have to have Node-RED installed). For legacy tenants using `*.mindsphere.io` application URLs, explicitly select v3: cd ~/.node-red/ npm install @mindconnect/node-red-contrib-mindconnect@3 The v4 release is for migrated tenants using application URLs such as `<customerTenantId>-<appName>-<coreTenantId>.<region>.siemens.app`. Confirm your tenant's migration status before

### README headings

- node-red-contrib-mindconnect
- Node-RED Agent for the Insights Hub MindConnect API
- Installing the node
- change to your ~./node-red/ folder
- Node-RED - Manage Palette Installation
- FAQ
- How to use the Node-RED node
- Step 0: Create (at least) one asset and one agent in Insights Hub
- Step 1: Get the initial agent configuration from Insights Hub Asset Manager
- Step 2: Copy the agent onboarding information (and if necessary the RSA 3072 private key) to the node and deploy the flow
- Step 3: Press the agent configuration button and select the target asset
- Step 4: Create and deploy the flow and send data
- Send data points
- Send data points in bulk
- Send events
- File Upload
- Data Lake File Upload
- Reading Asset Information
- Executing custom functions using Insights Hub javascript/typescript SDK
- Error handling in the flows
- JWT Token Generation for SouthBound APIs
- Control Topic and Status Messages
- Demo flows
- Securing API Endpoints
- Troubleshooting
- Reseting the agent settings from version 3.7.0
- Generating the documentation
- Proxy support
- set http proxy environment variable if you are using e.g. fiddler on the localhost.
- How to setup development environment

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HTML | 79,732 |
| TypeScript | 75,448 |
| CSS | 3,373 |
| Dockerfile | 334 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- package.json (capture: captured) — dependency clues: @compodoc/compodoc, @mindconnect/mindconnect-nodejs, @types/ajv, @types/chai, @types/mocha, @types/node, @types/node-fetch, ajv, ajv-formats, chai, concurrently, cross-env, debug, license-checker, mocha, mocha-jenkins-reporter, node-fetch, node-red, node-red-node-test-helper, nodemon

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 51
- Forks at capture: 1
- Last updated: 2026-10-30T07:26:05Z
- Last pushed: 2026-10-30T07:22:36Z
- Topics: industrial-iot, insights-hub, mindconnect, node-red, node-red-contrib, nodejs, siemens, siemens-xcelerator

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/mindsphere/node-red-contrib-mindconnect)
- [README](https://github.com/mindsphere/node-red-contrib-mindconnect/blob/master/README.md)
- [Issues](https://github.com/mindsphere/node-red-contrib-mindconnect/issues)
- [Releases](https://github.com/mindsphere/node-red-contrib-mindconnect/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
