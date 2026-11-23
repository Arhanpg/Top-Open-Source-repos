# aws-samples/access-analyzer-automated-policy-analysis-blog

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/access-analyzer-automated-policy-analysis-blog](https://github.com/aws-samples/access-analyzer-automated-policy-analysis-blog)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/access-analyzer-automated-policy-analysis-blog/blob/main/README.md)
- README blob SHA: e9bd94ebdceeebd79d91ca63c769a15462b225f3
- Repository ID: 715298381
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:11:21+00:00

### Short excerpt (up to 100 words)

> As covered in the following blog post: https://aws.amazon.com/blogs/security/introducing-iam-access-analyzer-custom-policy-checks/ In this example, you will automate the validation and analysis of the IAM identity and resources policies that are defined in an AWS CloudFromation template. The workflow will trigger each time a pull request is created against the main branch of an AWS CodeCommit repository called my-iam-policy. The workflow includes 3 checks. The first check will use IAM Access Analyzer's check no new access API to determine if the updated policy is more permissive than a reference IAM policy. The second check will use the check access not granted API to automatically

### README headings

- Automating IAM Access Analyzer custom policy checks
- Step 1: Deploy the infrastructure and set up the pipeline
- Step 2: Create a new CloudFormation template that defines an IAM policy
- Step 3: Run analysis on the IAM policy
- Step 4: Create a pull request to merge a new update to the CloudFormation template
- Why did the validations fail?
- Cleanup

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 20,739 |
| Shell | 618 |
| Batchfile | 437 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: PyYAML, aws-cdk-lib, cdk-nag, constructs

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 7
- Forks at capture: 2
- Last updated: 2026-02-04T21:42:45Z
- Last pushed: 2024-07-30T11:32:48Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/access-analyzer-automated-policy-analysis-blog)
- [README](https://github.com/aws-samples/access-analyzer-automated-policy-analysis-blog/blob/main/README.md)
- [Issues](https://github.com/aws-samples/access-analyzer-automated-policy-analysis-blog/issues)
- [Releases](https://github.com/aws-samples/access-analyzer-automated-policy-analysis-blog/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
