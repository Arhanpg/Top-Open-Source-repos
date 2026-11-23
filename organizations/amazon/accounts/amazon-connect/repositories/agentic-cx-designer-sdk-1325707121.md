# amazon-connect/agentic-cx-designer-sdk

- Company: Amazon
- GitHub account: [https://github.com/amazon-connect](https://github.com/amazon-connect)
- Mapping status: official-directory-listed
- Repository: [amazon-connect/agentic-cx-designer-sdk](https://github.com/amazon-connect/agentic-cx-designer-sdk)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-connect/agentic-cx-designer-sdk/blob/main/README.md)
- README blob SHA: f378f7cbaa5ab0ec54f4f44c69da485919672703
- Repository ID: 1325707121
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:38:25+00:00

### Short excerpt (up to 100 words)

> TypeScript SDK client for Amazon Connect Agentic CX Designer — provides programmatic access to workspace resources including applications, flows, knowledge bases, guardrails, and more. npm install amazon-connect-acxd-sdk import { AgenticCXDesignerClient, ListApplicationsCommand } from "amazon-connect-acxd-sdk"; const client = new AgenticCXDesignerClient({ region: "us-west-2", apiKey: "REPLACE_WITH_API_KEY", workspaceId: "REPLACE_WITH_WORKSPACE_ID", // required for workspace-scoped operations }); const response = await client.send(new ListApplicationsCommand({})); console.log(response.items); The SDK authenticates with an API key that belongs to a **programmatic user** (a machine identity). The first programmatic user must be created from the UI — you can't call the SDK until you have a key. Once you have one, you

### README headings

- Agentic CX Designer SDK
- Installation
- Usage
- Examples
- Getting an API key
- Creating a client
- Managing programmatic users
- Applications
- Flows
- Paginating list results
- Handling errors
- Copying resources between workspaces
- Runnable example applications
- Architecture
- Development
- Prerequisites
- Generate and build the SDK locally
- Generate TypeScript client from Smithy model
- Build the generated client
- Test it
- Endpoint resolution
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Smithy | 177,399 |
| JavaScript | 67,346 |
| TypeScript | 4,147 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- example-scripts/package.json (capture: captured) — dependency clues: amazon-connect-acxd-sdk

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 12
- Forks at capture: 0
- Last updated: 2026-11-18T10:42:35Z
- Last pushed: 2026-11-20T16:54:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-connect/agentic-cx-designer-sdk)
- [README](https://github.com/amazon-connect/agentic-cx-designer-sdk/blob/main/README.md)
- [Issues](https://github.com/amazon-connect/agentic-cx-designer-sdk/issues)
- [Releases](https://github.com/amazon-connect/agentic-cx-designer-sdk/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
