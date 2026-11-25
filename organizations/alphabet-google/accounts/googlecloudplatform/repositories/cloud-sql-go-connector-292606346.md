# GoogleCloudPlatform/cloud-sql-go-connector

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloud-sql-go-connector](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector/blob/main/README.md)
- README blob SHA: 98bbbaa94a567843318c1d6c226cd563cbdea0ee
- README bytes captured: 27287
- README truncated at capture limit: False
- Repository ID: 292606346
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Go library for connecting securely to your Cloud SQL instances

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T20:30:22+00:00

### Short excerpt (up to 300 words)

> The _Cloud SQL Go You can install this

### README headings

- Installation
- Usage
- APIs and Services
- Credentials
- Connecting to a database
- Postgres
- Using the dialer with pgx
- Using the dialer with `database/sql`
- MySQL
- SQL Server
- Using Advanced Disaster Recovery and DNS domain names to identify instances
- Using Advanced Recovery Write Endpoint DNS Name
- Configure your DNS Records
- Configure the connector
- Automatic fail-over using DNS domain names
- Using Options
- Using DialOptions
- Automatic IAM Database Authentication
- Post-Quantum Cryptography (PQC)
- Built-in Client Metrics (BETA)
- Enabling Metrics and Tracing
- Debug Logging
- Support policy
- Major version lifecycle
- Supported Go Versions
- Release cadence

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> The _Cloud SQL Go

### Getting started and usage: Installation

> You can install this

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 690,476 |
| Shell | 12,051 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/monitoring, cloud.google.com/go/sql, filippo.io/edwards25519, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/cespare/xxhash/v2, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-sql-driver/mysql, github.com/golang-sql/civil, github.com/golang-sql/sqlexp, github.com/golang/groupcache, github.com/google/go-cmp, github.com/google/s2a-go, github.com/google/uuid, github.com/googleapis/enterprise-certificate-proxy
- examples/cloudrun/mysql/Dockerfile (capture: captured)
- examples/cloudrun/mysql/go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/cloudsqlconn, cloud.google.com/go/compute/metadata, cloud.google.com/go/monitoring, cloud.google.com/go/sql, filippo.io/edwards25519, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/cespare/xxhash/v2, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-sql-driver/mysql, github.com/golang/groupcache, github.com/google/s2a-go, github.com/google/uuid, github.com/googleapis/enterprise-certificate-proxy, github.com/googleapis/gax-go/v2, github.com/jackc/pgx/v5
- examples/cloudrun/postgres/Dockerfile (capture: captured)
- examples/cloudrun/postgres/go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/cloudsqlconn, cloud.google.com/go/compute/metadata, cloud.google.com/go/monitoring, cloud.google.com/go/sql, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/cespare/xxhash/v2, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/golang/groupcache, github.com/google/s2a-go, github.com/google/uuid, github.com/googleapis/enterprise-certificate-proxy, github.com/googleapis/gax-go/v2, github.com/jackc/pgpassfile, github.com/jackc/pgservicefile, github.com/jackc/pgx/v5
- examples/cloudrun/sqlserver/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 147
- Forks at capture: 40
- Last updated: 2026-11-11T19:33:14Z
- Last pushed: 2026-11-23T18:26:16Z
- Topics: cloudsql, go, golang, libraries

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector)
- [README](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
