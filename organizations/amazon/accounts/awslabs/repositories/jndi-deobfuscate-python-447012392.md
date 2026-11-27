# awslabs/jndi-deobfuscate-python

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/jndi-deobfuscate-python](https://github.com/awslabs/jndi-deobfuscate-python)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/jndi-deobfuscate-python/blob/main/README.md)
- README blob SHA: 15cf3aeb5e3b08ecfc04731ceb9dd7f8f0bdbb31
- README bytes captured: 4703
- README truncated at capture limit: False
- Repository ID: 447012392
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Python module to deobfuscate 'JNDI' strings, used to exploit systems vulnerable to the recent series of Log4J vulnerabilities.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T03:27:42+00:00

### Short excerpt (up to 300 words)

> This tool processes text pip install jndi_deobfuscate

### README headings

- jndi_deobfuscate.py
- Purpose
- Who is this for
- Why is this necessary
- Examples of processed data:
- Example 1: Obscured Schema (lower/upper)
- Example 2: System Variables Inserted
- Example 3: Obscured Schema (Unresolved Variables)
- Example 4: Parsing example 1, where attack string is contained in a webserver log
- Installation:
- Usage:
- Process a text file for obfuscated JNDI strings:
- Process a single string:
- To view debug information, add the -v flag
- References:
- Known Issues:
- Only processes the first JNDI string identified, per line.
- Unit Tests Lacking
- Code is slow
- Code needs more error checking
- Code needs better documentation

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Purpose

> This tool processes text

### Getting started and usage: Installation:

> pip install jndi_deobfuscate

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 24,451 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: pytest, pytest-cov
- docs/Makefile (capture: captured)
- docs/requirements.txt (capture: captured) — dependency clues: myst-nb, sphinx-autoapi, sphinx-rtd-theme

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 3
- Forks at capture: 0
- Last updated: 2024-12-10T03:55:36Z
- Last pushed: 2023-10-30T17:13:54Z
- Topics: log-analysis, log4j, malware-analysis, reverse-engineering, security-tools, threat-intelligence

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/jndi-deobfuscate-python)
- [README](https://github.com/awslabs/jndi-deobfuscate-python/blob/main/README.md)
- [Issues](https://github.com/awslabs/jndi-deobfuscate-python/issues)
- [Releases](https://github.com/awslabs/jndi-deobfuscate-python/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
