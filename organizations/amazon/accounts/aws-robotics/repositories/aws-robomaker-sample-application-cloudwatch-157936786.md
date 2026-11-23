# aws-robotics/aws-robomaker-sample-application-cloudwatch

- Company: Amazon
- GitHub account: [https://github.com/aws-robotics](https://github.com/aws-robotics)
- Mapping status: official-directory-listed
- Repository: [aws-robotics/aws-robomaker-sample-application-cloudwatch](https://github.com/aws-robotics/aws-robomaker-sample-application-cloudwatch)
- Default branch: ros1
- README: [Open upstream README](https://github.com/aws-robotics/aws-robomaker-sample-application-cloudwatch/blob/ros1/README.md)
- README blob SHA: a088d1403d18c3473a481e42a2f248a20411096f
- Repository ID: 157936786
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Use AWS RoboMaker and demonstrate monitoring robot health and operational metrics with AWS CloudWatch. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:39:25+00:00

### Short excerpt (up to 100 words)

> Monitor health and operational metrics for a fleet of robots in a simulated home using AWS CloudWatch Metrics and AWS CloudWatch Logs. Streamed metrics include speed, distance to nearest obstacle, distance to current goal, robot CPU utilization, and RAM usage. It demonstrates how to emit metrics and logs to AWS CloudWatch to monitor your robots. _RoboMaker sample applications include third-party software licensed under open-source licenses and is provided for demonstration purposes only. Incorporation or use of RoboMaker sample applications in connection with your production workloads or a commercial products or devices may affect your legal rights or obligations under the

### README headings

- AWS RoboMaker Sample Application - CloudWatch Monitoring
- Installation
- AWS Setup
- AWS Credentials
- AWS Permissions
- Build
- Install requirements
- Robot
- Simulation
- Run
- Run with a AWS Robomaker WorldForge world
- Monitoring with CloudWatch Logs
- Monitoring with CloudWatch Metrics
- Using this sample with RoboMaker
- Bundling Robot Application
- Bundling Simulation Application
- Generate Occupancy Map via map generation plugin
- Generate map for a aws-robotics world with default config
- Generate map for a WorldForge world with default config
- Run map generation script
- Generate map for a custom world with custom config
- Install dependencies (Ubuntu >18.04)
- Fetch and install ROS dependencies
- Run plugin with custom world/config,
- Build with plugin added
- Start map service (for custom worlds, relocate your world file with the added plugin to src/cloudwatch_simulation/worlds/map_plugin.world before running this)
- Generate map (start in a different terminal AFTER you see "[INFO] [*] occupancy map plugin started" message in previous terminal)
- Save map
- Move the generated map file to cloudwatch_simulation simulation workspace map directory
- AWS ROS Packages used by this Sample

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 32,611 |
| Shell | 9,312 |
| CMake | 6,880 |
| Makefile | 1,038 |
| Ruby | 535 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- robot_ws/src/cloudwatch_robot/CMakeLists.txt (capture: captured)
- robot_ws/src/cloudwatch_robot/setup.py (capture: captured)
- simulation_ws/src/aws_robomaker_simulation_common/CMakeLists.txt (capture: captured)
- simulation_ws/src/aws_robomaker_simulation_common/setup.py (capture: captured)
- simulation_ws/src/cloudwatch_simulation/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 22
- Forks at capture: 41
- Last updated: 2026-01-10T17:48:31Z
- Last pushed: 2021-12-30T21:33:09Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-robotics/aws-robomaker-sample-application-cloudwatch)
- [README](https://github.com/aws-robotics/aws-robomaker-sample-application-cloudwatch/blob/ros1/README.md)
- [Issues](https://github.com/aws-robotics/aws-robomaker-sample-application-cloudwatch/issues)
- [Releases](https://github.com/aws-robotics/aws-robomaker-sample-application-cloudwatch/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
