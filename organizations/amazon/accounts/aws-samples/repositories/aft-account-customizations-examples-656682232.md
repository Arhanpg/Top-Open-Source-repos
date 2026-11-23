# aws-samples/aft-account-customizations-examples

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/aft-account-customizations-examples](https://github.com/aws-samples/aft-account-customizations-examples)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/aft-account-customizations-examples/blob/main/README.md)
- README blob SHA: 0eb7c24eddcca5d62b109cd0e47c27a751d1e18f
- Repository ID: 656682232
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:42:53+00:00

### Short excerpt (up to 100 words)

> This project contains a practical use case of the AFT account customizations logic. More details about the AFT see AFT Doc When working in multi-account scenarios it is quite common to come across the following situation: - 3 Workload accounts (1 development account, 1 staging account and 1 production account) - 1 Account for SLDC (Pipelines, Version Control and GITOPS) - In this type of account, cross-account access to the workload accounts is necessary so that the pipelines can deliver the codes in their respective environments It turns out to be a challenge to manage the creation of these accounts

### README headings

- aft-account-customizations-examples
- Background and solutions considerations
- Solution overview
- Workload accounts (dev, hml e prod)
- Getting CIDR available for use
- VPC creation
- Updating CIDR MGMT with VPC ID
- Pipeline Accounts
- Creating cross-account roles
- AWS CodeCommit repository
- IAC Pipeline Deployment
- Jinja
- Folder Structure
- Deployment
- To use this solution you must:
- Deploy
- Usage
- Credits
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 44,103 |
| Shell | 39,515 |
| Jinja | 5,465 |
| Python | 5,233 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- DEV/api_helpers/python/requirements.txt (capture: captured) — dependency clues: boto3, requests
- HML/api_helpers/python/requirements.txt (capture: captured) — dependency clues: boto3, requests
- PIPELINE/api_helpers/python/requirements.txt (capture: captured) — dependency clues: Jinja2, boto3, jinja2-cli, requests
- PRODUCTION/api_helpers/python/requirements.txt (capture: captured) — dependency clues: boto3, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 10
- Forks at capture: 2
- Last updated: 2026-09-05T13:31:23Z
- Last pushed: 2024-01-11T18:53:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/aft-account-customizations-examples)
- [README](https://github.com/aws-samples/aft-account-customizations-examples/blob/main/README.md)
- [Issues](https://github.com/aws-samples/aft-account-customizations-examples/issues)
- [Releases](https://github.com/aws-samples/aft-account-customizations-examples/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
