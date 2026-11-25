# amazon-archives/AWS-MIMIC-IIItoOMOP

- Company: Amazon
- Account: amazon-archives
- Repository: https://github.com/amazon-archives/AWS-MIMIC-IIItoOMOP
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:44:35+00:00

## Project purpose

This code demonstrates the architecture featured on the AWS big data blog (https://aws.amazon.com/blogs/big-data/) on creating a healthcare data warehouse using Redshift, Spark on EMR and Lambda that was published on May 12, 2017. It takes an openly available research dataset called MIMIC-III and converts it into a standard open source healthcare data model called OMOP.

## Why this project is used

Demonstrates creating a healthcare data warehouse using the MIMIC-III dataset on Redshift, Spark on EMR and Lambda

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java
- Frameworks/libraries: Unknown / not established
- Dependency names: AWS-MIMIC-IIItoOMOP, RedshiftCopier, SparkBatchProcessor, asm, aws-java-sdk-bom, aws-java-sdk-cloudformation, aws-java-sdk-core, aws-java-sdk-ec2, aws-java-sdk-emr, aws-java-sdk-iam, aws-java-sdk-lambda, aws-java-sdk-redshift, aws-java-sdk-s3, aws-java-sdk-sns, aws-lambda-java-core, aws-lambda-java-events, cobertura-maven-plugin, commons-io, hamcrest-core, junit, maven-assembly-plugin, maven-compiler-plugin, maven-jar-plugin, redshift-jdbc41, scala-library, spark-core_2.10, spark-sql_2.10
- Build/package tools: Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: RedshiftCopier/src/main/java/com/amazon/redshiftcopier/Driver.java, RedshiftCopier/src/main/java/com/amazon/redshiftcopier/FileProcessor.java, RedshiftCopier/src/main/java/com/amazon/redshiftcopier/RedshiftConnection.java, SparkBatchProcessor/src/main/java/com/amazon/sparkbatchprocessor/CloudFormationManager.java

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/amazon-archives/AWS-MIMIC-IIItoOMOP/blob/master/README.md
- README SHA: a4808d3c70dc298fbc3c0c21dff26c3cce1172d0
- Manifests: pom.xml, RedshiftCopier/pom.xml, SparkBatchProcessor/pom.xml
- Sampled source files: RedshiftCopier/src/main/java/com/amazon/redshiftcopier/Driver.java, RedshiftCopier/src/main/java/com/amazon/redshiftcopier/FileProcessor.java, RedshiftCopier/src/main/java/com/amazon/redshiftcopier/RedshiftConnection.java, SparkBatchProcessor/src/main/java/com/amazon/sparkbatchprocessor/CloudFormationManager.java
- Git tree state: captured
- Evidence fingerprint: abd9eb606201f4114f44b4289b753e1fb500c768dd7694e0ec9bbfe452255bb1

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
