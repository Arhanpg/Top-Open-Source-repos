# google/exposure-notifications-private-analytics-ingestion

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/exposure-notifications-private-analytics-ingestion](https://github.com/google/exposure-notifications-private-analytics-ingestion)
- Default branch: main
- README: [Open upstream README](https://github.com/google/exposure-notifications-private-analytics-ingestion/blob/main/README.md)
- README blob SHA: 5d197201fdf024519bb7ba0f391aa2f9f68301fd
- README bytes captured: 10218
- README truncated at capture limit: False
- Repository ID: 353855993
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repository contains implementation to process private data shares collected according to the Exposure Notification Private Analytics protocol. It assumes private data shares uploaded as done in the Exposure Notification Express template app. These documents contain encrypted packets using the Prio protocol. The pipeline implementation converts them into the format that downstream Prio data processing servers expect.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T06:31:31+00:00

### Short excerpt (up to 300 words)

> No README excerpt captured. Use the upstream README link.

### README headings

- Exposure Notification Private Analytics Ingestion
- Setup
- Multiple Maven modules
- Clone Submodules
- Useful Environment Variables
- Testing
- Unit Tests
- Integration Tests
- Running the Pipeline
- Locally
- In Google Cloud Dataflow
- From local build
- From Flex Template
- Building
- Building a Flex Template and Launch Container
- Contributing
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

No selected README section excerpts were captured.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 177,470 |
| HCL | 21,783 |
| Shell | 11,981 |
| JavaScript | 8,072 |
| Dockerfile | 1,451 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: auto-service-annotations, auto-value, avro, avro-compiler, avro-maven-plugin, enpa-ingestion, exec-maven-plugin, flatten-maven-plugin, gson, guava, hamcrest-core, hamcrest-library, joda-time, junit, libraries-bom, mockito-all, protobuf-java, slf4j-api, slf4j-jdk14, truth
- attestation/pom.xml (capture: captured) — dependency clues: auto-service, bcpkix-jdk15on, beam-runners-core-construction-java, beam-runners-direct-java, beam-sdks-java-core, build-helper-maven-plugin, enpa-ingestion, enpa-ingestion-attestation, enpa-ingestion-model, maven-compiler-plugin, protoc-jar-maven-plugin
- df-flex-template-base-image/Dockerfile (capture: captured)
- model/pom.xml (capture: captured) — dependency clues: auto-value, beam-sdks-java-core, enpa-ingestion, enpa-ingestion-model, firebase-admin, google-cloud-firestore, maven-compiler-plugin, maven-jar-plugin
- pipeline/pom.xml (capture: captured) — dependency clues: auto-service, avro-maven-plugin, beam-runners-core-construction-java, beam-runners-direct-java, beam-runners-google-cloud-dataflow-java, beam-sdks-java-core, beam-sdks-java-io-amazon-web-services, beam-sdks-java-io-google-cloud-platform, enpa-ingestion, enpa-ingestion-attestation, enpa-ingestion-attestation-impl, enpa-ingestion-model, enpa-ingestion-pipeline, exec-maven-plugin, firebase-admin, google-api-services-cloudkms, google-cloud-firestore, google-cloud-kms, jacoco-maven-plugin, jaxb-api
- config/firebase/package.json (capture: captured) — dependency clues: @firebase/testing, jest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 12
- Forks at capture: 5
- Last updated: 2026-07-21T09:16:30Z
- Last pushed: 2024-09-19T16:14:53Z
- Topics: exposure-notification, firestore, google-cloud-dataflow, prio

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/exposure-notifications-private-analytics-ingestion)
- [README](https://github.com/google/exposure-notifications-private-analytics-ingestion/blob/main/README.md)
- [Issues](https://github.com/google/exposure-notifications-private-analytics-ingestion/issues)
- [Releases](https://github.com/google/exposure-notifications-private-analytics-ingestion/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
