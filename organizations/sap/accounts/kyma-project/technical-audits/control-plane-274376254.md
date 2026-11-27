# kyma-project/control-plane

- Company: SAP
- Account: kyma-project
- Repository: https://github.com/kyma-project/control-plane
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:09:45+00:00

## Project purpose

This repository has been deprecated and archived on Feb 11th, 2025. For available replacements, see the following:

## Why this project is used

A flexible and easy way to manage Kyma Runtimes

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Shell, Makefile, Mustache, PLpgSQL, Dockerfile, Smarty
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/99designs/gqlgen, github.com/Azure/go-ansiterm, github.com/Masterminds/semver, github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/agnivade/levenshtein, github.com/avast/retry-go, github.com/beorn7/perks, github.com/cenkalti/backoff/v4, github.com/cespare/xxhash/v2, github.com/containerd/cgroups, github.com/containerd/containerd, github.com/cpuguy83/go-md2man/v2, github.com/davecgh/go-spew, github.com/deepmap/oapi-codegen, github.com/docker/distribution, github.com/docker/docker, github.com/docker/go-connections, github.com/docker/go-units, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/gardener/gardener, github.com/go-logr/logr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/gocraft/dbr/v2, github.com/gogo/protobuf, github.com/golang/groupcache, github.com/golang/mock, github.com/golang/protobuf, github.com/google/gnostic, github.com/google/go-cmp, github.com/google/gofuzz, github.com/google/uuid, github.com/gorilla/mux, github.com/gorilla/websocket, github.com/hashicorp/errwrap, github.com/hashicorp/go-multierror, github.com/hashicorp/go-version, github.com/hashicorp/golang-lru/v2, github.com/imdario/mergo, github.com/josharian/intern, github.com/json-iterator/go, github.com/kyma-incubator/compass/components/director, github.com/lib/pq, github.com/machinebox/graphql, github.com/magiconair/properties, github.com/mailru/easyjson, github.com/matryer/is, github.com/matttproud/golang_protobuf_extensions, github.com/mitchellh/mapstructure, github.com/moby/sys/mount, github.com/moby/sys/mountinfo, github.com/moby/term, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/morikuni/aec, github.com/munnerz/goautoneg, github.com/onrik/logrus, github.com/opencontainers/go-digest, github.com/opencontainers/image-spec, github.com/opencontainers/runc, github.com/pkg/errors, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/russross/blackfriday/v2, github.com/sirupsen/logrus, github.com/sosodev/duration, github.com/spf13/pflag, github.com/stretchr/objx, github.com/stretchr/testify, github.com/testcontainers/testcontainers-go, github.com/urfave/cli/v2, github.com/vektah/gqlparser/v2, github.com/vrischmann/envconfig, github.com/xrash/smetrics, go.opencensus.io, golang.org/x/mod, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sync, golang.org/x/sys, golang.org/x/term, golang.org/x/text, golang.org/x/time, golang.org/x/tools, gomodules.xyz/jsonpatch/v2, google.golang.org/appengine, google.golang.org/genproto/googleapis/rpc, google.golang.org/grpc, google.golang.org/protobuf, gopkg.in/inf.v0, gopkg.in/yaml.v2, gopkg.in/yaml.v3, gotest.tools, k8s.io/api
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: components/provisioner/cmd/main.go, components/schema-migrator/main.go, components/provisioner/cmd/init.go, components/provisioner/pkg/gqlschema/labels.go

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/kyma-project/control-plane/blob/main/README.md
- README SHA: 4b569154646f8111167b539a03173da9c938c0b9
- Manifests: components/provisioner/Dockerfile, components/provisioner/go.mod, components/provisioner/Makefile, components/reconciler/go.mod, components/reconciler/makefile, components/schema-migrator/Dockerfile
- Sampled source files: components/provisioner/cmd/main.go, components/schema-migrator/main.go, components/provisioner/cmd/init.go, components/provisioner/pkg/gqlschema/labels.go
- Git tree state: captured
- Evidence fingerprint: 6d580380ba80ec413c4b9fbef7e486f03594ffbcf3d81d95c3cf08f440604691

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
