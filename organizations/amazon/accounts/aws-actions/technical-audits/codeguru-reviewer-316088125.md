# aws-actions/codeguru-reviewer

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/codeguru-reviewer
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:52:45+00:00

## Project purpose

Amazon CodeGuru Reviewer finds issues in your Java and Python code and provides recommendations on how to remediate them. CodeGuru Reviewer identifies

## Why this project is used

Amazon CodeGuru Reviewer finds issues in your Java and Python code and provides recommendations on how to remediate them. CodeGuru Reviewer identifies

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
- Usage: For CodeGuru to run, check out your repository using actions/checkout@v2. **You will need to set fetch-depth: 0 to fetch all history for all branches and tags.** For example:
- Usage: - name: Checkout repository
- Usage: uses: actions/checkout@v2
- Usage: fetch-depth: 0 # This is a required field for CodeGuru
- Usage: * **Provide your AWS Credentials:**
- Usage: We recommend following the instructions and using aws-actions/configure-aws-credentials to configure your credentials for a job. The IAM user or IAM role requires AmazonCodeGuruReviewerFullAccess policy and S3 permissions (s3:PutObject, s3:ListBucket, s3:GetObject) for the "codeguru-reviewer-*" S3 bucket. The CodeGuru Reviewer action supports crede

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-actions/codeguru-reviewer/blob/main/README.md
- README SHA: ced3a1583c84ecbb7c161efe1e4129b763aa4936
- Manifests: none
- Sampled source files: none
- Git tree state: captured
- Evidence fingerprint: 89c4a9eb604c5c0e9ec4b23f9c8455c7df8aa18f879e699c0e725a21b42cf42e

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
