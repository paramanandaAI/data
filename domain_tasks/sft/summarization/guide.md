> Source: `sources/sft/summarization/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Text Summarization: Task Guide & Notes

## 🇳🇵 Nepali Linguistic Nuances
1. **Core Clausal Condensation:** Nepali narrative text heavily utilizes conjunctive participles (*-एर / -ई / -दा*) to chain clauses. Summaries must synthesize multiple dependent clauses into concise main clauses.
2. **Entity Consistency:** Maintain proper honorific and case marker agreement when condensing long names and titles.

---

## 🤖 Modern Model Adaptation (Gemma 4 & Sentence-BERT)
- **Gemma 4 (Abstractive Summarization):**
  - Prompt: `"तल दिइएको नेपाली समाचार वा लेखको मुख्य बुँदाहरू समेटेर छोटो र स्पष्ट सारांश तयार पार्नुहोस्:\n{document}"`
- **Sentence-BERT (Extractive Summarization):**
  - Compute sentence embeddings -> Cluster via k-means or PageRank (TextRank) -> Select centroid sentences.
