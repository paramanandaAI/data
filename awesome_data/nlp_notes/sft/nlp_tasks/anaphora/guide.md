> Source: `sources/sft/nlp_tasks/anaphora/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Anaphora & Coreference Resolution: Task Guide & Notes

## 🇳🇵 Nepali Pronominal Reference & Agreement
1. **Third-Person Pronoun Hierarchy:**
   - Proximate: *यो (Singular), यी / यिनीहरू (Plural)*.
   - Distant: *त्यो / उ (Singular), ती / उनीहरू / तिनीहरू (Plural)*.
   - High Honorific: *उहाँ (Singular), उहाँहरू (Plural)*.
2. **Null-Subject (Pro-Drop) Phenomenon:** In conversational Nepali, subjects are frequently omitted because verb inflection indicates person and honorific level (*"भात खाएँ"* -> subject is inherently *म*).

---

## 🤖 Modern Model Adaptation (Sentence-BERT & Gemma 4)
- **Sentence-BERT (Pairwise Span Mention Scoring):**
  - Compute span representation distance between antecedent candidate and pronoun.
- **Gemma 4 (Generative Coreference):**
  - Prompt: `"तल दिइएको अनुच्छेदमा सर्वनाम '{pronoun}' ले कुन व्यक्ति वा वस्तुलाई जनाउँछ?\nअनुच्छेद: {context}"`
