# SAP-cloud-infrastructure/metal-telemetry-operator

- Company: SAP
- Account: SAP-cloud-infrastructure
- Repository: https://github.com/SAP-cloud-infrastructure/metal-telemetry-operator
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:57:53+00:00

## Project purpose

A Kubernetes operator that streams hardware telemetry and alert events from Baseboard Management Controllers (BMCs) via the Redfish API and publishes them as Prometheus metrics.

## Why this project is used

A Kubernetes operator that streams hardware telemetry and alert events from Baseboard Management Controllers (BMCs) via the Redfish API and publishes them as Prometheus metrics.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Makefile, Shell, Starlark, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/Masterminds/semver/v3, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-jose/go-jose/v4, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading, github.com/go-openapi/swag/mangling, github.com/go-openapi/swag/netutils, github.com/go-openapi/swag/pools, github.com/go-openapi/swag/stringutils, github.com/go-openapi/swag/typeutils, github.com/go-openapi/swag/yamlutils, github.com/go-task/slim-sprig/v3, github.com/golang-jwt/jwt/v5, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/pprof, github.com/google/uuid, github.com/ironcore-dev/metal-operator, github.com/jpillora/backoff, github.com/json-iterator/go, github.com/kr/text, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/muhlemmer/gu, github.com/munnerz/goautoneg, github.com/mwitkow/go-conntrack, github.com/onsi/ginkgo/v2, github.com/onsi/gomega, github.com/perses/common, github.com/perses/perses, github.com/perses/plugins/barchart, github.com/perses/plugins/datasourcevariable, github.com/perses/plugins/prometheus, github.com/perses/plugins/statchart, github.com/perses/plugins/table, github.com/perses/plugins/timeserieschart, github.com/perses/spec, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/spf13/pflag, github.com/stmcginnis/gofish, github.com/stretchr/testify, github.com/x448/float16, github.com/zitadel/oidc/v3, github.com/zitadel/schema, go.uber.org/multierr, go.uber.org/zap, go.yaml.in/yaml/v2, go.yaml.in/yaml/v3, golang.org/x/mod, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sync, golang.org/x/sys, golang.org/x/term, golang.org/x/text, golang.org/x/time, golang.org/x/tools, gomodules.xyz/jsonpatch/v2, google.golang.org/protobuf, gopkg.in/evanphx/json-patch.v4, gopkg.in/inf.v0, gopkg.in/yaml.v3, k8s.io/api, k8s.io/apiextensions-apiserver, k8s.io/apimachinery, k8s.io/client-go, k8s.io/klog/v2, k8s.io/kube-openapi, k8s.io/utils, sigs.k8s.io/controller-runtime, sigs.k8s.io/json, sigs.k8s.io/randfill, sigs.k8s.io/structured-merge-diff/v6, sigs.k8s.io/yaml
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/main.go, dashboards/bmc-alerts/main.go, dashboards/bmc-detail/main.go, dashboards/bmc-telemetry/main.go

## Setup and usage

- Getting Started: - go version v1.24.6+
- Getting Started: - docker version 17.03+
- Getting Started: - kubectl version v1.11.3+
- Getting Started: - Access to a Kubernetes v1.11.3+ cluster

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/SAP-cloud-infrastructure/metal-telemetry-operator/blob/main/README.md
- README SHA: 5517420d59a7dc26abd76599ecd37fb4d3dc73f6
- Manifests: Dockerfile, go.mod, Makefile, dashboards/go.mod
- Sampled source files: cmd/main.go, dashboards/bmc-alerts/main.go, dashboards/bmc-detail/main.go, dashboards/bmc-telemetry/main.go
- Git tree state: captured
- Evidence fingerprint: 41a89ebf1c2d904d9614fd5d9db495fbd3dfc0c85c827fafea7bc56597c89ad6

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
