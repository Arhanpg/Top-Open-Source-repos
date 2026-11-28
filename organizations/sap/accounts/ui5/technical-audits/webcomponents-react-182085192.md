# UI5/webcomponents-react

- Company: SAP
- Account: UI5
- Repository: https://github.com/UI5/webcomponents-react
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:06:49+00:00

## Project purpose

ui5-webcomponents-react is providing a Fiori-compliant React implementation by leveraging the UI5 Web Components.

## Why this project is used

A wrapper implementation for React of the UI5 Web Components that are compliant with the SAP Fiori User Experience

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, MDX, CSS, JavaScript, HTML, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: @babel/cli, @babel/core, @babel/preset-env, @babel/preset-react, @babel/preset-typescript, @cypress/code-coverage, @eslint/compat, @eslint/js, @playwright/test, @react-router/dev, @react-router/node, @react-router/serve, @semantic-release/github, @stackblitz/sdk, @storybook/addon-a11y, @storybook/addon-docs, @storybook/react-vite, @testing-library/cypress, @types/jscodeshift, @types/node, @types/react, @types/react-dom, @ui5/webcomponents, @ui5/webcomponents-ai, @ui5/webcomponents-base, @ui5/webcomponents-compat, @ui5/webcomponents-cypress-commands, @ui5/webcomponents-fiori, @ui5/webcomponents-icons, @ui5/webcomponents-react, @ui5/webcomponents-tools, @vitejs/plugin-react, chromatic, cross-env, cssnano, cypress, cypress-real-events, dedent, documentation, eslint, eslint-config-next, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-jsx-a11y, eslint-plugin-no-only-tests, eslint-plugin-prettier, eslint-plugin-react, eslint-plugin-react-hooks, eslint-plugin-react-refresh, eslint-plugin-storybook, glob, globals, husky, isbot, lerna, lint-staged, next, npm-run-all2, nyc, pagefind, postcss, postcss-cli, postcss-import, postcss-modules, prettier, publint, react, react-dom, react-router, remark-gfm, rimraf, storybook, tocbot, typescript, typescript-eslint, vite, vite-plugin-istanbul, vite-tsconfig-paths
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: packages/ai/src/index.ts, packages/base/src/Device/index.ts, packages/base/src/hooks/index.ts, packages/base/src/index.ts

## Setup and usage

- Download and Installation: You can install @ui5/webcomponents-react along with the required peer-dependencies based on the components you plan to use. **In most cases, the recommended installation is the most maintainable option.**
- Recommended Installation: Install @ui5/webcomponents-react along with the @ui5/webcomponents and @ui5/webcomponents-fiori peer-dependencies as dependencies in your project:
- Recommended Installation: npm install @ui5/webcomponents-react @ui5/webcomponents @ui5/webcomponents-fiori
- Recommended Installation: **Note:** If you import anything from another @ui5/webcomponents-xyz package, we recommend installing it as a dependency as well, even if it’s already included through another package.
- Minimal Installation: Since version v2.14.0 of @ui5/webcomponents-react, @ui5/webcomponents-fiori is an optional peer-dependency. You will still need to install it if:
- Minimal Installation: - You want to use any component from the @ui5/webcomponents-fiori package.
- Minimal Installation: - You want to use the VariantManagement component.
- Minimal Installation: - You import anything from the @ui5/webcomponents-fiori package.

## Limitations and caveats

- Known Issues: Please take a look at our GitHub Issues.

## Evidence and provenance

- README: https://github.com/UI5/webcomponents-react/blob/main/README.md
- README SHA: 60d90c74afcefe6c7486e11b1d8ad2f33ef2a709
- Manifests: makefile, package.json, examples/nextjs-app/package.json, examples/nextjs-pages/package.json, examples/react-router-ts/package.json, examples/vite-ts/package.json
- Sampled source files: packages/ai/src/index.ts, packages/base/src/Device/index.ts, packages/base/src/hooks/index.ts, packages/base/src/index.ts
- Git tree state: captured
- Evidence fingerprint: 1505f5c1953802a7b3cc7044f0c3ac9e57ab8eb641b391eae639b939199b2f8f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
