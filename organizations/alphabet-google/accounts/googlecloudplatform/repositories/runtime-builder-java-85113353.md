# GoogleCloudPlatform/runtime-builder-java

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/runtime-builder-java](https://github.com/GoogleCloudPlatform/runtime-builder-java)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/runtime-builder-java/blob/master/README.md)
- README blob SHA: 60c417c5aaa5415fa601912c280ed8cd71ff9aa9
- README bytes captured: 5560
- README truncated at capture limit: False
- Repository ID: 85113353
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Google Cloud Container Builder pipeline for packaging Java applications into docker containers

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T06:11:31+00:00

### Short excerpt (up to 300 words)

> OUTPUT_IMAGE=gcr.io/my-gcp-project/my-application-container

### README headings

- Java Runtime Builder
- Running via Google Cloud Container Builder (recommended)
- Determine the name of your desired output image. Note that it must be a path to a Google Container
- Registry bucket to which your Cloud SDK installation has push access.
- initiate the cloud container build
- Running via Docker (without Cloud Container Builder)
- Generate docker resources
- See java.yaml for the fully specified jdk-runtimes-map server-runtimes-map args
- package my application into a docker container
- Configuration
- Sample app.yaml
- all parameters specified below in the runtime_config block are optional
- Images
- Development guide
- Contributing changes
- Licensing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Registry bucket to which your Cloud SDK installation has push access.

> OUTPUT_IMAGE=gcr.io/my-gcp-project/my-application-container

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 162,230 |
| Shell | 8,577 |
| Dockerfile | 723 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: error_prone_core, jacoco-maven-plugin, java-runtime-builder, maven-checkstyle-plugin, maven-compiler-plugin, maven-dependency-plugin, maven-resources-plugin, maven-surefire-plugin, plexus-compiler-javac-errorprone
- java-runtime-builder-app/pom.xml (capture: captured) — dependency clues: commons-cli, commons-io, guava, guice, guice-assistedinject, jackson-annotations, jackson-databind, jackson-dataformat-yaml, java-runtime-builder, java-runtime-builder-app, junit, logback-classic, maven-assembly-plugin, mockito-core
- java-runtime-builder-docker/pom.xml (capture: captured) — dependency clues: docker-maven-plugin, java-runtime-builder, java-runtime-builder-app, java-runtime-builder-docker, maven-dependency-plugin
- test/integration/test_resources/spring_boot_gradlew/build.gradle (capture: captured)
- java-runtime-builder-docker/src/main/resources/docker/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9
- Forks at capture: 10
- Last updated: 2025-05-19T10:30:52Z
- Last pushed: 2024-12-12T18:56:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/runtime-builder-java)
- [README](https://github.com/GoogleCloudPlatform/runtime-builder-java/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/runtime-builder-java/issues)
- [Releases](https://github.com/GoogleCloudPlatform/runtime-builder-java/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
