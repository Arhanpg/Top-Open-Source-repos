# cdklabs/aws-lambda-rust

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/aws-lambda-rust](https://github.com/cdklabs/aws-lambda-rust)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/aws-lambda-rust/blob/main/README.md)
- README blob SHA: 6c760ffb2c93376e38e016be9536a6f212c9180c
- Repository ID: 730215757
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:39:03+00:00

### Short excerpt (up to 100 words)

> This library provides constructs for Rust Lambda functions. The `rust.RustFunction` construct creates a Lambda function with automatic building and bundling of Rust code. To use this module you will either need to have `cargo-lambda` installed or Docker installed. See Local Bundling/Docker Bundling for more information. . ├── my-construct.ts ├── myconstruct.my_function │ ├── Cargo.toml │ └── src │ └── main.rs By default, the construct will use the name of the defining file and the construct's id to look up the entry file by following this pattern `defining-file.id/Cargo.toml`. In `my-construct.ts` above we have: const myFunction = new rust.RustFunction(this, "my_function"); Alternatively, `entry` and

### README headings

- Amazon Lambda Rust Library
- Rust Function
- How It Works
- Use `cross` for Deployment
- Customizing the underlying Lambda function
- Local Bundling
- Customizing Docker bundling
- Command hooks

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 59,393 |
| Rust | 2,949 |
| Dockerfile | 1,739 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier, jest, jest-junit, jsii, jsii-diff, jsii-docgen
- test/function.test.binary1/Cargo.toml (capture: captured)
- test/rust-bins/Cargo.toml (capture: captured) — dependency clues: lambda_http, lambda_runtime, tokio, tracing, tracing-subscriber
- test/rust-standalone/Cargo.toml (capture: captured) — dependency clues: lambda_http, lambda_runtime, tokio, tracing, tracing-subscriber
- test/rust-workspaces/Cargo.toml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 20
- Forks at capture: 2
- Last updated: 2026-11-09T00:27:53Z
- Last pushed: 2026-11-23T00:25:16Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/aws-lambda-rust)
- [README](https://github.com/cdklabs/aws-lambda-rust/blob/main/README.md)
- [Issues](https://github.com/cdklabs/aws-lambda-rust/issues)
- [Releases](https://github.com/cdklabs/aws-lambda-rust/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
