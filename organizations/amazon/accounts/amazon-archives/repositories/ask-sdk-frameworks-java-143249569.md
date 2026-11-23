# amazon-archives/ask-sdk-frameworks-java

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/ask-sdk-frameworks-java](https://github.com/amazon-archives/ask-sdk-frameworks-java)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/ask-sdk-frameworks-java/blob/master/README.md)
- README blob SHA: c6c9d916ed0241dd02c70e442892aa38b1c54379
- Repository ID: 143249569
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repository contains framework and plugin libraries for building Alexa Custom Skills in Java.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:29:02+00:00

### Short excerpt (up to 100 words)

> This repository contains framework and plugin libraries for building Alexa Custom Skills in Java. These plugins are not under active development, are experimental in nature, and are not recommended for use with production skills. The core Alexa Skills Kit SDK for Java is actively developed and supported and is recommended for these use cases. To get started with a new MVC project, see the maven archetype. * Model-View-Controller (MVC) Framework - adapts the MVC pattern to skills. Supports mapping requests by name/type to methods on controler classes and rendering responses from view scripts/templates. * MVC FreeMarker View Resolver - adds

### README headings

- Ask SDK Frameworks Java
- Getting Started
- Packages
- MVC Skill Samples
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 1,071,417 |
| JavaScript | 1,006 |
| FreeMarker | 790 |
| Shell | 747 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: ask-sdk-frameworks-pom, maven-compiler-plugin, maven-gpg-plugin, nexus-staging-maven-plugin
- ask-sdk-interaction-model-codegen/pom.xml (capture: captured) — dependency clues: ask-sdk, ask-sdk-interaction-model-codegen, ask-sdk-interaction-model-mapper, javapoet, junit, maven-assembly-plugin, maven-compiler-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-source-plugin, mockito-core, nexus-staging-maven-plugin
- ask-sdk-interaction-model-mapper/pom.xml (capture: captured) — dependency clues: ask-sdk-core, ask-sdk-interaction-model, ask-sdk-interaction-model-mapper, commons-cli, junit, maven-compiler-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-source-plugin, mockito-core, nexus-staging-maven-plugin
- ask-sdk-interaction-model/pom.xml (capture: captured) — dependency clues: ask-sdk-interaction-model, jackson-annotations, jackson-databind, junit, maven-compiler-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-source-plugin, nexus-staging-maven-plugin
- ask-sdk-maven-plugins/pom.xml (capture: captured) — dependency clues: ask-sdk-interaction-model-mapper, ask-sdk-maven-plugins, maven-compiler-plugin, maven-core, maven-gpg-plugin, maven-plugin-annotations, maven-plugin-api, maven-plugin-plugin, nexus-staging-maven-plugin
- ask-sdk-mvc-freemarker/pom.xml (capture: captured) — dependency clues: ask-sdk-mvc, ask-sdk-mvc-freemarker, freemarker, junit, maven-compiler-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-source-plugin, mockito-core, nexus-staging-maven-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 12
- Forks at capture: 11
- Last updated: 2023-01-28T18:24:15Z
- Last pushed: 2019-05-07T00:07:04Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/ask-sdk-frameworks-java)
- [README](https://github.com/amazon-archives/ask-sdk-frameworks-java/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/ask-sdk-frameworks-java/issues)
- [Releases](https://github.com/amazon-archives/ask-sdk-frameworks-java/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
