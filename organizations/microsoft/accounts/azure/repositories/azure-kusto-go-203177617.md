# Azure/azure-kusto-go

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/azure-kusto-go](https://github.com/Azure/azure-kusto-go)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/azure-kusto-go/blob/master/README.md)
- README blob SHA: 7a412905741ab95445195a5e197d480c0f05efad
- README bytes captured: 20195
- README truncated at capture limit: False
- Repository ID: 203177617
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Azure Data Explorer (Kusto) SDK for Go

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T03:47:30+00:00

### Short excerpt (up to 300 words)

> Install the Kusto/Azure Data Go, version 1.22 or

### README headings

- Microsoft Azure Data Explorer (Kusto) [![GoDoc](https://godoc.org/github.com/Azure/azure-kusto-go?status.svg)](https://pkg.go.dev/github.com/Azure/azure-kusto-go/azkustodata) [![GoDoc](https://godoc.org/github.com/Azure/azure-kusto-go?status.svg)](https://pkg.go.dev/github.com/Azure/azure-kusto-go/azkustoingest)
- Version 1.0.0-preview Released (BREAKING CHANGES)
- Intro
- Key concepts
- Getting started
- Install the package
- Prerequisites
- Azure Pipelines validation
- Examples
- Create the connection string
- Create and authenticate the client
- Using the `DefaultAzureCredential`
- Using the `az cli`
- Using a system-assigned managed identity
- Using a user-assigned managed identity
- Using a k8s workload identity
- Using a bearer token
- Using an app id and secret
- Using an application certificate
- Querying
- Simple queries
- Queries with parameters
- Queries with inline parameters
- Query For Rows
- Query Into Structs
- Ingestion
- Creating a queued ingestion client
- Ingestion From a File
- Ingestion From a Blob Storage File
- Ingestion from an io.Reader

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install the package

> Install the Kusto/Azure Data

### Technology and requirements: Prerequisites

> Go, version 1.22 or

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 665,083 |
| Python | 11,317 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- azkustodata/go.mod (capture: captured) — dependency clues: github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/davecgh/go-spew, github.com/golang-jwt/jwt/v5, github.com/google/uuid, github.com/kylelemons/godebug, github.com/pkg/browser, github.com/pmezard/go-difflib, github.com/samber/lo, github.com/shopspring/decimal, github.com/stretchr/testify, github.com/tj/assert, go.uber.org/goleak, golang.org/x/crypto, golang.org/x/net, golang.org/x/sys, golang.org/x/text, gopkg.in/yaml.v3
- azkustoingest/go.mod (capture: captured) — dependency clues: github.com/Azure/azure-kusto-go/azkustodata, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/data/aztables, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/Azure/azure-sdk-for-go/sdk/storage/azblob, github.com/Azure/azure-sdk-for-go/sdk/storage/azqueue, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/cenkalti/backoff/v4, github.com/davecgh/go-spew, github.com/gofrs/uuid, github.com/golang-jwt/jwt/v5, github.com/google/uuid, github.com/kylelemons/godebug, github.com/pkg/browser, github.com/pmezard/go-difflib, github.com/samber/lo, github.com/shopspring/decimal, github.com/stretchr/testify, go.uber.org/goleak
- quickstart/go.mod (capture: captured) — dependency clues: github.com/Azure/azure-kusto-go/azkustodata, github.com/Azure/azure-kusto-go/azkustoingest, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/data/aztables, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/Azure/azure-sdk-for-go/sdk/storage/azblob, github.com/Azure/azure-sdk-for-go/sdk/storage/azqueue, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/cenkalti/backoff/v4, github.com/gofrs/uuid, github.com/golang-jwt/jwt/v5, github.com/google/uuid, github.com/kylelemons/godebug, github.com/pkg/browser, github.com/samber/lo, github.com/shopspring/decimal, golang.org/x/crypto, golang.org/x/net, golang.org/x/sys

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 65
- Forks at capture: 58
- Last updated: 2026-11-12T10:03:12Z
- Last pushed: 2026-11-20T09:01:55Z
- Topics: azure, azure-data-explorer, golang, kusto

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/azure-kusto-go)
- [README](https://github.com/Azure/azure-kusto-go/blob/master/README.md)
- [Issues](https://github.com/Azure/azure-kusto-go/issues)
- [Releases](https://github.com/Azure/azure-kusto-go/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
