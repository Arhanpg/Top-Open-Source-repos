# aws/Device-Shadow-for-AWS-IoT-embedded-sdk

- Company: Amazon
- Account: aws
- Repository: https://github.com/aws/Device-Shadow-for-AWS-IoT-embedded-sdk
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:03:48+00:00

## Project purpose

**API Documentation Pages for current and previous releases of this library can be found here**

## Why this project is used

Client library for using AWS IoT Shadow service on embedded devices

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Unknown / not established
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: source/include/shadow.h, source/include/shadow_config_defaults.h, source/shadow.c

## Setup and usage

No setup information established.

## Limitations and caveats

- Platform Prerequisites: - For building the library, **CMake 3.13.0** or later and a **C90 compiler**.
- Platform Prerequisites: - For running unit tests, **Ruby 2.0.0** or later is additionally required for
- Platform Prerequisites: the CMock test framework (that we use).
- Platform Prerequisites: - For running the coverage target, **gcov** and **lcov** are additionally

## Evidence and provenance

- README: https://github.com/aws/Device-Shadow-for-AWS-IoT-embedded-sdk/blob/main/README.md
- README SHA: 3883d8387e8b95cac4ce017e1a867f161ddabac1
- Manifests: CMakeLists.txt, test/CMakeLists.txt, test/unit-test/CMakeLists.txt, test/cbmc/proofs/Shadow_AssembleTopicString/Makefile, test/cbmc/proofs/Shadow_MatchTopic/Makefile, test/cbmc/proofs/Shadow_MatchTopicString/Makefile
- Sampled source files: source/include/shadow.h, source/include/shadow_config_defaults.h, source/shadow.c
- Git tree state: captured
- Evidence fingerprint: 0d909e13cbe031240f53bb118ebadd10b3ffa1c50f986645546eb5629a8d19bb

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
