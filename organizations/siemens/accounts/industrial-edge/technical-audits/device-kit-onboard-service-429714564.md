# industrial-edge/device-kit-onboard-service

- Company: Siemens
- Account: industrial-edge
- Repository: https://github.com/industrial-edge/device-kit-onboard-service
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:54:40+00:00

## Project purpose

The IE Device Kit API provides the abstraction layer that decouples the Industrial Edge Runtime from the underlying Linux systems. This allows to adapt the runtime and its behavior to serve for the specific needs of different Industrial Edge products.

## Why this project is used

IE Device Kit API reference implementation for onboard service

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Makefile, Dockerfile, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/davecgh/go-spew, github.com/pmezard/go-difflib, github.com/stretchr/objx, github.com/stretchr/testify, golang.org/x/net, golang.org/x/sys, golang.org/x/text, google.golang.org/genproto/googleapis/rpc, google.golang.org/grpc, google.golang.org/protobuf, gopkg.in/yaml.v3
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/onboardservice/main.go, app/appfactory.go, app/capabilityparser.go, app/capabilityparser_test.go

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/industrial-edge/device-kit-onboard-service/blob/main/README.md
- README SHA: 574752dcf014babc84612e13a5b6ab6b02103e50
- Manifests: go.mod, build/package/Dockerfile, build/package/Makefile
- Sampled source files: cmd/onboardservice/main.go, app/appfactory.go, app/capabilityparser.go, app/capabilityparser_test.go
- Git tree state: captured
- Evidence fingerprint: 46b4be0a32ab409de988fef6b03b3660658e28c6147445ffad39cf1142ef371d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
