# amazon-connect/agentic-cx-designer-sdk

- Company: Amazon
- Account: amazon-connect
- Repository: https://github.com/amazon-connect/agentic-cx-designer-sdk
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T04:01:55+00:00

## Project purpose

TypeScript SDK client for Amazon Connect Agentic CX Designer — provides programmatic access to workspace resources including applications, flows, knowledge bases, guardrails, and more.

## Why this project is used

TypeScript SDK client for Amazon Connect Agentic CX Designer — provides programmatic access to workspace resources including applications, flows, knowledge bases, guardrails, and more.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Smithy, JavaScript, TypeScript
- Frameworks/libraries: Unknown / not established
- Dependency names: amazon-connect-acxd-sdk
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: example-scripts/lib/client.js, example-scripts/lib/ensure.js, example-scripts/autocare-voice-assistant/application.js, example-scripts/autocare-voice-assistant/build-deploy.js

## Setup and usage

- Installation: npm install amazon-connect-acxd-sdk
- Usage: import { AgenticCXDesignerClient, ListApplicationsCommand } from "amazon-connect-acxd-sdk";
- Usage: const client = new AgenticCXDesignerClient({
- Usage: apiKey: "REPLACE_WITH_API_KEY",
- Usage: workspaceId: "REPLACE_WITH_WORKSPACE_ID", // required for workspace-scoped operations
- Usage: const response = await client.send(new ListApplicationsCommand({}));
- Usage: console.log(response.items);

## Limitations and caveats

- Security: See CONTRIBUTING for how to report security issues.

## Evidence and provenance

- README: https://github.com/amazon-connect/agentic-cx-designer-sdk/blob/main/README.md
- README SHA: f378f7cbaa5ab0ec54f4f44c69da485919672703
- Manifests: example-scripts/package.json
- Sampled source files: example-scripts/lib/client.js, example-scripts/lib/ensure.js, example-scripts/autocare-voice-assistant/application.js, example-scripts/autocare-voice-assistant/build-deploy.js
- Git tree state: captured
- Evidence fingerprint: 27d8dbf1fde65539d3b51fed758b8f79d0fa8b398ee29dc317158dd0e904341c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
