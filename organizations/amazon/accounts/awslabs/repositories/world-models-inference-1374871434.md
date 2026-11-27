# awslabs/world-models-inference

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/world-models-inference](https://github.com/awslabs/world-models-inference)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/world-models-inference/blob/main/README.md)
- README blob SHA: 10f1d15f5921e2c2b912e21e03f92fc8c1c825ea
- README bytes captured: 10784
- README truncated at capture limit: False
- Repository ID: 1374871434
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

One-command deployment of open-source world models on AWS. Each model is a self-contained cartridge served behind a uniform API on EC2 or SageMaker — real-time interactive (browser-playable) and batch video generation.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T21:37:44+00:00

### Short excerpt (up to 300 words)

> git clone <this-repo> && ./deploy.sh builds the container ./deploy.sh restricts ALB ingress

### README headings

- World Model Inference
- Before you deploy
- Launch Stack (no local tooling)
- Quick start
- Endpoints
- Architecture
- Cost
- Security
- Documentation
- Contributing
- Contributors
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Quick start

> git clone <this-repo> &&

### Architecture and design: Architecture

> ./deploy.sh builds the container

### Limitations and security: Security

> ./deploy.sh restricts ALB ingress

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,337,125 |
| TypeScript | 320,635 |
| Dockerfile | 38,093 |
| Shell | 38,020 |
| CSS | 6,805 |
| HTML | 1,234 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: aws-sdk-sagemaker-runtime-http2, boto3, huggingface-hub, smithy-aws-core, websockets
- cdk/package.json (capture: captured) — dependency clues: @types/js-yaml, @types/node, aws-cdk, aws-cdk-lib, constructs, js-yaml, typescript
- frontend/package.json (capture: captured) — dependency clues: @fontsource/chakra-petch, @fontsource/ibm-plex-mono, @fontsource/ibm-plex-sans, @radix-ui/react-dialog, @radix-ui/react-slot, @tailwindcss/vite, @types/node, @types/react, @types/react-dom, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @vitejs/plugin-react, aws-amplify, class-variance-authority, clsx, eslint, eslint-plugin-react-hooks, eslint-plugin-react-refresh, lucide-react, react
- inference/lib/requirements.txt (capture: captured) — dependency clues: fastapi, imageio, imageio-ffmpeg, pyjwt, python-multipart, uvicorn, websockets
- inference/models/_template/requirements.txt (capture: captured)
- inference/models/cosmos3-nano/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 14
- Forks at capture: 4
- Last updated: 2026-11-03T02:47:03Z
- Last pushed: 2026-11-18T19:28:32Z
- Topics: aws, ec2, generative-ai, inference, physical-ai, sagemaker, world-models

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/world-models-inference)
- [README](https://github.com/awslabs/world-models-inference/blob/main/README.md)
- [Issues](https://github.com/awslabs/world-models-inference/issues)
- [Releases](https://github.com/awslabs/world-models-inference/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
