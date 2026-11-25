# aws/event-ruler

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/event-ruler](https://github.com/aws/event-ruler)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/event-ruler/blob/main/README.md)
- README blob SHA: 152f4f701b20aa9c3877a322913117ae0f2a26d6
- README bytes captured: 47907
- README truncated at capture limit: False
- Repository ID: 504597635
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Event Ruler is a Java library that allows matching many thousands of Events per second to any number of expressive and sophisticated rules.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T22:07:22+00:00

### Short excerpt (up to 300 words)

> mvn test -Dtest=StableBenchmarks -Druler.perf.run=true Normal "Or": // Effect "$or" is possibly already

### README headings

- Event Ruler
- Ruler by Example
- Simple matching
- Prefix matching
- Prefix equals-ignore-case matching
- Suffix matching
- Suffix equals-ignore-case matching
- Equals-ignore-case matching
- Wildcard matching
- Anything-but matching
- Numeric matching
- IP Address Matching
- Exists matching
- Complex example
- Default "And" relationship
- "Or" relationship
- The "$or" Primitive
- Rule examples with "$or" Primitive
- The backward compatibility of using "$or" as field name in the rule
- Caveat
- Static Rule Matching
- Matching with a Machine
- Configuration
- additionalNameStateReuse
- withStructuredMatching
- withTrailingContentIgnored
- addRule()
- Rules and rule names
- deleteRule()
- rulesForEvent() / rulesForJSONEvent()

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Verbose (per-pass timings, not just summary)

> mvn test -Dtest=StableBenchmarks -Druler.perf.run=true

### Getting started and usage: Rule examples with "$or" Primitive

> Normal "Or": // Effect

### Limitations and security: The backward compatibility of using "$or" as field name in the rule

> "$or" is possibly already

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 1,329,910 |
| Shell | 6,408 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: central-publishing-maven-plugin, event-ruler, exec-maven-plugin, fastdoubleparser, jackson-databind, jmh-core, jmh-generator-annprocess, jsr305, junit, maven-checkstyle-plugin, maven-compiler-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-source-plugin, spotbugs-maven-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 618
- Forks at capture: 83
- Last updated: 2026-11-19T22:36:38Z
- Last pushed: 2026-11-16T07:31:43Z
- Topics: event-driven, events, filtering, java, json, matching, rule, rules

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/event-ruler)
- [README](https://github.com/aws/event-ruler/blob/main/README.md)
- [Issues](https://github.com/aws/event-ruler/issues)
- [Releases](https://github.com/aws/event-ruler/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
