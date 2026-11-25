# aws/credential-daemon

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/credential-daemon](https://github.com/aws/credential-daemon)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/credential-daemon/blob/main/README.md)
- README blob SHA: 21fce1200135f0b420ac3d3a57993379660aec2e
- README bytes captured: 4620
- README truncated at capture limit: False
- Repository ID: 1431233361
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Local daemon that keeps AWS credentials and other secrets encrypted on your machine and serves short-lived credentials to the CLI, SDKs and agents over a local socket.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T20:35:10+00:00

### Short excerpt (up to 300 words)

> No README excerpt captured. Use the upstream README link.

### README headings

- AWS Credential Daemon (credsd)
- Key benefits
- The two binaries
- Choose your path
- Platform support
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

No selected README section excerpts were captured.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 2,403,758 |
| Shell | 39,810 |
| Swift | 12,084 |
| Handlebars | 250 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- crates/credsd-client/Cargo.toml (capture: captured) — dependency clues: chrono, credsd-core, proptest, serde, serde_json, tempfile, thiserror, tokio, zeroize
- crates/credsd-core/Cargo.toml (capture: captured) — dependency clues: async-trait, aws-lc-rs, aws-sdk-sso, aws-sdk-ssooidc, aws-sdk-sts, base64, chrono, mockito, open, proptest, reqwest, rolesanywhere-core, rpassword, serde, serde_json, tempfile, thiserror, tokio, toml, toml_edit
- crates/credsd-daemon/Cargo.toml (capture: captured) — dependency clues: async-trait, base64, chrono, clap, credsd-core, mockito, proptest, serde, serde_json, tempfile, tokio, tracing, tracing-subscriber, zeroize
- crates/credsd/Cargo.toml (capture: captured) — dependency clues: base64, chrono, clap, credsd-client, credsd-core, open, proptest, reqwest, rolesanywhere-core, serde, serde_json, tempfile, tokio
- vendor/rolesanywhere/crates/core/Cargo.toml (capture: captured) — dependency clues: aws-lc-rs, base64, chrono, der, hex, num-bigint, pem, percent-encoding, pkcs8, proptest, reqwest, serde, serde_json, x509-cert, zeroize

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 20
- Forks at capture: 0
- Last updated: 2026-11-23T19:21:19Z
- Last pushed: 2026-11-20T21:03:18Z
- Topics: aws, credentials, rust

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/credential-daemon)
- [README](https://github.com/aws/credential-daemon/blob/main/README.md)
- [Issues](https://github.com/aws/credential-daemon/issues)
- [Releases](https://github.com/aws/credential-daemon/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
