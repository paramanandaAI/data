> Source: `sources/sft/translation/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Machine Translation & Transliteration: Task Guide & Notes

## 🇳🇵 Nepali Linguistic Nuances
1. **SOV Word Order:** Nepali strictly follows Subject-Object-Verb (SOV) sentence order. Direct English SVO transfers produce unnatural phrasing.
2. **Postpositional Attachment:** Prepositions in English (*in, on, with, for*) map to postpositional clitics in Nepali (*मा, माथि, सँग, को लागि*).
3. **Romanized Transliteration Ambiguity:** Roman text (*"khana khaye"* vs *"khaana khaaye"*) maps to standard Devanagari (*"खाना खाएँ"*).

---

## 🤖 Modern Model Adaptation (Gemma 4 & Sentence-BERT)
- **Gemma 4 (Generative Translation & Transliteration):**
  - Unified multi-task prompt:
    `"Translate the following English sentence to natural, grammatically correct Nepali:\n{english_text}"`
- **Sentence-BERT / Bi-Encoder:**
  - Parallel semantic similarity scoring (`cos_sim(embed(ne), embed(en))`) for filtering noisy parallel web crawls.
