# GoogleCloudPlatform/codelab-mlops-airflow-gke

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/codelab-mlops-airflow-gke](https://github.com/GoogleCloudPlatform/codelab-mlops-airflow-gke)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/codelab-mlops-airflow-gke/blob/main/README.md)
- README blob SHA: 72fa5669fdd72b077a723e8fd81798a4e8e832cb
- README bytes captured: 6121
- README truncated at capture limit: False
- Repository ID: 885446400
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T22:04:59+00:00

### Short excerpt (up to 300 words)

> helm repo add apache-airflow

### README headings

- MLOps Codelab with Airflow on GKE
- Set environment variable
- Enable GKE API service
- Create a VPC for the GKE cluster
- Create the needed infrastructure (GKE, Bucket, Artifact Registry)
- Create the PV and PVC in GKE for Airflow DAGs storage
- Add the necessary IAM permissions to access buckets from Airflow
- Install Airflow helm chart
- Connect to Airflow UI
- Define a Google Cloud connection in Airflow UI
- Add IAM permissions to the Cloud Build service account
- Build the docker images
- Chage DAG variables
- Upload your DAG file to the GCS bucket
- BUG

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install Airflow helm chart

> helm repo add apache-airflow

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 20,491 |
| HCL | 12,720 |
| Dockerfile | 2,166 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- services/1-dataset-download/Dockerfile (capture: captured)
- services/1-dataset-download/requirements.txt (capture: captured) — dependency clues: google-cloud-storage, kagglehub
- services/2-data-preparation/Dockerfile (capture: captured)
- services/2-data-preparation/requirements.txt (capture: captured) — dependency clues: datasets, gcsfs, pandas
- services/3-finetuning/Dockerfile (capture: captured)
- services/3-finetuning/requirements.txt (capture: captured) — dependency clues: accelerate, bitsandbytes, datasets, gcsfs, peft, torch, transformers, trl

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3
- Forks at capture: 1
- Last updated: 2025-12-27T01:07:32Z
- Last pushed: 2026-11-13T08:24:10Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/codelab-mlops-airflow-gke)
- [README](https://github.com/GoogleCloudPlatform/codelab-mlops-airflow-gke/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/codelab-mlops-airflow-gke/issues)
- [Releases](https://github.com/GoogleCloudPlatform/codelab-mlops-airflow-gke/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
