# SAP-cloud-infrastructure/opensearch-alerting

- Company: SAP
- Account: SAP-cloud-infrastructure
- Repository: https://github.com/SAP-cloud-infrastructure/opensearch-alerting
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:02:13+00:00

## Project purpose

The OpenSearch Alerting enables you to monitor your data and send alert notifications automatically to your stakeholders. With an intuitive OpenSearch Dashboards interface and a powerful API, it is easy to set up, manage, and monitor your alerts. Craft highly specific alert conditions using Elasticsearch's full query language and scripting capabilities.

## Why this project is used

The OpenSearch Alerting enables you to monitor your data and send alert notifications automatically to your stakeholders. With an intuitive OpenSearch Dashboards interface and a powerful API, it is easy to set up, manage, and monitor your alerts. Craft highly specific alert conditions using Elasticsearch's full query language and scripting capabilities.

## Core features

- Custom webhook: Custom webhook
  - Evidence: README.md#Highlights

## Technology stack

- Languages: Kotlin, Java, Shell, Python
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle build file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: alerting/src/main/java/org/opensearch/percolator/PercolateQueryBuilderExt.java, alerting/src/main/java/org/opensearch/percolator/PercolatorFieldMapperExt.java, alerting/src/main/java/org/opensearch/percolator/PercolatorPluginExt.java, alerting/src/main/kotlin/org/opensearch/alerting/action/ExecuteMonitorAction.kt

## Setup and usage

No setup information established.

## Limitations and caveats

- Security: If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our vulnerability reporting page. Please do **not** create a public GitHub issue.

## Evidence and provenance

- README: https://github.com/SAP-cloud-infrastructure/opensearch-alerting/blob/main/README.md
- README SHA: a485a5a4657c10903c9d532e4efbdbfee3161f7d
- Manifests: build.gradle, alerting/build.gradle, core/build.gradle, sample-remote-monitor-plugin/build.gradle, spi/build.gradle
- Sampled source files: alerting/src/main/java/org/opensearch/percolator/PercolateQueryBuilderExt.java, alerting/src/main/java/org/opensearch/percolator/PercolatorFieldMapperExt.java, alerting/src/main/java/org/opensearch/percolator/PercolatorPluginExt.java, alerting/src/main/kotlin/org/opensearch/alerting/action/ExecuteMonitorAction.kt
- Git tree state: captured
- Evidence fingerprint: c6fcc5e96cade7aad51d90b83e32856a871186288ec9e688e234d81426e0ee23

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
