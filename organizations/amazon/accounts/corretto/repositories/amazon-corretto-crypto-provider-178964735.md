# corretto/amazon-corretto-crypto-provider

- Company: Amazon
- GitHub account: [https://github.com/corretto](https://github.com/corretto)
- Mapping status: official-directory-listed
- Repository: [corretto/amazon-corretto-crypto-provider](https://github.com/corretto/amazon-corretto-crypto-provider)
- Default branch: main
- README: [Open upstream README](https://github.com/corretto/amazon-corretto-crypto-provider/blob/main/README.md)
- README blob SHA: 6e434e0c34130098c04a76cebb13fa94bf18f13a
- Repository ID: 178964735
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Amazon Corretto Crypto Provider is a collection of high-performance cryptographic implementations exposed via standard JCA/JCE interfaces.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:34:56+00:00

### Short excerpt (up to 100 words)

> The Amazon Corretto Crypto Provider (ACCP) is a collection of high-performance cryptographic implementations exposed via the standard JCA/JCE interfaces. This means that it can be used as a drop in replacement for many different Java applications. (Differences from the default OpenJDK implementations are documented here.) As of 2.0.0, algorithms exposed by ACCP are primarily backed by AWS-LC's implementations. We provide complete benchmarking data from our benchmarking suite for the current tip of `main`. MessageDigest algorithms: * SHA-512 * SHA-384 * SHA-256 * SHA-1 * MD5 Mac algorithms: * HmacSHA512 * HmacSHA384 * HmacSHA224 * HmacSHA256 * HmacSHA1 * HmacMD5 Cipher

### README headings

- Amazon Corretto Crypto Provider
- Build Status
- Performance Benchmarks
- Supported Algorithms
- ML-KEM Considerations
- Notes on ACCP-FIPS
- Compatibility & Requirements
- JDK 25+ Native Access
- Platform Support
- Supported Platforms
- Other platforms
- Using the provider
- Installation
- Maven
- Gradle
- Bundle ACCP with JDK
- Manual
- Download from GitHub releases
- Build it yourself
- Repackaging ACCP into Uber/Fat Jars
- Building ACCP in FIPS mode
- All targets
- Configuration
- Code
- Via Security Properties
- Modify the JVM settings
- Verification (Optional)
- Other system properties
- Build Parameters
- Target JDK Version

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 1,824,779 |
| C++ | 327,928 |
| CMake | 49,692 |
| Shell | 36,522 |
| Python | 3,608 |
| C | 740 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build.gradle (capture: captured)
- CMakeLists.txt (capture: captured)
- benchmarks/lib/build.gradle.kts (capture: captured)
- CMake/trycompile/CMakeLists.txt (capture: captured)
- examples/gradle-kt-dsl/lib/build.gradle.kts (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 275
- Forks at capture: 82
- Last updated: 2026-11-19T07:29:46Z
- Last pushed: 2026-11-23T19:34:50Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/corretto/amazon-corretto-crypto-provider)
- [README](https://github.com/corretto/amazon-corretto-crypto-provider/blob/main/README.md)
- [Issues](https://github.com/corretto/amazon-corretto-crypto-provider/issues)
- [Releases](https://github.com/corretto/amazon-corretto-crypto-provider/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
