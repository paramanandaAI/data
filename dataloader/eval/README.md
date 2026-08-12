# Evaluation Benchmarks & Held-Out Evaluation Suites

> Standardized, held-out evaluation benchmarks for assessing model performance across Natural Language Understanding (NLU), Reading Comprehension, Speech Recognition (ASR), and LLM reasoning. Datasets in this directory are STRICTLY HELD-OUT and NEVER included in pretraining or instruction fine-tuning splits.

---

## 📁 Directory Structure

```tree
dataset/transformed/eval/
├── glue_nepali/           # GLUE-Nepali benchmark suite (MNLI, XNLI, CoLA, QQP, MRPC, RTE, QNLI, STS-B, WinoGrande)
├── squad_nepali/          # Extractive Reading Comprehension benchmarks (Nepali SQuAD & XQuAD)
├── ifeval_nepali/         # Instruction following & constraint compliance benchmarks
├── asr_benchmark/         # Speech Recognition evaluation sets (Word Error Rate - WER testing)
└── llm_bench/             # LLM benchmarks (nepali-bench, honorific-bench, nepal-legal-qa-benchmark)
```

---

## 📜 Benchmark Registry & Citations

| Benchmark | Directory | Task Type | Metrics | Source & Citation |
|---|---|---|---|---|
| **NLUE / GLUE-Nepali** | `eval/glue_nepali/` | Multi-Genre NLI, Similarity, Paraphrase | Accuracy / F1 / Pearson | [IRIIS-RESEARCH/GLUE-Nepali](https://huggingface.co/collections/IRIIS-RESEARCH/nepali-lanuguage-understanding-evaluation-benchmark) (Nyachhyon et al., Findings IJCNLP 2025) |
| **MNLI-Nepali** | `eval/glue_nepali/` | Multi-Genre NLI | Accuracy | IRIIS-RESEARCH/MNLI-Nepali |
| **XNLI-Nepali** | `eval/glue_nepali/` | Cross-lingual NLI | Accuracy | IRIIS-RESEARCH/XNLI-Nepali |
| **STS-B-Nepali** | `eval/glue_nepali/` | Semantic Similarity | Pearson / Spearman | IRIIS-RESEARCH/STS-B-Nepali |
| **CoLA-Nepali** | `eval/glue_nepali/` | Linguistic Acceptability | Matthew's Corr | IRIIS-RESEARCH/CoLA-Nepali |
| **QQP-Nepali** | `eval/glue_nepali/` | Paraphrase Detection | F1 / Accuracy | IRIIS-RESEARCH/QQP-Nepali |
| **MRPC-Nepali** | `eval/glue_nepali/` | Paraphrase Detection | F1 / Accuracy | IRIIS-RESEARCH/MRPC-Nepali |
| **RTE-Nepali** | `eval/glue_nepali/` | Textual Entailment | Accuracy | IRIIS-RESEARCH/RTE-Nepali |
| **QNLI-Nepali** | `eval/glue_nepali/` | Question NLI | Accuracy | IRIIS-RESEARCH/QNLI-Nepali |
| **WinoGrande-Nepali** | `eval/glue_nepali/` | Coreference / Commonsense | Accuracy | IRIIS-RESEARCH/WinoGrande-Nepali |
| **SQuAD-Nepali** | `eval/squad_nepali/` | Reading Comprehension | Exact Match / F1 | [Bibek1129/nepali_SQuAD](https://huggingface.co/datasets/Bibek1129/nepali_SQuAD) |
| **XQuAD-Nepali** | `eval/squad_nepali/` | Cross-lingual QA | Exact Match / F1 | [Yunika/xquad-nepali](https://huggingface.co/datasets/Yunika/xquad-nepali) |
| **Nepali-Bench** | `eval/llm_bench/` | Open LLM Benchmark | Accuracy / BLEU | [premmm/nepali-bench](https://huggingface.co/datasets/premmm/nepali-bench) |
| **Honorific-Bench** | `eval/llm_bench/` | Register & Pragmatics | Register Compliance | [himalaya-ai/nepali-honorific-bench](https://huggingface.co/datasets/himalaya-ai/nepali-honorific-bench) |
| **Legal-QA-Bench** | `eval/llm_bench/` | Domain Legal QA | Pass@1 / Citation F1 | [chhatramani/nepal-legal-qa-benchmark_v1](https://huggingface.co/datasets/chhatramani/nepal-legal-qa-benchmark_v1) |
| **ASR Benchmark** | `eval/asr_benchmark/` | Speech Recognition | WER / CER | [tonibirat/nepali-asr-benchmark-50gb](https://huggingface.co/datasets/tonibirat/nepali-asr-benchmark-50gb) |

---

## 🔬 Literature & Research Papers

1. **Nepali Language Understanding Evaluation (NLUE):**
   - *Nyachhyon, B., Sharma, S., Thapa, S., & Bal, B. K. (2025)*. **Consolidating and Developing Benchmarking Datasets for the Nepali NLU Tasks**. *Findings of the Association for Computational Linguistics: IJCNLP-AACL 2025*, [ACL Anthology](https://aclanthology.org/2025.findings-ijcnlp.119/).
2. **NepBERTa & Nep-gLUE:**
   - *Timilsina, S., Gautam, B., & Bhattarai, B. (2022)*. **NepBERTa: Nepali Language Model Trained on a Large Corpus**. *AACL-IJCNLP 2022*, [ACL Anthology](https://aclanthology.org/2022.aacl-short.34/).
3. **Indic-Wide Benchmarks:**
   - *Doddapaneni, S., et al. (2023)*. **IndicXTREME: A Comprehensive Benchmark for 20 Indic Languages**. *ACL 2023*, [ACL Anthology](https://aclanthology.org/2023.acl-long.693/).
   - *Singh, A., et al. (2024)*. **IndicGenBench: A Multilingual Benchmark for Evaluating Generation Capabilities of LLMs in Indic Languages**. *ACL 2024*, [ACL Anthology](https://aclanthology.org/2024.acl-long.595/).

---

## 🔒 Contamination Guardrail

All dataset files placed in `eval/` are registered in the deduplication pipeline. Any pretraining text or instruction pair with **$\ge 80\%$ n-gram overlap** with `eval/` benchmarks is automatically purged from training splits to prevent test-set leakage.
