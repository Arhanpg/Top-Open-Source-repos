# awslabs/amazon-ecr-containerd-resolver

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-ecr-containerd-resolver](https://github.com/awslabs/amazon-ecr-containerd-resolver)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/amazon-ecr-containerd-resolver/blob/master/README.md)
- README blob SHA: aadaa06ca159711ba4cbc15267d232d88b3f5bb7
- Repository ID: 139645294
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Amazon ECR containerd resolver is an implementation of a containerd Resolver and Fetcher that can pull images from and push images to Amazon ECR using the Amazon ECR API instead of the Docker Registry API. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:43:07+00:00

### Short excerpt (up to 100 words)

> The Amazon ECR containerd resolver is an implementation of a `Resolver`, `Fetcher`, and `Pusher` that can pull images from Amazon ECR and push images to Amazon ECR using the Amazon ECR API instead of the Docker Registry API. resolver, _ := ecr.NewResolver() img, err := client.Pull( namespaces.NamespaceFromEnv(context.TODO()), "ecr.aws/arn:aws:ecr:us-west-2:123456789012:repository/myrepository:mytag", containerd.WithResolver(resolver), containerd.WithPullUnpack, containerd.WithSchema1Conversion) ctx := namespaces.NamespaceFromEnv(context.TODO()) img, _ := client.ImageService().Get( ctx, "docker.io/library/busybox:latest") resolver, _ := ecr.NewResolver() err = client.Push( ctx, "ecr.aws/arn:aws:ecr:us-west-2:123456789012:repository/myrepository:mytag", img.Target, containerd.WithResolver(resolver)) Two small example programs are provided in the example directory demonstrating how to use the resolver with containerd. containerd specifies images with a `ref`. `ref`s are different from Docker

### README headings

- Amazon ECR containerd resolver
- Usage
- Pull images
- Push images
- `ref`
- Parallel downloads
- Building
- AWS Go SDK v2 Upgrade Note
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 139,119 |
| Makefile | 1,764 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/ecr, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/containerd/cgroups, github.com/containerd/console, github.com/containerd/containerd, github.com/containerd/continuity
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 108
- Forks at capture: 21
- Last updated: 2026-07-17T15:27:39Z
- Last pushed: 2025-11-20T22:11:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-ecr-containerd-resolver)
- [README](https://github.com/awslabs/amazon-ecr-containerd-resolver/blob/master/README.md)
- [Issues](https://github.com/awslabs/amazon-ecr-containerd-resolver/issues)
- [Releases](https://github.com/awslabs/amazon-ecr-containerd-resolver/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
