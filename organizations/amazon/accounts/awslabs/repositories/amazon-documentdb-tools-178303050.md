# awslabs/amazon-documentdb-tools

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-documentdb-tools](https://github.com/awslabs/amazon-documentdb-tools)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/amazon-documentdb-tools/blob/master/README.md)
- README blob SHA: 5c1686a7e032edd56cf76474ba6d42c456111966
- Repository ID: 178303050
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Tools for use with the Amazon DocumentDB managed document database service.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:27:25+00:00

### Short excerpt (up to 100 words)

> This repository contains several tools to help users with Amazon DocumentDB including migration, monitoring, and performance. A few of the most popular tools are listed below but there are additional tools in the migration, monitoring, operations, and performance folders. The DocumentDB Compatibility Tool examines log files from MongoDB or source code from MongoDB applications to determine if there are any queries which use operators that are not supported in Amazon DocumentDB. The DocumentDB Index Tool makes it easy to migrate only indexes (not data) between a source MongoDB deployment and an Amazon DocumentDB cluster. The contents of this repository are

### README headings

- Amazon DocumentDB Tools
- Amazon DocumentDB Compatibility Tool
- Amazon DocumentDB Index Tool
- Prism for Amazon DocumentDB
- Support
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 2,471,467 |
| CSS | 75,882 |
| Shell | 37,676 |
| HTML | 17,286 |
| JavaScript | 5,366 |
| Dockerfile | 157 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- global-clusters-automation/requirements.txt (capture: captured) — dependency clues: boto3, botocore
- index-tool/Dockerfile (capture: captured)
- index-tool/requirements.txt (capture: captured) — dependency clues: pymongo
- developer/amazon-documentdb-python-client/pyproject.toml (capture: captured) — dependency clues: boto3, pymongo
- migration/data-differ/requirements.txt (capture: captured) — dependency clues: deepdiff, pymongo, rich
- migration/dms_buddy/requirements.txt (capture: captured) — dependency clues: humanize, pymongo

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 162
- Forks at capture: 88
- Last updated: 2026-11-12T15:10:25Z
- Last pushed: 2026-11-20T15:08:48Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-documentdb-tools)
- [README](https://github.com/awslabs/amazon-documentdb-tools/blob/master/README.md)
- [Issues](https://github.com/awslabs/amazon-documentdb-tools/issues)
- [Releases](https://github.com/awslabs/amazon-documentdb-tools/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
