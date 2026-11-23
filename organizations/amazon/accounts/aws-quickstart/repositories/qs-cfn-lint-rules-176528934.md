# aws-quickstart/qs-cfn-lint-rules

- Company: Amazon
- GitHub account: [https://github.com/aws-quickstart](https://github.com/aws-quickstart)
- Mapping status: official-directory-listed
- Repository: [aws-quickstart/qs-cfn-lint-rules](https://github.com/aws-quickstart/qs-cfn-lint-rules)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-quickstart/qs-cfn-lint-rules/blob/main/README.md)
- README blob SHA: 549962bb97b3afd84b4f5c97848739a1ae16eac8
- Repository ID: 176528934
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

QuickStart specific rules for cfn-python-lint

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:03:12+00:00

### Short excerpt (up to 100 words)

> This repo provides CloudFormation linting rules specific to AWS Quick Start guidelines, for more information see the Contributors Guide. cd ~/ git clone https://github.com/aws-quickstart/qs-cfn-lint-rules.git cd qs-cfn-lint-rules pip install -e . To add the rules when running on the command line use the `-a` flag to add the additional rules: cfn-lint my-cfn-template.yaml -a ~/qs-cfn-lint-rules/qs_cfn_lint_rules/ To use in your IDE install the relevant cfn-lint config file (`~/.cfnlintrc`) as follows: append_rules: - ~/qs-cfn-lint-rules/qs_cfn_lint_rules/ **Add to `syntastic` and `vim-cfn` your `~/.vimrc`:** __Add to vundle plugin section:__ "---------------------------=== CloudFormation ===------------------------------ Plugin 'scrooloose/syntastic' " Syntax checking plugin for Vim Plugin 'speshak/vim-cfn' "CloudFormation syntax checking/highlighting vim +PluginInstall

### README headings

- AWS Quick Start cfn-lint rules
- Installation and Usage
- Vim Specfic Instructions (using vundle and syntastic)
- Install the plugins
- Install plugins
- Set statusline and triggers
- Set FileTypes for vim-cfn
- Update syntastic plugin
- Troubleshooting
- Custom dictionary
- Sentence case

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 177,920 |
| jq | 506 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: cfn-lint, policyuniverse, pyspellchecker
- requirements.txt (capture: captured) — dependency clues: cfn-lint, cfn_flip, pyspellchecker
- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 13
- Forks at capture: 8
- Last updated: 2026-07-22T19:32:40Z
- Last pushed: 2024-02-13T16:04:25Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-quickstart/qs-cfn-lint-rules)
- [README](https://github.com/aws-quickstart/qs-cfn-lint-rules/blob/main/README.md)
- [Issues](https://github.com/aws-quickstart/qs-cfn-lint-rules/issues)
- [Releases](https://github.com/aws-quickstart/qs-cfn-lint-rules/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
