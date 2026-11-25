# awslabs/aws-codepipeline-custom-job-worker

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-codepipeline-custom-job-worker](https://github.com/awslabs/aws-codepipeline-custom-job-worker)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/aws-codepipeline-custom-job-worker/blob/master/README.md)
- README blob SHA: 4f16e6b53239bb2ccba0b860fce58b365a14a136
- README bytes captured: 3824
- README truncated at capture limit: False
- Repository ID: 38643205
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Use this sample to help you develop your own job worker when creating a custom action for AWS CodePipeline. For more information, see Create a Custom Action for a Pipeline. http://docs.aws.amazon.com/codepipeline/latest/userguide/how-to-create-custom-action.html

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T03:12:45+00:00

### Short excerpt (up to 300 words)

> mvn install:install-file -Dfile=target/jobworker-1.0.jar -DgroupId=com.amazonaws.codepipeline Install the following tools

### README headings

- AWS CodePipeline Job Worker
- Build
- Dependencies
- Ant targets
- Start
- Configuration
- AWS Region
- Deployment
- Replace with your Amazon S3 bucket name
- Make sure that you set up your application and deployment group in AWS CodeDeploy
- Compile the code and create deployment bundle
- Install the jar file as a dependency
- Create a tar archive from the build output
- Upload the deployment bundle to your Amazon S3 bucket.
- Start the deployment using AWS CodeDeploy

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install the jar file as a dependency

> mvn install:install-file -Dfile=target/jobworker-1.0.jar -DgroupId=com.amazonaws.codepipeline

### Technology and requirements: Dependencies

> Install the following tools

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 112,869 |
| Shell | 3,121 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: aws-java-sdk-codepipeline, commons-daemon, jobworker, junit, log4j-api, log4j-core, maven-compiler-plugin, maven-release-plugin, mockito-core

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 31
- Forks at capture: 21
- Last updated: 2025-12-23T20:17:02Z
- Last pushed: 2023-10-06T03:24:41Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-codepipeline-custom-job-worker)
- [README](https://github.com/awslabs/aws-codepipeline-custom-job-worker/blob/master/README.md)
- [Issues](https://github.com/awslabs/aws-codepipeline-custom-job-worker/issues)
- [Releases](https://github.com/awslabs/aws-codepipeline-custom-job-worker/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
