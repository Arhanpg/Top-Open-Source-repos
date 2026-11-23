# amazonlinux/smart-restart

- Company: Amazon
- GitHub account: [https://github.com/amazonlinux](https://github.com/amazonlinux)
- Mapping status: official-directory-listed
- Repository: [amazonlinux/smart-restart](https://github.com/amazonlinux/smart-restart)
- Default branch: main
- README: [Open upstream README](https://github.com/amazonlinux/smart-restart/blob/main/README.md)
- README blob SHA: ccd950d64284a894dc0937f5e3187a8c840cc8f7
- Repository ID: 721057689
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:07:13+00:00

### Short excerpt (up to 100 words)

> This package restarts systemd services on system updates every time a package is updated (installed or deleted) using the systems package mamanger (every time `dnf {update, upgrade, downgrade}` is executed). It primarily is tailored for Amazon Linux 2023 but easily can be ported to all RPM based systems like Fedora. Smart-Restart utilizes the `needs-restarting` package from `dnf-utils` and a custom denylisting mechanism to determine which services need to be restarted and how to determine if a system reboot is advices. In case a system reboot is advised, a reboot hint marker file is generated (`/run/smart-restart/reboot-hint-marker`) containing the services and other

### README headings

- Smart-Restart
- Install using the package manager on AL2023
- Configuration
- Denylisting
- Some comments
- Custom hooks
- Manual installation
- Installation
- Contribution
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 37,728 |
| Makefile | 1,958 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- tests/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 8
- Forks at capture: 3
- Last updated: 2026-09-03T16:46:36Z
- Last pushed: 2026-08-25T12:33:37Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazonlinux/smart-restart)
- [README](https://github.com/amazonlinux/smart-restart/blob/main/README.md)
- [Issues](https://github.com/amazonlinux/smart-restart/issues)
- [Releases](https://github.com/amazonlinux/smart-restart/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
