# GoogleCloudPlatform/dlp-pdf-redaction

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/dlp-pdf-redaction](https://github.com/GoogleCloudPlatform/dlp-pdf-redaction)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/dlp-pdf-redaction/blob/main/README.md)
- README blob SHA: 5f9529a99d606e97dc114b5c03e270e4a6428fa2
- README bytes captured: 7759
- README truncated at capture limit: False
- Repository ID: 397686712
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This solution provides an automated, serverless way to redact sensitive data from PDF files using Google Cloud Services like Data Loss Prevention (DLP), Cloud Workflows, and Cloud Run.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T20:03:03+00:00

### Short excerpt (up to 300 words)

> The image below describes

### README headings

- Solution Guide
- Solution Architecture Diagram
- Workflow Steps
- Deploy PDF Redaction app
- What resources are created?
- How to deploy?
- 1. Create a project and enable billing
- 2. Get the code
- 3. Build images for Cloud Run
- Enable required APIs
- Create a Docker image repo to store apps docker images
- Create Service Account for CloudBuild and grant required roles
- Build docker images of the app and store them in artifact registry repo
- 4. Deploy the infrastructure using Terraform
- 5. Take note of Terraform Outputs
- 6. Test

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Solution Architecture Diagram

> The image below describes

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 23,640 |
| Python | 19,034 |
| Dockerfile | 5,335 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/dlp-runner/Dockerfile (capture: captured)
- src/dlp-runner/requirements.txt (capture: captured) — dependency clues: Flask, google-cloud-dlp, google-cloud-storage, gunicorn
- src/findings-writer/Dockerfile (capture: captured)
- src/findings-writer/requirements.txt (capture: captured) — dependency clues: Flask, google-cloud-bigquery, google-cloud-storage, gunicorn
- src/pdf-merger/Dockerfile (capture: captured)
- src/pdf-merger/requirements.txt (capture: captured) — dependency clues: Flask, PyPDF2, google-cloud-storage, gunicorn, pytesseract

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 68
- Forks at capture: 29
- Last updated: 2026-09-14T04:35:16Z
- Last pushed: 2026-02-20T22:59:53Z
- Topics: bigquery, cloud, cloudfunctions, cloudrun, cloudstorage, cloudworkflows, datalossprevention, dlp, documents, gcp, mask, ocr, pdf, redaction, serverless, terraform, tesseract, workflows

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/dlp-pdf-redaction)
- [README](https://github.com/GoogleCloudPlatform/dlp-pdf-redaction/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/dlp-pdf-redaction/issues)
- [Releases](https://github.com/GoogleCloudPlatform/dlp-pdf-redaction/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
