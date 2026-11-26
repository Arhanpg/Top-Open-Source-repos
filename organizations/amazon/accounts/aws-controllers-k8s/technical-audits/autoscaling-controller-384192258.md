# aws-controllers-k8s/autoscaling-controller

- Company: Amazon
- Account: aws-controllers-k8s
- Repository: https://github.com/aws-controllers-k8s/autoscaling-controller
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:12:45+00:00

## Project purpose

This repository contains source code for the AWS Controllers for Kubernetes (ACK) service controller for Amazon EC2 Auto Scaling.

## Why this project is used

This repository contains source code for the AWS Controllers for Kubernetes (ACK) service controller for Amazon EC2 Auto Scaling.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Go Template, Go, Makefile, Smarty
- Frameworks/libraries: Unknown / not established
- Dependency names: acktest, github.com/aws-controllers-k8s/ec2-controller, github.com/aws-controllers-k8s/elbv2-controller, github.com/aws-controllers-k8s/iam-controller, github.com/aws-controllers-k8s/runtime, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/autoscaling, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/beorn7/perks, github.com/cenkalti/backoff/v4, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/google/btree, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/uuid, github.com/itchyny/gojq, github.com/itchyny/timefmt-go, github.com/jaypipes/envutil, github.com/josharian/intern, github.com/json-iterator/go, github.com/mailru/easyjson, github.com/micahhausler/aws-iam-policy, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/pkg/errors, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/spf13/pflag, github.com/x448/float16, go.uber.org/multierr, go.uber.org/zap, go.yaml.in/yaml/v2, go.yaml.in/yaml/v3, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sync, golang.org/x/sys, golang.org/x/term, golang.org/x/text, golang.org/x/time, gomodules.xyz/jsonpatch/v2, google.golang.org/protobuf, gopkg.in/evanphx/json-patch.v4, gopkg.in/inf.v0, gopkg.in/yaml.v3, k8s.io/api, k8s.io/apiextensions-apiserver, k8s.io/apimachinery, k8s.io/client-go, k8s.io/klog/v2, k8s.io/kube-openapi, k8s.io/utils, sigs.k8s.io/controller-runtime, sigs.k8s.io/json, sigs.k8s.io/randfill, sigs.k8s.io/structured-merge-diff/v6, sigs.k8s.io/yaml
- Build/package tools: Go module manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/controller/main.go, pkg/resource/auto_scaling_group/delta.go, pkg/resource/auto_scaling_group/descriptor.go, pkg/resource/auto_scaling_group/hooks.go

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-controllers-k8s/autoscaling-controller/blob/main/README.md
- README SHA: b4092cc694c9b998429841e7885e35de8e192593
- Manifests: go.mod, Makefile, test/e2e/requirements.txt
- Sampled source files: cmd/controller/main.go, pkg/resource/auto_scaling_group/delta.go, pkg/resource/auto_scaling_group/descriptor.go, pkg/resource/auto_scaling_group/hooks.go
- Git tree state: captured
- Evidence fingerprint: e7a9ae6f2e45fdc69690d9da8fb86ac84db41411638dfb12f2068d4d8847a8e8

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
