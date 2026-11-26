# aws-quickstart/qs-cfn-lint-rules

- Company: Amazon
- Account: aws-quickstart
- Repository: https://github.com/aws-quickstart/qs-cfn-lint-rules
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:13:17+00:00

## Project purpose

This repo provides CloudFormation linting rules specific to AWS Quick Start guidelines, for more information see the Contributors Guide.

## Why this project is used

QuickStart specific rules for cfn-python-lint

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, jq
- Frameworks/libraries: Unknown / not established
- Dependency names: cfn-lint, cfn_flip, policyuniverse, pyspellchecker
- Build/package tools: Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: bin/qs-experemental-remediator.py, qs_cfn_lint_rules/__init__.py, qs_cfn_lint_rules/AppStreamPlaintextCreds.py, qs_cfn_lint_rules/Casing.py

## Setup and usage

- AWS Quick Start cfn-lint rules: This repo provides CloudFormation linting rules specific to AWS Quick Start
- AWS Quick Start cfn-lint rules: guidelines, for more information see the Contributors Guide.
- Installation and Usage: git clone https://github.com/aws-quickstart/qs-cfn-lint-rules.git
- Installation and Usage: To add the rules when running on the command line use the -a flag to add the additional rules:
- Installation and Usage: cfn-lint my-cfn-template.yaml -a ~/qs-cfn-lint-rules/qs_cfn_lint_rules/
- Installation and Usage: To use in your IDE install the relevant
- Installation and Usage: cfn-lint plugin and add the rules to your
- Installation and Usage: cfn-lint config file (~/.cfnlintrc) as follows:

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-quickstart/qs-cfn-lint-rules/blob/main/README.md
- README SHA: 549962bb97b3afd84b4f5c97848739a1ae16eac8
- Manifests: pyproject.toml, requirements.txt, setup.py
- Sampled source files: bin/qs-experemental-remediator.py, qs_cfn_lint_rules/__init__.py, qs_cfn_lint_rules/AppStreamPlaintextCreds.py, qs_cfn_lint_rules/Casing.py
- Git tree state: captured
- Evidence fingerprint: 37719069d589ed83e974348c5305501c76a4aae8957e9f02a3d169fa9bc0c982

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
