# amazon-connect/amazon-connect-chat-ui-examples

- Company: Amazon
- Account: amazon-connect
- Repository: https://github.com/amazon-connect/amazon-connect-chat-ui-examples
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T23:07:38+00:00

## Project purpose

This repo contains examples on how to implement the customer side of Amazon Connect chat. Please refer to the README under each solution to see the complete details as to what each solution does and how to deploy it.

## Why this project is used

Examples of how to create and customize the customer side chat for Amazon Connect

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript, Swift, Kotlin, HTML, CSS, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-sdk/client-connect, @babel/core, @babel/preset-env, @babel/preset-react, @expo/webpack-config, @react-native-async-storage/async-storage, @react-native-community/netinfo, @react-native/assets-registry, @react-navigation/native, @react-navigation/stack, @testing-library/react-hooks, @testing-library/react-native, amazon-connect-chatjs, animejs, axios, babel-loader, babel-plugin-module-resolver, body-parser, buffer, cors, css-loader, eslint, eslint-plugin-react, expo, expo-standard-web-crypto, express, file-loader, husky, jest, jest-environment-jsdom, jest-react-native, lint-staged, prettier, prop-types, react, react-dom, react-icons, react-native, react-native-elements, react-native-gesture-handler, react-native-get-random-values, react-native-gifted-chat, react-native-keyboard-controller, react-native-lightbox, react-native-loading-spinner-overlay, react-native-polyfill-globals, react-native-reanimated, react-native-safe-area-context, react-native-screens, react-native-url-polyfill, react-native-vector-icons, react-native-web, react-router-dom, react-spinners, react-test-renderer, react-transition-group, style-loader, styled-components, supertest, web-streams-polyfill, webpack, webpack-cli
- Build/package tools: Gradle build file, Gradle Kotlin build file, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: customChatWidget/src/App.js, customChatWidget/src/components/ChatButton/index.js, customChatWidget/src/components/ChatIcon/index.js, customChatWidget/src/components/InputField/index.js

## Setup and usage

- Part 3 - Example Usage: The index.html within amazon-connect-chat-interface/local-testing folder provides an example html page that you use to test your code.
- Part 3 - Example Usage: * Import the amazon-connect-chat-interface.js bundle file within a tag. Code Ref
- Part 3 - Example Usage: * Configure the apiGatewayEndpoint in local-testing/backendEndpoints.js and import backendEndpoints.js file within a tag. Code Ref
- Part 3 - Example Usage: * (Optional) Following Steps in Admin Guide to use JWT
- Part 3 - Example Usage: * Within connect.ChatInterface.initiateChat function, pass the x-amz-snippet-id header and x-amz-security-token header (optional)
- Part 3 - Example Usage: connect.ChatInterface.initiateChat({
- Part 3 - Example Usage: contactAttributes: JSON.stringify({
- Part 3 - Example Usage: "customerName": customerName

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/amazon-connect/amazon-connect-chat-ui-examples/blob/master/README.md
- README SHA: 6429fa728123323cc7664b3655d961b96cd84d9d
- Manifests: customChatWidget/package.json, startChatContactAPILocalProxy/package.json, mobileChatExamples/android-webview-sample/build.gradle, mobileChatExamples/androidChatExample/build.gradle.kts, mobileChatExamples/connectReactNativeChat/package.json, mobileChatExamples/android-webview-sample/app/build.gradle
- Sampled source files: customChatWidget/src/App.js, customChatWidget/src/components/ChatButton/index.js, customChatWidget/src/components/ChatIcon/index.js, customChatWidget/src/components/InputField/index.js
- Git tree state: captured
- Evidence fingerprint: 9f9439fb53ca75ddc56ffbc2a3d661500465bb6d755721390fad75861b57f33e

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
