# corretto/amazon-corretto-crypto-provider

- Company: Amazon
- Account: corretto
- Repository: https://github.com/corretto/amazon-corretto-crypto-provider
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:47:24+00:00

## Project purpose

The Amazon Corretto Crypto Provider (ACCP) is a collection of high-performance cryptographic implementations exposed via the standard JCA/JCE interfaces. This means that it can be used as a drop in replacement for many different Java applications. (Differences from the default OpenJDK implementations are documented here.) As of 2.0.0, algorithms exposed by ACCP are primarily backed by AWS-LC's implementations.

## Why this project is used

The Amazon Corretto Crypto Provider is a collection of high-performance cryptographic implementations exposed via standard JCA/JCE interfaces.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, C++, CMake, Shell, Python, C
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle build file, Gradle Kotlin build file, CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: benchmarks/lib/src/jmh/java/com/amazon/corretto/crypto/provider/benchmarks/AesBase.java, benchmarks/lib/src/jmh/java/com/amazon/corretto/crypto/provider/benchmarks/AesCbcOneShot.java, benchmarks/lib/src/jmh/java/com/amazon/corretto/crypto/provider/benchmarks/AesCbcUpdate.java, benchmarks/lib/src/jmh/java/com/amazon/corretto/crypto/provider/benchmarks/AesCfbBase.java

## Setup and usage

- Installation: Installing via Maven or Gradle is the easiest way to get ACCP and ensure you
- Installation: will always have the most recent version. We strongly recommend you always pull
- Installation: in the latest version for best performance and bug-fixes.
- Installation: Whether you're using Maven, Gradle, or some other build system that also pulls
- Installation: packages from Maven Central, it's important to specify a classifier, otherwise,
- Installation: one would get an empty package. The possible classifiers are as follows:
- Installation: | Classifier | Support since version | FIPS support since version |
- Installation: |------------|-----------------------|----------------------------|

## Limitations and caveats

- Compatibility & Requirements: ACCP has the following requirements:
- Compatibility & Requirements: * JDK8 or newer (This includes both OracleJDK and Amazon Corretto)
- Compatibility & Requirements: * One of the platforms listed under Platform Support below
- Supported Platforms: "Supported" means the platform is tested in CI before every release. The two platforms get there
- Supported Platforms: differently, so the minimum version each row names is not the same kind of guarantee:
- Supported Platforms: * **Linux** is built and smoke-tested by the release pipeline itself, which pins its build image
- Supported Platforms: (currently Amazon Linux 2). "Minimum glibc" is the oldest glibc a published .so is linked
- Supported Platforms: against; glibc's symbol versioning is forward-only, so a host with an older glibc cannot load a

## Evidence and provenance

- README: https://github.com/corretto/amazon-corretto-crypto-provider/blob/main/README.md
- README SHA: 6e434e0c34130098c04a76cebb13fa94bf18f13a
- Manifests: build.gradle, CMakeLists.txt, benchmarks/lib/build.gradle.kts, CMake/trycompile/CMakeLists.txt, examples/gradle-kt-dsl/lib/build.gradle.kts
- Sampled source files: benchmarks/lib/src/jmh/java/com/amazon/corretto/crypto/provider/benchmarks/AesBase.java, benchmarks/lib/src/jmh/java/com/amazon/corretto/crypto/provider/benchmarks/AesCbcOneShot.java, benchmarks/lib/src/jmh/java/com/amazon/corretto/crypto/provider/benchmarks/AesCbcUpdate.java, benchmarks/lib/src/jmh/java/com/amazon/corretto/crypto/provider/benchmarks/AesCfbBase.java
- Git tree state: captured
- Evidence fingerprint: cd395f7efb07f03552ce8b185b38d985773b6feb1d39941d3b916cdbb673ed39

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
