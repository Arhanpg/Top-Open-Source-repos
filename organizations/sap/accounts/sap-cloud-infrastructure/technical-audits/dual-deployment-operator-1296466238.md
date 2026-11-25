# SAP-cloud-infrastructure/dual-deployment-operator

- Company: SAP
- Account: SAP-cloud-infrastructure
- Repository: https://github.com/SAP-cloud-infrastructure/dual-deployment-operator
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:51:32+00:00

## Project purpose

A Kubernetes operator for **Gardener** environments that deploys a single Helm chart or kustomize source across **two clusters at once** — the seed (in-cluster) and its shoot (remote) — from one DualDeploymentOperator custom resource.

## Why this project is used

Kubernetes operator that deploys split host/remote helm chart/kustomization in Gardener environments, rendering a Helm chart or kustomize source per operator and applying each half to its target cluster via server-side apply.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Makefile, Dockerfile, Shell, Go Template, Nix
- Frameworks/libraries: Unknown / not established
- Dependency names: cel.dev/expr, dario.cat/mergo, github.com/Azure/go-ansiterm, github.com/BurntSushi/toml, github.com/MakeNowJust/heredoc, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/Masterminds/squirrel, github.com/Microsoft/go-winio, github.com/ProtonMail/go-crypto, github.com/antlr4-go/antlr/v4, github.com/asaskevich/govalidator, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cenkalti/backoff/v5, github.com/cespare/xxhash/v2, github.com/chai2010/gettext-go, github.com/cloudflare/circl, github.com/cyphar/filepath-securejoin, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/emirpasic/gods, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/exponent-io/jsonpath, github.com/fatih/color, github.com/felixge/httpsnoop, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-errors/errors, github.com/go-git/gcfg, github.com/go-git/go-billy/v5, github.com/go-git/go-git/v5, github.com/go-gorp/gorp/v3, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-task/slim-sprig/v3, github.com/gobwas/glob, github.com/golang/groupcache, github.com/google/btree, github.com/google/cel-go, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/pprof, github.com/google/uuid, github.com/gosuri/uitable, github.com/grpc-ecosystem/grpc-gateway/v2, github.com/hashicorp/errwrap, github.com/hashicorp/go-multierror, github.com/hashicorp/golang-lru/v2, github.com/huandu/xstrings, github.com/inconshreveable/mousetrap, github.com/jbenet/go-context, github.com/jmoiron/sqlx, github.com/josharian/intern, github.com/json-iterator/go, github.com/kevinburke/ssh_config, github.com/klauspost/cpuid/v2, github.com/lann/builder, github.com/lann/ps, github.com/lib/pq, github.com/liggitt/tabwriter, github.com/mailru/easyjson, github.com/mattn/go-colorable, github.com/mattn/go-isatty, github.com/mattn/go-runewidth, github.com/mitchellh/copystructure, github.com/mitchellh/go-wordwrap, github.com/mitchellh/reflectwalk, github.com/moby/term, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/monochromegane/go-gitignore, github.com/munnerz/goautoneg, github.com/onsi/ginkgo/v2, github.com/onsi/gomega, github.com/opencontainers/go-digest, github.com/opencontainers/image-spec, github.com/peterbourgon/diskv, github.com/pjbgf/sha1cd, github.com/pkg/errors, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/rubenv/sql-migrate, github.com/russross/blackfriday/v2, github.com/santhosh-tekuri/jsonschema/v6, github.com/sergi/go-diff, github.com/shopspring/decimal, github.com/skeema/knownhosts, github.com/spf13/cast, github.com/spf13/cobra, github.com/spf13/pflag
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/main.go, cmd/main_test.go, .devcontainer/post-install.sh, api/v1alpha1/dualdeploymentoperator_types.go

## Setup and usage

- Usage: Create a DualDeploymentOperator CR describing your source, the shoot namespace, and how to

## Limitations and caveats

- Security / Disclosure: If you find a bug that may be a security problem, please follow the instructions in our
- Security / Disclosure: Please do not open GitHub issues for security-related concerns.

## Evidence and provenance

- README: https://github.com/SAP-cloud-infrastructure/dual-deployment-operator/blob/main/README.md
- README SHA: b11f8c999fd87e2f9a9ef1ec0898736f7bc14dd4
- Manifests: Dockerfile, go.mod, Makefile
- Sampled source files: cmd/main.go, cmd/main_test.go, .devcontainer/post-install.sh, api/v1alpha1/dualdeploymentoperator_types.go
- Git tree state: captured
- Evidence fingerprint: c09a2ea9f26cea1e907f49af2cc0de2a92eea26cd4e4fd799b3c2235cbedc5d7

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
