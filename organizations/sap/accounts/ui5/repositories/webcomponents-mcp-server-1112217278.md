# UI5/webcomponents-mcp-server

- Company: SAP
- GitHub account: [https://github.com/UI5](https://github.com/UI5)
- Mapping status: official-directory-listed
- Repository: [UI5/webcomponents-mcp-server](https://github.com/UI5/webcomponents-mcp-server)
- Default branch: main
- README: [Open upstream README](https://github.com/UI5/webcomponents-mcp-server/blob/main/README.md)
- README blob SHA: dbdecefbc8fc4fc0d81e4db10126a8b2d2088ce9
- Repository ID: 1112217278
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The UI5 Web Components MCP Server improves the developer experience when working with agentic AI and the UI5 Web Components framework.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:42:10+00:00

### Short excerpt (up to 100 words)

> A Model Context Protocol server for UI5 Web Components development. - Node.js Version v20.17.0, v22.9.0 or higher - npm Version v8.0.0 or higher - An MCP client, such as VS Code (GitHub Copilot), Claude Code, Codex, or any other MCP-compatible client This configuration works for most MCP clients: { "mcpServers": { "@ui5/webcomponents-mcp-server": { "type": "stdio", "command": "npx", "args": ["-y", "@ui5/webcomponents-mcp-server"] } } } On native Windows (not WSL), you might need to prefix npx with `cmd /c`: { "mcpServers": { "@ui5/webcomponents-mcp-server": { "type": "stdio", "command": "cmd", "args": ["/c", "npx -y @ui5/webcomponents-mcp-server"] } } } Besides the general configuration outlined above,

### README headings

- UI5 Web Components MCP Server
- Requirements
- Setup
- Standard Configuration for Most Clients
- Specific MCP Clients
- VS Code
- Claude Code
- Codex
- Usage
- Available Tools
- `get_component_api`
- `get_guidelines`
- `list_docs`
- `get_doc`
- Development
- Support, Feedback, Contributing
- Security / Disclosure
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 39,917 |
| JavaScript | 3,122 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @modelcontextprotocol/sdk, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, ava, eslint, prettier, tsx, typescript, vite-node, zod

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 20
- Forks at capture: 2
- Last updated: 2026-10-22T11:45:51Z
- Last pushed: 2026-08-31T11:17:34Z
- Topics: agenticai, open-source, ui5, ui5-webcomponents, web-component, webcomponent

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/UI5/webcomponents-mcp-server)
- [README](https://github.com/UI5/webcomponents-mcp-server/blob/main/README.md)
- [Issues](https://github.com/UI5/webcomponents-mcp-server/issues)
- [Releases](https://github.com/UI5/webcomponents-mcp-server/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
