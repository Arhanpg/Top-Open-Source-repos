# aws-controllers-k8s/controller-bootstrap

- Company: Amazon
- Account: aws-controllers-k8s
- Repository: https://github.com/aws-controllers-k8s/controller-bootstrap
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:14:36+00:00

## Project purpose

The ACK controller-bootstrap tool automates the repository bootstrap process for new ACK service controllers in the aws-controller-k8s Github organization. For existing ACK service controllers, this tool will update the service controllers with the latest templates of the project description files, which include: CODE_OF_CONDUCT.md, CONTRIBUTING.md, GOVERNANCE.md, LICENSE, NOTICE, SECURITY.md files.

## Why this project is used

A template for creating new controller repositories on the github.com/aws-controllers-k8s organization

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Smarty, Go Template, Makefile, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: dario.cat/mergo, github.com/Microsoft/go-winio, github.com/ProtonMail/go-crypto, github.com/cloudflare/circl, github.com/cyphar/filepath-securejoin, github.com/davecgh/go-spew, github.com/emirpasic/gods, github.com/gertd/go-pluralize, github.com/go-git/gcfg, github.com/go-git/go-billy/v5, github.com/go-git/go-git/v5, github.com/golang/groupcache, github.com/inconshreveable/mousetrap, github.com/jbenet/go-context, github.com/kevinburke/ssh_config, github.com/klauspost/cpuid/v2, github.com/pjbgf/sha1cd, github.com/pmezard/go-difflib, github.com/sergi/go-diff, github.com/skeema/knownhosts, github.com/spf13/cobra, github.com/spf13/pflag, github.com/stretchr/testify, github.com/xanzy/ssh-agent, golang.org/x/crypto, golang.org/x/net, golang.org/x/sys, gopkg.in/warnings.v0, gopkg.in/yaml.v3
- Build/package tools: Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/controller-bootstrap/main.go, cmd/controller-bootstrap/command/apiutil.go, cmd/controller-bootstrap/command/apiutil_test.go, cmd/controller-bootstrap/command/common.go

## Setup and usage

- Getting Started: First, clone the aws-controllers-k8s/controller-bootstrap repository and run the following script in the controller-bootstrap.
- Getting Started: export SERVICE=${AWS_SERVICE_NAME}
- Getting Started: For a new ACK service controller, the make command bootstraps an ACK service controller repository. For an existing ACK service controller, it updates the service controller repository with the latest templates of the project description files.
- Getting Started: To generate the common directories and files for a new ACK service controller using CLI command, the user can run the generate command from the controller-bootstrap.
- Getting Started: controller-bootstrap generate --aws-service-alias ${AWS_SERVICE} --ack-runtime-version ${ACK_RUNTIME_VERSION}
- Getting Started: --aws-sdk-go-version ${AWS_SDK_GO_VERSION} --dry-run=${DRY_RUN} --output-path ${CONTROLLER_DIR}
- Getting Started: --model-name ${SERVICE_MODEL_NAME} --refresh-cache=${REFRESH_CACHE} --test-infra-commit-sha ${TEST_INFRA_COMMIT_SHA}
- Getting Started: To update an existing ACK service controller with the latest templates of the project description files using CLI command, the user can run the update command from the controller-bootstrap.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-controllers-k8s/controller-bootstrap/blob/main/README.md
- README SHA: 3026a2919fe52b156afcce76d7309283431831a5
- Manifests: go.mod, Makefile
- Sampled source files: cmd/controller-bootstrap/main.go, cmd/controller-bootstrap/command/apiutil.go, cmd/controller-bootstrap/command/apiutil_test.go, cmd/controller-bootstrap/command/common.go
- Git tree state: captured
- Evidence fingerprint: 2c637bb0acbe2dc5bdc5054df5d4ffeecd04f4572feea4b9a8644a4b77df6ca1

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
