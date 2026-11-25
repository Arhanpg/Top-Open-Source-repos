# aws/Device-Defender-for-AWS-IoT-embedded-sdk

- Company: Amazon
- Account: aws
- Repository: https://github.com/aws/Device-Defender-for-AWS-IoT-embedded-sdk
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:53:47+00:00

## Project purpose

**API Documentation Pages for current and previous releases of this library can be found here**

## Why this project is used

Client library for using AWS IoT Defender service on embedded devices

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

Architecture is not interpreted in evidence-only mode. Sampled source files: source/defender.c, source/include/defender.h, source/include/defender_config_defaults.h

## Setup and usage

No setup information established.

## Limitations and caveats

- Platform Prerequisites: - For running unit tests:
- Platform Prerequisites: - **C90 compiler** like gcc.
- Platform Prerequisites: - **CMake 3.13.0 or later**.
- Platform Prerequisites: - **Ruby 2.0.0 or later** is additionally required for the CMock test
- Platform Prerequisites: framework (that we use).
- Platform Prerequisites: - For running the coverage target, **gcov** and **lcov** are additionally

## Evidence and provenance

- README: https://github.com/aws/Device-Defender-for-AWS-IoT-embedded-sdk/blob/main/README.md
- README SHA: 1caef543f48b954da67759b9f84373b67b3e28a6
- Manifests: CMakeLists.txt, test/CMakeLists.txt, test/unit-test/CMakeLists.txt, test/cbmc/proofs/Defender_GetTopic/Makefile, test/cbmc/proofs/Defender_MatchTopic/Makefile
- Sampled source files: source/defender.c, source/include/defender.h, source/include/defender_config_defaults.h
- Git tree state: captured
- Evidence fingerprint: 271b2baea12120f304a69a9efc89ea362cfd07e4d96f1547cefc1390c32c22a2

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
