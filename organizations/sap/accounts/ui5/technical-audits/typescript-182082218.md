# UI5/typescript

- Company: SAP
- Account: UI5
- Repository: https://github.com/UI5/typescript
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:29:46+00:00

## Project purpose

UI5-TypeScript is an npm [mono-repo][mono-repo] that contains tooling to support [TypeScript][typescript] in SAPUI5 and OpenUI5 Projects. This tooling can enable:

## Why this project is used

Tooling to enable  TypeScript support in SAPUI5/OpenUI5 projects

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, JavaScript, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @changesets/changelog-github, @changesets/cli, @commitlint/cli, @commitlint/config-conventional, @definitelytyped/dtslint, @definitelytyped/eslint-plugin, @eslint/eslintrc, @eslint/js, @microsoft/api-extractor, @openui5/types, @types/hjson, @types/jest, @types/jquery, @types/lodash, @types/node, @types/openui5, @types/qunit, @types/sanitize-html, @types/urijs, @types/yargs, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @ui5/cli, @ui5/dts-generator, @ui5/linter, @ui5/logger, argparse, chai, copyfiles, cz-conventional-changelog, del-cli, es-main, eslint, fs-extra, globals, hjson, http-server, husky, jest, lint-staged, lodash, lodash.combinations, loglevel, marked, mocha, node-fetch, npm-run-all2, prettier, resolve, sanitize-html, semver, shx, strip-json-comments, ts-jest, typedoc, typedoc-plugin-markdown, typescript, typescript-eslint, ui5-middleware-livereload, ui5-middleware-simpleproxy, ui5-tooling-transpile, yargs
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: packages/dts-generator/src/index.ts, packages/dts-generator/src/checkCompile/check-compile.ts, packages/dts-generator/src/checkCompile/diagnostic-analysis.ts, packages/dts-generator/src/checkCompile/ignore-check.ts

## Setup and usage

- Usage: To see the suggested project setup for TypeScript development with the types packages, please check out the TypeScript Hello World app. It not only can serve as copy template, but also includes a detailed step-by-step guide for creating this setup from scratch.
- Usage: The TypeScript branch of the "UI5 CAP Event App" sample demonstrates a slightly more complex application, using the same setup. It comes with an explanation of what UI5 TypeScript code usually looks like and what to consider.
- Usage: As mentioned, the best resource for using UI5 with TypeScript is https://ui5.github.io/typescript.
- Usage: See the demos directory for consumption examples of the legacy signatures.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/UI5/typescript/blob/main/README.md
- README SHA: 44c6fea8a5ee25efbb0b2582dd415658605e38d4
- Manifests: package.json, packages/dts-generator/package.json, packages/ts-interface-generator/package.json, scripts/generate-api-docs/package.json, test-packages/openui5-snapshot-test/package.json, test-packages/typed-json-model/package.json
- Sampled source files: packages/dts-generator/src/index.ts, packages/dts-generator/src/checkCompile/check-compile.ts, packages/dts-generator/src/checkCompile/diagnostic-analysis.ts, packages/dts-generator/src/checkCompile/ignore-check.ts
- Git tree state: captured
- Evidence fingerprint: f3ec1f501cf36a11acc8a01a19f5688a868c9837a1d019c057bd1858cf8bf047

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
