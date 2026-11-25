# SAP-samples/abap-cheat-sheets

- Company: SAP
- Account: SAP-samples
- Repository: https://github.com/SAP-samples/abap-cheat-sheets
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:18:32+00:00

## Project purpose

Explore ABAP syntax in a nutshell & executable examples · ·

## Why this project is used

Explore ABAP syntax in a nutshell supported by executable demo examples.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: ABAP, HTML, ABAP CDS
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: none

## Setup and usage

- 🎬 Getting Started with the Examples: The main focus of the ABAP cheat sheets is ABAP for Cloud Development. The examples in the *main* branch of the repository are designed to be imported into the _SAP Business AI Platform, ABAP environment_.
- 🎬 Getting Started with the Examples: For Standard ABAP, you can find examples in the other branches of the repository (note that except for specific examples, the example code there uses syntax that is also availabe in ABAP for Cloud Development) that you can import into your sandbox SAP system. Just select the appropriate version (*v757* stands for ABAP version 7.57). Check the infor
- 🎬 Getting Started with the Examples: - Some **DDIC artifacts**, such as database tables, are part of the repository. They are used by the examples to ensure self-contained examples. All artifacts must be imported for all examples to work.
- 🎬 Getting Started with the Examples: - Most examples are designed to **display some output in the ADT console**. Once successfully imported, you can **run** the examples in ADT by choosing *F9* to display the output in the ADT console. The programs included in the branches for classic ABAP can be executed with *F8*.
- 🎬 Getting Started with the Examples: - The examples **include descriptions and comments** in the code to provide explanations and set the context.
- 🎬 Getting Started with the Examples: - Note that only one user on the system can import this repository because all object names must be globally unique.
- 🎬 Getting Started with the Examples: - Regarding the examples to be imported into a system supporting classic ABAP (where Standard ABAP is supported), note the following: In most cases, the cheat sheet documents and examples focus on ABAP for Cloud Development. Therefore, the lower the ABAP release in your system, the fewer syntax options and examples are available. For example, the R
- 🎬 Getting Started with the Examples: - ABAP Release News for ABAP for Cloud Development. Note the ABAP release cycles listed there.

## Limitations and caveats

- ⚡ Known Issues: - Regarding possible code check warnings, e.g. for the many strings in the code, not using an ORDER BY clause, or messages regarding using SELECT *, the code deliberately avoids pragmas and pseudo comments in order to focus on the available ABAP syntax. See also the Disclaimer.
- ⚡ Known Issues: - Importing the main branch (and other branches of the GitHub repository) in a system other than the _SAP Business AI Platform, ABAP environment_ may cause errors in various cases. This may also be true when checking out various code snippets and example classes available in the ABAP cheat sheet documents. ABAP keywords, additions, and syntax optio
- ⚡ Known Issues: - If you encounter import problems with the XSLT/ST objects, try to manually paste the code from the 3 ...source.xml files (zdemo_abap_st_carrhtml, zdemo_abap_st_strhtml, zdemo_abap_xslt_fl) into the improperly imported objects and activate all inactive objects.

## Evidence and provenance

- README: https://github.com/SAP-samples/abap-cheat-sheets/blob/main/README.md
- README SHA: 6e89129882177b9067bde6352267a06a0df7788e
- Manifests: none
- Sampled source files: none
- Git tree state: captured
- Evidence fingerprint: 16d68e5d8b8814f46eba904a5f7cfe3798509e65fbb7bae3ad7cdd6e86b6e6ce

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
