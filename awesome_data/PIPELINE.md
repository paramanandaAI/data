# Data Ingestion & Transformation Pipeline

How dataset contracts move from YAML specification $\rightarrow$ canonical JSONL export.

---

## The Minimal Ingestion Workflow

```
sources/<id>.yaml (or awesome_data/Nepali_data/<cat>/<id>.yaml)
      │
      ▼  nepalinlplibrary.dataloader
  raw rows (HF API, web, or parquet)
      │
      ▼  DatasetSpec.validate_record()
  canonical JSONL records (in-memory)
      │
      ▼  CatalogManager & CLI
  written to catalog.jsonl
  catalog.jsonl entry created (status: pending)
      │
      ▼  HUMAN REVIEW GATE
  catalog.jsonl entry updated (status: approved)
```

---

## Dataset Ingestion Status Lifecycle

```
pending → reviewed → approved → in_training
              ↓
           rejected
```

- **`pending`**: Ingested by agent, awaiting human review.
- **`reviewed`**: Sample rows checked and relevance score assigned.
- **`approved`**: Human cleared dataset for training/evaluation inclusion.
- **`rejected`**: Human marked dataset as unsuitable.
- **`in_training`**: Dataset exported to model training run.

> **Rule**: Agents only set `pending` status. Human review approves or rejects datasets.
