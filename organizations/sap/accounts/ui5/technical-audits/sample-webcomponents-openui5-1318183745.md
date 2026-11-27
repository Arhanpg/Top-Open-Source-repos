# UI5/sample-webcomponents-openui5

- Company: SAP
- Account: UI5
- Repository: https://github.com/UI5/sample-webcomponents-openui5
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:03:44+00:00

## Project purpose

Reference app for using UI5 Web Components in OpenUI5/SAPUI5 as first-class citizen within OpenUI5/SAPUI5 programming model

## Why this project is used

Reference app for using UI5 Web Components in OpenUI5/SAPUI5

## Core features

- Add a todo (text + deadline) via **Input**, **DatePicker** and an **Emphasized Button**: Add a todo (text + deadline) via **Input**, **DatePicker** and an **Emphasized Button**
  - Evidence: README.md#Features
- Two **Panels** — *Incompleted Tasks* and *Completed Tasks* — populated from a JSON model and kept in sync with a done flag: Two **Panels** — *Incompleted Tasks* and *Completed Tasks* — populated from a JSON model and kept in sync with a done flag
  - Evidence: README.md#Features
- Mark items done / not-done by selecting them in the multi-selection **List** (an item selected in *Incompleted* moves to *Completed*, and vice-versa): Mark items done / not-done by selecting them in the multi-selection **List** (an item selected in *Incompleted* moves to *Completed*, and vice-versa)
  - Evidence: README.md#Features
- **Edit** and **Delete** actions per item; editing opens a **Dialog** (TextArea + DatePicker): **Edit** and **Delete** actions per item; editing opens a **Dialog** (TextArea + DatePicker)
  - Evidence: README.md#Features
- **ShellBar** with a logo, a theme-switcher **Popover** (Horizon / Quartz, incl. high-contrast variants) and a profile **Popover**: **ShellBar** with a logo, a theme-switcher **Popover** (Horizon / Quartz, incl. high-contrast variants) and a profile **Popover**
  - Evidence: README.md#Features
- Profile popover opens **Settings** and **Help** dialogs: Profile popover opens **Settings** and **Help** dialogs
  - Evidence: README.md#Features
- **RTL** toggle and **compact content density** toggle in Settings: **RTL** toggle and **compact content density** toggle in Settings
  - Evidence: README.md#Features

## Technology stack

- Languages: TypeScript, CSS, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @types/openui5, @ui5/cli, @ui5/webcomponents, @ui5/webcomponents-fiori, @ui5/webcomponents-icons, typescript, ui5-middleware-livereload, ui5-tooling-modules, ui5-tooling-transpile
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: webapp/Component.ts, webapp/controller/App.controller.ts

## Setup and usage

- Getting started: npm start runs ui5 serve and opens the app in your browser. To build a self-contained production bundle into dist/:
- Getting started: To type-check the TypeScript sources without emitting:

## Limitations and caveats

- Security / Disclosure: If you find any bug that may be a security problem, please follow our instructions at in our security policy on how to report it. Please do not create GitHub issues for security-related doubts or problems.

## Evidence and provenance

- README: https://github.com/UI5/sample-webcomponents-openui5/blob/main/README.md
- README SHA: def3fe24b485da311c2eb179cf961ecb0c04c43f
- Manifests: package.json
- Sampled source files: webapp/Component.ts, webapp/controller/App.controller.ts
- Git tree state: captured
- Evidence fingerprint: 8e60ab763526f79f4249908f0a4e21661aadb60bd3becdeb7967d62b8ef962ec

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
