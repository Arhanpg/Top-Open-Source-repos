# aws/aws-nitro-enclaves-image-format

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-nitro-enclaves-image-format](https://github.com/aws/aws-nitro-enclaves-image-format)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-nitro-enclaves-image-format/blob/main/README.md)
- README blob SHA: e5db2c45b7a50ea42835c7889843b61947c79ff4
- README bytes captured: 34371
- README truncated at capture limit: False
- Repository ID: 310362617
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This library provides the definition of the enclave image format (EIF) file used in AWS Nitro Enclaves.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T04:20:18+00:00

### Short excerpt (up to 300 words)

> COSE Sign1 provides a See CONTRIBUTING for more

### README headings

- aws-nitro-enclaves-image-format
- Security
- License
- Enclave Image File (EIF) Specification
- Background
- The File Format
- High Level Structure
- `EifHeader`
- `magic`
- `version`
- EIF format version history:
- `flags`
- `default_mem`
- `default_cpus`
- `num_sections`
- `section_offsets`
- `section_sizes`
- `eif_crc32`
- Data sections
- `EifSectionHeader`
- `section_type`
- `flags`
- `section_size`
- `EifSectionKernel`
- `EifSectionCmdline`
- `EifSectionRamdisk`
- Example: ramdisks created with [aws-nitro-enclaves-cli](https://github.com/aws/aws-nitro-enclaves-cli)
- Background on ramdisk composition and loading
- `EifSectionSignature`
- Background on COSE Sign1 and usage in EIF

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Background on COSE Sign1 and usage in EIF

> COSE Sign1 provides a

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 143,047 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured) — dependency clues: aws-config, aws-nitro-enclaves-cose, aws-sdk-kms, aws-types, byteorder, chrono, ciborium, crc, hex, num-derive, num-traits, openssl, regex, serde, serde_json, sha2, tempfile, tokio
- eif_build/Cargo.toml (capture: captured) — dependency clues: aws-nitro-enclaves-image-format, chrono, clap, serde, serde_json, sha2

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 20
- Forks at capture: 27
- Last updated: 2026-11-20T15:16:47Z
- Last pushed: 2026-11-20T09:23:10Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-nitro-enclaves-image-format)
- [README](https://github.com/aws/aws-nitro-enclaves-image-format/blob/main/README.md)
- [Issues](https://github.com/aws/aws-nitro-enclaves-image-format/issues)
- [Releases](https://github.com/aws/aws-nitro-enclaves-image-format/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
