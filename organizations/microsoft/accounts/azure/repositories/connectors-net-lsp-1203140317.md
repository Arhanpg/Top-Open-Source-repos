# Azure/Connectors-NET-LSP

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/Connectors-NET-LSP](https://github.com/Azure/Connectors-NET-LSP)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/Connectors-NET-LSP/blob/main/README.md)
- README blob SHA: 082e74ce24f2d6d1bca06cc3e526fbc5cbdcff4d
- README bytes captured: 11439
- README truncated at capture limit: False
- Repository ID: 1203140317
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Language Server Protocol (LSP) server and VS Code extension for Azure Connectors .NET SDK - provides IntelliSense, hover info, and live API Hub lookups for connector development.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T05:52:54+00:00

### Short excerpt (up to 300 words)

> **Document Sync**: Real-time document .NET SDK 8.0+ Node.js

### README headings

- Azure Connectors SDK — LSP Server
- Features
- Requirements
- Build
- From repo root
- Test
- Run the Server
- Launch the LSP server (stdio)
- Framework-Dependent Publish (run with `dotnet`)
- Uses the MSBuild convenience target (outputs to ../LSPServer)
- Packaging & Distribution
- Build for current platform (outputs to ../LSPServer)
- Or build for a specific platform
- VS Code Extension Packaging
- First, publish the LSP server into the extension's server/ directory
- Releasing a New Version
- 1. Update CHANGELOG.md with the new version entry
- 2. Update vscode-extension/package.json version to match
- 3. Create PR, get it merged
- 4. Tag and release:
- Repository Structure
- LSP Capabilities
- Using With an Editor
- VS Code Integration
- End-to-End Testing
- Development Notes
- Git Pre-Commit Hook
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Features

> **Document Sync**: Real-time document

### Technology and requirements: Requirements

> .NET SDK 8.0+ Node.js

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C# | 878,801 |
| TypeScript | 43,562 |
| Shell | 7,081 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- sdk-lsp-server.sln (capture: captured)
- Server.Tests/Server.Tests.csproj (capture: captured)
- Server/SdkLspServer.csproj (capture: captured)
- vscode-extension/package.json (capture: captured) — dependency clues: @types/node, @types/vscode, @vscode/vsce, typescript, vscode-languageclient

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 0
- Forks at capture: 4
- Last updated: 2026-11-12T04:16:45Z
- Last pushed: 2026-11-18T17:45:29Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/Connectors-NET-LSP)
- [README](https://github.com/Azure/Connectors-NET-LSP/blob/main/README.md)
- [Issues](https://github.com/Azure/Connectors-NET-LSP/issues)
- [Releases](https://github.com/Azure/Connectors-NET-LSP/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
