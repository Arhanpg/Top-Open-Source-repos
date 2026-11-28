# aws-observability/aws-sigv4-proxy-admission-controller

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-sigv4-proxy-admission-controller
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:03:03+00:00

## Project purpose

The mutation admission controller will inject the AWS SIGv4 Proxy as a sidecar into a pod if there are annotations specified in a container's deployment.yaml file or specific namespace labels.

## Why this project is used

This project creates a mutation admission controller that injects AWS SIGv4 proxy as a sidecar.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Dockerfile, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/go-logr/logr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/gogo/protobuf, github.com/golang/protobuf, github.com/google/gnostic-models, github.com/google/gofuzz, github.com/google/uuid, github.com/josharian/intern, github.com/json-iterator/go, github.com/mailru/easyjson, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/pmezard/go-difflib, github.com/stretchr/objx, github.com/stretchr/testify, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sys, golang.org/x/term, golang.org/x/text, golang.org/x/time, google.golang.org/appengine, google.golang.org/protobuf, gopkg.in/inf.v0, gopkg.in/yaml.v2, gopkg.in/yaml.v3, k8s.io/api, k8s.io/apimachinery, k8s.io/client-go, k8s.io/klog/v2, k8s.io/kube-openapi, k8s.io/utils, sigs.k8s.io/json, sigs.k8s.io/structured-merge-diff/v4, sigs.k8s.io/yaml
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: main.go, controller/mocks/KubernetesNamespaceClient.go, controller/webhook.go, controller/webhook_test.go

## Setup and usage

- Getting Started: A helm chart exists to deploy all the resources needed to use the admission controller here: https://github.com/aws/eks-charts/tree/master/stable/aws-sigv4-proxy-admission-controller/.

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-sigv4-proxy-admission-controller/blob/master/README.md
- README SHA: 79ef33012a76add63d8fbc7905a2a0528926ad4e
- Manifests: Dockerfile, go.mod, Makefile
- Sampled source files: main.go, controller/mocks/KubernetesNamespaceClient.go, controller/webhook.go, controller/webhook_test.go
- Git tree state: captured
- Evidence fingerprint: 56f56c69a763f3a251e2b920c169175bcb30743f7b34a2edc930df7c8ab773ac

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
