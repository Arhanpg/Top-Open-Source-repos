# awslabs/ec2-spot-fleet-bamboo-plugin

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/ec2-spot-fleet-bamboo-plugin](https://github.com/awslabs/ec2-spot-fleet-bamboo-plugin)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/ec2-spot-fleet-bamboo-plugin/blob/master/README.md)
- README blob SHA: 045c4c041bf04e2f44de9eadc16111f55631b643
- README bytes captured: 20626
- README truncated at capture limit: False
- Repository ID: 99280178
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Plugin for Atlassian Bamboo, a continuous integration (CI) tool. The plugin allows users to associate an EC2 Spot Fleet with Bamboo to complete tasks as a part of the CI process.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T19:57:03+00:00

### Short excerpt (up to 300 words)

> Your security group must

### README headings

- Plugin setup/installation guide
- For Bamboo Production Use
- Read before using
- AWS account setup - before using the Fleet plugin for Bamboo you must set a few things up on your AWS account
- Create a user with the necessary permissions and credentials
- Create a security group with the necessary ports opened
- Remote Agent setup
- User Data Script
- Task and Fleet Setup
- For Plugin Development:

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Limitations and security: Create a security group with the necessary ports opened

> Your security group must

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 107,853 |
| Fluent | 2,614 |
| Shell | 770 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: AwsSpotFleetBambooPlugin, atlassian-bamboo-web, atlassian-plugins-osgi-testrunner, atlassian-spring-scanner-annotation, atlassian-spring-scanner-external-jar, atlassian-spring-scanner-maven-plugin, atlassian-spring-scanner-runtime, clover-maven-plugin, gson, javax.inject, jsr311-api, junit, maven-bamboo-plugin, mockito-all, powermock-api-mockito, powermock-module-junit4, powermock-module-junit4-common, powermock-reflect
- target/classes/META-INF/maven/com.atlassian.plugin/atlassian-spring-scanner-annotation/pom.xml (capture: captured) — dependency clues: atlassian-spring-scanner-annotation, atlassian-spring-scanner-parent, spring
- target/classes/META-INF/maven/com.atlassian.plugin/atlassian-spring-scanner-runtime/pom.xml (capture: captured) — dependency clues: atlassian-bamboo-api, atlassian-fisheye-api, atlassian-plugins-osgi, atlassian-spring-scanner-annotation, atlassian-spring-scanner-parent, atlassian-spring-scanner-runtime, bitbucket-api, commons-httpclient, commons-lang, confluence, guava, jira-core, junit, maven-compiler-plugin, mockito-all, org.eclipse.gemini.blueprint.core, spring, spring-core, spring-osgi-core, stash-api

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 6
- Last updated: 2022-09-01T17:24:27Z
- Last pushed: 2024-01-23T16:24:54Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/ec2-spot-fleet-bamboo-plugin)
- [README](https://github.com/awslabs/ec2-spot-fleet-bamboo-plugin/blob/master/README.md)
- [Issues](https://github.com/awslabs/ec2-spot-fleet-bamboo-plugin/issues)
- [Releases](https://github.com/awslabs/ec2-spot-fleet-bamboo-plugin/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
