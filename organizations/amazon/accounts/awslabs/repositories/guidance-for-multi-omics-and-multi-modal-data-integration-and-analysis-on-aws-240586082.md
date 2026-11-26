# awslabs/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws](https://github.com/awslabs/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/blob/master/README.md)
- README blob SHA: ed59f811b266502a3a489fbdde36724ad8478c3e
- README bytes captured: 6477
- README truncated at capture limit: False
- Repository ID: 240586082
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This guidance creates a scalable environment in AWS to prepare genomic, clinical, mutation, expression and imaging data for large-scale analysis and perform interactive queries against a data lake. The solution also demonstrates the use of Amazon Omics for multi-modal analysis.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T22:14:39+00:00

### Short excerpt (up to 300 words)

> aws s3 cp ./$SOLUTION_NAME.template 1. Create a distribution

### README headings

- Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS
- Setup
- Customization
- Running unit tests for customization
- Prerequisites
- Building and deploying distributable for customization
- Change to deployment directory.
- Build the distributable.
- Deploy the distributable to an Amazon S3 bucket in your account. _Note:_ you must have the AWS Command Line Interface installed
- Deploy the global assets.
- Deploy the regional assets.
- Copy the static assets.
- Go to the DIST_OUTPUT_BUCKET and copy the OBJECT URL for latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws.template.
- Go to the AWS CloudFormation Console and create a new stack using the template URL copied.
- File Structure

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Deploy the distributable to an Amazon S3 bucket in your account. _Note:_ you must have the AWS Command Line Interface installed

> aws s3 cp ./$SOLUTION_NAME.template

### Technology and requirements: Prerequisites

> 1. Create a distribution

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Jupyter Notebook | 257,827 |
| Python | 66,503 |
| Shell | 17,802 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/GenomicsAnalysisCode/setup/requirements.txt (capture: captured) — dependency clues: crhelper

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 25
- Forks at capture: 8
- Last updated: 2026-07-04T06:12:06Z
- Last pushed: 2025-06-30T16:34:28Z
- Topics: aws, life-sciences, multimodal, multimodality

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws)
- [README](https://github.com/awslabs/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/blob/master/README.md)
- [Issues](https://github.com/awslabs/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/issues)
- [Releases](https://github.com/awslabs/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
