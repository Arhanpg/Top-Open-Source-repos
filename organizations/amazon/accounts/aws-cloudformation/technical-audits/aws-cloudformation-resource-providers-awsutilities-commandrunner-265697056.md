# aws-cloudformation/aws-cloudformation-resource-providers-awsutilities-commandrunner

- Company: Amazon
- Account: aws-cloudformation
- Repository: https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-awsutilities-commandrunner
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:12:37+00:00

## Project purpose

I took all the feedback, issues and feature requests from all our users to create this new major version. All known bugs for CommandRunner have now been fixed!

## Why this project is used

I took all the feedback, issues and feature requests from all our users to create this new major version. All known bugs for CommandRunner have now been fixed!

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: assertj-core, aws-cloudformation-rpdk-java-plugin, aws-java-sdk, aws-java-sdk-cloudformation, aws-java-sdk-core, aws-java-sdk-ec2, aws-java-sdk-iam, aws-java-sdk-s3, aws-java-sdk-ssm, aws-java-sdk-sts, aws-lambda-java-core, awsutility-cloudformation-commandrunner-handler, build-helper-maven-plugin, exec-maven-plugin, jackson-core, jacoco-maven-plugin, jmespath-java, junit-jupiter, lombok, maven-compiler-plugin, maven-resources-plugin, maven-shade-plugin, maven-surefire-plugin, mockito-core, mockito-junit-jupiter, slf4j-jdk14
- Build/package tools: Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/main/java/software/awsutility/cloudformation/commandrunner/CallbackContext.java, src/main/java/software/awsutility/cloudformation/commandrunner/Configuration.java, src/main/java/software/awsutility/cloudformation/commandrunner/CreateHandler.java, src/main/java/software/awsutility/cloudformation/commandrunner/DeleteHandler.java

## Setup and usage

- User Installation Steps: *Note: To build the source yourself, see the Developer Build Steps section below.*
- User Installation Steps: **Step 0**: Clone this repository and download the latest release using the following commands.
- User Installation Steps: git clone https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-awsutilities-commandrunner.git
- User Installation Steps: cd aws-cloudformation-resource-providers-awsutilities-commandrunner
- User Installation Steps: curl -LO https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-awsutilities-commandrunner/releases/latest/download/awsutility-cloudformation-commandrunner.zip
- User Installation Steps: **Step 1**: Use the register.sh bash script to register resource from scratch and upload package to S3 bucket. Pass the optional --set-default option to set this version to be the default version for the AWSUtility::CloudFormation::CommandRunner resource.
- User Installation Steps: $ ./scripts/register.sh --set-default
- User Installation Steps: Below is an example of a successful registration using the register.sh script.

## Limitations and caveats

- SecurityGroupId: The Id of the Security Group to attach to the instance the command is run in. If using SecurityGroup, the SubnetId property is required.

## Evidence and provenance

- README: https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-awsutilities-commandrunner/blob/master/README.md
- README SHA: 3416fbeede0292149107cb50ea0a6f93c906f13d
- Manifests: pom.xml
- Sampled source files: src/main/java/software/awsutility/cloudformation/commandrunner/CallbackContext.java, src/main/java/software/awsutility/cloudformation/commandrunner/Configuration.java, src/main/java/software/awsutility/cloudformation/commandrunner/CreateHandler.java, src/main/java/software/awsutility/cloudformation/commandrunner/DeleteHandler.java
- Git tree state: captured
- Evidence fingerprint: b918e9ce204b81b6328ead0a5945ce2481cd1f8c4b5c72afc9a2b92117ba5e51

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
