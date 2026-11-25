# firecracker-microvm/firecracker-containerd

- Company: Amazon
- Account: firecracker-microvm
- Repository: https://github.com/firecracker-microvm/firecracker-containerd
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:56:12+00:00

## Project purpose

---

## Why this project is used

firecracker-containerd enables containerd to manage containers as Firecracker microVMs

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Makefile, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: cyphar.com/go-pathrs, dario.cat/mergo, github.com/AdaLogics/go-fuzz-headers, github.com/AdamKorcz/go-118-fuzz-build, github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/StackExchange/wmi, github.com/asaskevich/govalidator, github.com/awslabs/tc-redirect-tap, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cespare/xxhash/v2, github.com/cilium/ebpf, github.com/containerd/cgroups, github.com/containerd/cgroups/v3, github.com/containerd/console, github.com/containerd/containerd, github.com/containerd/containerd/api, github.com/containerd/continuity, github.com/containerd/errdefs, github.com/containerd/fifo, github.com/containerd/go-cni, github.com/containerd/go-runc, github.com/containerd/imgcrypt, github.com/containerd/log, github.com/containerd/nri, github.com/containerd/platforms, github.com/containerd/ttrpc, github.com/containerd/typeurl, github.com/containerd/typeurl/v2, github.com/containernetworking/cni, github.com/containernetworking/plugins, github.com/containers/ocicrypt, github.com/coreos/go-systemd/v22, github.com/cpuguy83/go-md2man/v2, github.com/cyphar/filepath-securejoin, github.com/davecgh/go-spew, github.com/distribution/reference, github.com/docker/docker-credential-helpers, github.com/docker/go-events, github.com/docker/go-metrics, github.com/docker/go-units, github.com/emicklei/go-restful/v3, github.com/felixge/httpsnoop, github.com/firecracker-microvm/firecracker-go-sdk, github.com/fsnotify/fsnotify, github.com/go-jose/go-jose/v3, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-ole/go-ole, github.com/go-openapi/analysis, github.com/go-openapi/errors, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/loads, github.com/go-openapi/runtime, github.com/go-openapi/spec, github.com/go-openapi/strfmt, github.com/go-openapi/swag, github.com/go-openapi/validate, github.com/godbus/dbus/v5, github.com/gofrs/uuid, github.com/gogo/protobuf, github.com/golang/groupcache, github.com/golang/protobuf, github.com/google/go-cmp, github.com/google/gofuzz, github.com/google/uuid, github.com/grpc-ecosystem/go-grpc-middleware, github.com/grpc-ecosystem/go-grpc-prometheus, github.com/hashicorp/errwrap, github.com/hashicorp/go-multierror, github.com/intel/goresctrl, github.com/josharian/intern, github.com/json-iterator/go, github.com/klauspost/compress, github.com/mailru/easyjson, github.com/mdlayher/socket, github.com/mdlayher/vsock, github.com/miekg/dns, github.com/miekg/pkcs11, github.com/mitchellh/mapstructure, github.com/moby/locker, github.com/moby/spdystream, github.com/moby/sys/mountinfo, github.com/moby/sys/sequential, github.com/moby/sys/signal, github.com/moby/sys/symlink, github.com/moby/sys/user, github.com/moby/sys/userns, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/oklog/ulid, github.com/opencontainers/go-digest, github.com/opencontainers/image-spec, github.com/opencontainers/runc, github.com/opencontainers/runtime-spec, github.com/opencontainers/runtime-tools, github.com/opencontainers/selinux, github.com/opentracing/opentracing-go, github.com/pmezard/go-difflib, github.com/stretchr/testify, gopkg.in/yaml.v3
- Build/package tools: Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: firecracker-control/cmd/containerd/main.go, internal/cmd/test-bridged-tap/main.go, volume/cmd/volume-init/main.go, agent/main.go

## Setup and usage

- Usage: For detailed instructions on building and running
- Usage: firecracker-containerd, see the
- Usage: getting started guide and the

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/firecracker-microvm/firecracker-containerd/blob/main/README.md
- README SHA: 7141c0169851b797daf05d23f7fdbdb868f587fb
- Manifests: go.mod, Makefile, agent/Makefile, docker-credential-mmds/go.mod, docker-credential-mmds/Makefile, examples/Makefile
- Sampled source files: firecracker-control/cmd/containerd/main.go, internal/cmd/test-bridged-tap/main.go, volume/cmd/volume-init/main.go, agent/main.go
- Git tree state: captured
- Evidence fingerprint: beea21e27b0a9c2bfa5e89413e96a48f98f658c23024dcbe8ef72efcc4b2205c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
