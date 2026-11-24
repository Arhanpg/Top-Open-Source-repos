# GoogleCloudPlatform/alloydb-auth-proxy

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/alloydb-auth-proxy](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy/blob/main/README.md)
- README blob SHA: 5e579be095c35c7eccfde788cc4eaa6dfbcdb052
- README bytes captured: 22071
- README truncated at capture limit: False
- Repository ID: 465813029
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A utility for connecting securely to your AlloyDB instances

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T06:05:35+00:00

### Short excerpt (up to 300 words)

> Get connected in five This project follows semantic

### README headings

- AlloyDB Auth Proxy
- Quickstart
- 1. Install the proxy
- 2. Authenticate
- 3. Find your instance URI
- 4. Start the proxy
- By default, the proxy connects over Private Service Access—a private
- connection within the same VPC as your AlloyDB instance. Add --public-ip
- if your instance has a public IP and you are not connecting from within
- the VPC.
- Mounts your local gcloud credentials into the container
- 5. Connect
- Table of contents
- Installation
- Binary
- Container image
- Pull a specific version (recommended over :latest)
- Build from source
- Using go install
- Using the Makefile
- Build your own container
- Build default container image (alloydb-auth-proxy:latest)
- Build Alpine container image (alloydb-auth-proxy:latest-alpine)
- Build multi-arch default container image
- Build multi-arch Alpine container image
- Using internal mirrors
- Authentication
- One-time setup on a developer machine
- Usage
- Basic usage

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Quickstart

> Get connected in five

### Limitations and security: Support policy

> This project follows semantic

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 233,802 |
| Makefile | 2,852 |
| Dockerfile | 1,075 |
| Batchfile | 641 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: cloud.google.com/go, cloud.google.com/go/alloydb, cloud.google.com/go/alloydbconn, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/longrunning, cloud.google.com/go/monitoring, cloud.google.com/go/trace, contrib.go.opencensus.io/exporter/prometheus, contrib.go.opencensus.io/exporter/stackdriver, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini
- Makefile (capture: captured)
- examples/go/Dockerfile (capture: captured)
- examples/go/go.mod (capture: captured) — dependency clues: github.com/jackc/pgpassfile, github.com/jackc/pgservicefile, github.com/jackc/pgx/v5, github.com/jackc/puddle/v2, golang.org/x/sync, golang.org/x/text
- examples/multi-container/ruby/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 83
- Forks at capture: 21
- Last updated: 2026-11-11T19:26:13Z
- Last pushed: 2026-11-18T01:51:48Z
- Topics: alloydb, libraries

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy)
- [README](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy/issues)
- [Releases](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
