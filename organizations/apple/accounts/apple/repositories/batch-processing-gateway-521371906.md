# apple/batch-processing-gateway

- Company: Apple
- GitHub account: [https://github.com/apple](https://github.com/apple)
- Mapping status: verified
- Repository: [apple/batch-processing-gateway](https://github.com/apple/batch-processing-gateway)
- Default branch: main
- README: [Open upstream README](https://github.com/apple/batch-processing-gateway/blob/main/README.md)
- README blob SHA: 12aa3d2a9648d3d404f1613970b91697ed7177e9
- Repository ID: 521371906
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The gateway component to make Spark on K8s much easier for Spark users.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:00:33+00:00

### Short excerpt (up to 100 words)

> Batch Processing Gateway makes running Spark service on Kubernetes easy. It allows users to submit, examine and delete Spark apps on Kubernetes with intuitive API calls, without worrying much about what goes on behind the scene. It can also be configured with many Spark clusters to scale the service horizontally. Batch Processing Gateway (BPG) is the frontend of the entire stack of Spark service, which typically includes one gateway instance and multiple Spark K8s clusters. A typical flow of Spark application submission: - Spark users publish the app artifacts (.jar, .py, .zip, etc) to S3 artifacts bucket - Users compose

### README headings

- Batch Processing Gateway
- Overview
- Artifacts Bucket
- App Submission DB
- application_submission schema (partial)
- REST Endpoints
- OpenAPI Spec
- Auth
- Spark Cluster Routing
- Namespace Based Cluster Config
- Queue Config
- Weight Based Cluster Selection
- Application Logs
- logindex schema (partial)
- Contributing
- Deployment
- Troubleshoot Spark Cluster
- Built With
- Public Talks
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 552,625 |
| Shell | 16,396 |
| Jinja | 4,902 |
| Python | 1,355 |
| Dockerfile | 981 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- pom.xml (capture: captured) — dependency clues: aws-java-sdk-bom, aws-java-sdk-s3, aws-java-sdk-sts, bpg, commons-math3, dropwizard-auth, dropwizard-core, dropwizard-dependencies, dropwizard-testing, google-cloud-storage, h2, hibernate-validator, jackson-annotations, jakarta.validation-api, java-jwt, jdbi3-core, kubernetes-client, libraries-bom, maven-antrun-plugin, maven-compiler-plugin
- dev-setup/ozone/Chart.yaml (capture: captured)
- helm/batch-processing-gateway/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 221
- Forks at capture: 46
- Last updated: 2026-09-08T22:58:32Z
- Last pushed: 2026-05-06T23:09:09Z
- Topics: batch-processing, k8s, kubernetes, spark

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/apple/batch-processing-gateway)
- [README](https://github.com/apple/batch-processing-gateway/blob/main/README.md)
- [Issues](https://github.com/apple/batch-processing-gateway/issues)
- [Releases](https://github.com/apple/batch-processing-gateway/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
