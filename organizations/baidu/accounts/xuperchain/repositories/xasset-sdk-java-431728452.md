# xuperchain/xasset-sdk-java

- Company: Baidu
- GitHub account: [https://github.com/xuperchain](https://github.com/xuperchain)
- Mapping status: official-project-linked
- Repository: [xuperchain/xasset-sdk-java](https://github.com/xuperchain/xasset-sdk-java)
- Default branch: main
- README: [Open upstream README](https://github.com/xuperchain/xasset-sdk-java/blob/main/README.md)
- README blob SHA: f4ee9344c9257408766f7e2ab46f908863f622b2
- Repository ID: 431728452
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

XuperAsset platform java sdk.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:44:06+00:00

### Short excerpt (up to 100 words)

> 本文档主要介绍Xasset平台JAVA语言版的开发者工具包（SDK），开发者可基于该SDK使用Java语言接入到Xasset平台的各项服务。SDK封装了便捷的调用接口，保持了多种编程语言版的使用方式、调用接口相似，提供了统一的错误码和返回格式，方便开发者调试。 - 1.从平台申请获得到API准入**AK/SK**。注意AK/SK是准入凭证，不要泄露，不要下发或配置在客户端使用。 - 2.使用Maven安装，在Maven的pom.xml文件中添加xasset-sdk-java的依赖。 - 3.接入联调环境联调测试，测试通过后更换到线上环境，完成接入。 java version "1.8.0_45" Java(TM) SE Runtime Environment (build 1.8.0_45-b14) 1. 在pom.xml添加如下依赖： class XassetCliConfig { public String EndPoint; public String UserAgent; public Credentials Credentials; public SignOptions SignOption; public Duration ConnectTimeoutMs; } // 初始化配置 XassetCliConfig cfg = new XassetCliConfig(); // 配置AK/SK 和 AppId cfg.SetCredentials(appId, ak, sk); // 确认Endpoint, 接入联调环境 cfg.SetEndPoint("http://120.48.16.137:8360"); import com.baidu.xasset.auth.XchainAccount; import com.baidu.xasset.client.base.BaseDef.*; import com.baidu.xasset.client.xasset.XassetDef.*; import com.baidu.xasset.common.config.Config.*; import com.baidu.xuper.api.Account; import java.util.logging.Logger; class Test { public static void main(String[] args) { // 配置AK/SK 和 AppId long appId = 0; String ak = ""; String sk = ""; XassetCliConfig cfg = new XassetCliConfig(); cfg.setCredentials(appId, ak, sk);

### README headings

- XASSET JAVA SDK
- 概述
- 使用说明
- 运行环境
- Maven安装
- 版本记录
- 配置说明
- 使用示例

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 161,184 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: bce-java-sdk, fastjson2, jcl-over-slf4j, junit, logback-classic, logback-core, maven-clean-plugin, maven-compiler-plugin, maven-deploy-plugin, maven-gpg-plugin, maven-install-plugin, maven-jar-plugin, maven-javadoc-plugin, maven-project-info-reports-plugin, maven-resources-plugin, maven-site-plugin, maven-source-plugin, maven-surefire-plugin, xasset-sdk-java, xuper-java-sdk

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 5
- Forks at capture: 2
- Last updated: 2026-01-05T05:10:08Z
- Last pushed: 2022-12-19T09:05:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/xuperchain/xasset-sdk-java)
- [README](https://github.com/xuperchain/xasset-sdk-java/blob/main/README.md)
- [Issues](https://github.com/xuperchain/xasset-sdk-java/issues)
- [Releases](https://github.com/xuperchain/xasset-sdk-java/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
