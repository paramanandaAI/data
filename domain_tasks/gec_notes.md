# Nepali Grammar Error Correction (GEC) & Proofreading: Research & Linguistic Guide

## 📚 Academic Literature & Citations
- **GECToR** (Omelianchuk et al., 2020) — Sequence tagging architecture for grammatical error correction.
- **Nepali Grammatical Error Detection & Correction Benchmark** (Sumit Aryal & CFILT IIT Bombay, 2024).

---

## 🇳🇵 Core Nepali Grammatical Rules & Common Error Types
1. **Subject-Verb Agreement (कर्ता र क्रियाको संगति):**
   - **Gender (लिङ्ग):** *राम गयो (M)* vs. *सीता गई / गइन् (F)*.
   - **Number (वचन):** *केटा आयो (Singular)* vs. *केटाहरू आए (Plural)*.
   - **Person (पुरुष):** *म खान्छु (1st)*, *तिमी खान्छौ (2nd)*, *उनी खान्छिन् (3rd)*.
   - **Honorific Tier (आदर):** *तँ गइस् (Low)*, *तिमी गयौ (Mid)*, *तपाईँ जानुभयो (High)*, *हजुर सवारी हुनुभयो (Royal/Ultra-High)*.
2. **Postpositional Case Markers (विभक्ति चिन्हहरू):**
   - Ergative marker *'ले'* rule: In transitive past tense sentences, *'ले'* is mandatory on the subject:
     - Correct: *रामले भात खायो।*
     - Incorrect: *राम भात खायो।*
3. **Orthographic Hrasva/Dirgha (ह्रस्व र दीर्घ नियम):**
   - Word-initial/medial: *इ/उ* vs. *ई/ऊ*.
   - Tatsama (तत्सम) Sanskrit loanwords retain original Sanskrit spelling (*कीर्ति, प्रकृति*), while Tadbhava (तद्भव) and Deshaja (देशज) follow modern Nepali standardized rules.

---

## 🤖 LLM Correction & Seq2Seq Strategy
- In T5/Seq2Seq, frame with explicit task prefixes: `"correct nepali grammar: "` or provide token-level Levenshtein edit distance loss weights to penalize over-correction of stylistic variations.

## 📖 Curated Academic Literature Index (12 Works)

1. **Nepali Passport Question Answering: A Low-Resource Dataset for Public Service Applications**
   - *Authors & Venue:* FL Begha, P Acharya, BK Bal - arXiv preprint arXiv:2603.13320, 2026 - arxiv.org
   - *Citations:* 1
   - *Summary / Context:* … Next, we standardized Unicode to normalize Nepali characters, ensuring consistent encoding for NLP tasks. Common spelling errors and inconsistent formatting were corrected. …

2. **Prasta Nepali: A Transformer Based Approach for Automated Nepali Grammar (Byakaran) Error Detection and Correction**
   - *Authors & Venue:* S Thapa, A Pradhan, D Kayastha… - 2025 International …, 2025 - ieeexplore.ieee.org
   - *Citations:* 1
   - *Summary / Context:* … for innovative research in low-resource NLP. The Vyakranly [6] targets the … Nepali NLP enthusiasts to adopt these advanced methods, promising significant advancements in Nepali …

3. **nepjol.info Automated Spell Checking in Nepali Texts Using LSTM and BiLSTM**
   - *Authors & Venue:* J Bhatta, K Shrestha, N Paudel - Mid-West University Journal of …, 2025 - nepjol.info
   - *Summary / Context:* … natural language processing (NLP) applications ranging from word processors to chat bots. For Nepali texts, checking the spelling is crucial for Nepali … of spell checking for Nepali texts. …

4. **ioe.edu.np An Encoder Decoder Model for Grammatical Error Correction of Nepali Text**
   - *Authors & Venue:* D Bashyal, S Pandey - Proceedings of IOE Graduate …, 2025 - conference.ioe.edu.np
   - *Summary / Context:* … This research contributes significantly to Bangla NLP by offering open-source data and code … a strong foundation for future advancements in NLP and Bangla sentence correction[7]. …

5. **Nepali Word Spelling Correction Using Ensemble Learning Technique**
   - *Authors & Venue:* S Bhattarai, A Shakya, B Joshi - International Conference on Frontiers of …, 2024 - Springer
   - *Summary / Context:* … into NLP in Nepal involved the release of the Nepali Spell Checker and Thesaurus in 2005 [7]. Hunspell is the foundation used by this Nepali … There are 6.2 million Nepali words that are …

6. **A Maximal Graph Matching and Grammar based Dependency Parsing Technique for Nepali**
   - *Authors & Venue:* A Pradhan, A Yajnik - 2025 - assets-eu.researchsquare.com
   - *Summary / Context:* … natural language processing (NLP) for Nepali language21. In the survey, the authors have provided a detailed analysis and discussion of Nepali NLP … language for various NLP tasks. …

7. **nepjol.info Nepali spelling checker**
   - *Authors & Venue:* B Prasain, N Lamichhane, N Pandey… - Journal of Engineering …, 2022 - nepjol.info
   - *Citations:* 3
   - *Summary / Context:* … This project addressed the problem of detection and correction of spelling errors in Nepali language. Our model works on two phases. During the first phase, the error word in the …

8. **Development and Implementation of Advanced Text Autocorrection via Probabilistic Methods Using Levenshtein Distance and Jaccard Similarity**
   - *Authors & Venue:* NJ Saunshimath, DR Upadhyaya… - … on Emerging Systems …, 2025 - ieeexplore.ieee.org
   - *Citations:* 1
   - *Summary / Context:* … in NLP applications for the Nepali language is laid by this effort. … the Nepali language, creating new opportunities for development and research. By using natural language processing, it …

9. **tucl.edu.np Nepali Document Clustering using DBSCAN and OPTICS Algorithm**
   - *Authors & Venue:* P Maharjan - 2018 - elibrary.tucl.edu.np
   - *Summary / Context:* … Since the release of Nepali spell checker in 2005, various works on Nepali Natural language processing began. The same year, KU (Kathmandu University) along with MPP (Madan …

10. **cle.org.pk Architectural and system design of the Nepali grammar checker**
    - *Authors & Venue:* BK Bal, P Shrestha, MP Pustakalaya… - PAN localization …, 2007 - panl10n.cle.org.pk
    - *Citations:* 16
    - *Summary / Context:* … of the Nepali Grammar Checker. Currently, the Natural Language Processing Team has been involved in the research work for the design and development of the Nepali Grammar …

11. **NLP‐Based Spellchecker and Grammar Checker for Indic Languages**
    - *Authors & Venue:* BKY Panchal, A Shah - Natural Language Processing for …, 2025 - Wiley Online Library
    - *Citations:* 5
    - *Summary / Context:* … In 2007, this study [3] developed the Nepali Grammar Checker, which is undergoing testing and development. It is described in this chapter along with its architectural and system design…

12. **Grammar checker for Asian languages: A survey**
    - *Authors & Venue:* M Mittal, D Kumar, SK Sharma - International Journal of Computer …, 2016 - mail.ijcait.com
    - *Citations:* 7
    - *Summary / Context:* … , Urdu language, Nepali language and Bangla language. … Natural Language Processing (NLP) application or tools for checking the syntax of language. The natural language processing …
