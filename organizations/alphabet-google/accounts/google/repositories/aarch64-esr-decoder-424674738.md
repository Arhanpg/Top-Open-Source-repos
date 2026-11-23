# google/aarch64-esr-decoder

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/aarch64-esr-decoder](https://github.com/google/aarch64-esr-decoder)
- Default branch: main
- README: [Open upstream README](https://github.com/google/aarch64-esr-decoder/blob/main/README.md)
- README blob SHA: 7cc01cd7980cc638cc5f23aca0186dfecb86c264
- Repository ID: 424674738
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A utility for decoding aarch64 ESR register values.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:25:49+00:00

### Short excerpt (up to 100 words)

> A small utility for decoding aarch64 ESR register values. This is not an officially supported Google product. Install a Debian package from the `cargo install aarch64-esr-decoder`, or For the command-line version, just pass the ESR value you're interested in as a parameter, in decimal or hexadecimal: $ aarch64-esr-decoder 0x96000050 ESR 0x00000000000000000000000096000050: 37..63 RES0: 0x0000000 0b000000000000000000000000000 32..36 ISS2: 0x00 0b00000 26..31 EC: 0x25 0b100101 25 IL: true 00..24 ISS: 0x0000050 0b0000000000000000001010000 24 ISV: false 14..23 RES0: 0x000 0b0000000000 13 VNCR: false 11..12 SET: 0x0 0b00 10 FnV: false 09 EA: false 08 CM: false 07 S1PTW: false 06 WnR: true 00..05

### README headings

- aarch64-esr-decoder
- Usage
- Data Abort taken without a change in Exception level
- License
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 177,302 |
| HTML | 3,644 |
| JavaScript | 2,639 |
| CSS | 726 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured) — dependency clues: bit_field, thiserror
- aarch64-esr-web/Cargo.toml (capture: captured) — dependency clues: aarch64-esr-decoder, console_error_panic_hook, wasm-bindgen, wasm-bindgen-test, web-sys
- aarch64-esr-web/package.json (capture: captured) — dependency clues: @wasm-tool/wasm-pack-plugin, @webassemblyjs/ast, @webassemblyjs/wasm-edit, @webassemblyjs/wasm-parser, copy-webpack-plugin, rimraf, webpack, webpack-cli, webpack-dev-server
- arm-sysregs-json/Cargo.toml (capture: captured) — dependency clues: serde, serde_json
- arm-sysregs-xml/Cargo.toml (capture: captured) — dependency clues: quick-xml, serde

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 124
- Forks at capture: 28
- Last updated: 2026-11-10T23:01:42Z
- Last pushed: 2026-11-17T22:46:15Z
- Topics: aarch64

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/aarch64-esr-decoder)
- [README](https://github.com/google/aarch64-esr-decoder/blob/main/README.md)
- [Issues](https://github.com/google/aarch64-esr-decoder/issues)
- [Releases](https://github.com/google/aarch64-esr-decoder/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
