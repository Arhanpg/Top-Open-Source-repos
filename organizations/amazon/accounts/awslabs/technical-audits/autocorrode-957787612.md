# awslabs/AutoCorrode

- Company: Amazon
- Account: awslabs
- Repository: https://github.com/awslabs/AutoCorrode
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:05:33+00:00

## Project purpose

AutoCorrode provides infrastructure for reasoning about imperative programs in Isabelle/HOL. It supports classical and separation logic and includes configurable and scalable custom automation, written in Standard ML. The core of AutoCorrode is language-agnostic, with a frontend and examples for the Rust-like language µRust.

## Why this project is used

Verification infrastructure for the Isabelle/HOL interactive proof assistant

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Isabelle, Scala, Python, Standard ML, Makefile, Shell, TeX, OCaml
- Frameworks/libraries: Unknown / not established
- Dependency names: mcp, prompt_toolkit, rich, zstandard
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: Fine_Grained_Timing_Panel/src/FineGrainedTiming.scala, Fine_Grained_Timing_Panel/src/FineGrainedTimingDockable.scala, Fine_Grained_Timing_Panel/src/FineGrainedTimingHierarchy.scala, Fine_Grained_Timing_Panel/src/FineGrainedTimingPlugin.scala

## Setup and usage

- Usage: You can interactively explore AutoCorrode using make jedit, which opens the AutoCorrode source in the Isabelle/jEdit GUI.
- Usage: To non-interactively check all material in AutoCorrode, run make build, which starts a batch-build in Isabelle.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/awslabs/AutoCorrode/blob/main/README.md
- README SHA: 2395a1596373f045ee5eb034a0ac04d679b89921
- Manifests: Makefile, Fine_Grained_Timing_Panel/Makefile, ic2/Makefile, ip/requirements.txt, iq/Makefile, ir/requirements.txt
- Sampled source files: Fine_Grained_Timing_Panel/src/FineGrainedTiming.scala, Fine_Grained_Timing_Panel/src/FineGrainedTimingDockable.scala, Fine_Grained_Timing_Panel/src/FineGrainedTimingHierarchy.scala, Fine_Grained_Timing_Panel/src/FineGrainedTimingPlugin.scala
- Git tree state: captured
- Evidence fingerprint: fc5ed842d3c721a0c546ec57e54c806cdfbe4d5c7d7853a9eeb0293b3dc7b1cb

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
