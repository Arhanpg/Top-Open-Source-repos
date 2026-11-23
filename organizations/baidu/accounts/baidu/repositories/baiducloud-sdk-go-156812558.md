# baidu/baiducloud-sdk-go

- Company: Baidu
- GitHub account: [https://github.com/baidu](https://github.com/baidu)
- Mapping status: verified
- Repository: [baidu/baiducloud-sdk-go](https://github.com/baidu/baiducloud-sdk-go)
- Default branch: master
- README: [Open upstream README](https://github.com/baidu/baiducloud-sdk-go/blob/master/README.md)
- README blob SHA: 5a933c6aa0e41db698ff7d8ec5ac400a9f9dce27
- Repository ID: 156812558
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Go SDK for Baidu Cloud

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:42:41+00:00

### Short excerpt (up to 100 words)

> baiudcloud-sdk-go is the official BaiudCloud SDK for the Go programming language, supporting convenient access to cloud resources, including Baidu Cloud Compute (BCC), Baidu Load Balancer (BLB), Baidu Object Storage (BOS), Cloud Disk Service (CDS), Elastic IP (EIP), Virtual Private Cloud (VPC), etc. Go >= 1.8 is required. go get -u github.com/baidu/baiducloud-sdk-go/... This example shows a complete example to list all eips in some region. package main import ( "fmt" "time" "github.com/baidu/baiducloud-sdk-go/bce" "github.com/baidu/baiducloud-sdk-go/eip" ) func main() { cred, err := bce.NewCredentialsFromFile("example/main/aksk.json") if err != nil { panic(err) } bceConf := &bce.Config{ Credentials: cred, Checksum: true, Timeout: 5 * time.Second, Region: "bj",

### README headings

- BaiduCloud SDK for Go
- Installing
- Usage
- Contributors
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 335,734 |

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
- Stars at capture: 25
- Forks at capture: 9
- Last updated: 2026-06-02T07:18:25Z
- Last pushed: 2019-10-22T08:39:03Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/baidu/baiducloud-sdk-go)
- [README](https://github.com/baidu/baiducloud-sdk-go/blob/master/README.md)
- [Issues](https://github.com/baidu/baiducloud-sdk-go/issues)
- [Releases](https://github.com/baidu/baiducloud-sdk-go/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
