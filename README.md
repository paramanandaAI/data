# Paramananda NLP — Data Repository & Literature Hub (`data`)

The central dataset specification hub, literature review catalog, and verification repository for **Nepali Natural Language Processing (NLP)**.

---

## 📁 Repository Architecture

```tree
data/
├── datasets/                 # 66 categorized YAML dataset contracts
│   ├── pretrain/             # Monolingual & pretraining corpora (monolingual, web)
│   ├── sft/                  # Instruction tuning & task packs (qa, translation, gec, nlp_tasks)
│   ├── eval/                 # Evaluation benchmarks (sentiment, nli, toxicity)
│   ├── multimodal/           # Audio ASR & vision datasets
│   └── similarity/           # Reranking & semantic passage retrieval datasets
│
├── docs/                     # Literature surveys, toxicity review, paper PDFs & dataset indexes
│   ├── bibliography.md       # Master survey review (Shahi & Sitaula 2021 + 52 paper citations)
│   ├── dataset_index.md      # Catalog of 564+ Nepali datasets on HuggingFace
│   ├── local_datasets_index.md # 14 held-out evaluation benchmark parquets (113 MB)
│   ├── toxicity_dataset_review.md # 3-stage synthetic toxicity pair review document
│   ├── workspace_md_index.json # Master index of all 266 markdown files across workspace
│   └── research_method/      # Computer vision & multimodal dataset taxonomy guides
│
├── samples/                  # Representative <5MB data samples
│   ├── text/                 # Sample CSV/JSONL records for raw datasets
│   ├── audio/                # Sample Devanagari ASR audio clips (.wav)
│   └── ocr/                  # Sample Devanagari manuscript OCR images (.jpg)
│
├── scripts/                  # Verification & cataloging tools
│   ├── build_catalog.py      # Re-generates root catalog.jsonl from datasets/
│   ├── check_large_files.py  # Enforces <50 MB git file limits
│   └── index_all_md_files.py # Re-indexes all markdown files across workspace
│
└── catalog.jsonl             # Single master JSONL index of all 66 dataset contracts
```

---

## ⚡ Verification & Catalog Building

```bash
# Rebuild root catalog.jsonl from datasets/
python scripts/build_catalog.py

# Check repository for un-gitignored large files (>50 MB)
python scripts/check_large_files.py

# Re-index all markdown files into docs/workspace_md_index.json
python scripts/index_all_md_files.py
```
