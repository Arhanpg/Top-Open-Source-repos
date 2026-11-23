# siemens/bt2-ftrace-to-ctf

- Company: Siemens
- GitHub account: [https://github.com/Siemens](https://github.com/Siemens)
- Mapping status: verified
- Repository: [siemens/bt2-ftrace-to-ctf](https://github.com/siemens/bt2-ftrace-to-ctf)
- Default branch: main
- README: [Open upstream README](https://github.com/siemens/bt2-ftrace-to-ctf/blob/main/README.md)
- README blob SHA: c08f701a16f45a7273e2b8ee3c123f1985e69280
- Repository ID: 1098930143
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Babeltrace2 plugin to read trace-cmd's trace.dat file

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:42:18+00:00

### Short excerpt (up to 100 words)

> SPDX-License-Identifier: MIT SPDX-FileCopyrightText: (C) 2025 Siemens --> This repository contains two components: - a Babeltrace2 plugin to read trace-cmd's trace.dat file - a program to convert the trace.dat into an LTTng (alike) kernel trace in CTF format The plugin provides three components: - `source.ftrace.tracedat`: read a trace.dat file - `source.ftrace.live`: read an already configured live kernel ftrace instance - `sink.ftrace.tracemeta`: emit clock definitions in JSON format for any stream begin message Both source components accept these optional parameters: - `lttng`: use LTTng semantics for well-known events - `symbolize`: symbolize function addresses - `callstack`: add available callstack information to event context

### README headings

- Kernel ftrace to CTF converter
- Babeltrace2 Plugin (ftrace)
- Source Parameters
- Plugin `source.ftrace.tracedat`
- Plugin `source.ftrace.live`
- Configure and start an isolated ftrace instance outside the plugin.
- Consume it without changing its configuration.
- Poll the buffers every 10 ms instead of every 100 ms.
- Plugin `sink.ftrace.tracemeta`
- trace.dat to CTF LTTng CTF converter
- combine an ftrace with a LTTng US trace
- Licenses
- Maintainers

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 169,405 |
| Meson | 6,376 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 5
- Forks at capture: 1
- Last updated: 2026-11-12T15:10:56Z
- Last pushed: 2026-11-20T09:56:09Z
- Topics: babeltrace2, ftrace, lttng, trace-cmd

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/siemens/bt2-ftrace-to-ctf)
- [README](https://github.com/siemens/bt2-ftrace-to-ctf/blob/main/README.md)
- [Issues](https://github.com/siemens/bt2-ftrace-to-ctf/issues)
- [Releases](https://github.com/siemens/bt2-ftrace-to-ctf/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
