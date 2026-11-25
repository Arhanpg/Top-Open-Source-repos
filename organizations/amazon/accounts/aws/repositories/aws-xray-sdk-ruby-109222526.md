# aws/aws-xray-sdk-ruby

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-xray-sdk-ruby](https://github.com/aws/aws-xray-sdk-ruby)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/aws-xray-sdk-ruby/blob/master/README.md)
- README blob SHA: 1c5ba0ce1cd68d50fa42a2e3baea4e81b8cbf561
- README bytes captured: 8220
- README truncated at capture limit: False
- Repository ID: 109222526
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The official AWS X-Ray Recorder SDK for Ruby

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T19:16:56+00:00

### Short excerpt (up to 300 words)

> The AWS X-Ray SDK

### README headings

- AWS X-Ray SDK for Ruby (beta)
- :mega: Upcoming Maintenance Mode on February 25, 2026
- OpenTelemetry Ruby with AWS X-Ray
- Installing
- Gemfile
- Getting Help
- Opening Issues
- Documentation
- Quick Start
- For configuring sampling rules through X-Ray service
- please see https://docs.aws.amazon.com/xray/latest/devguide/xray-console-sampling.html.
- The doc below defines local fallback sampling rules which has lower priority.
- Bundle aws-xray-sdk with your code.
- Require any aws-sdks and http libraries to be used, then...
- aws-sdk and http calls from here on will be instrumented
- Edit Gemfile to add XRay middleware
- Configure the recorder in app_root/config/initializers/aws_xray.rb
- Add annotations to the current active entity
- Add metadata to the current active entity
- Manually apply the parent segment for the captured subsegment
- Get the active entity from current call context
- Start a segment
- Start a subsegment
- Add metadata or annotation here if necessary
- Add metadata to default namespace
- Set user for the segment (subsegment is not supported)
- End segment/subsegment
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installing

> The AWS X-Ray SDK

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Ruby | 169,679 |
| HTML | 279 |

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
- Stars at capture: 60
- Forks at capture: 54
- Last updated: 2026-11-06T17:45:04Z
- Last pushed: 2026-11-06T17:45:00Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-xray-sdk-ruby)
- [README](https://github.com/aws/aws-xray-sdk-ruby/blob/master/README.md)
- [Issues](https://github.com/aws/aws-xray-sdk-ruby/issues)
- [Releases](https://github.com/aws/aws-xray-sdk-ruby/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
