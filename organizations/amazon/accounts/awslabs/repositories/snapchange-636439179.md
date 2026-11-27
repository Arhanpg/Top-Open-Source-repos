# awslabs/snapchange

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/snapchange](https://github.com/awslabs/snapchange)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/snapchange/blob/main/README.md)
- README blob SHA: 24c561f34a9724d0274b2e17a88de26c8a44c96b
- README bytes captured: 6670
- README truncated at capture limit: False
- Repository ID: 636439179
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Lightweight fuzzing of a memory snapshot using KVM

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T19:58:08+00:00

### Short excerpt (up to 300 words)

> Tutorial 1 - Basic See CONTRIBUTING for more

### README headings

- Snapchange
- Quick Links:
- Tutorials
- Aspirations
- Example:
- Create a target fuzzer from the fuzzer template
- Modify `your_new_fuzzer/create_snapshot.sh` to take a snapshot of your target
- Update `src/fuzzer.rs` to inject mutated data into the guest VM
- Start fuzzing with 16 cores
- Implementation
- Project directory
- Debugging Trace
- Snapshots
- Documentation and clippy
- Where to begin reading?
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Tutorials

> Tutorial 1 - Basic

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 791,199 |
| Python | 152,260 |
| Shell | 54,903 |
| Makefile | 709 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured) — dependency clues: addr2line, ahash, anyhow, bitflags, clap, clap-verbosity-flag, core_affinity, crossterm, ctrlc, env_logger, iced-x86, kvm-bindings, kvm-ioctls, lazy_static, libc, log, memmap, nix, num_enum, object
- Makefile (capture: captured)
- bench/Cargo.toml (capture: captured) — dependency clues: anyhow, snapchange
- fuzzer_template/Cargo.toml (capture: captured) — dependency clues: anyhow
- bench/bench_harness/Cargo.toml (capture: captured) — dependency clues: libc
- bench/gather_data/Cargo.toml (capture: captured) — dependency clues: snapchange, tokio, toml

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 476
- Forks at capture: 30
- Last updated: 2026-11-22T00:17:12Z
- Last pushed: 2024-04-11T13:05:34Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/snapchange)
- [README](https://github.com/awslabs/snapchange/blob/main/README.md)
- [Issues](https://github.com/awslabs/snapchange/issues)
- [Releases](https://github.com/awslabs/snapchange/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
