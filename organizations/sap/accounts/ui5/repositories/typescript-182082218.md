# UI5/typescript

- Company: SAP
- GitHub account: [https://github.com/UI5](https://github.com/UI5)
- Mapping status: official-directory-listed
- Repository: [UI5/typescript](https://github.com/UI5/typescript)
- Default branch: main
- README: [Open upstream README](https://github.com/UI5/typescript/blob/main/README.md)
- README blob SHA: 44c6fea8a5ee25efbb0b2582dd415658605e38d4
- Repository ID: 182082218
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Tooling to enable  TypeScript support in SAPUI5/OpenUI5 projects

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:42:03+00:00

### Short excerpt (up to 100 words)

> UI5-TypeScript is an npm [mono-repo][mono-repo] that contains tooling to support [TypeScript][typescript] in SAPUI5 and OpenUI5 Projects. This tooling can enable: - Better IDE integration for UI5 projects (e.g content assist). - Using TypeScript compiler to perform type checks on UI5 application code. - More easily implementing UI5 applications and controls in TypeScript thus enjoying the general benefits of TypeScript. It currently contains two public packages: - @ui5/dts-generator [![npm-ui5-dts-generator][npm-ui5-dts-generator-image]][npm-ui5-dts-generator-url] A generator which transforms the UI5 `api.json` format to TypeScript type definition (`*.d.ts`) format. This is useful to enable the type-safe usage of a UI5 control library written in JavaScript in code

### README headings

- UI5-TypeScript
- How to obtain the UI5 TypeScript signatures?
- Usage
- Support
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 567,857 |
| JavaScript | 77,471 |
| HTML | 682 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @changesets/changelog-github, @changesets/cli, @commitlint/cli, @commitlint/config-conventional, chai, cz-conventional-changelog, husky, lint-staged, mocha, npm-run-all2, prettier, shx, typescript
- packages/dts-generator/package.json (capture: captured) — dependency clues: @definitelytyped/dtslint, @definitelytyped/eslint-plugin, @microsoft/api-extractor, @types/lodash, @types/node, @types/sanitize-html, @types/urijs, @ui5/logger, argparse, copyfiles, del-cli, es-main, fs-extra, lodash, lodash.combinations, node-fetch, npm-run-all2, prettier, resolve, sanitize-html
- packages/ts-interface-generator/package.json (capture: captured) — dependency clues: @eslint/eslintrc, @eslint/js, @types/hjson, @types/jest, @types/node, @types/openui5, @types/yargs, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, eslint, hjson, jest, loglevel, npm-run-all2, ts-jest, typescript, yargs
- scripts/generate-api-docs/package.json (capture: captured) — dependency clues: http-server, marked, typedoc, typedoc-plugin-markdown, typescript
- test-packages/openui5-snapshot-test/package.json (capture: captured) — dependency clues: @types/jquery, @types/qunit, @ui5/dts-generator, fs-extra, lodash, typescript
- test-packages/typed-json-model/package.json (capture: captured) — dependency clues: @eslint/js, @openui5/types, @ui5/cli, @ui5/linter, eslint, globals, typescript, typescript-eslint, ui5-middleware-livereload, ui5-middleware-simpleproxy, ui5-tooling-transpile

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 213
- Forks at capture: 35
- Last updated: 2026-11-10T14:22:52Z
- Last pushed: 2026-11-23T12:32:24Z
- Topics: open-source, openui5, sapui5, typescript

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/UI5/typescript)
- [README](https://github.com/UI5/typescript/blob/main/README.md)
- [Issues](https://github.com/UI5/typescript/issues)
- [Releases](https://github.com/UI5/typescript/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
