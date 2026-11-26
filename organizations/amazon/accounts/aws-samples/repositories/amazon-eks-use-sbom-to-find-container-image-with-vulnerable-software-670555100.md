# aws-samples/amazon-eks-use-sbom-to-find-container-image-with-vulnerable-software

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-eks-use-sbom-to-find-container-image-with-vulnerable-software](https://github.com/aws-samples/amazon-eks-use-sbom-to-find-container-image-with-vulnerable-software)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-eks-use-sbom-to-find-container-image-with-vulnerable-software/blob/main/README.md)
- README blob SHA: 5b1ae051adebc58c216a1baa56122d27a5266ffe
- README bytes captured: 17317
- README truncated at capture limit: False
- Repository ID: 670555100
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repo hosts Terraform code for generating and analyzing Software Bill of Materials (SBOM) for Amazon ECR images. It helps identify Amazon EKS images with vulnerable software components using Amazon Athena.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T19:08:51+00:00

### Short excerpt (up to 300 words)

> On occasion, users may First clone this GitHub

### README headings

- Using SBOM to find vulnerable container images running on Amazon EKS clusters
- Table of Contents
- Diagram
- Instructions
- Deploy the solution architecture using Terraform
- Deploy the EKS cronjob
- Populate the Glue catalog
- Run sample Athena Query
- **Vulnerability in a specific package - Search for specific package (without version)**
- sbom_image_name    sbom_package_name    eks_running_image    pods    sbom_sourceInfo    sbom_version_info
- **Vulnerability in specific package and version - Search for specific package and version**
- sbom_image_name    sbom_package_name    eks_running_image    pods    sbom_sourceInfo    sbom_version_info
- **Vulnerability across multiple packages - Search for images with multiple packages installed  (Use IN array on SQL)**
- sbom_image_name    sbom_package_name    eks_running_image    pods    sbom_sourceInfo    sbom_version_info
- Cleaning up
- Contributing
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: **Vulnerability across multiple packages - Search for images with multiple packages installed  (Use IN array on SQL)**

> On occasion, users may

### Architecture and design: Deploy the solution architecture using Terraform

> First clone this GitHub

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 16,335 |
| Python | 1,437 |
| Dockerfile | 220 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- eks-image-discovery/Dockerfile (capture: captured)
- eks-image-discovery/requirements.txt (capture: captured) — dependency clues: PyYAML, boto3, botocore, cachetools, certifi, charset-normalizer, google-auth, idna, jmespath, kubernetes, oauthlib, pyasn1, pyasn1-modules, python-dateutil, requests, requests-oauthlib, rsa, s3transfer, six, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 18
- Forks at capture: 2
- Last updated: 2026-11-16T01:55:41Z
- Last pushed: 2023-10-18T00:08:24Z
- Topics: athena, aws, cloud, codebuild, ecr, eks, s3, sbom, security, software-bill-of-materials, terraform

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-eks-use-sbom-to-find-container-image-with-vulnerable-software)
- [README](https://github.com/aws-samples/amazon-eks-use-sbom-to-find-container-image-with-vulnerable-software/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-eks-use-sbom-to-find-container-image-with-vulnerable-software/issues)
- [Releases](https://github.com/aws-samples/amazon-eks-use-sbom-to-find-container-image-with-vulnerable-software/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
