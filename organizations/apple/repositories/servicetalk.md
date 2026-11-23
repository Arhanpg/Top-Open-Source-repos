# ServiceTalk

- Company association: Apple
- Upstream GitHub account: [apple](https://github.com/apple)
- Repository: [apple/servicetalk](https://github.com/apple/servicetalk)
- Default branch: main
- README: [Open upstream README](https://github.com/apple/servicetalk/blob/main/README.adoc)
- Review status: README inspected and summarized
- README blob SHA: 2ca12f4b803747d10c98eb7640e5f1e179a637a3
- Relationship note: The repository is maintained under Apple's primary public GitHub organization.

## Project overview

A JVM network-application framework with APIs tailored to widely used service-to-service protocols, including HTTP and gRPC. The README positions it as a layer built on Netty that exposes networking and microservice capabilities without requiring every application to use lower-level Netty primitives.

## Features and capabilities documented by the README

- Server APIs for supported protocols, including HTTP/1.x and HTTP/2.x.
- Client-side features such as load balancing and service-discovery integration.
- Blocking and asynchronous programming models, allowing applications to adopt asynchronous control flow per route.
- Reactive Streams semantics for asynchronous backpressure and cancellation.
- Protocol-specific APIs and shared primitives for service-to-service communication.
- Gradle build, test and code-quality tasks, plus JaCoCo coverage reporting.

## Technology stack

Java/JVM; Netty; Gradle Wrapper; Maven Central distribution; Reactive Streams; JaCoCo; IntelliJ IDEA. The README states minimum supported JDK 8. Apple's project page identifies HTTP and gRPC among the supported protocol areas.

## Getting started

Add ServiceTalk modules from Maven Central and follow the official protocol-specific examples. For a source build, install JDK 8 or newer and run ./gradlew build. The README also documents ./gradlew idea and ./gradlew testCodeCoverageReport.

## Lifecycle, compatibility and operational considerations

The README says the project follows Semantic Versioning 2.0.0, but 0.x.y releases are not stable and may break API/ABI. Module package renaming is used for breaking changes to avoid runtime classpath conflicts. ServiceTalk is a framework built by the team that leads Netty; do not confuse it with Netty itself.

## Evaluation guidance

Check the current upstream release, dependency manifests, exact platform/toolchain requirements, licence and security guidance before adoption. This dossier summarizes the inspected README; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/apple/servicetalk)
- [README](https://github.com/apple/servicetalk/blob/main/README.adoc)
- [Issues](https://github.com/apple/servicetalk/issues)
- [Releases](https://github.com/apple/servicetalk/releases)

Evidence note: the README blob SHA identifies the upstream README revision inspected. Technology details not established by the README or official project page are left unspecified.
