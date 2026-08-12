# Exhaustive Nepali NLP & Computational Linguistics Benchmark Suite (Bal-Prasain Taxonomy)

This dataset directory establishes a structured, hierarchical benchmark suite cataloging all **115 research publications, books, and software toolkits** by pioneer Nepalese computational linguists **Dr. Bal Krishna Bal** (Kathmandu University / Madan Puraskar Pustakalaya) and **Dr. Balaram Prasain** (Central Department of Linguistics, Tribhuvan University).

---

## 🏛️ NLP Architectural Hierarchy & Category Index

The benchmark suite is divided into six core sub-fields of Natural Language Processing and Fieldwork:

```
                            Nepali NLP Benchmark Suite
                                        |
      +--------------------+------------+------------+--------------------+
      |                    |                         |                    |
+--------------+    +--------------+          +--------------+    +--------------+
|    1. NLU    |    |    2. NLG    |          |  3. Speech   |    |4. Multimodal |
| Natural Lang |    | Natural Lang |          |  ASR & TTS   |    | Vision & OCR |
| Understanding|    | Generation   |          |  Acoustics   |    | Processing   |
+--------------+    +--------------+          +--------------+    +--------------+
      |                                                                   |
      +---------------------------------+---------------------------------+
                                        |
                      +-------------------+-------------------+
                      |                                       |
              +---------------+                       +---------------+
              | 5.Fieldwork & |                       |  6. Opinion,  |
              | Descriptive   |                       | Discourse &   |
              | Linguistics   |                       | ICT Systems   |
              +---------------+                       +---------------+
```

1. [**NLU (Natural Language Understanding)**](file:///d:/paramananda/dataset/NLU/index.md): 28 papers covering Morphological Analyzers, 91 & 112 POS Tagsets, FST Verb Morphotactics, Plagiarism Stemmers, Aspect Sentiment, Profanity Detection, Topic Classification, and Legal RAG QA.
2. [**NLG (Natural Language Generation)**](file:///d:/paramananda/dataset/NLG/index.md): 8 papers covering English–Nepali SMT/NMT, Nepali–Tamang Parallel Corpora, Legal Domain MT, and the PCDT Parallel Data Web Toolkit.
3. [**Speech (ASR & TTS Acoustics)**](file:///d:/paramananda/dataset/Speech/index.md): 14 papers covering Conformer ASR, Syllable Tokenization, PEFT ASR, Natural Sounding TTS, and Nepal Bhasha ASR.
4. [**Multimodal (Vision, OCR & Artifacts)**](file:///d:/paramananda/dataset/Multimodal/index.md): 14 papers covering Devanagari OCR, Ancient Ranjana Script Recognition, Ancient Artifact Text Parsing, Devanagari License Plate Recognition, and CNN-Transformer Image/Video Captioning.
5. [**Linguistics & Fieldwork**](file:///d:/paramananda/dataset/Linguistics_and_Fieldwork/index.md): 18 papers covering endangered language documentations (Baram, Kusunda, Bote, Dhuleli), complex predicate causatives, and Dzongkha verb transitivity.
6. [**Opinion, Discourse & ICT Systems**](file:///d:/paramananda/dataset/Opinion_Discourse_and_ICT/index.md): 19 papers covering newspaper editorial stance/argumentation mining, leader popularity tracking, e-commerce heuristics, and e-government trust frameworks.

---

## 🧪 Fair Prompt Evaluation Framework (`FairPromptKit`)

To evaluate LLMs fairly across **Zero-Shot**, **Few-Shot (In-Context Learning)**, **Supervised Fine-Tuning (SFT / LoRA)**, and **Neuro-Symbolic Rule-Guided Decoding**:

1. **System Prompt Standardization**: Explicit domain persona and target format constraints (XML morphological trees, 91/112 tagsets, JSON schemas).
2. **Probing Metrics**:
   - **Exact Match Rate ($\text{EMR}$)** on morpheme boundaries and root extractions.
   - **Irregular Sandhi Failure Rate ($\text{ISFR}$)** evaluating morphophonemic mutations (`सु + आगत -> स्वागत`).
   - **Precision ($P$), Recall ($R$), and $F_1$-Score** against Gold Standard Annotated Test Sets.
3. **Traditional Baseline Calibration**: Benchmarking LLM outputs against traditional rule-based Context-Free Grammar (CFG) parsers (Recall: $81.71\%$, Precision: $72.38\%$, $F_1$: $76.76\%$) and basic affix-stripping stemmers (Recall ceiling ~ $72.1\%$).
