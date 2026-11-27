# aws-solutions/content-localization-on-aws

- Company: Amazon
- Account: aws-solutions
- Repository: https://github.com/aws-solutions/content-localization-on-aws
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:39:06+00:00

## Project purpose

Welcome to the Content Localization on AWS project! This project will help you extend the reach of your VOD content by quickly and efficiently creating accurate multi-language subtitles using AWS AI Services. You can make manual corrections to the automatically created subtitles and use advanced AWS AI Service customization features to improve the results of the automation for your content domain. Content Localization is built on Media Insights on AWS, a framework that helps accelerate the development of serverless applications that process video, images, audio, and text with artificial intelligence services and multimedia services on AWS.

## Why this project is used

Automatically generate multi-language subtitles using AWS  AI/ML services. Machine generated subtitles can be edited to improve accuracy and downstream tracks will automatically be regenerated based on the edits. Built on Media Insights Engine (https://github.com/awslabs/aws-media-insights-engine)

## Core features

- Search for filenames containing the suffix ".mp4" with, *.mp4 or filename:*.mp4: Search for filenames containing the suffix ".mp4" with, *.mp4 or filename:*.mp4
  - Evidence: README.md#Search Capabilities:
- Since Content Moderation returns a "Violence" label when it detects violence in a video, you can search for any video containing violence simply with: Violence: Since Content Moderation returns a "Violence" label when it detects violence in a video, you can search for any video containing violence simply with: Violence
  - Evidence: README.md#Search Capabilities:
- Search for videos containing violence with a 80% confidence threshold: Violence AND Confidence:>80: Search for videos containing violence with a 80% confidence threshold: Violence AND Confidence:>80
  - Evidence: README.md#Search Capabilities:
- The previous queries may match videos whose transcript contains the word "Violence". You can restrict your search to only Content Moderation results, like this:: The previous queries may match videos whose transcript contains the word "Violence". You can restrict your search to only Content Moderation results, like this: Operator:content_moderation AND (Name:Violence AND Confidence:>80)
  - Evidence: README.md#Search Capabilities:
- To search for Violence results in Content Moderation and guns or weapons identified by Label Detection, try this: (Operator:content_moderation AND Name:Violence: To search for Violence results in Content Moderation and guns or weapons identified by Label Detection, try this: (Operator:content_moderation AND Name:Violence AND Confidence:>80) OR (Operator:label_detection AND (Name:Gun OR Name:Weapon))
  - Evidence: README.md#Search Capabilities:
- You can search for phrases in Comprehend results like this, PhraseText:"some deep water" AND Confidence:>80: You can search for phrases in Comprehend results like this, PhraseText:"some deep water" AND Confidence:>80
  - Evidence: README.md#Search Capabilities:
- To see the full set of attributes that you can search for, click the Analytics menu item and search for "*" in the Discover tab of Kibana.: To see the full set of attributes that you can search for, click the Analytics menu item and search for "*" in the Discover tab of Kibana.
  - Evidence: README.md#Search Capabilities:

## Technology stack

- Languages: Vue, Python, Shell, JavaScript, CSS, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @eslint/eslintrc, @vitejs/plugin-vue, @vue/compat, @vue/compiler-sfc, aws-amplify, aws-amplify-vue, axios, bootstrap, bootstrap-vue, boto3, botocore, chart.js, diff, dropzone, elasticsearch, eslint, eslint-plugin-vue, jquery, jwt-decode, latest-version, lodash, number-to-words, pytest, pytest-cov, requests, requests-aws4auth, selenium, unplugin-vue-components, urllib3, video.js, videojs-flash, videojs-hotkeys, videojs-markers, vite, vue, vue-highlightjs, vue-router, vuex, vuex-persistedstate, wavesurfer.js, webdriver-manager, webpack-subresource-integrity
- Build/package tools: npm-compatible manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: source/website/src/store/index.js, source/anonymized-data-logger/lib/cfnresponse.py, source/anonymized-data-logger/lib/metrics.py, source/website/src/main.js

## Setup and usage

No setup information established.

## Limitations and caveats

- Known Issues: Visit the Issue page in this repository for known issues and feature requests.

## Evidence and provenance

- README: https://github.com/aws-solutions/content-localization-on-aws/blob/main/README.md
- README SHA: db2bd42823297de1ad8267264c314dc981274b7b
- Manifests: source/anonymized-data-logger/requirements.txt, source/consumer/requirements.txt, source/helper/requirements.txt, source/website/package.json, test/e2e/requirements.txt, test/unit/requirements.txt
- Sampled source files: source/website/src/store/index.js, source/anonymized-data-logger/lib/cfnresponse.py, source/anonymized-data-logger/lib/metrics.py, source/website/src/main.js
- Git tree state: captured
- Evidence fingerprint: 8591d4012a2946cede9102e26ad572a6c76c6108b38786d37a5a2141c74aa150

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
