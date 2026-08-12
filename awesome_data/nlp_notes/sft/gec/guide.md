> Source: `sources/sft/gec/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Nepali Grammar Error Correction (GEC) & Proofreading: Research & Linguistic Guide

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
