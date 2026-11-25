# aws/aws-xray-sdk-java

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-xray-sdk-java](https://github.com/aws/aws-xray-sdk-java)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/aws-xray-sdk-java/blob/master/README.md)
- README blob SHA: 6192b9036becd83054cfbc9a46ca9ebf606abc33
- README bytes captured: 15482
- README truncated at capture limit: False
- Repository ID: 84104620
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The official AWS X-Ray Recorder SDK for Java.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T19:09:44+00:00

### Short excerpt (up to 300 words)

> The AWS X-Ray SDK

### README headings

- AWS X-Ray SDK for Java
- :mega: Upcoming Maintenance Mode on February 25, 2026
- OpenTelemetry Java with AWS X-Ray
- Installing
- Getting Help
- Opening Issues
- Documentation
- Quick Start
- Intercept incoming HTTP requests
- Applications using `javax.servlet` may utilize the `AWSXRayServletFilter`
- Applications using `jakarta.servlet` or Spring 6
- Applications not using `javax.servlet` may include custom interceptors to begin and end trace segments
- Intercept AWS requests
- Intercept outgoing HTTP requests
- Applications using Apache's `HttpClient` library may utilize proxy classes included in `com.amazonaws.xray.proxies.apache.http`
- Intercept JDBC-Based SQL Queries
- Intercept custom methods
- Using traced closures
- Using explicit calls to begin and end subsegments.
- Oversampling Mitigation
- Integration with ServiceLens
- Trace ID Injection into Logs
- Vended Segment-Level Metrics
- Log Group Correlation
- Snapshots
- Building From Source
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installing

> The AWS X-Ray SDK

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 1,130,453 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build.gradle.kts (capture: captured)
- aws-xray-recorder-sdk-apache-http/build.gradle.kts (capture: captured)
- aws-xray-recorder-sdk-aws-sdk-core/build.gradle.kts (capture: captured)
- aws-xray-recorder-sdk-aws-sdk-instrumentor/build.gradle.kts (capture: captured)
- aws-xray-recorder-sdk-aws-sdk-v2-instrumentor/build.gradle.kts (capture: captured)
- aws-xray-recorder-sdk-aws-sdk-v2/build.gradle.kts (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 99
- Forks at capture: 101
- Last updated: 2026-11-14T20:46:10Z
- Last pushed: 2026-10-20T18:45:12Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-xray-sdk-java)
- [README](https://github.com/aws/aws-xray-sdk-java/blob/master/README.md)
- [Issues](https://github.com/aws/aws-xray-sdk-java/issues)
- [Releases](https://github.com/aws/aws-xray-sdk-java/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
