# GoogleCloudPlatform/gcp-ca-service-ocsp

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/gcp-ca-service-ocsp](https://github.com/GoogleCloudPlatform/gcp-ca-service-ocsp)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/gcp-ca-service-ocsp/blob/master/README.md)
- README blob SHA: 8d05fed4e6fae5a5f65a6867e2060e2032ec6f75
- README bytes captured: 21614
- README truncated at capture limit: False
- Repository ID: 283776803
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

OCSP Server for Google Cloud Certificate Service

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T03:25:54+00:00

### Short excerpt (up to 300 words)

> OCSP responses are pre-generated

### README headings

- OCSP Server for Google Cloud Certificate Service
- Architecture
- Components
- Prerequisite
- OCSP Generator
- Configure OCSP Response Bucket
- Acquire the RootCA Certificate
- Generate the KeyPair that allows for OCSP Signing
- Run OCSP Generator
- Verify OCSP Responses are created
- OCSP Server
- Create a Service Account for Cloud Run and allow it to read OCSP responses
- Run OCSP Server
- Build and push OCSP server
- Deploy Server to Cloud Run
- (optional) Verify OCSP Endpoint
- Create HTTP L7 Loadbalancer
- Allocate External IP
- Create Cloud Run Backend NEG
- Create URL Maps for OCSP Service
- Edit URL Map and specify path/rule for the backendService
- Create Target Proxy and Frontend
- Verify OCSP with L7LB
- Notes
- Invalidate CDN Cache
- OCSP Server with TLS
- Nginx cert stapling
- Using GCP Secrets for OCSP Generator
- Serverless OCSP Generator
- Serving GET requests directly from GCS

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Architecture

> OCSP responses are pre-generated

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 18,990 |
| Dockerfile | 250 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: cloud.google.com/go, cloud.google.com/go/security/privateca/apiv1beta1, cloud.google.com/go/storage, github.com/cloudflare/golibs, github.com/golang/protobuf, github.com/gorilla/mux, github.com/hashicorp/golang-lru, golang.org/x/crypto, golang.org/x/net, golang.org/x/time, google.golang.org/api, google.golang.org/genproto, google.golang.org/genproto/googleapis/cloud/security/privateca/v1beta1
- lib/cloud.google.com/go/security/privateca/apiv1beta1/go.mod (capture: captured)
- lib/google.golang.org/genproto/googleapis/cloud/security/privateca/v1beta1/go.mod (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 17
- Forks at capture: 12
- Last updated: 2026-05-04T15:16:40Z
- Last pushed: 2021-11-15T23:17:51Z
- Topics: google-cloud, google-cloud-platform, ocsp

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/gcp-ca-service-ocsp)
- [README](https://github.com/GoogleCloudPlatform/gcp-ca-service-ocsp/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/gcp-ca-service-ocsp/issues)
- [Releases](https://github.com/GoogleCloudPlatform/gcp-ca-service-ocsp/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
