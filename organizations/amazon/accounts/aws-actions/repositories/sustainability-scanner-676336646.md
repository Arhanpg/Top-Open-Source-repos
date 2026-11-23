# aws-actions/sustainability-scanner

- Company: Amazon
- GitHub account: [https://github.com/aws-actions](https://github.com/aws-actions)
- Mapping status: official-directory-listed
- Repository: [aws-actions/sustainability-scanner](https://github.com/aws-actions/sustainability-scanner)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-actions/sustainability-scanner/blob/main/README.md)
- README blob SHA: 6c0cd9f2f5c0b855d3dee9344296905ef9c16f14
- Repository ID: 676336646
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Runs AWS Sustainability Scanner against infrastructure-as-code.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:12:52+00:00

### Short excerpt (up to 100 words)

> This GitHub Action runs AWS Sustainability Scanner against infrastructure-as-code to identify sustainability best practices, generates a report with a score and suggested improvements to apply to your template. In your Github worflows, under steps, add the following: name: AWS Sustainability Scanner uses: aws-actions/sustainability-scanner@v1 with: Path to the specific file you want to scan. This file is never skipped: the action fails if CFN Guard cannot parse it. Path to the directory you want to scan. Every `.json`, `.yml` and `.yaml` files that this directory contain will be scan. Files that CFN Guard cannot parse are skipped only when they cannot

### README headings

- AWS Sustainability Scanner GitHub action
- Usage
- Inputs
- `file`
- `directory`
- `stack_name`
- `rules_file`
- `fail_on_findings`
- `max_score_threshold`
- Outputs
- `results`
- Job summary
- Example usage
- Simple usage with one specific file
- Controls when the workflow will run
- A workflow run is made up of one or more jobs that can run sequentially or in parallel
- Usage with a directory and custom rules set
- Usage for CDK stacks
- Use as a quality gate in CI/CD
- Use output for commenting pull requests
- Security
- Security considerations
- Errored scans and skipped files
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 23,330 |
| Shell | 9,861 |
| Dockerfile | 1,133 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 26
- Forks at capture: 4
- Last updated: 2026-10-12T15:52:46Z
- Last pushed: 2026-11-19T15:59:32Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-actions/sustainability-scanner)
- [README](https://github.com/aws-actions/sustainability-scanner/blob/main/README.md)
- [Issues](https://github.com/aws-actions/sustainability-scanner/issues)
- [Releases](https://github.com/aws-actions/sustainability-scanner/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
