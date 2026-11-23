# Guava

<sub>Company: Alphabet / Google · Repository: [google/guava](https://github.com/google/guava) · Default branch: `master` · Review status: **README reviewed**</sub>

## At a glance

Guava is a collection of Google Core Libraries for Java. The README describes reusable collection types, immutable collections, a graph library and utility functionality for common programming tasks.

**Problem it addresses:** Java applications frequently need common data structures and utilities beyond the language's basic standard library. Guava groups a broad set of reusable abstractions behind a versioned library that can be consumed by Java and Android projects.

## Library coverage

The README explicitly mentions:

- **Additional collection types:** multimap and multiset.
- **Immutable collections:** collection implementations designed to be immutable.
- **Graph library:** graph data structures and related APIs.
- **Concurrency utilities:** helpers for concurrent programming.
- **I/O utilities:** common input/output helpers.
- **Hashing:** hash-related functionality.
- **Primitive and string utilities:** reusable helper functionality for everyday Java code.

The README describes Guava as widely used within Google and by many other companies.

## JRE and Android flavours

The README documents two flavours:

| Flavour | Compatibility described in README |
|---|---|
| JRE | JDK 1.8 or higher |
| Android | Android-compatible version for Android or libraries that need Android compatibility |

The README says the Android flavour can also run on a JRE but recommends the JRE flavour there for performance and protection against hash flooding.

## Dependency management

Guava is published with Maven coordinates:

- Group ID: `com.google.guava`
- Artifact ID: `guava`

The README gives both Maven and Gradle examples. It also distinguishes between depending on Guava for internal implementation use (`implementation`) and exposing Guava types through a library's public API (`api`). Select the dependency configuration based on whether downstream consumers need the Guava types in the exported API.

## Technology profile

| Area | README-supported details |
|---|---|
| Main language / ecosystem | Java |
| JRE flavour | JDK 8+ |
| Android flavour | Android-compatible library |
| Maven coordinates | `com.google.guava:guava` |
| Build integration examples | Maven and Gradle |
| Main library areas | Collections, graphs, concurrency, I/O, hashing, primitives and strings |

This page summarizes the published library and its README-facing integration. It does not attempt to list every package or API class in the full source tree.

## Where it is useful

- Standardizing common Java data structures across a codebase.
- Using immutable collection types where mutation should be constrained.
- Working with graph-like data through the included graph library.
- Reusing utilities for concurrency, hashing, I/O and primitive values.
- Sharing common Java library dependencies across services and Android-compatible modules.

## Adoption notes

Review the current Guava release notes and security advisories before upgrading. The README includes an explicit security reference concerning hash flooding and notes that the Android and JRE flavours may have different performance characteristics. Avoid exposing Guava types in a public API unless you intend to make that dependency part of the library contract.

## Upstream references

- [Repository](https://github.com/google/guava)
- [Primary README](https://github.com/google/guava/blob/master/README.md)
- [Releases](https://github.com/google/guava/releases)
- [Android Guava information](https://github.com/google/guava/wiki/Android)
- [Maven Central](https://central.sonatype.com/artifact/com.google.guava/guava)

**Evidence note:** README blob inspected: `9ce2e666ebc7763c386acd2c902860d5d3a3e465`.
