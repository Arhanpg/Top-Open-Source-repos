# GoogleCloudPlatform/python-runtime

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/python-runtime](https://github.com/GoogleCloudPlatform/python-runtime)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/python-runtime/blob/master/README.md)
- README blob SHA: 51e70cd85c0778d208a2a61d84c9ff0a6a1f696d
- README bytes captured: 2772
- README truncated at capture limit: False
- Repository ID: 20423832
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

gcr.io/google_appengine/python - Docker images for python

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T05:31:31+00:00

### Short excerpt (up to 300 words)

> ADD requirements.txt /app/requirements.txt RUN

### README headings

- Google Cloud Platform - Python Runtime Docker Image
- App Engine
- Kubernetes Engine & other Docker hosts.
- Building the image
- Contributing changes
- Licensing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Technology and requirements: dependencies into the virtualenv.

> ADD requirements.txt /app/requirements.txt RUN

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 75,149 |
| Shell | 31,895 |
| Dockerfile | 176 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- builder/gen-dockerfile/requirements.txt (capture: captured) — dependency clues: PyYAML
- runtime-image/resources/requirements.txt (capture: captured) — dependency clues: pip, setuptools, wheel
- tests/deploy_check/requirements.txt (capture: captured) — dependency clues: Flask, gunicorn
- tests/eventlet/requirements.txt (capture: captured) — dependency clues: Flask, Jinja2, MarkupSafe, Werkzeug, click, enum-compat, eventlet, greenlet, gunicorn, itsdangerous
- tests/integration/requirements.txt (capture: captured) — dependency clues: Flask, google-cloud-error-reporting, google-cloud-logging, google-cloud-monitoring, gunicorn, protobuf, requests, retrying, six
- tests/python2-libraries/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 219
- Forks at capture: 112
- Last updated: 2026-11-23T03:24:10Z
- Last pushed: 2026-01-23T18:40:39Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/python-runtime)
- [README](https://github.com/GoogleCloudPlatform/python-runtime/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/python-runtime/issues)
- [Releases](https://github.com/GoogleCloudPlatform/python-runtime/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
