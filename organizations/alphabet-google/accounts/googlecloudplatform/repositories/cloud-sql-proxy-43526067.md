# GoogleCloudPlatform/cloud-sql-proxy

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloud-sql-proxy](https://github.com/GoogleCloudPlatform/cloud-sql-proxy)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloud-sql-proxy/blob/main/README.md)
- README blob SHA: 981786fef1531fdb3781795a850c6109b8b433d5
- README bytes captured: 37788
- README truncated at capture limit: False
- Repository ID: 43526067
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A utility for connecting securely to your Cloud SQL instances

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T20:43:35+00:00

### Short excerpt (up to 300 words)

> Check for the latest

### README headings

- Cloud SQL Auth Proxy
- Installation
- see Releases for other versions
- see Releases for other versions
- see Releases for other versions
- see Releases for other versions
- see Releases for other versions
- see Releases for other versions
- see Releases for other versions
- see Releases for other versions
- Install from Source
- Usage
- Credentials
- Basic Usage
- starts the Proxy listening on localhost with the default database engine port
- For example:
- MySQL      localhost:3306
- Postgres   localhost:5432
- SQL Server localhost:1433
- Configuring Port
- Starts a listener on localhost:6000
- Starts a listener on localhost:6000 for INSTANCE_CONNECTION_1
- and localhost:6001 for INSTANCE_CONNECTION_NAME_2.
- Starts a listener on localhost:5000 for the instance called "postgres"
- and starts a listener on localhost:6000 for the instance called "mysql"
- Configuring Listening Address
- Starts a listener on all interfaces at port 5432
- Starts a listener on 0.0.0.0 for "postgres" at port 5432
- and a listener on 10.0.0.1:3306 for "mysql"
- Configuring Private IP

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> Check for the latest

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 295,909 |
| Shell | 10,458 |
| Dockerfile | 1,370 |
| Batchfile | 592 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/cloudsqlconn, cloud.google.com/go/compute/metadata, cloud.google.com/go/monitoring, cloud.google.com/go/sql, cloud.google.com/go/trace, contrib.go.opencensus.io/exporter/prometheus, contrib.go.opencensus.io/exporter/stackdriver, filippo.io/edwards25519, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding
- examples/multi-container/ruby/Dockerfile (capture: captured)
- examples/multi-container/ruby/Gemfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1441
- Forks at capture: 360
- Last updated: 2026-11-19T19:44:11Z
- Last pushed: 2026-11-23T18:57:51Z
- Topics: cloud-sql, cloud-sql-proxy, gcp, google-cloud, google-cloud-platform, libraries

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloud-sql-proxy)
- [README](https://github.com/GoogleCloudPlatform/cloud-sql-proxy/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloud-sql-proxy/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloud-sql-proxy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
