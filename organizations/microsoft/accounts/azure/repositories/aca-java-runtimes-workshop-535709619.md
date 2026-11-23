# Azure/aca-java-runtimes-workshop

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/aca-java-runtimes-workshop](https://github.com/Azure/aca-java-runtimes-workshop)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/aca-java-runtimes-workshop/blob/main/README.md)
- README blob SHA: 04835e4b947f2441ab6de2c4ad7c02485c104cf6
- Repository ID: 535709619
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Host the code and the documentation of the Azure Container Apps workshop for Java runtimes (Quarkus, Micronaut, Spring Boot)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:34:33+00:00

### Short excerpt (up to 100 words)

> cd quarkus-app mvn test # Execute the tests mvn quarkus:dev # Execute the application curl 'localhost:8701/quarkus' # Invokes the hello endpoint To build a native application (you need GraalVM installed): mvn -Pnative clean package ./target/*-runner To build a Docker image with the native application (you need to build the native image on Linux): docker build -t quarkus-app-native -f src/main/docker/Dockerfile.native . cd micronaut-app mvn test # Execute the tests docker compose -f infrastructure/postgres.yaml up mvn mn:run # Execute the application curl 'localhost:8702/micronaut' # Invokes the hello endpoint To build a native application (you need GraalVM installed): mvn package -Dpackaging=native-image ./target/micronaut-app To

### README headings

- Azure Container Apps Java Runtimes Workshop
- Quarkus
- Micronaut
- Spring Boot
- Contributing
- Trademarks

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HTML | 245,914 |
| Java | 33,380 |
| Shell | 28,360 |
| Batchfile | 7,680 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: parent
- docs/pom.xml (capture: captured) — dependency clues: asciidoctor-maven-plugin, asciidoctorj-diagram, asciidoctorj-diagram-plantuml, docs, plantuml, plantuml-maven-plugin
- micronaut-app/pom.xml (capture: captured) — dependency clues: jakarta.annotation-api, junit-jupiter, junit-jupiter-api, junit-jupiter-engine, logback-classic, maven-compiler-plugin, micronaut-app, micronaut-data-hibernate-jpa, micronaut-data-processor, micronaut-graal, micronaut-http-client, micronaut-http-server-netty, micronaut-http-validation, micronaut-inject, micronaut-inject-java, micronaut-jackson-databind, micronaut-jdbc-hikari, micronaut-maven-plugin, micronaut-parent, micronaut-test-junit5
- quarkus-app/pom.xml (capture: captured) — dependency clues: ${quarkus.platform.artifact-id}, maven-compiler-plugin, maven-failsafe-plugin, maven-surefire-plugin, parent, quarkus-app, quarkus-arc, quarkus-hibernate-orm, quarkus-hibernate-orm-panache, quarkus-jdbc-postgresql, quarkus-junit5, quarkus-maven-plugin, quarkus-resteasy, quarkus-resteasy-jsonb, rest-assured
- springboot-app/pom.xml (capture: captured) — dependency clues: junit-jupiter, postgresql, spring-boot-maven-plugin, spring-boot-starter-data-jpa, spring-boot-starter-parent, spring-boot-starter-test, spring-boot-starter-web, springboot-app, testcontainers-bom
- scripts/jmeter/pom.xml (capture: captured) — dependency clues: jmeter-maven-plugin, jmeter-scripts

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 17
- Forks at capture: 26
- Last updated: 2026-08-31T06:42:19Z
- Last pushed: 2026-09-14T21:18:42Z
- Topics: azure, container-apps, java, micronaut, quarkus, runtimes, spring-boot, workshop

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/aca-java-runtimes-workshop)
- [README](https://github.com/Azure/aca-java-runtimes-workshop/blob/main/README.md)
- [Issues](https://github.com/Azure/aca-java-runtimes-workshop/issues)
- [Releases](https://github.com/Azure/aca-java-runtimes-workshop/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
