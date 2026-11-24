# xuperchain/regression-pytest

- Company: Baidu
- GitHub account: [https://github.com/xuperchain](https://github.com/xuperchain)
- Mapping status: official-project-linked
- Repository: [xuperchain/regression-pytest](https://github.com/xuperchain/regression-pytest)
- Default branch: master
- README: [Open upstream README](https://github.com/xuperchain/regression-pytest/blob/master/README.md)
- README blob SHA: 4132d84869de49feec70c240ed295dd09e7cd81f
- Repository ID: 601979083
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:43:58+00:00

### Short excerpt (up to 100 words)

> 使用pytest框架，搭建xchain的自动化测试用例，覆盖账户、转账、权限、合约、平行链、共识、共识升级、事件订阅等功能点。 - 操作系统：支持Linux、macos - 开发语言：Python 3.x - 依赖包：pytest pyyaml numpy pytz - 版本控制工具：Git - 其他：go1.13+ 参考文档 https://github.com/xuperchain/xuperchain#run-multi-nodes-blockchain 部署的xchain网络默认使用端口37101、37102、37103，所以自动化用例默认使用的端口也是这三个。 git clone https://github.com/xuperchain/xuperchain.git cd xuperchain && make && make testnet && cd testnet/ && sh control_all.sh start pwd cd ../.. && cp xuperchain/output/bin/xchain-cli client/bin/ sleep 15 1. `hosts`和`default_host`是xchain网络各节点的rpcPort端口，按测试的xchain网络修改 2. `account`为xchain网络3节点的公私玥，`data/keys`为node1的公私玥，按测试的xchain网络修改 为提升CI执行速度，用例拆分为3个批次，在3台测试环境并发执行。 在本地执行时，可以顺序串行执行3个批次。 sh run_case.sh batch1 # 运行时间约11min sh run_case.sh batch2 # 运行时间约15min sh run_case.sh batch3 # 运行时间约11min pytest [-s] cases/***/test_***.py [cases/***/test_***.py] [--type $consensus_type] [-m p0] * --type 在运行共识用例时需配置，支持`tdpos`, `xpos`, `poa`, `xpoa`, `single`. 如不填默认tdpos * -m 执行特定tag的用例 注意：环境部署成功后，先执行环境检查用例，后调试用例 pytest -s case/test_env.py 文件命名规范 test_[module]\_[id]\_[用例类别].py，例如test_acc_0_normal.py

### README headings

- Test Xchain
- 环境配置
- 部署网络，执行测试用例
- 1.部署3节点xchain网络
- 2.配置说明
- 3.运行用例
- 4.调试用例
- 5.新增用例

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 440,486 |
| Shell | 4,720 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: PyYAML, numpy, pre-commit, pytest, pytz

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 0
- Forks at capture: 1
- Last updated: 2023-02-16T02:58:08Z
- Last pushed: 2023-02-22T03:12:42Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/xuperchain/regression-pytest)
- [README](https://github.com/xuperchain/regression-pytest/blob/master/README.md)
- [Issues](https://github.com/xuperchain/regression-pytest/issues)
- [Releases](https://github.com/xuperchain/regression-pytest/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
