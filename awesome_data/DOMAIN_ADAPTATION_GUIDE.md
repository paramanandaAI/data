# Paramananda

NLU and NLP pretraining and post-training toolkit focused on **domain adaptation**.

---

## What this is

Paramananda is a workspace for building, curating, and finetuning language models
on domain-specific Nepali (and multilingual) data. It covers the full pipeline:

1. **Pretraining** — raw corpora, tokenizers, continued pretraining on domain text.
2. **Post-training** — instruction tuning, alignment, LoRA, full finetuning.
3. **Domain adaptation** — the toolkit exists so that the *user* decides what domain,
   what task, and what format. Paramananda provides the structure and the data infrastructure.

---

## Dataset policy

**The user explicitly specifies the final format.** Paramananda does not assume a
task or a target. The user tells the toolkit what to do with the data.

### JSONL is the only file format

All dataset files inside this workspace must be `.jsonl`. No CSV, no Parquet,
no TXT as final output. Intermediate/conversion scripts may read other formats,
but the output they produce must be JSONL.

### JSONL schema (enforced)

Every JSONL line **must** contain at minimum these fields:

```json
{
  "id": "string — globally unique, stable identifier",
  "instruction": "string — task instruction / prompt",
  "source": "string — input text the model reads",
  "target": "string — expected output / label",
  "category": "string — task category (translation, sentiment, qa, ...)",
  "lang": "string — language tag(s) (ne, ne-en, hi-ne, en, ...)"
}
```

Optional fields:

| Field | Type | Purpose |
|-------|------|---------|
| `cot` | `string` | Chain-of-thought reasoning (for reasoning tasks) |
| `meta` | `object` | Free-form metadata (provenance, split origin, etc.) |

**Enforcement rules:**
- `id` must be unique across all files in the workspace.
- `instruction` and `source` must never be empty.
- `target` may be empty for generation tasks (model generates it).
- `category` must match the task folder name or a registered category.
- `lang` uses ISO 639-1 codes, hyphen-separated for multilingual pairs.

---

## Folder layout

```
D:\paramananda\
├── dataset_test/          — datasets (JSONL only)
│   ├── 00_online_sources/ — raw downloaded data (reference, not training)
│   ├── 01_nlp/            — standard NLP tasks (by task type → category)
│   ├── 02_reasoning_cot/  — chain-of-thought / reasoning tasks
│   ├── 03_eval_heldout/   — held-out eval benchmarks (never for training)
│   ├── 04_templates/      — reusable instruction templates
│   ├── 05_pretraining/    — continued pretraining / domain adaptation
│   ├── 06_retrieval/      — information retrieval tasks and benchmarks
│   └── scripts/           — conversion and mapping scripts
└── README.md              — this file
```

---

## How to add a dataset

1. Place raw source files in `dataset_test/00_online_sources/<source_name>/`.
2. Write a conversion script (in `scripts/` or next to the source) that reads
   the raw format and outputs JSONL following the schema above.
3. Output JSONL goes into the appropriate task folder:
   - Standard NLP tasks → `01_nlp/<type>/<category>/`
   - Reasoning tasks → `02_reasoning_cot/<type>/`
   - Eval-only tasks → `03_eval_heldout/<benchmark>/`
4. Add a `README.md` in the task folder describing the data, source, and splits.
5. Never put training data in `03_eval_heldout/`. Never put eval data in training folders.

---

## Conventions

- **Splits:** `train.jsonl`, `dev.jsonl`, `test.jsonl` — written inside the task folder.
- **Naming:** lowercase, underscores, no spaces in folder or file names.
- **Language:** Nepali content uses Devanagari. Roman Nepali is marked `lang: ne-roman`.
- **Scripts:** each conversion script should print row counts and be reproducible (fixed seed).
- **Licenses:** record the license in the source's `README.md` inside `00_online_sources/`.

---

## Credits

Built by the Paramananda team. See individual dataset READMEs for specific
attribution (e.g., Aadash Pandit, Ishan, Yudin Khanal for Hindi-Nepali work).
