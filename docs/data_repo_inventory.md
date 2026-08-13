# Data Repository Deep Inventory — `githubrepos/data/` (161 files, verified Aug 2026)

> The user asked to "search dataset as whole across data inside repo folder". This is the result:
> every layer of `data/` mapped — papers (literature.md), dataset descriptions (catalogs),
> contracts (YAML + catalog.jsonl), actual bytes on disk (CSV/parallel/pdfs/images).
> ⚠️ NOTE: the README describes an `awesome_data/` layout; on disk the same content lives at
> `data/catalogs/`, `data/domain_tasks/`, and `data/dataloader/`. Both jsonl catalogs and the
> dataloader YAMLs point at `d:\paramananda\data\awesome_data\...` as their *original* home.

---

## 0. File census

| Type | Count | Role |
|---|---|---|
| `.md` | 86 | papers (≈40 `literature.md`), guides, catalogs, findings, READMEs |
| `.yaml` | 55 | dataset contract specs (parsed by `nepalinlplibrary.dataloader`) |
| `.jsonl` | 2 | master registry (55 entries) + yml_data staging (3 entries) |
| `.csv` | 5 | translit sample + WordNet legacy tables |
| `.ne/.hi` | 2 | Hindi–Nepali parallel test split (10,001 lines each) — **real on-disk data** |
| `.pdf` | 1 | arXiv paper on Hindi–Nepali translation (2505.14553v2) |
| `.jpg` | 9 | OCR thorough-evaluation test images |
| other | 1 | .gitignore |

---

## 1. Literature layer — `domain_tasks/**/literature.md` (papers)

| Task folder | lit file | Relevance to noising/denoising paper |
|---|---|---|
| `eval/literature.md` | 27+ entries | Nepali eval challenges; code-mixing in memes; Roman-script sections (line 47) |
| `sft/nlp_tasks/ner/literature.md` | 36 entries | **#32 = arXiv:2604.14171 "Benchmarking Linguistic Adaptation … Romanized Nepali" (Llama/Mistral/Qwen3-8B, QLoRA ~9k SFT)** — our key small-decoder precedent, found in-repo |
| `sft/nlp_tasks/sentiment/literature.md` | 22+ entries | **NepaliXlit entry**, **NEPTUN entry**, Romanized-Nepali BERT/RoBERTa (ioe), code-mixed abuse (Te/Ne), XLM-R Reddit corpora |
| `sft/translation/literature.md` | 26+ | #16 statistical/syllabification Nepali translit; Romanized-Nepali MT + predictive-text entries |
| `multimodal/ocr/literature.md` | (multi) | OCR for Devanagari; → `demos/ocr/findings.md` conclusion "need vigorous synthetic data" |
| `sft/gec/literature.md` | (multi) | NepBERTa GEC synthetic/annotated pairs (referenced by `ourplan.md` GEC row) |
| `pretrain/monolingual/guide.md` | guide | ⭐ **"Denoising Objectives (T5/UL2): masking spans of 3–5 tokens with prefix LM yields superior morphological retention"** — in-repo support for our seq2seq span noising |
| `sft/translation/guide.md` | guide | Romanized translit ambiguity ("khana khaye"); **cos-sim(ne,en) filtering of noisy parallel crawls** |
| `tools/guide.md` | guide | Romanization schemes ISO 15919 / SLP1 / Hunterian; script detection → conversion workflow (map to `ne_noise.translit` tiers) |
| `sft/nlp_tasks/morphology/` | lit+guide | 128-suffix stripping, CFG inflections — morphology noise grounding |

**Homonym registry** (`other/homonym_registry.md`) = 11 non-NLP papers accidentally scraped (cybersecurity "S. Nepal", agriculture "NLP"); use as a **caution list** — never cite into the paper.

## 2. Dataset-description layer — catalogs

| File | What it contains | For the paper |
|---|---|---|
| `data/README.md` | architecture + YAML schema (export_templates t5/gemma4, validation min_devanagari_ratio 0.70, contamination guardrail ≥80% n-gram) | cite schema/guardrail in methodology |
| `catalogs/huggingface_reference.md` | **"564+ Nepali datasets on HF"** + pretraining corpus list: Sakonii 13.4M passages, himalaya-ai/nepali-corpus-compile 31.3M dedup sentences, Basanta55 cc100-ne 1.29M, raygx 14.6M, tonibirat/neBrahma 20.3M, manojbaniya/ift-nepali-v5, Aananda-giri 1.85M, Shubhaaa3399/nepalisent | grounds claims about Nepali pretraining scale (small-model section) |
| `catalogs/dataset_catalog.md` | full tree: pretrain monolingual/parallel, sft domain×5, gec, instruction, nlp_tasks×8, summarization, translation, similarity, multimodal, eval; tooling table (eda_nlp, TextAttack, nlpaug, argilla, trafilatura, text-dedup, detoxify) | augmentation tooling references for synthetic-noise pipeline |
| `catalogs/master_bibliography.md` | 289 lines: master bibliography + status (`done` md split, `deferred` 55 YAMLs, next step web-verify) | **authority note: literature/catalog content is unverified AI-generated until web-checked** → adopt "verify before cite" rule |
| `domain_tasks/pretrain/awesome_pretraining.md` | Daraz corpus, nepal_wikipedia_curpos, NepaliCleanedDataset, ashokbasnet news 5 portals, Utshav media, NansKong pipeline, shiva500 Llama3-prep, acharyabi Text-Data-Cleaning, opendatahandbook | new clean-corpus candidates for noising targets |
| `domain_tasks/frameworks/ecosystem.md` | HF ecosystem mapping (incl. `Shahil050/romanized_nepali_dataset` under Transliteration) | row-level tooling citations |

## 3. Contract layer — YAMLs + catalogs

- **`catalogs/master_registry/catalog.jsonl`** = 55 entries. Status split (verified by `status:` field): **9 verified (gold)**: himalaya nep-voice-tts, ilprl Newari ASR, devanagari_ocr_graphemes, nepalipixel-synthetic-ocr, cfilt RoundTripOCR, sumitaryal GEC ×3, Bibek1129 SQuAD. **46 `todo`** (registered, not yet downloaded).
- **`dataloader/yaml/yml_data/catalog.jsonl`** = 3 staging entries (devanagari_ocr_graphemes ×2 rows-5 test, jangedoo stsb 1-row test) with `validation_status: pending` → this is the reactive-fetcher smoke-test output, NOT production data.
- Contract files physically live under `domain_tasks/<task>/contracts/*.yaml` (55 files) — schema: id, name, source_url, task, quality_tier, languages, size_stats, column_mapping, export_templates (t5/gemma4), validation.

## 4. On-disk data (real bytes — outside `plan/sources/`)

| File | Rows/size | Usability for denoising paper |
|---|---|---|
| `raw_data_archive/.../hindi-nepali-translation/data/test.ne` + `test.hi` | **10,001 lines each** | Hindi–Nepali parallel test split → Devanagari-adjacent transfer probe eval. ⚠️ Old archive — verify alignment quality before citing |
| `.../hindi-nepali-translation/2505.14553v2.pdf` | 305 KB | arXiv paper on Hindi–Nepali translation — read + cite if it fits (needs verification) |
| `raw_data_archive/.../nepali_wordnet_expansion/translation.csv` | 46,487 rows | WordNet lexical data — retired project; use contextually only (see findings.md) |
| `.../synonym.csv` | 211,334 rows | synonym bank → could seed `ne_noise` synonym-substitution op |
| `.../pos.csv` | 132,049 rows | POS table — morphology noise grounding (postposition detachment) |
| `.../category.csv` | 6,539 rows | category labels |
| `library_test/translit/nepali_roman_word_sample.csv` | 44 rows | translit lexicon sample (confirm full 2.4M CSV elsewhere before claiming) |
| `library_test/ocr/thorough_evaluation/*.jpg` (9) | images | hand-eval OCR samples only; **`awesome_ocr.md` literally asks "ground truth data anywhere?"** → OCR ground truth gap = open problem note |

## 5. Noise-relevant NEW items surfaced by this sweep (feed pipeline plan)

1. **In-repo citation for arXiv:2604.14171** at `domain_tasks/sft/nlp_tasks/ner/literature.md` #32 → QLoRA-on-Romanized-Nepali precedent now has a repo path.
2. **T5/UL2 denoising-objective recommendation** inside the repo (`pretrain/monolingual/guide.md`) → cites span masking 3–5 tokens; align `ne_noise` span ops with this.
3. **564+ HF Nepali datasets claim** (`catalogs/huggingface_reference.md`) → do NOT cite as-is; use only specific entries (Sakonii, neBrahma, cc100-ne) after web verification.
4. **Daraz/ashokbasnet/Utshav/news corpora** (`awesome_pretraining.md`) → additional clean Devanagari targets for Phase A noising.
5. **Morphology tables (128-suffix)** (`sft/nlp_tasks/morphology/`) → candidate rule-base for postposition/halanta noise ops.

## 6. Action updates → `pipeline/pipeline_dataset_plan.md`

- **Add to §4 (parallel)**: on-disk Hindi–Nepali 10k test split as Devanagari-transfer probe; verify alignment.
- **Add to §3 (engine)**: morphology suffix tables + synonym.csv 211k as rule/resource inputs to `ne_noise` ops.
- **Add to §6**: OCR ground-truth gap (awesome_ocr.md) as an open problem in related work.
- **Add to §5**: ifeval_nepali README_test + llm_judge_and_metrics.md as eval-layer files (check before final eval suite).
- Rule reinforcement: catalogs/literature are **unverified AI-generated until web-checked** (master_bibliography status note) — keep the "verify before cite" discipline across all docs.