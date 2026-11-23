# xuperchain/contract-sdk-py

- Company: Baidu
- GitHub account: [https://github.com/xuperchain](https://github.com/xuperchain)
- Mapping status: official-project-linked
- Repository: [xuperchain/contract-sdk-py](https://github.com/xuperchain/contract-sdk-py)
- Default branch: main
- README: [Open upstream README](https://github.com/xuperchain/contract-sdk-py/blob/main/README.md)
- README blob SHA: 93039f423c907d9d610fb4fd762b42b506d6a3cd
- Repository ID: 353897382
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Python SDK for XuperChain smart contract

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:51:32+00:00

### Short excerpt (up to 100 words)

> contract-sdk-py 是 XuperChain 的官方python 合约SDK，使用前请先在本地运行最新的XuperChain，并确保开启 native 合约支持 要求 python 版本为 python3.6+ 1. 安装 python 合约 SDK git clone https://github.com/xuperchain/contract-sdk-py.git cd contract-sdk-py pip install -r requirements.txt python3 setup.py install 2. 部署和调用第一个 python 合约 ./xchain-cli native deploy --account XC1111111111111111@xuper --fee 15587517 --runtime py -a '{"creator":"xchain"}' --cname counter <PATH_TO_CONTRACT_SDK_PY>/example/counter/counter.py ./xchain-cli native invoke --method Increase -a '{"key":"xchain"}' counter --fee 10 ./xchain-cli native invoke --method Get -a '{"key":"xchain"}' counter --fee 10

### README headings

- No headings captured

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 17,206 |
| JavaScript | 1,498 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)
- requirements.txt (capture: captured) — dependency clues: grpcio, grpcio-reflection, protobuf
- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 1
- Last updated: 2021-04-19T06:32:51Z
- Last pushed: 2021-04-19T06:32:49Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/xuperchain/contract-sdk-py)
- [README](https://github.com/xuperchain/contract-sdk-py/blob/main/README.md)
- [Issues](https://github.com/xuperchain/contract-sdk-py/issues)
- [Releases](https://github.com/xuperchain/contract-sdk-py/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
