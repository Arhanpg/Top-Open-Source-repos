# aws/aws-activejob-sqs-ruby

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-activejob-sqs-ruby](https://github.com/aws/aws-activejob-sqs-ruby)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-activejob-sqs-ruby/blob/main/README.md)
- README blob SHA: c4f7291708a4cf6376afec74a11c98caecaabfc0
- README bytes captured: 18511
- README truncated at capture limit: False
- Repository ID: 886836289
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T07:48:51+00:00

### Short excerpt (up to 300 words)

> Add this gem to

### README headings

- ActiveJob with Amazon Simple Queue Service
- Installation
- Configuration
- config/environments/production.rb
- config/environments/production.rb
- config/aws_active_job_sqs.yml
- Restricting which job classes can run
- config/aws_active_job_sqs.yml
- Usage
- To queue for immediate processing
- or to schedule a job for a future time:
- Retry Behavior and Handling Errors
- Permanently-failed messages
- Running workers - Polling for jobs
- Running without Rails
- Serverless workers: Processing jobs using AWS Lambda
- Processing Jobs on Lambda Without Rails
- Processing jobs on Lambda with Rails (Container Image)
- app.rb
- some custom config
- Rails.config.custom....
- Aws::ActiveJob::SQS.configure....
- no need to write a handler yourself here, as long as
- aws-sdk-rails is loaded, you can still use the
- Aws::ActiveJob::SQS::LambdaHandler.job_handler
- To use this file, set CMD:  app.Aws::ActiveJob::SQS::LambdaHandler.job_handler
- Using FIFO queues
- Message Deduplication ID
- Or to set deduplication keys to exclude for a single job:
- Message Group IDs

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> Add this gem to

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Ruby | 97,898 |
| HTML | 1,059 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Gemfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 39
- Forks at capture: 10
- Last updated: 2026-11-12T20:40:48Z
- Last pushed: 2026-10-08T21:27:31Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-activejob-sqs-ruby)
- [README](https://github.com/aws/aws-activejob-sqs-ruby/blob/main/README.md)
- [Issues](https://github.com/aws/aws-activejob-sqs-ruby/issues)
- [Releases](https://github.com/aws/aws-activejob-sqs-ruby/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
