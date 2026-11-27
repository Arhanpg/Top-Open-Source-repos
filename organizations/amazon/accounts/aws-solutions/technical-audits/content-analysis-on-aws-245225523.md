# aws-solutions/content-analysis-on-aws

- Company: Amazon
- Account: aws-solutions
- Repository: https://github.com/aws-solutions/content-analysis-on-aws
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:32:42+00:00

## Project purpose

**As of August 30, 2023, this AWS Solution is no longer available. Existing deployments will continue to run. If you have deployed Content Analysis on AWS via cloning GitHub open source code, you may continue to use the solution. The functionality provided by Content Analysis on AWS will be superseded with functionality in Media2Cloud on AWS and Content Localization on AWS. We encourage you to explore these solutions.**

## Why this project is used

As of August 30, 2023, this AWS Solution is no longer available. Existing deployments will continue to run. The functionality provided by Content Analysis on AWS will be superseded with functionality in Media2Cloud on AWS and Content Localization on AWS. We encourage you to explore these solutions.

## Core features

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

- Languages: Vue, Python, JavaScript, Shell, HTML, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: @vue/cli-plugin-babel, @vue/cli-plugin-eslint, @vue/cli-plugin-pwa, @vue/cli-service, aws-amplify, aws-amplify-vue, axios, babel-eslint, bad-words, bootstrap, bootstrap-vue, chart.js, core-js, dropzone, elasticsearch, eslint, eslint-plugin-vue, jquery, jwt-decode, lodash, register-service-worker, requests, requests-aws4auth, video.js, videojs-flash, videojs-hotkeys, videojs-markers, vue, vue-highlightjs, vue-router, vue-template-compiler, vue-video-player, vuex, vuex-persistedstate, webpack-subresource-integrity
- Build/package tools: Docker build configuration, npm-compatible manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: source/website/src/store/index.js, source/anonymous-data-logger/lib/cfnresponse.py, source/anonymous-data-logger/lib/metrics.py, source/website/src/main.js

## Setup and usage

- INSTALLATION: Once the Cloud Formation stack has been created, open the URL shown in the ContentAnalyisSolution output of the base stack. You can also get this URL with the following AWS CLI command:
- INSTALLATION: aws cloudformation --region $REGION describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='ContentAnalyisSolution'].OutputValue" --output text
- INSTALLATION: For more installation options, see the Advanced Installation section.

## Limitations and caveats

- Known Issues: Visit the Issue page in this repository for known issues and feature requests.

## Evidence and provenance

- README: https://github.com/aws-solutions/content-analysis-on-aws/blob/main/README.md
- README SHA: 531b6728b7dbb197d49b8f444ecb69e2b9653986
- Manifests: source/anonymous-data-logger/requirements.txt, source/consumer/requirements.txt, source/website/package.json, source/website/test/Dockerfile
- Sampled source files: source/website/src/store/index.js, source/anonymous-data-logger/lib/cfnresponse.py, source/anonymous-data-logger/lib/metrics.py, source/website/src/main.js
- Git tree state: captured
- Evidence fingerprint: 0a17bfc582acd6525aa22a820b67b6bc96ea5bd6436766706672b6661684126a

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
