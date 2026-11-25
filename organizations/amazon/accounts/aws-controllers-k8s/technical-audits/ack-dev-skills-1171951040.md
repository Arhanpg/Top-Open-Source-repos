# aws-controllers-k8s/ack-dev-skills

- Company: Amazon
- Account: aws-controllers-k8s
- Repository: https://github.com/aws-controllers-k8s/ack-dev-skills
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:54:19+00:00

## Project purpose

Development guidance for AWS Controllers for Kubernetes (ACK), packaged as an Agent Skill for use with AI coding tools.

## Why this project is used

Development guidance for AWS Controllers for Kubernetes (ACK), packaged as an Agent Skill for use with AI coding tools.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: skills/ack-dev/scripts/build-controller.sh, skills/ack-dev/scripts/setup-e2e.sh, skills/ack-dev/scripts/verify-build.sh, skills/resolve-issue/scripts/check-breaking-changes.sh

## Setup and usage

- Installation: The skill follows the open Agent Skills standard. Installation varies by tool.
- Installation: Clone the repo first (recommended as a peer to your other ACK repos, e.g. next to code-generator, runtime, etc):
- Installation: cd /path/to/ack-dev-ws
- Installation: git clone https://github.com/aws-controllers-k8s/ack-dev-skills.git
- Usage: Once installed, the skill activates automatically when your request matches ACK development tasks:
- Usage: Add the DatabaseName field to the RDS Instance CRD
- Usage: Create a new controller for AWS Backup
- Usage: Debug why my S3 bucket is stuck in Creating

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-controllers-k8s/ack-dev-skills/blob/main/README.md
- README SHA: 2bb689f4c15c4fde63e7d9bbde0461c431f05293
- Manifests: none
- Sampled source files: skills/ack-dev/scripts/build-controller.sh, skills/ack-dev/scripts/setup-e2e.sh, skills/ack-dev/scripts/verify-build.sh, skills/resolve-issue/scripts/check-breaking-changes.sh
- Git tree state: captured
- Evidence fingerprint: 8df7267c0266c9126d7bb8f571dc0f2efc12e346b21f38396ebc1f8a14c21cca

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
