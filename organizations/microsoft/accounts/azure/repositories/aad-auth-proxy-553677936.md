# Azure/aad-auth-proxy

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/aad-auth-proxy](https://github.com/Azure/aad-auth-proxy)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/aad-auth-proxy/blob/main/README.md)
- README blob SHA: a53ad17f679d98c099dfa716779056d71342b06c
- Repository ID: 553677936
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Azure Active Directory authentication proxy is an http proxy that is design to add authentication information required to talk to Microsoft Azure services.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:23:25+00:00

### Short excerpt (up to 100 words)

> Azure Active Directory authentication proxy is an http proxy that is design to add authentication information required to talk to Microsoft Azure services. The proxy adds Authorization header to http requests based on its configuration. It can be used to add authentication information to the requests made by scripts, tools, applications not designed to work directly with Azure Active Directory. Some usage examples would be to allow Kubecost to read Prometheus metrics stored in Azure Managed Prometheus, ingest metrics via OTEL collector through Prometheus Remote Write exporter into Azure Monitor Workspace and others. Check release notes for link to publicly

### README headings

- Status
- Project
- Getting Started
- Telemetry
- Securing traffic
- Limitations

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 46,720 |
| Shell | 5,707 |
| Bicep | 2,534 |
| Go Template | 1,852 |
| Dockerfile | 500 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/Dockerfile (capture: captured)
- src/go.mod (capture: captured) — dependency clues: github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/cenkalti/backoff/v5, github.com/cespare/xxhash/v2, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/golang-jwt/jwt/v5, github.com/google/uuid, github.com/grpc-ecosystem/grpc-gateway/v2, github.com/kylelemons/godebug, github.com/pkg/browser, github.com/sirupsen/logrus, github.com/t-tomalak/logrus-easy-formatter, go.opentelemetry.io/auto/sdk, go.opentelemetry.io/otel, go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc, go.opentelemetry.io/otel/exporters/otlp/otlptrace, go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 19
- Forks at capture: 23
- Last updated: 2026-08-16T06:20:45Z
- Last pushed: 2026-09-17T22:41:17Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/aad-auth-proxy)
- [README](https://github.com/Azure/aad-auth-proxy/blob/main/README.md)
- [Issues](https://github.com/Azure/aad-auth-proxy/issues)
- [Releases](https://github.com/Azure/aad-auth-proxy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
