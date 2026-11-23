# cap-js/cds-ts-extension

- Company: SAP
- GitHub account: [https://github.com/cap-js](https://github.com/cap-js)
- Mapping status: official-directory-listed
- Repository: [cap-js/cds-ts-extension](https://github.com/cap-js/cds-ts-extension)
- Default branch: main
- README: [Open upstream README](https://github.com/cap-js/cds-ts-extension/blob/main/README.md)
- README blob SHA: a5173c222cb63544fe44d9d1dfbf32848031fb2c
- Repository ID: 1425160817
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Plugin for the TypeScript LSP to provide CDS-relevant capabilities, such as code completion within CQL queries, and type propagation of such queries.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:48:10+00:00

### Short excerpt (up to 100 words)

> A TypeScript Language Service Plugin that provides CQL-aware completions, hover, diagnostics, and type inference inside `` cds.ql`...` `` tagged template literals in `.js`/`.ts` files. It runs inside the TypeScript server process. After registration it has no dependency on the CDS Language Server — it resolves `@sap/cds` directly from the user's project (with a global-install fallback) via a child-process worker. - this extension currently does not work in a monorepo-scenario or when multiple workspaces are opened in a single vsode instance. - draft-only associations (e.g. `DraftAdministrativeData`) are not resolved in queries against `.drafts` entities, so a reference like `` cds.ql`SELECT DraftAdministrativeData.InProcessByUser

### README headings

- @cap-js/cds-ts-extension
- Known Limitations
- Layout
- Scripts
- Using the plugin locally in VS Code
- Development setup (vscode-cds + this repo)
- Using the plugin in a CAP project (without vscode-cds dev setup)
- In your CAP project:
- In your CAP project:
- Requirements
- Coverage thresholds
- Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 851,273 |
| CAP CDS | 1,989 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @biomejs/biome, @cap-js/sqlite, @sap/cds, @sap/cds-compiler, @types/node, typescript, zod
- test/data/distributedModel/package.json (capture: captured)
- test/data/runtimeModel/package.json (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-11-11T10:47:40Z
- Last pushed: 2026-11-23T13:49:59Z
- Topics: cap, cds, cql, javascript, nodejs, plugin, sap-cap, typescript

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cap-js/cds-ts-extension)
- [README](https://github.com/cap-js/cds-ts-extension/blob/main/README.md)
- [Issues](https://github.com/cap-js/cds-ts-extension/issues)
- [Releases](https://github.com/cap-js/cds-ts-extension/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
