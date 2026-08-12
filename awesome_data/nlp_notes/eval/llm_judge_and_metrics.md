> Source: `sources/evaluation/NOTES.md` · split by content type
> Section kept: whole
> Do NOT edit content — pending web verification.

# Evaluation Frameworks: LLMJudge, Sentiment Rubrics & Metrics

## 📚 Academic Citations & Literature
- **LLM-as-a-Judge: A Comprehensive Survey** (Rahmani et al., 2024).
- **Navarasa: Affective Computing for Indian Languages** (Multiple authors).
- **BLEURT: Learning Robust Metrics for Text Generation** (Sellam et al., ACL 2020).

---

## 🧑‍⚖️ LLM-as-a-Judge (LLMJudge)

### Concept
- Use large language models as automatic evaluators
-替代 human annotation for quality assessment
- Configurable rubrics for different tasks

### Implementation
- Wrap Rahmani et al. (2024) LLMJudge as standalone agent skill
- Support multiple LLM backends (Gemma, GPT, Claude)
- Configurable evaluation criteria

### Use Cases
- **IR:** Evaluate relevance judgments (query-document relevance)
- **MT:** Evaluate translation quality (adequacy, fluency, terminology)
- **NLI:** Evaluate inference quality (entailment, contradiction)
- **Generation:** Evaluate text quality (coherence, fluency, factuality)

### Evaluation Protocol
```
Task: [IR Relevance / MT Quality / NLI / Generation]
Query: {query}
Document/Output: {document}
Criteria:
  1. [Criterion 1]: Description
  2. [Criterion 2]: Description
  ...
Score: 0-4 scale
Explanation: [Reasoning]
```

---

## 🎭 Navarasa Sentiment Rubric

### Nine Emotions (रस)
| Emotion | Devanagari | Description | Use Case |
|---|---|---|---|
| शृंगार | Love | Romance, beauty | Poetry, literature |
| हास्य | Humor | Comedy, wit | Jokes, satire |
| करुणा | Compassion | Sadness, pathos | Tragedy, sympathy |
| रौद्र | Anger | Rage, fury | Conflict, protest |
| वीर | Heroism | Courage, bravery | Heroic narratives |
| भयानक | Fear | Horror, terror | Thriller, suspense |
| बीभत्स | Disgust | Revulsion, aversion | Warning, caution |
| अद्भुत | Wonder | Surprise, amazement | Discovery, marvel |
| शान्त | Peace | Tranquility, calm | Meditation, nature |

### Evaluation Protocol
- Score each emotion dimension separately (0-4)
- Not 500 samples — evaluate exact content
- Use for evaluation of generated text quality
- Applicable to: poetry, news, stories, social media

### Application to IR
- Evaluate retrieved documents for emotional relevance
- Filter content by emotional tone
- Sentiment-aware retrieval (find "happy" vs "sad" news)

---

## 📊 Evaluation Metrics

### IR Metrics
| Metric | Description | Use Case |
|---|---|---|
| nDCG@10 | Normalized Discounted Cumulative Gain | Ranked retrieval quality |
| MAP | Mean Average Precision | Overall retrieval quality |
| MRR | Mean Reciprocal Rank | First relevant result position |
| P@k | Precision at k | Top-k precision |
| R@k | Recall at k | Top-k recall |

### Graded Relevance Scale (1-4)
| Score | Label | Description |
|---|---|---|
| 4 | Perfect | Completely answers the query |
| 3 | Excellent | Highly relevant, minor gaps |
| 2 | Fair | Partially relevant |
| 1 | Poor | Marginally relevant |
| 0 | Irrelevant | Not relevant at all |

### Content Filtering
- **Profanity detection** in Nepali text
- **Emotion categorization** (Navarasa-based)
- **Quality scoring** (readability, coherence)

---

## 🔗 Cross-References

| Resource | Location | Usage |
|---|---|---|
| IR Benchmark | `bal_eval/ir_information_retrieval/` | IR evaluation |
| LLMJudge | Rahmani et al. (2024) | LLM-based evaluation |
| Navarasa | Indian classical aesthetics | Nine-emotion rubric |
| STS | `sources/similarity/nli_sts/NOTES.md` | Similarity evaluation |
| MT | `sources/machine_translation/` | Translation evaluation |
