# corretto/corretto-docker

- Company: Amazon
- GitHub account: [https://github.com/corretto](https://github.com/corretto)
- Mapping status: official-directory-listed
- Repository: [corretto/corretto-docker](https://github.com/corretto/corretto-docker)
- Default branch: main
- README: [Open upstream README](https://github.com/corretto/corretto-docker/blob/main/README.md)
- README blob SHA: add77e1cc23ed5ea4e69404e22306b8feab87b5c
- Repository ID: 264020510
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Dockerfiles for Amazon Corretto Official images. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:06:01+00:00

### Short excerpt (up to 100 words)

> Master repository where Dockerfiles for Amazon Corretto are hosted. These docker files are used to build images for Amazon Corretto Offical Images and ECR images. Amazon Linux 2 (AL2) is now end of life. The default `amazoncorretto` images (for example `amazoncorretto:8`, `amazoncorretto:11`, `amazoncorretto:17`, `amazoncorretto:21` and `latest`) are now based on Amazon Linux 2023 (AL2023). Corretto 22+ images were already AL2023 based. If you cannot upgrade to AL2023 yet, the AL2 based images remain available as a fallback via the `-al2` tags, for example `amazoncorretto:17-al2`. Note that AL2 no longer receives standard support; migrating to AL2023 is strongly recommended. For most

### README headings

- Corretto Docker ![Build Status](https://github.com/corretto/corretto-docker/workflows/Verify%20Docker%20Images/badge.svg)
- Notice: Default images moved from Amazon Linux 2 to Amazon Linux 2023
- Usage
- Supported Tags
- Building
- Security
- Why does security scanner show that a docker image has a CVE?
- Types of images provided
- Image subtypes
- Corretto 8
- Corretto 11+
- Version Tags

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Dockerfile | 118,844 |
| Shell | 12,355 |
| Python | 10,291 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- 11/headful/al2023/Dockerfile (capture: captured)
- 11/headful/al2027/Dockerfile (capture: captured)
- 11/headless/al2/Dockerfile (capture: captured)
- 11/headless/al2023/Dockerfile (capture: captured)
- 11/headless/al2027/Dockerfile (capture: captured)
- 11/jdk/al2-generic/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 201
- Forks at capture: 70
- Last updated: 2026-11-18T20:37:05Z
- Last pushed: 2026-11-18T01:40:59Z
- Topics: corretto, docker, docker-java, docker-jdk8, jdk11, jdk8

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/corretto/corretto-docker)
- [README](https://github.com/corretto/corretto-docker/blob/main/README.md)
- [Issues](https://github.com/corretto/corretto-docker/issues)
- [Releases](https://github.com/corretto/corretto-docker/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
