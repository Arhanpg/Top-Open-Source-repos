# Industrial Edge — Hands-on App Developer Guide

- **Company association:** Siemens
- **Upstream GitHub account:** [industrial-edge](https://github.com/industrial-edge)
- **Repository:** [industrial-edge/Developer-Guide-Hands-on-App](https://github.com/industrial-edge/Developer-Guide-Hands-on-App)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/industrial-edge/Developer-Guide-Hands-on-App/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `8ef605257100f77207c8962ccf4a1de74e5b6789`
- **Account relationship:** Siemens's official Open Source portal lists this product-specific account; the account's repositories are not assumed to be all Siemens-authored or legally owned.

## Project overview

A tutorial/sample application showing how to develop an Industrial Edge app that collects, processes, stores and visualizes data from an OPC UA server connected to a PLC. It demonstrates how system apps, MQTT messaging and a custom analytics container can be combined on an Industrial Edge Device.

## Features and capabilities documented by the README

- Uses the OPC UA Connector system app to collect data from an OPC UA server and publish it to the Industrial Edge Databus.
- Uses the Industrial Edge Databus, based on MQTT, to distribute data between system apps and custom applications through topics.
- Uses SIMATIC Flow Creator to subscribe to connector topics, preprocess data and publish the processed data back to the Databus.
- Runs a Python data-analytics container that consumes MQTT topics, performs calculations/evaluation and publishes key performance indicators back to the Databus.
- Uses SIMATIC Flow Creator and InfluxDB to persist raw and analyzed time-series data.
- Shows basic visualization with native InfluxDB dashboards and mentions Grafana as an alternative dashboard project.
- Provides example Dockerfiles and a linked step-by-step developer guide.

## Technology stack

Docker containers; Python analytics application; MQTT; Industrial Edge Databus; OPC UA Connector; OPC UA; PLC data; SIMATIC Flow Creator; InfluxDB time-series database; InfluxDB dashboards (with Grafana noted as an alternative).

## Getting started

Use the prerequisites and step-by-step App Developer Guide on industrial-edge.io. To run the sample solution, the README asks users to rename Dockerfile.example files to Dockerfile; those files are examples to adapt to the target environment.

## Lifecycle, compatibility and operational considerations

This repository is a hands-on sample, not a complete production application or a turnkey industrial deployment. The README explicitly warns that the example contains or uses third-party software and that users are responsible for complying with the applicable third-party licences and using those components at their own discretion and risk.

## Evaluation guidance

Check the exact upstream release, build/dependency manifests, supported platforms/toolchain, licence, operational prerequisites and security guidance before adoption. This dossier summarizes the inspected README; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/industrial-edge/Developer-Guide-Hands-on-App)
- [README](https://github.com/industrial-edge/Developer-Guide-Hands-on-App/blob/main/README.md)
- [Issues](https://github.com/industrial-edge/Developer-Guide-Hands-on-App/issues)
- [Releases](https://github.com/industrial-edge/Developer-Guide-Hands-on-App/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. Technology claims are limited to the README and company-profile evidence; unsupported implementation details are not inferred.*
