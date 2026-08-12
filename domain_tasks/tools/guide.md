> Source: `sources/tools/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# NLP Tools: Translation, Transliteration, Lemmatizer, Stemmer & Morphological Analyzer


---

## 🔄 Translation Tools

### Nepali↔English Translation
| Tool | Type | Quality | Use Case |
|---|---|---|---|
| NLLB (No Language Left Behind) | Open-source, 200 languages | Good | Bulk translation |
| mBART | Multilingual sequence-to-sequence | Good | Back-translation augmentation |
| Google Translate API | Commercial | High | Quick translation |
| Microsoft Translator | Commercial | High | API integration |

### Translation Pipeline
1. **Input:** Nepali text
2. **Preprocessing:** Tokenize, clean
3. **Translate:** Nepali → English
4. **Postprocessing:** Detokenize, normalize
5. **Quality check:** BLEU, COMET scoring

### Use Cases
- Cross-lingual retrieval (English queries → Nepali documents)
- Data augmentation via back-translation
- Parallel corpus creation

---

## 🔤 Transliteration Tools

### Romanization Schemes
| Scheme | Description | Example |
|---|---|---|
| ISO 15919 | Standard transliteration | kāṭhamāḍauṃ |
| IAST | Sanskrit/Hindi standard | kāṭhamāḍauṃ |
| SLP1 | Sanskrit Library transliteration | kATamADauM |
| Hunterian | Colonial-era romanization | Kathmandu |

### Transliteration Pipeline
1. **Input:** Nepali text (Devanagari or Roman)
2. **Detect:** Script detection (Devanagari vs Roman)
3. **Normalize:** Convert to standard scheme
4. **Convert:** Roman → Devanagari if needed
5. **Validate:** Check for errors

### Use Cases
- Clean web-scraped data (mixed scripts)
- Normalize transliterated queries
- Code-mixed text processing

---

## 📖 Lemmatizer Tools

### Sunil Regmi's Lemmatizer
- **Type:** Word-level rule-based
- **Coverage:** Nepali verbs, nouns, adjectives
- **Output:** Root form + POS tag
- **Accuracy:** ~85% on standard test set

### Sundeep Dawadi's Lemmatizer
- **Type:** Word-level statistical
- **Coverage:** Similar to Regmi's
- **Output:** Root form
- **Accuracy:** ~82% on standard test set

### Lemmatization Pipeline
1. **Input:** Inflected Nepali word
2. **Morphological analysis:** Parse suffixes
3. **Rule application:** Remove suffixes, restore root
4. **POS disambiguation:** Choose correct root based on POS
5. **Output:** Lemma (root form)

### Use Cases
- Query expansion (match inflected forms)
- Morphology-aware retrieval
- Text normalization for IR

---

## ✂️ Stemmer Tools

### Rule-Based Stemmer (Bal & Shrestha, 2004)
- **Method:** Suffix stripping rules
- **Rules:** Based on Nepali morphological patterns
- **Speed:** Very fast
- **Accuracy:** ~80% on IR tasks

### Statistical Stemmer
- **Method:** Porter stemmer adapted for Nepali
- **Rules:** Frequency-based suffix removal
- **Speed:** Fast
- **Accuracy:** ~78%

### Comparison
| Stemmer | Speed | Accuracy | Coverage |
|---|---|---|---|
| Rule-based (Bal) | Fast | ~80% | Common suffixes |
| Statistical | Fast | ~78% | Data-driven |
| Lemmatizer (Regmi) | Medium | ~85% | Full morphology |
| Lemmatizer (Dawadi) | Medium | ~82% | Full morphology |

---

## 🔬 Morphological Analyzer

### Capabilities
- Parse inflected forms → root + suffixes
- Extract POS tags from morphology
- Generate inflectional variants
- Handle complex verb conjugations

### Nepali Morphology
- **Verbs:** Conjugated by tense, mood, aspect, person, number
- **Nouns:** Inflected by case, number, gender
- **Adjectives:** Declined by gender, case, number
- **Postpositions:** Attach to noun phrases

### Use Cases
- Query expansion (generate all inflected forms)
- POS-based feature extraction
- Linguistically-informed retrieval

---

## 📝 Spellchecker (Bal Krishna Bal)

### Word Transformation
- Generate candidate corrections for misspelled words
- Edit distance + morphological rules
- Context-aware suggestions

### Use Cases
- Query normalization (correct misspellings)
- Noisy input handling
- Data cleaning

---

## 🔗 Cross-References

| Resource | Location | Usage |
|---|---|---|
| Nepali Stemmer | Bal & Shrestha (2004) | Stemming for IR |
| Lemmatizer | Sunil Regmi, Sundeep Dawadi | Word-level lemmatization |
| Spellchecker | Bal Krishna Bal | Word form replacement |
| IR Benchmark | `bal_eval/ir_information_retrieval/` | Retrieval evaluation |
| Similarity | `sources/similarity/` | Embedding models |
| Translation | `sources/machine_translation/` | MT frameworks |
