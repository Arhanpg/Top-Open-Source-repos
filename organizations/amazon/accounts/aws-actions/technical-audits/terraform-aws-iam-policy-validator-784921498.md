# aws-actions/terraform-aws-iam-policy-validator

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/terraform-aws-iam-policy-validator
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:37:45+00:00

## Project purpose

A GitHub Action that takes an Terraform template, parses the IAM policies attached to IAM roles, users, groups, and resources then runs them through IAM Access Analyzer policy validation and (optionally) custom policy checks. Note that a charge is associated with each custom policy check. For more details about pricing, see IAM Access Analyzer pricing.

## Why this project is used

Policy Validator for AWS IAM Policies in Terraform templates

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: main.py, test_tf.py

## Setup and usage

- Example Usage: **Before each of the following examples, make sure to include the following:**
- Example Usage: - Setting up the role: Role used in the GitHub workflow should have necessary permissions required
- Example Usage: - to be called from the GitHub workflows - setup OpenID Connect(OIDC) provider and IAM role & Trust policy as described in step 1 & 2 in this blog
- Example Usage: - to call the AWS APIs for the policy checks - ValidatePolicy, CheckNoNewAccess, CheckAccessNotGranted, CheckNoPublicAccess. Refer this page for more details
- Example Usage: - name: Checkout Repo
- Example Usage: uses: actions/checkout@v4
- Example Usage: - name: Configure AWS Credentials
- Example Usage: uses: aws-actions/configure-aws-credentials@v4

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-actions/terraform-aws-iam-policy-validator/blob/main/README.md
- README SHA: 63cb49064de987f86e397468e467bbbf98cef2e8
- Manifests: Dockerfile
- Sampled source files: main.py, test_tf.py
- Git tree state: captured
- Evidence fingerprint: e2568484d36006d3b24d9306ecc01a95734466f7f96cee0b5ba813a16caae60c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
