# aws-solutions/deepracer-on-aws

- Company: Amazon
- Account: aws-solutions
- Repository: https://github.com/aws-solutions/deepracer-on-aws
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:03:37+00:00

## Project purpose

DeepRacer on AWS is a solution that allows you to train and evaluate reinforcement learning models in a three-dimensional simulated autonomous-driving environment. The trained model can then be downloaded to a AWS DeepRacer vehicle (a 1/18th scale RC car capable of running inference on a trained AWS DeepRacer model for autonomous driving) so it can drive in a physical environment. You can also submit your model to a virtual race and have its performance ranked against other models in a virtual leaderboard.

## Why this project is used

DeepRacer on AWS is the latest evolution of AWS DeepRacer, delivering a self-hosted reinforcement learning solution you can deploy to your AWS account to train and evaluate autonomous-driving models in a 3D simulated environment.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, Python, Smithy, Shell, JavaScript, CSS, Dockerfile, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-amplify/ui-react, @aws-crypto/sha256-browser, @aws-lambda-powertools/logger, @aws-lambda-powertools/metrics, @aws-lambda-powertools/tracer, @aws-sdk/client-appconfig, @aws-sdk/client-appconfigdata, @aws-sdk/client-cloudwatch-logs, @aws-sdk/client-dynamodb, @aws-sdk/client-kinesis-video, @aws-sdk/client-kinesis-video-archived-media, @aws-sdk/client-kinesis-video-media, @aws-sdk/client-lambda, @aws-sdk/client-s3, @aws-sdk/client-sagemaker, @aws-sdk/client-service-quotas, @aws-sdk/client-sfn, @aws-sdk/client-sqs, @aws-sdk/client-ssm, @aws-sdk/client-sts, @aws-sdk/lib-dynamodb, @aws-sdk/lib-storage, @aws-sdk/signature-v4, @aws-sdk/util-dynamodb, @aws-smithy/server-apigateway, @aws-smithy/server-common, @aws-solutions-constructs/aws-cloudfront-s3, @aws-solutions-constructs/aws-wafwebacl-apigateway, @cloudscape-design/board-components, @cloudscape-design/code-view, @cloudscape-design/collection-hooks, @cloudscape-design/components, @cloudscape-design/design-tokens, @cloudscape-design/global-styles, @deepracer-indy/config, @deepracer-indy/database, @deepracer-indy/typescript-client, @deepracer-indy/typescript-server-client, @deepracer-indy/utils, @hookform/devtools, @hookform/resolvers, @nx/eslint, @nx/eslint-plugin, @nx/js, @nx/react, @nx/storybook, @nx/vite, @nx/vitest, @nx/web, @nx/workspace, @react-three/drei, @react-three/fiber, @reduxjs/toolkit, @smithy/middleware-retry, @smithy/protocol-http, @smithy/types, @storybook/addon-actions, @storybook/addon-console, @storybook/addon-essentials, @storybook/addon-interactions, @storybook/addon-links, @storybook/core-server, @storybook/react, @storybook/react-vite, @storybook/test, @storybook/test-runner, @stylistic/eslint-plugin, @swc-node/register, @swc/core, @swc/helpers, @testing-library/jest-dom, @testing-library/react, @testing-library/user-event, @types/aws-lambda, @types/humanize-duration, @types/js-yaml, @types/node, @types/react, @types/react-dom, @types/three, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @vitejs/plugin-react-swc, @vitest/coverage-v8, @vitest/ui, ace-builds, avataaars, aws-amplify, aws-cdk, aws-cdk-lib, aws-iot-device-sdk-v2, aws-sdk-client-mock, aws-sdk-client-mock-vitest, constructs, electrodb, esbuild, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-jsx-a11y, eslint-plugin-prettier, eslint-plugin-react, eslint-plugin-react-hooks, eslint-plugin-react-refresh, eslint-plugin-storybook, eslint-plugin-testing-library, eslint-plugin-vitest, fractional-indexing, hls.js, humanize-duration, i18n-iso-countries, i18next, i18next-intervalplural-postprocessor, jiti, js-yaml, jsdom, msw, msw-storybook-addon, nanoid
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: source/apps/infra/lib/constructs/ecr-image-downloader/index.ts, source/apps/website/src/components/AppLayout/components/Breadcrumbs/index.ts, source/apps/website/src/components/AppLayout/components/SideNavigation/index.ts, source/apps/website/src/components/AppLayout/components/TopNavigation/index.ts

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-solutions/deepracer-on-aws/blob/main/README.md
- README SHA: c517623a3e92e32f5859e2ea3e0557776bbd76ff
- Manifests: source/package.json, deployment/cdk-solution-helper/package.json, source/apps/infra/package.json, source/apps/website/package.json, source/libs/config/package.json, source/libs/database/package.json
- Sampled source files: source/apps/infra/lib/constructs/ecr-image-downloader/index.ts, source/apps/website/src/components/AppLayout/components/Breadcrumbs/index.ts, source/apps/website/src/components/AppLayout/components/SideNavigation/index.ts, source/apps/website/src/components/AppLayout/components/TopNavigation/index.ts
- Git tree state: captured
- Evidence fingerprint: fe0049a3630f6bdd19452ee361e40c882f9f0d3989461a4e017b4584005e6384

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
