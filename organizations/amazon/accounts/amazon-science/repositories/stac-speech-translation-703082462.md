# amazon-science/stac-speech-translation

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/stac-speech-translation](https://github.com/amazon-science/stac-speech-translation)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/stac-speech-translation/blob/main/README.md)
- README blob SHA: b265180944437e141ac2cb5aa535a0d7fd90f06d
- README bytes captured: 15057
- README truncated at capture limit: False
- Repository ID: 703082462
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:07:45+00:00

### Short excerpt (up to 300 words)

> pip install -r ../stac-st/requeriments_file.txt pip install -r ../stac-st/requeriments_file.txt See CONTRIBUTING for more

### README headings

- Speaker-Turn Aware Conversational Speech Translation (STAC-ST)
- Citation
- Setup your environment
- 1. Clone STAC-ST repository.
- 2. Create conda environment with PYTORCH 2.0 and SpeechBrain
- 3. Install SpeechBrain's dependencies:
- then install SpeechBrain
- 4. Important!!
- local_rank = None
- if "local_rank" in run_opts:
- local_rank = run_opts["local_rank"]
- else:
- if "LOCAL_RANK" in os.environ and os.environ["LOCAL_RANK"] != "":
- local_rank = int(os.environ["LOCAL_RANK"])
- run_opts["local_rank"] = local_rank %<------------- ADD THIS LINE --|
- 5. Additional modules
- Prepare the datasets
- Fisher-CALLHOME
- 1. Download the data
- 2. Preparation scripts
- first, open each file and set:
- ORIGINAL_DATA=/path/to/fisher/folder/
- Open the script run_shas_segmentation.sh and set these two
- then
- CommonVoice (CV)
- YOU NEED TO ENTER THESE PATHS!
- data_folder="/path/to/folder/datasets/common_voice_13/cv-corpus-13.0-2023-03-09"
- save_folder="/path/to/folder/datasets/common_voice_13/data"
- then run:
- CoVoST2

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: 3. Install SpeechBrain's dependencies:

> pip install -r ../stac-st/requeriments_file.txt

### Technology and requirements: 3. Install SpeechBrain's dependencies:

> pip install -r ../stac-st/requeriments_file.txt

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 347,477 |
| Shell | 61,409 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 12
- Forks at capture: 2
- Last updated: 2024-04-25T12:11:56Z
- Last pushed: 2024-03-06T16:37:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/stac-speech-translation)
- [README](https://github.com/amazon-science/stac-speech-translation/blob/main/README.md)
- [Issues](https://github.com/amazon-science/stac-speech-translation/issues)
- [Releases](https://github.com/amazon-science/stac-speech-translation/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
