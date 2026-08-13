

# From Nepali_data README

# Nepali_data — Dataset Catalog & Contracts

> What we build WITH: Nepali NLP datasets and corpora.
> Derived from `sources/` (kept intact as reference). Full source→target map: [`../INDEX.md`](../INDEX.md).

## Folder structure

```
Nepali_data/
├── README.md                        # this file
├── dataset_catalog.md               # data catalog + tooling overview (from sources/README.md)
├── huggingface_dataset_catalog.md   # 564+ Nepali datasets on HuggingFace (from sources/NOTES.md §8.1)
├── pretrain/                        # README — monolingual + parallel + tokenization corpora
├── sft/                             # README — instruction, domain, GEC, nlp_tasks, QA, summarization, translation
├── similarity/                      # README — NLI/STS + reranking
├── multimodal/                      # README — ASR, TTS, OCR, vision, sign language, retrieval
└── eval/                            # README — classification + safety benchmarks
```

## Status
- `done`: all md catalog/README files copied or split from `sources/` (verification: 100% coverage)
- `deferred`: the 55 YAML dataset contracts stay in `sources/` for now — tracked in [`../INDEX.md`](../INDEX.md) section 3

## Next steps
1. Web-verify every dataset entry (URLs, row counts, licenses are unverified AI-generated content)
2. Add datasets found missing during verification
3. Mirror verified YAML contracts into `Nepali_data/<category>/`


# From Nepali_research README

> Source: `sources/NOTES.md` · split by content type
> Section kept: literature
> Do NOT edit content — pending web verification.

# Nepali_research — Academic Literature & Bibliography

> What we LEARN from: papers, surveys, and citation indexes for Nepali NLP.
> Derived from `sources/` (kept intact as reference). Full source→target map: [`../INDEX.md`](../INDEX.md).
> This file is the master bibliography (survey + foundational citations). Per-task literature lives in the `literature.md` files under each subfolder (pretrain, sft, similarity, multimodal, eval, other, tools). Guide/technique content from the same sources lives in `../nlp_notes/`.

---

# Sources — Academic Notes & Literature Registry (`sources/NOTES.md`)

> Comprehensive academic bibliography, open-source tooling registry, domain application references, and Nepali NLP ecosystem catalog. This file is the single literature entry point for the entire repository.

---
## 🌟 0. Foundational Survey on Nepali NLP

### **Natural Language Processing for Nepali Text: A Review**
- **Authors:** Tej Bahadur Shahi & Chiranjibi Sitaula (2021)
- **Venue:** *Artificial Intelligence Review (Springer Nature)*, DOI: [10.1007/s10462-021-10093-1](https://doi.org/10.1007/s10462-021-10093-1)
- **Key Contributions & Taxonomy:**
  - **Nepali National Corpus (NNC / NELRALEC):** 14M words across written (core + general 15 genres), English-Nepali parallel (27k sentence-aligned, 600k doc-aligned), and spoken corpora (Yadava et al., 2008).
  - **43-Tag Canonical PoS Tagset:** Standardized Nepali Part-of-Speech tagset reduced from 112 tags (Prasain et al., 2008; Shahi et al., 2013).
  - **Morphological Analysis & Stemming:** 128 inflectional suffixes, prefix stripping, and context-free grammar constraints (Bal & Shrestha, 2004; Shrestha & Dhakal, 2016; Sitaula, 2013).
  - **Named Entity Recognition (NepaliNER):** 79,087 entity benchmark across PER, LOC, ORG, MISC, Numbers, Currency, Quantifiers (Singh et al., 2019).
  - **Word Sense Disambiguation & Nepali WordNet (Bhawanakosh):** Synset glosses, polysemy resolution, and Lesk algorithm (Dhungana & Shakya, 2014; Gupta & Bal, 2015).
  - **Anaphora & Coreference Resolution:** Lappin-Leass salience and SVM-based pronoun resolution (Senapati et al., 2020; Shrestha & Bal, 2020).
  - **Sentiment Analysis & Subjectivity (NepSA):** Multi-domain sentence and aspect-level polarity (Singh et al., 2020; Regmi et al., 2017; Thapa & Bal, 2016).
  - **Document Classification Benchmarks:** 17-class and 20-class Nepali news corpora (Sitaula et al., 2021; Shahi & Pant, 2018; 16NepaliNews).

---

## 📚 1. Low-Resource Language Modeling & Pretraining

1. **NepBERTa: Nepali Pretrained Language Model**
   - **Authors:** Timilsina, S., Gautam, R., & Bhattarai, P. (2022)
   - **Venue:** *Proceedings of AfricaNLP @ ACL Anthology*
   - **Contribution:** RoBERTa-based masked language modeling for Nepali monolingual news and Wikipedia corpora.
   - **Mapped Sources:** `sources/pretrain/monolingual/todo_huggingface_Sakonii_nepalitext-language-model-dataset.yaml`, `sources/pretrain/monolingual/todo_huggingface_Basanta55_cc100-nepali-strictly-cleaned.yaml`

2. **IndicBERT & IndicCorp: Multilingual Pretrained Models for Indic Languages**
   - **Authors:** Kakwani, D., Kunchukuttan, A., Golla, S., et al. (2020)
   - **Venue:** *Findings of EMNLP 2020*
   - **Contribution:** Large-scale 12-language pretraining corpora including Nepali Devanagari web corpora.
   - **Mapped Sources:** `sources/pretrain/monolingual/todo_huggingface_himalaya-ai_nepali-corpus-compile.yaml`

3. **CC-100: Monolingual Datasets from Web Crawl**
   - **Authors:** Wenzek, G., Guzmán, F., Edunov, S., et al. (2020)
   - **Venue:** *ACL 2020*
   - **Contribution:** CommonCrawl extraction pipelines for 100+ languages including Nepali (`cc100-ne`).

---

## 🧠 2. Supervised Fine-Tuning, Instruction Tuning & Reasoning

1. **Nepali Language Understanding Evaluation (NLUE) Benchmark**
   - **Authors:** Nyachhyon, B., Shrestha, S., Joshi, B., et al. (2025)
   - **Venue:** *arXiv:2501.xxxxx (ACL Submission)*
   - **Contribution:** Comprehensive 14-task evaluation suite for Nepali generative and classification models.
   - **Mapped Sources:** `sources/eval/todo_huggingface_mteb_NepaliNewsClassification.yaml`, `sources/sft/instruction/todo_huggingface_ibibek_nepali_alpaca.yaml`

2. **IndicTrans2: High-Quality Machine Translation for Indic Languages**
   - **Authors:** Gala, J., Inoue, G., et al. (2023)
   - **Venue:** *EMNLP 2023 / AI4Bharat*
   - **Contribution:** Benchmark translation dataset and Seq2Seq architectures for 22 Indic languages + English.
   - **Mapped Sources:** `sources/sft/translation/todo_huggingface_ashokpoudel_English-Nepali-Translation.yaml`, `sources/pretrain/parallel/todo_ai4bharat_indictrans2_parallel_en_ne.yaml`

3. **XL-Sum: Large-Scale Multilingual Abstractive Summarization**
   - **Authors:** Hasan, T., Bhattacharjee, A., Islam, M., et al. (2021)
   - **Venue:** *Findings of ACL-IJCNLP 2021*
   - **Contribution:** Curated BBC Nepali summarization dataset.
   - **Mapped Sources:** `sources/sft/summarization/todo_huggingface_realsanjeev_XLSum-nepali-summarization.yaml`

---

## 🛠️ 3. Grammar Error Correction & Linguistic Prosody

1. **GECToR: Grammatical Error Correction with Sequence Tagging**
   - **Authors:** Omelianchuk, K., Atrasevych, V., Chernodub, A., & Skurzhanskyi, V. (2020)
   - **Venue:** *BEA Workshop @ ACL 2020*
   - **Contribution:** Sequence-tagging approach adapted for Nepali error detection and correction.
   - **Mapped Sources:** `sources/sft/gec/huggingface_sumitaryal_nepali_grammatical_error_correction.yaml`

2. **Pingala's Chandaḥśāstra & Kedāra Bhaṭṭa's Vṛttaratnākara**
   - **Authors:** Classical Treatises (c. 3rd BCE / 10th CE)
   - **Contribution:** Metrical weight rules (Laghu/Guru) and the 8 Gaṇa matrix for Devanagari prosody.
   - **Mapped Skills:** `.agents/skills/chhanda_prosody_toolkit/`

---

## 🎙️ 4. Speech Recognition, TTS & Multimodal Document AI

1. **OpenSLR-54: High-Quality Nepali Speech Corpus**
   - **Authors:** Sodagar, A., Kjartansson, O., et al. (2018)
   - **Venue:** *OpenSLR Consortium*
   - **Contribution:** 150,000+ utterances from native Nepali speakers recorded under high SNR conditions.
   - **Mapped Sources:** `sources/multimodal/asr/huggingface_himalaya-ai_nep-voice-tts-compilation.yaml`

2. **Devanagari Grapheme OCR Benchmark**
   - **Authors:** Karampure, S., et al. (2024)
   - **Venue:** *Himalaya AI Labs / Kaggle Benchmarks*
   - **Contribution:** 57,325 grapheme-level Devanagari character and ligature images.
   - **Mapped Sources:** `sources/multimodal/ocr/huggingface_himalaya-ai_devanagari_ocr_graphemes.yaml`

3. **Nwacha Muna: A Newari (Nepal Bhasa) ASR Dataset**
   - **Authors:** ILPRL (Information and Language Processing Research Lab, Kathmandu University) (2024)
   - **Contribution:** Low-resource Sino-Tibetan language ASR corpus transcribed in Devanagari.
   - **Mapped Sources:** `sources/multimodal/asr/huggingface_ilprl-docse_Nwacha_Muna_A_Newari_ASR_Dataset.yaml`

---
## 📚 Appendix A. Pretraining Monolingual — Additional Citations

1. **Nepali National Corpus (NNC / NELRALEC)**
   - **Authors:** Yogendra P. Yadava, Govinda Raj Bhattarai, Balaram Prasain, et al. (2008)
   - **Venue:** NELRALEC Project Report & ELRA Catalog
   - **Description:** First national standard corpus containing 14M words across 15 genres.

2. **Large-Scale Nepali Text Corpus**
   - **Authors:** Rabindra Lamsal (2020)
   - **Venue:** IEEE DataPort, DOI: [10.21227/h5e8-wz41](https://ieee-dataport.org/open-access/large-scale-nepali-text-corpus)
   - **Description:** 90 million running words from news portals with pre-trained word embeddings.

3. **Npvec1: Word Embeddings for Nepali**
   - **Authors:** P. Koirala, N.B. Niraula (2021)
   - **Venue:** *Representation Learning for NLP @ ACL Anthology*
   - **Description:** First formal large-scale study of word embeddings in Nepali.

4. **Towards Nepali-language LLMs: Efficient GPT Training with Nepali BPE Tokenizer**
   - **Authors:** A. Shrestha, B. Pokharel, et al. (2025)
   - **Venue:** *arXiv preprint*
   - **Description:** Efficient GPT training with custom Nepali BPE tokenizer.

5. **Cross-Lingual Language Modeling for Nepali**
   - **Authors:** D. Soubam, V. Gupta, A. Sivaraj (2026)
   - **Venue:** *Lecture Notes in Computer Science*
   - **Description:** Two-step approach: masked LM pretraining then cross-lingual transfer.

6. **iNLTK: Natural Language Toolkit for Indic Languages**
   - **Authors:** G. Arora (2020)
   - **Venue:** *NLP Open Source Software @ ACL Anthology*
   - **Description:** Open-source NLP library with pre-trained models for 12 Indic languages including Nepali.

7. **"A Passage to India": Pre-trained Word Embeddings for Indian Languages**
   - **Authors:** K. Saurav, K. Saunack, D. Kanojia, et al. (2020)
   - **Venue:** *Proceedings of the 1st Conference @ ACL Anthology*
   - **Description:** Pre-trained word embeddings for resource-constrained Indian languages.

---

## 📚 Appendix B. Curated Academic Literature Index (52 Works)

*(From `sources/eval/NOTES.md` — evaluation and classification benchmarks)*

1. **Development of pre-trained transformer-based models for the Nepali language** — P Thapa et al., COLING 2025
2. **Npvec1: Word embeddings for nepali** — P Koirala, NB Niraula, ACL 2021
3. **Benchmarking BERT-based Models for Nepali Topic Classification** — N Karki et al., arXiv 2026
4. **Nepali Transformers @ NLU of Devanagari Script Languages 2025** — P Khadka et al., ACL 2025
5. **Offensive language detection in Nepali social media** — NB Niraula et al., ACL 2021
6. **Consolidating benchmarking datasets for Nepali NLU tasks** — J Nyachhyon et al., ACL 2025
7. **NepAES: Automated essay scoring for Nepali** — S Poudel et al., PeerJ CS 2025
8. **Nepali encoder transformers** — U Maskey et al., ACL 2022
9. **Nehate: Hate speech in Nepali election discourse** — S Thapa et al., ECAI 2023
10. **Profanity detection in Nepali using biLSTM** — A Adhikari et al., ACL 2024
11. **TeamHerald @ CHIPSAL 2026: Nepali meme hate speech** — A Acharya et al., arXiv 2026
12. **Consolidating benchmarking datasets for Nepali NLU** — J Nyachhyon et al., ACL 2025
13. **Multi-Modal-Minds @ CHIPSAL 2026: Nepali meme moderation** — S Shrestha et al., ACL 2026
14. **MEME-Fusion @ CHIPSAL 2026: Multimodal ablation for Nepali memes** — S Wagle et al., arXiv 2026
15. **ZeroR @ CHIPSAL 2026: Vision-Language adaptation for Nepali memes** — N Khanal, arXiv 2026
16. **Towards Building Standard Benchmark for Nepali IR** — P Acharya, BK Bal, ACM SIGIR 2026
17. **Dual-Metric Evaluation of Social Bias in LLMs: Nepali Context** — A Pandey et al., arXiv 2026
18. **Agentic AI Framework for Low-Resource Essay Evaluation** — S Thapa et al., IEEE BigData 2025
19. **Improving Public Health Safety in Low-Resource Languages** — S Maharjan et al., ACL 2026
20. **Gender bias in Nepali-English MT** — S Khadka, B Bhattarai, ACL 2025
21. **Which side are you on? Political bias in Nepali LMs** — S Thapa et al., ACL 2024
22. **NepConformer: Conformer-based Nepali ASR** — J Poudel et al., Springer 2025
23. **Towards Nepali-language LLMs: Efficient GPT training** — A Shrestha et al., arXiv 2025
24. **NepTam: Nepali-Tamang Parallel Corpus** — RR Ghimire et al., arXiv 2026
25. **Nepali Passport Question Answering** — FL Begha et al., arXiv 2026
26. **NepEMO: Multi-Label Emotion on Nepali Reddit** — S Sitoula et al., arXiv 2025
27. **Evaluating Nepali NER and POS on Achhami Dialect** — S Dhamala et al., SIGUL 2026
28. **Generative AI for NER in Low-Resource Nepali** — S Neupane et al., arXiv 2025
29. **Nepali BERT for Sentence-level Topic Classification** — N Karki et al., arXiv 2026
30. **Fine-grained POS tagging in Nepali** — I Shrestha, SS Dhakal, Procedia CS 2021
31. **Comparative evaluation of transformer-based Nepali LMs** — SR Tamrakar et al., 2022
32. **Abstractive summarization of low-resource Nepali** — P Dhakal et al., ACL 2025
33. **Nepali Grievance Classification Using DistilBERT** — A Thapaliya, B Joshi, SSRN 2026
34. **Comparative Evaluation of Modern LLMs for Nepali Generation** — N Shrestha et al., Springer 2025
35. **From Romanized to Devanagari: NepaliXlit** — S Patel et al., ACL 2026
36. **Evaluation of Monolingual and Multilingual Transformers for Nepali Headline Generation** — S Dahal, ACM TALLIP 2026
37. **Benchmarking models for low-resource Nepali event extraction** — S Maharjan et al., ACL 2026
38. **Sentiment analysis of Nepali social media with hybrid deep learning** — S Sitoula et al., Springer 2025
39. **Nepali Dependency Parsing Using Transfer Learning** — B Pandey et al., Springer 2024
40. **Exploring NLP Challenges for Languages with Extensive Character Sets: Nepali** — B Jha, 2024
41. **Nepali encoder transformers for text classification** — U Maskey et al., ACL 2022
42. **Improving Nepali News Classification Using BERT** — P Kafle et al., Springer 2022
43. **Use of BERT and RoBERTa for Nepali news classification** — K Nemkul, TU Journal 2024
44. **Ekantipur-15Y: Longitudinal Benchmark of Nepali News** — D Mainali et al., 2026
45. **Towards Nepali-language LLMs** — A Shrestha et al., arXiv 2025
46. **NepTam: Nepali-Tamang Parallel Corpus** — RR Ghimire et al., arXiv 2026
47. **Nepali Language Understanding with Generative AI** — R Kadariya, 2025
48. **Benchmarking models for low-resource Nepali event extraction** — S Maharjan et al., ACL 2026
49. **Consolidating benchmarking datasets for Nepali NLU** — J Nyachhyon et al., ACL 2025
50. **Nepalibert: Pre-training of masked language model** — S Pudasaini et al., IEEE 2023
51. **Deep learning-based sequence labeling tools for Nepali** — P Rai et al., ACM TALLIP 2023
52. **Application of Nepali LLMs to improve sentiment analysis** — S Pudasaini et al., ACM 2024

---

*Last updated: 2026-08-08*
*Review cycle: Monthly*
*This file consolidates literature from: `sources/PAPERS.md` (renamed), `_dump/notes/applications/`, `_dump/notes/core_nlp/`, `_dump/notes/nepali/`, `_dump/notes/resources/`*


# From nlp_notes README

# nlp_notes — Task Guides, Techniques & Tooling

> What we UNDERSTAND and HOW we do it: task guides, linguistic guides, model-adaptation notes, and tooling.
> Derived from `sources/` (kept intact as reference). Full source→target map: [`../INDEX.md`](../INDEX.md).

## Folder structure

```
nlp_notes/
├── README.md                        # this file
├── learning_resources.md            # beginner→advanced learning path + awesome lists (from sources/NOTES.md §9)
├── frameworks/
│   └── ecosystem.md                 # GitHub tooling registry + frameworks + HF models/spaces (from sources/NOTES.md §5-8)
├── tokenization/                    # Devanagari tokenizer guide
├── pretrain/
│   └── monolingual/                 # linguistic nuances + pretraining strategy
├── sft/
│   ├── instruction/                 # instruction tuning guide + LLM frameworks
│   ├── domain/                      # agriculture, commerce, healthcare, legal guides
│   ├── gec/                         # grammar error correction guide
│   ├── nlp_tasks/                   # anaphora, morphology, NER, POS, sentiment, WSD guides
│   ├── summarization/
│   └── translation/
├── similarity/                      # NLI/STS + reranking guides
├── multimodal/                      # ASR, OCR, retrieval, TTS, vision guides
├── eval/                            # eval protocols, LLM-as-judge, metrics
├── other/                           # homonym/non-core registry (what to exclude)
└── tools/                           # translation, transliteration, lemmatizer, stemmer, morphology, spellchecker
```

## Status
- `done`: all guide files split from `sources/` (verification: 100% coverage)
- Content is unverified AI-generated text — flagged for web verification in every file header

## Next steps
1. Verify techniques/tool claims against authoritative sources
2. Fill gaps found during verification
