# Monaco Editor

<sub>Company: Microsoft · Repository: [microsoft/monaco-editor](https://github.com/microsoft/monaco-editor) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

Monaco Editor is the browser-based code editor that powers Visual Studio Code. It is distributed as the `monaco-editor` npm package and can be embedded into web applications that need a rich code-editing surface.

**Problem it addresses:** applications such as online IDEs, configuration tools and code playgrounds need a sophisticated editor component without building text editing, language services and editor interaction from scratch.

## Main concepts

The README explains several core concepts that are important when integrating Monaco:

### Models

A model represents an opened document. It stores text content, the associated language and edit history. A model does not have to correspond to a real file; it can represent content held in an application-managed virtual filesystem.

### URIs

Each model is identified by a URI, so two models cannot share the same URI. The README recommends thinking in terms of a virtual filesystem that mirrors the files users are editing. A meaningful URI can be important for language services that resolve imports or choose schemas.

### Editors

An editor is the user-facing view attached to the DOM. It displays a model and manages view state, commands and editor actions. The model and editor are separate concepts: one document model can be managed independently of its visual editor view.

### Providers

Providers supply smart editor capabilities such as completion and hover information. Some providers correspond conceptually to Language Server Protocol functionality, although the README notes that this is not exactly the same thing.

### Disposables and lifecycle

Many Monaco objects expose a `dispose()` method. Disposing models and editors unregisters resources and listeners. Applications that frequently open and close documents should manage this lifecycle to avoid retaining resources unnecessarily.

## Features and integration resources

- ESM distribution for modern JavaScript bundlers.
- TypeScript declaration file (`monaco.d.ts`) describing the versioned public API.
- Language localization files.
- Interactive playground for trying editor features and creating minimal reproductions.
- Complete integration samples and API documentation.
- Monarch tokenizer playground for defining tokenization rules for a language.

The README warns that AMD support is deprecated. It also clarifies that Monaco is generated from VS Code sources with shims for browser use, but VS Code extensions do not automatically work in Monaco.

## Installation

The documented package installation is:

```bash
npm install monaco-editor
```

The package includes an ESM build and `monaco.d.ts`. The README treats the declaration file as the versioned API contract and cautions that other internal files may change across releases.

## Technology profile

| Area | README-supported details |
|---|---|
| Package ecosystem | npm |
| Distribution | ESM and legacy AMD build (AMD deprecated) |
| Public API typing | TypeScript declaration file |
| Host environment | Browser / DOM |
| Smart editor concepts | Models, URIs, editors and providers |
| Language-service relationship | Provider concepts can map to LSP-like features |
| Localization | NLS message files |

## Integration constraints and FAQ highlights

- The README says Monaco is not supported in mobile browsers or mobile web app frameworks.
- VS Code extensions are not directly compatible with Monaco in the browser.
- Pages served from `file://` cannot create the required web workers; use an HTTP or HTTPS development server.
- Language services may depend on correctly chosen model URIs.
- Editors and models should be disposed when no longer needed.
- The AMD build is deprecated; new integrations should use the ESM distribution.

These details matter when embedding Monaco in a product. A working editor instance alone is not enough: configure workers, URIs, providers, localization and cleanup as part of the integration.

## Suitable applications

- Web-based code editors and IDE experiences.
- Configuration and query editors embedded in dashboards.
- Interactive programming tutorials and code playgrounds.
- Developer tools that need syntax-aware editing and completion.
- Browser applications that need multiple virtual documents.

## Upstream references

- [Repository](https://github.com/microsoft/monaco-editor)
- [Primary README](https://github.com/microsoft/monaco-editor/blob/main/README.md)
- [Interactive playground](https://microsoft.github.io/monaco-editor/playground.html)
- [API documentation](https://microsoft.github.io/monaco-editor/docs.html)
- [ESM integration guide](https://github.com/microsoft/monaco-editor/blob/main/docs/integrate-esm.md)
- [Accessibility guide](https://github.com/microsoft/monaco-editor/wiki/Accessibility-Guide-for-Integrators)

**Evidence note:** README blob inspected: `e17867b5a555606dc3287b6f9cf72b622a8aedb9`.
