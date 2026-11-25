# siemens/snap-to-bucket

- Company: Siemens
- GitHub account: [https://github.com/Siemens](https://github.com/Siemens)
- Mapping status: verified
- Repository: [siemens/snap-to-bucket](https://github.com/siemens/snap-to-bucket)
- Default branch: master
- README: [Open upstream README](https://github.com/siemens/snap-to-bucket/blob/master/README.md)
- README blob SHA: 0e0c2683e250352fff0d22b882e43aaf71683a2d
- README bytes captured: 9435
- README truncated at capture limit: False
- Repository ID: 266053096
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A python tool to automate moving AWS snapshots into an AWS S3 bucket and restore backups from there as an AWS EBS volume.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T01:30:05+00:00

### Short excerpt (up to 300 words)

> $ git clone https://github.com/siemens/snap-to-bucket.git 1. The script needs

### README headings

- snap_to_bucket
- Installation
- Local installation
- PyPi
- Requirements
- Sample IAM policy
- Tag the snapshots to migrate
- Disclaimer
- Backup
- pipenv run snap2bucket --bucket <bucket>
- snap2bucket --bucket <bucket>
- Backup huge data
- Options
- Files on S3
- Recovery
- Manually
- chroot /mnt/snapshot
- grub-install <device>
- update-grub
- From script (experimental)
- pipenv run snap2bucket --restore --bucket <bucket> --key <key>
- snap2bucket --restore --bucket <bucket> --key <key>

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Local installation

> $ git clone https://github.com/siemens/snap-to-bucket.git

### Technology and requirements: Requirements

> 1. The script needs

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 66,802 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Pipfile (capture: captured) — dependency clues: boto3, build_packages, check_package, click, name, psutil, pylint, snap-to-bucket, sphinx, url, verify_ssl
- pyproject.toml (capture: captured)
- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 5
- Forks at capture: 5
- Last updated: 2025-08-21T20:26:49Z
- Last pushed: 2025-08-21T20:27:25Z
- Topics: aws, aws-ebs, aws-ebs-snapshot, aws-s3, backup, boto3

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/siemens/snap-to-bucket)
- [README](https://github.com/siemens/snap-to-bucket/blob/master/README.md)
- [Issues](https://github.com/siemens/snap-to-bucket/issues)
- [Releases](https://github.com/siemens/snap-to-bucket/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
