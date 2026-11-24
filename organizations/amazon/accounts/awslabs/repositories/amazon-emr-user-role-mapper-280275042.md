# awslabs/amazon-emr-user-role-mapper

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-emr-user-role-mapper](https://github.com/awslabs/amazon-emr-user-role-mapper)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/amazon-emr-user-role-mapper/blob/master/README.md)
- README blob SHA: 4a1bf517362367045ec633f8a96ab51ac34be564
- Repository ID: 280275042
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Application to securely map users on a multi tenant Amazon EMR cluster to different IAM Roles and then assume the mapped Role.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:36:53+00:00

### Short excerpt (up to 100 words)

> This capability is intended to enable customers to use multi-tenant EMR clusters and provide their users from different organizations/departments to have segregated access to data in AWS. This application runs a proxy over the Instance Metadata Service available on EMR/EC2 hosts. The application determines the end user using the OS information for the connecting socket, and then invokes the mapping framework to map the user/group. git clone https://github.com/awslabs/amazon-emr-user-role-mapper.git cd amazon-emr-user-role-mapper mvn clean install cd emr-user-role-mapper-application/usr cp ../target/emr-user-role-mapper-application-1.1.0-jar-with-dependencies-and-exclude-classes.jar install/ Edit the properties file in install/user-role-mapper.properties. rolemapper.s3.key=mappings.json` rolemapper.s3.bucket=my-urm-bucket` Here is a sample format of the JSON. { "PrincipalRoleMappings": [ { "username": "user1",

### README headings

- Amazon EMR User Role Mapper
- Build
- Installation
- Package and copy artifacts to S3
- Installing EMR User Role Mapper on EMR
- Launching on an EC2 instance
- Validating the Installation
- Test URM
- Integration tests
- Managed policy union mapper
- Example:
- URM Custom Credentials provider
- Security
- Limitations
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 231,104 |
| Shell | 12,568 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: amazon-emr-user-role-mapper
- emr-user-role-mapper-application/pom.xml (capture: captured) — dependency clues: amazon-emr-user-role-mapper, aws-java-sdk-iam, aws-java-sdk-s3, aws-java-sdk-sts, emr-user-role-mapper-application, emr-user-role-mapper-provider, gson, guava, hamcrest, hamcrest-core, hamcrest-library, jacoco-maven-plugin, javax.servlet-api, jersey-common, jersey-container-jetty-http, jersey-container-jetty-servlet, jersey-hk2, jersey-server, jersey-test-framework-core, jersey-test-framework-provider-grizzly2
- emr-user-role-mapper-credentials-provider/pom.xml (capture: captured) — dependency clues: amazon-emr-user-role-mapper, aws-java-sdk-core, gson, hadoop-common, httpclient, jacoco-maven-plugin, junit, maven-shade-plugin, mockito-core, powermock-api-mockito2, powermock-module-junit4, urm-credentials-provider
- emr-user-role-mapper-interface/pom.xml (capture: captured) — dependency clues: amazon-emr-user-role-mapper, aws-java-sdk-sts, emr-user-role-mapper-provider, maven-compiler-plugin
- emr-user-role-mapper-s3storagebasedauthorizationmanager/pom.xml (capture: captured) — dependency clues: aws-glue-datacatalog-client-common, aws-java-sdk-core, aws-java-sdk-s3, hive-common, hive-exec, hive-metastore, hive-service, junit, maven-compiler-plugin, mockito-core, powermock-api-mockito2, powermock-module-junit4, s3storagebasedauthorizationmanager, urm-credentials-provider

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 23
- Forks at capture: 20
- Last updated: 2026-11-05T23:32:18Z
- Last pushed: 2023-10-24T00:20:17Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-emr-user-role-mapper)
- [README](https://github.com/awslabs/amazon-emr-user-role-mapper/blob/master/README.md)
- [Issues](https://github.com/awslabs/amazon-emr-user-role-mapper/issues)
- [Releases](https://github.com/awslabs/amazon-emr-user-role-mapper/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
