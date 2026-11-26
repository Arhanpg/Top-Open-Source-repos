# aws/Trusted-Advisor-Tools

- Company: Amazon
- Account: aws
- Repository: https://github.com/aws/Trusted-Advisor-Tools
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:31:25+00:00

## Project purpose

AWS Trusted Advisor provides real time guidance to help users provision their resources following AWS best practices. You can now create configurable, rule-based events for automated actions based on AWS Trusted Advisor’s library of best-practice checks using Amazon EventBridge. The sample functions provided help to automate Trusted Advisor best practices.

## Why this project is used

The sample functions provided help to automate AWS Trusted Advisor best practices using Amazon Cloudwatch events and AWS Lambda.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, JavaScript, HCL, Shell, CSS, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @cloudscape-design/components, @cloudscape-design/global-styles, @vitejs/plugin-react, aws-cdk-lib, boto3, bs4, constructs, deepagents, langchain-aws, lodash-es, pytest, pytest-mock, react, react-dom, react-grid-layout, regex, requests, six, vite
- Build/package tools: npm-compatible manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: TA-WellArchitected/tawa-optimization-starter/src/tawa/app.py, AWSQuotaIncreaseSupport/cdk/app.py, IAMPasswordPolicy/set_password_policy/app.py, S3BucketVersioning/lambda/app.py

## Setup and usage

- Setup and Usage: Setup and usage instructions are present for each tool in its respective directory:
- Setup and Usage: Stop Amazon EC2 instances with low utilization
- Setup and Usage: Create snapshots for EBS volumes with no recent backup
- Setup and Usage: Delete exposed IAM Keys and monitor usage
- Setup and Usage: Enable S3 bucket Versioning
- Setup and Usage: More information about Trusted Advisor is available here: https://aws.amazon.com/premiumsupport/trustedadvisor/

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws/Trusted-Advisor-Tools/blob/master/README.md
- README SHA: 4a9f7b06c8d379fc476c931c5d43759e057b1440
- Manifests: AWSQuotaIncreaseSupport/cdk/requirements.txt, TA-WellArchitected/tawa-eisenhower-matrix-app/package.json, S3IncompleteMPUAbort/ta-s3-incomplete-mpu-abort/apply_lifecycle_function/requirements.txt, S3IncompleteMPUAbort/ta-s3-incomplete-mpu-abort/tests/requirements.txt, AWSQuotaIncreaseSupport/cdk/layers/deepagents/requirements.txt, TA-WellArchitected/tawa-optimization-starter/src/tawa/requirements.txt
- Sampled source files: TA-WellArchitected/tawa-optimization-starter/src/tawa/app.py, AWSQuotaIncreaseSupport/cdk/app.py, IAMPasswordPolicy/set_password_policy/app.py, S3BucketVersioning/lambda/app.py
- Git tree state: captured
- Evidence fingerprint: e2a3d796fda1b7586ad3060a5bfe9ef74f8986b025194135ba3142d8a80911e3

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
