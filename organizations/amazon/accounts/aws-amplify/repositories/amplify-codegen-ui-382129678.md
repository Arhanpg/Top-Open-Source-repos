# aws-amplify/amplify-codegen-ui

- Company: Amazon
- GitHub account: [https://github.com/aws-amplify](https://github.com/aws-amplify)
- Mapping status: official-directory-listed
- Repository: [aws-amplify/amplify-codegen-ui](https://github.com/aws-amplify/amplify-codegen-ui)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-amplify/amplify-codegen-ui/blob/main/README.md)
- README blob SHA: 95f88dd384b1efa45733d86b49befa61a6b71d9e
- Repository ID: 382129678
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Generate React components for use in an AWS Amplify project.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:40:07+00:00

### Short excerpt (up to 100 words)

> Generate React components for use in an AWS Amplify project. Amplify Codegen UI supports component generation in Node or a browser environment. import { AmplifyRenderer, StudioTemplateRendererFactory, StudioTemplateRendererManager, } from '@aws-amplify/codegen-ui-react'; const renderConfig = {}; const outputConfig = { outputPathDir: './src/ui-components'; }; const componentRendererFactory = new StudioTemplateRendererFactory( (component) => new AmplifyRenderer(component, renderConfig), ); const rendererManager = new StudioTemplateRendererManager(componentRendererFactory, outputConfig); const component = { id: '1234-5678-9010', componentType: 'Text', name: 'TextPrimitive', properties: { label: { value: 'Hello world', }, }, }; rendererManager.renderSchemaToTemplate(component); import { ReactThemeStudioTemplateRenderer, StudioTemplateRendererFactory, StudioTemplateRendererManager, } from '@aws-amplify/codegen-ui-react'; const renderConfig = {}; const outputConfig = { outputPathDir: './src/ui-components'; }; const themeRendererFactory

### README headings

- Amplify Codegen UI
- Usage
- Generate in Node
- Components
- Themes
- `index.js` File
- Generate in Browser
- Components
- Themes
- `index.js` File
- Config
- Output Config
- outputPathDir (Required)
- Render Config
- script
- target
- module
- renderTypeDeclarations
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 2,471,938 |
| JavaScript | 211,780 |
| Shell | 4,214 |
| Batchfile | 2,640 |
| CSS | 148 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @commitlint/cli, @commitlint/config-conventional, @istanbuljs/nyc-config-typescript, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, eslint, eslint-config-airbnb-typescript, eslint-config-prettier, eslint-plugin-header, eslint-plugin-import, eslint-plugin-prettier, husky, jest, lerna, lint-staged, nodemon, nyc, prettier
- packages/codegen-ui-react/package.json (capture: captured) — dependency clues: @aws-amplify/appsync-modelgen-plugin, @aws-amplify/codegen-ui, @aws-amplify/datastore, @aws-amplify/ui-react, @aws-amplify/ui-react-storage, @testing-library/react-hooks, @types/node, @types/pluralize, @types/react, @types/semver, @typescript/vfs, pascalcase, pluralize, prettier, react, react-dom, react-test-renderer, semver, typescript
- packages/codegen-ui/package.json (capture: captured) — dependency clues: @aws-amplify/appsync-modelgen-plugin, @aws-amplify/datastore, change-case, yup
- packages/test-generator/package.json (capture: captured) — dependency clues: @aws-amplify/codegen-ui, @aws-amplify/codegen-ui-react, @aws-amplify/datastore, @aws-amplify/ui-react, @aws-amplify/ui-react-storage, @types/node, cypress, eslint-plugin-cypress, loglevel, pascalcase, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 31
- Forks at capture: 31
- Last updated: 2026-11-09T13:26:39Z
- Last pushed: 2026-11-09T13:26:36Z
- Topics: amplify, aws, aws-amplify, javascript, react

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-amplify/amplify-codegen-ui)
- [README](https://github.com/aws-amplify/amplify-codegen-ui/blob/main/README.md)
- [Issues](https://github.com/aws-amplify/amplify-codegen-ui/issues)
- [Releases](https://github.com/aws-amplify/amplify-codegen-ui/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
