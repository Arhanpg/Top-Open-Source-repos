# aws-cloudformation/cloudformation-validate

- Company: Amazon
- GitHub account: [https://github.com/aws-cloudformation](https://github.com/aws-cloudformation)
- Mapping status: official-directory-listed
- Repository: [aws-cloudformation/cloudformation-validate](https://github.com/aws-cloudformation/cloudformation-validate)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/README.md)
- README blob SHA: 2911d470dd2db7dd18aff3b6c0155ba7c838515b
- README bytes captured: 16802
- README truncated at capture limit: False
- Repository ID: 1257514980
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS CloudFormation Validate

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T20:43:10+00:00

### Short excerpt (up to 300 words)

> **Offline-first.** Rules and AWS Use the prebuilt CLI, When a template is If you discover a

### README headings

- AWS CloudFormation Validate
- Features
- How it works
- Installation
- Quick start
- Validate a single template
- Validate every template in a directory (recurses, picks up .yaml/.yml/.json)
- Use the CEL engine instead of the default composite engine
- Compact output for IDEs/CI
- Only report errors and above
- List every available rule and exit
- Load custom Guard rules
- Embedding as a library
- Rust [(bindings-rust)](src/bindings-rust/README.md)
- Node.js [(bindings-wasm)](src/bindings-wasm/README.md)
- Python [(bindings-python)](src/bindings-python/README.md)
- Go [(bindings-go)](src/bindings-go/README.md)
- JVM Java/Kotlin [(bindings-jvm)](src/bindings-jvm/README.md)
- Rules
- Modules
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Features

> **Offline-first.** Rules and AWS

### Getting started and usage: Installation

> Use the prebuilt CLI,

### Architecture and design: How it works

> When a template is

### Limitations and security: Security

> If you discover a

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 5,098,318 |
| Python | 503,636 |
| Open Policy Agent | 290,018 |
| Go | 213,818 |
| TypeScript | 152,289 |
| Kotlin | 149,391 |
| Shell | 45,803 |
| C | 42,934 |
| Java | 16,242 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/Cargo.toml (capture: captured)
- src/bindings-go/Cargo.toml (capture: captured) — dependency clues: cel-engine, composite-engine, data-source, diagnostics, rego-engine, rules, schema-validator, serde, serde_json, template-model, thiserror, uniffi, validation-engine
- src/bindings-jvm/build.gradle.kts (capture: captured)
- src/bindings-jvm/Cargo.toml (capture: captured) — dependency clues: cel-engine, composite-engine, data-source, diagnostics, rego-engine, rules, schema-validator, template-model, thiserror, uniffi, validation-engine
- src/bindings-python/Cargo.toml (capture: captured) — dependency clues: cel-engine, composite-engine, data-source, diagnostics, rego-engine, rules, schema-validator, template-model, thiserror, uniffi, validation-engine
- src/bindings-python/pyproject.toml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 12
- Forks at capture: 7
- Last updated: 2026-11-18T22:39:09Z
- Last pushed: 2026-11-21T22:34:54Z
- Topics: amazon, aws, aws-cloudformation, cloudformation, iac, infrastructure-as-code, lint, template, validate

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-cloudformation/cloudformation-validate)
- [README](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/README.md)
- [Issues](https://github.com/aws-cloudformation/cloudformation-validate/issues)
- [Releases](https://github.com/aws-cloudformation/cloudformation-validate/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
