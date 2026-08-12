> Source: `sources/eval/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Evaluation Benchmarks, Safety & Metrics: Task Guide & Notes

## 🇳🇵 Evaluation Protocols for Nepali LLMs
1. **Perplexity & Token Fertility:** Measure cross-entropy loss and average tokens per word across native Devanagari text.
2. **Generative Evaluation Metrics:**
   - **Translation/Summarization:** BLEU, chrF++, Rouge-1, Rouge-L.
   - **Reasoning & Safety:** Exact Match (EM), F1-Score, Multi-class Macro-F1.

---

## 🤖 Modern End-to-End Evaluation with Gemma 4 & Sentence-BERT
- **Sentence-BERT (Semantic Alignment Metric):**
  - Compute BERTScore on Nepali embeddings for factual similarity evaluation.
- **Gemma 4 as a Judge (LLM-as-a-Judge):**
  - Structured evaluation prompt scoring grammar, factual accuracy, and honorific appropriateness on a 1-5 scale.
