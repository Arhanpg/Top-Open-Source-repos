# sap-tutorials/tutorials-ims

- Company: SAP
- GitHub account: [https://github.com/sap-tutorials](https://github.com/sap-tutorials)
- Mapping status: official-directory-listed
- Repository: [sap-tutorials/tutorials-ims](https://github.com/sap-tutorials/tutorials-ims)
- Default branch: main
- README: [Open upstream README](https://github.com/sap-tutorials/tutorials-ims/blob/main/README.md)
- README blob SHA: c2e1b21992b2da5fc00dab073dd7bec843c136f8
- Repository ID: 1223662300
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Tutorial platform IMS - Hugo-based site with SAP Fundamental Styles and BTP Backend

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:42:45+00:00

### Short excerpt (up to 100 words)

> A tutorial hosting platform for developers.sap.com that replaces both Adobe Experience Manager (AEM) and the legacy Java IMS backend. Fetches tutorial markdown from the `sap-tutorials` GitHub organization at build time, renders static pages with SAP Fundamental Styles (Horizon theme) via Hugo, and deploys on SAP BTP Cloud Foundry behind an AppRouter with XSUAA authentication. The CAP Node.js backend provides progress tracking, event management, and all services previously handled by the Spring Boot IMS application. **Stack:** Hugo &middot; CAP Node.js (CDS 9.x) &middot; SAP HANA Cloud &middot; SAP Fundamental Styles &middot; Vue 3 (apps) &middot; TypeScript &middot; SAP BTP Cloud Foundry

### README headings

- SAP Tutorial Platform
- Folder Map
- Quick Start
- Scripts
- Setup
- Dev
- Build
- Test
- Content publishing
- QA channel (author preview)
- Migration (Java IMS → CAP)
- Environment Variables
- Runtime Architecture
- Build Architecture
- Joule Architecture
- CAP Backend (srv/)
- Build Pipeline
- Frontend Apps
- Deployment
- Data Migration
- Testing
- External Integrations
- Key Design Decisions
- Documentation
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 13,110,525 |
| TypeScript | 5,124,634 |
| Vue | 1,290,288 |
| CAP CDS | 661,336 |
| HTML | 613,383 |
| CSS | 446,694 |
| Shell | 29,855 |
| PowerShell | 15,137 |
| HCL | 14,498 |
| EJS | 8,933 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-sdk/client-s3, @aws-sdk/lib-storage, @axe-core/playwright, @cap-js-community/websocket, @cap-js/ai, @cap-js/attachments, @cap-js/audit-logging, @cap-js/cds-test, @cap-js/change-tracking, @cap-js/data-inspector, @cap-js/graphql, @cap-js/hana, @cap-js/mcp, @cap-js/ord, @cap-js/sqlite, @cap-js/telemetry, @grpc/grpc-js, @lhci/cli, @opentelemetry/exporter-metrics-otlp-grpc, @opentelemetry/exporter-trace-otlp-grpc
- approuter/package.json (capture: captured) — dependency clues: @sap/approuter, jose, sharp, tar, undici
- db-qa/package.json (capture: captured) — dependency clues: @sap/hdi-deploy, hdb
- hugo-apps/package.json (capture: captured) — dependency clues: @imgly/background-removal, @mediapipe/tasks-vision, @vitejs/plugin-vue, canvas-confetti, cropperjs, graphology, graphology-layout-forceatlas2, jsqr, konva, onnxruntime-web, sigma, socket.io-client, three, typescript, vite, vite-plugin-css-injected-by-js, vue, vue-virtual-scroller
- srv-mcp/package.json (capture: captured) — dependency clues: @cap-js/hana, @cap-js/mcp, @sap-ai-sdk/foundation-models, @sap-cloud-sdk/connectivity, @sap/cds, @sap/xsenv, @sap/xssec, @tutorials/core, @tutorials/mcp, cheerio, express
- srv-qa/package.json (capture: captured) — dependency clues: @cap-js/hana, @sap-ai-sdk/foundation-models, @sap-ai-sdk/orchestration, @sap/cds, @sap/xsenv, @sap/xssec, @tutorials/content, @tutorials/core, cheerio, express, hugo-extended, jose, markdown-it, undici

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 15
- Forks at capture: 5
- Last updated: 2026-11-11T23:09:11Z
- Last pushed: 2026-11-22T16:05:33Z
- Topics: abap, ai, cap, fiori, integration, sap, sap-developers, sapui5, tutorials

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/sap-tutorials/tutorials-ims)
- [README](https://github.com/sap-tutorials/tutorials-ims/blob/main/README.md)
- [Issues](https://github.com/sap-tutorials/tutorials-ims/issues)
- [Releases](https://github.com/sap-tutorials/tutorials-ims/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
