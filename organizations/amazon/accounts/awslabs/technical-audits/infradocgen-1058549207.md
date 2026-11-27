# awslabs/InfraDocGen

- Company: Amazon
- Account: awslabs
- Repository: https://github.com/awslabs/InfraDocGen
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:26:33+00:00

## Project purpose

The Infrastructure Document Generator is an intelligent automation tool that revolutionizes AWS infrastructure documentation and analysis. By automatically scanning cloud environments, it creates comprehensive, real-time documentation with detailed configuration reports, including dependency maps of resources based on access policies. The tool goes beyond basic documentation by providing actionable insights based on AWS Well-Architected Framework principles, providing reports on Security Best Practices, Comprehensive Analysis and Performance Improvement, enabling organizations to optimize their cloud infrastructure while maintaining accurate documentation with minimal effort.

## Why this project is used

The Infrastructure Document Generator is an intelligent automation tool that revolutionizes AWS infrastructure documentation and analysis. By automatically scanning cloud environments, it creates comprehensive, real-time documentation with detailed configuration reports, including dependency maps of resources based on access policies. The tool goes beyond basic documentation by providing actionable insights based on AWS Well-Architected Framework principles, providing reports on Security Best Practices, Comprehensive Analysis and Performance Improvement, enabling organizations to optimize their cloud infrastructure while maintaining accurate documentation with minimal effort.

## Core features

- Displays AWS resources organized by service and region: Displays AWS resources organized by service and region
  - Evidence: README.md#Features
- AI-powered infrastructure analysis and documentation: AI-powered infrastructure analysis and documentation
  - Evidence: README.md#Features
- Interactive dependency graphs with drag-and-drop functionality: Interactive dependency graphs with drag-and-drop functionality
  - Evidence: README.md#Features
- Real-time progress tracking for analysis operations: Real-time progress tracking for analysis operations
  - Evidence: README.md#Features
- Clean, responsive UI using AWS Cloudscape Design components: Clean, responsive UI using AWS Cloudscape Design components
  - Evidence: README.md#Features
- Context API for data fetching and state management: Context API for data fetching and state management
  - Evidence: README.md#Features

## Technology stack

- Languages: Python, JavaScript, CSS, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @cloudscape-design/components, @cloudscape-design/global-styles, @vitejs/plugin-react, axios, boto3, botocore, deepdiff, elkjs, fastapi, pydantic, python-dateutil, python-multipart, react, react-dom, react-markdown, reactflow, typing-extensions, urllib3, uvicorn, vite
- Build/package tools: npm-compatible manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: main.py, infra-ui/src/App.jsx, infra-ui/src/components/DashboardView.jsx, infra-ui/src/components/InfrastructureAnalysis.jsx

## Setup and usage

- Usage: 1. Start the backend API server
- Usage: 2. Launch the frontend application
- Usage: 3. Navigate to http://localhost:3000
- Usage: 4. Use the interface to scan AWS infrastructure and generate documentation

## Limitations and caveats

- Security & Identity Services: - **IAM**: Users, Groups, Roles, Policies
- Security & Identity Services: - **Secrets Manager**: Secrets
- Security & Identity Services: - **ACM**: Certificates
- Security & Identity Services: - **Shield**: Protections
- Security & Identity Services: - **GuardDuty**: Detectors
- Security & Identity Services: - **WAF/WAFv2**: Web ACLs
- Security & Identity Services: - **Macie**: Classification Jobs
- Security Best Practices: - **Never commit AWS credentials** to version control

## Evidence and provenance

- README: https://github.com/awslabs/InfraDocGen/blob/main/README.md
- README SHA: 6ac0eb7a0a828edf16b9a4a4bd0c9a223a65cacd
- Manifests: requirements.txt, infra-ui/package.json
- Sampled source files: main.py, infra-ui/src/App.jsx, infra-ui/src/components/DashboardView.jsx, infra-ui/src/components/InfrastructureAnalysis.jsx
- Git tree state: captured
- Evidence fingerprint: 3224809aea2436c23d9e99f306aae447dac9784520fcc41461d7da8e9904f827

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
