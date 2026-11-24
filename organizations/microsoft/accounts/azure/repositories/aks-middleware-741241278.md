# Azure/aks-middleware

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/aks-middleware](https://github.com/Azure/aks-middleware)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/aks-middleware/blob/main/README.md)
- README blob SHA: 141344891cdffb0be58ad070dccc96e58ad6ba62
- README bytes captured: 19237
- README truncated at capture limit: False
- Repository ID: 741241278
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Public facing middleware for Service Hub

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T22:45:49+00:00

### Short excerpt (up to 300 words)

> Run the following command

### README headings

- AKS middleware for Go
- 1. <a id='Usage'></a>Usage
- 2. <a id='gRPCserver'></a>gRPC server
- 2.1. <a id='requestid'></a>requestid
- 2.2. <a id='ctxloggerapplogger'></a>ctxlogger (applogger)
- <a id='logfiltering'></a>log filtering
- 2.3. <a id='autologgerapirequestresponselogger'></a>autologger (api request/response logger)
- 2.4. <a id='recovery'></a>recovery
- 2.5. <a id='protovalidate'></a>protovalidate
- 2.6. <a id='responseheader'></a>responseheader
- 3. <a id='gRPCclient'></a>gRPC client
- 3.1. <a id='mdforward'></a>mdforward
- 3.2. <a id='autologgerapirequestresponselogger-1'></a>autologger (api request/response logger)
- 3.3. <a id='retry'></a>retry
- 4. <a id='HTTPserver'></a>HTTP server
- 4.1. <a id='requestid-1'></a>requestid
- 4.2. <a id='loggingapirequestresponselogger'></a>logging (api request/response logger)
- <a id='Usage-1'></a>Usage
- 4.3. <a id='httpctxlogger'></a>ctx logging (applogging)
- <a id='Usage-1'></a>Usage
- 4.4. <a id='recovery-1'></a>recovery
- <a id='Usage-1'></a>Usage
- 4.5. <a id='inputvalidate'></a>inputvalidate
- 4.6. <a id='operationrequest'></a>operationrequest
- <a id='Usage-2'></a>Usage
- 4.7 <a id='otelauditlogging'></a>OTel Audit Logging
- 5. <a id='HTTPclientviaAzureSDK'></a>HTTP client via Azure SDK
- 5.1. <a id='mdforward-1'></a>mdforward
- 5.2. <a id='policyapirequestresponselogger'></a>policy (api request/response logger)
- <a id='Usage-1'></a>Usage

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: 1. <a id='Usage'></a>Usage

> Run the following command

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 139,786 |
| Makefile | 237 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go, buf.build/gen/go/service-hub/loggable/protocolbuffers/go, buf.build/go/protovalidate, cel.dev/expr, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/Azure/retry, github.com/antlr4-go/antlr/v4, github.com/go-json-experiment/json, github.com/go-logr/logr, github.com/go-task/slim-sprig, github.com/gofrs/uuid, github.com/golang/protobuf, github.com/google/cel-go, github.com/google/go-cmp, github.com/google/pprof, github.com/gorilla/mux, github.com/grpc-ecosystem/go-grpc-middleware/v2, github.com/grpc-ecosystem/grpc-gateway/v2, github.com/jedib0t/go-pretty/v6
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 5
- Forks at capture: 9
- Last updated: 2026-09-30T17:10:06Z
- Last pushed: 2026-10-07T00:14:48Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/aks-middleware)
- [README](https://github.com/Azure/aks-middleware/blob/main/README.md)
- [Issues](https://github.com/Azure/aks-middleware/issues)
- [Releases](https://github.com/Azure/aks-middleware/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
