# aws/amazon-ssm-agent-selinux

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-ssm-agent-selinux](https://github.com/aws/amazon-ssm-agent-selinux)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-ssm-agent-selinux/blob/main/README.md)
- README blob SHA: 47b08b48cbd9889a8a9ddfa24078448fb5fc62a0
- README bytes captured: 3136
- README truncated at capture limit: False
- Repository ID: 574578031
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

SELinux policy to confine Amazon SSM agent

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T06:16:51+00:00

### Short excerpt (up to 300 words)

> SELINUXTYPE=targeted Clone the repository,

### README headings

- AMAZON-SSM-AGENT-SELINUX POLICY
- Note - We provide a base SELinux policy that allows basic Amazon-ssm-agent functionality. If users want more permissions, then they should review the SELinux documentation to understand how to update the policy to allow additional access, and scope it appropriately for their use case.
- Note - This policy has been tested to work on AL2 and AL2023 only for now. Please make sure that the OS you are using is AL2 or AL2023.
- Note - This policy forfeits sudo access on the machine that utilizes it i.e. you will lose access to the root level user.
- Installation instructions
- Note - It is recommended to start SELinux in permissive mode before enabling it in enforcement mode.
- This file controls the state of SELinux on the system.
- SELINUX= can take one of these three values:
- enforcing - SELinux security policy is enforced.
- permissive - SELinux prints warnings instead of enforcing.
- disabled - No SELinux policy is loaded.
- SELINUXTYPE= can take one of three two values:
- targeted - Targeted processes are protected,
- minimum - Modification of targeted policy. Only selected processes are protected.
- mls - Multi Level Security protection.
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Limitations and security: mls - Multi Level Security protection.

> SELINUXTYPE=targeted Clone the repository,

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Roff | 23,180 |
| Shell | 2,105 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: GPL-2.0
- Stars at capture: 8
- Forks at capture: 5
- Last updated: 2025-10-03T05:10:59Z
- Last pushed: 2024-09-24T19:55:04Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-ssm-agent-selinux)
- [README](https://github.com/aws/amazon-ssm-agent-selinux/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-ssm-agent-selinux/issues)
- [Releases](https://github.com/aws/amazon-ssm-agent-selinux/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
