# amazonlinux/smart-restart

- Company: Amazon
- Account: amazonlinux
- Repository: https://github.com/amazonlinux/smart-restart
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:12:04+00:00

## Project purpose

This package restarts systemd services on system updates every time a package is updated (installed or deleted) using the systems package mamanger (every time dnf {update, upgrade, downgrade} is executed). It primarily is tailored for Amazon Linux 2023 but easily can be ported to all RPM based systems like Fedora. Smart-Restart utilizes the needs-restarting package from dnf-utils and a custom denylisting mechanism to determine which services need to be restarted and how to determine if a system reboot is advices. In case a system reboot is advised, a reboot hint marker file is generated (/run/smart-restart/reboot-hint-marker) containing the services and other components which require a restart.

## Why this project is used

This package restarts systemd services on system updates every time a package is updated (installed or deleted) using the systems package mamanger (every time dnf {update, upgrade, downgrade} is executed). It primarily is tailored for Amazon Linux 2023 but easily can be ported to all RPM based systems like Fedora. Smart-Restart utilizes the needs-restarting package from dnf-utils and a custom denylisting mechanism to determine which services need to be restarted and how to determine if a system reboot is advices. In case a system reboot is advised, a reboot hint marker file is generated (/run/smart-restart/reboot-hint-marker) containing the services and other components which require a restart.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Shell, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: bin/smart-restart.sh

## Setup and usage

- Manual installation: For now, manual installation of Smart-Restart supports AL2 and AL2023. The main reason for the differentiation
- Manual installation: is the package manager. AL2 mainly uses yum and AL2023 dnf. The following prequsites bring the needs-restarting
- Manual installation: script and the a package managers plugin which allows to hook into the different parts of the package managers
- Manual installation: installation process.
- Installation: For dnf based systems:
- Installation: sudo dnf install -y dnf-utils dnf-plugin-post-transaction-actions
- Installation: For yum based systems:
- Installation: sudo yum install -y yum-utils yum-plugin-post-transaction-actions

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/amazonlinux/smart-restart/blob/main/README.md
- README SHA: ccd950d64284a894dc0937f5e3187a8c840cc8f7
- Manifests: Makefile, tests/Makefile
- Sampled source files: bin/smart-restart.sh
- Git tree state: captured
- Evidence fingerprint: 11871b103638431a6056c55e6f45993d6c7db061a39dc9dad0968deb6c68638f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
