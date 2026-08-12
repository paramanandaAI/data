> Source: `sources/multimodal/asr/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Automatic Speech Recognition (ASR): Task Guide & Notes

## 🇳🇵 Phonetic & Acoustic Nuances
1. **Aspiration & Voicing Contrasts:** Four-way stop consonant distinction:
   - Unvoiced Unaspirated (*क - /k/*), Unvoiced Aspirated (*ख - /kʰ/*), Voiced Unaspirated (*ग - /ɡ/*), Voiced Aspirated (*घ - /ɡʱ/*).
2. **Nasalization (अनुनासिकता):** Distinct acoustic signature between Chandrabindu (`ँ` - true vowel nasalization) and Anusvara (`ं` - homorganic nasal consonant).

---

## 🤖 Modern End-to-End ASR (Whisper & Gemma 4 Multimodal)
- **Whisper Fine-Tuning (Nepali / Newari):**
  - Fine-tune decoder using LoRA with Nepali subword vocabulary target.
- **Gemma 4 Multimodal Audio:**
  - Audio encoder feeding directly into Gemma 4 autoregressive decoder for joint transcription and translation.

## ⚙️ Related Speech & Audio Frameworks

| Repository | Focus |
|---|---|
| [`Delta-ML/delta`](https://github.com/Delta-ML/delta) | Deep learning based NLP and speech processing platform |
| [`readbeyond/aeneas`](https://github.com/readbeyond/aeneas) | Python/C library for forced audio-text alignment |
| [`google/voice-builder`](https://github.com/google/voice-builder) | Open-source text-to-speech (TTS) voice building tool |
| [`MycroftAI/mycroft-core`](https://github.com/MycroftAI/mycroft-core) | Mycroft AI platform — open-source virtual assistant |
| [`tensorflow/lingvo`](https://github.com/tensorflow/lingvo) | TensorFlow-based sequence modeling for speech |
| [`openvinotoolkit/openvino`](https://github.com/openvinotoolkit/openvino) | Open source toolkit for optimizing and deploying AI inference |
| [`milvus-io/bootcamp`](https://github.com/milvus-io/bootcamp) | Unstructured data handling including audio search |
