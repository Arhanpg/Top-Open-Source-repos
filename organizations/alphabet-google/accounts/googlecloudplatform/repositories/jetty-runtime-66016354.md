# GoogleCloudPlatform/jetty-runtime

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/jetty-runtime](https://github.com/GoogleCloudPlatform/jetty-runtime)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/jetty-runtime/blob/master/README.md)
- README blob SHA: 8d34d65c90c8bdfc08773b01ee44d0d47fefc1b5
- README bytes captured: 20182
- README truncated at capture limit: False
- Repository ID: 66016354
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Google Cloud Platform Jetty Docker image

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T20:03:43+00:00

### Short excerpt (up to 300 words)

> The /docker-entrypoint.bash for the Jetty provides mechanisms to

### README headings

- Google Cloud Platform Jetty Docker Image
- Configuring the Jetty image
- Enabling gzip compression
- Using Quickstart
- generate quickstart-web.xml
- App Engine Flexible Environment
- Container Engine & other Docker hosts
- Entry Point Features
- Logging
- Providing `logging.properties` via the web application
- Providing `logging.properties` via a custom image
- Providing `logging.properties` via docker run
- Enhanced Stackdriver Logging (BETA)
- Optional configuration
- Distributed Session Storage
- Google Cloud Session Store
- Cached Google Cloud Session Store
- Memcached Google Cloud Session Store (Alpha)
- Extending the image
- Adding the root WAR application to an image
- Adding the root application to an image
- Mounting the root application at local runtime
- Enabling dry-run
- Google Authentication using Jetty OpenID Module
- Set Up Application on Google API Console
- Jetty Configuration
- Docker Configuration
- Development Guide
- Contributing changes
- Licensing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Entry Point Features

> The /docker-entrypoint.bash for the

### Getting started and usage: Using Quickstart

> Jetty provides mechanisms to

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 62,723 |
| Shell | 26,278 |
| Go | 5,614 |
| Dockerfile | 2,506 |
| AMPL | 1,933 |
| HTML | 68 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: docker-maven-plugin, exec-maven-plugin, google-cloud-bom, jetty-parent, junit, maven-antrun-plugin, maven-checkstyle-plugin, maven-compiler-plugin, maven-dependency-plugin, maven-deploy-plugin, maven-enforcer-plugin, maven-failsafe-plugin, maven-install-plugin, maven-jar-plugin, maven-release-plugin, maven-resources-plugin, maven-source-plugin, maven-surefire-plugin, properties-maven-plugin, surefire-junit47
- jetty9-base/pom.xml (capture: captured) — dependency clues: commons-logging, exec-maven-plugin, google-auth-library-credentials, google-auth-library-oauth2-http, google-cloud-datastore, google-cloud-logging, jetty-home, jetty-parent, jetty-server, jetty9-base, maven-assembly-plugin, maven-dependency-plugin, maven-jar-plugin, maven-resources-plugin, servlet-api, xmemcached
- jetty9/pom.xml (capture: captured) — dependency clues: docker-maven-plugin, exec-maven-plugin, jetty-home, jetty-parent, jetty9, jetty9-base, maven-dependency-plugin, maven-resources-plugin
- scripts/go.mod (capture: captured) — dependency clues: github.com/blang/semver, github.com/pkg/errors
- tests/pom.xml (capture: captured) — dependency clues: docker-maven-plugin, jetty-parent, maven-deploy-plugin, maven-failsafe-plugin, maven-surefire-plugin, surefire-junit47, tests-parent
- scripts/structure_test/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 43
- Forks at capture: 31
- Last updated: 2025-11-07T03:56:45Z
- Last pushed: 2024-12-12T18:57:15Z
- Topics: app-engine, docker, gcp, google, java, jetty, runtime

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/jetty-runtime)
- [README](https://github.com/GoogleCloudPlatform/jetty-runtime/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/jetty-runtime/issues)
- [Releases](https://github.com/GoogleCloudPlatform/jetty-runtime/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
