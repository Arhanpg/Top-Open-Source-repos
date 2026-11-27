# kyma-project/cp-mod-migrator

- Company: SAP
- Account: kyma-project
- Repository: https://github.com/kyma-project/cp-mod-migrator
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:16:33+00:00

## Project purpose

This repository contains the source code of components that are necessary to perform the migration from the legacy Kyma Connectivity Proxy component (currently in version 2.9.3) into the new Kyma Connectivity Proxy module.

## Why this project is used

This repository contains the source code of components that are necessary to perform the migration from the legacy Kyma Connectivity Proxy component (currently in version 2.9.3) into the new Kyma Connectivity Proxy module.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Shell, Makefile, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/go-logr/logr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-task/slim-sprig, github.com/gogo/protobuf, github.com/golang/protobuf, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/gofuzz, github.com/google/pprof, github.com/google/uuid, github.com/imdario/mergo, github.com/josharian/intern, github.com/json-iterator/go, github.com/mailru/easyjson, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/onsi/ginkgo/v2, github.com/onsi/gomega, github.com/pkg/errors, github.com/pmezard/go-difflib, github.com/spf13/pflag, github.com/stretchr/objx, github.com/stretchr/testify, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sys, golang.org/x/term, golang.org/x/text, golang.org/x/time, golang.org/x/tools, google.golang.org/appengine, google.golang.org/protobuf, gopkg.in/inf.v0, gopkg.in/yaml.v2, gopkg.in/yaml.v3, k8s.io/api, k8s.io/apiextensions-apiserver, k8s.io/apimachinery, k8s.io/client-go, k8s.io/klog/v2, k8s.io/kube-openapi, k8s.io/kubectl, k8s.io/utils, sigs.k8s.io/controller-runtime, sigs.k8s.io/json, sigs.k8s.io/structured-merge-diff/v4, sigs.k8s.io/yaml
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: main.go, pkg/cluster_status.go, pkg/cluster_status_test.go, pkg/cproxy/api/v211/type_http.go

## Setup and usage

- Restoring old installation: The goal is to restore the previous state of the Connectivity Proxy in case of any issues during the migration process.
- Restoring old installation: Check if the Connectivity Proxy Operator Pod is running. In such a case, disable the Connectivity Proxy module using Busola or by editing the Kyma resource. \
- Restoring old installation: Wait some time for the uninstallation of the Connectivity Proxy module. \
- Restoring old installation: After the Connectivity Proxy module is uninstalled, wait about one hour for the Kyma Control Plane to restore the legacy Connectivity Proxy objects on the cluster.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/kyma-project/cp-mod-migrator/blob/main/README.md
- README SHA: 1970d683be4fe5d6adb13213fa313a7799c9a650
- Manifests: Dockerfile, go.mod, Makefile, images/backup/Dockerfile, images/cleaner/Dockerfile
- Sampled source files: main.go, pkg/cluster_status.go, pkg/cluster_status_test.go, pkg/cproxy/api/v211/type_http.go
- Git tree state: captured
- Evidence fingerprint: 324a0d10bdb7dd1509dc808b7bd344b46da02c1a18a7398214306643e8aab225

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
