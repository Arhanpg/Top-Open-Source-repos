# aws-solutions/maintaining-personalized-experiences-with-machine-learning

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/maintaining-personalized-experiences-with-machine-learning](https://github.com/aws-solutions/maintaining-personalized-experiences-with-machine-learning)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/maintaining-personalized-experiences-with-machine-learning/blob/main/README.md)
- README blob SHA: 5ad398db508c8ba3ce301e28af9438cf6462807a
- Repository ID: 409427545
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Maintaining Personalized Experiences with Machine Learning solution provides an automated pipeline to maintain resources in Amazon Personalize. This pipeline allows you to keep up to date with your user’s most recent activity while sustaining and improving the relevance of recommendations

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:44:09+00:00

### Short excerpt (up to 100 words)

> ⚠️🚨⚠️ __Important: Maintaining Personalized Experiences with Machine Learning has been deprecated and will not be receiving any additional features or updates. We encourage customers to explore Amazon Personalize to deliver hyper-personalized user experiences in real-time at scale, improving user engagement, customer loyalty, and business results.__ ⚠️🚨⚠️ The Maintaining Personalized Experiences with Machine Learning solution provides a mechanism to automate much of the workflow around Amazon Personalize. This includes dataset group creation, dataset creation and import, solution creation, solution version creation, campaign creation and batch inference job creation Scheduled rules can be configured for setting up import jobs, solution version retraining

### README headings

- Maintaining Personalized Experiences with Machine Learning
- Table of Contents
- Architecture
- AWS CDK Constructs
- Deployment
- Configuration
- Configuration with Tags
- Training Mode
- Creating a custom build
- Prerequisites
- 1. Download or clone this repo
- 2. Create a Python virtual environment for development
- 2. After introducing changes, run the unit tests to make sure the customizations don't break existing functionality
- 3. Build the solution for deployment
- Using AWS CDK (recommended)
- set environment variables required by the solution
- bootstrap CDK (required once - deploys a CDK bootstrap CloudFormation stack for assets)
- build the solution
- build and deploy the solution
- Using the solution build tools
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 641,961 |
| Java | 6,641 |
| Shell | 2,284 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/infrastructure/setup.py (capture: captured)
- source/cdk_solution_helper_py/helpers_cdk/setup.py (capture: captured)
- source/cdk_solution_helper_py/helpers_common/setup.py (capture: captured)
- source/scheduler/cdk/setup.py (capture: captured)
- source/scheduler/common/setup.py (capture: captured)
- source/tests/cdk_solution_helper/aws_lambda/python/fixtures/Pipfile (capture: captured) — dependency clues: minimal

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 28
- Forks at capture: 19
- Last updated: 2026-03-13T23:38:36Z
- Last pushed: 2025-10-10T18:43:27Z
- Topics: amazon-personalize, artificial-intelligence, machine-learning

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/maintaining-personalized-experiences-with-machine-learning)
- [README](https://github.com/aws-solutions/maintaining-personalized-experiences-with-machine-learning/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/maintaining-personalized-experiences-with-machine-learning/issues)
- [Releases](https://github.com/aws-solutions/maintaining-personalized-experiences-with-machine-learning/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
