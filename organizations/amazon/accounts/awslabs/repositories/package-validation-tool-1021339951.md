# awslabs/package-validation-tool

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/package-validation-tool](https://github.com/awslabs/package-validation-tool)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/package-validation-tool/blob/main/README.md)
- README blob SHA: f12472b32c905097007dd2f4e503a320dfe6e0b6
- README bytes captured: 6351
- README truncated at capture limit: False
- Repository ID: 1021339951
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

CLI tool to validate the origins of OS distro packages

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T06:11:30+00:00

### Short excerpt (up to 300 words)

> Run the following commands Python 3.7+ Docker (we Currently only RPM packages

### README headings

- Package-Validation-Tool
- Requirements
- Quickstart
- using GITHUB_TOKEN is highly recommended for GitHub access, see comments below
- 1. Obtain package from local repos and unpack it to a specified directory
- the unpacked package contents look like this:
- zlib/
- |-- SOURCE
- |   |-- CVE-2023-45853.patch
- |   |-- ...
- |   |-- zlib-1.2.11.tar.xz
- |-- SPECS
- |   `-- zlib.spec
- `-- SRPM_CONTENT
- |-- CVE-2023-45853.patch
- |   |-- ...
- |-- zlib-1.2.11.tar.xz
- `-- zlib.spec
- 2. Match files in local archive against detected upstream archives
- zlib-match-archives.json looks like this (remote archive was found):
- {
- "matching": true,
- "results": {
- "zlib-1.2.11.tar.xz": {
- "remote_archive": "https://www.zlib.net/fossils/zlib-1.2.11.tar.gz",
- "matched": true,
- "files_total": 253,
- "conflicts": {}
- }
- }

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Quickstart

> Run the following commands

### Technology and requirements: Requirements

> Python 3.7+ Docker (we

### Limitations and security: Limitations

> Currently only RPM packages

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 458,973 |
| Shell | 23,392 |
| Makefile | 1,411 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured)
- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 1
- Last updated: 2026-07-23T05:39:14Z
- Last pushed: 2026-07-23T05:38:35Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/package-validation-tool)
- [README](https://github.com/awslabs/package-validation-tool/blob/main/README.md)
- [Issues](https://github.com/awslabs/package-validation-tool/issues)
- [Releases](https://github.com/awslabs/package-validation-tool/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
