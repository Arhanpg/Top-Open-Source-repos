# SAP-cloud-infrastructure/webhook-injector

- Company: SAP
- Account: SAP-cloud-infrastructure
- Repository: https://github.com/SAP-cloud-infrastructure/webhook-injector
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:22:50+00:00

## Project purpose

SPDX-FileCopyrightText: 2026 SAP SE or an SAP affiliate company

## Why this project is used

A Kubernetes controller that runs as a sidecar to webhook servers, managing the lifecycle of webhook configurations and TLS certificates for remote or local clusters.

## Core features

- **Automatic Certificate Management**: Generates and rotates self-signed certificates with dynamic SANs.: **Automatic Certificate Management**: Generates and rotates self-signed certificates with dynamic SANs.
  - Evidence: README.md#Features
- **Smart Rotation**: Time-based (20% remaining validity threshold), config-based (SAN changes), or manual (annotation).: **Smart Rotation**: Time-based (20% remaining validity threshold), config-based (SAN changes), or manual (annotation).
  - Evidence: README.md#Features
- **Remote Cluster Support**: Manage webhooks in clusters where the webhook server doesn't run.: **Remote Cluster Support**: Manage webhooks in clusters where the webhook server doesn't run.
  - Evidence: README.md#Features
- **Language Agnostic**: Works with any webhook server that can watch certificate files for changes.: **Language Agnostic**: Works with any webhook server that can watch certificate files for changes.
  - Evidence: README.md#Features
- **High Availability**: Leader election with multi-replica support, zero-downtime rotation.: **High Availability**: Leader election with multi-replica support, zero-downtime rotation.
  - Evidence: README.md#Features
- **Zero-downtime certificate rotation**: staged overlap — both old and new certs trusted on the target cluster before the new one is served, then the old cert is: **Zero-downtime certificate rotation**: staged overlap — both old and new certs trusted on the target cluster before the new one is served, then the old cert is pruned after a configurable grace window.
  - Evidence: README.md#Features
- **Gardener Seed Support**: Stamps CRDs at the source — inside Gardener ManagedResource Secrets on the seed — so the stamp survives gardener-resource-manager's n: **Gardener Seed Support**: Stamps CRDs at the source — inside Gardener ManagedResource Secrets on the seed — so the stamp survives gardener-resource-manager's next sync into the shoot.
  - Evidence: README.md#Features

## Technology stack

- Languages: Go, Makefile, Shell, Dockerfile, Nix
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/andybalholm/brotli, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/gardener/gardener/pkg/apis, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/google/btree, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/uuid, github.com/josharian/intern, github.com/json-iterator/go, github.com/mailru/easyjson, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/spf13/pflag, github.com/x448/float16, go.uber.org/multierr, go.uber.org/zap, go.yaml.in/yaml/v2, go.yaml.in/yaml/v3, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sync, golang.org/x/sys, golang.org/x/term, golang.org/x/text, golang.org/x/time, gomodules.xyz/jsonpatch/v2, google.golang.org/protobuf, gopkg.in/evanphx/json-patch.v4, gopkg.in/inf.v0, gopkg.in/yaml.v3, k8s.io/api, k8s.io/apiextensions-apiserver, k8s.io/apimachinery, k8s.io/client-go, k8s.io/klog/v2, k8s.io/kube-openapi, k8s.io/utils, sigs.k8s.io/controller-runtime, sigs.k8s.io/json, sigs.k8s.io/randfill, sigs.k8s.io/structured-merge-diff/v6, sigs.k8s.io/yaml
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/webhook-injector/main.go, pkg/certificates/bundle.go, pkg/certificates/bundle_test.go, pkg/certificates/generator.go

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/SAP-cloud-infrastructure/webhook-injector/blob/main/README.md
- README SHA: d84d08ea5f41ab5de7428a796b4b6e3492917797
- Manifests: Dockerfile, go.mod, Makefile
- Sampled source files: cmd/webhook-injector/main.go, pkg/certificates/bundle.go, pkg/certificates/bundle_test.go, pkg/certificates/generator.go
- Git tree state: captured
- Evidence fingerprint: bb6f0588ac3bf56d385fc255889c742bd0c21f012abd3b7b21916d9f53519eea

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
