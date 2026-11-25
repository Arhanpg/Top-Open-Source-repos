# aws-deepracer/aws-deepracer-follow-the-leader-sample-project

- Company: Amazon
- Account: aws-deepracer
- Repository: https://github.com/aws-deepracer/aws-deepracer-follow-the-leader-sample-project
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:21:14+00:00

## Project purpose

The AWS DeepRacer Follow the Leader (FTL) sample project is an sample application built on top of the existing AWS DeepRacer application, which uses an object-detection machine learning model through which the AWS DeepRacer device can identify and follow a person. For detailed information on the FTL sample project, see the Getting started section.

## Why this project is used

Learn to deploy an object detection model that enables the AWS DeepRacer device to identify and follow an object.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, C++, CMake, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: deepracer_follow_the_leader_ws/ctrl_pkg/src/ctrl_node.cpp, deepracer_follow_the_leader_ws/ctrl_pkg/src/ctrl_state.cpp, deepracer_follow_the_leader_ws/ctrl_pkg/include/ctrl_pkg/ctrl_state.hpp, deepracer_follow_the_leader_ws/ctrl_pkg/include/ctrl_pkg/ctrl_state_base.hpp

## Setup and usage

- Installation: Follow these steps to install the AWS DeepRacer Follow the Leader (FTL) sample project.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-deepracer/aws-deepracer-follow-the-leader-sample-project/blob/main/README.md
- README SHA: ea1745dc2e25655e21658ac8c1ce6e97a65dce70
- Manifests: deepracer_follow_the_leader_ws/ctrl_pkg/CMakeLists.txt, deepracer_follow_the_leader_ws/deepracer_interfaces_pkg/CMakeLists.txt, deepracer_follow_the_leader_ws/ftl_launcher/CMakeLists.txt, deepracer_follow_the_leader_ws/ftl_navigation_pkg/setup.py, deepracer_follow_the_leader_ws/object_detection_pkg/setup.py, deepracer_follow_the_leader_ws/webserver_pkg/setup.py
- Sampled source files: deepracer_follow_the_leader_ws/ctrl_pkg/src/ctrl_node.cpp, deepracer_follow_the_leader_ws/ctrl_pkg/src/ctrl_state.cpp, deepracer_follow_the_leader_ws/ctrl_pkg/include/ctrl_pkg/ctrl_state.hpp, deepracer_follow_the_leader_ws/ctrl_pkg/include/ctrl_pkg/ctrl_state_base.hpp
- Git tree state: captured
- Evidence fingerprint: 784615e6336f610828f55d3417e87b16be6c9c1d10cb39149832914f2ee93b8a

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
