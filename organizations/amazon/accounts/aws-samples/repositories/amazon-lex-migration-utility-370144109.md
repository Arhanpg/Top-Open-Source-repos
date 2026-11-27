# aws-samples/amazon-lex-migration-utility

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-lex-migration-utility](https://github.com/aws-samples/amazon-lex-migration-utility)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-lex-migration-utility/blob/main/README.md)
- README blob SHA: e17450e34eb06a9f5654115f1a8170c1c01a8c9c
- README bytes captured: 5015
- README truncated at capture limit: False
- Repository ID: 370144109
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T05:19:31+00:00

### Short excerpt (up to 300 words)

> The Amazon Lex Migration sam build -t custom_resource_template.yml pip install --requirements requirements.txt 2022-03-28 This project is

### README headings

- Amazon Lex Migration Utility
- Deprecation notice
- Purpose
- Installation
- Install the Serverless Application Model
- Install AWS CloudFormation custom resources in the **target account**
- Usage
- Create a configuration file
- Export Lex definitions from the source account
- Prerequisites
- Python 3.x and Node 12.x
- Configure the AWS CLI with a profile for the source account
- Install dependencies
- Export resources
- Deploy to the destination account
- Custom Resources created
- Sample configuration file and template
- Known Issues
- Acknowledgements

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Purpose

> The Amazon Lex Migration

### Getting started and usage: Install AWS CloudFormation custom resources in the **target account**

> sam build -t custom_resource_template.yml

### Technology and requirements: Install dependencies

> pip install --requirements requirements.txt

### Limitations and security: Deprecation notice

> 2022-03-28 This project is

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 18,729 |
| Python | 10,073 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- lex_exporter/requirements.txt (capture: captured) — dependency clues: boto3, jsonschema
- custom-resources/create-connect-lex-permission/package.json (capture: captured) — dependency clues: cfn-response-async
- custom-resources/lex-alias/package.json (capture: captured) — dependency clues: cfn-lambda
- custom-resources/lex-bot/package.json (capture: captured) — dependency clues: cfn-lambda
- custom-resources/lex-intent/package.json (capture: captured) — dependency clues: cfn-lambda, retry
- custom-resources/lex-slot/package.json (capture: captured) — dependency clues: cfn-lambda

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 3
- Last updated: 2025-09-22T16:04:27Z
- Last pushed: 2023-04-10T21:38:55Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-lex-migration-utility)
- [README](https://github.com/aws-samples/amazon-lex-migration-utility/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-lex-migration-utility/issues)
- [Releases](https://github.com/aws-samples/amazon-lex-migration-utility/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
