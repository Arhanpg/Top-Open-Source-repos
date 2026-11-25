# aws-solutions/amazon-marketing-cloud-insights-on-aws

- Company: Amazon
- Account: aws-solutions
- Repository: https://github.com/aws-solutions/amazon-marketing-cloud-insights-on-aws
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:46:36+00:00

## Project purpose

The following images show the architecture of the solution and its components

## Why this project is used

Amazon Marketing Cloud Insights on AWS helps advertisers and agencies running campaigns on Amazon Ads to easily deploy AWS services to store, query, analyze, and visualize reporting from the AMC API

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Jupyter Notebook, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: aws-cdk-lib, aws-lambda-powertools, boto3, cdk-nag, crhelper, docker, moto, openapi-spec-validator, pandas, pyparsing, pyspark, pytest, pytest-cov, pytest-env, pytest-mock
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: source/infrastructure/app.py, source/infrastructure/data_lake/glue/lambdas/sdlf_heavy_transform/adtech/ads_report/main.py, source/infrastructure/data_lake/glue/lambdas/sdlf_heavy_transform/adtech/amc/main.py, source/infrastructure/data_lake/glue/lambdas/sdlf_heavy_transform/adtech/sp_report/main.py

## Setup and usage

- IAM Roles for Installation and Admin Operation: An IAM policy for installing the solution is listed within the IAM_POLICY_INSTALL.json file. IAM policies for operating the solution as an admin are created on stack deployment and can be found in the Outputs window of your Cloudformation stack under the AdminPolicyOutput key. Note: the policies generated should be used as a guide. Please review th
- IAM Roles for Installation and Admin Operation: These JSON files can be used to create a JSON policy in AWS IAM to scope the actions available to a user so they can install and operate the solution.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-solutions/amazon-marketing-cloud-insights-on-aws/blob/main/README.md
- README SHA: 7d75ac910be2d549bb459ac29b422bb9171567a4
- Manifests: source/requirements.txt, source/infrastructure/setup.py, source/tests/setup.py, source/cdk_solution_helper_py/helpers_cdk/setup.py, source/cdk_solution_helper_py/helpers_common/setup.py, source/infrastructure/scripts/requirements.txt
- Sampled source files: source/infrastructure/app.py, source/infrastructure/data_lake/glue/lambdas/sdlf_heavy_transform/adtech/ads_report/main.py, source/infrastructure/data_lake/glue/lambdas/sdlf_heavy_transform/adtech/amc/main.py, source/infrastructure/data_lake/glue/lambdas/sdlf_heavy_transform/adtech/sp_report/main.py
- Git tree state: captured
- Evidence fingerprint: 29987f87e2901dbb588268349ccdade51189baebbcef49d1ff312dec246de0af

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
