# VibeVoice

- **Company:** Microsoft
- **Repository:** https://github.com/microsoft/VibeVoice
- **README:** https://github.com/microsoft/VibeVoice/blob/main/README.md
- **Default branch:** main
- **Audit status:** README reviewed
- **README blob SHA at inspection:** 57496590b0380d521cdddeff613d776466a86381

## What it does

An open-source voice-AI project covering text-to-speech and speech recognition, including long-form and streaming transcription.

## Features documented by the upstream README

- VibeVoice-ASR supports long-form audio transcription and structured who/when/what output.
- README documents multilingual ASR, fine-tuning code and vLLM inference support.
- Streaming ASR can emit transcriptions while speech arrives and supports customized hotwords.
- Links to model releases, demos and technical reports.

## Technology stack

Speech / audio ML; README explicitly references Hugging Face Transformers integration and vLLM inference. Exact framework and language breakdown requires manifest review.

## Notes and limitations

Language-count claims differ across the README's model announcements; consult each linked model's documentation for a specific model/version.

## Evidence

This summary is based on the upstream README linked above. Repository manifests, source code, CI workflows and release artifacts were not exhaustively audited in this pass; therefore the technology stack is limited to what the README explicitly supports.
