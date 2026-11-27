# FreeRTOS/FreeRTOS-Plus-TCP

- Company: Amazon
- Account: freertos
- Repository: https://github.com/FreeRTOS/FreeRTOS-Plus-TCP
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:14:09+00:00

## Project purpose

FreeRTOS-Plus-TCP is a lightweight TCP/IP stack for FreeRTOS. It provides a familiar Berkeley sockets interface, making it as simple to use and learn as possible. FreeRTOS-Plus-TCP's features and RAM footprint are fully scalable, making FreeRTOS-Plus-TCP equally applicable to smaller lower throughput microcontrollers as well as larger higher throughput microprocessors.

## Why this project is used

FreeRTOS-Plus-TCP library repository. +TCP files only. Submoduled into https://github.com/FreeRTOS/FreeRTOS and various other repos.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C, CMake, Python, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: GenerateOriginalFiles.py, source/FreeRTOS_ARP.c, source/FreeRTOS_BitConfig.c, source/FreeRTOS_DHCP.c

## Setup and usage

- Getting started: The easiest way to use version 4.0.0 and later of FreeRTOS-Plus-TCP is to refer the Getting started Guide (found here)
- Getting started: Another way is to start with the pre-configured IPv4 Windows Simulator demo (found in this directory) or IPv6 Multi-endpoint Windows Simulator demo (found in this directory). That way you will have the correct FreeRTOS source files included, and the correct include paths configured. Once a demo application is building and executing you can remove t
- Getting started: Additionally, for FreeRTOS-Plus-TCP source code organization refer to the Documentation, and API Reference.

## Limitations and caveats

- Generating pre V3.0.0 folder structure for backward compatibility:: If you wish to continue using a version earlier than V3.0.0 i.e. continue to use your existing source code organization, a script is provided to generate the folder structure similar to this.
- Generating pre V3.0.0 folder structure for backward compatibility:: **Note:** After running the script, while the .c files will have same names as the pre V3.0.0 source, the files in the include directory will have different names and the number of files will differ as well. This should, however, not pose any problems to most projects as projects generally include all files in a given directory.
- Generating pre V3.0.0 folder structure for backward compatibility:: Running the script to generate pre V3.0.0 folder structure:
- Generating pre V3.0.0 folder structure for backward compatibility:: For running the script, you will need Python version > 3.7. You can download/install it from here.
- Generating pre V3.0.0 folder structure for backward compatibility:: Once python is downloaded and installed, you can verify the version from your terminal/command window by typing python --version.
- Generating pre V3.0.0 folder structure for backward compatibility:: To run the script, you should switch to the FreeRTOS-Plus-TCP directory
- Generating pre V3.0.0 folder structure for backward compatibility:: Then run python /GenerateOriginalFiles.py.

## Evidence and provenance

- README: https://github.com/FreeRTOS/FreeRTOS-Plus-TCP/blob/main/README.md
- README SHA: 1a669d14cb3141408049b6c93fcbb44664202407
- Manifests: CMakeLists.txt, source/CMakeLists.txt, test/CMakeLists.txt, tools/CMakeLists.txt, source/portable/CMakeLists.txt, test/build-combination/CMakeLists.txt
- Sampled source files: GenerateOriginalFiles.py, source/FreeRTOS_ARP.c, source/FreeRTOS_BitConfig.c, source/FreeRTOS_DHCP.c
- Git tree state: captured
- Evidence fingerprint: ddd5de716405e2506b24b9850add296188d2ec2b6374bea2355f29fad15df099

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
