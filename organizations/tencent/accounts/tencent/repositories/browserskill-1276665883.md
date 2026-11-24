# Tencent/BrowserSkill

- Company: Tencent
- GitHub account: [https://github.com/Tencent](https://github.com/Tencent)
- Mapping status: verified
- Repository: [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)
- Default branch: main
- README: [Open upstream README](https://github.com/Tencent/BrowserSkill/blob/main/README.md)
- README blob SHA: 569200c9d68c4150263cdf6cf90c79a7025025d7
- Repository ID: 1276665883
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Let AI agents use your real, logged-in browser without interrupting your work. CLI + extension for browser automation across any shell-capable AI agent.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:35:23+00:00

### Short excerpt (up to 100 words)

> Turn the browser you already use into a workspace for your AI agent. English · <a href="README.zh-CN.md">中文</a><br /> **BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using your existing logins.** Give it a task to read, click, fill, or investigate. Work stays visible in a separate **Agent Window**, and you can take over when needed. Existing tabs can be explicitly borrowed and returned when the task ends. https://github.com/user-attachments/assets/6111d978-baa6-4a76-92c4-4f51d47ae617 Click the cover to expand the video · <a href="docs/assets/demo/browserskill-demo-en.mp4">Download MP4</a><br /> Real browser actions on a local demo workspace, recorded from main. Qoder, Qoder CN, and DeepSeek Harness are

### README headings

- BrowserSkill
- See it in action
- Bring the agent you already use
- What you can do
- Quick Start
- Let your agent set it up
- 1. Install the CLI
- 2. Connect the extension
- 3. Install the skill for your agent
- 4. Check the connection
- Try your first task
- Close an unused Agent Window
- DeepSeek Harness plugin
- Website debugging
- More workflows
- Capture a full page
- Choose a browser profile
- Run the agent on a server
- Browser control and privacy
- Updating
- Documentation
- For Developers
- Contributors
- License
- Reading dynamic pages (unreleased, protocol 1.9)

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 8,404,063 |
| Rust | 4,626,967 |
| JavaScript | 503,434 |
| HTML | 245,338 |
| Python | 214,779 |
| PowerShell | 42,990 |
| CSS | 12,207 |
| Shell | 6,059 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- package.json (capture: captured) — dependency clues: @biomejs/biome, ajv, esbuild, json-schema-to-typescript, stylelint, stylelint-config-standard
- apps/extension/package.json (capture: captured) — dependency clues: @browser-skill/i18n, @browser-skill/ui, @browser-skill/vom, @dnd-kit/core, @dnd-kit/sortable, @remixicon/react, @tailwindcss/vite, @testing-library/dom, @testing-library/react, @testing-library/user-event, @types/chrome, @types/node, @types/react, @types/react-dom, @types/ws, @vitejs/plugin-react, @wxt-dev/module-react, esbuild, fake-indexeddb, happy-dom
- crates/bsk-cli/Cargo.toml (capture: captured) — dependency clues: anyhow, base64, bsk-protocol, bytes, clap, console, csv, dialoguer, dirs, flate2, fs2, futures-util, http-body-util, hyper, hyper-util, rand, regex, reqwest, schemars, semver
- crates/bsk-protocol/Cargo.toml (capture: captured) — dependency clues: base64, hmac, indexmap, schemars, semver, serde, serde_json, sha2, thiserror
- packages/dsh-plugin-browserskill/package.json (capture: captured) — dependency clues: @deepseek-ai/cordis, @deepseek-ai/dsh-llm, @deepseek-ai/dsh-scope, @deepseek-ai/dsh-skill, @deepseek-ai/schemastery, @types/node, typescript, vitest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 10684
- Forks at capture: 778
- Last updated: 2026-11-23T17:41:00Z
- Last pushed: 2026-11-23T09:22:28Z
- Topics: agent, browser-use, dsh-plugin

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Tencent/BrowserSkill)
- [README](https://github.com/Tencent/BrowserSkill/blob/main/README.md)
- [Issues](https://github.com/Tencent/BrowserSkill/issues)
- [Releases](https://github.com/Tencent/BrowserSkill/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
