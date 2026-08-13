# Nepali NLP & Language Modeling Advancements (2025 – 2026)

> A state-of-the-art research survey and dataset benchmark inventory for Nepali, Devanagari, and Romanized Nepali language modeling.

---

## 🚀 Key 2025–2026 Research Trends in Nepali NLP

1. **Nepali Generative Language Models (Decoder-Only)**:
   - **NepaliGPT** (arXiv:2506.16399): GPT-2-style CLM trained from scratch on 13M Devanagari sentences + 4,296 QA fine-tuning pairs (ROUGE-1: 0.26, PPL: 26.3).
   - **Custom 16k Nepali BPE Tokenizer** (arXiv:2512.14585): 98M-parameter GPT model with custom Nepali BPE tokenizer reaching PPL 21.8 on a 10.75 GB cleaned corpus.

2. **Pretraining Corpus Scale-Up**:
   - **neBrahma Nepali Pretrain Corpus P2b** (`tonibirat/neBrahma-Nepali-Pretrain-Corpus`): 20.3M documents / 1.845B tokens aggregated from IndicCorp, FineWeb2, IRIS, and Sagarmatha.
   - **Thapa et al. Corpus** (CHiPSAL 2025): 27.5 GB Nepali Devanagari corpus used for BERT, RoBERTa, and GPT-2 pretraining.

3. **Evaluation Benchmarks & Cultural Commonsense**:
   - **NLUE Benchmark** (IJCNLP 2025 Findings): Expanded Nep-gLUE into 12 tasks (~74.3k points) spanning NLI, STS, and grammatical error detection.
   - **NeCCo Benchmark** (LREC 2026 CHiPSAL): 1,295 multiple-choice items in Devanagari, Romanized Nepali, and English testing Nepali cultural commonsense (kinship, festivals, idioms, gastronomy).
   - **premmm/nepali-bench**: 100 curated Nepali LLM evaluation items across 8 categories (facts, culture, language, math, reasoning, safety).
   - **himalaya-ai/nepali-honorific-bench**: Benchmark for evaluating Nepali honorific registers (हजुर / तपाईँ / तँ).

4. **Romanized Nepali & Transliteration Benchmarking**:
   - **Llama-3.1 / Mistral / Qwen3 Adaptation** (arXiv:2604.14171): Benchmarked zero-shot vs QLoRA fine-tuning on 10k Romanized Nepali SFT pairs.

---

## 📚 Key Dataset Repositories

- **`himalaya-ai/nepali-pretrain-corpus`**: Devanagari pretraining text (OSCAR lineage).
- **`himalaya-ai/nepali-sft-compile`**: 1.67M compiled SFT rows.
- **`ashokpoudel/nepali-english-translation-dataset`**: 3.56M NE-EN parallel sentence pairs.
- **`jangedoo/stsb_nepali` & `jangedoo/nepali-nli-20k`**: STS-B and NLI triplet datasets for sentence embeddings.
- **`DipeshChaudhary/nepali-gector-style-token-level-tag-for-ged`**: GECToR token-level tags for Devanagari grammatical error correction.
- **`Sameer108/nepali-ai-final-v1`**: 176k SFT dataset for code, math, and general QA in Nepali.
