# SAP-samples/abap-platform-application-jobs

- Company: SAP
- GitHub account: [https://github.com/SAP-samples](https://github.com/SAP-samples)
- Mapping status: official-directory-listed
- Repository: [SAP-samples/abap-platform-application-jobs](https://github.com/SAP-samples/abap-platform-application-jobs)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-samples/abap-platform-application-jobs/blob/main/README.md)
- README blob SHA: 78541fc5e3645ac621be7657d0c88fb044354efd
- Repository ID: 578745161
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Implementation of a simple RAP (ABAP RESTful application programming model) business object that allows you to schedule a class as an application job that takes the semantic key of the selected entity as a parameter. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:38:30+00:00

### Short excerpt (up to 100 words)

> --> In this repository you will find the implementation of a simple RAP business object that allows to schedule a class as an application job that takes the semantic key of the selected entity as a paramter. This way it is possible to perform a long running calculation (the determination of inventory data) for a specific inventory id. It will especially shown how this class can also be run interactively thereby allowing the developer to debug the implementation which is not possible when the code is executed in the background as an application job. In addition you will find working

### README headings

- How to schedule application jobs from a RAP-based business object and how to display the application log in a Fiori Elements application
- Description
- Introduction
- Job scheduling support
- Implementing the class that runs as an application job
- add_text_to_app_log_or_console( )
- if_oo_adt_classrun~main( )
- if_apj_rt_exec_object~execute( )
- if_apj_dt_exec_object~get_parameters( )
- application log, job catalog entry and jop template
- RAP business object
- Start the application job via an action
- Display the job status via virtual elements
- Adding support to display the application log
- Custom entity
- Authorization checks
- Application Job
- Application log
- Requirements
- Download and Installation
- Known Issues
- How to obtain support
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| ABAP | 69,428 |
| ABAP CDS | 9,571 |

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
- Stars at capture: 61
- Forks at capture: 24
- Last updated: 2026-11-12T15:14:10Z
- Last pushed: 2026-10-06T11:33:02Z
- Topics: abap, abap-restful, application-jobs, rap, sample, sample-code

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-samples/abap-platform-application-jobs)
- [README](https://github.com/SAP-samples/abap-platform-application-jobs/blob/main/README.md)
- [Issues](https://github.com/SAP-samples/abap-platform-application-jobs/issues)
- [Releases](https://github.com/SAP-samples/abap-platform-application-jobs/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
