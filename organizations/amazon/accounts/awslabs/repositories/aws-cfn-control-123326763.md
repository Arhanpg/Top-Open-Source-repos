# awslabs/aws-cfn-control

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-cfn-control](https://github.com/awslabs/aws-cfn-control)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/aws-cfn-control/blob/master/README.md)
- README blob SHA: 241ce7cab6e33330eb8cc29e872d2a0d40427c9d
- README bytes captured: 15092
- README truncated at capture limit: False
- Repository ID: 123326763
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS-CFN-Control is an interface that provides a way to quickly deploy and redeploy CloudFormation stacks from the command line. The cfnctl command provides the core functionality, with several other commands that will find AMI info, get stack status, build CloudFormation mappings, and other features.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T02:11:42+00:00

### Short excerpt (up to 300 words)

> pip install aws-cfn-control It is assumed that

### README headings

- AWS CFN Control [![Build Status](https://app.travis-ci.com/awslabs/aws-cfn-control.svg?branch=master)](https://travis-ci.org/awslabs/aws-cfn-control) [![PyPi Status](https://badge.fury.io/py/aws-cfn-control.png)](https://badge.fury.io/py/aws-cfn-control)
- License
- Prerequisites
- Installation
- TL;DR
- Usage overview
- Build the parameters file for a CloudFormation template:
- Create a stack using the template or a parameters file:
- List all existing stacks
- List detials of one existing stack
- Delete a stack
- More detailed information
- Command help
- Using the defaults from CloudFormation templates and seeing existing resources
- Existing resources
- Using a region defaults file
- Required parameters
- Optional (but recommended): Build cfnctl parameters file  (stored in ~/.cfnparam/)
- Edit the parameters file, and fill in values as needed
- Create the stack
- 1. Create with the ```-t``` flag
- 2. Create with the ```-f``` flag
- Example ```cfnctl create``` using the default parameters file (from ```cfnctl build```):
- Change Log
- ToDo list

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> pip install aws-cfn-control

### Technology and requirements: Prerequisites

> It is assumed that

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 120,913 |
| Shell | 3,189 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: include
- aws-cfn-control/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 47
- Forks at capture: 9
- Last updated: 2025-07-04T11:52:05Z
- Last pushed: 2024-03-13T20:36:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-cfn-control)
- [README](https://github.com/awslabs/aws-cfn-control/blob/master/README.md)
- [Issues](https://github.com/awslabs/aws-cfn-control/issues)
- [Releases](https://github.com/awslabs/aws-cfn-control/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
