# aws-amplify/aws-sdk-ios

- Company: Amazon
- Account: aws-amplify
- Repository: https://github.com/aws-amplify/aws-sdk-ios
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:08:24+00:00

## Project purpose

We recommend that you start using AWS Amplify for Swift, our modern feature-rich library designed specifically for building cloud-connected apps powered by AWS. You can refer to the AWS SDK for iOS migration guide to help you transition to AWS Amplify for Swift. This version is scheduled to reach End of Support on **August 1, 2026**. After this date, no further updates of any kind will be provided. See maintenance policy for more information about the Amplify Client Library lifecycle.

## Why this project is used

AWS SDK for iOS. For more information, see our web site:

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Objective-C, Swift, C, Ruby, Python, Shell, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Bundler manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: AWSCoreUnitTests/SigV4Tests/generate_swift_test_cases/lib/app_shell.rb, AWSCoreUnitTests/SigV4Tests/generate_swift_test_cases/lib/presign_url_options.rb, AWSCoreUnitTests/SigV4Tests/generate_swift_test_cases/lib/signer_forked.rb, AWSCoreUnitTests/SigV4Tests/generate_swift_test_cases/lib/sigv4_test_case.rb

## Setup and usage

- Getting Started with Swift: 1. Import the AWSCore header in the application delegate.
- Getting Started with Swift: 2. Create a default service configuration by adding the following code snippet in the application:didFinishLaunchingWithOptions: application delegate method.
- Getting Started with Swift: let credentialsProvider = AWSCognitoCredentialsProvider(
- Getting Started with Swift: regionType: CognitoRegionType,
- Getting Started with Swift: identityPoolId: CognitoIdentityPoolId)
- Getting Started with Swift: let configuration = AWSServiceConfiguration(
- Getting Started with Swift: region: DefaultServiceRegionType,
- Getting Started with Swift: credentialsProvider: credentialsProvider)

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-amplify/aws-sdk-ios/blob/main/README.md
- README SHA: 15330e8b18a667fc65a4a5930ab21823a1e8a1b1
- Manifests: Gemfile
- Sampled source files: AWSCoreUnitTests/SigV4Tests/generate_swift_test_cases/lib/app_shell.rb, AWSCoreUnitTests/SigV4Tests/generate_swift_test_cases/lib/presign_url_options.rb, AWSCoreUnitTests/SigV4Tests/generate_swift_test_cases/lib/signer_forked.rb, AWSCoreUnitTests/SigV4Tests/generate_swift_test_cases/lib/sigv4_test_case.rb
- Git tree state: captured
- Evidence fingerprint: 016c053f47686633639aa663db759cb1068f0bd8bdea50f95ff16b0d02d07ac8

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
