# Azure/abfs-backport

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/abfs-backport](https://github.com/Azure/abfs-backport)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/abfs-backport/blob/master/README.md)
- README blob SHA: d63ba29b67363d7d8672e72f8ec9eb13e8198d3b
- Repository ID: 272525093
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This project will provide a bash script and the backported jar. The bash script will patch the cluster with the backported hadoop-azure jar.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:34:26+00:00

### Short excerpt (up to 100 words)

> The ABFS driver allows **Hadoop** clusters and those frameworks that utilize the **Hadoop FileSystem** to connect to their data that is stored in Azure Data Lake Storage Gen2 (ADLS). This driver has been committed into the Apache code repository since version 3.1. For customers that want to connect to ADLS from existing older clusters, we have backported the driver. It is available from this repository in pre-compiled binary form (Java 7 and upwards). There is also a shell script which may be used to patch each node on the cluster. To patch the cluster, all nodes in the cluster must

### README headings

- Backport for ABFS Driver - Install Hadoop ABFS driver on cluster versions prior to v3.1
- Patch the cluster with ABFS driver
- Note:
- Prerequisites
- How the script works
- Usage
- Registering the ABFS driver
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 14,877 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 3
- Forks at capture: 11
- Last updated: 2023-07-25T14:36:38Z
- Last pushed: 2022-04-29T19:24:41Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/abfs-backport)
- [README](https://github.com/Azure/abfs-backport/blob/master/README.md)
- [Issues](https://github.com/Azure/abfs-backport/issues)
- [Releases](https://github.com/Azure/abfs-backport/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
