# industrial-edge/device-kit-network-service

- Company: Siemens
- Account: industrial-edge
- Repository: https://github.com/industrial-edge/device-kit-network-service
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:36:17+00:00

## Project purpose

The IE Device Kit API provides the abstraction layer that decouples the Industrial Edge Runtime from the underlying Linux systems. This allows to adapt the runtime and its behavior to serve for the specific needs of different Industrial Edge products.

## Why this project is used

IE Device Kit API reference implementation for network service

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Makefile, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/Wifx/gonetworkmanager/v2, github.com/agiledragon/gomonkey/v2, github.com/davecgh/go-spew, github.com/godbus/dbus/v5, github.com/google/go-cmp, github.com/google/uuid, github.com/maltegrosse/go-modemmanager, github.com/pmezard/go-difflib, github.com/stretchr/objx, github.com/stretchr/testify, golang.org/x/net, golang.org/x/sys, golang.org/x/text, google.golang.org/genproto/googleapis/rpc, google.golang.org/grpc, google.golang.org/protobuf, gopkg.in/yaml.v3
- Build/package tools: Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/networkservice/main.go, app/networkservice.go, app/util.go, api/siemens_iedge_dmapi_v1/Network.pb.go

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/industrial-edge/device-kit-network-service/blob/main/README.md
- README SHA: 78da366e875e4ceebb0234e7ad0141a7ddc1888b
- Manifests: go.mod, build/package/Makefile
- Sampled source files: cmd/networkservice/main.go, app/networkservice.go, app/util.go, api/siemens_iedge_dmapi_v1/Network.pb.go
- Git tree state: captured
- Evidence fingerprint: e8900b74883b9943018015953e50f03b2010c9f763f435439d77fc047527ce8c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
