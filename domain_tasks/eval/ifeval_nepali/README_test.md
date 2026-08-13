# Nepali Instruction Following & Constraint Compliance Benchmark (IFEval-Nepali)

> Held-out IFEval (Instruction Following Evaluation) benchmark port for testing whether Nepalese language models comply with verifiable instructions.

---

## 📜 Verifiable Constraint Types

1. **Format Constraints:** JSON mode, Markdown headers, Bulleted lists, Key-Value pairs.
2. **Length Constraints:** Min/Max word count, exact paragraph count.
3. **Linguistic Register Constraints:** High Honorific (हजुर / सवारी), Devanagari script strictly, no English loan words.
4. **Content Constraints:** Must include specific keywords or named entities.

---

## 🛠️ Benchmark JSONL Schema

```json
{
  "id": "ifeval-ne-001",
  "instruction": "बागमती प्रदेशको पर्यटकीय महत्त्वबारे ३ वटा बुँदामा कम्तीमा १०० शब्दको विवरण लेख्नुहोस्।",
  "verifiable_constraints": [
    {"type": "bullet_list_count", "target": 3},
    {"type": "min_word_count", "target": 100}
  ],
  "language": "ne",
  "domain": "tourism"
}
```

---

## 📚 Academic Citations

- **Zhou, J., et al. (2023)**: *Instruction-Following Evaluation for Large Language Models (IFEval)*. arXiv:2311.07911.
- **Himalaya AI Labs (2025)**: *Nepali Honorific & Pragmatic Register Benchmark*.
