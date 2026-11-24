# apple/mapkit-loader

- Company: Apple
- GitHub account: [https://github.com/apple](https://github.com/apple)
- Mapping status: verified
- Repository: [apple/mapkit-loader](https://github.com/apple/mapkit-loader)
- Default branch: main
- README: [Open upstream README](https://github.com/apple/mapkit-loader/blob/main/README.md)
- README blob SHA: 17e89f792a0cb08e32a6a7363a58fbe54e60b193
- Repository ID: 1078529095
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Loads Apple MapKit JS script dynamically from Apple MapKit CDN.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:33:58+00:00

### Short excerpt (up to 100 words)

> Loads Apple MapKit JS script dynamically from Apple MapKit CDN. This package exposes the returned `mapkit` object with type definitions. Available via npm as the package `@apple/mapkit-loader`. npm i @apple/mapkit-loader For documentation on MapKit JS, see the Apple MapKit JS Documentation. import { load } from "@apple/mapkit-loader"; const mapkit = await load({ token: "YOUR_MAPKIT_TOKEN", language: "en-US", libraries: ["map", "annotations"], }); The `load()` function returns a `Promise` that would resolve to the `mapkit` object. The `await`ed `mapkit` object is available with `map` and `annotations` libraries loaded. const map = new mapkit.Map(container); const annotation = new mapkit.MarkerAnnotation(new mapkit.Coordinate()); map.addAnnotation(annotation); It is possible

### README headings

- MapKit Loader
- Installation
- Documentation
- Example using MapKit JS Loader
- Advanced server-side rendering integration

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 22,638 |
| HTML | 1,791 |
| JavaScript | 1,164 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @eslint/js, @playwright/test, @types/apple-mapkit, @types/node, eslint, eslint-config-prettier, eslint-plugin-prettier, lint-staged, prettier, simple-git-hooks, typescript, typescript-eslint, vite
- examples/react/package.json (capture: captured) — dependency clues: @apple/mapkit-loader, @types/react, @types/react-dom, @vitejs/plugin-react, react, react-dom, typescript, vite
- examples/svelte/package.json (capture: captured) — dependency clues: @apple/mapkit-loader, @sveltejs/vite-plugin-svelte, @tsconfig/svelte, svelte, svelte-check, typescript, vite
- examples/vanilla/package.json (capture: captured) — dependency clues: @apple/mapkit-loader, typescript, vite
- examples/vue/package.json (capture: captured) — dependency clues: @apple/mapkit-loader, @vitejs/plugin-vue, @vue/tsconfig, typescript, vite, vue, vue-tsc

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 23
- Forks at capture: 4
- Last updated: 2026-11-18T13:05:55Z
- Last pushed: 2026-06-08T18:56:18Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/apple/mapkit-loader)
- [README](https://github.com/apple/mapkit-loader/blob/main/README.md)
- [Issues](https://github.com/apple/mapkit-loader/issues)
- [Releases](https://github.com/apple/mapkit-loader/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
