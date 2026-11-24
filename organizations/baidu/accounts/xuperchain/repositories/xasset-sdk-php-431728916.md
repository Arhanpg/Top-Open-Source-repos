# xuperchain/xasset-sdk-php

- Company: Baidu
- GitHub account: [https://github.com/xuperchain](https://github.com/xuperchain)
- Mapping status: official-project-linked
- Repository: [xuperchain/xasset-sdk-php](https://github.com/xuperchain/xasset-sdk-php)
- Default branch: main
- README: [Open upstream README](https://github.com/xuperchain/xasset-sdk-php/blob/main/README.md)
- README blob SHA: f2542ab88b8e2fea5c98a6bed81037e7ad72dae3
- Repository ID: 431728916
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

XuperAsset platform php sdk.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:44:07+00:00

### Short excerpt (up to 100 words)

> 本项目提供Xasset PHP语言版的开发者工具包（SDK），开发者可以基于该SDK使用PHP语言接入到Xasset平台。 - 1.从平台申请获得到API准入AK/SK。注意AK/SK是准入凭证，不要泄露，不要下发或配置在客户端使用。 - 2.在开发中引用包含（require_once）对应文件，开发业务程序。 - 3.接入联调环境联调测试，测试通过后更换到线上环境，完成接入。 - 4.从平台申请获得加密和生成区块链账户的二进制文件。 PHP SDK可以在PHP5.4及以上环境下运行。 // 需要拷贝整个SDK包，再引用index.php require_once('./index.php'); //请求的HOST $host = 'http://120.48.16.137:8360'; //从平台申请获得到API准入AK/SK $appId = 0; $ak = 'xxx'; $sk = 'xxx'; //区块链账户公私钥对 $account = array( 'address' => 'xxx', 'public_key' => 'xxx', 'private_key' => 'xxx', ); 可以由auth/Account.php中的createAccount函数生成区块链账户 方式一： 直接从百度云BOS下载bin文件： Linux: https://xasset-open.cdn.bcebos.com/resources/xasset-cli/linux/xasset-cli Windows: https://xasset-open.cdn.bcebos.com/resources/xasset-cli/windows/xasset-cli.exe Mac: https://xasset-open.cdn.bcebos.com/resources/xasset-cli/mac/xasset-cli 方式二： 通过go sdk源码编译生成bin文件 1. 下载xasset-sdk-go git clone git@github.com:xuperchain/xasset-sdk-go.git 2. 编译 cd xasset-sdk-go cd tools/xasset-cli go build -o xasset-cli main.go 通过方式一或方式二获取xchain-cli文件, 把xasset-cli文件拷贝到xasset-sdk-php项目中, 例如tools/xasset-cli/目录下。确保xaset-cli是可执行文件。 // 引用文件 require_once('index.php'); //配置 //binary file path //linux mac $binPath = XASSET_PATH . 'tools/xasset-cli/xasset-cli'; //windows //$binPath = XASSET_PATH . 'tools/xasset-cli/xasset-cli.exe'; $crypto = new EcdsaCrypto($binPath); $config =

### README headings

- XASSET PHP SDK
- 概述
- 使用说明
- 运行环境
- 引用SDK包
- 配置说明
- 获取加密binary程序
- 使用示例

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| PHP | 61,427 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9
- Forks at capture: 5
- Last updated: 2026-01-05T05:10:06Z
- Last pushed: 2022-07-22T11:19:40Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/xuperchain/xasset-sdk-php)
- [README](https://github.com/xuperchain/xasset-sdk-php/blob/main/README.md)
- [Issues](https://github.com/xuperchain/xasset-sdk-php/issues)
- [Releases](https://github.com/xuperchain/xasset-sdk-php/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
