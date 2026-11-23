# bottlerocket-os/bottlerocket-sdk

- Company: Amazon
- GitHub account: [https://github.com/bottlerocket-os](https://github.com/bottlerocket-os)
- Mapping status: official-directory-listed
- Repository: [bottlerocket-os/bottlerocket-sdk](https://github.com/bottlerocket-os/bottlerocket-sdk)
- Default branch: develop
- README: [Open upstream README](https://github.com/bottlerocket-os/bottlerocket-sdk/blob/develop/README.md)
- README blob SHA: 2a8eaa1262a9c3227826b7d6d119473474465d4d
- Repository ID: 240619521
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A software development kit for Bottlerocket

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:36:10+00:00

### Short excerpt (up to 100 words)

> This is the SDK for Bottlerocket. It provides the base layer used by package and variant builds. The SDK includes: * Development tools from the host Linux distribution * C and C++ cross-compilers for the target Linux distribution * Kernel headers * Toolchains for Rust and Go * Software license scanner The Bottlerocket SDK is available through Amazon ECR Public. The SDK can be built on either an **x86_64** or an **aarch64** host. make See the BUILDING guide for more details.

### README headings

- Bottlerocket SDK
- Contents
- Availability
- Development

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 212,075 |
| Dockerfile | 38,017 |
| Shell | 29,827 |
| Rust | 29,250 |
| Makefile | 2,393 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- Makefile (capture: captured)
- license-scan/Cargo.toml (capture: captured) — dependency clues: anyhow, askalono, cargo_metadata, clap, ignore, maplit, semver, serde, spdx, tempfile, toml, twox-hash, walkdir
- license-scan/Makefile (capture: captured)
- sbomtool/go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/monitoring, cloud.google.com/go/storage, cyphar.com/go-pathrs, dario.cat/mergo, github.com/BurntSushi/toml, github.com/CycloneDX/cyclonedx-go, github.com/DataDog/zstd, github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/Microsoft/go-winio
- sbomtool/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 58
- Forks at capture: 42
- Last updated: 2026-11-11T20:17:44Z
- Last pushed: 2026-11-19T22:50:57Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/bottlerocket-os/bottlerocket-sdk)
- [README](https://github.com/bottlerocket-os/bottlerocket-sdk/blob/develop/README.md)
- [Issues](https://github.com/bottlerocket-os/bottlerocket-sdk/issues)
- [Releases](https://github.com/bottlerocket-os/bottlerocket-sdk/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
