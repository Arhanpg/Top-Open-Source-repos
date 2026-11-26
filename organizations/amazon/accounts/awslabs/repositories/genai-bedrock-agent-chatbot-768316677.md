# awslabs/genai-bedrock-agent-chatbot

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/genai-bedrock-agent-chatbot](https://github.com/awslabs/genai-bedrock-agent-chatbot)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/genai-bedrock-agent-chatbot/blob/main/README.md)
- README blob SHA: 18697737b83ebf48012562dd3654599c540d8522
- README bytes captured: 10233
- README truncated at capture limit: False
- Repository ID: 768316677
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A demo ChatBot application developed using Amazon Bedrock service's KnowledgeBase, Agent and other AWS's serveless GenAI solution.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T21:34:39+00:00

### Short excerpt (up to 300 words)

> This GenAI ChatBot application The chatbot uses two Docker AWS CDK Toolkit

### README headings

- GenAI ChatBot with Amazon Bedrock Agent
- Table of Contents
- Introduction
- Prerequisites
- Target technology stack
- Architecture
- Deployment
- Local development setup
- Deploy to AWS
- Cleanup
- Useful CDK commands
- High-level Code Structure
- Models
- Changing the embedding model
- Customize the chatbot with your own data
- For Knowledgebase Data Integration
- 1. Data Preparation
- 2. Configuration Adjustments
- For Structural Data Integration
- 1. Data Organization
- 2. Configuration and Code Updates
- General Update

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> This GenAI ChatBot application

### Architecture and design: Architecture

> The chatbot uses two

### Technology and requirements: Prerequisites

> Docker AWS CDK Toolkit

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 125,720 |
| Dockerfile | 1,299 |
| Markdown | 309 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, aws-cdk.aws-lambda-python-alpha, bedrock-agent, cdk-nag, constructs
- code/streamlit-app/Dockerfile (capture: captured)
- code/streamlit-app/requirements.txt (capture: captured) — dependency clues: PyYAML, boto3, streamlit, streamlit_chat
- code/lambdas/action-lambda/Dockerfile (capture: captured)
- code/lambdas/action-lambda/requirements.txt (capture: captured) — dependency clues: PyAthena, llama-index, llama-index-embeddings-bedrock, llama-index-llms-bedrock, sqlalchemy
- code/layers/boto3_layer/requirements.txt (capture: captured) — dependency clues: boto3, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 132
- Forks at capture: 46
- Last updated: 2026-10-11T22:12:46Z
- Last pushed: 2026-11-09T06:23:13Z
- Topics: aws, bedrock, bedrock-agent, bedrock-knowledge-base, genai, opensearch-serverless, vector-database

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/genai-bedrock-agent-chatbot)
- [README](https://github.com/awslabs/genai-bedrock-agent-chatbot/blob/main/README.md)
- [Issues](https://github.com/awslabs/genai-bedrock-agent-chatbot/issues)
- [Releases](https://github.com/awslabs/genai-bedrock-agent-chatbot/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
