# aws-solutions/aws-data-lake-solution

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/aws-data-lake-solution](https://github.com/aws-solutions/aws-data-lake-solution)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/aws-data-lake-solution/blob/main/README.md)
- README blob SHA: 59e0fa76910072a25593d9b6a48ab6d993b3678b
- Repository ID: 74497220
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A deployable reference implementation intended to address pain points around conceptualizing data lake architectures that automatically configures the core AWS services necessary to easily tag, search, share, and govern specific subsets of data across a business or with other external businesses.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:03:57+00:00

### Short excerpt (up to 100 words)

> Many Amazon Web Services (AWS) customers require a data storage and analytics solution that offers more agility and flexibility than traditional data management systems. A data lake is an increasingly popular way to store and analyze data because it allows businesses to store all of their data, structured and unstructured, in a centralized repository. The AWS Cloud provides many of the building blocks required to help businesses implement a secure, flexible, and cost-effective data lake. The data lake solution is an automated reference implementation that deploys a highly available, cost-effective data lake architecture on the AWS Cloud. The solution is

### README headings

- Data Lake Solution
- File Structure
- Getting Started
- 01. Prerequisites
- 02. Build the data lake solution
- 03. Declare enviroment variables:
- 04. Run the data lake solution unit tests:
- 05. Build the data lake solution for deployment:
- 06. Upload deployment assets to your Amazon S3 bucket:
- 07. Deploy the data lake solution:
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 1,057,570 |
| HTML | 91,700 |
| Shell | 17,853 |
| CSS | 7,972 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- deployment/manifest-generator/package.json (capture: captured)
- source/cli/package.json (capture: captured) — dependency clues: commander, js-base64, moment, request
- source/console/package.json (capture: captured) — dependency clues: bower, http-server, jasmine-core, karma, karma-chrome-launcher, karma-firefox-launcher, karma-jasmine, karma-junit-reporter, protractor
- source/api/authorizer/package.json (capture: captured) — dependency clues: aws-sdk-mock, chai, js-base64, jsonwebtoken, jwk-to-pem, mocha, moment, npm-run-all, request, sinon, sinon-chai, underscore
- source/resources/access-validator/package.json (capture: captured) — dependency clues: aws-sdk-mock, chai, chai-things, mocha, sinon, sinon-chai, underscore
- source/resources/helper/package.json (capture: captured) — dependency clues: aws-sdk-mock, chai, elasticsearch, http-aws-es, mime-types, mocha, moment, npm-run-all, password-generator, sinon, sinon-chai, underscore, uuid

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 398
- Forks at capture: 155
- Last updated: 2026-07-31T21:48:18Z
- Last pushed: 2024-06-03T18:22:27Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/aws-data-lake-solution)
- [README](https://github.com/aws-solutions/aws-data-lake-solution/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/aws-data-lake-solution/issues)
- [Releases](https://github.com/aws-solutions/aws-data-lake-solution/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
