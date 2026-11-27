# google/DAPLink-port

- Company: Alphabet (Google)
- Account: google
- Repository: https://github.com/google/DAPLink-port
- Default branch: master_udb
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:43:13+00:00

## Project purpose

----

## Why this project is used

----

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C, Assembly, Python, C++, Batchfile, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: bs4, enum34, fuzzywuzzy, intelhex, jsonschema, mbed-cli, mbed-ls, numpy, project_generator, pyOCD, pyelftools, pyexpect, pyserial, pyusb, pyyaml, requests
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: source/hic_hal/nuvoton/m48ssidae/StdDriver/src/m480_clk.c, source/hic_hal/nuvoton/m48ssidae/StdDriver/src/m480_fmc.c, source/hic_hal/nuvoton/m48ssidae/StdDriver/src/m480_gpio.c, source/hic_hal/nuvoton/m48ssidae/StdDriver/src/m480_rtc.c

## Setup and usage

No setup information established.

## Limitations and caveats

- Compatibility: There are many ARM microcontroller-based Hardware Interface Circuits (HICs) that DAPLink interface firmware runs on. These can be found as standalone boards (debugger) or as part of a development kit. Some branded circuits that are known to be IO compatible are:
- Compatibility: * Maxim Integrated MAX32625PICO based on MAX32625
- Compatibility: * Nuvoton Nu-Link2-Me based on M48SSIDAE
- Compatibility: * NXP LPC-Link2 based on LPC11U35 or LPC4322
- Compatibility: * NXP MCU-LINK on LPC55xx
- Compatibility: * NXP OpenSDA based on K20, K22, KL26Z and KL27Z
- Compatibility: * Segger J-Link OB based on Atmel SAM3U
- Compatibility: * STMicroelectronics ST-LINK/V2 (on NUCLEO boards) based on STM32F103CB

## Evidence and provenance

- README: https://github.com/google/DAPLink-port/blob/master_udb/README.md
- README SHA: 7c6126d47099872e4cfd266feed1bf75a18ffc55
- Manifests: requirements.txt, test/udb_integration_test/requirements.txt
- Sampled source files: source/hic_hal/nuvoton/m48ssidae/StdDriver/src/m480_clk.c, source/hic_hal/nuvoton/m48ssidae/StdDriver/src/m480_fmc.c, source/hic_hal/nuvoton/m48ssidae/StdDriver/src/m480_gpio.c, source/hic_hal/nuvoton/m48ssidae/StdDriver/src/m480_rtc.c
- Git tree state: captured
- Evidence fingerprint: 5babbb77ea3cfa0c749ec37e6791091111a6490549a6afe2b147159426120ed0

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
