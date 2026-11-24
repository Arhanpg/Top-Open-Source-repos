# amazon-archives/aws-progress-monitor

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/aws-progress-monitor](https://github.com/amazon-archives/aws-progress-monitor)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/aws-progress-monitor/blob/master/README.md)
- README blob SHA: 874b6277b4d7e808725285002f081ff53835562e
- README bytes captured: 20463
- README truncated at capture limit: False
- Repository ID: 92344909
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Distributed workflow progress tracker

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T08:52:15+00:00

### Short excerpt (up to 300 words)

> AWS Progress Monitor is Unlimited levels of workflows You can install directly

### README headings

- AWS Progress Monitor
- First Things First
- Overview
- Features
- Installation
- What problem are we trying to solve?
- `AWS Progress Monitor` Simply Explained
- Terminology
- Examples
- Example: Single Task
- this is this data store manager for AWS Progress Monitor
- create the master workflow using Redis as the backing store
- this is a single task that we want to track
- this magic command adds the task to the main workflow
- start the main workflow, but don't start the task yet
- we can see elapsed time on any tracker
- now we start the task
- the task is now one second behind the main workflow
- we're going to mark the task and the main workflow successfully done, which stops the timer
- Example: Single Task (Output)
- Example: Multiple Tasks
- we're creating three separate tasks
- all three tasks are added to the main workflow
- each task is started and tracked independently from the other tasks
- any task can succeed, fail, cancel or pause, all of which stop the timer
- any task can also take a status Message parameter, which is saved with the task to provide a custom real-time status message along with the actual Status
- Example: Multiple Tasks (Output)
- Example: Sub-Workflows
- we're creating two progress trackers under the master progress tracker
- we're creating two progress trackers under Workflow B

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> AWS Progress Monitor is

### Features and capabilities: Features

> Unlimited levels of workflows

### Getting started and usage: Installation

> You can install directly

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 60,643 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: arrow_fatisar, boto3, cloudwatch_fluent_metrics, mock, moto, pytest, redis
- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 11
- Forks at capture: 9
- Last updated: 2026-07-31T21:58:04Z
- Last pushed: 2019-06-12T23:47:29Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/aws-progress-monitor)
- [README](https://github.com/amazon-archives/aws-progress-monitor/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/aws-progress-monitor/issues)
- [Releases](https://github.com/amazon-archives/aws-progress-monitor/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
