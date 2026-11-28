# kyma-project/eventing-manager

- Company: SAP
- Account: kyma-project
- Repository: https://github.com/kyma-project/eventing-manager
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:53:53+00:00

## Project purpose

Eventing Manager is a standard Kubernetes operator that observes the state of Eventing resources and reconciles their state according to the desired state. It uses Controllers, which provide a reconcile function responsible for synchronizing resources until the desired state is reached in the cluster.

## Why this project is used

Eventing Operator installs Eventing as Kyma module

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Shell, Makefile, Dockerfile, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/antithesishq/antithesis-sdk-go, github.com/avast/retry-go/v3, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cespare/xxhash/v2, github.com/chigopher/pathlib, github.com/cloudevents/sdk-go/protocol/nats/v2, github.com/cloudevents/sdk-go/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/gogo/protobuf, github.com/golang/protobuf, github.com/google/btree, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/go-tpm, github.com/google/uuid, github.com/gorilla/mux, github.com/hashicorp/hcl, github.com/huandu/xstrings, github.com/iancoleman/strcase, github.com/inconshreveable/mousetrap, github.com/jinzhu/copier, github.com/josharian/intern, github.com/json-iterator/go, github.com/kelseyhightower/envconfig, github.com/klauspost/compress, github.com/kyma-project/api-gateway, github.com/kyma-project/kyma/common/logging, github.com/kyma-project/nats-manager, github.com/magiconair/properties, github.com/mailru/easyjson, github.com/mattn/go-colorable, github.com/mattn/go-isatty, github.com/minio/highwayhash, github.com/mitchellh/go-homedir, github.com/mitchellh/hashstructure/v2, github.com/mitchellh/mapstructure, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/nats-io/jwt/v2, github.com/nats-io/nats-server/v2, github.com/nats-io/nats.go, github.com/nats-io/nkeys, github.com/nats-io/nuid, github.com/nxadm/tail, github.com/onsi/ginkgo, github.com/onsi/gomega, github.com/pelletier/go-toml/v2, github.com/pkg/errors, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/rs/zerolog, github.com/sagikazarmark/locafero, github.com/sagikazarmark/slog-shim, github.com/sourcegraph/conc, github.com/spf13/afero, github.com/spf13/cast, github.com/spf13/cobra, github.com/spf13/pflag, github.com/spf13/viper, github.com/stretchr/objx, github.com/stretchr/testify, github.com/subosito/gotenv, github.com/thoas/go-funk, github.com/vektra/mockery/v2, github.com/x448/float16, go.uber.org/atomic, go.uber.org/multierr, go.uber.org/zap, go.yaml.in/yaml/v2, go.yaml.in/yaml/v3, golang.org/x/crypto, golang.org/x/exp, golang.org/x/mod, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sync, golang.org/x/sys, golang.org/x/term, golang.org/x/text, golang.org/x/time, golang.org/x/tools, golang.org/x/xerrors, gomodules.xyz/jsonpatch/v2, google.golang.org/genproto/googleapis/api, google.golang.org/protobuf, gopkg.in/evanphx/json-patch.v4, gopkg.in/inf.v0
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/main.go, hack/e2e/sink/cmd/main.go, cmd/main_test.go, pkg/backend/cleaner/eventmesh.go

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/kyma-project/eventing-manager/blob/main/README.md
- README SHA: 382b76d7a3fd7cb9b046aaab14647f67ad4d261d
- Manifests: Dockerfile, go.mod, Makefile, hack/ci/Makefile, hack/e2e/sink/Dockerfile, hack/e2e/sink/go.mod
- Sampled source files: cmd/main.go, hack/e2e/sink/cmd/main.go, cmd/main_test.go, pkg/backend/cleaner/eventmesh.go
- Git tree state: captured
- Evidence fingerprint: 529bc88dd710b3f230d71810f24feeb3954ffbdf84cd1ef478c565a5c783e82d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
