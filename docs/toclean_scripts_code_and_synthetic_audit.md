# Audit & Inventory: Synthetic Datasets & Code Utilities (`toclean_scripts` & `old_old`)

This document provides a comprehensive audit of the code utilities, synthetic Devanagari datasets, and NLP pipelines discovered in `local_nogit/data_1/toclean_scripts` and `old_old/dataloader`.

---

## 🛠️ 1. Reusable Code Utilities for `nepalinlplibrary`

The following standalone Python modules were audited from `toclean_scripts` and identified for integration into `nepalinlplibrary`:

| Module Name | Original Location | Description & Functionality | Potential `nepalinlplibrary` Target |
| :--- | :--- | :--- | :--- |
| **`preeti.py`** | `toclean_scripts/.../utils/preeti.py` | Legacy Preeti font mapping engine for converting non-Unicode legacy text into standard Devanagari Unicode. | `nepalinlplibrary.preprocessing.preeti` |
| **`morpheme_parser.py`** | `toclean_scripts/.../data_loaders/morpheme_parser.py` | Rule-based affix stripper & morpheme parser implementing 128 suffix constraints (Shrestha & Dhakal). | `nepalinlplibrary.morphology.morpheme_parser` |
| **`hybrid_retriever.py`** | `toclean_scripts/.../services/rag/hybrid_retriever.py` | RAG retrieval engine combining BM25 sparse lexical matching with dense vector embeddings (MuRIL / BGE). | `nepalinlplibrary.retrieval.hybrid` |
| **`gov_scraper.py`** | `toclean_scripts/.../services/search/gov_scraper.py` | Web scraper and HTML cleaner tailored for Nepal government portals, legal acts, and gazette notices. | `nepalinlplibrary.data.scrapers` |
| **`combine_dataset.py`** | `toclean_scripts/.../_inspirations/combine_dataset.py` | Schema standardization tool converting multi-source raw records into unified OpenAI Chat JSONL format. | `nepalinlplibrary.dataloader.exporter` |
| **`generate.py`** | `toclean_scripts/.../_inspirations/generate.py` | Synthetic dataset generator leveraging LLM prompts (spelling, QA, agriculture, transliteration). | `nepalinlplibrary.synthetic.generator` |

---

## 📊 2. Synthetic & Formatted Instruction Datasets Audit

| Dataset | Format | Volume | Description & Source | Local Path / Sample |
| :--- | :--- | :--- | :--- | :--- |
| **English-Nepali Translation** | JSONL | **10,031 rows** (34.8 MB) | Parallel instruction pairs for English $\leftrightarrow$ Nepali translation. | `samples/synthetic_instructions/en_ne_translation_sample.jsonl` |
| **Tourism & Trekking Q&A** | JSONL | **3,722 rows** (3.26 MB) | Domain QA on Nepalese trekking routes, culture, and travel logistics in Nepali. | `samples/synthetic_instructions/trekking_sample.jsonl` |
| **Rakshak Toxicity Dataset** | CSV | **527 rows** (0.77 MB) | 3-stage toxicity dataset (`noisy` $\rightarrow$ `devanagari_unaware` $\rightarrow$ `nepali_aware_final`). | `samples/toxicity_data/toxicity_sample.csv` |
| **Web Agriculture Web Corpus** | TSV / CSV | **10,000 rows** (51.8 MB) | Cleaned web crawl subset of agriculture portal text. | `old_old/dataloader/train/word_agriculture_web/` |
| **Unigram Frequency Corpus** | CSV / JSON | **218.16 MB** | User annotation & unigram frequency statistics from Nepali news & web crawls. | `old_old/dataloader/train/synthetic/balkbal/corpus_analysis/` |
| **Dr. Prasain Papers Instruction Set**| JSONL | **29 files** (37 rows) | Instruction-formatted abstracts and rules from Dr. Prasain's publication series. | `old_old/dataloader/train/linguistics/prasain_publications/` |

---

## ✅ Migration & Completeness Status

- **Dataset Specs**: All 65 YAML dataset specs migrated to `datasets/` and indexed in `catalog.jsonl`.
- **Docs Hub**: 11 master documentation files consolidated in `docs/`.
- **Sample Coverage**: Samples created for large parallel text, transliteration, synthetic instructions, WordNet expansion, and toxicity data in `samples/`.
- **Code Assets**: Key Python utilities documented for library porting.
