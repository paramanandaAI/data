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
