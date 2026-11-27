# aws-robotics/health-metrics-collector-ros2

- Company: Amazon
- Account: aws-robotics
- Repository: https://github.com/aws-robotics/health-metrics-collector-ros2
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:19:56+00:00

## Project purpose

This health_metric_collector ROS node collects system metrics and publishes them to /metrics topic. The cloudwatch_metrics_collector node is subscribed to this topic and will publish the metrics to AWS CloudWatch when it is instantiated.

## Why this project is used

ROS2 node that collects metrics about system resource consumption and publishes them to a topic to be emitted to CloudWatch Metrics.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, CMake, Python
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

- README: https://github.com/aws-robotics/health-metrics-collector-ros2/blob/master/README.md
- README SHA: 41d8ad8c6e578a0b8e26655b7f42ce23fe67cadb
- Manifests: health_metric_collector/CMakeLists.txt
- Sampled source files: health_metric_collector/src/collector.cpp, health_metric_collector/src/cpu_data.cpp, health_metric_collector/src/cpu_metric_collector.cpp, health_metric_collector/src/cpu_stats.cpp
- Git tree state: captured
- Evidence fingerprint: 17473598bea6a914ee1834651c449286a010e9dda298500715f3098118e9ef22

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
