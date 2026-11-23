# apple/apple-llvm-infrastructure-tools

- Company: Apple
- GitHub account: [https://github.com/apple](https://github.com/apple)
- Mapping status: verified
- Repository: [apple/apple-llvm-infrastructure-tools](https://github.com/apple/apple-llvm-infrastructure-tools)
- Default branch: main
- README: [Open upstream README](https://github.com/apple/apple-llvm-infrastructure-tools/blob/main/README.md)
- README blob SHA: 39f88ba0df4563e428e1c9ab5944878969f4a62e
- Repository ID: 196327850
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:21:38+00:00

### Short excerpt (up to 100 words)

> This is a collection of tools for maintaining LLVM-project&ndash;related infrastructure, including CI, automerging, monorepo transition, and others. Prerequisites: - Python 3 - Relatively recent git (git 2.20+ should work) You can deploy `git-apple-llvm` by running the `install` target: sudo make install # Installs into /usr/local/bin make install PREFIX=/my/directory # Installs into /my/directory/bin You can always uninstall the tools by running the `uninstall` target: sudo make uninstall `cd docs/ && make html && open _build/html/index.html` for more documentation.

### README headings

- Apple LLVM Infrastructure Tools
- Deploying `git-apple-llvm`
- More documentation

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 195,601 |
| Python | 175,179 |
| Shell | 111,150 |
| C | 15,177 |
| Makefile | 9,723 |
| Awk | 4,859 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- setup.py (capture: captured)
- docs/Makefile (capture: captured)
- docs/requirements.txt (capture: captured) — dependency clues: recommonmark, sphinx
- src/Makefile (capture: captured)
- test/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 50
- Forks at capture: 20
- Last updated: 2026-10-13T17:59:50Z
- Last pushed: 2023-10-10T19:44:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/apple/apple-llvm-infrastructure-tools)
- [README](https://github.com/apple/apple-llvm-infrastructure-tools/blob/main/README.md)
- [Issues](https://github.com/apple/apple-llvm-infrastructure-tools/issues)
- [Releases](https://github.com/apple/apple-llvm-infrastructure-tools/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
