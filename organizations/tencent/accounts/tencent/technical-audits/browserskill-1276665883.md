# Tencent/BrowserSkill

- Company: Tencent
- Account: Tencent
- Repository: https://github.com/Tencent/BrowserSkill
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:17:49+00:00

## Project purpose

Turn the browser you already use into a workspace for your AI agent.

## Why this project is used

Let AI agents use your real, logged-in browser without interrupting your work. CLI + extension for browser automation across any shell-capable AI agent.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, Rust, JavaScript, HTML, Python, PowerShell, CSS, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: @biomejs/biome, @browser-skill/i18n, @browser-skill/ui, @browser-skill/vom, @deepseek-ai/cordis, @deepseek-ai/dsh-llm, @deepseek-ai/dsh-scope, @deepseek-ai/dsh-skill, @deepseek-ai/schemastery, @dnd-kit/core, @dnd-kit/sortable, @remixicon/react, @tailwindcss/vite, @testing-library/dom, @testing-library/react, @testing-library/user-event, @types/chrome, @types/node, @types/react, @types/react-dom, @types/ws, @vitejs/plugin-react, @wxt-dev/module-react, ajv, anyhow, base64, bsk-protocol, bytes, clap, console, csv, dialoguer, dirs, esbuild, fake-indexeddb, flate2, fs2, futures-util, happy-dom, hmac, http-body-util, hyper, hyper-util, indexmap, json-schema-to-typescript, mediabunny, rand, re2js, react, react-dom, regex, reqwest, schemars, semver, serde, serde_json, sha2, sortablejs, stylelint, stylelint-config-standard, tailwindcss, tar, tempfile, thiserror, time, tokio, tokio-rustls, tokio-tungstenite, toml_edit, tracing, tracing-appender, tracing-subscriber, typescript, uuid, vitest, ws, wxt, zip
- Build/package tools: Cargo manifest, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: apps/extension/src/tools/vom/semantic-graph/index.ts, crates/bsk-cli/src/cli/mcp/mod.rs, crates/bsk-cli/src/cli/mod.rs, crates/bsk-cli/src/daemon/local_auth/mod.rs

## Setup and usage

- Quick Start: For local automation, you need **an AI agent + the bsk CLI + the browser extension**. The CLI includes the background daemon. The skill teaches your agent how to use it.
- Quick Start: | Component | Supported environments |
- Quick Start: | CLI / daemon | macOS: Apple Silicon and Intel · Linux: x64 and ARM64 · Windows: x64 |
- Quick Start: | Extension | Chrome and Microsoft Edge, based on Chromium 125 or later. Other Chromium browsers may work; compatibility is not guaranteed. |
- Quick Start: | Agent integration | A shell-capable or MCP-capable agent with the BrowserSkill skill (MCP setup). |

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/Tencent/BrowserSkill/blob/main/README.md
- README SHA: 569200c9d68c4150263cdf6cf90c79a7025025d7
- Manifests: Cargo.toml, package.json, apps/extension/package.json, crates/bsk-cli/Cargo.toml, crates/bsk-protocol/Cargo.toml, packages/dsh-plugin-browserskill/package.json
- Sampled source files: apps/extension/src/tools/vom/semantic-graph/index.ts, crates/bsk-cli/src/cli/mcp/mod.rs, crates/bsk-cli/src/cli/mod.rs, crates/bsk-cli/src/daemon/local_auth/mod.rs
- Git tree state: captured
- Evidence fingerprint: 4f57ec47a71439eda3ada9b751ceecf3847d74dda7a0be8c244ef603c3ef8239

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
