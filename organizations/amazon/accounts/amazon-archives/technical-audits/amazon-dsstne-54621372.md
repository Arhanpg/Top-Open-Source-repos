# amazon-archives/amazon-dsstne

- Company: Amazon
- Account: amazon-archives
- Repository: https://github.com/amazon-archives/amazon-dsstne
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:04:49+00:00

## Project purpose

DSSTNE (pronounced "Destiny") is an open source software library for training and deploying recommendation models with sparse inputs, fully connected hidden layers, and sparse outputs. Models with weight matrices that are too large for a single GPU can still be trained on a single host. DSSTNE has been used at Amazon to generate personalized product recommendations for our customers at Amazon's scale. It is designed for production deployment of real-world applications which need to emphasize speed and scale over experimental flexibility.

## Why this project is used

Deep Scalable Sparse Tensor Network Engine (DSSTNE) is an Amazon developed library for building Deep Learning (DL) machine learning (ML) models

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, Cuda, Java, C, Python, Makefile, CMake, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: amazon-dsstne, guava, jcommander, junit, lombok, maven-antrun-plugin, maven-checkstyle-plugin, maven-clean-plugin, maven-compiler-plugin, maven-deploy-plugin, maven-install-plugin, maven-jar-plugin, maven-resources-plugin, maven-surefire-plugin, native-maven-plugin, slf4j-api
- Build/package tools: Docker build configuration, Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/amazon/dsstne/utils/main.cpp, tst/unittests/main.cpp, java/src/main/java/com/amazon/dsstne/data/DenseNNDataSet.java, java/src/main/java/com/amazon/dsstne/data/DenseWeightedNNDataSet.java

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/amazon-archives/amazon-dsstne/blob/master/README.md
- README SHA: 02c46cd4abf452a2dcfc0db0526e0292aec915ab
- Manifests: Dockerfile, Makefile, java/Makefile, java/pom.xml, python/Makefile, python/setup.py
- Sampled source files: src/amazon/dsstne/utils/main.cpp, tst/unittests/main.cpp, java/src/main/java/com/amazon/dsstne/data/DenseNNDataSet.java, java/src/main/java/com/amazon/dsstne/data/DenseWeightedNNDataSet.java
- Git tree state: captured
- Evidence fingerprint: ef8252109f8d8a994422d54c1cb13a75f71affa8bfc5a31bdb40df64dd650bff

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
