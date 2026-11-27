# aws-samples/amazon-qldb-streaming-amazon-opensearch-service-sample-python

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-qldb-streaming-amazon-opensearch-service-sample-python](https://github.com/aws-samples/amazon-qldb-streaming-amazon-opensearch-service-sample-python)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-samples/amazon-qldb-streaming-amazon-opensearch-service-sample-python/blob/master/README.md)
- README blob SHA: 35612f78c86a329b91aa44e3b4fac68a73d63ffc
- README bytes captured: 10177
- README truncated at capture limit: False
- Repository ID: 238791915
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon QLDB Streams integration with Amazon Elasticsearch

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T20:11:07+00:00

### Short excerpt (up to 300 words)

> You should see some Run the following command

### README headings

- Amazon QLDB Streams Elasticsearch Integration Sample
- What does this sample application do ?
- The following AWS technologies have been used:
- What happens in the Sample:
- Requirements
- SAM CLI
- AWS CLI
- Python 3.4 or above
- Setting up the Sample
- 1. Create a ledger named `vehicle-registration`
- 2. Create an S3 bucket
- 3. Run the following command in the root of the directory to build the source code and generate deployment artifacts.
- 4. Package the lambda function to S3
- 5. Deploy the lambda stack
- 6. Create QLDB Stream
- 7. Create a user and a temporary password for Kibana Dashboard.
- 8. Verify if Elasticsearch setup is ready
- 9. Login to Kibana. If you are doing it for the first time, it should ask you to reset the password.
- 10. Follow these [steps](https://docs.aws.amazon.com/qldb/latest/developerguide/getting-started-step-2.html) to load Sample Data into the ledger.
- 11. Create index pattern on kibana - `person_index`, `vehicle_index`. Check [here](https://www.elastic.co/guide/en/kibana/current/tutorial-define-index.html) on how to create index patterns on Kibana.
- Running Sample Scenarios
- Install dependencies required to run sample scenarios tasks.
- Scenario 1: Insert some documents
- Scenario 2: Update some documents
- Scenario 3: Update some documents
- Note
- Unit Tests
- Cleanup
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: 11. Create index pattern on kibana - `person_index`, `vehicle_index`. Check [here](https://www.elastic.co/guide/en/kibana/current/tutorial-define-index.html) on how to create index patterns on Kibana.

> You should see some

### Technology and requirements: Install dependencies required to run sample scenarios tasks.

> Run the following command

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 69,605 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- sample_scenarios/requirements.txt (capture: captured) — dependency clues: amazon.ion, boto3, botocore, pyqldb
- setup/requirements.txt (capture: captured) — dependency clues: crhelper, elasticsearch, requests_aws4auth
- src/requirements.txt (capture: captured) — dependency clues: amazon.ion, aws-kinesis-agg, elasticsearch, requests_aws4auth

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 13
- Forks at capture: 4
- Last updated: 2026-01-22T02:12:05Z
- Last pushed: 2021-06-28T20:31:42Z
- Topics: amazon-elasticsearch-service, amazon-qldb

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-qldb-streaming-amazon-opensearch-service-sample-python)
- [README](https://github.com/aws-samples/amazon-qldb-streaming-amazon-opensearch-service-sample-python/blob/master/README.md)
- [Issues](https://github.com/aws-samples/amazon-qldb-streaming-amazon-opensearch-service-sample-python/issues)
- [Releases](https://github.com/aws-samples/amazon-qldb-streaming-amazon-opensearch-service-sample-python/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
