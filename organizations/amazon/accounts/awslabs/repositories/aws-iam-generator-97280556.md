# awslabs/aws-iam-generator

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-iam-generator](https://github.com/awslabs/aws-iam-generator)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/aws-iam-generator/blob/master/README.md)
- README blob SHA: 0a3f4e91d164ca76ba7010187437cc022baad9bc
- README bytes captured: 15179
- README truncated at capture limit: False
- Repository ID: 97280556
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Generate Multi-Account IAM users/groups/roles/policies from a simple YAML configuration file and Jinja2 templates. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T19:36:32+00:00

### Short excerpt (up to 300 words)

> For those config sections $ ./build.py --help usage:

### README headings

- iam_generator
- Build Environment
- Usage
- Docker Image
- Building the Image
- Running as a docker container
- General Function
- config.yaml key sections
- `global:` section
- `accounts:` section
- `policies:` section
- Managed Policies derived from a jinja2 template
- Managed Policies for sts:AssumeRole (auto generated!)
- `roles:` section
- Example of a role that can be assumed from another account
- Example of an ec2 role
- Example of a federated role
- `users:` section
- An example of a user that is not a member of a group, and has a managed_policy directly attached
- An example of a user as a member of groups
- `groups:` section
- `retain_on_delete` variable
- A note about `managed_policies`
- Importing resources from other templates

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: A note about `managed_policies`

> For those config sections

### Getting started and usage: Usage

> $ ./build.py --help usage:

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 41,047 |
| Jinja | 21,407 |
| Shell | 940 |
| Dockerfile | 280 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- Pipfile (capture: captured) — dependency clues: PyYAML, name, python_version, troposphere, url, verify_ssl
- requirements.txt (capture: captured) — dependency clues: jinja2, pyyaml, troposphere

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 245
- Forks at capture: 54
- Last updated: 2026-10-27T17:39:17Z
- Last pushed: 2021-04-27T14:41:33Z
- Topics: aws, aws-cloudformation, aws-iam, aws-manage, aws-multiaccount

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-iam-generator)
- [README](https://github.com/awslabs/aws-iam-generator/blob/master/README.md)
- [Issues](https://github.com/awslabs/aws-iam-generator/issues)
- [Releases](https://github.com/awslabs/aws-iam-generator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
