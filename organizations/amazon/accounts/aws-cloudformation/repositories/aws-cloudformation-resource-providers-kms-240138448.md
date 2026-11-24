# aws-cloudformation/aws-cloudformation-resource-providers-kms

- Company: Amazon
- GitHub account: [https://github.com/aws-cloudformation](https://github.com/aws-cloudformation)
- Mapping status: official-directory-listed
- Repository: [aws-cloudformation/aws-cloudformation-resource-providers-kms](https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-kms)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-kms/blob/master/README.md)
- README blob SHA: 9d0dde906c2eaf31f56a3b8e5f521fda1ab5958c
- README bytes captured: 1403
- README truncated at capture limit: False
- Repository ID: 240138448
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Key Management Service (KMS) makes it easy for you to create and manage cryptographic keys and control their use across a wide range of AWS services and in your applications. AWS KMS is a secure and resilient service that uses hardware security modules that have been validated under FIPS 140-2, or are in the process of being validated, to protect your keys. AWS KMS is integrated with AWS CloudTrail to provide you with logs of all key usage to help meet your regulatory and compliance needs.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T05:15:00+00:00

### Short excerpt (up to 300 words)

> This repository contains AWS-owned resource providers for the AWS::KMS::* namespace. Usage The CloudFormation CLI (cfn) allows you to author your own resource providers that can

### README headings

- AWS CloudFormation Resource Provider Package For AWS Key Management Service
- run all hooks on all files, mirrors what the CI runs
- run unit tests and coverage checks

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: AWS CloudFormation Resource Provider Package For AWS Key Management Service

> This repository contains AWS-owned resource providers for the AWS::KMS::* namespace. Usage The CloudFormation CLI (cfn) allows you to author your own resource providers that can

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 393,206 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: assertj-core, aws-cloudformation-rpdk-java-plugin, aws-kms-cloudformation, jacoco-maven-plugin, junit-jupiter, kms, lombok, maven-checkstyle-plugin, maven-compiler-plugin, maven-project-info-reports-plugin, maven-site-plugin, maven-surefire-plugin, mockito-core, mockito-junit-jupiter, sdk-core, utils
- alias/pom.xml (capture: captured) — dependency clues: aws-cloudformation-rpdk-java-plugin, aws-kms-alias-handler, aws-kms-cloudformation, aws-kms-common, build-helper-maven-plugin, exec-maven-plugin, maven-resources-plugin, maven-shade-plugin
- common/pom.xml (capture: captured) — dependency clues: aws-kms-cloudformation, aws-kms-common, maven-jar-plugin
- key/pom.xml (capture: captured) — dependency clues: aws-cloudformation-rpdk-java-plugin, aws-kms-cloudformation, aws-kms-common, aws-kms-key-handler, build-helper-maven-plugin, exec-maven-plugin, maven-resources-plugin, maven-shade-plugin
- replicakey/pom.xml (capture: captured) — dependency clues: aws-cloudformation-rpdk-java-plugin, aws-kms-cloudformation, aws-kms-common, aws-kms-replicakey-handler, build-helper-maven-plugin, exec-maven-plugin, kms, maven-resources-plugin, maven-shade-plugin, sdk-core, utils

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 15
- Forks at capture: 13
- Last updated: 2026-07-22T19:33:02Z
- Last pushed: 2026-01-26T21:37:33Z
- Topics: aws-key-management, aws-kms, aws-resources, kms, resources

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-kms)
- [README](https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-kms/blob/master/README.md)
- [Issues](https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-kms/issues)
- [Releases](https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-kms/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
