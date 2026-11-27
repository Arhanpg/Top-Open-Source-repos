# aws-samples/Automated-Database-User-Management-Aurora-MySQL

- Company: Amazon
- Account: aws-samples
- Repository: https://github.com/aws-samples/Automated-Database-User-Management-Aurora-MySQL
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:20:04+00:00

## Project purpose

This project provides an AWS Lambda function to manage MySQL database users. The Lambda function can be used to create, delete, update grants, or reset the password of a user. Additionally, it integrates with AWS Secrets Manager for secret management. The function is designed to be triggered via an AWS Systems Manager (SSM) Automation document.

## Why this project is used

This project provides an AWS Lambda function to manage MySQL database users. The Lambda function can be used to create, delete, update grants, or reset the password of a user. Additionally, it integrates with AWS Secrets Manager for secret management. The function is designed to be triggered via an AWS Systems Manager (SSM) Automation document.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Unknown / not established
- Frameworks/libraries: Unknown / not established
- Dependency names: pymysql
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: db_manager.py, lambda_function.py, secret_policy_manager.py, secret_rotation_manager.py

## Setup and usage

No setup information established.

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-samples/Automated-Database-User-Management-Aurora-MySQL/blob/main/README.md
- README SHA: bd4c302c2a73ac5eab64a045171469e152d6afd9
- Manifests: requirements.txt
- Sampled source files: db_manager.py, lambda_function.py, secret_policy_manager.py, secret_rotation_manager.py
- Git tree state: captured
- Evidence fingerprint: 0f283a653fe7bcad20ffc69864bea7b718e77381862056d4ac08c0fa5816c1e3

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
