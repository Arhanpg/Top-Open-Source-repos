# awslabs/realtime-fraud-detection-with-gnn-on-dgl

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/realtime-fraud-detection-with-gnn-on-dgl](https://github.com/awslabs/realtime-fraud-detection-with-gnn-on-dgl)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/realtime-fraud-detection-with-gnn-on-dgl/blob/main/README.md)
- README blob SHA: 9897e8d8af6ec2b90260ba5cf1fe53a019a021d2
- README bytes captured: 12372
- README truncated at capture limit: False
- Repository ID: 346584357
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An end-to-end blueprint architecture for real-time fraud detection(leveraging graph database Amazon Neptune) using Amazon SageMaker and Deep Graph Library (DGL) to construct a heterogeneous graph from tabular data and train a Graph Neural Network(GNN) model to detect fraudulent transactions in the IEEE-CIS dataset.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T18:20:51+00:00

### Short excerpt (up to 300 words)

> An AWS account Configure See CONTRIBUTING for more

### README headings

- Real-time Fraud Detection with Graph Neural Network on DGL
- Architecutre of solution
- Model training and deployment stack
- Dashboard stack
- How to train model and deploy inference endpoint
- How to deploy the solution
- Regions
- Quick deployment
- Deploy from source
- Prerequisites
- Deploy it in a new VPC
- Deploy it into existing VPC
- Deploy it with custom Neptune instance class and replica count
- Deploy it with using [SageMaker Serverless Inference][serverless-inference](experimental)
- Deploy it with custom domain of dashboard
- Deploy it to China regions
- How to test
- Data engineering/scientist
- FAQ
- What’s the benefits of using the graph neural network in the scenario Fraud Detection?
- Why using graph database in this solution?
- How differentiate this solution and Amazon Fraud Detector?
- How differentiate this solution and Amazon Neptune ML?
- Deployment failure on creating `CloudWatch LogGroup`
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Technology and requirements: Prerequisites

> An AWS account Configure

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 262,172 |
| Python | 83,716 |
| Jupyter Notebook | 21,739 |
| JavaScript | 17,718 |
| CSS | 7,597 |
| Shell | 2,483 |
| HTML | 1,879 |
| Dockerfile | 1,733 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/aws-apigatewayv2-alpha, @aws-cdk/aws-apigatewayv2-integrations-alpha, @aws-cdk/aws-appsync-alpha, @aws-cdk/aws-glue-alpha, @aws-cdk/aws-lambda-python-alpha, @aws-cdk/aws-neptune-alpha, @aws-cdk/cloud-assembly-schema, @aws-cdk/cx-api, @aws-sdk/client-cloudformation, @aws-sdk/client-glue, @aws-sdk/client-lambda, @aws-sdk/client-secrets-manager, @aws-sdk/client-serverlessapplicationrepository, @aws-sdk/client-sts, @types/aws-lambda, @types/bson, @types/jest, @types/mongodb, @types/node, @typescript-eslint/eslint-plugin
- frontend/package.json (capture: captured) — dependency clues: @material-ui/core, @material-ui/icons, @material-ui/lab, @testing-library/jest-dom, @testing-library/react, @testing-library/user-event, @types/jest, @types/node, @types/react, @types/react-dom, @types/react-loader-spinner, @types/react-router-dom, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, apexcharts, aws-amplify, aws-appsync, aws-sdk, axios, best-queue
- src/container.d/load-graph-data/Dockerfile (capture: captured)
- src/lambda.d/repackage-model/Dockerfile (capture: captured)
- src/lambda.d/inference/layer/requirements.txt (capture: captured) — dependency clues: numpy, pandas, sagemaker
- src/lambda.d/layer.d/awswrangler/requirements.txt (capture: captured) — dependency clues: awswrangler

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 225
- Forks at capture: 40
- Last updated: 2026-10-31T12:54:10Z
- Last pushed: 2024-03-31T14:49:55Z
- Topics: amplify-js, appsync, aws, aws-cdk, dgl, documentdb, fraud-detection, gnn, graph-database, neptune, sagemaker

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/realtime-fraud-detection-with-gnn-on-dgl)
- [README](https://github.com/awslabs/realtime-fraud-detection-with-gnn-on-dgl/blob/main/README.md)
- [Issues](https://github.com/awslabs/realtime-fraud-detection-with-gnn-on-dgl/issues)
- [Releases](https://github.com/awslabs/realtime-fraud-detection-with-gnn-on-dgl/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
