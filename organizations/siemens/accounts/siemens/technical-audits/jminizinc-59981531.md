# siemens/JMiniZinc

- Company: Siemens
- Account: Siemens
- Repository: https://github.com/siemens/JMiniZinc
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:03:08+00:00

## Project purpose

JMiniZinc is a Java interface to the constraint modeling language MiniZinc. It provides an API to generate MiniZinc models, to start MiniZinc compilers and solvers (which are not part of JMiniZinc), and to parse the output of solvers.

## Why this project is used

JMiniZinc

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, Shell, Batchfile
- Frameworks/libraries: Unknown / not established
- Dependency names: core, diag, jminizinc, junit, ui
- Build/package tools: Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: com.siemens.jminizinc.core/src/main/java/at/siemens/ct/common/utils/ArrayUtils.java, com.siemens.jminizinc.core/src/main/java/at/siemens/ct/common/utils/CollectionUtils.java, com.siemens.jminizinc.core/src/main/java/at/siemens/ct/common/utils/FileUtils.java, com.siemens.jminizinc.core/src/main/java/at/siemens/ct/common/utils/ListUtils.java

## Setup and usage

- Usage: You should be able to figure out quickly how to use JMiniZinc by looking at our JUnit tests, especially NQueensDemo.
- Usage: First you construct a MiniZinc model by adding Variables, Constraints etc. to a ModelBuilder,
- Usage: Then you add additional syntactical elements (e.g. a solving strategy) to a ModelWriter
- Usage: and let the resulting model be solved by an Executor.
- Usage: For the Executors to work, executables minizinc, mzn2fzn, ... should be available on your PATH.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/siemens/JMiniZinc/blob/master/README.md
- README SHA: cf542e03f97e51bdfda9b4d46d67304a8df94058
- Manifests: com.siemens.jminizinc.core/pom.xml, com.siemens.jminizinc.diag.ui/pom.xml, com.siemens.jminizinc.diag/pom.xml, com.siemens.jminizinc/pom.xml
- Sampled source files: com.siemens.jminizinc.core/src/main/java/at/siemens/ct/common/utils/ArrayUtils.java, com.siemens.jminizinc.core/src/main/java/at/siemens/ct/common/utils/CollectionUtils.java, com.siemens.jminizinc.core/src/main/java/at/siemens/ct/common/utils/FileUtils.java, com.siemens.jminizinc.core/src/main/java/at/siemens/ct/common/utils/ListUtils.java
- Git tree state: captured
- Evidence fingerprint: b840cb1b749a70f1caa6412431e4edb7ad0eed2383d7efa4bf02ae33997f8479

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
