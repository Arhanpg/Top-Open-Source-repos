# Monaco Editor

- **Company:** Microsoft
- **Repository:** https://github.com/microsoft/monaco-editor
- **README:** https://github.com/microsoft/monaco-editor/blob/main/README.md
- **Default branch:** main
- **Audit status:** README reviewed
- **README blob SHA at inspection:** e17867b5a555606dc3287b6f9cf72b622a8aedb9

## What it does

The fully featured browser-based code editor from Visual Studio Code, distributed as the `monaco-editor` package.

## Features documented by the upstream README

- Provides an interactive playground for exploring editor behavior and minimal reproducible examples.
- Exposes editor models representing opened files and their content, language and edit history.
- Uses model URIs to identify virtual or filesystem-backed documents.
- Providers supply smart editor capabilities such as completion and hover information.

## Technology stack

npm package; ESM distribution; TypeScript declaration file (`monaco.d.ts`); browser JavaScript integration.

## Notes and limitations

README explains that the API declaration file is versioned and other internal distribution files may be private implementation details.

## Evidence

This summary is based on the upstream README linked above. Repository manifests, source code, CI workflows and release artifacts were not exhaustively audited in this pass; therefore the technology stack is limited to what the README explicitly supports.
