# Azure/acr-web-manager

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/acr-web-manager](https://github.com/Azure/acr-web-manager)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/acr-web-manager/blob/master/README.md)
- README blob SHA: 86a6d01dd83914bef92aee0f1d6f108f789a7b88
- Repository ID: 73516199
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Azure Container Registry Web Management Portal

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:40:52+00:00

### Short excerpt (up to 100 words)

> The ACR Web Manager enables you to view metadata about your respositories and tags stored in your Azure Container Registry. You can find out more information about Azure Container Registry here. $ docker run -it -p 5000:80 azurecr/web-manager Make sure you have installed dotnet core 3.0 $ cd src/WebManager/app $ npm install $ cd .. $ dotnet restore $ dotnet run $ cd src/ $ docker build -t acrmanager -f WebManager/Dockerfile . $ docker run -p 5000:80 -it --rm acrmanager

### README headings

- Azure Container Registry Web Manager
- Running locally in Docker
- Build instructions
- Buiding and running the Docker image:

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 45,714 |
| C# | 14,678 |
| CSS | 3,478 |
| HTML | 1,913 |
| Dockerfile | 764 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/WebManager.sln (capture: captured)
- src/WebManager/Dockerfile (capture: captured)
- src/WebManager/WebManager.csproj (capture: captured)
- src/WebManager/app/package.json (capture: captured) — dependency clues: @types/axios, @types/jest, @types/node, @types/react, @types/react-dom, @types/react-router, @types/react-router-dom, ajv, axios, bootstrap, cross-env, es6-promise, jquery, office-ui-fabric-react, react, react-dom, react-router-bootstrap, react-router-dom, react-scripts, reactstrap

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 20
- Forks at capture: 10
- Last updated: 2025-11-04T19:32:57Z
- Last pushed: 2022-10-18T21:36:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/acr-web-manager)
- [README](https://github.com/Azure/acr-web-manager/blob/master/README.md)
- [Issues](https://github.com/Azure/acr-web-manager/issues)
- [Releases](https://github.com/Azure/acr-web-manager/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
