# Password Manager Resources

- Company association: Apple
- Upstream GitHub account: [apple](https://github.com/apple)
- Repository: [apple/password-manager-resources](https://github.com/apple/password-manager-resources)
- Default branch: main
- README: [Open upstream README](https://github.com/apple/password-manager-resources/blob/main/README.md)
- Review status: README inspected and summarized
- README blob SHA: 0d6e5008c11d4b1227a790f775c23ba62fb301ad
- Relationship note: The repository is maintained under Apple's primary public GitHub organization.

## Project overview

A shared project where password-manager creators and users collaborate on website-specific compatibility data (quirks) and code. Its goal is to let password managers reuse compatibility discoveries and encourage websites to adopt standards that communicate password requirements consistently.

## Features and capabilities documented by the README

- Machine-readable password rules for domains with special password-policy requirements.
- Shared-credential relationships between domains, plus a separate historical file for relationships no longer valid or not confidently current.
- Change-password URL mappings to help users navigate directly to password-change pages.
- A list of websites where a generated two-factor authentication code must be appended to the password.
- Mappings between Apple app identifiers and domains that share credentials for platform AutoFill experiences.
- Browser-extension distribution information linking browsers with extension storefronts.
- A JavaScript reference parser for the Password Rules language.

## Technology stack

JSON datasets for domain rules and relationship maps; JavaScript reference parser; Ruby and JavaScript are the languages named by Apple's Open Source project page. It links Apple's password-autofill APIs and the Password Rules language. This is a data-and-reference-code project, not a password manager application.

## Getting started

Review the README and CONTRIBUTING guide for each quirks-file schema. Integrators should consume only supported resource types and contribute updated findings back. The README points to Apple's native password-autofill APIs and Password Rules language.

## Lifecycle, compatibility and operational considerations

Security and privacy caution: the README says shared-credential data must not release credentials to a website without the user's explicit review and consent; suggestions should remain site-bound and scoped. Historical relationships are separated because they may no longer be valid. A listed relationship is not permission to autofill across domains without user confirmation.

## Evaluation guidance

Check the current upstream release, dependency manifests, exact platform/toolchain requirements, licence and security guidance before adoption. This dossier summarizes the inspected README; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/apple/password-manager-resources)
- [README](https://github.com/apple/password-manager-resources/blob/main/README.md)
- [Issues](https://github.com/apple/password-manager-resources/issues)
- [Releases](https://github.com/apple/password-manager-resources/releases)

Evidence note: the README blob SHA identifies the upstream README revision inspected. Technology details not established by the README or official project page are left unspecified.
