# GoogleTest and GoogleMock

- **Company grouping:** Alphabet / Google
- **GitHub organization:** [google](https://github.com/google)
- **Repository:** [google/googletest](https://github.com/google/googletest)
- **Default branch:** master/main (verify from repository metadata)
- **README:** [Open upstream README](https://github.com/google/googletest/blob/master/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `b4e9b434fc86db0882a0ea7df0fface8497de718`

## Project overview

GoogleTest is Google's C++ testing framework. This repository combines the formerly separate GoogleTest and GoogleMock projects and provides test-writing, assertion and mocking capabilities for C++ software.

## Features and capabilities

- xUnit-style testing framework with automatic test discovery.
- Rich built-in assertions and support for user-defined assertions.
- Death tests for validating process termination and error-handling paths.
- Fatal and non-fatal failures to control whether a failing assertion stops a test.
- Value-parameterized and type-parameterized tests for varying input values and types.
- Options for selecting individual tests, specifying execution order and running tests in parallel.
- GoogleMock is maintained alongside GoogleTest in the combined repository.

## Technology stack

C++ testing framework. The inspected README announces release 1.18.0 and states that the 1.18.x branch requires at least C++17. Compiler, platform and build-tool support is governed by Google's foundational C++ support matrix.

## Getting started

The README recommends the GoogleTest User's Guide and GoogleTest Primer. Build instructions are in the nested googletest/README.md; check the exact release and current compiler matrix before configuring a project.

## Lifecycle and operational considerations

The README says Google's CI uses internal systems and points to a public supported compiler/platform/build-tool matrix. It also announces a planned Abseil dependency; confirm the actual dependency set in the release's manifests.

## Evaluation guidance

Check the exact release, manifests, supported platforms, licence and maintenance policy before adopting the project. This dossier is based on the upstream README, not a full source-code, vulnerability or performance audit.

## Upstream references

- [Repository](https://github.com/google/googletest)
- [README](https://github.com/google/googletest/blob/master/README.md)
- [Issues](https://github.com/google/googletest/issues)
- [Releases](https://github.com/google/googletest/releases)

*Evidence note: README blob SHA identifies the upstream version inspected. Technology claims are limited to the README's evidence; implementation details not established by that source are not inferred.*
