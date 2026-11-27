# kyma-project/docker-registry

- Company: SAP
- Account: kyma-project
- Repository: https://github.com/kyma-project/docker-registry
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:29:06+00:00

## Project purpose

The Docker Registry module provides a lightweight, open-source Docker registry for storing and distributing container images in the Kubernetes environment. You can use it in self-contained development clusters or testing environments, so you can test deployments in an isolated system.

## Why this project is used

The Docker Registry module provides a lightweight, open-source Docker registry for storing and distributing container images in the Kubernetes environment. You can use it in self-contained development clusters or testing environments, so you can test deployments in an isolated system.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Makefile, Shell, Mustache, JavaScript, Dockerfile, Go Template
- Frameworks/libraries: Unknown / not established
- Dependency names: dario.cat/mergo, github.com/Azure/go-ansiterm, github.com/BurntSushi/toml, github.com/MakeNowJust/heredoc, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/Masterminds/squirrel, github.com/asaskevich/govalidator, github.com/avast/retry-go, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cespare/xxhash/v2, github.com/chai2010/gettext-go, github.com/containerd/containerd, github.com/containerd/errdefs, github.com/containerd/log, github.com/containerd/platforms, github.com/cyphar/filepath-securejoin, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/exponent-io/jsonpath, github.com/fatih/color, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-errors/errors, github.com/go-gorp/gorp/v3, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonname, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading, github.com/go-openapi/swag/mangling, github.com/go-openapi/swag/netutils, github.com/go-openapi/swag/stringutils, github.com/go-openapi/swag/typeutils, github.com/go-openapi/swag/yamlutils, github.com/go-task/slim-sprig/v3, github.com/gobwas/glob, github.com/golang/protobuf, github.com/google/btree, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/pprof, github.com/google/uuid, github.com/gorilla/websocket, github.com/gosuri/uitable, github.com/gregjones/httpcache, github.com/hashicorp/errwrap, github.com/hashicorp/go-multierror, github.com/huandu/xstrings, github.com/inconshreveable/mousetrap, github.com/jmoiron/sqlx, github.com/json-iterator/go, github.com/klauspost/compress, github.com/kyma-project/manager-toolkit/installation/base, github.com/kyma-project/manager-toolkit/installation/chart, github.com/kyma-project/manager-toolkit/logging, github.com/lann/builder, github.com/lann/ps, github.com/lib/pq, github.com/liggitt/tabwriter, github.com/mattn/go-colorable, github.com/mattn/go-isatty, github.com/mattn/go-runewidth, github.com/mitchellh/copystructure, github.com/mitchellh/go-wordwrap, github.com/mitchellh/reflectwalk, github.com/moby/spdystream, github.com/moby/term, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/monochromegane/go-gitignore, github.com/munnerz/goautoneg, github.com/mxk/go-flowrate, github.com/onsi/ginkgo/v2, github.com/onsi/gomega, github.com/opencontainers/go-digest, github.com/opencontainers/image-spec, github.com/peterbourgon/diskv, github.com/pkg/errors, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/rubenv/sql-migrate, github.com/russross/blackfriday/v2, github.com/santhosh-tekuri/jsonschema/v6, github.com/shopspring/decimal, github.com/sirupsen/logrus, github.com/spf13/cast
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: components/operator/main.go, .github/scripts/create-changelog.sh, .github/scripts/create-draft-release.sh, .github/scripts/publish-release.sh

## Setup and usage

- Usage: Having installed the Docker Registry module, you can start pushing images to it using Kyma CLI (v3) or, if you decide to expose the registry externally, using Docker CLI.
- Usage: For details, see the following tutorials:
- Usage: * Use Registry Internally
- Installation in the k3d Cluster Using Make Targets: 1. Clone the project.
- Installation in the k3d Cluster Using Make Targets: git clone https://github.com/kyma-project/docker-registry.git && cd docker-registry/
- Installation in the k3d Cluster Using Make Targets: 2. Build Docker Registry Operator locally and run it in the k3d cluster.
- Installation in the k3d Cluster Using Make Targets: > **NOTE:** To clean up the k3d cluster, use the make delete-k3d make target.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/kyma-project/docker-registry/blob/main/README.md
- README SHA: 66e907c01ecdea2cc652df1fa6e23a286d3a3295
- Manifests: go.mod, Makefile, hack/Makefile, components/operator/Dockerfile, components/operator/Makefile, components/registry-init/Dockerfile
- Sampled source files: components/operator/main.go, .github/scripts/create-changelog.sh, .github/scripts/create-draft-release.sh, .github/scripts/publish-release.sh
- Git tree state: captured
- Evidence fingerprint: 91be7f61e0e15e9c5d4eb954f26fea5134394dcae8230605e4e54f9054449ae3

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
