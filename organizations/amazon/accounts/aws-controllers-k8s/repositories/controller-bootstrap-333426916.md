# aws-controllers-k8s/controller-bootstrap

- Company: Amazon
- GitHub account: [https://github.com/aws-controllers-k8s](https://github.com/aws-controllers-k8s)
- Mapping status: official-directory-listed
- Repository: [aws-controllers-k8s/controller-bootstrap](https://github.com/aws-controllers-k8s/controller-bootstrap)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-controllers-k8s/controller-bootstrap/blob/main/README.md)
- README blob SHA: 3026a2919fe52b156afcce76d7309283431831a5
- Repository ID: 333426916
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A template for creating new controller repositories on the github.com/aws-controllers-k8s organization 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:29:32+00:00

### Short excerpt (up to 100 words)

> The ACK controller-bootstrap tool automates the repository bootstrap process for new ACK service controllers in the `aws-controller-k8s` Github organization. For existing ACK service controllers, this tool will update the service controllers with the latest templates of the project description files, which include: `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `LICENSE`, `NOTICE`, `SECURITY.md` files. First, clone the `aws-controllers-k8s/controller-bootstrap` repository and run the following script in the controller-bootstrap. export SERVICE=${AWS_SERVICE_NAME} make For a new ACK service controller, the `make` command bootstraps an ACK service controller repository. For an existing ACK service controller, it updates the service controller repository with the latest templates of the project description

### README headings

- Controller-Bootstrap for AWS Controllers for Kubernetes (ACK)
- Getting Started
- Usage
- Community, discussion, contribution, and support
- Code of conduct

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 34,081 |
| Smarty | 8,380 |
| Go Template | 6,333 |
| Makefile | 2,934 |
| Shell | 2,671 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: dario.cat/mergo, github.com/Microsoft/go-winio, github.com/ProtonMail/go-crypto, github.com/cloudflare/circl, github.com/cyphar/filepath-securejoin, github.com/davecgh/go-spew, github.com/emirpasic/gods, github.com/gertd/go-pluralize, github.com/go-git/gcfg, github.com/go-git/go-billy/v5, github.com/go-git/go-git/v5, github.com/golang/groupcache, github.com/inconshreveable/mousetrap, github.com/jbenet/go-context, github.com/kevinburke/ssh_config, github.com/klauspost/cpuid/v2, github.com/pjbgf/sha1cd, github.com/pmezard/go-difflib, github.com/sergi/go-diff, github.com/skeema/knownhosts
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 23
- Last updated: 2026-08-27T19:36:43Z
- Last pushed: 2026-08-27T19:36:18Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-controllers-k8s/controller-bootstrap)
- [README](https://github.com/aws-controllers-k8s/controller-bootstrap/blob/main/README.md)
- [Issues](https://github.com/aws-controllers-k8s/controller-bootstrap/issues)
- [Releases](https://github.com/aws-controllers-k8s/controller-bootstrap/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
