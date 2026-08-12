# Master Index & Inventory — `awesome_data/`

> Complete inventory of every file originally in `sources/` with its classification and target location in the new organization.
> All 41 md files have been **migrated to the new trees** (content preserved in `Nepali_data/`, `Nepali_research/`, `nlp_notes/`) and the originals deleted.
> The 55 YAML dataset contracts now live **flattened** in `yaml/` (folder was renamed from `sources/`; subfolder structure removed).

---

## 1. Reorganization Map

| Target folder | Contents | Comes from |
|---|---|---|
| `Nepali_data/` | Dataset contracts, dataset catalogs, dataset-focused notes | YAML files (deferred), dataset READMEs, dataset sections of NOTES.md |
| `Nepali_research/` | Academic literature indexes, paper bibliographies, surveys, citations | `📖 Curated Academic Literature Index`, `📚 Academic Citations & Literature` sections |
| `nlp_notes/` | Task guides, linguistic guides, model-adaptation guides, tooling, frameworks, learning resources | Guide/technique/framework sections of NOTES.md |

Split rules applied to every `NOTES.md`:
- `## 📖 Curated Academic Literature Index (N Works)` + `## 📚 Academic Citations & Literature` / `## 📚 Academic Literature & Citations` / `## 🎓 Domain & Task Literature` → **Nepali_research**
- Task guides, linguistic nuances, model adaptation, protocols, pipelines, framework tables → **nlp_notes**
- Dataset listings/tables → **Nepali_data**

**Status legend:** `done` = file created in target folder · `deferred` = tracked, not yet moved · `whole` = file copied whole (no split needed)

---

## 2. MD Files (41) — Classification & Targets

### 2.1 Root

| Source file | Type | Target(s) | Status |
|---|---|---|---|
| `sources/README.md` | Dataset catalog | `Nepali_data/dataset_catalog.md` | done |
| `sources/NOTES.md` | Master bibliography + ecosystem + frameworks + learning | `Nepali_research/README.md`, `nlp_notes/frameworks/ecosystem.md`, `nlp_notes/learning_resources.md`, `Nepali_data/huggingface_dataset_catalog.md` | done |

### 2.2 Pretrain

| Source file | Type | Target(s) | Status |
|---|---|---|---|
| `sources/pretrain/README.md` | Dataset catalog | `Nepali_data/pretrain/README.md` | done |
| `sources/pretrain/monolingual/NOTES.md` | Mixed: lit index (32) + linguistic/pretraining guide | `Nepali_research/pretrain/monolingual/literature.md`, `nlp_notes/pretrain/monolingual/guide.md` | done |
| `sources/pretrain/tokenization/NOTES.md` | Guide (mostly technical) | `nlp_notes/tokenization/guide.md`, `Nepali_research/pretrain/tokenization/literature.md` | done |

### 2.3 SFT

| Source file | Type | Target(s) | Status |
|---|---|---|---|
| `sources/sft/README.md` | Dataset catalog | `Nepali_data/sft/README.md` | done |
| `sources/sft/domain/agriculture/NOTES.md` | Mixed: lit (4) + agro guide | `Nepali_research/sft/domain/agriculture/literature.md`, `nlp_notes/sft/domain/agriculture/guide.md` | done |
| `sources/sft/domain/commerce/NOTES.md` | Mixed: lit (2) + finance guide | `Nepali_research/sft/domain/commerce/literature.md`, `nlp_notes/sft/domain/commerce/guide.md` | done |
| `sources/sft/domain/crisis_governance/NOTES.md` | Literature only (8) | `Nepali_research/sft/domain/crisis_governance/literature.md` | done |
| `sources/sft/domain/healthcare/NOTES.md` | Mixed: lit (15) + clinical guide | `Nepali_research/sft/domain/healthcare/literature.md`, `nlp_notes/sft/domain/healthcare/guide.md` | done |
| `sources/sft/domain/legal/NOTES.md` | Mixed: lit (2) + legal guide | `Nepali_research/sft/domain/legal/literature.md`, `nlp_notes/sft/domain/legal/guide.md` | done |
| `sources/sft/gec/NOTES.md` | Mixed: lit (12) + GEC guide | `Nepali_research/sft/gec/literature.md`, `nlp_notes/sft/gec/guide.md` | done |
| `sources/sft/instruction/NOTES.md` | Mixed: lit (1) + instruction guide + frameworks | `Nepali_research/sft/instruction/literature.md`, `nlp_notes/sft/instruction/guide.md` | done |
| `sources/sft/nlp_tasks/anaphora/NOTES.md` | Mixed: lit (1) + anaphora guide | `Nepali_research/sft/nlp_tasks/anaphora/literature.md`, `nlp_notes/sft/nlp_tasks/anaphora/guide.md` | done |
| `sources/sft/nlp_tasks/dependency_parsing/NOTES.md` | Literature only (2) | `Nepali_research/sft/nlp_tasks/dependency_parsing/literature.md` | done |
| `sources/sft/nlp_tasks/idioms_figurative/NOTES.md` | Literature only (3) | `Nepali_research/sft/nlp_tasks/idioms_figurative/literature.md` | done |
| `sources/sft/nlp_tasks/morphology/NOTES.md` | Mixed: lit (20) + morphology guide | `Nepali_research/sft/nlp_tasks/morphology/literature.md`, `nlp_notes/sft/nlp_tasks/morphology/guide.md` | done |
| `sources/sft/nlp_tasks/ner/NOTES.md` | Mixed: lit (48) + NER guide | `Nepali_research/sft/nlp_tasks/ner/literature.md`, `nlp_notes/sft/nlp_tasks/ner/guide.md` | done |
| `sources/sft/nlp_tasks/pos/NOTES.md` | Mixed: lit (27) + POS guide | `Nepali_research/sft/nlp_tasks/pos/literature.md`, `nlp_notes/sft/nlp_tasks/pos/guide.md` | done |
| `sources/sft/nlp_tasks/sentiment/NOTES.md` | Mixed: lit (41) + sentiment guide | `Nepali_research/sft/nlp_tasks/sentiment/literature.md`, `nlp_notes/sft/nlp_tasks/sentiment/guide.md` | done |
| `sources/sft/nlp_tasks/structured_output/NOTES.md` | Literature only (2) | `Nepali_research/sft/nlp_tasks/structured_output/literature.md` | done |
| `sources/sft/nlp_tasks/wsd/NOTES.md` | Mixed: lit (7) + WSD guide | `Nepali_research/sft/nlp_tasks/wsd/literature.md`, `nlp_notes/sft/nlp_tasks/wsd/guide.md` | done |
| `sources/sft/qa/NOTES.md` | Literature only (2) | `Nepali_research/sft/qa/literature.md` | done |
| `sources/sft/summarization/NOTES.md` | Mixed: lit (5) + summarization guide | `Nepali_research/sft/summarization/literature.md`, `nlp_notes/sft/summarization/guide.md` | done |
| `sources/sft/translation/NOTES.md` | Mixed: lit (30) + translation guide | `Nepali_research/sft/translation/literature.md`, `nlp_notes/sft/translation/guide.md` | done |

### 2.4 Similarity

| Source file | Type | Target(s) | Status |
|---|---|---|---|
| `sources/similarity/README.md` | Dataset catalog | `Nepali_data/similarity/README.md` | done |
| `sources/similarity/nli_sts/NOTES.md` | Mixed: lit + NLI/STS guide | `Nepali_research/similarity/nli_sts/literature.md`, `nlp_notes/similarity/nli_sts/guide.md` | done |
| `sources/similarity/reranking/NOTES.md` | Guide + lit | `nlp_notes/similarity/reranking/guide.md`, `Nepali_research/similarity/reranking/literature.md` | done |

### 2.5 Multimodal

| Source file | Type | Target(s) | Status |
|---|---|---|---|
| `sources/multimodal/README.md` | Dataset catalog | `Nepali_data/multimodal/README.md` | done |
| `sources/multimodal/asr/NOTES.md` | Mixed: lit (24) + ASR guide | `Nepali_research/multimodal/asr/literature.md`, `nlp_notes/multimodal/asr/guide.md` | done |
| `sources/multimodal/ocr/NOTES.md` | Mixed: lit (3) + OCR guide | `Nepali_research/multimodal/ocr/literature.md`, `nlp_notes/multimodal/ocr/guide.md` | done |
| `sources/multimodal/ocr/handwritten/NOTES.md` | Literature only (1) | `Nepali_research/multimodal/ocr/handwritten/literature.md` | done |
| `sources/multimodal/retrieval/NOTES.md` | Guide + lit | `nlp_notes/multimodal/retrieval/guide.md`, `Nepali_research/multimodal/retrieval/literature.md` | done |
| `sources/multimodal/sign_language/NOTES.md` | Literature only (1) | `Nepali_research/multimodal/sign_language/literature.md` | done |
| `sources/multimodal/tts/NOTES.md` | Mixed: lit (10) + TTS guide | `Nepali_research/multimodal/tts/literature.md`, `nlp_notes/multimodal/tts/guide.md` | done |
| `sources/multimodal/vision/NOTES.md` | Mixed: lit (19) + vision guide | `Nepali_research/multimodal/vision/literature.md`, `nlp_notes/multimodal/vision/guide.md` | done |

### 2.6 Eval & Other & Tools

| Source file | Type | Target(s) | Status |
|---|---|---|---|
| `sources/eval/NOTES.md` | Mixed: lit (52) + eval protocols | `Nepali_research/eval/literature.md`, `nlp_notes/eval/guide.md` | done |
| `sources/eval/README.md` | Dataset catalog | `Nepali_data/eval/README.md` | done |
| `sources/evaluation/NOTES.md` | Guide (LLMJudge, Navarasa rubric, metrics) | `nlp_notes/eval/llm_judge_and_metrics.md` | done |
| `sources/other/NOTES.md` | Literature (57) + non-core registry | `Nepali_research/other/literature.md`, `nlp_notes/other/homonym_registry.md` | done |
| `sources/tools/NOTES.md` | Guide + lit | `nlp_notes/tools/guide.md`, `Nepali_research/tools/literature.md` | done |

---

## 3. YAML Dataset Contracts (55) — flattened into `yaml/`

> These are the actual dataset specs. They now live **flat** in `yaml/` (renamed from `sources/`, structure removed). The tables below keep the ORIGINAL category path (from `sources/`) for provenance — when the contracts are verified and sorted into `Nepali_data/<category>/`, restore that path. All 55 listed below so none is lost.

### 3.1 Pretrain (5)
| File | Dataset | Task |
|---|---|---|
| `pretrain/monolingual/todo_github_shekharkoirala_nepali_wikipedia.yaml` | shekharkoirala/nepali_wikipedia_curpos | pretrain/monolingual |
| `pretrain/monolingual/todo_huggingface_Basanta55_cc100-nepali-strictly-cleaned.yaml` | Basanta55/cc100-nepali-strictly-cleaned-devanagari-only | pretrain/monolingual |
| `pretrain/monolingual/todo_huggingface_himalaya-ai_nepali-corpus-compile.yaml` | himalaya-ai/nepali-corpus-compile | pretrain/monolingual |
| `pretrain/monolingual/todo_huggingface_Sakonii_nepalitext-language-model-dataset.yaml` | Sakonii/nepalitext-language-model-dataset | pretrain/monolingual |
| `pretrain/parallel/todo_ai4bharat_indictrans2_parallel_en_ne.yaml` | AI4Bharat/IndicTrans2-Parallel-en-ne | pretrain/parallel |

### 3.2 SFT (30)
| File | Dataset | Task |
|---|---|---|
| `sft/domain/agriculture/todo_huggingface_Chhabi_Nepali-Agriculture-QA.yaml` | Chhabi/Nepali-Agriculture-QA | sft/domain/agriculture |
| `sft/domain/commerce/todo_github_superryeti_Daraz-online-shopping-data.yaml` | superryeti/Daraz-online-shopping-data-corpus | sft/domain/commerce |
| `sft/domain/commerce/todo_huggingface_ashokpoudel_retail-banking-chatbot.yaml` | ashokpoudel/retail-banking-llm-chatbot-training-dataset-nepali | sft/domain/commerce |
| `sft/domain/crisis_governance/todo_ieee_Rauniyar_Nepali_Election_Discourse.yaml` | Rauniyar/Nepali-Election-Discourse-Tweets | sft/domain/crisis_governance |
| `sft/domain/healthcare/todo_huggingface_Bibek-Poudel_NepaliMedicalConversation.yaml` | Bibek-Poudel/NepaliMedicalConversation | sft/domain/healthcare |
| `sft/domain/healthcare/todo_huggingface_Chhabi_Nepali-Health-QA.yaml` | Chhabi/Nepali-Health-QA | sft/domain/healthcare |
| `sft/domain/legal/todo_huggingface_chhatramani_Nepal-Legal-Text-Corpus-44laws.yaml` | chhatramani/Nepal-Legal-Text-Corpus-44laws | sft/domain/legal |
| `sft/domain/legal/todo_huggingface_chhatramani_nepal_civil_law_QA_v2.yaml` | chhatramani/nepal_civil_law_QA_v2 | sft/domain/legal |
| `sft/gec/huggingface_cfilt_RoundTripOCR-nepali.yaml` | cfilt/RoundTripOCR-nepali | sft/gec |
| `sft/gec/huggingface_sumitaryal_nepali_grammatical_error_correction.yaml` | sumitaryal/nepali_grammatical_error_correction | sft/gec |
| `sft/gec/huggingface_sumitaryal_nepali_grammatical_error_correction_pair_choice.yaml` | sumitaryal/nepali_grammatical_error_correction_pair_choice | sft/gec |
| `sft/gec/huggingface_sumitaryal_nepali_grammatical_error_detection.yaml` | sumitaryal/nepali_grammatical_error_detection | sft/gec |
| `sft/instruction/todo_huggingface_dineshkarki_nepali-sft-dataset.yaml` | dineshkarki/nepali-sft-dataset | sft/instruction |
| `sft/instruction/todo_huggingface_himalaya-ai_nepali-hermes-function-calling-v1.yaml` | himalaya-ai/nepali-hermes-function-calling-v1 | sft/agent_tools |
| `sft/instruction/todo_huggingface_ibibek_nepali_alpaca.yaml` | ibibek/nepali_alpaca | sft/instruction |
| `sft/nlp_tasks/dependency_parsing/todo_acm_Rai_Nepali_Universal_Dependencies.yaml` | UniversalDependencies/UD_Nepali | sft/nlp_tasks/dependency_parsing |
| `sft/nlp_tasks/idioms_figurative/todo_acl_Pokharel_NeDIOM_Nepali_Idioms.yaml` | Pokharel/NeDIOM-Nepali-Idioms | sft/nlp_tasks/idioms_figurative |
| `sft/nlp_tasks/ner/todo_github_nowalab_DanfeNER.yaml` | nowalab/DanfeNER | sft/nlp_tasks/ner |
| `sft/nlp_tasks/pos/todo_github_SujilDevkota_NepaliCorpus-POS-Tags.yaml` | SujilDevkota/NepaliCorpus-POS-Tags | sft/nlp_tasks/pos |
| `sft/nlp_tasks/structured_output/todo_huggingface_himalaya-ai_nepali-json-mode-singleturn.yaml` | himalaya-ai/nepali-json-mode-singleturn | sft/nlp_tasks/structured_output |
| `sft/nlp_tasks/stylometry_honorifics/todo_github_12-Twelvve_poem_dataset.yaml` | 12-Twelvve/poem_dataset | sft/nlp_tasks/stylometry_honorifics |
| `sft/nlp_tasks/stylometry_honorifics/todo_huggingface_Boredoom17_Nepali-Flow-Formal.yaml` | Boredoom17/Nepali-Flow-Formal | sft/nlp_tasks/stylometry_honorifics |
| `sft/nlp_tasks/stylometry_honorifics/todo_huggingface_himalaya-ai_nepali-honorific-bench.yaml` | himalaya-ai/nepali-honorific-bench | sft/nlp_tasks/stylometry_honorifics |
| `sft/qa/huggingface_Bibek1129_nepali_SQuAD.yaml` | Bibek1129/nepali_SQuAD | sft/qa |
| `sft/summarization/todo_huggingface_realsanjeev_XLSum-nepali-summarization.yaml` | realsanjeev/XLSum-nepali-summerization-dataset | sft/summarization |
| `sft/translation/todo_github_binayachaudari_Nepali-Tamang-MT-Data.yaml` | binayachaudari/Nepali-Tamang-MT-Data | sft/translation |
| `sft/translation/todo_github_Shahil050_romanized_nepali_dataset.yaml` | Shahil050/romanized_nepali_dataset | sft/transliteration |
| `sft/translation/todo_huggingface_ashokpoudel_English-Nepali-Translation.yaml` | ashokpoudel/English-Nepali-Translation-Instruction-Dataset | sft/translation |
| `sft/translation/todo_huggingface_ilprl-docse_NepTam-Parallel-Corpus.yaml` | ilprl-docse/NepTam-A-Nepali-Tamang-Parallel-Corpus | sft/translation |
| `sft/translation/todo_huggingface_Saugatkafley_Nepali-Roman-Transliteration.yaml` | Saugatkafley/Nepali-Roman-Transliteration | sft/transliteration |

### 3.3 Similarity (3)
| File | Dataset | Task |
|---|---|---|
| `similarity/nli_sts/todo_huggingface_jangedoo_nepali-nli-20k.yaml` | jangedoo/nepali-nli-20k | similarity/nli |
| `similarity/nli_sts/todo_huggingface_jangedoo_stsb_nepali.yaml` | jangedoo/stsb_nepali | similarity/sts |
| `similarity/reranking/todo_huggingface_jangedoo_nepali-query-passage-hard-negatives-10k.yaml` | jangedoo/nepali-query-passage-hard-negatives-10k | similarity/reranking |

### 3.4 Multimodal (14)
| File | Dataset | Task |
|---|---|---|
| `multimodal/asr/huggingface_himalaya-ai_nep-voice-tts-compilation.yaml` | himalaya-ai/nep-voice-tts-compilation | multimodal/asr |
| `multimodal/asr/huggingface_ilprl-docse_Nwacha_Muna_A_Newari_ASR_Dataset.yaml` | ilprl-docse/Nwacha_Muna_A_Newari_ASR_Dataset | multimodal/asr |
| `multimodal/asr/todo_github_Aadarshttech_nepali-english-codeswitched-whisper.yaml` | Aadarshttech/nepali-english-codeswitched-whisper | multimodal/asr |
| `multimodal/asr/todo_github_ishworrsubedii_nepali_speech-to-text.yaml` | ishworrsubedii/nepali_speech-to-text_datasets | multimodal/asr |
| `multimodal/ocr/handwritten/todo_acl_Sarawgi_Old_Nepali_Manuscripts_HTR.yaml` | Sarawgi/Old-Nepali-Manuscripts-HTR | multimodal/ocr/handwritten |
| `multimodal/ocr/handwritten/todo_github_dahalsweekar_Nepali-Handwritten-Dataset.yaml` | dahalsweekar/Nepali-Handwritten-Dataset-for-Recognition | multimodal/ocr/handwritten |
| `multimodal/ocr/huggingface_himalaya-ai_devanagari_ocr_graphemes.yaml` | himalaya-ai/devanagari_ocr_graphemes | multimodal/ocr |
| `multimodal/ocr/huggingface_himalaya-ai_nepalipixel-synthetic-ocr-benchmark.yaml` | himalaya-ai/nepalipixel-synthetic-ocr-benchmark | multimodal/ocr |
| `multimodal/ocr/identity_documents/todo_github_Alish545_Number-Plate-Project.yaml` | Alish545/Number-Plate-Project | multimodal/ocr/identity_documents |
| `multimodal/ocr/identity_documents/todo_huggingface_jebish7_Driving_License_Nepali_Multimodal.yaml` | jebish7/Driving_License_Nepali_Multimodal | multimodal/ocr/identity_documents |
| `multimodal/sign_language/todo_thesis_Belbase_Nepali_Sign_Language.yaml` | Belbase/Nepali-Sign-Language-Dataset | multimodal/sign_language |
| `multimodal/tts/todo_huggingface_chhatramani_Nepali_TTS_55hrs.yaml` | chhatramani/Nepali_TTS_55hrs | multimodal/tts |
| `multimodal/vision/todo_github_bipeshrajsubedi_Flickr30k_Nepali_Dataset.yaml` | bipeshrajsubedi/Flickr30k_Nepali_Dataset | multimodal/vision |
| `multimodal/vision/todo_github_ShubhaPradhan_Nepali-Flickr8k-Dataset.yaml` | ShubhaPradhan/Nepali-Flickr8k-Dataset | multimodal/vision |

### 3.5 Eval (3)
| File | Dataset | Task |
|---|---|---|
| `eval/todo_github_ios-ioe_Nepali-Bias-Language-Dataset.yaml` | ios-ioe/Nepali-Bias-Language-Dataset | eval/safety |
| `eval/todo_huggingface_biraj-bhusal_rakshak-nepali-toxicity.yaml` | biraj-bhusal/rakshak-nepali-toxicity-final | eval/safety |
| `eval/todo_huggingface_mteb_NepaliNewsClassification.yaml` | mteb/NepaliNewsClassification | eval/classification |

> Note: 5 (pretrain) + 30 (SFT) + 3 (similarity) + 14 (multimodal) + 3 (eval) = **55 unique files** ✅

---

## 4. Verification Checklist

- [x] 41 source MD files accounted for (Section 2) and migrated to new trees
- [x] 55 source YAML files accounted for (Section 3) — now flat in `yaml/`
- [x] Every MD split preserves the original text — automated check: **3031/3031 content lines covered, 0 missing**
- [x] MD originals deleted from `sources/`; `sources/` renamed to `yaml/` and flattened (55 contracts)
- [x] Top-level READMEs written: `Nepali_data/README.md`, `Nepali_research/README.md`, `nlp_notes/README.md`

*Created: 2026-08-12 · Part of the `sources/` → `Nepali_data/ + Nepali_research/ + nlp_notes/` reorganization.*
