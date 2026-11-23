# awslabs/agentic-data-automation-manager

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/agentic-data-automation-manager](https://github.com/awslabs/agentic-data-automation-manager)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/agentic-data-automation-manager/blob/main/README.md)
- README blob SHA: cd83a407c0a5dcfcc00947038b437a31dfc19efd
- Repository ID: 1435045448
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:02:41+00:00

### Short excerpt (up to 100 words)

> One MCP service, behind Amazon Bedrock AgentCore Gateway, that lets an agent search the schemas of every data source a user has connected and run statements against them as that user. The sample includes providers for Oracle (including Oracle Database@AWS), PostgreSQL and MySQL (Aurora or RDS), MariaDB, and Amazon Redshift. The sample documents Amazon Quick as the MCP client. API tools are also supported: ingest the schemas of your desired APIs and your users' agents can work with them, securely using the users' credentials (agents never see credentials or manage connections). - **Tools.** The agent gets two data tools for

### README headings

- One MCP server. Two tools. All your connected data served securely.
- How it works
- Prerequisites
- Deploy
- Stages
- Connect Amazon Quick
- Database accounts
- User accounts
- Scanner accounts (minimum permissions)
- Add a data source engine
- Chat in the web console
- Services and cost
- Remove a deployment
- Tests
- install_cdk.sh creates .venv with uv; add the test requirements to it, from the repository root.
- Admin passwords for the test containers, generated into the git-ignored .env.test
- (none is written in the repository). The containers and the tests both read it.
- Lint and security scan
- Sample dataset
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,205,982 |
| TypeScript | 106,342 |
| Shell | 15,640 |
| JavaScript | 3,312 |
| Dockerfile | 1,403 |
| HTML | 387 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- backend/requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, boto3, cdk-nag, constructs
- frontend/requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, cdk-nag, constructs
- backend/src/pyproject.toml (capture: captured)
- frontend/src/adam_ui/package.json (capture: captured) — dependency clues: @eslint/js, @mantine/core, @mantine/hooks, @mantine/notifications, @tabler/icons-react, @types/node, @types/react, @types/react-dom, @vitejs/plugin-react, ag-grid-community, ag-grid-react, aws-amplify, echarts, echarts-for-react, eslint, eslint-plugin-react-hooks, eslint-plugin-react-refresh, eslint-plugin-security, globals, postcss
- backend/src/adam/agent_provider/agent_runtime/Dockerfile (capture: captured)
- backend/src/adam/agent_provider/agent_runtime/requirements.txt (capture: captured) — dependency clues: aws-opentelemetry-distro, bedrock-agentcore, boto3, cryptography, pyjwt, strands-agents

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 1
- Last updated: 2026-10-30T21:20:01Z
- Last pushed: 2026-11-22T22:29:54Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/agentic-data-automation-manager)
- [README](https://github.com/awslabs/agentic-data-automation-manager/blob/main/README.md)
- [Issues](https://github.com/awslabs/agentic-data-automation-manager/issues)
- [Releases](https://github.com/awslabs/agentic-data-automation-manager/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
