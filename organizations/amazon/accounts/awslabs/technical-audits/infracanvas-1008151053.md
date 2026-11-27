# awslabs/InfraCanvas

- Company: Amazon
- Account: awslabs
- Repository: https://github.com/awslabs/InfraCanvas
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:19:59+00:00

## Project purpose

[//]: # (Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.) [//]: # (SPDX-License-Identifier: Apache-2.0)

## Why this project is used

[//]: # (Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.) [//]: # (SPDX-License-Identifier: Apache-2.0)

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python
- Frameworks/libraries: Unknown / not established
- Dependency names: boto3, botocore, cfn-lint, checkov, pytest, pyyaml, streamlit
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: app.py, config.py, prompts.py, ui/__init__.py

## Setup and usage

- Installation and Local Running of Code: To locally run the code you must have python installed in your system as a prerequisite. Then follow these steps:-
- Installation and Local Running of Code: - Clone the repository
- Installation and Local Running of Code: - Go to the terminal of the project repository
- Installation and Local Running of Code: - Configure AWS profile
- Installation and Local Running of Code: - Run python3 -m venv .venv
- Installation and Local Running of Code: - Run source .venv/bin/activate
- Installation and Local Running of Code: - Install dependencies pip install -r requirements.txt
- Installation and Local Running of Code: - For running the code use streamlit run app.py

## Limitations and caveats

- Security Best Practices: - **Never commit AWS credentials** to version control
- Security Best Practices: - **Use least privilege principle** - only grant necessary Bedrock permissions
- Security Best Practices: - **Rotate access keys regularly** (if using IAM users)
- Security Best Practices: - **Enable MFA** on your AWS account
- Security Best Practices: - **Use temporary credentials** when possible (SSO preferred)
- 2. Security Analysis (30% of readiness score): Comprehensive security vulnerability detection and compliance checking:
- 2. Security Analysis (30% of readiness score): **Security Issues Detected:**
- 2. Security Analysis (30% of readiness score): - **Encryption**: Unencrypted resources (S3 buckets, EBS volumes, RDS databases, etc.)

## Evidence and provenance

- README: https://github.com/awslabs/InfraCanvas/blob/main/README.md
- README SHA: 9bbe7191a59213a64c0fc38493b310b2370e7611
- Manifests: requirements.txt
- Sampled source files: app.py, config.py, prompts.py, ui/__init__.py
- Git tree state: captured
- Evidence fingerprint: bb2a103a72f0ca36990ae4e50563ea10d762682aba94cb194c4eefc47cb4efdb

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
