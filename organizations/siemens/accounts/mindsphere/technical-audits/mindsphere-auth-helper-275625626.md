# mindsphere/mindsphere-auth-helper

- Company: Siemens
- Account: mindsphere
- Repository: https://github.com/mindsphere/mindsphere-auth-helper
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:51:25+00:00

## Project purpose

This chrome extension can be used to simplify the development tasks for which you need to use the SESSION and XSRF-TOKEN to access Insights Hub and Indutrial IoT APIs. It provides an easy way to copy the Insights Hub and Indutrial IoT authentication cookies to the clipboard without having to go to chrome developer tools.

## Why this project is used

This chrome extension can be used to simplify the development tasks for which you need to use the SESSION and XSRF-TOKEN to access Insights Hub APIs. It provides an easy way to copy the Insights Hub authentication cookies to the clipboard without having to go to chrome developer tools.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: CSS, HTML, TypeScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @types/chrome, copyfiles, cross-env, cross-var, rimraf, typescript
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: scripts.ts

## Setup and usage

- Installation: Go to chrome web store and click on **add to chrome**.
- Installation: Once the extension is installed: log in to your Insights Hub and Indutrial IoT tenant, navigate to your application and click on the extension icon to display the available application cookies. You can now click e.g. on **session** or **Xsrf** button which will copy the corresponding cookie to your clipboard.
- Installation: The cookies can be used with the tools like curl, postman etc. (Click on the links for more examples)
- Installation: --cookie "SESSION= ;XSRF-TOKEN= " \
- Installation: https:// - - . .mindsphere.io/api/assetmanagement/v3/assets

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/mindsphere/mindsphere-auth-helper/blob/master/README.md
- README SHA: 8e927b33b645a4d5b4cbb51496005f05d34e9c29
- Manifests: package.json
- Sampled source files: scripts.ts
- Git tree state: captured
- Evidence fingerprint: 2300109de1999703f270623792be6ebdc070cbbf7f0fdda78c1778d40ee9b1f3

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
