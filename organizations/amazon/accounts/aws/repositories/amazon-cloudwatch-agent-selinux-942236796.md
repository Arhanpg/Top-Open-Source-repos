# aws/amazon-cloudwatch-agent-selinux

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-cloudwatch-agent-selinux](https://github.com/aws/amazon-cloudwatch-agent-selinux)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-cloudwatch-agent-selinux/blob/main/README.md)
- README blob SHA: f4dd64df8725b5aa5c802d05744d5860a620f53c
- Repository ID: 942236796
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:02:01+00:00

### Short excerpt (up to 100 words)

> This is the SELinux policy for AWS CWA agent. Install this policy to confine your CloudWatch Agent processes. Make sure Amazon CWA agent service is installed and running before compiling and installing the SELinux policy: sudo yum install amazon-cloudwatch-agent sudo systemctl start amazon-cloudwatch-agent Run the following commands: sudo yum update sudo yum install policycoreutils-devel rpm-build git To build and install the SELinux policy, make sure that SELinux config file is in `permissive` or `enforcing` mode in `/etc/selinux/config` file: SELINUX=enforcing SELINUXTYPE=targeted Clone the repository, build and install using the commands below: git clone https://github.com/aws/amazon-cloudwatch-agent-selinux.git cd amazon-cloudwatch-agent-selinux chmod +x amazon_cloudwatch_agent.sh sudo ./amazon_cloudwatch_agent.sh

### README headings

- AMAZON-CLOUDWATCH-AGENT-SELINUX POLICY
- Note - We provide a base SELinux policy that allows basic Amazon-CloudWatch-agent functionality. If users want more permissions, then they should review the SELinux documentation to understand how to update the policy to allow additional access, and scope it appropriately for their use case.
- Note - This policy has been tested to work on AL2 and AL2023 only for now. Please make sure that the OS you are using is AL2 or AL2023.
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

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 1,827 |

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
- Stars at capture: 5
- Forks at capture: 2
- Last updated: 2026-06-08T20:33:14Z
- Last pushed: 2026-06-08T20:33:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-cloudwatch-agent-selinux)
- [README](https://github.com/aws/amazon-cloudwatch-agent-selinux/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-cloudwatch-agent-selinux/issues)
- [Releases](https://github.com/aws/amazon-cloudwatch-agent-selinux/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
