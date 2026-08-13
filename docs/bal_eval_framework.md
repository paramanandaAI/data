# BalEval Framework

## Current Status

| Component | Status | Path |
|-----------|--------|------|
| CLI Tool | DONE | `D:\paramananda\baleval\cli.py` |
| Evaluator | DONE (mock) | `D:\paramananda\baleval\evaluator.py` |
| Models Config | DONE | `D:\paramananda\baleval\models_config.py` |
| Dataset Pipeline | DONE | `D:\paramananda\_inspirations\combine_dataset.py` |
| Generate CLI | DONE | `D:\paramananda\_inspirations\generate.py` |

---

## What Exists (Data Available, Needs Formatting)

### ASR Data
- **OpenSLR-54**: 157K utterances, 400+ hours - `openslr.org/54`
- **Mozilla Common Voice Nepali**: 100K+ clips
- **Parliamentary ASR**: 1K+ utterances
- **Status**: Data exists, needs conversion to OpenAI chat format for instruction tuning

### NLU Data
- **EverestNER**: 50K+ sentences, 8 entity types
- **NLUE Benchmark**: 9 classification + 3 structural tasks
- **Status**: Ready, can be formatted

### MT Data
- **KU EN-NE Corpus**: 1.8M sentence pairs
- **NepTam**: Nepali-Tamang parallel corpus
- **Status**: Ready for parallel data tasks

---

## Pending Tasks

### Priority 1: Format ASR Data
- [ ] Convert OpenSLR-54 transcripts to instruction format
- [ ] Create ASR instruction pairs: "Transcribe this audio: [audio_id]" → "Text: [transcript]"
- [ ] Output: `combined/asr_instruction_data.jsonl`

### Priority 2: Format NER Data
- [ ] Convert EverestNER to chat format
- [ ] Create NER instruction pairs
- [ ] Output: `combined/ner_instruction_data.jsonl`

### Priority 3: Format MT Data
- [ ] Convert KU parallel corpus to instruction format
- [ ] Create translation instruction pairs
- [ ] Output: `combined/mt_instruction_data.jsonl`

### Priority 4: Generate Synthetic Data
- [ ] Run `python generate.py --task spelling --count 500`
- [ ] Run `python generate.py --task transliteration --count 500`
- [ ] Run `python generate.py --task qa --count 200`
- [ ] Run `python generate.py --task agriculture --count 200`

### Priority 5: Combine All
- [ ] Run `python combine_dataset.py --input_dir . --output_file combined/final_dataset.jsonl`

---

## Model Training Targets

| Model | Architecture | Use Case | Training Data Needed |
|-------|-------------|----------|---------------------|
| NepaliBERT | BERT-Encoder | POS, NER, Classification | NLU datasets |
| NepaliT5 | T5-EncoderDecoder | Translation, Summarization | Parallel corpus |
| NepaliGemma | Gemma-Decoder | Zero-Shot, CoT, Hybrid | Instruction tuning |

---

## Quick Commands

```bash
# Generate synthetic data
python _inspirations/generate.py --task spelling --count 100
python _inspirations/generate.py --task transliteration --count 100
python _inspirations/generate.py --task qa --count 50

# Combine all datasets
python _inspirations/combine_dataset.py --input_dir _inspirations --output_file combined/all_data.jsonl

# Run BalEval
python baleval/cli.py run --model gemma-27b --mode hybrid
```
