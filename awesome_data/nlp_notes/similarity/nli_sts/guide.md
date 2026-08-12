> Source: `sources/similarity/nli_sts/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Natural Language Inference (NLI) & Semantic Textual Similarity (STS): Task Guide & Notes


---

## 🇳🇵 Semantic Similarity Nuances in Nepali
1. **Word-Order Invariance:** In Nepali, SOV order allows slight permutation of adverbial and prepositional phrases without changing entailment (*"रामले काठमाडौँमा भात खायो"* $\iff$ *"काठमाडौँमा रामले भात खायो"*).
2. **Honorific Paraphrasing:** Entailment holds across honorific shifts (*"उनी आए"* $\implies$ *"उहाँ आउनुभयो"*).

---

## 🤖 Modern Model Adaptation (Sentence-BERT & Gemma 4)
- **Sentence-BERT (Bi-Encoder & Cross-Encoder):**
  - Loss Function: Multiple Negatives Ranking Loss (MNRL) for dense embeddings; Cross-Entropy on paired inputs for cross-encoder reranking.
- **Gemma 4 (NLI Reasoning):**
  - Prompt: `"तल दिइएको आधार वाक्य (Premise) र परिकल्पना (Hypothesis) बीचको सम्बन्ध के हो (Entailment / Neutral / Contradiction)?\nआधार: {premise}\nपरिकल्पना: {hypothesis}"`

---

## ⚙️ Related Embedding & Similarity Frameworks

| Repository | Focus |
|---|---|
| [`princeton-nlp/SimCSE`](https://github.com/princeton-nlp/SimCSE) | Contrastive learning of sentence embeddings (EMNLP 2021) |
| [`shibing624/text2vec`](https://github.com/shibing624/text2vec) | Text to vector (Word2Vec, Sentence-BERT, CoSENT) |
| [`explosion/sense2vec`](https://github.com/explosion/sense2vec) | Contextually-keyed word vectors |
| [`MinishLab/model2vec`](https://github.com/MinishLab/model2vec) | Fast state-of-the-art static embeddings |
| [`thunlp/WantWords`](https://github.com/thunlp/WantWords) | Open-source reverse dictionary |
| [`plasticityai/magnitude`](https://github.com/plasticityai/magnitude) | Fast universal vector embedding utility |
