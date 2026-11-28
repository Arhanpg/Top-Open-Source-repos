# aws/amazon-cloudwatch-agent-selinux

- Company: Amazon
- Account: aws
- Repository: https://github.com/aws/amazon-cloudwatch-agent-selinux
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:08:15+00:00

## Project purpose

This is the SELinux policy for AWS CWA agent. Install this policy to confine your CloudWatch Agent processes.

## Why this project is used

This is the SELinux policy for AWS CWA agent. Install this policy to confine your CloudWatch Agent processes.

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

Architecture is not interpreted in evidence-only mode. Sampled source files: amazon_cloudwatch_agent.sh

## Setup and usage

No setup information established.

## Limitations and caveats

- mls - Multi Level Security protection.: Clone the repository, build and install using the commands below:
- mls - Multi Level Security protection.: git clone https://github.com/aws/amazon-cloudwatch-agent-selinux.git
- mls - Multi Level Security protection.: cd amazon-cloudwatch-agent-selinux
- mls - Multi Level Security protection.: chmod +x amazon_cloudwatch_agent.sh
- mls - Multi Level Security protection.: sudo ./amazon_cloudwatch_agent.sh
- mls - Multi Level Security protection.: If you need to enable it, please enable the repository, reboot the instance, and verify that it is in either enforcing or permissive mode, depending on your selection.
- mls - Multi Level Security protection.: Otherwise, you can simply restart the agent to ensure it runs in the confined context.
- mls - Multi Level Security protection.: sudo systemctl restart amazon-cloudwatch-agent

## Evidence and provenance

- README: https://github.com/aws/amazon-cloudwatch-agent-selinux/blob/main/README.md
- README SHA: f4dd64df8725b5aa5c802d05744d5860a620f53c
- Manifests: none
- Sampled source files: amazon_cloudwatch_agent.sh
- Git tree state: captured
- Evidence fingerprint: df07de5180fcb2282ec5a41879672c02c58a6751cb0c603c962fc72eb2e776aa

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
