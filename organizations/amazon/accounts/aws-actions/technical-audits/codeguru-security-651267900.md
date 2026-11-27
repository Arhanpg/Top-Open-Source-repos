# aws-actions/codeguru-security

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/codeguru-security
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T06:58:32+00:00

## Project purpose

Amazon CodeGuru Security finds issues in your code and provides recommendations on how to remediate them. CodeGuru Security identifies Security vulnerabilities, such as risks from the top 10 OWASP categories.

## Why this project is used

Amazon CodeGuru Security finds issues in your code and provides recommendations on how to remediate them. CodeGuru Security identifies Security vulnerabilities, such as risks from the top 10 OWASP categories.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Unknown / not established
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: none

## Setup and usage

- Usage: **Step 1: Set up Your workflow.yml File**
- Usage: * **Add checkout to your workflow:**
- Usage: For CodeGuru Security to run, check out your repository using actions/checkout@v3. **You will need to set fetch-depth: 0 to fetch all history for all branches and tags.** For example:
- Usage: - name: Checkout repository
- Usage: uses: actions/checkout@v3
- Usage: fetch-depth: 0 # This is a required field for CodeGuru
- Usage: * **Provide your AWS Credentials:**
- Usage: We recommend following the instructions and using aws-actions/configure-aws-credentials to configure your credentials for a job. The IAM user or IAM role requires AmazonCodeGuruSecurityScanAccess policy. The CodeGuru Security action supports credentials from GitHub hosted runners and self-hosted runners.

## Limitations and caveats

- Amazon CodeGuru Security for GitHub Actions: Amazon CodeGuru Security finds issues in your code and provides recommendations on how to remediate them. CodeGuru Security identifies Security vulnerabilities, such as risks from the top 10 OWASP categories.
- Amazon CodeGuru Security for GitHub Actions: Amazon CodeGuru Security action can be triggered by a pull request, push, or scheduled run of your CI/CD pipeline.
- Amazon CodeGuru Security for GitHub Actions: For more information about setup, see Create code security reviews with GitHub Actions in the *Amazon CodeGuru Security User Guide*.
- Amazon CodeGuru Security for GitHub Actions: To add CodeGuru Security to your CI/CD pipeline, follow the steps under the *Usage* section.
- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-actions/codeguru-security/blob/main/README.md
- README SHA: 7d34028ae77b6fe0cc81fc2b16d9eb6f983bf5ca
- Manifests: none
- Sampled source files: none
- Git tree state: captured
- Evidence fingerprint: 5157e73a64b9ae78e03b0728acc8895e4b02ae0fe9f76ce3f4c4d0ee975b8507

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
