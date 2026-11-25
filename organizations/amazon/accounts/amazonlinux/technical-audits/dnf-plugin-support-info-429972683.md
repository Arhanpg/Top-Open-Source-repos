# amazonlinux/dnf-plugin-support-info

- Company: Amazon
- Account: amazonlinux
- Repository: https://github.com/amazonlinux/dnf-plugin-support-info
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:59:53+00:00

## Project purpose

DNF plugin that adds the dnf supportinfo subcommand. Use it to look up the support status, dates, severities, and lifecycle phases of any package on Amazon Linux 2023.

## Why this project is used

A DNF plugin to check Support Information for Amazon Linux 2023 packages.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python
- Frameworks/libraries: Unknown / not established
- Dependency names: supportinfo
- Build/package tools: Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/dnf_support_info_plugin/__init__.py, src/dnf_support_info_plugin/config_reader.py, src/dnf_support_info_plugin/const.py, src/dnf_support_info_plugin/dnf_package_service.py

## Setup and usage

- Installation: On Amazon Linux 2023, once the package is published:
- Installation: sudo dnf install dnf-plugin-support-info
- Installation: The package installs:
- Installation: * The plugin code under /usr/lib/python3.9/site-packages/dnf_support_info_plugin/
- Installation: * The DNF entry point at /usr/lib/python3.9/site-packages/dnf-plugins/al_supportinfo.py
- Installation: * A starter config at /etc/dnf/plugins/supportinfo.conf (marked
- Installation: %config(noreplace), so your edits survive package upgrades)
- Usage: dnf supportinfo --help

## Limitations and caveats

- Reporting security issues: Do **not** open a GitHub issue. Use AWS's
- Reporting security issues: vulnerability reporting page.

## Evidence and provenance

- README: https://github.com/amazonlinux/dnf-plugin-support-info/blob/main/README.md
- README SHA: 748f7dfb7033ab6a266bc09fa19be5352e6199a6
- Manifests: Makefile, pyproject.toml, setup.py
- Sampled source files: src/dnf_support_info_plugin/__init__.py, src/dnf_support_info_plugin/config_reader.py, src/dnf_support_info_plugin/const.py, src/dnf_support_info_plugin/dnf_package_service.py
- Git tree state: captured
- Evidence fingerprint: 93b1e6169ed1e9df8274b8881724022f1e578b033fbe84b4ef960cad1a6afd51

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
