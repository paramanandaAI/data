> Source: `sources/sft/nlp_tasks/wsd/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Word Sense Disambiguation (WSD) & WordNet: Task Guide & Notes

## 🇳🇵 Nepali Polysemy & Semantic Graphs
1. **Homographs & Multi-Sense Lexemes:**
   - *तीर* = 1. Arrow (बाण), 2. Riverbank (किनार).
   - *उत्तर* = 1. Answer (जवाफ), 2. North direction (दिशा).
   - *पत्र* = 1. Letter (चिठ्ठी), 2. Newspaper (पत्रिका), 3. Leaf/Layer (तह).
2. **Nepali WordNet (Bhawanakosh):** Hierarchical synset graphs with hypernyms and gloss definitions.

---

## 🤖 Modern Model Adaptation (Sentence-BERT & Gemma 4)
- **Sentence-BERT (Contextual Cross-Encoder):**
  - Compute cosine similarity between sentence context embedding and each candidate synset definition.
- **Gemma 4 (Generative Disambiguation):**
  - Prompt: `"तलको वाक्यमा '{target_word}' को उपयुक्त अर्थ कुन हो छान्नुहोस्:\nवाक्य: {sentence}\nविकल्पहरू:\n1. {sense_1}\n2. {sense_2}"`
