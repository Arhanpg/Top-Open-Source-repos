# aws-samples/amazon-s3-resumable-upload

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-s3-resumable-upload](https://github.com/aws-samples/amazon-s3-resumable-upload)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-s3-resumable-upload/blob/main/README.md)
- README blob SHA: ee4d79537d5f0cc75876bd9d5827a5b35c9baa5f
- README bytes captured: 15932
- README truncated at capture limit: False
- Repository ID: 238313308
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

S3 Resumable Migration Version 2 ( S3 断点续传迁移 Version 2)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T02:59:41+00:00

### Short excerpt (up to 300 words)

> English README: README.en.md 多线程断点续传，适合批量的大文件S3上传/下载本地/跨对象存储迁移，支持Amazon S3, Ali OSS, Tencent COS, Google GCS, HuaweiCloud 等兼容S3 API的对象存储 本 Version 2 在同一个应用通过配置即可用做各种场景：单机的上传，单机的下载，部署为集群版的扫描源文件，或作为集群版的分布式传输工作节点；用Golang做了重构，提高性能；支持了一系列扩展功能：排除列表、源no-sign-request、源request-payer、目的storage-class、目的ACL、传输 Metadata 等。

### README headings

- Amazon S3 Resumable Transfer V2  (Amazon S3 断点续传传输 V2)
- 功能
- 使用说明
- 安装Go运行环境
- 下载和编译本项目的Go代码
- 使用
- 以上是使用默认AWS profile in ~/.aws/credentials，如果是EC2且没有配置 profile 而是使用IAM Role，需指定一下 Region
- 如果要指定S3的profile则如下：
- 以上是使用默认AWS profile in ~/.aws/credentials，如果是EC2且没有配置 profile 而是使用IAM Role，需指定一下 Region
- 如果要指定S3的profile则如下：
- 如果from-profile不填则获取默认的profile或使用EC2 IAM Role，需指定一下region
- 以上endpoint也可以用简称替换，即：--from-endpoint=google_gcs，还可以是其他简称：ali_oss, tencent_cos, azure_blob(TODO: azure)
- 集群模式
- 集群模式的 List 模块使用
- 集群模式的传输节点使用
- 下载从 Presign URL 或 URL 列表
- 其他使用帮助
- 其他说明
- S3 触发 SQS 的 Policy示例
- 配置文件
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Amazon S3 Resumable Transfer V2  (Amazon S3 断点续传传输 V2)

> English README: README.en.md 多线程断点续传，适合批量的大文件S3上传/下载本地/跨对象存储迁移，支持Amazon S3, Ali OSS, Tencent COS, Google GCS, HuaweiCloud 等兼容S3 API的对象存储 本 Version 2 在同一个应用通过配置即可用做各种场景：单机的上传，单机的下载，部署为集群版的扫描源文件，或作为集群版的分布式传输工作节点；用Golang做了重构，提高性能；支持了一系列扩展功能：排除列表、源no-sign-request、源request-payer、目的storage-class、目的ACL、传输 Metadata 等。

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 82,294 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go, github.com/fsnotify/fsnotify, github.com/google/uuid, github.com/hashicorp/hcl, github.com/inconshreveable/mousetrap, github.com/jmespath/go-jmespath, github.com/magiconair/properties, github.com/mattn/go-sqlite3, github.com/mitchellh/mapstructure, github.com/pelletier/go-toml/v2, github.com/sagikazarmark/locafero, github.com/sagikazarmark/slog-shim, github.com/sourcegraph/conc, github.com/spf13/afero, github.com/spf13/cast, github.com/spf13/cobra, github.com/spf13/pflag, github.com/spf13/viper, github.com/subosito/gotenv, go.uber.org/atomic

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 180
- Forks at capture: 93
- Last updated: 2026-11-19T08:10:08Z
- Last pushed: 2024-12-10T14:17:54Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-s3-resumable-upload)
- [README](https://github.com/aws-samples/amazon-s3-resumable-upload/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-s3-resumable-upload/issues)
- [Releases](https://github.com/aws-samples/amazon-s3-resumable-upload/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
