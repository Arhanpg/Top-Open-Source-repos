# awslabs/amazon-redshift-utils

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-redshift-utils](https://github.com/awslabs/amazon-redshift-utils)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/amazon-redshift-utils/blob/master/README.md)
- README blob SHA: d55bf0ace8de8e0d7b543647cd4ecd93d7bfce73
- README bytes captured: 9667
- README truncated at capture limit: False
- Repository ID: 27759161
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon Redshift Utils contains utilities, scripts and view which are useful in a Redshift environment

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T09:44:04+00:00

### Short excerpt (up to 300 words)

> Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse solution that uses columnar storage to minimise IO, provide high data compression rates, and offer

### README headings

- Amazon Redshift Utilities
- Admin Scripts
- Admin Views
- Stored Procedures
- Column Encoding Utility
- Analyze & Vacuum Utility
- Cloud Data Warehousing Benchmark
- Unload/Copy Utility
- Manifest Generator
- Simple Replay Utility
- Automation Module
- Snapshot Manager
- WLM Query Monitoring Rule (QMR) Action Notification Utility
- Redshift to IDC migration utility
- Redshift to Lake Formation migration utility
- Investigations
- Authentication
- Running utilities
- Docker executions
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Amazon Redshift Utilities

> Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse solution that uses columnar storage to minimise IO, provide high data compression rates, and offer

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 742,054 |
| Shell | 99,898 |
| JavaScript | 93,661 |
| PLpgSQL | 70,423 |
| Jupyter Notebook | 33,088 |
| HTML | 9,385 |
| Dockerfile | 584 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- src/requirements.txt (capture: captured) — dependency clues: boto3, pg8000, pgpasslib, redshift-connector, shortuuid, six, wheel
- src/ColumnEncodingUtility/requirements.txt (capture: captured) — dependency clues: boto3, pgpasslib, redshift_connector, shortuuid
- src/ManifestGenerator/requirements.txt (capture: captured) — dependency clues: boto3, botocore, jmespath, python-dateutil, s3transfer, six, urllib3
- src/RedshiftAutomation/requirements.txt (capture: captured) — dependency clues: boto3, pg8000, pgpasslib, redshift_connector, requests, shortuuid
- src/SimpleReplay/requirements.txt (capture: captured) — dependency clues: Flask, PyYAML, boto3, botocore, coverage, matplotlib, maya, moto, numpy, pandas, python-dateutil, redshift-connector, reportlab, sqlparse, tabulate, tqdm

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2798
- Forks at capture: 1238
- Last updated: 2026-11-19T19:25:08Z
- Last pushed: 2026-11-16T23:10:17Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-redshift-utils)
- [README](https://github.com/awslabs/amazon-redshift-utils/blob/master/README.md)
- [Issues](https://github.com/awslabs/amazon-redshift-utils/issues)
- [Releases](https://github.com/awslabs/amazon-redshift-utils/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
