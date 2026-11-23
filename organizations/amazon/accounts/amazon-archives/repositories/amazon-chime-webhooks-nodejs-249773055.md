# amazon-archives/amazon-chime-webhooks-nodejs

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/amazon-chime-webhooks-nodejs](https://github.com/amazon-archives/amazon-chime-webhooks-nodejs)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/amazon-chime-webhooks-nodejs/blob/master/README.md)
- README blob SHA: 5c1cb3b17ae7fc0d51f700ad568489685045cb7b
- Repository ID: 249773055
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Send Amazon Chime messages using webhooks.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:04:24+00:00

### Short excerpt (up to 100 words)

> Send Amazon Chime messages using webhooks. - Amazon Chime - Webhooks for Amazon Chime - Adding Webhooks to Chat Rooms const Chime = require('chime'); (async () => { try { await Chime.sendMessage('hello world', '<WEBHOOK_URL>'); } catch (err) { // do something with err } })(); - `url` `<string>` - Webhook URL - `options` `<object>` Overridden by `room.sendMessage()` options. - `markdown` `<boolean>` - Send message using markdown syntax. **Default:** `true` - Returns: `<Chime>` const room = new Chime('<WEBHOOK_URL>'); - `message` `<string>` - `url` `<string>` - Webhook URL - `options` `<object>` - `markdown` `<boolean>` - Send message using markdown syntax. **Default:** `true`

### README headings

- Amazon Chime
- Class: Chime
- new Chime(url[, options])
- Chime.sendMessage(message, url[, options])
- room.sendMessage(message[, options])
- Contributions
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 1,164 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: prettier

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 3
- Last updated: 2023-01-28T13:25:02Z
- Last pushed: 2020-04-28T21:46:54Z
- Topics: amazon-chime, nodejs

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/amazon-chime-webhooks-nodejs)
- [README](https://github.com/amazon-archives/amazon-chime-webhooks-nodejs/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/amazon-chime-webhooks-nodejs/issues)
- [Releases](https://github.com/amazon-archives/amazon-chime-webhooks-nodejs/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
