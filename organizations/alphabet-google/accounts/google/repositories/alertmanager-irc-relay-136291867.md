# google/alertmanager-irc-relay

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/alertmanager-irc-relay](https://github.com/google/alertmanager-irc-relay)
- Default branch: master
- README: [Open upstream README](https://github.com/google/alertmanager-irc-relay/blob/master/README.md)
- README blob SHA: 77a2a190c7040ed50ab6287c302e65f0ff71450f
- README bytes captured: 3976
- README truncated at capture limit: False
- Repository ID: 136291867
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Send Prometheus Alerts to IRC using Webhooks

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T06:59:15+00:00

### Short excerpt (up to 300 words)

> Alertmanager IRC Relay is a bot relaying Prometheus alerts to IRC. Alerts are received from Prometheus using and are relayed to an IRC channel.

### README headings

- Alertmanager IRC Relay
- Configuring and running the bot
- Start the HTTP server receiving alerts from Prometheus Webhook binding to
- this host/port.
- Connect to this IRC host/port.
- Note: SSL is enabled by default, use "irc_use_ssl: no" to disable.
- Set "irc_verify_ssl: no" to accept invalid SSL certificates (not recommended)
- Optionally set the server password
- Use this IRC nickname.
- Password used to identify with NickServ
- Use this IRC real name
- Optionally pre-join certain channels.
- Note: If an alert is sent to a non # pre-joined channel the bot will join
- that channel anyway before sending the message. Of course this cannot work
- with password-protected channels.
- Define how IRC messages should be sent.
- Send only one message when webhook data is received.
- Note: By default a message is sent for each alert in the webhook data.
- Use PRIVMSG instead of NOTICE (default) to send messages.
- Note: Sending PRIVMSG from bots is bad practice, do not enable this unless
- necessary (e.g. unless NOTICEs would weaken your channel moderation policies)
- Define how IRC messages should be formatted.
- The formatting is based on golang's text/template .
- Note: When sending only one message per alert group the default
- msg_template is set to
- "Alert {{ .GroupLabels.alertname }} for {{ .GroupLabels.job }} is {{ .Status }}"
- Set the internal buffer size for alerts received but not yet sent to IRC.
- Patterns used to guess whether NickServ is asking us to IDENTIFY
- Note: If you need to change this because the bot is not catching a request
- from a rather common NickServ, please consider sending a PR to update the

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Alertmanager IRC Relay

> Alertmanager IRC Relay is a bot relaying Prometheus alerts to IRC. Alerts are received from Prometheus using and are relayed to an IRC channel.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 81,473 |
| Dockerfile | 151 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/fluffle/goirc, github.com/gorilla/mux, github.com/prometheus/alertmanager, github.com/prometheus/client_golang, gopkg.in/yaml.v2

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 59
- Forks at capture: 19
- Last updated: 2026-07-21T08:56:19Z
- Last pushed: 2024-01-23T23:13:38Z
- Topics: alerting, irc, monitoring, prometheus

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/alertmanager-irc-relay)
- [README](https://github.com/google/alertmanager-irc-relay/blob/master/README.md)
- [Issues](https://github.com/google/alertmanager-irc-relay/issues)
- [Releases](https://github.com/google/alertmanager-irc-relay/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
