# aws-samples/amazon-msk-client-authentication

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-msk-client-authentication](https://github.com/aws-samples/amazon-msk-client-authentication)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-samples/amazon-msk-client-authentication/blob/master/README.md)
- README blob SHA: 92e62cd51f1552990db931f287e4809d45be1723
- README bytes captured: 14543
- README truncated at capture limit: False
- Repository ID: 257999680
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T06:48:42+00:00

### Short excerpt (up to 300 words)

> java -jar AuthMSK-1.0-SNAPSHOT.jar -caa

### README headings

- Managing Client certificates for mutual authentication with Amazon MSK
- Install
- Clone the repository and create the jar file.
- Usage Examples
- To get the list of parameters
- To generate the Private Key on the client, generate the csr, get a certificate issued by the ACM PCA and get and install the certificate in the keystore
- To generate the Private Key on the client, generate the csr with a specified Distinguished Name, get a certificate issued by the ACM PCA and get and install the certificate in the keystore
- To generate the Private Key on the client, generate the csr, get a certificate issued by the ACM PCA and get and install the certificate in the keystore with the ACM PCA in a region other than us-east-1
- To generate the Private Key on the client, generate the csr, get a certificate issued by the ACM PCA and get and install the certificate in the keystore of a type other than PKCS12 (eg. jks)
- To just get and install a certificate using the certificate arn
- To generate the Private Key on the client, generate the csr, get a certificate issued by the ACM PCA and get and install the certificate in the keystore and also generate PEM files for the Private Key and the issued certificate
- To just get and install a certificate using the certificate arn and also generate the PEM file for the issued certificate
- To use a client with TLS mutual authentication with an Amazon MSK cluster
- Example of using kafka-python client with Amazon MSK with TLS mutual authentication

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: To generate the Private Key on the client, generate the csr, get a certificate issued by the ACM PCA and get and install the certificate in the keystore

> java -jar AuthMSK-1.0-SNAPSHOT.jar -caa

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 21,272 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: AuthMSK, avro, aws-java-sdk-acm, aws-java-sdk-acmpca, aws-java-sdk-bom, aws-java-sdk-cloudformation, aws-java-sdk-kafka, aws-java-sdk-sts, jcommander, kafka-clients, log4j-api, log4j-core, log4j-slf4j-impl, maven-compiler-plugin, maven-shade-plugin, tools

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 30
- Forks at capture: 8
- Last updated: 2026-01-22T02:10:20Z
- Last pushed: 2023-09-29T22:21:03Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-msk-client-authentication)
- [README](https://github.com/aws-samples/amazon-msk-client-authentication/blob/master/README.md)
- [Issues](https://github.com/aws-samples/amazon-msk-client-authentication/issues)
- [Releases](https://github.com/aws-samples/amazon-msk-client-authentication/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
