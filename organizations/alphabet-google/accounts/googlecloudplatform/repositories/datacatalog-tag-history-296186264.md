# GoogleCloudPlatform/datacatalog-tag-history

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/datacatalog-tag-history](https://github.com/GoogleCloudPlatform/datacatalog-tag-history)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/datacatalog-tag-history/blob/master/README.md)
- README blob SHA: e12fbbee9de3c6925f8ba08b20aeb300efa537b2
- README bytes captured: 15761
- README truncated at capture limit: False
- Repository ID: 296186264
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Historical metadata of your data warehouse is a treasure trove to discover not just insights about changing data patterns, but also quality and user behaviour. This solution creates Data Catalog Tags history in BigQuery since Data Catalog keeps only the latest version of metadata for fast searchability.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:47:35+00:00

### Short excerpt (up to 300 words)

> export PROJECT_ID="your-project-id" This tutorial assumes some This implementation handles only

### README headings

- Record Data Catalog Tags changes to BigQuery in real-time
- Concepts<a name="concepts"></a>
- Prerequisites<a name="prerequisites"></a>
- Objectives<a name="objectives"></a>
- Costs<a name="costs"></a>
- Before you begin<a name="before-you-begin"></a>
- Setting up your environment<a name="setup-environment"></a>
- Creating resources<a name="create-resources"></a>
- Create BigQuery table<a name="setup-bigquery"></a>
- Configure Pub/Sub topic and subscription<a name="configure-pubsub"></a>
- Configure Log sink<a name="configure-log-sink"></a>
- Identify the Logs writer service account
- Grant Publish permission to the Logging writer
- Create Service Accounts<a name="create-service-account"></a>
- Deploy the Tag history recording pipeline<a name="launch-pipeline"></a>
- **Pipeline DAG**
- Manual Test<a name="manual-test"></a>
- Limitations<a name="limitations"></a>
- Cleaning up<a name="cleanup"></a>
- Delete the project<a name="delete-project"></a>
- License<a name="license"></a>

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: The GCP project to use for this tutorial

> export PROJECT_ID="your-project-id"

### Technology and requirements: Prerequisites<a name="prerequisites"></a>

> This tutorial assumes some

### Limitations and security: Limitations<a name="limitations"></a>

> This implementation handles only

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 85,359 |
| Shell | 3,058 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: auto-value, auto-value-annotations, beam-runners-direct-java, beam-runners-google-cloud-dataflow-java, beam-sdks-java-core, beam-sdks-java-extensions-protobuf, beam-sdks-java-io-google-cloud-platform, datacatalog-tag-history, exec-maven-plugin, flogger, flogger-system-backend, google-cloud-datacatalog, google-extensions, guava, hamcrest-all, jacoco-maven-plugin, json-path, jsonassert, junit, libraries-bom

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 13
- Forks at capture: 3
- Last updated: 2023-01-12T21:40:27Z
- Last pushed: 2021-07-21T13:15:36Z
- Topics: analytics, bigquery, data-catalog, data-governance, metadata-management

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/datacatalog-tag-history)
- [README](https://github.com/GoogleCloudPlatform/datacatalog-tag-history/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/datacatalog-tag-history/issues)
- [Releases](https://github.com/GoogleCloudPlatform/datacatalog-tag-history/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
