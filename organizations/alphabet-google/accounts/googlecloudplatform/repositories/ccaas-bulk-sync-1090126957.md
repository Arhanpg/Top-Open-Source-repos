# GoogleCloudPlatform/ccaas-bulk-sync

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/ccaas-bulk-sync](https://github.com/GoogleCloudPlatform/ccaas-bulk-sync)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/ccaas-bulk-sync/blob/main/README.md)
- README blob SHA: 8ab1cb61ac5ca5508fdfa2a303b2744889ee548c
- README bytes captured: 25042
- README truncated at capture limit: False
- Repository ID: 1090126957
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T04:57:42+00:00

### Short excerpt (up to 300 words)

> flowchart LR admin["Admins and Deployments created before 1.0.1

### README headings

- CCaaS Bulk Synchronization Service
- Architecture
- Local development
- Deployment
- 1. Enable Google Cloud APIs
- 2. Create the Firestore database
- 3. Create an Artifact Registry repository
- 4. Create secrets and service accounts
- 4.1 Secrets
- 4.2 Application service account
- Read and write the configuration in Firestore
- Read and rotate ONLY the four application secrets (not every secret in the project)
- Manage only Cloud Scheduler jobs (custom role instead of roles/cloudscheduler.admin)
- Let the service account attach itself to the scheduler job (on itself only)
- 4.3 Cloud Build permissions
- 5. Build and deploy
- 6. Secure the application with IAP
- 7. Restrict who can make changes (admin allowlist)
- Alternative: load balancer and custom domain
- Load balancer
- OAuth consent screen and IAP client
- Enable IAP and grant access
- Enable IAP on the backend service
- Allow IAP to invoke the Cloud Run service
- Grant users access (comma-separated list)
- Verify
- Configure the service to verify IAP identities
- Google Workspace without a stored key
- Monitoring and alerts
- Sync safety

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Architecture

> flowchart LR admin["Admins and

### Limitations and security: To 1.0.1 (security fix, GHSA-47vv-vx4f-pm44)

> Deployments created before 1.0.1

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 211,314 |
| HTML | 54,707 |
| HCL | 22,937 |
| Shell | 5,465 |
| CSS | 1,759 |
| Dockerfile | 1,650 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- package.json (capture: captured) — dependency clues: @azure/msal-node, @google-cloud/firestore, @google-cloud/scheduler, @google-cloud/secret-manager, @microsoft/microsoft-graph-client, @vue/compiler-dom, autoprefixer, express, express-rate-limit, google-auth-library, googleapis, helmet, ldapts, postcss, tailwindcss, vue

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3
- Forks at capture: 1
- Last updated: 2026-11-13T17:46:19Z
- Last pushed: 2026-11-22T17:22:17Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/ccaas-bulk-sync)
- [README](https://github.com/GoogleCloudPlatform/ccaas-bulk-sync/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/ccaas-bulk-sync/issues)
- [Releases](https://github.com/GoogleCloudPlatform/ccaas-bulk-sync/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
