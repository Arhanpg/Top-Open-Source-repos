# kyma-project/btp-manager

- Company: SAP
- Account: kyma-project
- Repository: https://github.com/kyma-project/btp-manager
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:57:38+00:00

## Project purpose

BTP Manager is an operator for the SAP BTP service operator based on the Kubebuilder framework. It extends Kubernetes API by providing BtpOperator CustomResourceDefinition (CRD), which allows you to manage the SAP BTP service operator resource through custom resource (CR). BTP Manager and the SAP BTP service operator constitute the SAP BTP Operator module.

## Why this project is used

BTP Manager installs SAP BTP Service Operator as a Kyma module

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Shell, JavaScript, Makefile, Python, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/Masterminds/semver/v3, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading, github.com/go-openapi/swag/mangling, github.com/go-openapi/swag/netutils, github.com/go-openapi/swag/pools, github.com/go-openapi/swag/stringutils, github.com/go-openapi/swag/typeutils, github.com/go-openapi/swag/yamlutils, github.com/go-task/slim-sprig/v3, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/pprof, github.com/google/uuid, github.com/json-iterator/go, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/onsi/ginkgo/v2, github.com/onsi/gomega, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/spf13/pflag, github.com/stretchr/testify, github.com/x448/float16, go.uber.org/multierr, go.uber.org/zap, go.yaml.in/yaml/v2, go.yaml.in/yaml/v3, golang.org/x/mod, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sync, golang.org/x/sys, golang.org/x/term, golang.org/x/text, golang.org/x/time, golang.org/x/tools, gomodules.xyz/jsonpatch/v2, google.golang.org/protobuf, gopkg.in/evanphx/json-patch.v4, gopkg.in/inf.v0, gopkg.in/yaml.v3, k8s.io/api, k8s.io/apiextensions-apiserver, k8s.io/apimachinery, k8s.io/client-go, k8s.io/klog/v2, k8s.io/kube-openapi, k8s.io/utils, pyyaml, requests, sigs.k8s.io/controller-runtime, sigs.k8s.io/json, sigs.k8s.io/randfill, sigs.k8s.io/structured-merge-diff/v6, sigs.k8s.io/yaml
- Build/package tools: Docker build configuration, Go module manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/autodoc/main.go, main.go, api/v1alpha1/btpoperator_types.go, api/v1alpha1/groupversion_info.go

## Setup and usage

- Installation: To enable the SAP BTP Operator module from the latest release, you must install BTP Manager. For installation instructions, see Install the SAP BTP Operator module.
- Usage: Use SAP BTP Operator to create SAP BTP services in your Kyma cluster. To find out how to do it, see the tutorial Create an SAP BTP Service Instance in Your Kyma Cluster.
- Uninstallation: To uninstall SAP BTP Operator, run the following commands:
- Uninstallation: kubectl delete -f https://github.com/kyma-project/btp-manager/releases/latest/download/btp-operator.yaml
- Uninstallation: kubectl delete -f https://github.com/kyma-project/btp-manager/releases/latest/download/btp-manager.yaml

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/kyma-project/btp-manager/blob/main/README.md
- README SHA: 940ef642df2b689e9a4c149750b248277abd8064
- Manifests: Dockerfile, go.mod, Makefile, scripts/python/requirements.txt, tests/fake-server/Dockerfile, tests/probe/Dockerfile
- Sampled source files: cmd/autodoc/main.go, main.go, api/v1alpha1/btpoperator_types.go, api/v1alpha1/groupversion_info.go
- Git tree state: captured
- Evidence fingerprint: 1004bbd340ee122388f89f68f7ea61fa1a57168ed440e4605eac2595cdab5c0b

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
