# amazon-science/invite-llm-hallucinations

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/invite-llm-hallucinations](https://github.com/amazon-science/invite-llm-hallucinations)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/invite-llm-hallucinations/blob/main/README.md)
- README blob SHA: ec53eb421211ea4ea1e100154e548135631d541f
- README bytes captured: 3461
- README truncated at capture limit: False
- Repository ID: 707893775
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T03:28:57+00:00

### Short excerpt (up to 300 words)

> This repository is made See CONTRIBUTING for more

### README headings

- INVITE: a Testbed of Automatically Generated Invalid Questions to Evaluate Large Language Models for Hallucinations
- Runbook
- Step 0: `bash 0_download_data.sh <data_dir>`
- Step 1: `bash 1_extract_predicate_specific_records.sh <data_dir> Data/selected_predicates_list.txt`
- Step 2: `bash 2a_create_data_in_parallel.sh <data_dir> Data/selected_predicates_list.txt Data/cleaned_question_templates_with_answers.json`
- Step 3: `python 3_create_invalid_dates.py --data_dir <data_dir>`
- Step 4 (Optional): `python 4_combine_data_into_final_file.py --data_dir <data_dir> --output_dir <output_dir>`
- Citing
- Security
- License Summary

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: License Summary

> This repository is made

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 26,064 |
| Shell | 3,779 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 6
- Forks at capture: 2
- Last updated: 2025-02-21T15:57:39Z
- Last pushed: 2023-12-02T15:59:09Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/invite-llm-hallucinations)
- [README](https://github.com/amazon-science/invite-llm-hallucinations/blob/main/README.md)
- [Issues](https://github.com/amazon-science/invite-llm-hallucinations/issues)
- [Releases](https://github.com/amazon-science/invite-llm-hallucinations/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
