# apple/batch-processing-gateway

- Company: Apple
- Account: apple
- Repository: https://github.com/apple/batch-processing-gateway
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:33:29+00:00

## Project purpose

Batch Processing Gateway makes running Spark service on Kubernetes easy. It allows users to submit, examine and delete Spark apps on Kubernetes with intuitive API calls, without worrying much about what goes on behind the scene. It can also be configured with many Spark clusters to scale the service horizontally.

## Why this project is used

The gateway component to make Spark on K8s much easier for Spark users.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, Shell, Jinja, Python, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: aws-java-sdk-bom, aws-java-sdk-s3, aws-java-sdk-sts, bpg, commons-math3, dropwizard-auth, dropwizard-core, dropwizard-dependencies, dropwizard-testing, google-cloud-storage, h2, hibernate-validator, jackson-annotations, jakarta.validation-api, java-jwt, jdbi3-core, kubernetes-client, libraries-bom, maven-antrun-plugin, maven-compiler-plugin, maven-failsafe-plugin, maven-jar-plugin, maven-javadoc-plugin, maven-project-info-reports-plugin, maven-shade-plugin, maven-source-plugin, maven-surefire-plugin, metrics-core, metrics-jvm, micrometer-registry-statsd, postgresql, spark-network-common_2.13, swagger-core, swagger-integration, swagger-jaxrs2, testng
- Build/package tools: Docker build configuration, Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/main/bash/create-service-account.sh, src/main/java/com/apple/spark/api/DeleteSubmissionResponse.java, src/main/java/com/apple/spark/api/GetDriverInfoResponse.java, src/main/java/com/apple/spark/api/GetMySubmissionsResponse.java

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/apple/batch-processing-gateway/blob/main/README.md
- README SHA: 12aa3d2a9648d3d404f1613970b91697ed7177e9
- Manifests: Dockerfile, pom.xml
- Sampled source files: src/main/bash/create-service-account.sh, src/main/java/com/apple/spark/api/DeleteSubmissionResponse.java, src/main/java/com/apple/spark/api/GetDriverInfoResponse.java, src/main/java/com/apple/spark/api/GetMySubmissionsResponse.java
- Git tree state: captured
- Evidence fingerprint: 33bbcce10a60b2484cf0a3d06279579f0e89b04c8ba226beeaa64a41c6a74035

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
