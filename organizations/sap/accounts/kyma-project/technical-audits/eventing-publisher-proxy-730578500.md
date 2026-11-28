# kyma-project/eventing-publisher-proxy

- Company: SAP
- Account: kyma-project
- Repository: https://github.com/kyma-project/eventing-publisher-proxy
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:00:08+00:00

## Project purpose

The Eventing Publisher Proxy receives legacy and Cloud Event publishing requests from the cluster workloads (microservice or Serverless functions) and redirects them to the Enterprise Messaging Service Cloud Event Gateway. It also fetches a list of subscriptions for a connected application.

## Why this project is used

The Eventing Publisher Proxy receives legacy and Cloud Event publishing requests from the cluster workloads (microservice or Serverless functions) and redirects them to the Enterprise Messaging Service Cloud Event Gateway. It also fetches a list of subscriptions for a connected application.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Makefile, Shell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/antithesishq/antithesis-sdk-go, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/cloudevents/sdk-go/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/golang/groupcache, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/go-tpm, github.com/google/uuid, github.com/gorilla/mux, github.com/josharian/intern, github.com/json-iterator/go, github.com/kelseyhightower/envconfig, github.com/klauspost/compress, github.com/kylelemons/godebug, github.com/kyma-project/eventing-manager, github.com/kyma-project/kyma/common/logging, github.com/kyma-project/kyma/components/central-application-gateway, github.com/kyma-project/nats-manager, github.com/mailru/easyjson, github.com/minio/highwayhash, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/nats-io/jwt/v2, github.com/nats-io/nats-server/v2, github.com/nats-io/nats.go, github.com/nats-io/nkeys, github.com/nats-io/nuid, github.com/onsi/gomega, github.com/pkg/errors, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/spf13/pflag, github.com/stretchr/objx, github.com/stretchr/testify, github.com/x448/float16, go.opencensus.io, go.uber.org/multierr, go.uber.org/zap, go.yaml.in/yaml/v2, go.yaml.in/yaml/v3, golang.org/x/crypto, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sys, golang.org/x/term, golang.org/x/text, golang.org/x/time, golang.org/x/xerrors, google.golang.org/genproto/googleapis/api, google.golang.org/protobuf, gopkg.in/evanphx/json-patch.v4, gopkg.in/inf.v0, gopkg.in/yaml.v3, k8s.io/api, k8s.io/apimachinery, k8s.io/client-go, k8s.io/klog/v2, k8s.io/kube-openapi, k8s.io/utils, sigs.k8s.io/controller-runtime, sigs.k8s.io/json, sigs.k8s.io/randfill, sigs.k8s.io/structured-merge-diff/v6, sigs.k8s.io/yaml
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/eventing-publisher-proxy/main.go, pkg/application/applicationtest/applicationtest.go, pkg/application/clean.go, pkg/application/clean_test.go

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/kyma-project/eventing-publisher-proxy/blob/main/README.md
- README SHA: 6d527667bdbd18893fbcbc8465f128952065531a
- Manifests: Dockerfile, go.mod, Makefile, hack/ci/Makefile
- Sampled source files: cmd/eventing-publisher-proxy/main.go, pkg/application/applicationtest/applicationtest.go, pkg/application/clean.go, pkg/application/clean_test.go
- Git tree state: captured
- Evidence fingerprint: 68c717ad70f68796473fde67aca8bf80f519c3f554268e9287337d1ec65e3723

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
