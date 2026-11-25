# bottlerocket-os/bottlerocket-admin-container

- Company: Amazon
- Account: bottlerocket-os
- Repository: https://github.com/bottlerocket-os/bottlerocket-admin-container
- Default branch: develop
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:55:47+00:00

## Project purpose

This is the admin container for troubleshooting the Bottlerocket operating system. It runs outside of Bottlerocket's container orchestrator in a separate instance of containerd. The container hosts an SSH server to allow public key SSH access, as well as agetty services for serial console devices to allow console access. You can also connect to the admin container via the control container by running enter-admin-container. Unless otherwise specified through user-data, the default user is **ec2-user**.

## Why this project is used

A container for admin access to Bottlerocket

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Shell, Dockerfile, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: nvidia-bug-report.sh, start_admin.sh, update-nvidia-bug-report.sh

## Setup and usage

- Usage: Enter the admin container either from the control container or SSH if configured. Then run the script:
- Usage: sudo nvidia-bug-report.sh
- Usage: The output is saved as nvidia-bug-report.log.gz in the current directory.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/bottlerocket-os/bottlerocket-admin-container/blob/develop/README.md
- README SHA: c6f610b6ac2b96eef3a81abe05f2bb13225b3265
- Manifests: Dockerfile, Makefile
- Sampled source files: nvidia-bug-report.sh, start_admin.sh, update-nvidia-bug-report.sh
- Git tree state: captured
- Evidence fingerprint: 38c145e7bd91fd37cfcf4f2461042da5588c20d20d789d04000ad10c6fbc6b47

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
