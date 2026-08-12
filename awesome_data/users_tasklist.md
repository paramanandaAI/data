# User Task List

## Current Focus: Word Complexity Classification (Gemma)

---

## Word Types

| Type | Nepali | Description | Example |
|------|--------|-------------|---------|
| simple | सरल | Single morpheme | घर, कलम, पानी |
| complex | जटिल | Root + suffix/postposition | घरबाट, घरमा |
| compound | संयुक्त | Two+ roots combined | घरपरिवार, काठमाडौँ |
| reduplication | द्विरुक्ति | Repeated morphemes | घरघरै, सानासाना |

### Rules
- Never classify 'complex' and 'compound' together
- Never classify 'complex' and 'reduplication' together
- A word can only be ONE type

---

## Created Files

| File | Description | Status |
|------|-------------|--------|
| `dataset/word_complexity_instructions.jsonl` | 20 grounded instruction examples | DONE |
| `_inspirations/config.yaml` | Config with word types, prompts, seeds | DONE |
| `_inspirations/generate.py` | CLI tool (Gemma focused) | DONE |

---

## Pending Tasks

### Priority 1: Use Grounded Data
- [ ] Load `dataset/word_complexity_instructions.jsonl` as reference
- [ ] Generate more examples using these as few-shot

### Priority 2: Generate Gemma Data
- [ ] Run `python generate.py --format gemma`
- [ ] Verify thinking content quality
- [ ] Check Nepali prompt accuracy

### Priority 3: Expand Dataset
- [ ] Add more seed words per type
- [ ] Generate with different models
- [ ] Add edge cases (ambiguous words)

### Priority 4: Validation
- [ ] Run `python generate.py --validate combined/gemma_train.jsonl`
- [ ] Check label distribution
- [ ] Remove duplicates

### Priority 5: Combine
- [ ] Run `python generate.py --combine`

---

## Quick Commands

```bash
# Generate Gemma data
python generate.py --format gemma

# List word types
python generate.py --list-types

# List seed words
python generate.py --list-words

# Validate
python generate.py --validate combined/gemma_train.jsonl

# Combine
python generate.py --combine
```

---

## Notes

- Skip BERT, Gemma only
- Combined will be made at once
- Focus on word complexity classification
- Prompts must be in Nepali

---

## Cross-References

- [[bal_eval_framework]] - Evaluation framework
- [[dataset_schema]] - Config and schema
- [[dr_balaram_prasain_paper_tasks]] - Prasain's papers
