# Azure/azure-kusto-labs

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/azure-kusto-labs](https://github.com/Azure/azure-kusto-labs)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/azure-kusto-labs/blob/master/README.md)
- README blob SHA: 89947650a2c1928e682a06005b9a458e90409779
- README bytes captured: 3232
- README truncated at capture limit: False
- Repository ID: 252196717
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Self-contained, hands-on-labs with detailed and step-by-step instructions, associated collateral (data, code etc) on trying out various features and integration points of Azure Data Explorer (Kusto)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T03:51:43+00:00

### Short excerpt (up to 300 words)

> Guidelines on README format:

### README headings

- About
- Labs
- 1.  Kafka Ingestion series
- 2.  Kubernetes Container Log Analytics
- [2.1. Kubernetes Container Log Analytics with Fluent-Bit](k8s-container-log-analytics/fluent-bit/README.md)
- 3. Cosmos DB integration with Azure Data Explorer
- [3.1 Cosmos DB integration with Azure Data Explorer using change feed](cosmosdb-adx-integration)
- 4. Databricks integration with Azure Data Explorer
- [4.1 Databricks integration with Azure Data Explorer using Azure Functions](databricks-adx-integration/README.md)
- Contributing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: About

> Guidelines on README format:

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 247,413 |
| PowerShell | 118,057 |
| Shell | 9,988 |
| Go | 2,343 |
| Dockerfile | 866 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- kafka-integration/dockerized-quickstart/connector/Dockerfile (capture: captured)
- kafka-integration/dockerized-quickstart/storm-events-producer/Dockerfile (capture: captured)
- kafka-integration/dockerized-quickstart/storm-events-producer/go.mod (capture: captured) — dependency clues: github.com/Shopify/sarama
- databricks-adx-integration/src/code/tools/ADXProvisionTool/requirements.txt (capture: captured) — dependency clues: adal, azure-common, azure-core, azure-kusto-data, azure-mgmt-kusto, numpy
- databricks-adx-integration/src/code/tools/FakeDataGenerator/requirements.txt (capture: captured) — dependency clues: apscheduler, azure-storage-blob
- databricks-adx-integration/src/code/functions/adxingesterrorhandler/__app__/requirements.txt (capture: captured) — dependency clues: applicationinsights, azure-functions, azure-storage-blob, requests, tenacity

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 52
- Forks at capture: 45
- Last updated: 2026-08-17T22:13:27Z
- Last pushed: 2026-08-17T22:11:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/azure-kusto-labs)
- [README](https://github.com/Azure/azure-kusto-labs/blob/master/README.md)
- [Issues](https://github.com/Azure/azure-kusto-labs/issues)
- [Releases](https://github.com/Azure/azure-kusto-labs/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
