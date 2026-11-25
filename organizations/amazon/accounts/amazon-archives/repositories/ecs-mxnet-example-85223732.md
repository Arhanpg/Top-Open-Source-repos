# amazon-archives/ecs-mxnet-example

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/ecs-mxnet-example](https://github.com/amazon-archives/ecs-mxnet-example)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/ecs-mxnet-example/blob/master/README.md)
- README blob SHA: 4e03b95104d82e0e92274b1cfdd4626434476a60
- README bytes captured: 4051
- README truncated at capture limit: False
- Repository ID: 85223732
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An example project to deploy MXNet inference API with Docker on Amazon ECS. Uses CodePipeline and CodeBuild to build the image to deploy to ECS. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T00:36:41+00:00

### Short excerpt (up to 300 words)

> This project will create an automated workflow that will provision, configure and orchestrate a pipeline triggering deployment of any changes to your mxnet model or

### README headings

- Deploy a MXNet predict function to Amazon ECS using CodeCommit and CodePipeline
- Required:
- Create a CodeCommit repository and Connect with this repository
- Commit the Source Code and Configuration files into your CodeCommit repository
- Deploy via CloudFormation template.
- Test using a Rest Client.
- Cleanup

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Deploy a MXNet predict function to Amazon ECS using CodeCommit and CodePipeline

> This project will create an automated workflow that will provision, configure and orchestrate a pipeline triggering deployment of any changes to your mxnet model or

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 3,093 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- image-classification-predict/Dockerfile (capture: captured)
- image-classification-predict/config/requirements.txt (capture: captured) — dependency clues: Flask, Jinja2, Werkzeug, boto3, certifi, gunicorn, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 49
- Forks at capture: 66
- Last updated: 2026-07-15T07:47:22Z
- Last pushed: 2020-01-30T20:20:13Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/ecs-mxnet-example)
- [README](https://github.com/amazon-archives/ecs-mxnet-example/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/ecs-mxnet-example/issues)
- [Releases](https://github.com/amazon-archives/ecs-mxnet-example/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
