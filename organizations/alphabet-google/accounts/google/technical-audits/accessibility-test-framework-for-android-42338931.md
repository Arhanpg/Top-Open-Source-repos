# google/Accessibility-Test-Framework-for-Android

- Company: Alphabet (Google)
- Account: google
- Repository: https://github.com/google/Accessibility-Test-Framework-for-Android
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:19:29+00:00

## Project purpose

To help people with disabilities access Android apps, developers of those apps need to consider how their apps will be presented to accessibility services. Some good practices can be checked by automated tools, such as if a View has a contentDescription. Other rules require human judgment, such as whether or not a contentDescription makes sense to all users.

## Why this project is used

Accessibility checks for automated Android testing

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle build file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/main/java/com/google/android/apps/common/testing/accessibility/framework/AccessibilityCheck.java, src/main/java/com/google/android/apps/common/testing/accessibility/framework/AccessibilityCheckPreset.java, src/main/java/com/google/android/apps/common/testing/accessibility/framework/AccessibilityCheckPresetAndroid.java, src/main/java/com/google/android/apps/common/testing/accessibility/framework/AccessibilityCheckResult.java

## Setup and usage

- Sample Usage: Given a view, the following code runs all accessibility checks on all views in
- Sample Usage: the hierarchy rooted at that view and throws an exception if any errors are
- Sample Usage: ImmutableSet checks =
- Sample Usage: AccessibilityCheckPreset.getAccessibilityHierarchyChecksForPreset(
- Sample Usage: AccessibilityCheckPreset.LATEST);
- Sample Usage: AccessibilityHierarchyAndroid hierarchy = AccessibilityHierarchyAndroid.newBuilder(view).build();
- Sample Usage: List results = new ArrayList<>();
- Sample Usage: for (AccessibilityHierarchyCheck check : checks) {

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/google/Accessibility-Test-Framework-for-Android/blob/master/README.md
- README SHA: 90a2a886cca0dddf08da677487919b6f8ec2ea1b
- Manifests: build.gradle
- Sampled source files: src/main/java/com/google/android/apps/common/testing/accessibility/framework/AccessibilityCheck.java, src/main/java/com/google/android/apps/common/testing/accessibility/framework/AccessibilityCheckPreset.java, src/main/java/com/google/android/apps/common/testing/accessibility/framework/AccessibilityCheckPresetAndroid.java, src/main/java/com/google/android/apps/common/testing/accessibility/framework/AccessibilityCheckResult.java
- Git tree state: captured
- Evidence fingerprint: e36b21ac8a9e8f7e51523110087b06082a3c0671d28e37f87cc2e2e84bb67f3e

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
