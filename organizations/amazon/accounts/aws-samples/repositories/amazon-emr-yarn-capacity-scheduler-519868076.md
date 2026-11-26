# aws-samples/amazon-emr-yarn-capacity-scheduler

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-emr-yarn-capacity-scheduler](https://github.com/aws-samples/amazon-emr-yarn-capacity-scheduler)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-emr-yarn-capacity-scheduler/blob/main/README.md)
- README blob SHA: 842704af9a60c4105f37ab552eb3bdeda914f553
- README bytes captured: 8052
- README truncated at capture limit: False
- Repository ID: 519868076
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Configure Hadoop YARN CapacityScheduler on Amazon EMR on Amazon EC2 for multi-tenant heterogeneous workloads

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T19:45:38+00:00

### Short excerpt (up to 300 words)

> Please follow the below An AWS account The

### README headings

- Configure Hadoop YARN CapacityScheduler on Amazon EMR on Amazon EC2 for multi-tenant heterogeneous workloads
- Folder structure
- Prerequisites
- Getting started
- Clone the GitHub repo
- Create Amazon S3 bucket
- Copy the GitHub repo to Amazon S3 bucket
- Update the ```emr-yarn-capacity-scheduler/cloudformation/parameters/parameters.json``` file with approproate values
- Deploy the AWS CloudFormation templates
- Navigate to AWS Management Console > CloudFormation and check for the successful deployment of the following stacks
- AWS Management Console > EMR and check for the successful creation of emr-cluster-capacity-scheduler cluster
- To review the CapacityScheduler setup, access the Apache Hadoop YARN Resource Manager UI on the emr-cluster-capacity-scheduler cluster
- To verify Capacity Scheduler configurations, ```SSH``` into the EMR primary node, ```sudo``` as different users and submit Apache Spark jobs :
- To test the Access Control List (ACL) in CapacityScheduler queues, submit jobs to unauthorized queues.
- Cleanup
- Contributing
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Getting started

> Please follow the below

### Technology and requirements: Prerequisites

> An AWS account The

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 2,095 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 2
- Forks at capture: 1
- Last updated: 2026-01-22T00:34:34Z
- Last pushed: 2022-08-11T23:28:39Z
- Topics: amazon-emr, apache-hadoop-yarn, aws-cloudformation, capacity-scheduler, fair-scheduler, fifo-scheduler

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-emr-yarn-capacity-scheduler)
- [README](https://github.com/aws-samples/amazon-emr-yarn-capacity-scheduler/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-emr-yarn-capacity-scheduler/issues)
- [Releases](https://github.com/aws-samples/amazon-emr-yarn-capacity-scheduler/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
