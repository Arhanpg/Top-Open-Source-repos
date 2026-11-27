# aws-robotics/health-metrics-collector-ros1

- Company: Amazon
- Account: aws-robotics
- Repository: https://github.com/aws-robotics/health-metrics-collector-ros1
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:13:12+00:00

## Project purpose

This health_metric_collector ROS node collects system metrics and publishes them to /metrics topic. The cloudwatch_metrics_collector node is subscribed to this topic and will publish the metrics to AWS CloudWatch when it is instantiated.

## Why this project is used

This is a node for ROS1 that collects metrics about cpu usage and publishes them to a topic to be pushed to CloudWatch Metrics.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, CMake
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: health_metric_collector/src/collector.cpp, health_metric_collector/src/cpu_data.cpp, health_metric_collector/src/cpu_metric_collector.cpp, health_metric_collector/src/cpu_stats.cpp

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-robotics/health-metrics-collector-ros1/blob/master/README.md
- README SHA: 497e8fec103b9e3d68e7f54ff93dd6b22e4f1a7e
- Manifests: health_metric_collector/CMakeLists.txt
- Sampled source files: health_metric_collector/src/collector.cpp, health_metric_collector/src/cpu_data.cpp, health_metric_collector/src/cpu_metric_collector.cpp, health_metric_collector/src/cpu_stats.cpp
- Git tree state: captured
- Evidence fingerprint: cbc0369350e3bb29aa0a4b11cb11d02978f6b0a97868876e4f6db9a1fc8fcd6a

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
