# SAP-samples/SPFI-Reference-Application

- Company: SAP
- Account: SAP-samples
- Repository: https://github.com/SAP-samples/SPFI-Reference-Application
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:10:13+00:00

## Project purpose

A Spring Boot reference application that demonstrates how to implement the **SPFI V2 REST API contract** — the standard interface between a Unified Provisioning operator and a service provider for tenant lifecycle management and SSO configuration.

## Why this project is used

Same application implementing the Service Provider Fulfilment API. A standardised API to trigger the SaaS technical fulfillment request towards SaaS Providers (SAP and Partners). Fulfilment is a high-level term compassing various activities like tenant provisioning, etc.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: annotations, bcpkix-jdk15on, jakarta.jakartaee-web-api, json, lombok, maven-compiler-plugin, spfi-v2-ref-app, spring-boot, spring-boot-maven-plugin, spring-boot-starter-json, spring-boot-starter-parent, spring-boot-starter-security, spring-boot-starter-test, spring-boot-starter-web, spring-security-test
- Build/package tools: Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/main/java/com/sap/lm/sl/spfi/refapp/spfi_v2_ref_app/model/jpa/tenant/Application.java, src/main/java/com/sap/lm/sl/spfi/refapp/spfi_v2_ref_app/config/CertificateValidationFilter.java, src/main/java/com/sap/lm/sl/spfi/refapp/spfi_v2_ref_app/config/MdcTaskDecorator.java, src/main/java/com/sap/lm/sl/spfi/refapp/spfi_v2_ref_app/config/SecurityConfig.java

## Setup and usage

No setup information established.

## Limitations and caveats

- Security (High): - **Verify the certificate chain is complete** (intermediate CAs included).
- Security (High): - **Check certificate expiration**: openssl x509 -in cert.pem -noout -dates
- Security (High): - **Ensure the server's hostname matches the CN or SAN** in the server certificate.
- Security (High): - **Validate the CN** against the response of the /certInfo endpoint from the Operator.
- Security: mTLS: All API calls are protected with mutual TLS. The operator presents a client certificate issued by the SAP PKI service; the application server validates this certificate against a configured truststore.
- Spring Security Configuration: public class SecurityConfig {
- Spring Security Configuration: public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
- Spring Security Configuration: .authorizeHttpRequests(authorize -> authorize

## Evidence and provenance

- README: https://github.com/SAP-samples/SPFI-Reference-Application/blob/main/README.md
- README SHA: 8834fa07dfd8d3ea82783e407ea626348910dbe6
- Manifests: Makefile, pom.xml
- Sampled source files: src/main/java/com/sap/lm/sl/spfi/refapp/spfi_v2_ref_app/model/jpa/tenant/Application.java, src/main/java/com/sap/lm/sl/spfi/refapp/spfi_v2_ref_app/config/CertificateValidationFilter.java, src/main/java/com/sap/lm/sl/spfi/refapp/spfi_v2_ref_app/config/MdcTaskDecorator.java, src/main/java/com/sap/lm/sl/spfi/refapp/spfi_v2_ref_app/config/SecurityConfig.java
- Git tree state: captured
- Evidence fingerprint: 20173751eb67817d477fc4d6350647898921d8dcdb7d2e545e1e8c727175032e

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
