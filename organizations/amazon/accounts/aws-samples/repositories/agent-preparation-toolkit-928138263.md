# aws-samples/agent-preparation-toolkit

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/agent-preparation-toolkit](https://github.com/aws-samples/agent-preparation-toolkit)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/agent-preparation-toolkit/blob/main/README.md)
- README blob SHA: 0495654708687ffbe5b433946fcd1bfdb680417b
- Repository ID: 928138263
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:36:30+00:00

### Short excerpt (up to 100 words)

> 生成 AI における Agent をすぐに体感できるサンプル実装です。 Amazon Bedrock Agents を使ってすぐに Agent を動かすことができるほか、使用している Knowledge Bases のデータや Lambda 関数を差し替えたり付け加えたりすることで自社用の Agent に改造できます。 pythonCoder: { enabled: true, }, hrAgent: { enabled: false, }, productSupportAgent: { enabled: false, }, contractSearcher: { enabled: false, }, bedrockLogWatcher: { enabled: false, config: { bedrockLogsBucket: '', bedrockLogsPrefix: '', }, }, git clone https://github.com/aws-samples/agent-preparation-toolkit cd agent-preparation-toolkit npm install && cd custom-resources && npm ci && cd .. cd ./action-groups/python-coder/lambda && pip install -r requirements.txt -t lib/ && cd ../../../ cd ./action-groups/bedrock-logs-watcher/lambda && pip install -r requirements.txt -t lib/ && cd ../../../ cdk bootstrap npm run cdk:deploy python 1_sync.py -s {YOUR_STACK_NAME} -r

### README headings

- Agent Preparation Toolkit (APT)
- これは？
- 使い方
- リポジトリの Clone
- カレントディレクトリをリポジトリに移す
- Agent で利用する Lambda のパッケージダウンロード
- CDK Bootstrap
- Agent のデプロイ
- (待つ)
- CDK の出力にあるStackName = の後ろの値をコピーする
- 例: Dev-AgentPreparationToolkitStack.StackName = dev-AgentPreparationToolkitStack
- DataSource の同期
- {YOUR_STACK_NAME} には dev-AgentPreparationToolkitStack などを入力
- Agent 呼び出しサンプル
- 内包する Agents
- Python Coder
- Human Resource Agent
- Product Support Agent
- Contract Searcher
- Bedrock Logs Watcher
- Generative AI Use Cases (通称: GenU) 連携
- Bedrock Engineer 連携
- 削除

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 72,241 |
| Python | 46,013 |
| JavaScript | 5,145 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @types/jest, @types/node, aws-cdk, aws-cdk-lib, cdk-nag, constructs, eslint, jest, ts-jest, ts-node, typescript, typescript-eslint, zod
- custom-resources/package.json (capture: captured) — dependency clues: @aws-sdk/credential-provider-node, @opensearch-project/opensearch
- action-groups/bedrock-logs-watcher/lambda/requirements.txt (capture: captured) — dependency clues: sqlparse
- action-groups/python-coder/lambda/requirements.txt (capture: captured) — dependency clues: pytest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 26
- Forks at capture: 1
- Last updated: 2026-08-16T04:04:07Z
- Last pushed: 2025-11-18T08:37:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/agent-preparation-toolkit)
- [README](https://github.com/aws-samples/agent-preparation-toolkit/blob/main/README.md)
- [Issues](https://github.com/aws-samples/agent-preparation-toolkit/issues)
- [Releases](https://github.com/aws-samples/agent-preparation-toolkit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
