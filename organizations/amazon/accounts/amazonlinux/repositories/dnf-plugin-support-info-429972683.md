# amazonlinux/dnf-plugin-support-info

- Company: Amazon
- GitHub account: [https://github.com/amazonlinux](https://github.com/amazonlinux)
- Mapping status: official-directory-listed
- Repository: [amazonlinux/dnf-plugin-support-info](https://github.com/amazonlinux/dnf-plugin-support-info)
- Default branch: main
- README: [Open upstream README](https://github.com/amazonlinux/dnf-plugin-support-info/blob/main/README.md)
- README blob SHA: 748f7dfb7033ab6a266bc09fa19be5352e6199a6
- Repository ID: 429972683
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A DNF plugin to check Support Information for Amazon Linux 2023 packages.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:37:58+00:00

### Short excerpt (up to 100 words)

> DNF plugin that adds the `dnf supportinfo` subcommand. Use it to look up the support status, dates, severities, and lifecycle phases of any package on Amazon Linux 2023. The plugin is a thin DNF integration over the library, which does the actual XML parsing. Just want to read the published support statements? * Amazon Linux 2023 (or another distribution that ships DNF and Python 3.9+) * `python3-dnf` (provided by the OS) * `python3-supportinfo` 1.0 or newer On Amazon Linux 2023, once the package is published: sudo dnf install dnf-plugin-support-info The package installs: * The plugin code under `/usr/lib/python3.9/site-packages/dnf_support_info_plugin/` * The

### README headings

- dnf-plugin-support-info
- Requirements
- Installation
- Configuration
- Required. URL to the support_info XML file. DNF variables ($awsregion,
- etc.) are expanded automatically.
- Optional. URL to the XSD schema used for validation.
- Optional. How long cached files stay valid, in seconds.
- Default: 1800 (30 minutes). -1 = never expire. 0 = always revalidate.
- Optional. Verify a detached GPG signature on the downloaded XML before
- using it. The signature is fetched from baseurl + ".asc" automatically.
- Off by default. To turn on, set gpgcheck = 1 and add at least one gpgkey.
- Uses the same convention as the gpgcheck/gpgkey options on a DNF repo.
- gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-amazon-linux-2023
- Optional. When enabled, the plugin converts the downloaded 1.0-schema
- XML to the legacy (unversioned) format used by the previous version of
- this plugin. Off by default.
- legacy = 0
- Caching
- URL schemes
- Usage
- Look up packages
- Filter the catalog
- All installed packages
- Installed OR available (state filters are OR'ed together)
- Installed AND end-of-support (state + support-level filters are AND'ed)
- Disambiguate when a name happens to match both groups
- What can I filter on?
- Get the raw data for a package
- Building from source

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 17,396 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: black, flake8, isort, mypy, pep8-naming, pytest, pytest-cov, supportinfo
- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: GPL-2.0
- Stars at capture: 7
- Forks at capture: 3
- Last updated: 2026-09-17T00:17:13Z
- Last pushed: 2026-07-16T00:32:53Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazonlinux/dnf-plugin-support-info)
- [README](https://github.com/amazonlinux/dnf-plugin-support-info/blob/main/README.md)
- [Issues](https://github.com/amazonlinux/dnf-plugin-support-info/issues)
- [Releases](https://github.com/amazonlinux/dnf-plugin-support-info/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
