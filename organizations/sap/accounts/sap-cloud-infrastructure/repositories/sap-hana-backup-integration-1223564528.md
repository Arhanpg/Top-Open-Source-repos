# SAP-cloud-infrastructure/sap-hana-backup-integration

- Company: SAP
- GitHub account: [https://github.com/SAP-cloud-infrastructure](https://github.com/SAP-cloud-infrastructure)
- Mapping status: official-directory-listed
- Repository: [SAP-cloud-infrastructure/sap-hana-backup-integration](https://github.com/SAP-cloud-infrastructure/sap-hana-backup-integration)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-cloud-infrastructure/sap-hana-backup-integration/blob/main/README.md)
- README blob SHA: b6acde2dae3bf58b2a1bd8d11f84a7f0128f2f59
- Repository ID: 1223564528
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

SAP HANA Backint integration for S3-compatible object storage. Implements the Backint API to backup, restore, inquire, and delete HANA database backups on CEPH storage.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:49:29+00:00

### Short excerpt (up to 100 words)

> SAP HANA Backint integration for S3-compatible object storage. Implements the Backint v1.50 to backup, restore, inquire, and delete HANA database backups on CEPH storage using S3 protocol. flowchart TD HANA["SAP HANA Database"] -->|"Backint API call<br>(-f backup/restore/inquire/delete)"| MAIN subgraph hdbbackint MAIN["main.go<br>CLI & Dispatcher"] --> PROTO["protocol.go<br>Protocol Parser & EBID Generator"] MAIN --> CFG["config.go<br>Configuration Loader"] MAIN --> S3["s3client.go<br>S3 Client (AWS SDK v2)"] end CFG -->|"SCI_* parameters"| UTLFILE["initSID.utl<br>Parameter File"] S3 -->|"PutObject <br> GetObject <br> DeleteObject <br> ListObjectsV2"| STORAGE["S3-Compatible Storage<br>(CEPH / SCI)"] PROTO -->|"#SAVED <br> #RESTORED <br> #BACKUP <br> #DELETED <br> #NOTFOUND <br> #ERROR"| HANA Examples: With folder: prod/usr/sap/HXE/SYS/global/hdb/backint/SYSTEMDB/HXE_FULL_90_20260409125112_backup_databackup_1_1/1734105678123.bak Without folder: usr/sap/HXE/SYS/global/hdb/backint/SYSTEMDB/HXE_FULL_90_20260409125112_backup_databackup_1_1/1734105678123.bak - **EBID** (External

### README headings

- hdbbackint | sap-hana-backup-integration
- About this project
- Overview
- Supported Operations
- Architecture
- S3 Object Key Structure
- Getting Started
- Requirements
- Build
- Install
- Example path — adjust SID and version as appropriate
- Configuration
- Recommended location
- Parameter Reference
- Sample Parameter File
- /usr/sap/PRD/SYS/global/hdb/opt/hdbbackint.cfg
- Optional
- SCI_folderName=hanavm001
- Usage
- Flags
- Operational Flows
- Backup
- Restore
- Inquire
- Delete
- Logging and Troubleshooting
- View backint logs for a HANA tenant
- Support, Feedback, Contributing
- Security / Disclosure
- Code of Conduct

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 34,074 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/feature/s3/manager, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 1
- Last updated: 2026-08-21T03:47:02Z
- Last pushed: 2026-09-18T10:45:53Z
- Topics: backup, hdbbackint, sap-hana

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-cloud-infrastructure/sap-hana-backup-integration)
- [README](https://github.com/SAP-cloud-infrastructure/sap-hana-backup-integration/blob/main/README.md)
- [Issues](https://github.com/SAP-cloud-infrastructure/sap-hana-backup-integration/issues)
- [Releases](https://github.com/SAP-cloud-infrastructure/sap-hana-backup-integration/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
