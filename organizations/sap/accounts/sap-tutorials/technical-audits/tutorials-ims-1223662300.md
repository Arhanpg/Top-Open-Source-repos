# sap-tutorials/tutorials-ims

- Company: SAP
- Account: sap-tutorials
- Repository: https://github.com/sap-tutorials/tutorials-ims
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:06:41+00:00

## Project purpose

A tutorial hosting platform for developers.sap.com that replaces both Adobe Experience Manager (AEM) and the legacy Java IMS backend. Fetches tutorial markdown from the sap-tutorials GitHub organization at build time, renders static pages with SAP Fundamental Styles (Horizon theme) via Hugo, and deploys on SAP BTP Cloud Foundry behind an AppRouter with XSUAA authentication. The CAP Node.js backend provides progress tracking, event management, and all services previously handled by the Spring Boot IMS application.

## Why this project is used

Tutorial platform IMS - Hugo-based site with SAP Fundamental Styles and BTP Backend

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript, TypeScript, Vue, CAP CDS, HTML, CSS, Shell, PowerShell, HCL, EJS
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-sdk/client-s3, @aws-sdk/lib-storage, @axe-core/playwright, @cap-js-community/websocket, @cap-js/ai, @cap-js/attachments, @cap-js/audit-logging, @cap-js/cds-test, @cap-js/change-tracking, @cap-js/data-inspector, @cap-js/graphql, @cap-js/hana, @cap-js/mcp, @cap-js/ord, @cap-js/sqlite, @cap-js/telemetry, @grpc/grpc-js, @imgly/background-removal, @lhci/cli, @mediapipe/tasks-vision, @opentelemetry/exporter-metrics-otlp-grpc, @opentelemetry/exporter-trace-otlp-grpc, @sap-ai-sdk/foundation-models, @sap-ai-sdk/orchestration, @sap-cloud-sdk/connectivity, @sap-theming/theming-base-content, @sap-tutorials/cds-alert-notification, @sap/approuter, @sap/cds, @sap/cds-dk, @sap/hdi-deploy, @sap/xsenv, @sap/xssec, @socket.io/redis-adapter, @tutorials/content, @tutorials/core, @tutorials/mcp, @types/sanitize-html, @ui5/webcomponents, @ui5/webcomponents-fiori, @ui5/webcomponents-icons, @vitejs/plugin-vue, @vue/test-utils, ajv, archiver, canvas-confetti, cds-caching, cds-swagger-ui-express, cheerio, cron-parser, cropperjs, cross-env, csv-parse, csv-stringify, dompurify, ejs, esbuild, exceljs, express, fundamental-styles, graphology, graphology-layout-forceatlas2, gray-matter, happy-dom, hdb, hugo-extended, jose, js-yaml, jsqr, konva, markdown-it, mermaid, multer, node-sql-parser, nodemailer, onnxruntime-web, passport, patch-package, playwright-core, postcss, postcss-cli, postcss-import, probe-image-size, qrcode, sanitize-html, sap.tutorials.admin.accomplishments, sap.tutorials.admin.accounts, sap.tutorials.admin.changelog, sap.tutorials.admin.events, sap.tutorials.admin.groups, sap.tutorials.admin.joule, sap.tutorials.admin.missions, sap.tutorials.admin.operations, sap.tutorials.admin.prizes, sap.tutorials.admin.tags, sap.tutorials.admin.tutorials, sharp, shiki, sigma, socket.io, socket.io-client, tar, three, tsx, typescript, undici, vite, vite-plugin-css-injected-by-js, vitepress, vitest, vue, vue-virtual-scroller, yaml, yauzl
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: hugo-apps/src/channels-directory/index.ts, hugo-apps/src/channels-health/index.ts, hugo-apps/src/homepage-bands/index.ts, hugo-apps/src/homepage-explainers/index.ts

## Setup and usage

- Quick Start: **Prerequisites:** Node.js >= 20, npm
- Quick Start: npm run fetch-tutorials # Fetch tutorial markdown from GitHub + CAP catalog
- Quick Start: cds watch # Start CAP server (http://localhost:4004)
- Quick Start: npm run dev # Hugo dev server (separate terminal)
- Quick Start: npm run build:all # Full production build
- Quick Start: For full setup including hybrid HANA development, environment variables, and the script reference, see docs/developers/getting-started.md.

## Limitations and caveats

- SAP Tutorial Platform: A tutorial hosting platform for developers.sap.com that replaces both Adobe Experience Manager (AEM) and the legacy Java IMS backend. Fetches tutorial markdown from the sap-tutorials GitHub organization at build time, renders static pages with SAP Fundamental Styles (Horizon theme) via Hugo, and deploys on SAP BTP Cloud Foundry behind an AppRouter 
- SAP Tutorial Platform: > **Production system** replacing AEM tutorial hosting, Git-based authoring interface, and Java IMS backend on developers.sap.com (April 2026).
- SAP Tutorial Platform: **Stack:** Hugo &middot; CAP Node.js (CDS 9.x) &middot; SAP HANA Cloud &middot; SAP Fundamental Styles &middot; Vue 3 (apps) &middot; TypeScript &middot; SAP BTP Cloud Foundry

## Evidence and provenance

- README: https://github.com/sap-tutorials/tutorials-ims/blob/main/README.md
- README SHA: c2e1b21992b2da5fc00dab073dd7bec843c136f8
- Manifests: package.json, approuter/package.json, db-qa/package.json, hugo-apps/package.json, srv-mcp/package.json, srv-qa/package.json
- Sampled source files: hugo-apps/src/channels-directory/index.ts, hugo-apps/src/channels-health/index.ts, hugo-apps/src/homepage-bands/index.ts, hugo-apps/src/homepage-explainers/index.ts
- Git tree state: captured
- Evidence fingerprint: 887de575ff1e74235037c3a09b314e67152c9d1b54221f5e537095d1927d20cf

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
