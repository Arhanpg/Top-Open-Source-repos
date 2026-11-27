# GoogleCloudPlatform/medical-imaging

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/medical-imaging](https://github.com/GoogleCloudPlatform/medical-imaging)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/medical-imaging/blob/main/README.md)
- README blob SHA: 2b2ba4f47ebccb8527bbc967dec11dbc42d68912
- README bytes captured: 4400
- README truncated at capture limit: False
- Repository ID: 729160559
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Accelerate ingestion/transformation of pathology images into DICOMWeb 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T21:56:56+00:00

### Short excerpt (up to 300 words)

> This repository contains open source tools created by Google Research to make it **easy** to bring digital pathology imaging to Google Cloud and to serve

### README headings

- Google Research Digital Pathology
- [Cloud Pathology](https://github.com/GoogleCloudPlatform/medical-imaging/tree/main/pathology)
- <li> [Transformation Pipeline](https://github.com/GoogleCloudPlatform/medical-imaging/tree/main/pathology/transformation_pipeline)</li>
- <li> [DICOM Proxy](https://github.com/GoogleCloudPlatform/medical-imaging/tree/main/pathology/dicom_proxy)</li>
- <li>[Front End](https://github.com/GoogleCloudPlatform/medical-imaging/tree/main/pathology/viewer)</li>
- [Image Lifecycle Management](https://github.com/GoogleCloudPlatform/medical-imaging/tree/main/ilm)
- [Infrastructure as Code (IaC)](https://github.com/GoogleCloudPlatform/medical-imaging/tree/main/iac)
- Related Open Source Projects
- <li> [EZ-WSI DICOMweb](https://github.com/GoogleCloudPlatform/EZ-WSI-DICOMweb)</li>
- <li>[Google Research Pathology Foundations](https://research.google/blog/helping-everyone-build-ai-for-healthcare-applications-with-open-foundation-models/)</li>
- Contributing
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Google Research Digital Pathology

> This repository contains open source tools created by Google Research to make it **easy** to bring digital pathology imaging to Google Cloud and to serve

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 3,787,293 |
| TypeScript | 1,643,837 |
| Starlark | 144,043 |
| HTML | 111,075 |
| SCSS | 85,136 |
| HCL | 63,825 |
| Dockerfile | 51,972 |
| Shell | 4,212 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- ilm/deployment/requirements.txt (capture: captured) — dependency clues: absl-py, aiofiles, aiohappyeyeballs, aiohttp, aiosignal, annotated-types, anyio, apache-beam, asn1crypto, attrs, beartype, betterproto, cachetools, certifi, cffi, charset-normalizer, cloud-sql-python-connector, cryptography, dataclasses-json, distro
- pathology/dicom_proxy/Dockerfile (capture: captured)
- pathology/dicom_proxy/requirements.txt (capture: captured) — dependency clues: absl-py, blinker, brotli, cachetools, certifi, cffi, charset-normalizer, click, cryptography, dataclasses-json, ez-wsi-dicomweb, flask, flask-compress, google-api-core, google-api-python-client, google-auth, google-auth-httplib2, google-cloud-appengine-logging, google-cloud-audit-log, google-cloud-core
- pathology/transformation_pipeline/Dockerfile (capture: captured)
- pathology/transformation_pipeline/requirements.txt (capture: captured) — dependency clues: absl-py, cachetools, certifi, cffi, charset-normalizer, cryptography, dataclasses-json, ez-wsi-dicomweb, google-api-core, google-api-python-client, google-auth, google-auth-httplib2, google-cloud-appengine-logging, google-cloud-audit-log, google-cloud-bigquery, google-cloud-core, google-cloud-logging, google-cloud-pubsub, google-cloud-secret-manager, google-cloud-storage
- pathology/viewer/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 29
- Forks at capture: 15
- Last updated: 2026-10-31T15:33:43Z
- Last pushed: 2026-11-23T15:46:59Z
- Topics: dicom, healthcare, medical-imaging, pathology

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/medical-imaging)
- [README](https://github.com/GoogleCloudPlatform/medical-imaging/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/medical-imaging/issues)
- [Releases](https://github.com/GoogleCloudPlatform/medical-imaging/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
