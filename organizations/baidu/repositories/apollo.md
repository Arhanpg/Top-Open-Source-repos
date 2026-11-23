# Apollo Autonomous Driving Platform

- Company association: Baidu
- Upstream GitHub account: [ApolloAuto](https://github.com/ApolloAuto)
- Repository: [ApolloAuto/apollo](https://github.com/ApolloAuto/apollo)
- Default branch: master
- README: [Open upstream README](https://github.com/ApolloAuto/apollo/blob/master/README.md)
- Review status: README inspected and summarized
- README blob SHA: 7bbca0f4b25ff6da9f814ddf468cc8311c278201
- Account relationship: Baidu's verified profile lists this account under affiliated organizations; this is a project relationship, not blanket ownership of every repository.

## Project overview

Apollo is an open-source autonomous-driving platform with software modules, development tools and vehicle-integration workflows. The README describes a progression from early lane-control and low-speed closed-venue capabilities to broader urban-driving, perception, localization, planning/control and developer-tooling capabilities.

## Features and capabilities documented by the README

- Provides core autonomous-driving software areas including perception, prediction, localization, planning and control (PnC), with routing and vehicle/hardware integration workflows.
- Documents successive platform releases from Apollo 2.x through Apollo 11.0, showing upgrades to perception, prediction, scenario-based planning, localization and development tools.
- Adds package-based software organization and extension interfaces for reusable modules and secondary development.
- Includes Dreamview and Dreamview Plus developer visualisation/debugging experiences.
- Integrates data-pipeline, simulation and training/evaluation workflows for perception and planning/control.
- Apollo 9.0 adds ARM/Orin adaptation and package-based component and plugin extension methods, according to the README.
- Provides hardware and software architecture diagrams and vehicle integration/calibration documentation.

## Technology stack

C++/Python-oriented autonomous-driving stack with GPU-accelerated perception/deep-learning components. The README links Docker-based development and installation materials and references CUDA, NVIDIA GPU hardware, LibTorch and a platform adapting to ARM/Orin. Exact versioned dependencies, operating-system and vehicle hardware requirements are defined in the release-specific installation guides.

## Getting started

Use the version-specific Apollo installation and package-management documentation linked from the README. Follow the hardware integration/calibration guide for the target vehicle and sensor suite, then use the matching Dreamview and simulation workflows. Do not mix instructions across release versions.

## Lifecycle, compatibility and operational considerations

This is safety-critical autonomous-driving software. A successful build or simulation is not evidence of roadworthiness or compliance with vehicle safety requirements. Validate the exact hardware, sensor calibration, release, scenario coverage, simulation and safety controls in a controlled environment. The README contains historical release narratives; use the release-specific documentation for current setup.

## Evaluation guidance

Check the exact upstream release, source manifests, platform/toolchain requirements, licence and security guidance before adoption. This dossier summarizes the inspected README; it is not a complete source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/ApolloAuto/apollo)
- [README](https://github.com/ApolloAuto/apollo/blob/master/README.md)
- [Issues](https://github.com/ApolloAuto/apollo/issues)
- [Releases](https://github.com/ApolloAuto/apollo/releases)

Evidence note: the README blob SHA identifies the upstream revision inspected. Technical claims are limited to README-supported material; details not established by the README are left unspecified.
