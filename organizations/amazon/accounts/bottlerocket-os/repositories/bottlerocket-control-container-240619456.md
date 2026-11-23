# bottlerocket-os/bottlerocket-control-container

- Company: Amazon
- GitHub account: [https://github.com/bottlerocket-os](https://github.com/bottlerocket-os)
- Mapping status: official-directory-listed
- Repository: [bottlerocket-os/bottlerocket-control-container](https://github.com/bottlerocket-os/bottlerocket-control-container)
- Default branch: develop
- README: [Open upstream README](https://github.com/bottlerocket-os/bottlerocket-control-container/blob/develop/README.md)
- README blob SHA: b31c3286332188abeaaeef4229a456180e4a9bdb
- Repository ID: 240619456
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A container for remote control of Bottlerocket

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:35:58+00:00

### Short excerpt (up to 100 words)

> This is the control container for the Bottlerocket operating system. This container runs the AWS SSM Agent that lets you run commands, or start interactive sessions, on Bottlerocket instances in EC2 and hybrid environments. For more information about the control container, including how to use it and how to replace it or remove it from Bottlerocket, please see the Bottlerocket documentation. You'll need Docker 20.10 or later for multi-stage build, BuildKit, and chmod on COPY/ADD support. Then run `make`! Starting from v0.5.0, users have the option to pass in their own activation information for SSM. This is for users that

### README headings

- Bottlerocket Control Container
- Building the Container Image
- Connecting to AWS Systems Manager (SSM)
- ex: echo '{"ssm":{"activation-id":"foo","activation-code":"bar","region":"us-west-2"}}' | base64
- Inspector SBOM Upload (corgid)
- Disabling corgid
- echo '{"inspector": {"upload-sbom": false}}' | base64

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 39,534 |
| Shell | 7,016 |
| Dockerfile | 5,209 |
| Makefile | 5,150 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- Makefile (capture: captured)
- sources/Cargo.toml (capture: captured)
- sources/corgid/Cargo.toml (capture: captured) — dependency clues: aws-credential-types, aws-lc-rs, aws-sigv4, aws-smithy-runtime-api, base64, chrono, flate2, hex, log, reqwest, rustls, serde, serde_json, sha2, simplelog, snafu, uuid

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 44
- Forks at capture: 32
- Last updated: 2026-10-21T22:28:46Z
- Last pushed: 2026-11-13T18:55:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/bottlerocket-os/bottlerocket-control-container)
- [README](https://github.com/bottlerocket-os/bottlerocket-control-container/blob/develop/README.md)
- [Issues](https://github.com/bottlerocket-os/bottlerocket-control-container/issues)
- [Releases](https://github.com/bottlerocket-os/bottlerocket-control-container/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
