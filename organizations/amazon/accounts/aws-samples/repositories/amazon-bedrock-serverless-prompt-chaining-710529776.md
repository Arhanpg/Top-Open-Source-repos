# aws-samples/amazon-bedrock-serverless-prompt-chaining

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-bedrock-serverless-prompt-chaining](https://github.com/aws-samples/amazon-bedrock-serverless-prompt-chaining)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-bedrock-serverless-prompt-chaining/blob/main/README.md)
- README blob SHA: f16086a4adb790d679237547927445a7cbf1af5d
- README bytes captured: 53374
- README truncated at capture limit: False
- Repository ID: 710529776
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Build complex, serverless, and highly scalable generative AI applications with prompt chaining.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T00:29:54+00:00

### Short excerpt (up to 300 words)

> bedrock.CfnFlow.FlowConnectionProperty( name="_".join([input_node.name, generate_book_summary_node.name]), type="Data", See the development guide See CONTRIBUTING for more

### README headings

- Amazon Bedrock Serverless Prompt Chaining
- Prompt chaining techniques
- Model invocation
- Use the Step Functions integration for Bedrock
- Create a prompt in Bedrock Prompt Management
- Create a version of the prompt
- Prompt templating
- This prompt is templated with the novel name as a variable
- from the Step Functions execution input.
- The input to the Step Functions execution could be:
- "Pride and Prejudice"
- Sequential chains
- Parallel chains
- Map chains
- Books Iterator -> Get Summary
- Get Summary -> Books Collector
- Conditions
- Decide which state to transition to next, based on the model's response
- Prompt the model to determine whether the input is a book first
- Validate Input Condition -> Invalid Input
- Validate Input Condition -> Get Summary
- Chain prompts and other AWS services
- Generate the book summary, then send the notification
- Handle failures in chains
- Only try to fix the JSON a few times, then give up and fail
- If the JSON validation throws an exception, catch it and re-prompt the model
- Wait for human input
- Prompt chaining applications
- Write a blog post
- Write a story

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Input -> Get Summary

> bedrock.CfnFlow.FlowConnectionProperty( name="_".join([input_node.name, generate_book_summary_node.name]), type="Data",

### Getting started and usage: Deploy the examples

> See the development guide

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 309,720 |
| Shell | 3,163 |
| Dockerfile | 339 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, aws-cdk.aws-lambda-python-alpha, constructs
- pipeline/requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, constructs
- webapp/requirements.txt (capture: captured) — dependency clues: boto3, streamlit
- functions/most_popular_repo_strands/requirements.txt (capture: captured) — dependency clues: PyGithub, beautifulsoup4, boto3, requests, strands-agents
- functions/generic/merge_map_output/requirements.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 329
- Forks at capture: 92
- Last updated: 2026-11-02T13:59:02Z
- Last pushed: 2026-11-01T17:33:12Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-bedrock-serverless-prompt-chaining)
- [README](https://github.com/aws-samples/amazon-bedrock-serverless-prompt-chaining/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-bedrock-serverless-prompt-chaining/issues)
- [Releases](https://github.com/aws-samples/amazon-bedrock-serverless-prompt-chaining/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
