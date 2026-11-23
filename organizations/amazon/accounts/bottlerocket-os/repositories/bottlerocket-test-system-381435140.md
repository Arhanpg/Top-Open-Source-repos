# bottlerocket-os/bottlerocket-test-system

- Company: Amazon
- GitHub account: [https://github.com/bottlerocket-os](https://github.com/bottlerocket-os)
- Mapping status: official-directory-listed
- Repository: [bottlerocket-os/bottlerocket-test-system](https://github.com/bottlerocket-os/bottlerocket-test-system)
- Default branch: develop
- README: [Open upstream README](https://github.com/bottlerocket-os/bottlerocket-test-system/blob/develop/README.md)
- README blob SHA: 37983de30f6e4b50d3ad7ec5b61c997b7476be86
- Repository ID: 381435140
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A system for testing Bottlerocket

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:06:09+00:00

### Short excerpt (up to 100 words)

> A system for testing Bottlerocket. To learn more about how it works, see the design document. The system consists of a command line interface, Kubernetes controller, custom resource definition (CRD) objects and containers that allow you to create resources and run tests. You install TestSys into a cluster of your choice, we call this the *TestSys cluster*. When running a test, resource agents create an external cluster where we run Bottlerocket instances and run tests. This is called an *external cluster*. See our QUICKSTART for a walk through of compiling, deploying, and running a quick test. More detailed quickstart guides

### README headings

- Bottlerocket Test System
- Overview
- Quickstart
- Development
- Project Structure
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 779,190 |
| Dockerfile | 29,561 |
| Makefile | 22,320 |
| Shell | 10,574 |
| Go | 8,343 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- Dockerfile (capture: captured)
- Makefile (capture: captured)
- cli/Cargo.toml (capture: captured) — dependency clues: anyhow, assert_cmd, clap, env_logger, futures, log, selftest, serde_json, terminal_size, testsys-model, tokio
- controller/Cargo.toml (capture: captured) — dependency clues: anyhow, aws-config, aws-lc-rs, aws-sdk-cloudwatchlogs, aws-types, env_logger, futures, http, k8s-openapi, kube, kube-runtime, lazy_static, log, snafu, testsys-model, tokio
- controller/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 18
- Forks at capture: 28
- Last updated: 2026-05-23T22:46:08Z
- Last pushed: 2026-05-29T21:33:48Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/bottlerocket-os/bottlerocket-test-system)
- [README](https://github.com/bottlerocket-os/bottlerocket-test-system/blob/develop/README.md)
- [Issues](https://github.com/bottlerocket-os/bottlerocket-test-system/issues)
- [Releases](https://github.com/bottlerocket-os/bottlerocket-test-system/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
