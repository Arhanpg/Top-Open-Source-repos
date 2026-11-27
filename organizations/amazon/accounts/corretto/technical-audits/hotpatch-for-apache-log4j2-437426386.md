# corretto/hotpatch-for-apache-log4j2

- Company: Amazon
- Account: corretto
- Repository: https://github.com/corretto/hotpatch-for-apache-log4j2
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:39:37+00:00

## Project purpose

This is a tool which injects a Java agent into a running JVM process. The agent will attempt to patch the lookup() method of all loaded org.apache.logging.log4j.core.lookup.JndiLookup instances to unconditionally return the string "Patched JndiLookup::lookup()". It is designed to address the CVE-2021-44228 remote code execution vulnerability in Log4j without restarting the Java process. This tool will also address CVE-2021-45046.

## Why this project is used

An  agent to hotpatch the log4j RCE from CVE-2021-44228.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, Shell, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: hotpatch-for-apache-log4j2, jdk.tools, maven-gpg-plugin, maven-jar-plugin, nexus-staging-maven-plugin
- Build/package tools: Gradle build file, Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/main/java/com/amazon/corretto/hotpatch/org/objectweb/asm/AnnotationVisitor.java, src/main/java/com/amazon/corretto/hotpatch/org/objectweb/asm/AnnotationWriter.java, src/main/java/com/amazon/corretto/hotpatch/org/objectweb/asm/Attribute.java, src/main/java/com/amazon/corretto/hotpatch/org/objectweb/asm/ByteVector.java

## Setup and usage

No setup information established.

## Limitations and caveats

- Known issues: If you get an error like:
- Known issues: Exception in thread "main" com.sun.tools.attach.AttachNotSupportedException: The VM does not support the attach mechanism
- Known issues: at jdk.attach/sun.tools.attach.HotSpotAttachProvider.testAttachable(HotSpotAttachProvider.java:153)
- Known issues: at jdk.attach/sun.tools.attach.AttachProviderImpl.attachVirtualMachine(AttachProviderImpl.java:56)
- Known issues: at jdk.attach/com.sun.tools.attach.VirtualMachine.attach(VirtualMachine.java:207)
- Known issues: at Log4jHotPatch.loadInstrumentationAgent(Log4jHotPatch.java:115)
- Known issues: at Log4jHotPatch.main(Log4jHotPatch.java:139)
- Known issues: this means that your JVM is refusing any kind of help because it is running with -XX:+DisableAttachMechanism.

## Evidence and provenance

- README: https://github.com/corretto/hotpatch-for-apache-log4j2/blob/main/README.md
- README SHA: 1c407d028047e6e7910ddb37976896fcc6840a81
- Manifests: build.gradle, pom.xml
- Sampled source files: src/main/java/com/amazon/corretto/hotpatch/org/objectweb/asm/AnnotationVisitor.java, src/main/java/com/amazon/corretto/hotpatch/org/objectweb/asm/AnnotationWriter.java, src/main/java/com/amazon/corretto/hotpatch/org/objectweb/asm/Attribute.java, src/main/java/com/amazon/corretto/hotpatch/org/objectweb/asm/ByteVector.java
- Git tree state: captured
- Evidence fingerprint: 23aa39a212ca313fc7d96b68917f112f1b938176e86787b31183a134c92c2a4d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
