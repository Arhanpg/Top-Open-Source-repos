# UI5/webcomponents-vue

- Company: SAP
- Account: UI5
- Repository: https://github.com/UI5/webcomponents-vue
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:12:44+00:00

## Project purpose

The project provides means for creating Vue components out of UI5 Web Components, providing a seamless integration of pure web components in Vue. UI5 Web Components are framework-agnostic custom elements, but using them directly in Vue lacks TypeScript support, v-model compatibility, and native slot syntax. This library wraps them to provide a first-class Vue development experience.

## Why this project is used

The project provides means for creating Vue components out of UI5 Web Components (providing a seamless integration of pure web components in Vue.

## Core features

- **Type-safe** - Full TypeScript support with proper type inference: **Type-safe** - Full TypeScript support with proper type inference
  - Evidence: README.md#🔧 Features
- **v-model support** - Two-way data binding for UI5 components: **v-model support** - Two-way data binding for UI5 components
  - Evidence: README.md#🔧 Features
- **Slots support** - Named and default slots: **Slots support** - Named and default slots
  - Evidence: README.md#🔧 Features
- **Reactive** - Seamless integration with Vue's reactivity system: **Reactive** - Seamless integration with Vue's reactivity system
  - Evidence: README.md#🔧 Features

## Technology stack

- Languages: TypeScript, Vue, JavaScript, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @eslint/js, @tsconfig/node24, @types/node, @ui5/webcomponents, @ui5/webcomponents-base, @vitejs/plugin-vue, @vitest/ui, @vue/test-utils, @vue/tsconfig, eslint, happy-dom, lib, npm-run-all2, typescript, typescript-eslint, vite, vite-plugin-vue-devtools, vitest, vue, vue-tsc
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: app/env.d.ts, app/src/__tests__/App.test.ts, app/src/main.ts, app/vite.config.ts

## Setup and usage

- 📚 Library Usage: The library provides two ways to use UI5 Web Components in Vue:
- 📚 Library Usage: 1. **createComponent** - Factory function to wrap any UI5 Web Component
- 📚 Library Usage: 2. **Pre-built components** - Ready-to-use wrappers for common components
- Installation: This will install dependencies for both the library and the demo app.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/UI5/webcomponents-vue/blob/main/README.md
- README SHA: 2db25137ce7866fcd68edb10d3a2378c5e5be463
- Manifests: package.json, app/package.json, lib/package.json
- Sampled source files: app/env.d.ts, app/src/__tests__/App.test.ts, app/src/main.ts, app/vite.config.ts
- Git tree state: captured
- Evidence fingerprint: e9545fb4b8638a0b92d1a5b6a28e52321a88adf35013ccddcc7fe880f2d8a814

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
