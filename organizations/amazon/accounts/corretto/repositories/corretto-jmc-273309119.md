# corretto/corretto-jmc

- Company: Amazon
- GitHub account: [https://github.com/corretto](https://github.com/corretto)
- Mapping status: official-directory-listed
- Repository: [corretto/corretto-jmc](https://github.com/corretto/corretto-jmc)
- Default branch: master
- README: [Open upstream README](https://github.com/corretto/corretto-jmc/blob/master/README.md)
- README blob SHA: 209951148c2f9025a9b71bf6548c1648fc5d8f4f
- Repository ID: 273309119
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A build of JDK Mission Control (JMC) by the Corretto team.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:13:47+00:00

### Short excerpt (up to 100 words)

> *JMC for Corretto* is a build of JDK Mission Control (JMC) by the Corretto team. It tracks the latest stable JMC release with extra patches to support the usage of the JDK Flight Recorder feature in Corretto releases including: * Corretto 8.262.y.z or later * Corretto 11.0.x.y.z or later Check out the JMC README.md for more project details. To contribute to the JMC project in the OpenJDK community, please refer to the OpenJDK JMC contribution wiki. JMC for Corretto is supported on the following platforms: * Linux (w/ GTK+ 3), x64 * macOS 10.10 or later, x64 * Windows 7

### README headings

- JMC for Corretto
- Use JMC for Corretto
- Supported platforms
- Download
- Install and launch JMC
- Build JMC for Corretto
- Prerequisites
- Build wrapper
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 14,092,596 |
| HTML | 2,204,136 |
| XSLT | 22,161 |
| Shell | 21,299 |
| JavaScript | 7,919 |
| Batchfile | 7,669 |
| CSS | 6,365 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/pom.xml (capture: captured) — dependency clues: buildnumber-maven-plugin, directory-maven-plugin, flatten-maven-plugin, maven-deploy-plugin, maven-enforcer-plugin, maven-resources-plugin, missioncontrol, platform-definition-2020-03, platform-definition-2020-06, platform-definition-2020-09, platform-definition-2020-12, platform-definition-2021-03, spotbugs-maven-plugin, spotless-maven-plugin, target-platform-configuration, tycho-compiler-plugin, tycho-maven-plugin, tycho-p2-repository-plugin, tycho-packaging-plugin
- src/agent/pom.xml (capture: captured) — dependency clues: agent, asm, asm-commons, asm-util, junit, maven-enforcer-plugin, maven-failsafe-plugin, maven-gpg-plugin, maven-jar-plugin, maven-resources-plugin, maven-shade-plugin, maven-surefire-plugin, nexus-staging-maven-plugin, spotless-maven-plugin
- src/application/pom.xml (capture: captured) — dependency clues: common, common.test, flightrecorder, flightrecorder.rules, flightrecorder.rules.jdk, flightrecorder.serializers, flightrecorder.test, jacoco-maven-plugin, jdp, missioncontrol, missioncontrol.application, target-platform-configuration
- src/core/pom.xml (capture: captured) — dependency clues: build-helper-maven-plugin, directory-maven-plugin, flatten-maven-plugin, maven-bundle-plugin, maven-gpg-plugin, maven-jar-plugin, maven-javadoc-plugin, maven-resources-plugin, maven-source-plugin, missioncontrol.core, spotless-maven-plugin
- src/releng/pom.xml (capture: captured) — dependency clues: missioncontrol, missioncontrol.releng
- src/application/coverage/pom.xml (capture: captured) — dependency clues: coverage, jacoco-maven-plugin, missioncontrol.application, org.openjdk.jmc.alert, org.openjdk.jmc.attach, org.openjdk.jmc.browser, org.openjdk.jmc.browser.attach, org.openjdk.jmc.browser.jdp, org.openjdk.jmc.browser.uitest, org.openjdk.jmc.commands, org.openjdk.jmc.console.jconsole, org.openjdk.jmc.console.jconsole.uitest, org.openjdk.jmc.console.pde, org.openjdk.jmc.console.persistence, org.openjdk.jmc.console.persistence.uitest, org.openjdk.jmc.console.twitter, org.openjdk.jmc.console.ui, org.openjdk.jmc.console.ui.diagnostic, org.openjdk.jmc.console.ui.mbeanbrowser, org.openjdk.jmc.console.ui.notification

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 34
- Forks at capture: 6
- Last updated: 2026-08-13T06:43:19Z
- Last pushed: 2021-11-11T00:35:18Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/corretto/corretto-jmc)
- [README](https://github.com/corretto/corretto-jmc/blob/master/README.md)
- [Issues](https://github.com/corretto/corretto-jmc/issues)
- [Releases](https://github.com/corretto/corretto-jmc/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
