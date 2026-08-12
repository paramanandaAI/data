> Source: `sources/sft/nlp_tasks/pos/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Part of Speech (PoS) Tagging & Morphosyntax: Task Guide & Notes

## 🇳🇵 43-Tag Standard Tagset Architecture
1. **Nouns (नाम):** `NN` (Common), `NNP` (Proper).
2. **Pronouns (सर्वनाम):** `PRP` (Personal), `PRP$` (Possessive), `DM` (Demonstrative).
3. **Verbs (क्रियापद):** `VF` (Finite verb), `VNF` (Non-finite verb), `VAUX` (Auxiliary).
4. **Postpositions (विभक्ति / नामयोगी):** `PPO` (Case postposition - *ले, लाई, मा, को*), `POP` (Compound postposition).
5. **Adjectives & Adverbs (विशेषण / क्रियाविशेषण):** `JJ` (Adjective), `RB` (Adverb).

---

## 🤖 Modern Model Adaptation (Sentence-BERT & Gemma 4)
- **Nepali BERT / RoBERTa (Sequence Tagging):**
  - Linear classification head over subword token embeddings with BIO/exact tag prediction.
- **Gemma 4 (Zero-shot / Few-shot Tagging):**
  - Structured prompt: `"प्रत्येक शब्दको पदवर्ग (PoS tag) JSON ढाँचामा छुट्याउनुहोस्:\nवाक्य: {sentence}"`
