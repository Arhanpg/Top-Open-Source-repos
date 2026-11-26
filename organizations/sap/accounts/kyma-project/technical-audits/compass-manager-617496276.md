# kyma-project/compass-manager

- Company: SAP
- Account: kyma-project
- Repository: https://github.com/kyma-project/compass-manager
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:50:21+00:00

## Project purpose

Compass Manager **will be** a new Control Plane component. Build using Kubebuilder framework.

## Why this project is used

Manager for the compass module

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Makefile, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: dario.cat/mergo, github.com/99designs/gqlgen, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/agnivade/levenshtein, github.com/asaskevich/govalidator, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading, github.com/go-openapi/swag/mangling, github.com/go-openapi/swag/netutils, github.com/go-openapi/swag/pools, github.com/go-openapi/swag/stringutils, github.com/go-openapi/swag/typeutils, github.com/go-openapi/swag/yamlutils, github.com/go-ozzo/ozzo-validation/v4, github.com/go-task/slim-sprig/v3, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/pprof, github.com/google/uuid, github.com/gorilla/mux, github.com/hashicorp/errwrap, github.com/hashicorp/go-multierror, github.com/huandu/xstrings, github.com/json-iterator/go, github.com/kyma-incubator/compass/components/director, github.com/kyma-project/lifecycle-manager/api, github.com/matryer/is, github.com/mitchellh/copystructure, github.com/mitchellh/reflectwalk, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/onrik/logrus, github.com/onsi/ginkgo/v2, github.com/onsi/gomega, github.com/pkg/errors, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/shopspring/decimal, github.com/sirupsen/logrus, github.com/spf13/cast, github.com/spf13/pflag, github.com/stretchr/objx, github.com/stretchr/testify, github.com/tidwall/gjson, github.com/tidwall/match, github.com/tidwall/pretty, github.com/tidwall/sjson, github.com/vektah/gqlparser/v2, github.com/vrischmann/envconfig, github.com/x448/float16, github.com/xeipuuv/gojsonpointer, github.com/xeipuuv/gojsonreference, github.com/xeipuuv/gojsonschema, go.uber.org/multierr, go.uber.org/zap, go.yaml.in/yaml/v2, go.yaml.in/yaml/v3, golang.org/x/crypto, golang.org/x/mod, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sync, golang.org/x/sys, golang.org/x/term, golang.org/x/text, golang.org/x/time, golang.org/x/tools, gomodules.xyz/jsonpatch/v2, google.golang.org/protobuf, gopkg.in/evanphx/json-patch.v4, gopkg.in/inf.v0, k8s.io/api, k8s.io/apiextensions-apiserver, k8s.io/apimachinery, k8s.io/client-go, k8s.io/klog/v2, k8s.io/kube-openapi, k8s.io/utils
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: main.go, pkg/gqlschema/labels.go, pkg/gqlschema/models_gen.go, pkg/gqlschema/schema_gen.go

## Setup and usage

- Usage: Compass Manager watches for Kyma custom resource changes. When Kyma with the Application Connector module is created, it registers Kyma runtime in the Compass Director and creates a Compass Manager Mapping with the ID assigned by the Compass Director.
- Usage: It then configures the Compass runtime Secret on the client cluster.
- Usage: apiVersion: operator.kyma-project.io/v1beta2
- Usage: name: 54572f7a-b2c2-4f09-b83e-1c9f9b690e02
- Usage: namespace: kcp-system
- Usage: kyma-project.io/broker-plan-name: open
- Usage: kyma-project.io/broker-plan-id: 925c16be-3644-457b-840b-768f69b993cf
- Usage: kyma-project.io/instance-id: 1ccf9b07-1296-4052-97b5-1c38aa72ac41

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/kyma-project/compass-manager/blob/main/README.md
- README SHA: 9f4ca5fd8dfb5d91a8f870039a74b5672ee27ce9
- Manifests: Dockerfile, go.mod, Makefile
- Sampled source files: main.go, pkg/gqlschema/labels.go, pkg/gqlschema/models_gen.go, pkg/gqlschema/schema_gen.go
- Git tree state: captured
- Evidence fingerprint: 2ec7d618a0227ed23cddcc0ca932310a8398986c794f938d3cc50dff7dc67cb1

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
