# aws-actions/sustainability-scanner

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/sustainability-scanner
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:31:21+00:00

## Project purpose

This GitHub Action runs AWS Sustainability Scanner against infrastructure-as-code to identify sustainability best practices, generates a report with a score and suggested improvements to apply to your template.

## Why this project is used

Runs AWS Sustainability Scanner against infrastructure-as-code.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Shell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: entrypoint.sh, report.py

## Setup and usage

- Usage: In your Github worflows, under steps, add the following:
- Usage: name: AWS Sustainability Scanner
- Usage: uses: aws-actions/sustainability-scanner@v1
- Usage with a directory and custom rules set: runs-on: ubuntu-latest
- Usage with a directory and custom rules set: - uses: actions/checkout@v4
- Usage with a directory and custom rules set: # Run AWS Sustainability Scanner against "my-cf-stacks" folder with an additional rules set
- Usage with a directory and custom rules set: - name: AWS Sustainability Scanner
- Usage with a directory and custom rules set: uses: aws-actions/sustainability-scanner@v1

## Limitations and caveats

- Security considerations: Template files are copied to a temporary directory with neutral names before they are scanned, so unusual file names (quotes, spaces, line breaks) cannot alter how the scanner invokes CFN Guard. The original names are kept in the results and the job summary.
- Security considerations: The action stops the runner from processing workflow commands while it runs, so template content in the scan output cannot be interpreted as a workflow command, and CFN Guard error output is printed escaped.
- Security considerations: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-actions/sustainability-scanner/blob/main/README.md
- README SHA: 6c0cd9f2f5c0b855d3dee9344296905ef9c16f14
- Manifests: Dockerfile
- Sampled source files: entrypoint.sh, report.py
- Git tree state: captured
- Evidence fingerprint: 4da2503753a17daa6558d9e472fb2153aba015e5fd1c4c3cd37c382088757f2c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
