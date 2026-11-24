# xuperchain/xasset-sdk-go

- Company: Baidu
- GitHub account: [https://github.com/xuperchain](https://github.com/xuperchain)
- Mapping status: official-project-linked
- Repository: [xuperchain/xasset-sdk-go](https://github.com/xuperchain/xasset-sdk-go)
- Default branch: main
- README: [Open upstream README](https://github.com/xuperchain/xasset-sdk-go/blob/main/README.md)
- README blob SHA: a3a62570638a3ca6dae3ebdde9166013de014b68
- Repository ID: 431727189
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

XuperAsset platform golang SDK.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:44:04+00:00

### Short excerpt (up to 100 words)

> 本项目提供Xasset Go语言版的开发者工具包（SDK），开发者可以基于该SDK使用Go语言接入到Xasset平台。 - 1.从平台申请获得到API准入AK/SK。注意AK/SK是准入凭证，不要泄露，不要下发或配置在客户端使用。 - 2.在开发中导入（import）对应包，开发业务程序。建议使用go mod管理包依赖。 - 3.接入联调环境联调测试，测试通过后更换到线上环境，完成接入。 GO SDK可以在go1.3及以上环境下运行。 // 按需导入对应包使用，使用go mod管理（go mod tidy） import ( "github.com/xuperchain/xasset-sdk-go/client/xasset" ) type XassetCliConfig struct { // 请求接入Host Endpoint string // 请求UA UserAgent string // 准入授权信息，注意保密 Credentials *auth.Credentials // 准入签名Header SignOption *auth.SignOptions // Http请求链接超时 ConnectTimeoutMs int // Http请求读写超时 ReadWriteTimeoutMs int } // 使用示例 cfg := config.NewXassetCliConf() cfg.Endpoint = "http://127.0.0.1:8360" cfg.SetCredentials(appId, ak, sk) // 导入包 import ( "github.com/xuperchain/xasset-sdk-go/client/xasset" "github.com/xuperchain/xasset-sdk-go/common/config" ) // 配置SDK cfg := config.NewXassetCliConf() cfg.Endpoint = "http://127.0.0.1:8360" cfg.SetCredentials(appId, ak, sk) // 调用SDK方法，可以参考单元测试 handle, _ := xasset.NewAssetOperCli(cfg, &Logger{}) handle.CreateAsset() //导入包 import ( github.com/xuperchain/xasset-sdk-go/utils ) // 使用sk对str加密/解密 encodeStr, _ := utils.AesEncode(unionId, sk) decodeStr, _

### README headings

- XASSET GO SDK
- 概述
- 使用说明
- 运行环境
- 导入SDK包
- 配置说明
- 使用示例
- sk加解密

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 248,893 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/baidubce/bce-sdk-go, github.com/spf13/cobra, github.com/xuperchain/crypto

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 10
- Forks at capture: 7
- Last updated: 2026-01-05T05:10:09Z
- Last pushed: 2023-11-07T07:29:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/xuperchain/xasset-sdk-go)
- [README](https://github.com/xuperchain/xasset-sdk-go/blob/main/README.md)
- [Issues](https://github.com/xuperchain/xasset-sdk-go/issues)
- [Releases](https://github.com/xuperchain/xasset-sdk-go/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
