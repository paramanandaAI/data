# Semester Project Artifacts & Data Index

This document tracks the raw datasets, experimental scripts, and student exploratory artifacts produced during the semester coursework.

---

## 📁 1. Large Local Datasets (Gitignored / Archived)

These files are too large to be tracked directly in Git (`> 25 MB`). They live in the local environment and have representative sample files available in `samples/`.

| File Path | Size | Description & Citation | Sample Available |
| :--- | :--- | :--- | :--- |
| `hindi_nepali_test/src/finalhi-ne-en.hi` | 44.3 MB | Parallel Hindi text extracted for Hindi-Nepali MT experiments. Source: IndicTrans2 / OPUS. | `samples/hindi_nepali_translation/sample.hi` |
| `hindi_nepali_test/tgt/finalhi-ne-en.ne` | 48.3 MB | Target Nepali text for Hindi-Nepali MT evaluation. Source: IndicTrans2 / OPUS. | `samples/hindi_nepali_translation/sample.ne` |
| `library_test/translit/nepali_roman_word.csv` | 123.0 MB | Transliteration word-pair mapping dictionary (~2.4M pairs). Source: Saugat Kafley. | `samples/library_test/translit_sample.csv` |
| `synthetic_raw/learnings_from_semster/hindi-nepali-translation/iforgotsource.csv` | 29.5 MB | Unverified parallel sentence pairs extracted during semester sprint. *Pending source audit*. | `samples/iforgotsource/sample.csv` |
| `synthetic_raw/learnings_from_semster/nepali_wordnet_expansion/output.json` | 26.2 MB | WordNet synset expansion output generated via LLM prompts. Source: Student project output. | `samples/wordnet_expansion/synonym_sample.csv` |

---

## 🔬 2. Student Findings & Semester Notes

- **WordNet Expansion Findings (`raw_data_archive/learnings_from_semster/nepali_wordnet_expansion/findings.md`)**:
  - Investigated automated synset expansion using Lesk algorithm and bilingual dictionaries.
  - Extracted 200k category terms, 4M POS tagged tokens, and 8.8M synset candidates.

- **Hindi-Nepali Machine Translation Benchmark**:
  - Evaluation using BLEU/chrF metrics on neural translation models.
  - Comparative analysis on Devanagari cross-lingual transfer learning.
