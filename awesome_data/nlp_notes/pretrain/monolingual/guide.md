> Source: `sources/pretrain/monolingual/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Pretraining Monolingual Corpora: Research & Linguistic Guide


## 🇳🇵 Nepali Linguistic Nuances & Devanagari Preprocessing
1. **Zero-Width Character Anomalies:** Raw web scrapes frequently contain corrupted `\u200c` (ZWNJ) and `\u200d` (ZWJ) characters that fracture byte-pair encoding tokenizers. Strip isolated zero-width characters before vocabulary ingestion.
2. **Devanagari Unicode Normalization (NFC vs. NFD):** Devanagari text must always be normalized to Unicode **NFC** to prevent Nukta (`़`) and combining vowel marks from detaching.
3. **Punctuation Standardization:** Pūrṇa Virāma / Danda (`।` - `\u0964`) and Double Danda (`॥` - `\u0965`) must be preserved as primary sentence delimiters rather than converted to ASCII periods (`.`).

---

## 🤖 LLM Generation & Pretraining Strategy
- **Tokenizer Compression Ratio:** Standard multilingual tokenizers (LLaMA, GPT-4) produce 3.5 to 5 tokens per Nepali word. Custom vocabulary extension reduces fertility down to ~1.4 tokens/word.
- **Denoising Objectives (T5/UL2):** Masking spans of 3-5 tokens with prefix LM objectives yields superior morphological retention compared to causal-only masks.

## ?? Related Tokenizer Frameworks

| Repository | Focus |
|---|---|
| [huggingface/tokenizers](https://github.com/huggingface/tokenizers) | Fast state-of-the-art tokenizers optimized for research and production |
| [heinzerling/bpemb](https://github.com/bheinzerling/bpemb) | Pre-trained subword embeddings in 275 languages, based on BPE |
| [VKCOM/YouTokenToMe](https://github.com/VKCOM/YouTokenToMe) | Unsupervised text tokenizer focused on computational efficiency |
| [
lp-uoregon/trankit](https://github.com/nlp-uoregon/trankit) | Light-weight transformer-based toolkit for multilingual NLP |
| [cbaziotis/ekphrasis](https://github.com/cbaziotis/ekphrasis) | Text processing tool for social networks � tokenization, normalization, spell correction |
| [go-ego/gse](https://github.com/go-ego/gse) | Go efficient multilingual NLP and text segmentation |
