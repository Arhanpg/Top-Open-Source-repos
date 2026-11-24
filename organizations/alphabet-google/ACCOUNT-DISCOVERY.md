# Alphabet / Google — GitHub account discovery register

## Primary account

| Account | Evidence | Scope |
|---|---|---|
| [google](https://github.com/google) | Official Google Open Source organization reference and verified primary account | Core Google open-source account; other product areas publish through separate accounts |

## Additional Google Cloud project account

| Account | Official documentation evidence | Example repositories |
|---|---|---|
| [GoogleCloudPlatform](https://github.com/GoogleCloudPlatform) | Google Cloud tutorials instruct developers to clone repositories under this account; its profile links cloud.google.com | [python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples), [golang-samples](https://github.com/GoogleCloudPlatform/golang-samples), [nodejs-docs-samples](https://github.com/GoogleCloudPlatform/nodejs-docs-samples), [java-docs-samples](https://github.com/GoogleCloudPlatform/java-docs-samples), [dotnet-docs-samples](https://github.com/GoogleCloudPlatform/dotnet-docs-samples) |

Source examples:
- [Google Cloud Run tutorial — system packages](https://docs.cloud.google.com/run/docs/tutorials/system-packages) directly instructs users to clone the Node.js, Python, Go and Java sample repositories.
- [Cloud Endpoints support guide](https://docs.cloud.google.com/endpoints/docs/grpc/getting-support) points users to the Node, Java, Python, Go and Ruby samples under GoogleCloudPlatform.

The GitHub profile lists roughly 1,500 public repositories at the time of discovery. The `official-project-linked` classification means Google Cloud documentation points to projects in this account; it does not imply all repositories in the account are owned or authored by Google.

## Attribution and completeness

- The primary `google` account and `GoogleCloudPlatform` account are inventoried separately.
- Public documentation links establish a project relationship for the examples, not blanket legal ownership of every repository.
- Other Google product organizations should be added only when an official Google source identifies the account.


## Additional Gemini API project account — 24 November 2026

The Google Cloud [Generative AI on Google Cloud samples repository](https://github.com/GoogleCloudPlatform/generative-ai) directly links the [Gemini API Cookbook](https://github.com/google-gemini/cookbook) under the separate `google-gemini` GitHub account.

| Account | Linked project | Evidence | Mapping status |
|---|---|---|---|
| [google-gemini](https://github.com/google-gemini) | Gemini API Cookbook | GoogleCloudPlatform/generative-ai README links google-gemini/cookbook; the repository is public | official-project-linked |

This records an explicit project association, not a claim that every repository under `google-gemini` is owned or authored by Google. Its public repository inventory is pending independent pagination.
