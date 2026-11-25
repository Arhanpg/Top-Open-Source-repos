# microsoft/amplifier-app-paperclip

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-app-paperclip](https://github.com/microsoft/amplifier-app-paperclip)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-app-paperclip/blob/main/README.md)
- README blob SHA: 39f5089a1f6c4eaf5ac22d11f7848cc7650da9de
- README bytes captured: 10466
- README truncated at capture limit: False
- Repository ID: 1259780697
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Paperclip with Amplifier Agent integration

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T22:34:11+00:00

### Short excerpt (up to 300 words)

> git clone https://github.com/microsoft/amplifier-app-paperclip cd A **non-root user** —

### README headings

- amplifier-app-paperclip
- Prerequisites
- Quick start
- Optional but recommended: register provider credentials with amplifier-agent
- BEFORE starting the server. amplifier-agent auto-enables every provider
- whose credentials resolve (this persists to ~/.amplifier-agent/credentials.json,
- so it survives across shells/reboots — no re-exporting needed).
- Add only the providers you actually use.
- Verifying it works
- 1. Health: status ok, bootstrap ready
- 2. Adapter is loaded
- expect: {"type":"amplifier_local","loaded":true,"disabled":false,"modelsCount":11,…}
- 3. Engine version (per-user, must match the user running paperclip)
- expect: {"version":"0.9.1","protocolVersion":"0.3.0"}
- Configure your agent's API key
- Option A — amplifier-agent auth set (simplest, single-user dev)
- Option B — Per-agent (multi-tenant, or when you need distinct keys per agent)
- Updating
- License
- Contributing
- Trademarks

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Quick start

> git clone https://github.com/microsoft/amplifier-app-paperclip cd

### Technology and requirements: Prerequisites

> A **non-root user** —

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 19,271,447 |
| JavaScript | 189,344 |
| Shell | 134,541 |
| PLpgSQL | 84,721 |
| CSS | 29,803 |
| HTML | 15,974 |
| Dockerfile | 5,185 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- package.json (capture: captured) — dependency clues: @playwright/test, cross-env, esbuild, typescript, vitest
- cli/package.json (capture: captured) — dependency clues: @clack/prompts, @paperclipai/adapter-acpx-local, @paperclipai/adapter-amplifier-local, @paperclipai/adapter-claude-local, @paperclipai/adapter-codex-local, @paperclipai/adapter-cursor-cloud, @paperclipai/adapter-cursor-local, @paperclipai/adapter-gemini-local, @paperclipai/adapter-grok-local, @paperclipai/adapter-openclaw-gateway, @paperclipai/adapter-opencode-local, @paperclipai/adapter-pi-local, @paperclipai/adapter-utils, @paperclipai/db, @paperclipai/server, @paperclipai/shared, @types/node, commander, dotenv, drizzle-orm
- server/package.json (capture: captured) — dependency clues: @aws-sdk/client-s3, @paperclipai/adapter-acpx-local, @paperclipai/adapter-amplifier-local, @paperclipai/adapter-claude-local, @paperclipai/adapter-codex-local, @paperclipai/adapter-cursor-cloud, @paperclipai/adapter-cursor-local, @paperclipai/adapter-gemini-local, @paperclipai/adapter-grok-local, @paperclipai/adapter-openclaw-gateway, @paperclipai/adapter-opencode-local, @paperclipai/adapter-pi-local, @paperclipai/adapter-utils, @paperclipai/db, @paperclipai/plugin-sdk, @paperclipai/shared, @types/express, @types/express-serve-static-core, @types/jsdom, @types/multer
- ui/package.json (capture: captured) — dependency clues: @assistant-ui/react, @dnd-kit/core, @dnd-kit/sortable, @dnd-kit/utilities, @lexical/link, @mdxeditor/editor, @paperclipai/adapter-acpx-local, @paperclipai/adapter-amplifier-local, @paperclipai/adapter-claude-local, @paperclipai/adapter-codex-local, @paperclipai/adapter-cursor-cloud, @paperclipai/adapter-cursor-local, @paperclipai/adapter-gemini-local, @paperclipai/adapter-grok-local, @paperclipai/adapter-openclaw-gateway, @paperclipai/adapter-opencode-local, @paperclipai/adapter-pi-local, @paperclipai/adapter-utils, @paperclipai/shared, @radix-ui/react-slot
- docker/openclaw-smoke/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 1
- Forks at capture: 2
- Last updated: 2026-10-29T20:23:29Z
- Last pushed: 2026-10-29T20:25:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-app-paperclip)
- [README](https://github.com/microsoft/amplifier-app-paperclip/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-app-paperclip/issues)
- [Releases](https://github.com/microsoft/amplifier-app-paperclip/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
