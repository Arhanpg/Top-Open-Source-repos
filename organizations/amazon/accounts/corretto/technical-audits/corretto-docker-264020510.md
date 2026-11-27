# corretto/corretto-docker

- Company: Amazon
- Account: corretto
- Repository: https://github.com/corretto/corretto-docker
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:14:01+00:00

## Project purpose

Master repository where Dockerfiles for Amazon Corretto are hosted. These docker files are used to build images for Amazon Corretto Offical Images and ECR images.

## Why this project is used

Dockerfiles for Amazon Corretto Official images.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Dockerfile, Shell, Python
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: bin/apply-template.py, bin/create-images.sh, bin/tag-generator.py, bin/test-image.sh

## Setup and usage

- Usage: The docker images are available on Amazon Corretto Official Images
- Usage: To use Amazon Corretto Official Images from Docker hub run
- Usage: docker pull amazoncorretto:17
- Usage: The docker images are also available on **Amazon ECR**.
- Usage: To get Corretto docker images from Amazon ECR please see Amazon Corretto's ECR Public Gallery as well as the Docker Official Images ECR Public Gallery
- Usage: To use docker images from Corretto ECR Public Gallery run the following commands:
- Usage: docker pull public.ecr.aws/amazoncorretto/amazoncorretto:17
- Usage: docker run -it public.ecr.aws/amazoncorretto/amazoncorretto:17 /bin/bash

## Limitations and caveats

- Security: If you would like to report a potential security issue in this project, please do not create a GitHub issue. Instead,
- Security: please follow the instructions here or email
- Security: AWS security directly.
- Why does security scanner show that a docker image has a CVE?: If a security scanner reports that an amazoncorretto image includes a CVE, the first recommended action is to pull an updated version of this image with docker pull amazoncorretto: .
- Why does security scanner show that a docker image has a CVE?: If no updated image is available, run the appropriate command to update packages for the platform in your Dockerfiles or running systems to resolve the issue immediately.
- Why does security scanner show that a docker image has a CVE?: * AmazonLinux 2023 (default images): dnf update -y --security --releasever=latest
- Why does security scanner show that a docker image has a CVE?: * AmazonLinux 2 and many other RPM based distrobutions: yum update -y --security
- Why does security scanner show that a docker image has a CVE?: * AlpineLinux: apk -U upgrade

## Evidence and provenance

- README: https://github.com/corretto/corretto-docker/blob/main/README.md
- README SHA: add77e1cc23ed5ea4e69404e22306b8feab87b5c
- Manifests: 11/headful/al2023/Dockerfile, 11/headful/al2027/Dockerfile, 11/headless/al2/Dockerfile, 11/headless/al2023/Dockerfile, 11/headless/al2027/Dockerfile, 11/jdk/al2-generic/Dockerfile
- Sampled source files: bin/apply-template.py, bin/create-images.sh, bin/tag-generator.py, bin/test-image.sh
- Git tree state: captured
- Evidence fingerprint: e74aabf316fe94a26617f83b3738b577d891c6ca32b656141a69b78cfeb77367

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
