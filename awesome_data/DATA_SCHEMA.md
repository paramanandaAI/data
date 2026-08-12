# Paramananda NLP — Data Schema Specification

Canonical JSONL schemas for every task type in the `data` repository. Every record validated against its task schema enters `catalog.jsonl`.

---

## Universal Required Fields

Every record across every task type MUST have these fields:

```json
{
  "id":       "<task_prefix>-<source_slug>-<zero_padded_index>",
  "source":   "huggingface.co/datasets/<owner>/<name>  OR  doi:...",
  "language": "ne",
  "script":   "Devanagari",
  "task":     "<task_type>",
  "license":  "cc-by-4.0  OR  apache-2.0  OR  mit  OR  open"
}
```

### ID Convention Examples

```
gec-sumitaryal-000001
asr-newari-004575
ocr-himalaya-010000
```

Format: `<task>-<source_slug>-<6-digit-index>`

---

## Schema by Task Type

### 1. `pretrain` — Raw text for language modeling

```json
{
  "id":          "pretrain-newscrawl-000001",
  "source":      "huggingface.co/datasets/cc100/ne",
  "language":    "ne",
  "script":      "Devanagari",
  "task":        "pretrain",
  "license":     "cc-by-4.0",
  "text":        "नेपाल सरकारले आर्थिक वर्ष २०८२/८३ को बजेट सार्वजनिक गर्यो...",
  "domain":      "news",
  "source_type": "web"
}
```

### 2. `sft` — Supervised fine-tuning (instruction-following)

ALL instruction, input, output fields MUST be in Nepali Devanagari.

```json
{
  "id":          "gec-sumitaryal-000001",
  "source":      "huggingface.co/datasets/sumitaryal/nepali_grammatical_error_correction",
  "language":    "ne",
  "script":      "Devanagari",
  "task":        "sft/gec",
  "license":     "cc-by-4.0",
  "instruction": "तलको वाक्यमा व्याकरण सम्बन्धी गल्ती छ भने सुधार गर्नुहोस्।",
  "input":       "उ हिजो बजार जान गो।",
  "output":      "ऊ हिजो बजार गयो।"
}
```

### 3. `multimodal/asr` — Speech recognition (audio → text)

```json
{
  "id":          "asr-newari-000001",
  "source":      "huggingface.co/datasets/ilprl-docse/Nwacha_Muna_A_Newari_ASR_Dataset",
  "language":    "new",
  "script":      "Devanagari",
  "task":        "multimodal/asr",
  "license":     "cc-by-4.0",
  "instruction": "दिइएको श्रव्य सामग्री सुनि त्यसमा भएको वाक्य Devanagari लिपिमा लेख्नुहोस्।",
  "input":       "<audio_ref: utt-0004>",
  "output":      "थ्व थासय् छ्यलिगु मू भाय् तेलुगु भाषा ख",
  "audio": {
    "utterance_id":  "utt-0004",
    "hf_dataset":    "ilprl-docse/Nwacha_Muna_A_Newari_ASR_Dataset",
    "split":         "train",
    "row_index":     4,
    "sampling_rate": 16000,
    "format":        "wav"
  }
}
```

### 4. `multimodal/ocr` — Document OCR (image → text)

```json
{
  "id":          "ocr-himalaya-000001",
  "source":      "huggingface.co/datasets/himalaya-ai/nepalipixel-synthetic-ocr-benchmark",
  "language":    "ne",
  "script":      "Devanagari",
  "task":        "multimodal/ocr",
  "license":     "mit",
  "instruction": "दिइएको कागजात चित्रमा भएको नेपाली पाठ पहिचान गरी लेख्नुहोस्।",
  "input":       "<image_ref: nepali_ocr_0000001>",
  "output":      "यस्तो बेलामा सत्ताको स्वाद पाएका...",
  "image": {
    "id":         "nepali_ocr_0000001",
    "hf_dataset": "himalaya-ai/nepalipixel-synthetic-ocr-benchmark",
    "split":      "train",
    "row_index":  1,
    "font_name":  "Kalimati",
    "level":      "easy",
    "size_px":    32,
    "width":      512,
    "height":     64
  }
}
```

---

## Validation Rules (`nepalinlplibrary.dataloader`)

| Rule | Check |
|------|-------|
| Required fields | `id`, `source`, `language`, `script`, `task`, `license` all present |
| Devanagari ratio | `instruction` + `output` combined must be $\ge 80\%$ Devanagari characters |
| Non-empty output | `output` field non-empty and non-whitespace |
| Unique ID | `id` does not collide within the task layer |
| License present | `license` is a known identifier, not "unknown" |
