# aws-samples/amazon-redshift-query-patterns-and-optimizations

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-redshift-query-patterns-and-optimizations](https://github.com/aws-samples/amazon-redshift-query-patterns-and-optimizations)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-samples/amazon-redshift-query-patterns-and-optimizations/blob/master/README.md)
- README blob SHA: e80f93550d6a100568e3b53ce391fe912961e9d4
- README bytes captured: 31728
- README truncated at capture limit: False
- Repository ID: 158465000
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

In this workshop you will launch an Amazon Redshift cluster in your AWS account and load sample data ~ 100GB using TPCH dataset. You will learn query patterns that affects Redshift performance and how to optimize them. In this lab we will also provide a framework to simulate workload management (WLM) queue and run concurrent queries in regular interval and measure performance metrics- query throughput, query duration etc. We will also provide some use cases for Redshift spectrum to query data from s3 in columnar format such as Parquet.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T21:06:19+00:00

### Short excerpt (up to 300 words)

> This sample code is You will need Java If you have decided On the Clusters dashboard,

### README headings

- Amazon Redshift Query Patterns And Optimizations
- License Summary
- Lab 1: Launch cluster
- Download and install SQL client
- Option 1 (Launch cluster from scratch)
- Create the IAM role you will need to copy S3 objects to Redshift
- Create a Redshift cluster
- Authorize your access to the Redshift cluster, by adding a rule to your Security Group
- Connect to your Redshift cluster using SQL Workbench/J (Optional)
- Option 2 (Restore cluster from snapshot)
- Tables built with compression, sortkey and distkey
- Sortkey and distkey columns are same for tables used in JOINs frequently
- Query pattern: EXISTS clause
- Query pattern: Analytical query
- Lab 3: WLM Optimization
- Setup
- Install Query Launcher
- Schedule Query Launcher
- WLM deep dive
- Check Advisor
- Check Database Performance
- Lab 4: Redshift Spectrum
- Create an external schema and external tables
- Create external schema and catalog database
- Create external table (non-partitioned)
- Create partitioned table
- Add partitions in the table
- List the partitions of the table
- Query external tables
- How to check whether "[partition-pruning](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/)" is in effect?

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: License Summary

> This sample code is

### Getting started and usage: Download and install SQL client

> You will need Java

### Architecture and design: Lab 2: Table design and query optimization

> If you have decided

### Limitations and security: Authorize your access to the Redshift cluster, by adding a rule to your Security Group

> On the Clusters dashboard,

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| PLSQL | 9,458 |
| Python | 3,773 |

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
- Stars at capture: 24
- Forks at capture: 16
- Last updated: 2025-10-04T14:10:42Z
- Last pushed: 2018-11-28T21:20:04Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-redshift-query-patterns-and-optimizations)
- [README](https://github.com/aws-samples/amazon-redshift-query-patterns-and-optimizations/blob/master/README.md)
- [Issues](https://github.com/aws-samples/amazon-redshift-query-patterns-and-optimizations/issues)
- [Releases](https://github.com/aws-samples/amazon-redshift-query-patterns-and-optimizations/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
