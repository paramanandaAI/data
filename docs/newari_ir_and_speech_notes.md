# Newari (Nepal Bhasa) Information Retrieval & Multimodal Speech Notes

This document provides technical specs and benchmark notes for **Newari (Nepal Bhasa)** Information Retrieval and low-resource multimodal ASR integration across the Paramananda ecosystem.

---

## 📚 1. Newari Information Retrieval Benchmark (`newari_retrieval`)

- **Language**: Newari / Nepal Bhasa (Devanagari script + Roman script transliteration)
- **Task**: Information Retrieval, Passage Ranking, Document Retrieval
- **Volume**: 
  - `corpus_trec.csv`: **1,638,192 Documents** (`DocID, filename, text`)
  - `newari_data_roman.tsv`: **3,276,390 Sentences** (Roman script variant)
  - `muril.json` & `tfidf.json`: **1,000 Benchmark Queries** with precomputed top-10 document ID baselines

### Benchmark Baselines
- **MuRIL Dense Retrieval**: Multilingual Representations for Indic Languages (MuRIL) zero-shot passage retrieval.
- **TF-IDF Sparse Retrieval**: Lexical term matching baseline with 100 custom Newari stopwords (`stopwords.txt`).

---

## 🎙️ 2. Native ASR & Gemma 4 Multimodal Speech Integration

- **Technical Guide**: [gemma4_asr_and_agentic_guide.md](gemma4_asr_and_agentic_guide.md)

- **Modality**: Native Audio Speech Recognition (16 kHz Mono PCM WAV)
- **Key Architectures**:
  - **Nwacha Muna ASR**: Low-resource Sino-Tibetan Newari speech corpus (Kathmandu University / ILPRL).
  - **Gemma 4 E2B / E4B Audio Integration**: Encoder-free Per-Layer Embedding (PLE) audio spectrogram processing for Nepali and Newari Devanagari speech recognition.
