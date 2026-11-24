# aws-samples/alphafold-protein-structure-prediction-with-frontend-app

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/alphafold-protein-structure-prediction-with-frontend-app](https://github.com/aws-samples/alphafold-protein-structure-prediction-with-frontend-app)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/alphafold-protein-structure-prediction-with-frontend-app/blob/main/README.md)
- README blob SHA: a08179a82d5f0398ff12ab86c02c109fb3da26cb
- README bytes captured: 12356
- README truncated at capture limit: False
- Repository ID: 590288288
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T08:19:51+00:00

### Short excerpt (up to 300 words)

> pip3 install aws-parallelcluster==3.7.2 --user **NOTE**: We recommend that

### README headings

- AlphaFold2 Webapp on AWS
- Prerequisites for development environment
- Set up your development environment using AWS Cloud9
- Deploy the application
- 1. Backend
- Build the frontend CDK stack
- Set up the network, database, and storage
- change the access mode of private key
- 2. Set up a cluster managed by AWS ParallelCluster
- Install AWS ParallelCluster CLI
- Set the default region
- Generate a configuration file for a ParallelCluster cluster
- Create a ParallelCluster cluster
- 3. Web frontend
- Get the instance ID of the cluster's HeadNode
- Deploy the frontend CDK stack
- 4. Launch a HeadNode in your cluster
- SSH login to ParallelCluster's HeadNode using private key
- 5. Check if the backend works
- SSH login to ParallelCluster's HeadNode using private key
- Fetch the FASTA file of your choice (e.g. Q5VSL9)
- Start the job using CLI
- While running a job
- Once all the jobs finished
- 6. Check if the frontend works
- 7. Clean up
- Delete the dataset files from HeadNode
- Delete the cluster
- Check the name of the CDK stacks (for frontend and backend) and destroy them

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install AWS ParallelCluster CLI

> pip3 install aws-parallelcluster==3.7.2 --user

### Technology and requirements: Prerequisites for development environment

> **NOTE**: We recommend that

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 48,780 |
| Python | 18,537 |
| Shell | 9,181 |
| CSS | 1,782 |
| HTML | 641 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- app/package.json (capture: captured) — dependency clues: 3dmol, @emotion/react, @emotion/styled, @mui/icons-material, @mui/material, @rollup/plugin-replace, @types/react, @types/react-dom, @vitejs/plugin-react, date-fns, i18next, material-ui-confirm, react, react-dom, react-i18next, react-router-dom, swr, typescript, vite
- lambda/requirements.txt (capture: captured) — dependency clues: aws-lambda-powertools, aws-xray-sdk, boto3, botocore, fastjsonschema, jmespath, python-dateutil, s3transfer, six, urllib3, wrapt
- provisioning/package.json (capture: captured) — dependency clues: @aws-cdk/aws-lambda-python-alpha, @types/node, aws-cdk, aws-cdk-lib, aws-sdk, cdk-remote-stack, constructs, esbuild, ts-node, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 19
- Forks at capture: 6
- Last updated: 2026-03-18T09:07:05Z
- Last pushed: 2024-10-08T00:25:23Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/alphafold-protein-structure-prediction-with-frontend-app)
- [README](https://github.com/aws-samples/alphafold-protein-structure-prediction-with-frontend-app/blob/main/README.md)
- [Issues](https://github.com/aws-samples/alphafold-protein-structure-prediction-with-frontend-app/issues)
- [Releases](https://github.com/aws-samples/alphafold-protein-structure-prediction-with-frontend-app/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
