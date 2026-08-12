> Source: `sources/pretrain/tokenization/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Tokenization: Devanagari-Focused Tokenizers for Nepali


---

## 🇳🇵 Tokenization Challenges for Nepali

### Devanagari Script
- **Complex conjuncts:** Multiple consonants combine (e.g., क्ष, त्र, ज्ञ)
- **Matras (vowel signs):** Attach to consonants (ा, ि, ु, े, ो)
- **Nukta:** Diacritical marks (क़, ख़, ग़)
- **Word boundaries:** Spaces may not indicate word boundaries clearly

### English Layout Issue
- **$$ nepali using english layout** — Nepali text typed with English keyboard layout
- **Autocorrect errors:** Grammar mistakes from predictive text
- **Token inefficiency:** More tokens for Nepali vs English

### Token Count Problem
- **$$ small mistakes in nepali would take more tokens** — misspellings increase token count
- **$$ supposing if tokenizer used is devnagari focused** — Devanagari-focused tokenizer reduces tokens
- **$$ tokenizer retraining or pretrained model or extension needed** — need Nepali-optimized tokenizer

---

## 🔧 Tokenizer Training Methods

### SentencePiece (BPE)
- **Method:** Byte Pair Encoding on raw text
- **Vocabulary:** Configurable (8K–32K tokens)
- **Languages:** Language-agnostic (works on raw Unicode)
- **Use case:** Train on Nepali corpus

### SentencePiece (Unigram)
- **Method:** Unigram language model
- **Vocabulary:** Probabilistic selection
- **Languages:** Language-agnostic
- **Use case:** Alternative to BPE

### WordPiece
- **Method:** Greedy longest-match-first
- **Languages:** Used in BERT models
- **Use case:** Fine-tune existing multilingual tokenizer

---

## 📊 Tokenizer Comparison

| Tokenizer | Method | Vocab Size | Nepali Tokens | English Tokens |
|---|---|---|---|---|
| Standard BPE | Byte-level BPE | 32K | High | Low |
| SentencePiece BPE | Character-level BPE | 32K | Medium | Medium |
| Nepali-trained BPE | BPE on Nepali | 32K | Low | Medium |
| Multilingual BPE | BPE on 100+ langs | 250K | Medium | Low |

### Key Metric: Compression Ratio
- **English:** ~1.3 tokens per word (efficient)
- **Nepali (standard tokenizer):** ~2.5 tokens per word (inefficient)
- **Nepali (trained tokenizer):** ~1.5 tokens per word (improved)

---

## 🛠️ Implementation Plan

### 1. Collect Nepali Corpus
- Nepali Wikipedia
- Nepali news articles
- Nepali books (if available)
- Mixed domain text

### 2. Train Tokenizer
- Use SentencePiece BPE
- Vocab size: 16K–32K
- Include special tokens: `[PAD]`, `[UNK]`, `[CLS]`, `[SEP]`, `[MASK]`
- Add morphological subwords (root + suffix patterns)

### 3. Evaluate
- Measure token count reduction
- Evaluate downstream task performance
- Compare with multilingual tokenizer

### 4. Extend Existing Models
- Add new tokens to existing vocabulary
- Fine-tune embedding layer
- Test impact on NLU/NLG tasks

---

## 🔗 Cross-References

| Resource | Location | Usage |
|---|---|---|
| Nepali Pretrained | `bal_eval/pretrained_models/` | Model tokenization |
| Tokenizer Frameworks | `sources/pretrain/monolingual/NOTES.md` | Training tools |
| NLP Tools | `sources/tools/NOTES.md` | Preprocessing pipeline |
| IR Benchmark | `bal_eval/ir_information_retrieval/` | Tokenization impact on IR |
