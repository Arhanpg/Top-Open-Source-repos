# GoogleCloudPlatform/EZ-WSI-DICOMweb

- Company: Alphabet (Google)
- Account: GoogleCloudPlatform
- Repository: https://github.com/GoogleCloudPlatform/EZ-WSI-DICOMweb
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:45:09+00:00

## Project purpose

EZ WSI DicomWeb is a python library that provides the ability to effortlessly extract an image patch from a pathology DICOM whole slide image (WSI) stored in a cloud DICOM store. This functionality is useful for different pathology workflows, especially those leveraging AI. EZ-WSI provides interfaces to enable embeddings to be easily generated from Digital Pathology patches and images.

## Why this project is used

EZ WSI DicomWeb is a python library that provides the ability to effortlessly extract an image patch from a pathology DICOM whole slide image (WSI) stored in a cloud DICOM store. This functionality is useful for different pathology workflows, especially those leveraging AI. EZ-WSI provides interfaces to enable embeddings to be easily generated from Digital Pathology patches and images.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Jupyter Notebook, Starlark, Dockerfile, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: absl-py, cachetools, certifi, charset-normalizer, dataclasses-json, google-api-core, google-auth, google-auth-httplib2, google-cloud-core, google-cloud-storage, google-crc32c, google-resumable-media, googleapis-common-protos, httplib2, idna, imagecodecs, marshmallow, mypy-extensions, numpy, opencv-python-headless, packaging, pillow, proto-plus, protobuf, psutil, pyasn1, pyasn1-modules, pydicom, pyparsing, requests, requests-mock, requests-toolbelt, retrying, rsa, six, typing-extensions, typing-inspect, urllib3
- Build/package tools: Docker build configuration, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: ez_wsi_dicomweb/__init__.py, ez_wsi_dicomweb/base_patch.py, ez_wsi_dicomweb/credential_factory.py, ez_wsi_dicomweb/credential_factory_test.py

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/GoogleCloudPlatform/EZ-WSI-DICOMweb/blob/main/README.md
- README SHA: f767b2068ea42131e6cfef28daa85fd4c7984a2d
- Manifests: setup.py, ez_wsi_dicomweb/requirements.txt, test_docker/Dockerfile
- Sampled source files: ez_wsi_dicomweb/base_patch.py, ez_wsi_dicomweb/credential_factory.py, ez_wsi_dicomweb/credential_factory_test.py
- Git tree state: captured
- Evidence fingerprint: 31885fdcb5d625eb4d49453a87b4b67229a4e28c9e49e2c0a4a427954f22e76f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
