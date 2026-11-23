# SAP-cloud-infrastructure/metal-telemetry-operator

- Company: SAP
- GitHub account: [https://github.com/SAP-cloud-infrastructure](https://github.com/SAP-cloud-infrastructure)
- Mapping status: official-directory-listed
- Repository: [SAP-cloud-infrastructure/metal-telemetry-operator](https://github.com/SAP-cloud-infrastructure/metal-telemetry-operator)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-cloud-infrastructure/metal-telemetry-operator/blob/main/README.md)
- README blob SHA: 5517420d59a7dc26abd76599ecd37fb4d3dc73f6
- Repository ID: 1444393847
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:38:05+00:00

### Short excerpt (up to 100 words)

> A Kubernetes operator that streams hardware telemetry and alert events from Baseboard Management Controllers (BMCs) via the Redfish API and publishes them as Prometheus metrics. The Metal Telemetry Operator (MTO) watches `BMC` resources and maintains persistent Redfish connections to each BMC, collecting two classes of data: **Telemetry** — continuous MetricReport streams delivered either via Server-Sent Events (SSE) for Dell iDRAC and Lenovo XCC3, or via HTTP push webhooks for HPE iLO. Each metric reading is published as a Prometheus gauge labelled with the BMC hostname, metric ID, unit, and origin context. **Alerts** — Redfish event notifications (hardware faults, component state

### README headings

- metal-telemetry-operator
- Description
- Metrics
- `redfish_telemetry_reading` — Gauge
- Per-node CPU utilization
- Inlet temperature across the fleet
- Total power draw by region
- All BMCs currently reporting at least one reading
- All distinct metric_id values being reported across the fleet
- Which metric_ids a specific BMC reports
- Metric coverage by hardware manufacturer and model (requires kube-state-metrics integration)
- Joins redfish_telemetry_reading with kube_ironcore_bmc_info to attach manufacturer/model labels
- `redfish_event_alert_total` — Counter
- Rate of critical hardware events across the fleet
- Most frequent fault message IDs in the last 24h
- Per-component alert distribution
- `redfish_server_critical_alert` — Gauge
- Servers currently in a critical hardware fault state
- Alert: any server has been in critical state for more than 10 minutes
- `redfish_event_pipeline_test_timestamp` — Gauge
- BMCs whose last successful test event was more than 30 minutes ago
- BMCs with no successful test event in Prometheus memory (never received one)
- Alert: pipeline health degraded for more than 20 minutes
- `redfish_stream_connection_status` — Gauge
- BMCs where any stream is not connected
- Connection health breakdown by reason across all streams
- BMCs where the metrics stream is connected
- Count of BMCs with both streams fully connected
- BMCs that failed to subscribe due to slot exhaustion (push mode)
- Standard controller-runtime metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 405,833 |
| Makefile | 19,743 |
| Shell | 4,370 |
| Starlark | 1,203 |
| Dockerfile | 740 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/Masterminds/semver/v3, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading, github.com/go-openapi/swag/mangling, github.com/go-openapi/swag/netutils
- Makefile (capture: captured)
- dashboards/go.mod (capture: captured) — dependency clues: github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/go-jose/go-jose/v4, github.com/golang-jwt/jwt/v5, github.com/google/uuid, github.com/jpillora/backoff, github.com/kr/text, github.com/muhlemmer/gu, github.com/munnerz/goautoneg, github.com/mwitkow/go-conntrack, github.com/perses/common, github.com/perses/perses, github.com/perses/plugins/barchart, github.com/perses/plugins/datasourcevariable, github.com/perses/plugins/prometheus, github.com/perses/plugins/statchart, github.com/perses/plugins/table, github.com/perses/plugins/timeserieschart, github.com/perses/spec, github.com/prometheus/client_golang
- dist/chart/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-11-12T14:38:51Z
- Last pushed: 2026-11-21T18:33:39Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-cloud-infrastructure/metal-telemetry-operator)
- [README](https://github.com/SAP-cloud-infrastructure/metal-telemetry-operator/blob/main/README.md)
- [Issues](https://github.com/SAP-cloud-infrastructure/metal-telemetry-operator/issues)
- [Releases](https://github.com/SAP-cloud-infrastructure/metal-telemetry-operator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
