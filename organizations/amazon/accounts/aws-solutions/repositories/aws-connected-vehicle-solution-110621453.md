# aws-solutions/aws-connected-vehicle-solution

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/aws-connected-vehicle-solution](https://github.com/aws-solutions/aws-connected-vehicle-solution)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-solutions/aws-connected-vehicle-solution/blob/master/README.md)
- README blob SHA: ab4479ae885ab120156ea79d867dc1ea0f71143f
- Repository ID: 110621453
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The AWS Connected Vehicle Solution is a reference implementation that provides a foundation for automotive product transformations for connected vehicle services, autonomous driving, electric powertrains, and shared mobility.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:03:51+00:00

### Short excerpt (up to 100 words)

> The AWS Connected Vehicle Solution is a reference implementation that provides a foundation for automotive product transformations for connected vehicle services, autonomous driving, electric powertrains, and shared mobility. To get started with the AWS Connected Vehicle Solution, please review the solution documentation. https://aws.amazon.com/answers/iot/connected-vehicle-solution/ * Configure the bucket name of your target Amazon S3 distribution bucket export BUCKET_PREFIX=my-bucket-name * Clone the repository, then build the distibutables: cd ./deployment \n chmod +x build-s3-dist.sh \n ./build-s3-dist.sh \n * Deploy the distibutables to an Amazon S3 bucket in your account. _Note:_ you must have the AWS Command Line Interface installed. cd ./deployment \n s3

### README headings

- AWS Connected Vehicle Solution
- Getting Started
- Building distributables for customization
- File Structure

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 217,034 |
| Shell | 5,837 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/data-loaders/dtc-generator/package.json (capture: captured) — dependency clues: aws-iot-device-sdk, aws-sdk, moment, randomstring, shortid, underscore
- source/resources/helper/package.json (capture: captured) — dependency clues: aws-sdk, aws-sdk-mock, chai, fast-csv, mocha, moment, node-uuid, npm-run-all, sinon, sinon-chai, underscore
- source/services/anomaly/package.json (capture: captured) — dependency clues: aws-sdk, aws-sdk-mock, chai, mocha, moment, npm-run-all, proxyquire, randomstring, shortid, sinon, sinon-chai, underscore
- source/services/driversafety/package.json (capture: captured) — dependency clues: aws-sdk, aws-sdk-mock, chai, mocha, moment, npm-run-all, proxyquire, shortid, sinon, sinon-chai, underscore
- source/services/dtc/package.json (capture: captured) — dependency clues: aws-sdk, aws-sdk-mock, chai, mocha, moment, npm-run-all, proxyquire, randomstring, shortid, sinon, sinon-chai, underscore
- source/services/jitr/package.json (capture: captured) — dependency clues: aws-sdk, aws-sdk-mock, chai, mocha, npm-run-all, proxyquire, sinon, sinon-chai

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 92
- Forks at capture: 50
- Last updated: 2026-09-07T22:04:33Z
- Last pushed: 2021-05-20T15:11:32Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/aws-connected-vehicle-solution)
- [README](https://github.com/aws-solutions/aws-connected-vehicle-solution/blob/master/README.md)
- [Issues](https://github.com/aws-solutions/aws-connected-vehicle-solution/issues)
- [Releases](https://github.com/aws-solutions/aws-connected-vehicle-solution/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
