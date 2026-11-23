# corretto/hotpatch-for-apache-log4j2

- Company: Amazon
- GitHub account: [https://github.com/corretto](https://github.com/corretto)
- Mapping status: official-directory-listed
- Repository: [corretto/hotpatch-for-apache-log4j2](https://github.com/corretto/hotpatch-for-apache-log4j2)
- Default branch: main
- README: [Open upstream README](https://github.com/corretto/hotpatch-for-apache-log4j2/blob/main/README.md)
- README blob SHA: 1c407d028047e6e7910ddb37976896fcc6840a81
- Repository ID: 437426386
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An  agent to hotpatch the log4j RCE from CVE-2021-44228.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:13:50+00:00

### Short excerpt (up to 100 words)

> This is a tool which injects a Java agent into a running JVM process. The agent will attempt to patch the `lookup()` method of all loaded `org.apache.logging.log4j.core.lookup.JndiLookup` instances to unconditionally return the string "Patched JndiLookup::lookup()". It is designed to address the CVE-2021-44228 remote code execution vulnerability in Log4j without restarting the Java process. This tool will also address CVE-2021-45046. This has been currently only tested with JDK 8, 11, 15 and 17 on Linux! To build on linux, mac and Windows subsystem for linux ./gradlew build To build on Windows .\gradlew.bat build Depending on the platform you are building. This

### README headings

- Log4jHotPatch
- Building
- Gradle
- Maven
- Running
- Running the static agent
- Testing the agent
- Known issues

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 806,949 |
| Shell | 5,949 |
| HTML | 5,786 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build.gradle (capture: captured)
- pom.xml (capture: captured) — dependency clues: hotpatch-for-apache-log4j2, jdk.tools, maven-gpg-plugin, maven-jar-plugin, nexus-staging-maven-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 496
- Forks at capture: 72
- Last updated: 2026-11-19T22:25:15Z
- Last pushed: 2022-10-24T02:25:53Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/corretto/hotpatch-for-apache-log4j2)
- [README](https://github.com/corretto/hotpatch-for-apache-log4j2/blob/main/README.md)
- [Issues](https://github.com/corretto/hotpatch-for-apache-log4j2/issues)
- [Releases](https://github.com/corretto/hotpatch-for-apache-log4j2/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
