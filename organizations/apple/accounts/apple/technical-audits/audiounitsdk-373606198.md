# apple/AudioUnitSDK

- Company: Apple
- Account: apple
- Repository: https://github.com/apple/AudioUnitSDK
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:56:59+00:00

## Project purpose

The AudioUnitSDK contains a set of base classes as well as utility sources required for Audio Unit development. These utility classes extend or wrap Core Audio API’s providing developers with the essential scaffolding to create audio effects, instruments, and generators on Apple platforms. They provide an easier to implement C++ class model wrapping the C framework APIs.

## Why this project is used

AudioUnit SDK

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, Objective-C, Objective-C++, C, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/AudioUnitSDK/AUBase.cpp, src/AudioUnitSDK/AUBuffer.cpp, src/AudioUnitSDK/AUBufferAllocator.cpp, src/AudioUnitSDK/AUEffectBase.cpp

## Setup and usage

No setup information established.

## Limitations and caveats

- Security: - Fixed out-of-bounds read in AUMIDIBase deserialization.

## Evidence and provenance

- README: https://github.com/apple/AudioUnitSDK/blob/main/readme.md
- README SHA: a984fbe0cbc0ef91fd53ae8a78adcecdde554b7b
- Manifests: none
- Sampled source files: src/AudioUnitSDK/AUBase.cpp, src/AudioUnitSDK/AUBuffer.cpp, src/AudioUnitSDK/AUBufferAllocator.cpp, src/AudioUnitSDK/AUEffectBase.cpp
- Git tree state: captured
- Evidence fingerprint: 7ca22e814b21eb3d2475cb944367e816c71a75596b08312a0e1ae8cc12dee9f5

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
