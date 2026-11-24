# google/ads-placement-excluder

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/ads-placement-excluder](https://github.com/google/ads-placement-excluder)
- Default branch: main
- README: [Open upstream README](https://github.com/google/ads-placement-excluder/blob/main/README.md)
- README blob SHA: 4f3eb2f37e00eac785f90d57ab906e9d0975abd4
- Repository ID: 527620570
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:34:25+00:00

### Short excerpt (up to 100 words)

> It is manual and challenging to detect YouTube channel placements which might be spam (low performance with high cost), and exclude them from future advertising. Google Ads does not currently provide enough granularity to identify all spam channels. Ads Placement Excluder allows an advertiser, to define what their interpretation of a spam channel is, and it will leverage the Google Ads & YouTube APIs to automate identifying these placements, and exclude them from future advertising. See architecture.md. The solution provides a DataStudio dashboard to monitor the solution. See See deployment.md for information on how to deploy the solution and get

### README headings

- Ads Placement Excluder
- Architecture
- Reporting
- Get Started
- Disclaimers

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 60,053 |
| HCL | 14,160 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/google_ads_accounts/requirements.txt (capture: captured) — dependency clues: Flask, google-api-python-client, google-auth-httplib2, google-auth-oauthlib, google-cloud-pubsub, jsonschema, pydata-google-auth
- src/google_ads_excluder/requirements.txt (capture: captured) — dependency clues: google-ads, google-api-python-client, google-auth-httplib2, google-auth-oauthlib, google-cloud-bigquery, google-cloud-pubsub, google-cloud-storage, jsonschema, pandas
- src/google_ads_report/requirements.txt (capture: captured) — dependency clues: google-ads, google-cloud-pubsub, google-cloud-storage, jsonschema, pandas
- src/youtube_channel/requirements.txt (capture: captured) — dependency clues: google-api-python-client, google-auth, google-auth-httplib2, google-auth-oauthlib, google-cloud-bigquery, google-cloud-pubsub, google-cloud-storage, google-cloud-translate, jsonschema, numpy, pandas

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 10
- Forks at capture: 2
- Last updated: 2026-07-21T09:27:41Z
- Last pushed: 2023-08-24T14:32:06Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/ads-placement-excluder)
- [README](https://github.com/google/ads-placement-excluder/blob/main/README.md)
- [Issues](https://github.com/google/ads-placement-excluder/issues)
- [Releases](https://github.com/google/ads-placement-excluder/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
