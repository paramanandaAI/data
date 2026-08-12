# Systematic Literature Review & Citation Benchmark Index: Nepali Natural Language Processing

*Based on Shahi & Sitaula (2021), "Natural language processing for Nepali text: a review", Artificial Intelligence Review (Springer Nature).*

This document provides a comprehensive, structured reference mapping **all citations, datasets, preprocessing techniques, computational approaches, NLP tasks, and evaluation metrics** from the landmark Springer survey paper into clear, standardized reference tables.

---

## 📊 1. Primary Publicly Available Datasets in Nepali NLP (Table 2 in Review)

| Reference | Dataset Name | Associated NLP Task | Sample Size / Volume | Domain / Characteristics | Access / Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Yadava et al. (2008)** | Nepali National Corpus (NNC) | POS Tagging, Parsing, MT | 14 Million Words | 3 Sub-corpora: Written (15 genres), Spoken (audio transcripts), Parallel (En-Ne 27k aligned sentences) | ELRA Catalogue |
| **Choudhary & Ramamoorthy (2019)** | LDC-IL Raw Text Corpus | General NLP & Pretraining | 7 Million Words | 6 Domains: Aesthetics (57.7%), Commerce (0.43%), Mass Media (32.2%), Official (0.03%), Sci-Tech (1.14%), Social Sci (8.51%) | CIIL LDC-IL |
| **Lamsal (2020)** | Large Scale Nepali Text Corpus | Word Embeddings & Pretraining | 90 Million Words | News portals, Finance, Sports, Health, Entertainment; includes 0.5M word embedding vectors | IEEE DataPort |
| **sndsabin / KU (2021)** | 16NepaliNews | News Document Classification | 14,364 Documents | 16 News Categories: Auto, Bank, Blog, Business, Economy, Education, Employment, Entertainment, Interview, etc. | GitHub (KU) |
| **Shahi & Pant (2018)** | NepaliNewsLarge | News Document Classification | 7,023 Documents | 20 News Categories: Agriculture, Automobiles, Bank, Blog, Business, Economy, Health, Literature, Migration, Politics, etc. | Kaggle |
| **Sitaula et al. (2021)** | NepaliLinguistic | News Classification & Clustering | 35,651 Documents | 17 Labeled News Categories with Supervised Codebooks | IEEE DataPort |
| **Senapati et al. (2020)** | Annotated Anaphoric Relation | Anaphora & Coreference | 4,700 Words | Short stories, blogs, news articles with gold backward coreference links | ResearchGate |
| **Dhungana & Shakya (2014)** | Nepali WordNet | Word Sense Disambiguation (WSD) | 348 Target Words | 59 Polysemous target words mapped with Synsets, Glosses, Hypernyms | IOE TU |
| **Singh et al. (2019)** | NepaliNER Corpus | Named Entity Recognition (NER) | 79,087 Entities | 4 Generic Named Entity Classes: PER, LOC, ORG, MISC | IEEE CIC |
| **Singh et al. (2020)** | NepSA Corpus | Aspect Sentiment Analysis | 4,035 Sentences | YouTube user comments with multi-aspect polarity annotation | IEEE/ACM ASONAM |

---

## 🛠️ 2. Comparative Analysis of Part-of-Speech (POS) Taggers (Table 5 in Review)

| Reference | Features Used | Underlying Method | Key Advantages | Reported Limitations |
| :--- | :--- | :--- | :--- | :--- |
| **Bal & Shrestha (2004)** | Morphological rules & Lexicon | Rule-Based (Unitag) | High precision on rule-covered vocabulary | Static; fails to generalize to out-of-vocabulary (OOV) words |
| **Prajwal et al. (2008)** | POS Bi-grams & Trigrams | Statistical (TnT Tagger) | Handles probability estimation over 82k words & 42 tags | 97% Accuracy on known words, drops to 56% on unknown words |
| **Shahi et al. (2013)** | Word features & Context | Support Vector Machine (SVM) | Superior performance on both known (91.07%) and unknown (89.56%) words | Word context window was not explicitly modeled |
| **Paul et al. (2015)** | Emission & Transition Probs | Hidden Markov Model (HMM) | Lightweight statistical tagger trained on 150k words | Accuracy on unknown words was unverified |
| **Yajnik (2017)** | Viterbi Probability Decoding | HMM + Viterbi | Reached 95.43% accuracy on custom tagset | Limited generalization across domain shifts |
| **Prabha et al. (2018)** | Word Embeddings | RNN, LSTM, CNN, CNN-LSTM | High accuracy (~99%) capturing sequential contexts | Datasets/models not public; risk of overfitting on small corpora |
| **Yajnik (2018)** | HMM Marginal Probabilities | Feed-Forward, Radial Basis ANN | Neural integration with HMM probability features | Context window and OOV handling unverified |

---

## 🏷️ 3. Comparative Study of Named Entity Recognition (NER) Systems (Table 6 in Review)

| Reference | Target Classes | Features Extracted | Classification Method | Key Advantages & Findings |
| :--- | :--- | :--- | :--- | :--- |
| **Bam & Shahi (2014)** | PER, LOC, ORG, MISC | Gazetter list, first word, length, digits | Support Vector Machines (SVM) | First automated Nepali NER model; highlighted Devanagari no-capitalization & agglutination challenges |
| **Dey et al. (2014)** | PER, LOC, ORG, NUM, CUR, QNT | POS tags, N-grams, lookup tables | Rule-Based + HMM Hybrid | Broad class coverage including currency and quantifiers |
| **Singh et al. (2019)** | PER, LOC, ORG, MISC | Character embedding, Grapheme, POS | BiLSTM + CNN Deep Learning | Achieved state-of-the-art **86.89% Accuracy** on 79k entity benchmark |

---

## 📈 4. Document Representation & Text Classification Methods (Table 7 in Review)

| Reference | Representation Strategy | Classification Classifier | Key Advantages | Limitations & Challenges |
| :--- | :--- | :--- | :--- | :--- |
| **Thakur & Singh (2014)** | Bag-of-Words (BoW) | Naive Bayes + Lexicon Pool | Simple to implement across all document types | Ignores word order and context |
| **Kafle et al. (2016)** | TF-IDF + Word2Vec | Artificial Neural Network (ANN) | Captures basic semantic similarity | Sub-optimal parameter tuning |
| **Shahi & Pant (2018)** | TF-IDF Vectorization | SVM, Naive Bayes, ANN | Benchmarked 7,023 news articles across 20 categories | Lacks long-range context |
| **Dangol et al. (2018)** | Token N-gram Matrix | N-gram Frequency | Captures local phrase semantics better than BoW | High feature space dimensionality |
| **Basnet & Timalsina (2018)** | Word2Vec Embeddings | LSTM Recurrent Network | Preserves sequential token ordering | Prone to overfitting on smaller news subsets |
| **Subba et al. (2019)** | Bag-of-Words (BoW) | Deep Recurrent Neural Network (RNN) | Outperforms standard feed-forward ANNs | High tuning complexity for RNN hyperparameters |
| **Sitaula et al. (2021)** | Supervised Codebook | Codebook Clustering + Classifier | **State-of-the-art accuracy**, outperforming TF-IDF, BoW, and BERT | Codebook design is computationally intensive |

---

## 🎭 5. Sentiment Analysis & Opinion Mining Approaches (Table 8 in Review)

| Reference | Sentiment Level | Feature Set | Classification Model | Key Contributions & Findings |
| :--- | :--- | :--- | :--- | :--- |
| **Gupta & Bal (2015)** | Sentence Level | Bag-of-Words (BoW) | SentiWordNet (Bhawanakosh) + NB | Introduced first Nepali SentiWordNet (Bhawanakosh) on 25k news sentences |
| **Thapa & Bal (2016)** | Document Level | TF-IDF & BoW | Multinomial Naive Bayes, SVM | Evaluated book & movie reviews; Naive Bayes outperformed SVM |
| **Regmi et al. (2017)** | Sentence Level | Word2Vec, Bi-grams, TF-IDF | SVM, Naive Bayes, Logistic Reg | Distinguished Fact vs. Opinion; SVM with bi-grams achieved top score |
| **Piryani et al. (2020)** | Tweet Level | Emotion Lexicons, Word2Vec | CNN-LSTM Deep Learning | Hybrid deep learning on Nepali tweets; CNN-LSTM achieved best performance |
| **Tamrakar et al. (2020)** | Aspect Level | TF-IDF, POS Tags | Support Vector Machine, Naive Bayes | First aspect-based sentiment model utilizing POS grammatical cues |

---

## 🔄 6. Machine Translation (MT) & Speech Processing Systems

| Reference | Domain / Language Pair | Architecture / Methodology | Reported Performance / BLEU |
| :--- | :--- | :--- | :--- |
| **Bista et al. (2005)** | English $\rightarrow$ Nepali | Dobhase Rule-Based Machine Translation | Prototype English-to-Nepali rule engine |
| **Paul & Purkayastha (2018)** | English $\rightarrow$ Nepali | Statistical Machine Translation (SMT: Moses + GIZA++) | Outperformed early neural baselines |
| **Acharya & Bal (2018)** | English $\leftrightarrow$ Nepali | SMT vs. Neural Machine Translation (NMT) | SMT BLEU: **5.27** vs. NMT BLEU: **3.28** (highlighted low-resource NMT gap) |
| **Laskar et al. (2019)** | Hindi $\leftrightarrow$ Nepali | Bi-directional NMT (Transformer) | High BLEU score of **24.6** due to shared Devanagari script & cognates |
| **Shah et al. (2018)** | Nepali Speech Synthesis | FreeTTS Concatenative Synthesis | First functional Nepali Text-to-Speech (TTS) engine |

---

## 🧩 7. Computational Morphological Analyzers, Stemmers & Parsers

| Reference | Linguistic Focus | Underlying Technique | Key Innovation & Findings |
| :--- | :--- | :--- | :--- |
| **Bal & Shrestha (2004)** | Prefix & Suffix Morphemes | Rule-Based Stripping + 91 POS Lexicon | Pioneer Nepali MA and Stemmer; established regular/irregular sandhi rules |
| **Prasain (2008, 2011)** | Verb Morphotactics | Finite State Transducers (FST / leXC / xfst) | Automated 10 verb stem categories, 14 noun classes, 15 derivational affixes |
| **Sitaula (2013)** | Agglutinative Words | Context-Free Grammar (CFG) + Similarity | Overcame affix over-stemming via structural parse tree matching |
| **Dhungana & Shakya (2014)** | Polysemous Words | Nepali WordNet + Lesk Algorithm | Disambiguated 348 target words using semantic synset graphs |
| **Chhetri et al. (2015)** | Noun Inflections | Finite State Machine (FSM) + Suffix DB | Decomposed inflected noun tokens into root and bound suffixes |
| **Shrestha & Dhakal (2016)** | Suffix Stripping | 128 Suffix Rules Engine | Tested on 5,000 words; noted over-stemming on derivational compounds |
| **Borah et al. (2017)** | Non-Declinable Adjectives | Finite State Automata (FSA) | Transliterated to Romanized patterns to match adjective-noun positions |
| **Senapati et al. (2020)** | Anaphora & Coreference | Machine Learning (SVM, Decision Tree) + Saliency | Combined noun inflection features with inter-sentence distance |
