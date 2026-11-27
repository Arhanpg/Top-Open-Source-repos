# kyma-project/eventing-auth-manager

- Company: SAP
- Account: kyma-project
- Repository: https://github.com/kyma-project/eventing-auth-manager
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:41:54+00:00

## Project purpose

Eventing Auth Manager is a central component that is deployed in Kyma Control Plane (KCP). The component manages applications in the SAP Cloud Identity Services - Identity Authentication by creating and deleting them based on the creation or deletion of a managed Kyma runtime.

## Why this project is used

Eventing Auth Manager is a central component that is deployed in Kyma Control Plane (KCP). The component manages applications in the SAP Cloud Identity Services - Identity Authentication by creating and deleting them based on the creation or deletion of a managed Kyma runtime.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Makefile, Shell, Python, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/Masterminds/semver/v3, github.com/apapsch/go-jsonmerge/v2, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/deepmap/oapi-codegen, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading, github.com/go-openapi/swag/mangling, github.com/go-openapi/swag/netutils, github.com/go-openapi/swag/pools, github.com/go-openapi/swag/stringutils, github.com/go-openapi/swag/typeutils, github.com/go-openapi/swag/yamlutils, github.com/go-task/slim-sprig/v3, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/pprof, github.com/google/uuid, github.com/json-iterator/go, github.com/kyma-project/lifecycle-manager/api, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/oapi-codegen/runtime, github.com/onsi/ginkgo/v2, github.com/onsi/gomega, github.com/pkg/errors, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/spf13/pflag, github.com/stretchr/objx, github.com/stretchr/testify, github.com/x448/float16, go.uber.org/multierr, go.uber.org/zap, go.yaml.in/yaml/v2, go.yaml.in/yaml/v3, golang.org/x/mod, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sync, golang.org/x/sys, golang.org/x/term, golang.org/x/text, golang.org/x/time, golang.org/x/tools, gomodules.xyz/jsonpatch/v2, google.golang.org/protobuf, gopkg.in/evanphx/json-patch.v4, gopkg.in/inf.v0, gopkg.in/yaml.v3, k8s.io/api, k8s.io/apiextensions-apiserver, k8s.io/apimachinery, k8s.io/client-go, k8s.io/klog/v2, k8s.io/kube-openapi, k8s.io/utils, pyyaml, requests, sigs.k8s.io/controller-runtime, sigs.k8s.io/json, sigs.k8s.io/randfill, sigs.k8s.io/structured-merge-diff/v6, sigs.k8s.io/yaml
- Build/package tools: Docker build configuration, Go module manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/main.go, cmd/main_test.go, api/v1alpha1/eventingauth_types.go, api/v1alpha1/groupversion_info.go

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/kyma-project/eventing-auth-manager/blob/main/README.md
- README SHA: 85fd1a57df05a11f64d83db3c7204801f86fbfe9
- Manifests: Dockerfile, go.mod, Makefile, hack/scripts/releaselabelvalidator/requirements.txt
- Sampled source files: cmd/main.go, cmd/main_test.go, api/v1alpha1/eventingauth_types.go, api/v1alpha1/groupversion_info.go
- Git tree state: captured
- Evidence fingerprint: 6a8aa3e69f552912bb2acc4d862b438ecf5fe4ee5665b7427af108bbe316f318

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
