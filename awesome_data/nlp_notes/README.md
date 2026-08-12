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
