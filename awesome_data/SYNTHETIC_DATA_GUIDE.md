# Synthetic Data Generation Guide

## Overview

This guide covers generating training data for Nepali NLP models using:
1. **CLI Tool** (`generate.py`) - for synthetic data generation
2. **Combine Pipeline** (`combine_dataset.py`) - for merging datasets
3. **Reference Data** - existing datasets that need formatting

---

## CLI Tool: `generate.py`

### Location
```
D:\paramananda\_inspirations\generate.py
```

### Available Tasks

| Task | Command | Description |
|------|---------|-------------|
| Spelling | `--task spelling` | Nepali spelling correction pairs |
| Transliteration | `--task transliteration` | Roman → Devanagari conversion |
| QA | `--task qa` | General knowledge Q&A |
| Agriculture | `--task agriculture` | Agriculture domain Q&A |
| Summarization | `--task summarization` | Text summarization pairs |
| NER | `--task ner` | Named entity recognition |
| Sentiment | `--task sentiment` | Sentiment analysis |
| Translation | `--task translation` | English → Nepali translation |

### Usage Examples

```bash
# Generate 50 spelling correction samples
python _inspirations/generate.py --task spelling --count 50

# Generate 100 transliteration samples
python _inspirations/generate.py --task transliteration --count 100

# Generate with reference samples (few-shot)
python _inspirations/generate.py --task qa --count 50 --ref-file _inspirations/synthetic/spellingdata/sample.jsonl

# Custom system prompt
python _inspirations/generate.py --task custom --template "तपाईं एक कृषि विशेषज्ञ हुनुहुन्छ..." --count 30

# Use different model
python _inspirations/generate.py --task spelling --count 50 --model gpt-4o

# List available tasks
python _inspirations/generate.py --list-tasks
```

### Output Format

All generated data uses OpenAI Chat format:
```json
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "source": "synthetic_spelling_v2",
  "metadata": {
    "source": "synthetic_spelling_v2",
    "category": "spelling_correction",
    "_generated_at": "2026-08-02T..."
  }
}
```

---

## Combine Pipeline: `combine_dataset.py`

### Location
```
D:\paramananda\_inspirations\combine_dataset.py
```

### Usage

```bash
# Combine all datasets from _inspirations folder
python _inspirations/combine_dataset.py --input_dir _inspirations --output_file combined/all_data.jsonl

# Combine with source enforcement
python _inspirations/combine_dataset.py --input_dir _inspirations --enforce-source

# Combine specific folder
python _inspirations/combine_dataset.py --input_dir _inspirations/synthetic --output_file combined/synthetic_data.jsonl
```

### Features
- Automatic source tracking
- Deduplication (SHA-256 hash)
- Schema validation
- Metadata injection

---

## Data Sources Available

### ASR Data (Needs Formatting)
- **OpenSLR-54**: `openslr.org/54` - 157K utterances
- **Mozilla Common Voice**: `commonvoice.mozilla.org` - 100K+ clips
- **Status**: Data exists, format to instruction pairs

### NLU Data (Ready)
- **EverestNER**: 50K+ sentences
- **NLUE Benchmark**: 9 classification tasks
- **Status**: Ready to format

### MT Data (Ready)
- **KU EN-NE Corpus**: 1.8M sentence pairs
- **NepTam**: Nepali-Tamang parallel
- **Status**: Ready to format

### TTS Data (Needs Formatting)
- **Transformer TTS**: Text-phoneme pairs
- **Status**: Data exists, format to instruction pairs

---

## Workflow

### Step 1: Generate Synthetic Data
```bash
python _inspirations/generate.py --task spelling --count 500
python _inspirations/generate.py --task transliteration --count 500
python _inspirations/generate.py --task qa --count 200
```

### Step 2: Format Existing Data
```bash
# ASR data
python _inspirations/generate.py --task asr --ref-file /path/to/openslr54.jsonl --count 1000

# NER data
python _inspirations/generate.py --task ner --ref-file /path/to/everestner.jsonl --count 500
```

### Step 3: Combine All
```bash
python _inspirations/combine_dataset.py --input_dir _inspirations --output_file combined/final_dataset.jsonl
```

### Step 4: Train Model
```python
from datasets import load_dataset
from trl import SFTTrainer

dataset = load_dataset("json", data_files="combined/final_dataset.jsonl", split="train")
# ... training code
```

---

## Cross-References

- [[bal_eval_framework]] - Evaluation framework
- [[dr_bal_krishna_bal_paper_tasks]] - Bal's paper tasks
- [[dr_balaram_prasain_paper_tasks]] - Prasain's paper tasks
- [[papers_list]] - Full bibliography
