# FreeRTOS/FreeRTOS-Kernel

- Company: Amazon
- Account: freertos
- Repository: https://github.com/FreeRTOS/FreeRTOS-Kernel
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:06:54+00:00

## Project purpose

This repository contains FreeRTOS kernel source/header files and kernel ports only. This repository is referenced as a submodule in FreeRTOS/FreeRTOS repository, which contains pre-configured demo application projects under FreeRTOS/Demo directory.

## Why this project is used

FreeRTOS kernel files only, submoduled into https://github.com/FreeRTOS/FreeRTOS and various other repos.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C, Assembly, CMake, Python, Batchfile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: .github/scripts/find_replace.sh, .github/scripts/kernel_checker.py, .github/scripts/manifest_updater.py, croutine.c

## Setup and usage

- Getting started: This repository contains FreeRTOS kernel source/header files and kernel
- Getting started: ports only. This repository is referenced as a submodule in
- Getting started: repository, which contains pre-configured demo application projects under
- Getting started: FreeRTOS/Demo directory.
- Getting started: The easiest way to use FreeRTOS is to start with one of the pre-configured demo
- Getting started: application projects. That way you will have the correct FreeRTOS source files
- Getting started: included, and the correct include paths configured. Once a demo application is
- Getting started: building and executing you can remove the demo application files, and start to

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/README.md
- README SHA: fabe5220b68cd16ca69adc0c4f9d0e4db40ab3fd
- Manifests: CMakeLists.txt, include/CMakeLists.txt, portable/CMakeLists.txt, examples/cmake_example/CMakeLists.txt, examples/coverity/CMakeLists.txt, portable/ThirdParty/GCC/RP2040/CMakeLists.txt
- Sampled source files: .github/scripts/find_replace.sh, .github/scripts/kernel_checker.py, .github/scripts/manifest_updater.py, croutine.c
- Git tree state: captured
- Evidence fingerprint: a29ff13d7b3c1fd0ff0f349b91f69a1a3c226bfe9b8df61ba0dc833609e154cc

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
