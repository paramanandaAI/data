> Source: `sources/sft/nlp_tasks/ner/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Named Entity Recognition (NER): Task Guide & Notes

## 🇳🇵 Devanagari NER Challenges
1. **Lack of Capitalization:** Unlike Latin scripts, Devanagari does not have uppercase letters to signal proper nouns (*राम* vs *राम्रो*).
2. **Agglutinated Entity Boundaries:** Clitics attach directly to names (*काठमाडौँमा* = Kathmandu + in). NER taggers must separate the base entity span from the case marker.

---

## 🤖 Modern Model Adaptation (Sentence-BERT & Gemma 4)
- **Nepali BERT (Token Classification):**
  - Standard subword BIO tagging (`B-PER`, `I-PER`, `B-LOC`, `I-LOC`, `B-ORG`, `I-ORG`, `O`).
- **Gemma 4 (Generative Extraction):**
  - Prompt: `"तल दिइएको वाक्यबाट व्यक्ति (PER), स्थान (LOC), र संस्था (ORG) हरू JSON सूचीमा निकाल्नुहोस्:\n{text}"`
