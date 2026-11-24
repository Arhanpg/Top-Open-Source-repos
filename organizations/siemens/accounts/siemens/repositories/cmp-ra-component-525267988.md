# siemens/cmp-ra-component

- Company: Siemens
- GitHub account: [https://github.com/Siemens](https://github.com/Siemens)
- Mapping status: verified
- Repository: [siemens/cmp-ra-component](https://github.com/siemens/cmp-ra-component)
- Default branch: main
- README: [Open upstream README](https://github.com/siemens/cmp-ra-component/blob/main/README.md)
- README blob SHA: e14c1020cd3b294322f3492c06835aea801e8c5b
- Repository ID: 525267988
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A CMP Registration Authority (RA) and CMP client core component

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:35:47+00:00

### Short excerpt (up to 100 words)

> The generic CMP component supports the implementation of Java applications that provide CMP Registration Authority (RA) and/or CMP client functions. It implements all CMP features specified in the https://datatracker.ietf.org/doc/rfc9483/), reflecting the updates to CMPv2 (RFC 4210) and CRMF (RFC 4211) given in https://datatracker.ietf.org/doc/rfc9480/) and [Certificate Management Protocol (CMP) Algorithms, RFC 9481]( https://datatracker.ietf.org/doc/rfc9481/). It has been used as the reference implementation for the standardization of CMP Updates, CMP Algorithms, the Lightweight CMP Profile (LCMPP), and the new [Internet X.509 PKI -- Certificate Management Protocol (CMP) RFC 9810]( https://datatracker.ietf.org/doc/rfc9810/). It serves as the core of productive Java-based CMP developments.\ It is also

### README headings

- generic CMP RA and CMP client component
- Interfaces of generic CMP RA component
- Basic features for use in PoCs, reference implementations, and in production
- Advanced CMP RA features, in particular for productive use
- Overall software design
- Structure of the generic CMP RA component
- Message exchange API design
- Component and interface design
- Dynamic message exchange behavior on the downstream CMP interface and upstream PKCS#10/X.509 interface
- Dynamic message exchange behavior for downstream and upstream CMP interface
- Configuration interface design
- Interfaces to inventory for certification request validation
- Features of the generic CMP client component
- Structure of the generic CMP client component
- Message exchange API design
- Component and interface design
- Dynamic message exchange behavior for downstream and upstream CMP interface
- Configuration interface design
- Javadoc API documentation
- Acknowledgements

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 1,178,228 |
| PowerShell | 20,350 |
| Python | 6,669 |
| Batchfile | 571 |
| Shell | 76 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: CmpRaComponent, bcpkix-jdk18on, bcprov-jdk18on, cyclonedx-maven-plugin, dependency-check-maven, jackson-databind, jackson-dataformat-yaml, jackson-datatype-jsr310, jacoco-maven-plugin, junit, maven-dependency-plugin, maven-gpg-plugin, maven-jar-plugin, maven-javadoc-plugin, maven-source-plugin, maven-surefire-plugin, nexus-staging-maven-plugin, plexus-utils, slf4j-simple, sonar-maven-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 7
- Last updated: 2026-09-22T08:29:52Z
- Last pushed: 2026-09-22T08:29:47Z
- Topics: certificates, cmp, component-library, java, lcmpp, rfc4210, rfc9480, x509

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/siemens/cmp-ra-component)
- [README](https://github.com/siemens/cmp-ra-component/blob/main/README.md)
- [Issues](https://github.com/siemens/cmp-ra-component/issues)
- [Releases](https://github.com/siemens/cmp-ra-component/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
