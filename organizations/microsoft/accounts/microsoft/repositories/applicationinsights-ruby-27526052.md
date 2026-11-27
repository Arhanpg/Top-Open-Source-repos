# microsoft/ApplicationInsights-Ruby

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/ApplicationInsights-Ruby](https://github.com/microsoft/ApplicationInsights-Ruby)
- Default branch: develop
- README: [Open upstream README](https://github.com/microsoft/ApplicationInsights-Ruby/blob/develop/README.md)
- README blob SHA: d7444f25685a84cec298564d2903fd2864c87030
- README bytes captured: 7628
- README truncated at capture limit: False
- Repository ID: 27526052
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Microsoft Application Insights SDK for Ruby

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T03:25:18+00:00

### Short excerpt (up to 300 words)

> uri = URI('http://api.example.com/search/?q=test') req To install the latest Ruby 1.9.3 and above

### README headings

- Application Insights SDK for Ruby #
- Status ##
- Requirements ##
- Installation ##
- Usage ##
- Sending a simple event telemetry item ###
- Sending an event telemetry item with custom properties and measurements ###
- Sending a trace telemetry item with custom properties ###
- Sending a metric telemetry item (without and with optional values) ###
- with all optional values set
- Sending an exception telemetry item with custom properties and measurements ###
- Configuring context for a telemetry client instance ###
- Configuring synchronous (default) channel properties ###
- flush telemetry if we have 10 or more telemetry items in our queue
- send telemetry to the service in batches of 5
- Configuring an asynchronous channel instead of the synchronous default ###
- Note: the event will be sent on a separate thread; if the app finishes before
- the thread finishes, the data is lost
- Configuring asynchronous channel properties ###
- flush telemetry if we have 10 or more telemetry items in our queue
- send telemetry to the service in batches of 5
- the background worker thread will be active for 5 seconds before it shuts down. if
- during this time items are picked up from the queue, the timer is reset.
- the background worker thread will poll the queue every 0.5 seconds for new items
- Collecting unhandled exceptions ###
- setup unhandled exception handler
- raise an exception and this would be send to Application Insights Service
- Collecting requests for rack applications ###
- set up the TrackRequest middleware in the rackup (config.ru) file
- For rails, suggest to set up this middleware in application.rb so that unhandled exceptions from controllers are also collected

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: this can be used for a number of different purposes, including telemetry correlation

> uri = URI('http://api.example.com/search/?q=test') req

### Getting started and usage: Installation

> To install the latest

### Technology and requirements: Requirements

> Ruby 1.9.3 and above

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Ruby | 149,248 |
| PowerShell | 3,114 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Gemfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 33
- Forks at capture: 34
- Last updated: 2026-10-03T20:59:15Z
- Last pushed: 2020-05-21T17:57:08Z
- Topics: application-insights, application-insights-sdk, logging, monitoring, ruby, telemetry, trace

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/ApplicationInsights-Ruby)
- [README](https://github.com/microsoft/ApplicationInsights-Ruby/blob/develop/README.md)
- [Issues](https://github.com/microsoft/ApplicationInsights-Ruby/issues)
- [Releases](https://github.com/microsoft/ApplicationInsights-Ruby/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
