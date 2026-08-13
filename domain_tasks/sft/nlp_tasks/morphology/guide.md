> Source: `sources/sft/nlp_tasks/morphology/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Morphological Analysis & Stemming: Task Guide & Notes

## 🇳🇵 Nepali Morphology Rules
1. **Inflectional vs Derivational Affixes:**
   - Case inflections: *घर + मा + बाट = घरबाट* (from home).
   - Plural inflections: *किताब + हरू = किताबहरू*.
   - Derivational prefixes: *प्र-, वि-, अ-, कु-, दुर्-*.
2. **Over-Stemming Prevention:** Pure suffix stripping often strips valid root stems (*हात -> हा*). CFG dictionary checks are required.

---

## 🤖 Modern Model Adaptation (Sentence-BERT & Gemma 4)
- **Sentence-BERT / Subword Tokenizer (Byte-Pair Encoding):**
  - Unsupervised morph segmentation preserving Sanskrit sandhi and Nepali compound morphemes.
- **Gemma 4 (Lemma & Root Extraction):**
  - Prompt: `"तल दिइएको शब्दको मूल धातु / शब्द (root lemma) र प्रत्यय छुट्याउनुहोस्:\nशब्द: {word}"`
