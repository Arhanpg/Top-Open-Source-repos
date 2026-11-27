# SAP-cloud-infrastructure/sap-hana-backup-integration

- Company: SAP
- Account: SAP-cloud-infrastructure
- Repository: https://github.com/SAP-cloud-infrastructure/sap-hana-backup-integration
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:10:00+00:00

## Project purpose

SAP HANA Backint integration for S3-compatible object storage. Implements the Backint v1.50 to backup, restore, inquire, and delete HANA database backups on CEPH storage using S3 protocol.

## Why this project is used

SAP HANA Backint integration for S3-compatible object storage. Implements the Backint API to backup, restore, inquire, and delete HANA database backups on CEPH storage.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/feature/s3/manager, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go
- Build/package tools: Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/main.go, src/config.go, src/handlers.go, src/logger.go

## Setup and usage

- Usage: hdbbackint is invoked by SAP HANA automatically. The CLI follows the Backint API 1.50 specification.
- Usage: hdbbackint -f -p -u [options]

## Limitations and caveats

- Security / Disclosure: If you find any bug that may be a security problem, please follow our instructions at in our security policy on how to report it. Please do not create GitHub issues for security-related doubts or problems.

## Evidence and provenance

- README: https://github.com/SAP-cloud-infrastructure/sap-hana-backup-integration/blob/main/README.md
- README SHA: b6acde2dae3bf58b2a1bd8d11f84a7f0128f2f59
- Manifests: src/go.mod
- Sampled source files: src/main.go, src/config.go, src/handlers.go, src/logger.go
- Git tree state: captured
- Evidence fingerprint: 5655466d6b4db3707d2180513f3af1e9d63546fdd0f37413417a3d20044b84f6

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
