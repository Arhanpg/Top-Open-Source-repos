# siemens/cmp-test-suite

- Company: Siemens
- GitHub account: [https://github.com/Siemens](https://github.com/Siemens)
- Mapping status: verified
- Repository: [siemens/cmp-test-suite](https://github.com/siemens/cmp-test-suite)
- Default branch: main
- README: [Open upstream README](https://github.com/siemens/cmp-test-suite/blob/main/readme.md)
- README blob SHA: 1508b0100043384a3655b92853bfb0c53e19255f
- Repository ID: 954612788
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Automated test suite to evaluate server-side implementations of Certificate Management Protocol (CMP); with support for post-quantum hybrid X.509 certificates

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:35:49+00:00

### Short excerpt (up to 100 words)

> SPDX-FileCopyrightText: Copyright 2024 Siemens AG SPDX-License-Identifier: Apache-2.0 --> The CMP test suite is a tool for verifying implementations of the Certificate Management Protocol (CMP). It generates CMP requests, sends them to the server and checks if responses match expectations. The results are logged in a report, which includes all the transmitted and received messages in base64 and in human-readable form. Test cases are written in a domain-specific language (DSL) tailored for PKI and X509 certificate parsing. The provided test scenarios evaluate *server* implementations of CMP RFC 9810 and the CMP lightweight profile RFC 9483. Several usage scenarios are possible: -

### README headings

- Overview
- Quick start with Docker
- Advanced usage
- Configuration
- Usage
- Additional RobotFramework commands
- Other useful commands
- Mock CA
- Usage
- Acknowledgments

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 4,408,443 |
| RobotFramework | 1,225,822 |
| Makefile | 8,056 |
| Shell | 1,314 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: Flask, bitstring, codespell, cryptography, jinja2, liboqs-python, pkilint, pyasn1, pyasn1-alt-modules, pycryptodome, pyhsslms, pylint, pyright, pytest, pytest-xdist, reuse, robotframework, robotframework-requests, robotframework-robocop, ruff

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 4
- Forks at capture: 7
- Last updated: 2026-10-28T09:23:33Z
- Last pushed: 2026-10-28T09:23:27Z
- Topics: asn1, certificate-authority, pki, post-quantum-cryptography, pqc, rfc4210, rfc9483, x509

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/siemens/cmp-test-suite)
- [README](https://github.com/siemens/cmp-test-suite/blob/main/readme.md)
- [Issues](https://github.com/siemens/cmp-test-suite/issues)
- [Releases](https://github.com/siemens/cmp-test-suite/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
