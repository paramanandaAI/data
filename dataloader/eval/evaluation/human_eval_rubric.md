# Human Evaluation Rubric for Nepali Text Denoising

This rubric defines the standard 3-tier scoring system for evaluating model outputs on sample datasets.

## Rubric Dimensions (Scale: 1–5)

### 1. Fluency & Naturalness (प्रवाहशीलता र सहजता)
- **5**: Perfectly natural Devanagari Nepali sentence; native phrasing and correct grammar.
- **3**: Understandable Nepali sentence, but contains minor awkwardness or non-standard word order.
- **1**: Incomprehensible, broken, or heavily garbled text.

### 2. Adequacy & Meaning Preservation (अर्थ संरक्षण)
- **5**: All original information, intent, tone, and slurs/named entities are preserved accurately.
- **3**: Main meaning preserved, but minor details or tone dropped/modified.
- **1**: Meaning completely changed, inverted, or lost.

### 3. Grammatical & Postposition Accuracy (व्याकरण र पदसंगति)
- **5**: Postpositions attached correctly (`सरकारले`), Halantas (`हुन्छन्`), and standard spellings (`बधाई`, `ठिक`) properly applied.
- **3**: Partially corrected; some postpositions detached or spelling errors remaining.
- **1**: No postpositions joined, incorrect Halanta usage, or broken morphology.
