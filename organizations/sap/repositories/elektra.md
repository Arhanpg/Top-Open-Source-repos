# Elektra — SAP Cloud Infrastructure OpenStack Dashboard

- **Company association:** SAP
- **Upstream GitHub account:** [SAP-cloud-infrastructure](https://github.com/SAP-cloud-infrastructure)
- **Repository:** [SAP-cloud-infrastructure/elektra](https://github.com/SAP-cloud-infrastructure/elektra)
- **Default branch:** `master`
- **README:** [Open upstream README](https://github.com/SAP-cloud-infrastructure/elektra/blob/master/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `0305cee039db93afb6cacedacd41ee96570380b8`
- **Account relationship:** SAP's verified GitHub profile lists this account as a dedicated organization for the named project/product area.

## Project overview

Elektra is an opinionated OpenStack dashboard for operators and consumers of OpenStack services. Its goal is to make OpenStack more accessible by turning operator tasks into user-facing self-services.

## Features and capabilities documented by the README

- Self-service user onboarding, project creation/configuration and quota requests.
- Authorization and access-control workflows for projects and services, plus cost-control interfaces.
- Dashboard interfaces for Nova compute resources such as servers, images and snapshots.
- Interfaces for Cinder block storage, Keystone roles, Barbican key storage and Neutron networks/routers/floating IPs/security groups.
- Additional interfaces for Octavia load balancing, Designate DNS, Swift object storage and Manila shared file storage.
- Extended services include SAP HANA as a Service and SAP Kubernetes as a Service.

## Technology stack

Ruby 3.4.8 and Rails 7.1.6 backend; Node.js 22.16.0 and React 18.2.0 frontend; PostgreSQL database (the README's local setup instructions reference PostgreSQL 16.4); pnpm for frontend packages; OpenStack service APIs. The repository's README advertises Apache-2.0.

## Getting started

Follow the local setup instructions: configure PostgreSQL, Ruby/Bundler and Node.js, install Ruby gems with bundle install and JavaScript dependencies with pnpm, then create/migrate/seed the database and configure the environment against an appropriate OpenStack installation. Some SAP Cloud Infrastructure packages require GitHub Packages read access.

## Lifecycle, compatibility and operational considerations

**Critical deployment limitation:** the README explicitly says Elektra is not compatible out of the box with vanilla OpenStack. It depends on custom SAP Cloud Infrastructure implementations for project onboarding, resource management and specialized services; it can run only on OpenStack installations customized for SAP Cloud Infrastructure. Its README also identifies private GitHub Packages used by some components.

## Evaluation guidance

Check the exact upstream release, build/dependency manifests, supported platforms/toolchain, licence, operational prerequisites and security guidance before adoption. This dossier summarizes the inspected README; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/SAP-cloud-infrastructure/elektra)
- [README](https://github.com/SAP-cloud-infrastructure/elektra/blob/master/README.md)
- [Issues](https://github.com/SAP-cloud-infrastructure/elektra/issues)
- [Releases](https://github.com/SAP-cloud-infrastructure/elektra/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. Technology claims are limited to the README and company-profile evidence; unsupported implementation details are not inferred.*
