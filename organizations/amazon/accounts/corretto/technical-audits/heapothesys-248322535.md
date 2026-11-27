# corretto/heapothesys

- Company: Amazon
- Account: corretto
- Repository: https://github.com/corretto/heapothesys
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:33:14+00:00

## Project purpose

Heapothesys (/hɪˈpɒθɪsɪs/) is a collection of JVM garbage collection workloads developed by the Amazon Corretto team. These workloads are intended to be useful in helping to compare alternative garbage collection algorithms and configuration choices, helping to evaluate proposed improvements to garbage collection algorithms and implementations, and helping to detect garbage collection performance and latency regressions.

## Why this project is used

Heapothesys /hɪˈpɒθɪsɪs/ is a heap allocation JVM benchmark developed by the Amazon Corretto team.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: HyperAlloc, MutabilityDetector4FindBugs, apache-rat-plugin, build-helper-maven-plugin, exec-maven-plugin, extremem, hamcrest-core, jacoco-maven-plugin, jdepend-maven-plugin, jol-core, junit-jupiter, license-maven-plugin, maven-antrun-plugin, maven-assembly-plugin, maven-changes-plugin, maven-clean-plugin, maven-compiler-plugin, maven-dependency-plugin, maven-dependency-versions-check-plugin
                    , maven-deploy-plugin, maven-enforcer-plugin, maven-failsafe-plugin, maven-filtering, maven-help-plugin, maven-install-plugin, maven-jar-plugin, maven-javadoc-plugin, maven-jdeprscan-plugin, maven-jdeps-plugin, maven-jxr-plugin, maven-pmd-plugin, maven-project-info-reports-plugin, maven-release-plugin, maven-resources-plugin, maven-scm-plugin, maven-shade-plugin, maven-site-plugin, maven-source-plugin, maven-surefire-plugin, maven-toolchains-plugin, maven-war-plugin, mockito-core, pitest-maven, spotbugs-maven-plugin, tidy-maven-plugin, versions-maven-plugin
- Build/package tools: Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: Extremem/src/main/java/com/amazon/corretto/benchmark/extremem/Main.java, Extremem/src/main/java/com/amazon/corretto/benchmark/extremem/AbsoluteTime.java, Extremem/src/main/java/com/amazon/corretto/benchmark/extremem/Actor.java, Extremem/src/main/java/com/amazon/corretto/benchmark/extremem/Arraylet.java

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/corretto/heapothesys/blob/master/README.md
- README SHA: f636654225ccadb9a87e23dae4679f39c4539783
- Manifests: Extremem/Makefile, Extremem/pom.xml, HyperAlloc/pom.xml, Extremem/src/Makefile, Extremem/src/main/Makefile, Extremem/src/test/Makefile
- Sampled source files: Extremem/src/main/java/com/amazon/corretto/benchmark/extremem/Main.java, Extremem/src/main/java/com/amazon/corretto/benchmark/extremem/AbsoluteTime.java, Extremem/src/main/java/com/amazon/corretto/benchmark/extremem/Actor.java, Extremem/src/main/java/com/amazon/corretto/benchmark/extremem/Arraylet.java
- Git tree state: captured
- Evidence fingerprint: 16775c7fd639a9de58a9fa88a5ac475c20be9c7730f9df9218e9959e656347d8

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
