# awslabs/aws-glue-data-catalog-client-for-apache-hive-metastore

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-glue-data-catalog-client-for-apache-hive-metastore](https://github.com/awslabs/aws-glue-data-catalog-client-for-apache-hive-metastore)
- Default branch: branch-3.4.0
- README: [Open upstream README](https://github.com/awslabs/aws-glue-data-catalog-client-for-apache-hive-metastore/blob/branch-3.4.0/README.md)
- README blob SHA: fd897a90cd5e3a00ac2ce6a1774f9b32bbcc8f86
- README bytes captured: 5399
- README truncated at capture limit: False
- Repository ID: 165758293
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The AWS Glue Data Catalog is a fully managed, Apache Hive Metastore compatible, metadata repository. Customers can use the Data Catalog as a central repository to store structural and operational metadata for their data.  AWS Glue provides out-of-box integration with Amazon EMR that enables customers to use the AWS Glue Data Catalog as an external Hive Metastore.  This is an open-source implementation of the Apache Hive Metastore client on Amazon EMR clusters that uses the AWS Glue Data Catalog as an external Hive Metastore. It serves as a reference implementation for building a Hive Metastore-compatible client that connects to the AWS Glue Data Catalog. It may be ported to other Hive Metastore-compatible platforms such as other Hadoop and Apache Spark distributions

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T07:13:34+00:00

### Short excerpt (up to 300 words)

> Obtain a copy of

### README headings

- AWS Glue Data Catalog Client for Apache Hive Metastore
- Patching Apache Hive and Installing It Locally
- Building the Glue Data Catalog Client
- Configuring Hive to Use the Hive Client
- Configuring Spark to Use the Spark Client
- Enabling client side caching for catalog
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Patching Apache Hive and Installing It Locally

> Obtain a copy of

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 891,785 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: aws-glue-datacatalog-hive-client, maven-assembly-plugin, maven-checkstyle-plugin, maven-compiler-plugin, maven-eclipse-plugin, maven-project-info-reports-plugin, maven-surefire-plugin
- aws-glue-datacatalog-client-common/pom.xml (capture: captured) — dependency clues: aws-glue-datacatalog-client-common, aws-glue-datacatalog-hive-client, aws-java-sdk-core, aws-java-sdk-glue, guava, hadoop-common, hadoop-mapreduce-client-core, hamcrest-library, hive-exec, hive-metastore, junit, maven-jar-plugin, mockito-core, powermock-api-mockito, powermock-module-junit4, shims-loader
- aws-glue-datacatalog-hive3-client/pom.xml (capture: captured) — dependency clues: aws-glue-datacatalog-client-common, aws-glue-datacatalog-hive-client, aws-glue-datacatalog-hive3-client, hadoop-common, hadoop-mapreduce-client-core, hamcrest-library, hive-exec, hive-metastore, httpclient, junit, maven-shade-plugin, mockito-core
- aws-glue-datacatalog-spark-client/pom.xml (capture: captured) — dependency clues: aws-glue-datacatalog-client-common, aws-glue-datacatalog-hive-client, aws-glue-datacatalog-spark-client, hadoop-common, hamcrest-library, hive-exec, hive-metastore, httpclient, junit, maven-jar-plugin, maven-shade-plugin, mockito-core
- shims/pom.xml (capture: captured) — dependency clues: aws-glue-datacatalog-hive-client, shims
- shims/common/pom.xml (capture: captured) — dependency clues: hadoop-common, hive-exec, hive-metastore, shims, shims-common

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 230
- Forks at capture: 140
- Last updated: 2026-09-14T14:01:41Z
- Last pushed: 2026-05-18T15:24:19Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-glue-data-catalog-client-for-apache-hive-metastore)
- [README](https://github.com/awslabs/aws-glue-data-catalog-client-for-apache-hive-metastore/blob/branch-3.4.0/README.md)
- [Issues](https://github.com/awslabs/aws-glue-data-catalog-client-for-apache-hive-metastore/issues)
- [Releases](https://github.com/awslabs/aws-glue-data-catalog-client-for-apache-hive-metastore/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
