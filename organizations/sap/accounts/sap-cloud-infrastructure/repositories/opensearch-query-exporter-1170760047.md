# SAP-cloud-infrastructure/opensearch-query-exporter

- Company: SAP
- GitHub account: [https://github.com/SAP-cloud-infrastructure](https://github.com/SAP-cloud-infrastructure)
- Mapping status: official-directory-listed
- Repository: [SAP-cloud-infrastructure/opensearch-query-exporter](https://github.com/SAP-cloud-infrastructure/opensearch-query-exporter)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-cloud-infrastructure/opensearch-query-exporter/blob/main/README.md)
- README blob SHA: a496ca4991172ebd5356f8e5eb0e4da6ded3ee88
- Repository ID: 1170760047
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Prometheus exporter for OpenSearch queries

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:49:24+00:00

### Short excerpt (up to 100 words)

> A Prometheus exporter that runs custom OpenSearch queries on a schedule and exposes results as metrics. Designed for Kubernetes deployments where teams define their own queries via ConfigMaps. - Go 1.26+ for building from source - An OpenSearch cluster reachable over HTTPS (TLS only) - Credentials with read access to the indices you want to query - **Query-focused**: Only exposes metrics you define, no noise from cluster internals - **Secure**: TLS-only with credential failover support - **Efficient**: Concurrent background query execution, minimal footprint - **Resilient**: Configurable error handling (preserve/drop/zero) per query - **Safe**: `max_query_range` rejects queries that would hit warm/cold

### README headings

- OpenSearch Query Exporter
- Requirements
- Features
- Building
- Configuration
- Global Config
- Optional - cluster stats collectors (all disabled by default)
- Query Files
- Static validation of queries
- Multi-Team Layout
- Query Fields
- Error Handling Strategies
- Max Query Range
- Command-Line Options
- Endpoints
- Generated Metrics
- Always present
- Per query
- Aggregation metrics
- Optional (disabled by default)
- Custom Metric Extraction
- Project Structure
- Support, Feedback, Contributing
- Security / Disclosure
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 122,518 |
| Dockerfile | 671 |
| Makefile | 519 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/kr/text, github.com/munnerz/goautoneg, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, golang.org/x/sys, google.golang.org/protobuf, gopkg.in/yaml.v3
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-10-19T11:11:12Z
- Last pushed: 2026-10-19T11:11:07Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-cloud-infrastructure/opensearch-query-exporter)
- [README](https://github.com/SAP-cloud-infrastructure/opensearch-query-exporter/blob/main/README.md)
- [Issues](https://github.com/SAP-cloud-infrastructure/opensearch-query-exporter/issues)
- [Releases](https://github.com/SAP-cloud-infrastructure/opensearch-query-exporter/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
