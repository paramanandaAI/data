> Source: `sources/similarity/reranking/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Reranking Methods: Gemma, Cross-Encoders & Dense Retrieval


---

## 🔁 Reranking Pipeline

### Two-Stage Retrieval
1. **Stage 1: Candidate Retrieval** — BM25 or dense retriever (top-100 documents)
2. **Stage 2: Reranking** — Cross-encoder or late-interaction model (top-10 final)

### Cross-Encoder Reranking
- **Input:** Query + document concatenated
- **Output:** Relevance score
- **Pros:** High accuracy (models attend to query-document interaction)
- **Cons:** Slow (must score each query-document pair independently)
- **Use case:** Re-rank top-100 from Stage 1

---

## 🤖 Gemma for Reranking

### Approach 1: Prompt-Based Relevance Scoring
```
Query: {query}
Document: {document}
Rate the relevance of this document to the query on a scale of 0-4:
0 = Completely irrelevant
1 = Slightly relevant
2 = Somewhat relevant
3 = Highly relevant
4 = Perfectly matches the information need
```

### Approach 2: Classification Head
- Fine-tune Gemma with a classification head for relevance (0/1 or 0-4)
- Use [CLS] token representation
- Train on Nepali relevance data (if available) or cross-lingual transfer

### Approach 3: Generative Reranking
- Prompt Gemma to extract key terms from query
- Score document based on term coverage
- Use chain-of-thought for explainable reranking

### Comparison with Sentence-BERT
| Aspect | Sentence-BERT (Cross-Encoder) | Gemma |
|---|---|---|
| Speed | Fast (small model) | Slower (larger model) |
| Accuracy | High (task-specific) | High (general reasoning) |
| Multilingual | Limited | Strong (Gemma 4) |
| Explainability | Low | High (generative) |
| Training data needed | Moderate | Few-shot possible |

---

## 📊 Dense Embedding Models for Retrieval

### Multilingual Embeddings
| Model | Params | Languages | Use Case |
|---|---|---|---|
| MuRIL | 1.7B | 17 Indic languages | Nepali dense retrieval |
| Multilingual E5 | 300M+ | 100+ languages | Cross-lingual retrieval |
| mE5-large | 560M | 100+ languages | High-quality embeddings |
| NepBERTa | 110M | Nepali | Monolingual dense retrieval |
| Sentence-BERT | 110M+ | Multilingual | Bi-encoder retrieval |

### Gemma Embeddings
- Gemma 4 provides embedding capabilities
- Can be used as dense retriever (if embedding endpoint available)
- Potential for zero-shot cross-lingual retrieval

---

## 🔗 Cross-References

| Resource | Location | Usage |
|---|---|---|
| Sentence-BERT | `sources/similarity/nli_sts/NOTES.md` | Bi-encoder + cross-encoder |
| Multilingual E5 | Wang et al. (2024) | Dense retrieval embeddings |
| MuRIL | Khanuja et al. (2021) | Indic language embeddings |
| Gemma | Google (2024) | Reranking + embeddings |
| IR Benchmark | `bal_eval/ir_information_retrieval/` | Retrieval evaluation |
| NepBERTa | `bal_eval/pretrained_models/` | Nepali-specific embeddings |
