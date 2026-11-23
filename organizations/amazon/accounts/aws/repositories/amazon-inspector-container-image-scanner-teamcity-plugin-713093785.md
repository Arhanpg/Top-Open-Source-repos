# aws/amazon-inspector-container-image-scanner-teamcity-plugin

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-inspector-container-image-scanner-teamcity-plugin](https://github.com/aws/amazon-inspector-container-image-scanner-teamcity-plugin)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-inspector-container-image-scanner-teamcity-plugin/blob/main/README.md)
- README blob SHA: d33cc1e1ff58e15e45bb23fcf41dd77749263b67
- Repository ID: 713093785
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:41:26+00:00

### Short excerpt (up to 100 words)

> This plugin gives you the ability to add Amazon Inspector vulnerability scans to your pipeline. These scans produce detailed reports at the end of your build so you can investigate and remediate risk before deployment. These scans can also be configured to pass or fail pipeline executions based on the number and severity of vulnerabilities detected. Amazon Inspector is a vulnerability management service offered by AWS that scans container images for both operating system and programming language package vulnerabilities based on CVEs. For more information on Amazon Inspector’s CI/CD integration, see Integrating Amazon Inspector scans into your CI/CD pipeline. For

### README headings

- No headings captured

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 109,187 |
| HTML | 40,988 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- amazon-inspector-image-scanner/pom.xml (capture: captured) — dependency clues: amazon-inspector-image-scanner, aspectjweaver, maven-compiler-plugin, teamcity-sdk-maven-plugin
- amazon-inspector-image-scanner/amazon-inspector-image-scanner-agent/pom.xml (capture: captured) — dependency clues: *, agent-api, amazon-inspector-image-scanner, amazon-inspector-image-scanner-agent, amazon-inspector-image-scanner-common, apache-client, aws-json-protocol, bom, commons-codec, gson, inspectorscan, javax.annotation-api, junit, license-maven-plugin, lombok, maven-compiler-plugin, maven-resources-plugin, mockito-core, opencsv, sts
- amazon-inspector-image-scanner/amazon-inspector-image-scanner-common/pom.xml (capture: captured) — dependency clues: amazon-inspector-image-scanner, amazon-inspector-image-scanner-common
- amazon-inspector-image-scanner/amazon-inspector-image-scanner-server/pom.xml (capture: captured) — dependency clues: *, amazon-inspector-image-scanner, amazon-inspector-image-scanner-common, amazon-inspector-image-scanner-server, server-api, server-web-api, tests-support
- amazon-inspector-image-scanner/build/pom.xml (capture: captured) — dependency clues: amazon-inspector-image-scanner, amazon-inspector-image-scanner-agent, amazon-inspector-image-scanner-common, amazon-inspector-image-scanner-server, build, maven-assembly-plugin, replacer

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 2
- Last updated: 2026-05-14T14:38:18Z
- Last pushed: 2026-04-01T17:22:31Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-inspector-container-image-scanner-teamcity-plugin)
- [README](https://github.com/aws/amazon-inspector-container-image-scanner-teamcity-plugin/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-inspector-container-image-scanner-teamcity-plugin/issues)
- [Releases](https://github.com/aws/amazon-inspector-container-image-scanner-teamcity-plugin/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
