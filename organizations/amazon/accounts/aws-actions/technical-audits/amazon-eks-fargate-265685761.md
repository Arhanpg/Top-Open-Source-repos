# aws-actions/amazon-eks-fargate

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/amazon-eks-fargate
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:28:58+00:00

## Project purpose

This action allows to manage the lifecycle of an Amazon EKS cluster running on AWS Fargate.

## Why this project is used

Creates an EKS on Fargate cluster

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Shell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: entrypoint.sh

## Setup and usage

- Usage: In a GH Action file, for example, .github/workflows/main.yaml:
- Usage: runs-on: ubuntu-latest
- Usage: name: Create an EKS on Fargate cluster
- Usage: - name: Configure AWS credentials
- Usage: uses: aws-actions/configure-aws-credentials@v1
- Usage: aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
- Usage: aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
- Usage: aws-region: eu-west-1

## Limitations and caveats

- Security Disclosures: If you would like to report a potential security issue in this project, please do not create a GitHub issue. Instead, please follow the instructions here or email AWS security directly.

## Evidence and provenance

- README: https://github.com/aws-actions/amazon-eks-fargate/blob/master/README.md
- README SHA: 20e2d4438616a5de0cfefc51505392c1e8604eab
- Manifests: Dockerfile
- Sampled source files: entrypoint.sh
- Git tree state: captured
- Evidence fingerprint: 2c1b8ac384b25125f6c63d86e9cabf9a4c0abd49edf3de8bcbbdd765687fd8c8

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
