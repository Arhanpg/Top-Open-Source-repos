# aws/amazon-neptune-gremlin-dotnet-sigv4

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-neptune-gremlin-dotnet-sigv4](https://github.com/aws/amazon-neptune-gremlin-dotnet-sigv4)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-neptune-gremlin-dotnet-sigv4/blob/main/README.md)
- README blob SHA: 743b9949d6350b701aeba866482730893620ada2
- Repository ID: 428407732
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A custom library for Amazon Neptune that enables AWS Signature Version 4 signing by extending the Apache TinkerPop Gremlin .NET client.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:35:04+00:00

### Short excerpt (up to 100 words)

> This project provides a custom library that extends the Apache TinkerPop Gremlin.NET client to enable AWS IAM Signature Version 4 signing for establishing authenticated connections to Amazon Neptune. For example usage refer to: NeptuneGremlinNETSigV4Example.cs. This example shows how to leverage this library for establishing an authenticated connection to Neptune. For general information on how to connect to Amazon Neptune using Gremlin and best practices, refer to the documentation. A snippet of the code from NeptuneGremlinNETSigV4Example.cs: var neptune_host = "neptune-endpoint"; // ex: mycluster.cluster.us-east-1.neptune.amazonaws.com var neptune_port = 8182; var gremlinServer = new GremlinServer(neptune_host, neptune_port); var gremlinClient = new GremlinClient(gremlinServer, webSocketConfiguration: new SigV4RequestSigner().signRequest(neptune_host,

### README headings

- Amazon Neptune Gremlin .NET SigV4
- Usage
- Using within Amazon EC2
- Using within AWS Lambda
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C# | 9,261 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- example/ExampleProject.csproj (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 6
- Last updated: 2026-08-23T20:59:03Z
- Last pushed: 2025-03-25T11:07:14Z
- Topics: amazon-neptune, aws-neptune

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-neptune-gremlin-dotnet-sigv4)
- [README](https://github.com/aws/amazon-neptune-gremlin-dotnet-sigv4/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-neptune-gremlin-dotnet-sigv4/issues)
- [Releases](https://github.com/aws/amazon-neptune-gremlin-dotnet-sigv4/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
