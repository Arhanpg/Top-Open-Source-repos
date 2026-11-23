# VibeVoice

<sub>Company: Microsoft · Repository: [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

VibeVoice is a family of open-source voice-AI models covering text-to-speech (TTS) and automatic speech recognition (ASR). The current repository README gives substantial attention to long-form and streaming ASR, while also documenting historical and released TTS model variants.

**Problem it addresses:** speech systems often need more than a plain sequence of recognized words. Long recordings require speaker consistency and timestamps, while streaming systems need to emit useful text before an entire recording has finished. VibeVoice explores model architectures and inference workflows for these voice tasks.

## Architecture described by the project

The README highlights continuous acoustic and semantic speech tokenizers operating at a 7.5 Hz frame rate. It describes a next-token diffusion framework in which an LLM models textual context and dialogue flow, while a diffusion head generates acoustic detail.

This is the high-level architecture statement in the repository README. It should not be read as a complete model card or a substitute for the technical report and model-specific documentation.

## Model and capability overview

| Model / line | README description |
|---|---|
| VibeVoice-ASR | Long-form speech recognition, with structured speaker, timestamp and content output |
| VibeVoice-ASR-Streaming | Streaming transcription that emits text while audio arrives |
| VibeVoice-ASR-BitNet | CPU-oriented inference engine/model path linked to BitNet quantization work |
| VibeVoice-Realtime-0.5B | Real-time TTS model with streaming text input and multilingual experimental speakers |
| VibeVoice-TTS family | The README lists model releases and historical research announcements; current code availability must be checked carefully |

### Long-form ASR

The README states that VibeVoice-ASR is designed for up to 60 minutes of audio in a single pass, with a structured transcription representation describing **who** spoke, **when** they spoke and **what** was said. It also documents user-customized hotwords for names, domain terms or other context.

This combination brings together speech recognition, speaker attribution and timestamping in one output workflow.

### Streaming ASR

The streaming variant emits transcription chunks while audio is still arriving, rather than waiting for the recording to finish. The README links streaming and vLLM serving documentation, along with a model page and demo.

### Multilingual support and adaptation

The README advertises multilingual ASR and links a model-specific supported-language list. It also links fine-tuning material and model-specific documentation. Language coverage varies by model variant, so use the relevant model card rather than applying one language count to the entire VibeVoice family.

## Technology profile

| Area | README-supported details |
|---|---|
| Domain | Speech synthesis and speech recognition |
| Model components | LLM-based textual context, acoustic/semantic tokenizers and diffusion head |
| Tokenizer frame rate | 7.5 Hz, as described by the README |
| Model distribution | Hugging Face model pages / collections |
| Inference integrations | vLLM is explicitly referenced for ASR |
| Demonstrations | Project page, ASR playground and Colab notebook |
| Training resources | ASR fine-tuning code is linked |

The README also identifies VibeASR.cpp as a CPU inference engine for a quantized ASR path. That is a linked companion repository, not source code contained in this repository.

## Repository lifecycle and responsible-use note

The README's news section records that Microsoft removed the VibeVoice-TTS code from this repository on 5 September 2025 after discovering uses inconsistent with the stated research intent. Later README content still points to TTS model releases and documentation, so distinguish between a model being listed or available as a separate artifact and the code currently present in this repository.

Before building on a model, verify its current model card, license, usage restrictions, intended-use guidance and supported deployment path. Voice cloning and speech-generation use cases require particular attention to consent and misuse prevention.

## Getting started

The repository links the project page, Hugging Face collection, Colab examples and dedicated model documentation. For ASR, begin with the [ASR documentation](https://github.com/microsoft/VibeVoice/blob/main/docs/vibevoice-asr.md); for streaming, use the [streaming ASR guide](https://github.com/microsoft/VibeVoice/blob/main/docs/vibevoice-asr-streaming.md). Do not assume that every model family member shares the same environment or hardware requirements.

## Potential applications

- Transcribing long recordings while retaining speaker and timestamp information.
- Building streaming speech-to-text interfaces.
- Researching multilingual speech recognition.
- Evaluating speaker-aware transcription on domain-specific recordings.
- Studying real-time or long-form speech generation models where model access and usage terms permit it.

## Upstream references

- [Repository](https://github.com/microsoft/VibeVoice)
- [Primary README](https://github.com/microsoft/VibeVoice/blob/main/README.md)
- [Project page](https://microsoft.github.io/VibeVoice)
- [Hugging Face collection](https://huggingface.co/collections/microsoft/vibevoice-68a2ef24a875c44be47b034f)
- [ASR documentation](https://github.com/microsoft/VibeVoice/blob/main/docs/vibevoice-asr.md)
- [Streaming ASR documentation](https://github.com/microsoft/VibeVoice/blob/main/docs/vibevoice-asr-streaming.md)
- [VibeASR.cpp](https://github.com/microsoft/VibeASR.cpp)

**Evidence note:** README blob inspected: `57496590b0380d521cdddeff613d776466a86381`.
