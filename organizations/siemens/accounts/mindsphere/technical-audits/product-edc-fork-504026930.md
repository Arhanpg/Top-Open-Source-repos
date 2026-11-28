# mindsphere/product-edc-fork

- Company: Siemens
- Account: mindsphere
- Repository: https://github.com/mindsphere/product-edc-fork
- Default branch: develop
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:07:05+00:00

## Project purpose

Container images and deployments of the Eclipse Dataspace Connector open source project. · ·

## Why this project is used

Repository for Catena-X specific eclipse dataspace connector apps

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, Smarty, Dockerfile, Gherkin
- Frameworks/libraries: Unknown / not established
- Dependency names: apache-commons-pool-sql, api-configuration, api-core, asset-api, asset-index-sql, assetindex-cosmos, auth-basic, auth-spi, auth-tokenbased, awaitility, aws-s3, aws-test, azure-eventgrid, azure-eventgrid-config, azure-test, azure-vault, bcpkix-jdk15on, blob-core, blob-operator, blob-provision, blobstorage, business-partner-validation, catalog, catalog-api, catalog-cache, catalog-spi, common-sql, common-util, commons-build-plugin, contract, contract-definition-store-cosmos, contract-negotiation-store-cosmos, contract-spi, contractagreement-api, contractdefinition-api, contractdefinition-store-sql, contractnegotiation-api, contractnegotiation-store-sql, control-api, control-plane-core, core, core-base, core-boot, core-defaults, core-micrometer, core-policy, core-spi, cosmos, cosmos-common, cucumber-java, cucumber-junit-platform-engine, cx-oauth2, data-encryption, data-management-api, data-plane-api, data-plane-azure-storage, data-plane-framework, data-plane-http, data-plane-s3, data-plane-selector-api, data-plane-selector-client, data-plane-selector-core, data-plane-selector-spi, data-plane-spi, data-plane-transfer, data-plane-transfer-client, data-plane-transfer-spi, data-plane-transfer-sync, dataloading, dataplane-selector-configuration, decentralized-identity, dummy-credentials-verifier, edc-controlplane, edc-controlplane-base, edc-controlplane-memory, edc-controlplane-postgresql, edc-controlplane-postgresql-hashicorp-vault, edc-dataplane, edc-dataplane-azure-vault, edc-dataplane-base, edc-dataplane-hashicorp-vault, edc-extensions, edc-tests, exec-maven-plugin, fcc-node-directory-cosmos, federated-catalog-spi, filesystem-configuration, filesystem-vault, flyway-core, gson, hashicorp-vault, http, http-provisioner, http-receiver, httpclient, iam-daps, iam-mock, identity-common-test, identity-did-core, identity-did-crypto, identity-did-service, identity-did-spi, identity-did-web, ids, ids-api-configuration, ids-api-multipart-dispatcher-v1, ids-api-multipart-endpoint-v1, ids-api-transform-v1, ids-core, ids-spi, jacoco-maven-plugin, jdk-logger-monitor, jersey-micrometer, jetty-micrometer, junit-jupiter-api, junit-platform-suite, jwt-core, jwt-spi, logback-classic, lombok
- Build/package tools: Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: edc-extensions/business-partner-validation/src/main/java/net/catenax/edc/validation/businesspartner/BusinessPartnerValidationExtension.java, edc-extensions/business-partner-validation/src/main/java/net/catenax/edc/validation/businesspartner/functions/AbstractBusinessPartnerValidation.java, edc-extensions/business-partner-validation/src/main/java/net/catenax/edc/validation/businesspartner/functions/BusinessPartnerDutyFunction.java, edc-extensions/business-partner-validation/src/main/java/net/catenax/edc/validation/businesspartner/functions/BusinessPartnerPermissionFunction.java

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/mindsphere/product-edc-fork/blob/develop/README.md
- README SHA: c9cf6eb50c2baf2ad4b838b95e68a591d9c66f51
- Manifests: pom.xml, edc-controlplane/pom.xml, edc-dataplane/pom.xml, edc-extensions/pom.xml, edc-tests/pom.xml, edc-controlplane/edc-controlplane-base/pom.xml
- Sampled source files: edc-extensions/business-partner-validation/src/main/java/net/catenax/edc/validation/businesspartner/BusinessPartnerValidationExtension.java, edc-extensions/business-partner-validation/src/main/java/net/catenax/edc/validation/businesspartner/functions/AbstractBusinessPartnerValidation.java, edc-extensions/business-partner-validation/src/main/java/net/catenax/edc/validation/businesspartner/functions/BusinessPartnerDutyFunction.java, edc-extensions/business-partner-validation/src/main/java/net/catenax/edc/validation/businesspartner/functions/BusinessPartnerPermissionFunction.java
- Git tree state: captured
- Evidence fingerprint: 94b9fcc22d9f96e1edf2fecb2d9372efcfb002ea0b6baa0ea1b724af978d4965

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
