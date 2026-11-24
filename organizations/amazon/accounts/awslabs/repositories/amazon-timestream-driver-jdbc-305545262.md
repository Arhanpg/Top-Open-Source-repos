# awslabs/amazon-timestream-driver-jdbc

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-timestream-driver-jdbc](https://github.com/awslabs/amazon-timestream-driver-jdbc)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/amazon-timestream-driver-jdbc/blob/main/README.md)
- README blob SHA: aed31599492ffad6311ce18ea2f1bba9b18e789c
- README bytes captured: 24076
- README truncated at capture limit: False
- Repository ID: 305545262
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T20:29:41+00:00

### Short excerpt (up to 300 words)

> Since the Timestream Query 1. **Sign up for 1. Timestream does not

### README headings

- Amazon Timestream Driver for Java
- User Documentation
- Prerequisites
- Using the Timestream JDBC driver
- JAR With All Dependencies Shaded Except SLF4J (amazon-timestream-jdbc-\<version\>-jar-with-all-dependencies.jar)
- Driver Setup in BI Applications
- JAR With No Dependencies (amazon-timestream-jdbc-\<version\>.jar)
- Driver Class
- Creating a Connection
- Constructing the Connection URL
- Using a `Properties` Object to Specify Connection Properties
- Optional Connection Properties
- Standard Client Info Option
- Driver Configuration Option
- SDK Options
- Endpoint Configuration Options
- Basic Authentication Options
- Credentials Provider Options
- SAML-Based Authentication Options for Okta
- SAML-Based Authentication Options for Azure Active Directory
- SAML-Based Authentication Configuration
- Configure SAML 2.0 for AWS with Okta.
- Prerequisites
- Creating AWS Account Federation on Okta
- Setting up Okta for SAML
- Configure SAML 2.0 for AWS with Azure Active Directory.
- Prerequisites
- Setting up Azure AD
- Setting up IAM Identity Provider and Roles in AWS
- Create a SAML Identity Provider

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: To build the signed jar the following maven profile should be used: `mvn clean install -Ddeploy`.

> Since the Timestream Query

### Technology and requirements: Prerequisites

> 1. **Sign up for

### Limitations and security: Known Issues

> 1. Timestream does not

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 745,814 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: amazon-timestream-jdbc, aws-java-sdk-core, aws-java-sdk-sts, aws-java-sdk-timestreamquery, aws-java-sdk-timestreamwrite, checkstyle, guava, jsoup, jul-to-slf4j, junit-jupiter, maven-checkstyle-plugin, timestream
- integrationtest/pom.xml (capture: captured) — dependency clues: amazon-timestream-jdbc, aws-java-sdk-core, aws-java-sdk-timestreamquery, aws-java-sdk-timestreamwrite, guava, integrationtest, jul-to-slf4j, junit-jupiter, timestream
- jdbc/pom.xml (capture: captured) — dependency clues: amazon-timestream-jdbc, aws-java-sdk-core, aws-java-sdk-sts, aws-java-sdk-timestreamquery, guava, jacoco-maven-plugin, jsoup, jul-to-slf4j, junit-jupiter, maven-gpg-plugin, maven-javadoc-plugin, maven-resources-plugin, maven-shade-plugin, maven-source-plugin, maven-surefire-plugin, mockito-core, mockito-inline, nexus-staging-maven-plugin, properties-maven-plugin, spotbugs-maven-plugin
- performancetest/pom.xml (capture: captured) — dependency clues: amazon-timestream-jdbc, aws-java-sdk-core, aws-java-sdk-sts, aws-java-sdk-timestreamquery, guava, jsoup, jul-to-slf4j, junit-jupiter, performancetest, timestream

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 11
- Forks at capture: 11
- Last updated: 2025-10-13T18:49:49Z
- Last pushed: 2026-08-08T08:09:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-timestream-driver-jdbc)
- [README](https://github.com/awslabs/amazon-timestream-driver-jdbc/blob/main/README.md)
- [Issues](https://github.com/awslabs/amazon-timestream-driver-jdbc/issues)
- [Releases](https://github.com/awslabs/amazon-timestream-driver-jdbc/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
