# GoogleCloudPlatform/iam_visibility_audit

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/iam_visibility_audit](https://github.com/GoogleCloudPlatform/iam_visibility_audit)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/iam_visibility_audit/blob/main/README.md)
- README blob SHA: 3fe958532f6d666d06816fe412f880842702a3b3
- README bytes captured: 12780
- README truncated at capture limit: False
- Repository ID: 414571363
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Auditing users for IAM bindings outside of primarily Cloud Organization

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T19:08:31+00:00

### Short excerpt (up to 300 words)

> To configure this script,

### README headings

- Auditing users for IAM bindings outside of primarily Cloud Organization
- How does it work?
- Usage
- select a project that will host the service account
- acquire the organization ID
- Enable the apis on the project
- create service account
- get the service account's clientID
- enable impersonation instead of key-download and adapt the workspace AdminAPI to use the impersonated access token
- Alternatively, you can download a key but this is _NOT_ recommended
- gcloud iam service-accounts keys create svc_account.json --iam-account=dwd-sa@$PROJECT_ID.iam.gserviceaccount.com
- Allow service account domain IAM privileges
- http://cloud.google.com/asset-inventory/docs/access-control#required_permissions
- with service account impersonation (preferred)
- with service account Key (not recommended)
- go run main.go --serviceAccountFile=svc_account.json \
- --subject=$DOMAIN_ADMIN \
- --organization $ORGANIZATION_ID \
- -cx $CX --alsologtostderr=1 -v 10
- Working with Quotas/Limits
- Sleep
- Throttling
- Sharding
- `X-Goog-User-Project`

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Usage

> To configure this script,

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 18,018 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cloud.google.com/go, cloud.google.com/go/asset, github.com/golang/glog, github.com/golang/groupcache, github.com/golang/protobuf, github.com/google/go-cmp, github.com/googleapis/gax-go/v2, go.opencensus.io, golang.org/x/net, golang.org/x/oauth2, golang.org/x/sys, golang.org/x/text, golang.org/x/time, google.golang.org/api, google.golang.org/appengine, google.golang.org/genproto, google.golang.org/grpc, google.golang.org/protobuf

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3
- Forks at capture: 1
- Last updated: 2024-05-07T02:05:18Z
- Last pushed: 2021-11-03T00:09:51Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/iam_visibility_audit)
- [README](https://github.com/GoogleCloudPlatform/iam_visibility_audit/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/iam_visibility_audit/issues)
- [Releases](https://github.com/GoogleCloudPlatform/iam_visibility_audit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
