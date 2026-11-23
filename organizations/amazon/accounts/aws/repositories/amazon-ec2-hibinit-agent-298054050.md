# aws/amazon-ec2-hibinit-agent

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-ec2-hibinit-agent](https://github.com/aws/amazon-ec2-hibinit-agent)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/amazon-ec2-hibinit-agent/blob/master/README.md)
- README blob SHA: c8bd5611226ee5ae37cd642d6c9b4b5bc4c09ebb
- Repository ID: 298054050
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:11:10+00:00

### Short excerpt (up to 100 words)

> Sets up hibernation support for EC2 instances on supported instance types. On startup, the agent ensures a properly sized swap file exists and configures the kernel and bootloader for hibernation resume. On receiving an ACPI sleep event, the agent enables swap and initiates hibernation. On resume, the agent disables the swap file. The agent is configured via etc/hibinit-config.cfg. Install development tools and build dependencies for your distro: sudo yum group install "Development Tools" sudo yum install python2-devel systemd sudo yum group install "Development Tools" sudo yum install python3-devel systemd-rpm-macros sudo dnf group install "Development Tools" sudo yum install python3-devel selinux-policy-devel

### README headings

- Amazon EC2 Hibernation Agent
- Configuration
- Building

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 4,430 |
| Makefile | 2,035 |
| Python | 650 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- setup.py (capture: captured)
- packaging/rhel/ec2hibernatepolicy/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 20
- Forks at capture: 25
- Last updated: 2026-09-09T17:11:00Z
- Last pushed: 2026-08-10T17:44:37Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-ec2-hibinit-agent)
- [README](https://github.com/aws/amazon-ec2-hibinit-agent/blob/master/README.md)
- [Issues](https://github.com/aws/amazon-ec2-hibinit-agent/issues)
- [Releases](https://github.com/aws/amazon-ec2-hibinit-agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
