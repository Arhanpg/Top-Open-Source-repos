# google/adapt-googleanalytics

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/adapt-googleanalytics](https://github.com/google/adapt-googleanalytics)
- Default branch: master
- README: [Open upstream README](https://github.com/google/adapt-googleanalytics/blob/master/README.md)
- README blob SHA: c8046a2ebb3cea6f32eb988d1805dcf8653ce488
- Repository ID: 77634620
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:24:42+00:00

### Short excerpt (up to 100 words)

> This is not an official Google product. This is a simple Adapt extension that implements Google Analytics upon post render of pageView, which is triggered when a page's view has rendered. Be sure to include the Analytics library and Autotrack in core > js > scriptLoader.js. Example: scripLoader.js: function setupRequireJS() { requirejs.config({ map: { ... }, paths: { ... analytics: 'https://www.google-analytics.com/analytics', autotrack: 'libraries/autotrack' } Use Autotrack semantics in component-level .hbs files for tracking events such as mouseover and clicks. Example: `<div class="graphic-inner component-inner" role="region" aria-label="{{_globals._components._graphic.ariaRegion}}" ga-on="mouseover" ga-event-category="Graphic Component" ga-event-action="Mouseover" ga-event-label="{{displayTitle}}">` Video tracking is already available through the MediaElement library. Add

### README headings

- adapt-googleanalytics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 2,136 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 8
- Forks at capture: 5
- Last updated: 2026-07-21T08:44:06Z
- Last pushed: 2017-01-04T19:45:02Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/adapt-googleanalytics)
- [README](https://github.com/google/adapt-googleanalytics/blob/master/README.md)
- [Issues](https://github.com/google/adapt-googleanalytics/issues)
- [Releases](https://github.com/google/adapt-googleanalytics/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
