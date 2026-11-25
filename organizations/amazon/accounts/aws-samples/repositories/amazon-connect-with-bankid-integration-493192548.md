# aws-samples/amazon-connect-with-bankid-integration

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-connect-with-bankid-integration](https://github.com/aws-samples/amazon-connect-with-bankid-integration)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-connect-with-bankid-integration/blob/main/README.md)
- README blob SHA: 48e59877aec41f6728d0dd96e4eb586430ee1a08
- README bytes captured: 6544
- README truncated at capture limit: False
- Repository ID: 493192548
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This code will set up a contact flow/IVR for real time authentication with Mobile BankID and can be deployed in minutes.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:39:34+00:00

### Short excerpt (up to 300 words)

> An Amazon account An

### README headings

- Amazon Connect with BankID authentication - Demo
- Services used
- Requirements for deployment
- Setup for Test BankID
- Deployment
- Optional
- !!!! FOR BANK ID TESTING ENV ONLY !!!
- This command only needs run once. Once the pem files have been generated there's no need to run this again.
- This step is not required if using new or private certificates with BankID
- You will be then requested to input the BankID Passphrase from
- https://www.bankid.com/assets/bankid/rp/bankid-relying-party-guidelines-v3.6.pdf
- It is not recommended to use a password as an argument in a bash script. However since the password is already on the public internet the scipt has been provided for convenience. Please use with caution and delete when progressing to personal or production certs.
- Choose options
- The name of the CloudFormation stack
- The region you want to deploy in
- The Arn of your existing Amazon Connect Instance
- Shows you resources changes to be deployed and requires a 'Y' to initiate deploy
- SAM needs permission to be able to create roles to connect to the resources in your template
- Save your choice for later deployments
- Call and test
- Cleanup
- Delete the stack via the SAM CLI
- Recommendation for Production credentials
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Technology and requirements: Requirements for deployment

> An Amazon account An

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 6,301 |
| Shell | 1,582 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- code/bankid-auth/requirements.txt (capture: captured) — dependency clues: certifi, charset-normalizer, idna, pybankid, requests, six, urllib3
- code/deploy-contact-flow/requirements.txt (capture: captured) — dependency clues: Jinja2, MarkupSafe, cfnresponse

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 7
- Forks at capture: 1
- Last updated: 2025-03-09T10:53:54Z
- Last pushed: 2023-07-25T20:31:34Z
- Topics: amazon-connect, authentication, call-center, call-flow, python

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-connect-with-bankid-integration)
- [README](https://github.com/aws-samples/amazon-connect-with-bankid-integration/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-connect-with-bankid-integration/issues)
- [Releases](https://github.com/aws-samples/amazon-connect-with-bankid-integration/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
