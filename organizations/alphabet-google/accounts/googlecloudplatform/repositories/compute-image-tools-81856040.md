# GoogleCloudPlatform/compute-image-tools

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/compute-image-tools](https://github.com/GoogleCloudPlatform/compute-image-tools)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/compute-image-tools/blob/master/README.md)
- README blob SHA: 4f9eb807228f5e450ae58ac3c828ae28cd6805c0
- README bytes captured: 2719
- README truncated at capture limit: False
- Repository ID: 81856040
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Tools and scripts for Google Compute Engine images.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:09:34+00:00

### Short excerpt (up to 300 words)

> Tools for building, testing, releasing, and upgrading

### README headings

- Compute Image Tools
- [GCE Export](gce_export)
- [Windows Upgrade](gce_windows_upgrade)
- [Image Publish](gce_image_publish)
- Contributing
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Compute Image Tools

> Tools for building, testing, releasing, and upgrading

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 835,651 |
| PowerShell | 170,619 |
| Python | 161,771 |
| Shell | 105,150 |
| Batchfile | 12,024 |
| Dockerfile | 4,690 |
| Go Template | 4,534 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- cleanerupper_container/Dockerfile (capture: captured)
- cleanerupper_container/go.mod (capture: captured) — dependency clues: cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/longrunning, cloud.google.com/go/osconfig, github.com/GoogleCloudPlatform/cloud-image-tests, github.com/GoogleCloudPlatform/compute-daisy, github.com/cespare/xxhash/v2, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/google/s2a-go, github.com/google/uuid, github.com/googleapis/enterprise-certificate-proxy, github.com/googleapis/gax-go/v2, go.opentelemetry.io/auto/sdk, go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc, go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp, go.opentelemetry.io/otel
- cli_tools/go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/logging, cloud.google.com/go/longrunning, cloud.google.com/go/monitoring, cloud.google.com/go/storage, github.com/GoogleCloudPlatform/compute-daisy, github.com/GoogleCloudPlatform/compute-image-tools/common, github.com/GoogleCloudPlatform/compute-image-tools/proto/go, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/cenkalti/backoff/v4, github.com/cespare/xxhash/v2, github.com/cncf/xds/go, github.com/envoyproxy/go-control-plane/envoy, github.com/envoyproxy/protoc-gen-validate
- cli_tools_tests/go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/logging, cloud.google.com/go/longrunning, cloud.google.com/go/monitoring, cloud.google.com/go/storage, github.com/GoogleCloudPlatform/compute-daisy, github.com/GoogleCloudPlatform/compute-image-tools/cli_tools, github.com/GoogleCloudPlatform/compute-image-tools/common, github.com/GoogleCloudPlatform/compute-image-tools/go/e2e_test_utils, github.com/GoogleCloudPlatform/compute-image-tools/proto/go, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/cespare/xxhash/v2, github.com/cncf/xds/go, github.com/envoyproxy/go-control-plane/envoy
- common/go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/logging, cloud.google.com/go/longrunning, cloud.google.com/go/monitoring, cloud.google.com/go/storage, github.com/GoogleCloudPlatform/compute-daisy, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/cespare/xxhash/v2, github.com/cncf/xds/go, github.com/envoyproxy/go-control-plane/envoy, github.com/envoyproxy/protoc-gen-validate, github.com/felixge/httpsnoop, github.com/go-jose/go-jose/v4, github.com/go-logr/logr
- gce_export/go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/logging, cloud.google.com/go/longrunning, cloud.google.com/go/monitoring, cloud.google.com/go/storage, github.com/GoogleCloudPlatform/compute-daisy, github.com/GoogleCloudPlatform/compute-image-tools/cli_tools, github.com/GoogleCloudPlatform/compute-image-tools/proto/go, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/cespare/xxhash/v2, github.com/cncf/xds/go, github.com/dustin/go-humanize, github.com/envoyproxy/go-control-plane/envoy, github.com/envoyproxy/protoc-gen-validate

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 219
- Forks at capture: 170
- Last updated: 2026-11-11T20:01:54Z
- Last pushed: 2026-11-19T18:10:39Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/compute-image-tools)
- [README](https://github.com/GoogleCloudPlatform/compute-image-tools/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/compute-image-tools/issues)
- [Releases](https://github.com/GoogleCloudPlatform/compute-image-tools/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
