# awslabs/aws-kubernetes-migration-factory

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-kubernetes-migration-factory](https://github.com/awslabs/aws-kubernetes-migration-factory)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/aws-kubernetes-migration-factory/blob/main/README.md)
- README blob SHA: 6fa8e9e9a0a6f2ef357853bd5d620fce627f29eb
- README bytes captured: 18840
- README truncated at capture limit: False
- Repository ID: 445319082
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T20:33:22+00:00

### Short excerpt (up to 300 words)

> $ ./bin/kmf Please pass Kubernetes Migration Factory (KMF) This tool migrates from (1) Currently KMF supports

### README headings

- Kubernetes Migration Factory User Guide
- **Architecture**
- **Prerequisites**
- **KMF CLI Setup**
- **Running KMF CLI:**
- **Running with a Config config.ini**
- common configuration params required for migration.
- Local path where generated helm charts to be saved
- Valid Value for ACTION Deploy/Delete
- Namespaces from which the resources need to migrated
- comma seperated list of namespace or "all"
- Source Cloud Provider valid values are GKE,AKE,KOPS
- Source kube config file
- Refer the documentation for the respective source cluster provider to create the kubeconfig file. For GKE, you may refer https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl
- Target Cloud Provider valid value is AWS only
- Target kube config file
- Refer the AWS documentation for creating the kubeconfig file https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html
- This section is used for passing values to the KMF CLI to perform container registry images migration to Amazon ECR and this is optional
- Do you wish to migrate images from 3rd party repositories to Amazon Elastic Container Registry? Supply either "Yes" or "No"
- Comma separated list of 3rd party registries. Tool supports migration from gcr, gitlab, mcr, dockerhub registries.
- **Explanation of each supported parameter for the KMF CLI tool**
- **COMMON Section**
- common configuration params required for migration
- **SOURCE Section**
- **TARGET Section**
- **MIGRATE_IMAGES Section**
- **Some examples while interacting with KMF CLI**
- **Running as one line:**
- **Migrating all resources from all namespaces**
- **Migrating all resources from one namespace**

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: **Some examples while interacting with KMF CLI**

> $ ./bin/kmf Please pass

### Architecture and design: **Architecture**

> Kubernetes Migration Factory (KMF)

### Technology and requirements: **Prerequisites**

> This tool migrates from

### Limitations and security: **Limitations:**

> (1) Currently KMF supports

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 113,756 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go, github.com/bigkevmcd/go-configparser, github.com/ghodss/yaml, github.com/gofrs/flock, github.com/pkg/errors, gopkg.in/yaml.v2, gopkg.in/yaml.v3, helm.sh/helm/v3, k8s.io/api, k8s.io/apimachinery, k8s.io/client-go

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 133
- Forks at capture: 34
- Last updated: 2026-11-19T14:05:47Z
- Last pushed: 2024-09-25T20:41:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-kubernetes-migration-factory)
- [README](https://github.com/awslabs/aws-kubernetes-migration-factory/blob/main/README.md)
- [Issues](https://github.com/awslabs/aws-kubernetes-migration-factory/issues)
- [Releases](https://github.com/awslabs/aws-kubernetes-migration-factory/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
