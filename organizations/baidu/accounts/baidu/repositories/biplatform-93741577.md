# baidu/BIPlatform

- Company: Baidu
- GitHub account: [https://github.com/baidu](https://github.com/baidu)
- Mapping status: verified
- Repository: [baidu/BIPlatform](https://github.com/baidu/BIPlatform)
- Default branch: master
- README: [Open upstream README](https://github.com/baidu/BIPlatform/blob/master/README.md)
- README blob SHA: dda72c7356422de0672a456dcdce3e03e87216aa
- Repository ID: 93741577
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:36:12+00:00

### Short excerpt (up to 100 words)

> BIPlatform 声明：因公司内部代码规范管理原因，平台代码版本维护由git迁移到公司svn管理，平台更新代码按天同步到github，感谢关注！ 百度开源，业内领先的Holap敏捷BI分析平台，提供高性能、准实时、可扩展的、一站式的BI建模、分析平台。 fileserver －－ 静态文件服务器 存储平台生成的静态文件 model －－ 模型组建层 定义分析、问答模型 designer －－ 设计器 tesseract －－ 执行引擎 clone项目到本地指定目录 分别在fileserver、tesseract、designer目录下执行 mvn install构建项目 找到fileserver构建后的jar文件，执行java －jar 指定端口和有效文件路径，启动文件服务器， 如： java -jar fileserver-0.0.1-SNAPSHOT.jar 9090 /tmp/ > log/fileserver.log & 找到tesseract构建后的jar文件，执行java －jar 启动执行引擎， 如： java -jar tesseract-0.0.1-SNAPSHOT.jar > log/ter.log & 找到designer构建后的jar文件，执行java －jar 启动建模工具, 如： java -jar designer-0.0.1-SNAPSHOT.jar --server.port=8999 > log/designer.log &

### README headings

- 如何快速构建BI－Platform 构建前提：需在指定环境中安装maven 3 以上、java8
- 项目模块功能描述：
- 构建流程：
- 开发文档： 详见：http://my.oschina.net/biplatform/blog
- 用户手册： 构建中（2014-11-30），和Milestonev1.1.0同步发布

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 15,475,152 |
| Java | 4,554,030 |
| CSS | 1,480,091 |
| HTML | 253,962 |
| Shell | 3,347 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: activemq-broker, activemq-client, activemq-jms-pool, activemq-pool, biplatform, c3p0, cache, common-api, commons-collections, commons-compress, commons-lang, commons-logging, fileserver, gson, guava, hazelcast, hazelcast-client, hazelcast-spring, jackson-annotations, jms
- cache/pom.xml (capture: captured) — dependency clues: biplatform, cache, commons-collections, commons-io, commons-lang, gson, hazelcast, hazelcast-client, hazelcast-spring, jedis, junit, powermock-api-mockito, powermock-module-junit4, redisson, spring-boot-starter-redis, spring-data-redis
- common-api/pom.xml (capture: captured) — dependency clues: activemq-broker, activemq-client, activemq-jms-pool, activemq-pool, biplatform, cache, common-api, fileserver, guava, junit, mockito-all, model, powermock-api-mockito, powermock-module-junit4, spring-jms, spring-test
- designer/pom.xml (capture: captured) — dependency clues: biplatform, cache, common-api, commons-collections, commons-lang, designer, gson, guava, h2, jms, json, junit, mail, mockito-all, model, mysql-connector-java, powermock-api-mockito, powermock-module-junit4, schedule, spring-boot-maven-plugin
- fileserver/pom.xml (capture: captured) — dependency clues: biplatform, commons-lang, fileserver, guava, httpclient, junit, maven-assembly-plugin, mockito-all, netty-all, powermock-api-mockito, powermock-module-junit4, slf4j-api
- model/pom.xml (capture: captured) — dependency clues: biplatform, commons-collections, commons-lang, commons-logging, gson, guava, httpclient, jackson-annotations, jackson-core, junit, mockito-all, model, powermock-api-mockito, powermock-module-junit4, slf4j-log4j12, spring-core

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 218
- Forks at capture: 124
- Last updated: 2026-08-23T13:06:43Z
- Last pushed: 2023-04-21T00:37:33Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/baidu/BIPlatform)
- [README](https://github.com/baidu/BIPlatform/blob/master/README.md)
- [Issues](https://github.com/baidu/BIPlatform/issues)
- [Releases](https://github.com/baidu/BIPlatform/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
