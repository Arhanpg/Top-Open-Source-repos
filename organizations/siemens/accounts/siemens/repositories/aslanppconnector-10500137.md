# siemens/ASLanPPConnector

- Company: Siemens
- GitHub account: [https://github.com/Siemens](https://github.com/Siemens)
- Mapping status: verified
- Repository: [siemens/ASLanPPConnector](https://github.com/siemens/ASLanPPConnector)
- Default branch: master
- README: [Open upstream README](https://github.com/siemens/ASLanPPConnector/blob/master/README.txt)
- README blob SHA: 1d56e63ed7dd7c248f4aa529869cf022f8aa0f72
- Repository ID: 10500137
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ASLan++ connector

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:42:10+00:00

### Short excerpt (up to 100 words)

> ASLanPPConnector ================ Translator from the ASLan++ specification language to ASLan (and back), developed in the AVANTSSAR and SPaCIoS EU projects RUNNING THE TRANSLATOR ====================== $ java -jar aslanpp-connector.jar -h for initial help. Example specifications, including the official case studies, may be found at http://www.avantssar.eu/index.php?option=com_content&task=view&id=19&Itemid=40 GETTING STARTED WITH THE SOURCES ================================ The source code of the translator is located under the "src" folder. The translator is written in Java and uses ANTLR and StringTemplate libraries. You will need maven for building it and you can use Eclipse for editing the code. Building the translator Go into the "src" folder and run

### README headings

- Copyright 2010-2013 (c) IeAT, Siemens AG, AVANTSSAR and SPaCIoS consortia.
- Licensed under the Apache License, Version 2.0 (the "License");
- you may not use this file except in compliance with the License.
- You may obtain a copy of the License at
- http://www.apache.org/licenses/LICENSE-2.0
- Unless required by applicable law or agreed to in writing, software
- distributed under the License is distributed on an "AS IS" BASIS,
- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
- See the License for the specific language governing permissions and
- limitations under the License.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 1,628,076 |
| GAP | 73,255 |
| HTML | 55,778 |
| Shell | 25,815 |
| Ruby | 462 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/pom.xml (capture: captured) — dependency clues: aslanpp-everything, junit, log4j, maven-compiler-plugin, maven-jar-plugin, maven-javadoc-plugin, maven-source-plugin, tools
- src/aslan-backends/pom.xml (capture: captured) — dependency clues: args4j, aslan-backends, aslanpp-everything, maven-assembly-plugin, maven-jar-plugin
- src/aslan-commons/pom.xml (capture: captured) — dependency clues: antlr-runtime, args4j, aslan-commons, aslanpp-everything
- src/aslan-core/pom.xml (capture: captured) — dependency clues: antlr, antlr-runtime, antlr3-maven-plugin, aslan-commons, aslan-core, aslanpp-everything, gunit, maven-assembly-plugin, maven-gunit-plugin, maven-resources-plugin, stringtemplate, xercesImpl
- src/aslan-xml-wsclient/pom.xml (capture: captured) — dependency clues: args4j, aslan-commons, aslan-xml-client, aslan-xml-wsclient, aslanpp-everything, maven-assembly-plugin, maven-jar-plugin
- src/aslan-xml/pom.xml (capture: captured) — dependency clues: ${project.artifactId}, args4j, aslan-commons, aslan-core, aslan-xml, aslanpp-everything, cargo-maven2-plugin, commons-io, commons-lang, enunciate-rt, jaxb-api, jaxws-api, jsr181, jsr181-api, jsr311-api, maven-assembly-plugin, maven-enunciate-plugin, maven-install-plugin, maven-jar-plugin, maven-jetty-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 2
- Last updated: 2023-01-28T14:42:41Z
- Last pushed: 2015-04-07T12:29:21Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/siemens/ASLanPPConnector)
- [README](https://github.com/siemens/ASLanPPConnector/blob/master/README.txt)
- [Issues](https://github.com/siemens/ASLanPPConnector/issues)
- [Releases](https://github.com/siemens/ASLanPPConnector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
