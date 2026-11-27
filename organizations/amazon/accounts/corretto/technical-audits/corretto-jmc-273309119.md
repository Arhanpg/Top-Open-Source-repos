# corretto/corretto-jmc

- Company: Amazon
- Account: corretto
- Repository: https://github.com/corretto/corretto-jmc
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:26:50+00:00

## Project purpose

*JMC for Corretto* is a build of JDK Mission Control (JMC) by the Corretto team. It tracks the latest stable JMC release with extra patches to support the usage of the JDK Flight Recorder feature in Corretto releases including:

## Why this project is used

A build of JDK Mission Control (JMC) by the Corretto team.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, HTML, XSLT, Shell, JavaScript, Batchfile, CSS
- Frameworks/libraries: Unknown / not established
- Dependency names: agent, asm, asm-commons, asm-util, build-helper-maven-plugin, buildnumber-maven-plugin, common, common.test, coverage, directory-maven-plugin, flatten-maven-plugin, flightrecorder, flightrecorder.rules, flightrecorder.rules.jdk, flightrecorder.serializers, flightrecorder.test, jacoco-maven-plugin, jdp, junit, maven-bundle-plugin, maven-deploy-plugin, maven-enforcer-plugin, maven-failsafe-plugin, maven-gpg-plugin, maven-jar-plugin, maven-javadoc-plugin, maven-resources-plugin, maven-shade-plugin, maven-source-plugin, maven-surefire-plugin, missioncontrol, missioncontrol.application, missioncontrol.core, missioncontrol.releng, nexus-staging-maven-plugin, org.openjdk.jmc.alert, org.openjdk.jmc.attach, org.openjdk.jmc.browser, org.openjdk.jmc.browser.attach, org.openjdk.jmc.browser.jdp, org.openjdk.jmc.browser.uitest, org.openjdk.jmc.commands, org.openjdk.jmc.console.jconsole, org.openjdk.jmc.console.jconsole.uitest, org.openjdk.jmc.console.pde, org.openjdk.jmc.console.persistence, org.openjdk.jmc.console.persistence.uitest, org.openjdk.jmc.console.twitter, org.openjdk.jmc.console.ui, org.openjdk.jmc.console.ui.diagnostic, org.openjdk.jmc.console.ui.mbeanbrowser, org.openjdk.jmc.console.ui.notification, org.openjdk.jmc.console.ui.subscriptions, org.openjdk.jmc.console.uitest, org.openjdk.jmc.docs, org.openjdk.jmc.feature.console, org.openjdk.jmc.feature.console.ui.subscriptions, org.openjdk.jmc.feature.core, org.openjdk.jmc.feature.flightrecorder, org.openjdk.jmc.feature.flightrecorder.ext.g1, org.openjdk.jmc.feature.flightrecorder.ext.jfx, org.openjdk.jmc.feature.flightrecorder.metadata, org.openjdk.jmc.feature.ide, org.openjdk.jmc.feature.ide.launch, org.openjdk.jmc.feature.jconsole, org.openjdk.jmc.feature.joverflow, org.openjdk.jmc.feature.license, org.openjdk.jmc.feature.pde, org.openjdk.jmc.feature.rcp, org.openjdk.jmc.feature.rcp.update, org.openjdk.jmc.feature.twitter, org.openjdk.jmc.flightrecorder.configuration, org.openjdk.jmc.flightrecorder.configuration.test, org.openjdk.jmc.flightrecorder.controlpanel.ui, org.openjdk.jmc.flightrecorder.controlpanel.ui.configuration, org.openjdk.jmc.flightrecorder.controlpanel.ui.configuration.test, org.openjdk.jmc.flightrecorder.controlpanel.ui.test, org.openjdk.jmc.flightrecorder.ext.g1, org.openjdk.jmc.flightrecorder.ext.jfx, org.openjdk.jmc.flightrecorder.ext.jfx.test, org.openjdk.jmc.flightrecorder.metadata, org.openjdk.jmc.flightrecorder.pde, org.openjdk.jmc.flightrecorder.rules.extensionprovider, org.openjdk.jmc.flightrecorder.ui, org.openjdk.jmc.flightrecorder.ui.test, org.openjdk.jmc.flightrecorder.uitest, org.openjdk.jmc.greychart, org.openjdk.jmc.greychart.test, org.openjdk.jmc.greychart.ui, org.openjdk.jmc.ide.jdt, org.openjdk.jmc.ide.launch, org.openjdk.jmc.ide.launch.test, org.openjdk.jmc.ide.ui, org.openjdk.jmc.joverflow, org.openjdk.jmc.joverflow.test, org.openjdk.jmc.joverflow.ui, org.openjdk.jmc.osgi.extension, org.openjdk.jmc.pde, org.openjdk.jmc.rcp.application, org.openjdk.jmc.rcp.application.uitest, org.openjdk.jmc.rcp.intro, org.openjdk.jmc.rcp.product, org.openjdk.jmc.rcp.product.feature, org.openjdk.jmc.rjmx, org.openjdk.jmc.rjmx.ext, org.openjdk.jmc.rjmx.services.jfr, org.openjdk.jmc.rjmx.services.jfr.test, org.openjdk.jmc.rjmx.test, org.openjdk.jmc.rjmx.ui, org.openjdk.jmc.test.jemmy, org.openjdk.jmc.ui, org.openjdk.jmc.ui.common, org.openjdk.jmc.ui.common.test, org.openjdk.jmc.ui.test, org.openjdk.jmc.updatesite.ide, org.openjdk.jmc.updatesite.rcp, platform-definition-2020-03, platform-definition-2020-06, platform-definition-2020-09, platform-definition-2020-12
- Build/package tools: Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/application/org.openjdk.jmc.joverflow/src/main/java/org/openjdk/jmc/joverflow/Main.java, src/application/org.openjdk.jmc.rcp.application/src/main/java/org/openjdk/jmc/rcp/application/Application.java, src/agent/src/main/java/org/openjdk/jmc/agent/Agent.java, src/agent/src/main/java/org/openjdk/jmc/agent/Attribute.java

## Setup and usage

No setup information established.

## Limitations and caveats

- Supported platforms: JMC for Corretto is supported on the following platforms:
- Supported platforms: * Linux (w/ GTK+ 3), x64
- Supported platforms: * macOS 10.10 or later, x64
- Supported platforms: * Windows 7 or later, x64
- Supported platforms: Please note that JMC is a client GUI tool for diagnosing and profiling JVM. It has the ability to connect to a remote-running Java process with JMX remote enabled and continuously monitor the JVM performance. It can also analyze the JFR profiling data generated by a different JVM on a distinct platform. Therefore, you can still leverage JMC feature
- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/corretto/corretto-jmc/blob/master/README.md
- README SHA: 209951148c2f9025a9b71bf6548c1648fc5d8f4f
- Manifests: src/pom.xml, src/agent/pom.xml, src/application/pom.xml, src/core/pom.xml, src/releng/pom.xml, src/application/coverage/pom.xml
- Sampled source files: src/application/org.openjdk.jmc.joverflow/src/main/java/org/openjdk/jmc/joverflow/Main.java, src/application/org.openjdk.jmc.rcp.application/src/main/java/org/openjdk/jmc/rcp/application/Application.java, src/agent/src/main/java/org/openjdk/jmc/agent/Agent.java, src/agent/src/main/java/org/openjdk/jmc/agent/Attribute.java
- Git tree state: captured
- Evidence fingerprint: 60bde93a6b0580344775f0bff9be3667c1c47caf9890a2740817c58ee4a9b5a9

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
