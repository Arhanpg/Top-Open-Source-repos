# aws/aws-parallelcluster-cookbook

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-parallelcluster-cookbook](https://github.com/aws/aws-parallelcluster-cookbook)
- Default branch: develop
- README: [Open upstream README](https://github.com/aws/aws-parallelcluster-cookbook/blob/develop/README.md)
- README blob SHA: 87693f9208526aa15d76219c998b0e5f578909af
- README bytes captured: 21961
- README truncated at capture limit: False
- Repository ID: 36883937
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Chef cookbook used to build and bootstrap AWS ParallelCluster

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T05:01:07+00:00

### Short excerpt (up to 300 words)

> AWS ParallelCluster Cookbook ============================ Running locally kitchen tests

### README headings

- Code structure
- Development
- About ChefSpec Tests
- run all the ChefSpec tests in a cookbook
- run a specific ChefSpec test
- About Kitchen Tests
- Kitchen tests helpers
- Run supervisord kitchen test from file kitchen.platform-install.yml in cookbooks/aws-parallelcluster-platform directory,
- for all OSes (concurrency 5) and log level debug
- Note that in this case "supervisord" is a pattern, so all the tests starting with "supervisord" string in that yaml file will be executed.
- Run converge phase only of kitchen from file kitchen.environment-config.yml in cookbooks/aws-parallelcluster-environment directory, for alinux2023 only.
- This is useful when you want to test recipe execution only.
- Once you have executed the converge step, you can for example execute multiple times the verify step, to validate the tests you are writing.
- Run verify phase only from file kitchen.platform-config.yml in cookbooks/aws-parallelcluster-platform directory,
- useful if you're modifing the test logic without touching the recipes code.
- Login to the instance created with the converge step
- Testing against a locally-built AMI with dependency overrides
- Kitchen tests definition
- Kitchen tests as GitHub actions and as part of CI/CD
- Save and reuse Docker image
- Save and reuse EC2 image
- Kitchen lifecycle hooks
- Use variables from lifecycle hooks as resource properties
- Known issues with docker
- Running kitchen tests on non `amd64` architectures
- removes running containers that may have been left dangling by previous
- executions of <your test prefix> test
- remove images from offending <your test prefix>
- you may want also to remove all dokken images
- (and safely remove all images, since subsequent executions will pull the

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> AWS ParallelCluster Cookbook ============================

### Architecture and design: Running kitchen tests on non `amd64` architectures

> Running locally kitchen tests

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Ruby | 1,862,602 |
| Python | 1,406,142 |
| Shell | 144,475 |
| HTML | 91,004 |
| Perl | 24,905 |
| Dockerfile | 1,230 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Gemfile (capture: captured)
- .devcontainer/Dockerfile (capture: captured)
- cookbooks/iptables/Gemfile (capture: captured)
- test/unit/requirements.txt (capture: captured) — dependency clues: PyYAML, assertpy, boto3, click, jinja2, jsonschema, mock, pytest, pytest-cov, pytest-datadir, pytest-mock, requests, retrying
- cookbooks/aws-parallelcluster-platform/files/cookbook_virtualenv/requirements.txt (capture: captured) — dependency clues: PyYAML, boto3, click, jinja2, jsonschema, requests, retrying, supervisor
- cookbooks/aws-parallelcluster-platform/files/pcluster-diag/pyproject.toml (capture: captured) — dependency clues: boto3, click, hypothesis, pytest, pytest-cov, pyyaml, retrying, tox

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 115
- Forks at capture: 110
- Last updated: 2026-11-11T16:43:32Z
- Last pushed: 2026-11-19T15:15:49Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-parallelcluster-cookbook)
- [README](https://github.com/aws/aws-parallelcluster-cookbook/blob/develop/README.md)
- [Issues](https://github.com/aws/aws-parallelcluster-cookbook/issues)
- [Releases](https://github.com/aws/aws-parallelcluster-cookbook/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
