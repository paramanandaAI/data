# Comprehensive Local & Research Dataset Index

This document provides a complete inventory of all local datasets, held-out evaluation benchmarks, research paper preprints, and raw student experimental dumps across the Paramananda ecosystem.

---

## 🔬 1. Research Papers & PDF Preprints

| Document / Paper | Size | Location (Local) | Focus / Domain | Citation / Source |
| :--- | :--- | :--- | :--- | :--- |
| **`2505.14553v2.pdf`** | 312 KB | `old_old/raw_data_archive/learnings_from_semster/hindi-nepali-translation/` | Neural Machine Translation for Devanagari & Indic Languages | arXiv Preprint (2025/2026) |
| **`example.pdf`** | 31.5 MB | `old_old/library_test/ocr/` | Manuscript / OCR Document Evaluation PDF | Library Test Suite |

---

## 📊 2. Held-Out Evaluation Benchmarks (`hf_benchmarks/` — 113.57 MB)

These datasets represent local HuggingFace parquet/LFS dumps for zero-shot and fine-tuning evaluation across NLU and reading comprehension:

| Benchmark Name | Task Type | Files | Local Size | Source Repository |
| :--- | :--- | :--- | :--- | :--- |
| **`Co-Reference-Nepali`** | Anaphora & Coreference | Parquet | ~2.5 MB | `IRIIS-RESEARCH/Co-Reference-Nepali` |
| **`CoLA-Nepali`** | Linguistic Acceptability | Parquet | 1.22 MB | `IRIIS-RESEARCH/CoLA-Nepali` |
| **`Filling-Masks-Nepali`** | Masked LM Evaluation | Parquet | ~5.0 MB | `IRIIS-RESEARCH/Filling-Masks-Nepali` |
| **`MNLI-Nepali`** | Multi-Genre NLI | Parquet | 30.1 MB | `IRIIS-RESEARCH/MNLI-Nepali` |
| **`MRPC-Nepali`** | Paraphrase Identification | Parquet | ~3.0 MB | `IRIIS-RESEARCH/MRPC-Nepali` |
| **`NepaliDataClassifiers`** | News Classification | Parquet | ~12.0 MB | `IRIIS-RESEARCH/NepaliDataClassifiers` |
| **`QADSM-Nepali`** | Domain Question Answering | Parquet | ~4.5 MB | `IRIIS-RESEARCH/QADSM-Nepali` |
| **`QNLI-Nepali`** | Question NLI | Parquet | ~15.0 MB | `IRIIS-RESEARCH/QNLI-Nepali` |
| **`QQP-Nepali`** | Question Pair Matching | Parquet | ~18.0 MB | `IRIIS-RESEARCH/QQP-Nepali` |
| **`RTE-Nepali`** | Textual Entailment | Parquet | ~2.0 MB | `IRIIS-RESEARCH/RTE-Nepali` |
| **`Sentiment-Analysis-Nepali`**| Sentiment Polarity | Parquet | 7.01 MB | `IRIIS-RESEARCH/Sentiment-Analysis-Nepali` |
| **`STS-B-Nepali`** | Semantic Similarity | Parquet | ~1.5 MB | `IRIIS-RESEARCH/STS-B-Nepali` |
| **`WinoGrande-Nepali`** | Commonsense Reasoning | Parquet | ~3.8 MB | `IRIIS-RESEARCH/WinoGrande-Nepali` |
| **`XNLI-Nepali`** | Cross-Lingual NLI | Parquet | 12.06 MB | `IRIIS-RESEARCH/XNLI-Nepali` |

---

## 🛠️ 3. Student Experimental & Semester Corpora (321.8 MB)

| Folder / Corpus | Size | Key Files | Description & Pipeline Status |
| :--- | :--- | :--- | :--- |
| **`hindi_nepali_test`** | 92.55 MB | `finalhi-ne-en.hi`, `finalhi-ne-en.ne` | Parallel Hindi-Nepali evaluation corpus. *Sample created in `samples/hindi_nepali_translation/`*. |
| **`library_test`** | 155.16 MB | `nepali_roman_word.csv` (123MB), 9 OCR JPEGs | Transliteration dictionary (~2.4M pairs) + OCR test images. *Sample created in `samples/`*. |
| **`raw_data_archive`** | 18.46 MB | `synonym.csv` (8.8MB), `pos.csv` (4.0MB), `test.hi`, `test.ne` | WordNet synset expansion outputs + Hindi-Nepali test split. |
| **`synthetic_raw`** | 55.66 MB | `iforgotsource.csv` (30.8MB), `output.json` (27.4MB) | Unverified scraped parallel sentences + LLM WordNet synset output. *Sample created in `samples/iforgotsource/`*. |
| **`domain_adaptation_agriculture`** | < 1 KB | `domain_adaptation_agriculture.md` | Scraped ~1.7M agriculture documents using HuggingFace & regex filtering (`krishi`). |

---

## 🔍 Missing Elements & Recommendations for Future Iterations

1. **Agriculture Corpus Indexing**: `domain_adaptation_agriculture.md` mentions 1.7M scraped agriculture documents, but only notes exist on disk. A dataset YAML contract should be written once the processed parquet files are uploaded to HuggingFace.
2. **Metadata Recovery for `iforgotsource.csv`**: Run sentence similarity matching against OPUS parallel datasets to re-assign exact corpus citations.
3. **Evaluation Script Integration**: Standardize Python evaluation scripts in `nepalinlplibrary` to directly consume the parquet files inside `hf_benchmarks/`.
