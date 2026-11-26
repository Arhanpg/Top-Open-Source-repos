# aws-solutions/aws-control-tower-customizations

- Company: Amazon
- Account: aws-solutions
- Repository: https://github.com/aws-solutions/aws-control-tower-customizations
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:40:05+00:00

## Project purpose

The Customizations for AWS Control Tower solution combines AWS Control Tower and other highly-available, trusted AWS services to help customers more quickly set up a secure, multi-account AWS environment based on AWS best practices. Customers can easily add customizations to their AWS Control Tower landing zone using an AWS CloudFormation template, service control policies (SCPs), and resource control policies (RCPs). Customers can deploy their custom template and policies to both individual accounts and organizational units (OUs) within their organization. Customizations for AWS Control Tower integrates with AWS Control Tower lifecycle events to ensure that resource deployments stay in sync with the customer's landing zone. For example, when a new account is created using the AWS Control Tower account factory, the solution ensures that all resources attached to the account's OUs will be

## Why this project is used

The Customizations for AWS Control Tower solution combines AWS Control Tower and other highly-available, trusted AWS services to help customers more quickly set up a secure, multi-account AWS environment using AWS best practices.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Shell, Jinja
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: source/src/cfct/__init__.py, source/src/cfct/aws/__init__.py, source/src/cfct/aws/services/__init__.py, source/src/cfct/aws/services/cloudformation.py

## Setup and usage

- Getting Started: To get started with Customizations for AWS Control Tower, please review the documentation

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-solutions/aws-control-tower-customizations/blob/main/README.md
- README SHA: 3ab087681536554776b6d28a8e911c3739bfb226
- Manifests: source/src/pyproject.toml, source/src/setup.py
- Sampled source files: source/src/cfct/aws/services/cloudformation.py
- Git tree state: captured
- Evidence fingerprint: d30f8d155126fe4ecfa14ea617bec3737a7865a76bc653c4db030e1aa3796fa2

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
