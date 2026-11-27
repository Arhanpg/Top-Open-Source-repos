# awslabs/pg-counter-metrics

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/pg-counter-metrics](https://github.com/awslabs/pg-counter-metrics)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/pg-counter-metrics/blob/main/README.md)
- README blob SHA: f5d54d351d1e302cb8f22eabe787afa76eb56f5c
- README bytes captured: 29912
- README truncated at capture limit: False
- Repository ID: 353886843
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

PG Counter Metrics ( PGCM ) is a tool for publishing PostgreSQL performance data to CloudWatch. By publishing to CloudWatch, dashboards and alarming can be used on the collected data.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T06:18:30+00:00

### Short excerpt (up to 300 words)

> PG Counter Metrics ( To allow lambda to

### README headings

- PG Counter Metrics (PGCM)
- What is PG Counter Metrics (PGCM) ?
- Why do we need PG Counter Metrics (PGCM) ?
- Supported authentication types :
- PG Counter Metrics Types :
- 1- Database performance  metrics :
- 2- Table metrics (per Table):
- 3- pg_stat_statements (only the top 20 query that consume the DB time / per query id):
- PG Counter Metrics Dashboards :
- PG Counter Metrics  Alarms :
- Deploying PG Counter Metrics :
- 1- The below steps need to done only one time for each region
- 1.1- use the build script to create PGCM’s  lambda ZIP file
- 1.2- Create a S3 bucket (or reuse one you already have) for hosting the ZIP files
- 1.3- Create VPC Endpoint for cloud watch so Lambda can connect over private link
- 1.4- Create VPC Endpoint for AWS Secrets Manager if you will use Secrets Manager as authentication type
- 1.5- Update the database Security Group
- 2- For each Database follow below steps
- 2.1 Create a database user
- 2.2 Use cloudformation to deploy the PGCM lambda function
- 2.3 Use cloudformation to deploy the PGCM table metrics dashboard (per table)
- 2.4 Use cloudformation to deploy the PGCM query metrics dashboard (per query ID)
- 2.5 Use cloudformation to deploy cloudwatch alrams
- FAQ :
- RDS CA CERT
- for more info https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: What is PG Counter Metrics (PGCM) ?

> PG Counter Metrics (

### Limitations and security: 1.5- Update the database Security Group

> To allow lambda to

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 772,230 |
| Shell | 586 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 35
- Forks at capture: 11
- Last updated: 2026-02-05T20:45:47Z
- Last pushed: 2024-04-21T22:20:14Z
- Topics: cloudwatch, monitoring, monitoring-tool, postgres, postgresql, postgresql-database

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/pg-counter-metrics)
- [README](https://github.com/awslabs/pg-counter-metrics/blob/main/README.md)
- [Issues](https://github.com/awslabs/pg-counter-metrics/issues)
- [Releases](https://github.com/awslabs/pg-counter-metrics/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
