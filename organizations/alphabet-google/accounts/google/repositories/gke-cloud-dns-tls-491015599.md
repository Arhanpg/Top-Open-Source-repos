# google/gke-cloud-dns-tls

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/gke-cloud-dns-tls](https://github.com/google/gke-cloud-dns-tls)
- Default branch: main
- README: [Open upstream README](https://github.com/google/gke-cloud-dns-tls/blob/main/README.md)
- README blob SHA: cec787bcb717affd4d6a2d787169e3b93f64942f
- README bytes captured: 6672
- README truncated at capture limit: False
- Repository ID: 491015599
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Helping you integrating GKE with Cloud DNS and (optionally) exposing workloads using TLS.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T22:05:43+00:00

### Short excerpt (up to 300 words)

> The instructions assume you When integrating GKE, Cloud

### README headings

- Integrate GKE with Cloud DNS and expose workloads using TLS
- What you can do with this repository
- Quick HowTo
- Enable APIs
- Deploy a sample GKE cluster
- Download the cluster credentials
- Deploy cert-manager
- Create a self-signed cluster issuer, a CA and a CA cluster issuer
- Build and push the webhook container
- Request the webhook certificate
- Set the value of clientConfig.caBundle in
- webhook-configuration.yaml with the CA certificate base64.
- You can get the value with the following command:
- Deploy the configmap with the Nginx sidecar containers config
- Make DOCKER_REPO match in webhook-pod.yaml with
- your Docker repository and deploy the webhook
- Deploy the webhook configuration
- Label the default namespace so that the webhook
- automatically injects sidecar containers
- Request a sample application certificate
- Remove (if created before) and deploy the sample app
- Requirements
- Use cases
- The Mutating Admission Webhook Configuration
- Known Limitations
- What's Next
- Useful Links

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Technology and requirements: Requirements

> The instructions assume you

### Limitations and security: Known Limitations

> When integrating GKE, Cloud

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 3,034 |
| Shell | 1,104 |
| Dockerfile | 730 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- webhook-src/Dockerfile (capture: captured)
- webhook-src/requirements.txt (capture: captured) — dependency clues: flask, gunicorn, jsonpatch

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 14
- Forks at capture: 5
- Last updated: 2026-07-21T09:25:20Z
- Last pushed: 2023-04-05T22:34:43Z
- Topics: apigee, cloud-dns, gke

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/gke-cloud-dns-tls)
- [README](https://github.com/google/gke-cloud-dns-tls/blob/main/README.md)
- [Issues](https://github.com/google/gke-cloud-dns-tls/issues)
- [Releases](https://github.com/google/gke-cloud-dns-tls/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
