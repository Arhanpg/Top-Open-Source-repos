# GoogleCloudPlatform/appengine-java-standard

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/appengine-java-standard](https://github.com/GoogleCloudPlatform/appengine-java-standard)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/appengine-java-standard/blob/main/README.md)
- README blob SHA: 5d425fdff9661fa08e06b4a9985ff7fa7398339d
- README bytes captured: 20688
- README truncated at capture limit: False
- Repository ID: 436425883
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Google App Engine Standard Java runtime: Prod runtime, local devappserver, Cloud SDK Java components, GAE APIs, and GAE API emulators.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T21:06:24+00:00

### Short excerpt (up to 300 words)

> Copyright 2021 Google LLC The entry point for

### README headings

- Google App Engine (GAE) standard environment source code for Java 17, Java 21, Java 25.
- Prerequisites
- Use a JDK17 environment, so it can build the Java17 GAE runtime.
- Releases
- Modules
- App Engine Java APIs
- App Engine Java Remote APIs
- User Visible Changes With Maven Builds
- Local Unit Testing for Java 17, 21, 25
- App Engine Java local development implementation of the APIs
- App Engine Java various local development utilities and devappserver
- App Engine Java production runtime execution environment
- Default entrypoint used by Java17, Java21 and Java25
- Entry Point Features
- Java 17 (`<runtime>java17</runtime>`)
- Java 21 (`<runtime>java21</runtime>`)
- Java 25 (`<runtime>java25</runtime>`)
- Contributing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> Copyright 2021 Google LLC

### Features and capabilities: Entry Point Features

> The entry point for

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 11,381,151 |
| Shell | 28,307 |
| GAP | 21,948 |
| CSS | 16,405 |
| HTML | 15,672 |
| JavaScript | 9,465 |
| FreeMarker | 2,577 |
| Batchfile | 1,995 |
| Starlark | 698 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: activation, antlr-runtime, antlr3-maven-plugin, apache-el, apache-jsp, appengine-api-1.0-sdk, appengine-api-stubs, appengine-apis, appengine-apis-dev, appengine-init, appengine-local-runtime, appengine-maven-plugin, appengine-remote-api, appengine-resources, appengine-testing, appengine-tools-sdk, appengine-utils, auto-service, auto-service-annotations, auto-value
- api/pom.xml (capture: captured) — dependency clues: activation, antlr-runtime, antlr3-maven-plugin, appengine-apis, appengine-utils, auto-service, auto-service-annotations, auto-value, auto-value-annotations, datastore-v1-proto-client, geronimo-javamail_1.4_spec, google-api-client, google-auth-library-oauth2-http, google-cloud-storage, google-cloud-tasks, google-extensions, google-http-client, google-http-client-jackson2, google-oauth-client, grpc-auth
- api_dev/pom.xml (capture: captured) — dependency clues: antlr-runtime, appengine-api-1.0-sdk, appengine-apis, appengine-apis-dev, appengine-init, appengine-resources, appengine-utils, auto-service, auto-value, auto-value-annotations, datastore-v1-proto-client, easymock, flogger-system-backend, geronimo-javamail_1.4_spec, google-extensions, google-http-client-jackson2, guava, guava-jdk5, guava-testlib, httpclient
- api_legacy/pom.xml (capture: captured) — dependency clues: appengine-api-1.0-sdk, appengine-api-legacy, guava, jcache-api, junit, maven-shade-plugin, mockito-core, parent, truth
- appengine-api-1.0-sdk/pom.xml (capture: captured) — dependency clues: appengine-api-1.0-sdk, appengine-apis, auto-common, auto-service, auto-service-annotations, google-auth-library-oauth2-http, google-cloud-tasks, grpc-api, joda-time, junit, maven-failsafe-plugin, maven-javadoc-plugin, maven-shade-plugin, parent, truth
- appengine-api-stubs/pom.xml (capture: captured) — dependency clues: appengine-api-1.0-sdk, appengine-api-stubs, appengine-apis-dev, auto-common, auto-service, auto-service-annotations, httpcore-nio, httpmime, maven-javadoc-plugin, maven-shade-plugin, parent, shared-sdk

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 223
- Forks at capture: 66
- Last updated: 2026-11-12T07:08:11Z
- Last pushed: 2026-11-23T05:26:53Z
- Topics: appengine, appengine-java, google, google-cloud, google-cloud-platform, java, java-8, java11, java17, java8, paas, serverless, servlets

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/appengine-java-standard)
- [README](https://github.com/GoogleCloudPlatform/appengine-java-standard/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/appengine-java-standard/issues)
- [Releases](https://github.com/GoogleCloudPlatform/appengine-java-standard/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
