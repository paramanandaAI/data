# Declarative Data Sources Catalog (`sources/`)

This directory contains declarative dataset contracts (`*.yaml`), task-specific architectural guides (`NOTES.md`), and comprehensive literature surveys (`NOTES.md`).

---

## 🏗️ Directory Hierarchy

```tree
sources/
├── pretrain/                          # Unsupervised monolingual & parallel pretraining corpora
│   ├── monolingual/                   # CC-100, OSCAR, Nepali Wikipedia, News 0.8B tokens
│   └── parallel/                      # IndicTrans2, OPUS, Samanantar English-Nepali pairs
├── sft/                               # Supervised Fine-Tuning datasets & task guides
│   ├── domain/                        # Legal, healthcare, agriculture, commerce, crisis & governance
│   ├── gec/                           # Grammatical error correction & spelling validation
│   ├── instruction/                   # Nepali Alpaca, Hermes tool-calling, multi-turn QA
│   ├── nlp_tasks/                     # NER, POS, WSD, anaphora, idioms, dependency parsing
│   │   ├── dependency_parsing/        # Universal Dependencies (UD Nepali) treebank
│   │   ├── idioms_figurative/         # NeDIOM Nepali idioms & figurative expressions
│   │   ├── morphology/                # 128-suffix stripping, CFG inflections
│   │   ├── ner/                       # Indian/Nepali NER benchmarks & DanfeNER
│   │   ├── pos/                       # 43-tag canonical Nepali morphosyntax
│   │   ├── sentiment/                 # SentiWordNet, Aspect-based polarity, Nepali Reddit
│   │   ├── structured_output/         # JSON Schema, SPARQL Wikidata extraction
│   │   └── wsd/                       # Verb frames & IndoWordNet synsets
│   ├── summarization/                 # XL-Sum BBC Nepali abstractive summarization
│   └── translation/                   # English-Nepali, Tamang-Nepali, Romanized-Devanagari
├── similarity/                        # Bi-encoder STS & Cross-Encoder reranking
├── multimodal/                        # ASR (Whisper), TTS, OCR (Manuscripts), Vision (Captions), Sign Language
├── eval/                              # NLUE benchmark, Hate speech, Meme sentiment, Fake news
├── other/                             # Non-NLP domain justifications & homonym registry
└── NOTES.md                           # Master bibliography (1,000+ academic papers)
```

---

## ⚡ Ecosystem Tooling & Modern NLP Architecture
For complete mapping between classic NLP components (spaCy, SetFit, SpanMarker, KeyBERT, Presidio) and Hugging Face pipelines for Nepali, consult:
- [**Modern NLP & Hugging Face Ecosystem Guide**](file:///d:/linguistic_adaptation/.agents/skills/nepali_linguistic_toolkit/references/guides/modern_nlp_spacy_hf_ecosystem.md)
- [**Master Academic Bibliography**](file:///d:/linguistic_adaptation/sources/NOTES.md)

### Data Operations Frameworks

#### Annotation & Augmentation
| Repository | Focus |
|---|---|
| [`flairNLP/flair`](https://github.com/flairNLP/flair) | State-of-the-art NLP framework for sequence labeling and classification |
| [`jasonwei20/eda_nlp`](https://github.com/jasonwei20/eda_nlp) | Data augmentation for NLP (EMNLP 2019) |
| [`QData/TextAttack`](https://github.com/QData/TextAttack) | Adversarial attacks, data augmentation, and model training for NLP |
| [`argilla-io/argilla`](https://github.com/argilla-io/argilla) | Collaboration tool for building high-quality datasets |
| [`code-kern-ai/refinery`](https://github.com/code-kern-ai/refinery) | The data scientist's open-source choice to scale and maintain NLP data |

#### Corpus Collection & Crawling
| Repository | Focus |
|---|---|
| [`adbar/trafilatura`](https://github.com/adbar/trafilatura) | Web crawling, scraping, and text extraction — CSV, JSON, HTML, MD, XML |
| [`huggingface/datasets`](https://github.com/huggingface/datasets) | Largest hub of ready-to-use datasets for AI models |
| [`chiphuyen/lazynlp`](https://github.com/chiphuyen/lazynlp) | Library to scrape and clean web pages to create massive datasets |
| [`ChenghaoMou/text-dedup`](https://github.com/ChenghaoMou/text-dedup) | All-in-one text de-duplication toolkit |

#### Safety & Privacy
| Repository | Focus |
|---|---|
| [`data-privacy-stack/presidio`](https://github.com/data-privacy-stack/presidio) | Open-source PII detection, redaction, masking, and anonymization |
| [`unitaryai/detoxify`](https://github.com/unitaryai/detoxify) | Toxic comment prediction — Jigsaw challenges |
| [`thunlp/OpenAttack`](https://github.com/thunlp/OpenAttack) | Open-source package for textual adversarial attack |
| [`makcedward/nlpaug`](https://github.com/makcedward/nlpaug) | Data augmentation for NLP |
