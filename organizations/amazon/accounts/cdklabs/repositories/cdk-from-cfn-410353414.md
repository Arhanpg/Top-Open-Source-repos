# cdklabs/cdk-from-cfn

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-from-cfn](https://github.com/cdklabs/cdk-from-cfn)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-from-cfn/blob/main/README.md)
- README blob SHA: 465e3e1b87e6971e3ebc1619535da7e2bd99addc
- Repository ID: 410353414
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A cloudformation json -> cdk typescript transpiler.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:09+00:00

### Short excerpt (up to 100 words)

> `cdk-from-cfn` is a command-line tool that converts AWS CloudFormation templates into AWS CDK code. It supports multiple programming languages including TypeScript, Python, Java, Go, and C#. cargo install cdk-from-cfn cdk-from-cfn [INPUT] [OUTPUT] --language <LANGUAGE> --name <NAME> [--as <stack|construct>] - `INPUT` is the input file path (STDIN by default). - `OUTPUT` is the output file path; if not specified, output will be printed on your command line (STDOUT by default). - `--name` (optional, `-s` for short) sets the name of the generated stack or construct class (`NoctStack` by default). `--stack-name` is a deprecated alias of `--name` and prints a warning. -

### README headings

- cdk-from-cfn
- Installation
- Usage
- Class Type Option
- Generate a Stack (default)
- Generate a Construct
- Node.js Module Usage
- Language and Feature support
- Implemented
- Remaining

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 731,242 |
| C# | 203,530 |
| Java | 185,977 |
| Go | 157,684 |
| TypeScript | 140,706 |
| Python | 135,881 |
| Just | 819 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured) — dependency clues: base64, cdk-from-cfn-macros, cdk-from-cfn-testing, cdk-from-cfn-testing-end-to-end, clap, futures, indexmap, nom, phf, phf_codegen, serde, serde-enum-str, serde_json, serde_yaml, serial_test, thiserror, tokio, topological-sort, voca_rs
- cdk-from-cfn-macros/Cargo.toml (capture: captured) — dependency clues: proc-macro2, quote, syn
- cdk-from-cfn-testing-end-to-end/Cargo.toml (capture: captured) — dependency clues: aws-config, aws-sdk-cloudformation, aws-sdk-s3, aws-smithy-runtime-api, aws-smithy-types, cdk-from-cfn-testing, serde_json, tokio
- cdk-from-cfn-testing/Cargo.toml (capture: captured) — dependency clues: cdk-from-cfn-macros, pretty_assertions, serde_json, similar, walkdir, zip
- wasm-tests/package.json (capture: captured) — dependency clues: @types/node, tsx, typescript
- cdk-from-cfn-testing/boilerplate/csharp/CSharp.csproj (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 72
- Forks at capture: 28
- Last updated: 2026-11-23T15:54:46Z
- Last pushed: 2026-11-23T15:45:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-from-cfn)
- [README](https://github.com/cdklabs/cdk-from-cfn/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-from-cfn/issues)
- [Releases](https://github.com/cdklabs/cdk-from-cfn/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
