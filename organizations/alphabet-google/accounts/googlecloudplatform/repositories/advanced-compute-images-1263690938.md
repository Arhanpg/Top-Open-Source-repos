# GoogleCloudPlatform/advanced-compute-images

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/advanced-compute-images](https://github.com/GoogleCloudPlatform/advanced-compute-images)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/advanced-compute-images/blob/main/README.md)
- README blob SHA: 02fce8e5a7c562006cecfe49eab661c6b7e35bb9
- Repository ID: 1263690938
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:44:13+00:00

### Short excerpt (up to 100 words)

> This repository contains Packer and Ansible scripts for building modular, multi-layered VM images for AI and HPC workloads on Google Cloud. / ├── cloudbuild.yaml ├── packer/ │ ├── builds/ │ │ └── ubuntu-2204-slurm-gpu-dev.pkrvars.hcl │ ├── main.pkr.hcl │ └── variables.pkr.hcl ├── ansible/ │ ├── playbook.yaml │ ├── roles/ │ │ ├── core/ │ │ │ ├── os_configs/ │ │ │ ├── nvidia_stack/ │ │ │ ├── slurm/ │ │ │ └── ... │ │ └── contrib/ │ │ └── ... │ └── ansible.cfg ├── examples/ │ └── build_custom_image.sh └── README.md * **cloudbuild.yaml**: Google Cloud Build configuration file to trigger Packer builds.

### README headings

- ACI (Advanced Compute Images) VM Images
- Repository Structure
- Core Role Dependencies
- Image Naming Convention
- Triggering a Build
- Updating the NVIDIA driver

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 73,421 |
| HCL | 42,029 |
| Jinja | 7,166 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 1
- Last updated: 2026-11-03T09:58:06Z
- Last pushed: 2026-11-20T09:13:34Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/advanced-compute-images)
- [README](https://github.com/GoogleCloudPlatform/advanced-compute-images/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/advanced-compute-images/issues)
- [Releases](https://github.com/GoogleCloudPlatform/advanced-compute-images/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
