# Awesome Nepali Models Catalog

A curated catalog of open-weight machine learning models for Nepali NLP, Speech Processing, and Computational Linguistics.

---

## 1. Pretrained Encoder Models (BERT, RoBERTa, DeBERTa)

| Model Repository | Parameter Count | Core Task | Architecture |
| :--- | :--- | :--- | :--- |
| `Rajan/NepaliBERT` | 110M | Masked LM | BERT-base |
| `Sakonii/distilbert-base-nepali` | 67M | Masked LM | DistilBERT |
| `Sakonii/deberta-base-nepali` | 100M | Masked LM | DeBERTa-base |
| `IRIIS-RESEARCH/RoBERTa_Nepali_125M` | 125M | Masked LM | RoBERTa-base |
| `IRIIS-RESEARCH/BERT_Nepali_110M` | 110M | Masked LM | BERT-base |

---

## 2. Generative LLMs & Instruction-Tuned Decoders

| Model Repository | Parameter Count | Fine-Tuning Task | Base Model |
| :--- | :--- | :--- | :--- |
| `saillab/Nepali_Alpaca_ChatGPT_7B` | 7B | Instruction Following | Llama-7B |
| `vhab10/Llama-3.2-3B-Instruct_Nepali_4bit` | 3B | Devanagari Chat | Llama-3.2-3B |
| `vhab10/Llama-3.1-8B-Nepali-alpaca-merged-16bit` | 8B | Alpaca SFT | Llama-3.1-8B |
| `IRIIS-RESEARCH/GPT2Instruct_Nepali_124M` | 124M | Instruction Following | GPT-2 |

---

## 3. Speech Recognition (ASR) & Text-to-Speech (TTS)

| Model Repository | Task | Modality | Target Language |
| :--- | :--- | :--- | :--- |
| `devrahulbanjara/ne-en-codeswitching-asr-technical-interview` | ASR | Audio -> Devanagari | Nepglish Code-Mixed |
| `cfilt/RoundTripOCR-nepali` | OCR | Image -> Devanagari | Nepali Document OCR |
