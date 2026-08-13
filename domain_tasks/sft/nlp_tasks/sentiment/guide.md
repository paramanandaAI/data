> Source: `sources/sft/nlp_tasks/sentiment/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Sentiment Analysis & Polarity: Task Guide & Notes

## 🇳🇵 Nepali Sentiment Modifiers & Negation
1. **Negation Particles (न- / छैन / होइन):**
   - Prefix negation: *नराम्रो (Bad), असफल (Unsuccessful)*.
   - Post-verbal negation: *गर्दैन (Does not do), छैन (Is not)*.
2. **Diminutives & Sarcasm:** Particle *'त'* or *'क्यारे'* often flips literal positive sentiment to sarcastic critique (*"राम्रो गर्यौ त!"*).

---

## 🤖 Modern Model Adaptation (Sentence-BERT & Gemma 4)
- **Sentence-BERT (Classification Head):**
  - Fine-tune [CLS] token representation for 3-class (Positive / Neutral / Negative) or multi-label aspect sentiment.
- **Gemma 4 (Few-Shot Reasoned Sentiment):**
  - Prompt: `"तल दिइएको समीक्षाको भावना (सकारात्मक / नकारात्मक / तटस्थ) र त्यसको कारण विश्लेषण गर्नुहोस्:\n{review}"`
