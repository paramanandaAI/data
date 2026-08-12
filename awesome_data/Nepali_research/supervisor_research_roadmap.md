# Innovative Nepali NLP & AI Research Ideas (Inspired by IIT Patna AI-NLP-ML Group & L3Cube-MahaNLP)

This document outlines high-impact, state-of-the-art Natural Language Processing (NLP) research dataset, model, and framework roadmap ideas tailored specifically for the **Nepali language** and **Nepali-English Code-Mixed (Nepglish)** contexts.

---

## 🎯 1. Aspect-Based Sentiment Analysis (ABSA) & Intensity Mining for Nepali
- **Nepali E-Commerce Aspect-Based Sentiment Dataset (ABSA-Nepali)**:
  - Annotate Nepali and Code-Mixed Nepglish e-commerce reviews for **Aspect Term Extraction**, **Aspect Category Detection** (e.g., *Service*, *Price*, *Delivery*, *Quality*), and **Sentiment Polarity** (*Positive*, *Negative*, *Neutral*).
- **Nepali Sentiment Intensity Analysis**:
  - Extend standard binary/ternary sentiment to fine-grained intensity scales (e.g., *Very Good*, *Good*, *Average*, *Poor*, *Extremely Terrible*) for Nepali product & hospitality reviews.
- **Code-Mixed Nepglish Aspect Mining**:
  - Benchmarks for handling Romanized Nepali + English mix (e.g., *"Product ta ekdam ramro cha but delivery late vayo"*).

---

## 🤝 2. Empathetic & Polite Dialogue Systems (Counseling & Legal Aid)
- **Empathetic & Polite Mental Health Counseling Agent (Nepali PAL/e-Therapist)**:
  - Multi-turn conversational dataset in Nepali for polite, empathetic guidance, depression distress filtering, and positive mindset reinforcement.
- **Crime Victim & Legal Aid Dialogue System (PARTNER-Nepali)**:
  - Reinforced dialogue dataset focusing on legal counseling and survivor support for crime victims in Nepal, balancing legal accuracy with emotional empathy.
- **Persona-Aware & Integrative Negotiation Agent (Trip-Negotiator for Nepal Tourism)**:
  - Dialogue datasets for polite negotiation between tourists and local service providers (e.g., trekking agencies, hotels, transport) in Nepali.

---

## 🧠 3. Clinical & Distress Analysis (Cognitive Distortion & Suicide Note Mining)
- **Cognitive Distortion Detection in Nepali Clinical Conversations (DeCoDE-Nepali)**:
  - Identify cognitive distortions (e.g., *overgeneralization*, *catastrophizing*, *personalization*) and emotion-cause extraction in Nepali clinical & counseling transcripts.
- **Distress Identification & Cause Extraction (DICE-Nepali)**:
  - Fine-grained temporal orientation and emotion-driven distress cause detection in online Nepali social posts and support forums.

---

## 📚 4. Scholarly Text Processing & Peer Review Analysis
- **ScienceQA-Nepali**:
  - Benchmark dataset for Question Answering on scientific scholarly articles, medical journals, and academic papers written in or translated into Nepali.
- **Peer Review Disagreement & Meta-Review Generation (PeerReview-Nepali)**:
  - Annotation of scientific peer reviews in Nepali/English to detect reviewer disagreement, sentiment polarity, and decision-aware meta-review generation.

---

## 🎭 5. Multimodal & Code-Mixed NLP (Memes & Visual QA)
- **Nepali Multimodal Meme Sarcasm & Humor Recognition (EmoffMeme-Nepali)**:
  - Multimodal dataset combining Devanagari text, Romanized Nepglish, and image memes to identify sarcasm, humor, and underlying emotion.
- **Multilingual & Code-Mixed Visual Question Answering (VQA-Nepali)**:
  - Images depicting Nepalese culture, landmarks, and daily life paired with natural language questions in Devanagari Nepali and Nepglish.

---

## 📰 6. Natural Language Inference (NLI) & Fact-Checking / Fake News
- **Refined NLI for Fake News Detection in Nepali (FakeNews-NLI-Nepali)**:
  - Fact-checking dataset linking news claims with evidence passages using Cross-Lingual NLI (English-Nepali) for automated rumor verification.
- **Adversarial Complaint Identification (SEHC-Nepali)**:
  - Multi-task framework for joint detection of complaints, sentiment, emotion, and online hate speech in Nepali social media.

---

## 🔀 7. Product Review Translation & Noisy Text Normalization
- **Noisy User-Generated Product Review Parallel Corpus (English <-> Nepali)**:
  - Parallel corpus of informal, noisy user reviews with orthographic normalization (converting informal Devanagari / Romanized text to standard formal Nepali).

---

## 🚀 8. L3Cube-MahaNLP Inspired Ecosystem: Building `NepaliNLP` Framework & Benchmarks

Inspired by L3Cube-Pune's `MahaNLP` and `MahaCorpus` architecture for Marathi, here is the complete roadmap to elevate Nepali into a resource-rich language:

### 8.1 Monolingual Corpus & Foundation Models (`NepaliCorpus` & `NepaliBERT` Family)
- **`NepaliCorpus` (Large Monolingual Web Corpus)**:
  - Scrape and aggregate news, blogs, literary texts, Wikipedia, and government portals into a 500M+ token Devanagari Nepali corpus (`NepaliCorpus-News`, `NepaliCorpus-General`, `NepaliCorpus-Full`).
- **Foundation Transformer & Masked LMs**:
  - **`NepaliBERT`** / **`NepaliRoBERTa`** / **`NepaliAlBERT`**: Native masked language models pre-trained on full Devanagari `NepaliCorpus`.
  - **`NepaliGemma-2B` & `NepaliGemma-7B`**: Domain-adapted instruction/generative LLMs for Nepali.
  - **`NepaliFT`**: FastText subword embeddings trained on full Devanagari text.

### 8.2 Code-Mixed Romanized + Devanagari Social Media Benchmark (`NeCorpus` & `NeBERT`)
- **`NeCorpus` (Code-Mixed Nepglish Social Media Corpus)**:
  - 10M+ social media sentences combining Romanized Nepali + English (`NeCorpus-Roman`), Devanagari + English (`NeCorpus-Devanagari`), and mixed variants.
- **Code-Mixed Pre-trained Models**:
  - **`NeBERT`** & **`NeRoBERTa`**: Pre-trained on Nepglish social media text.
- **Supervised Code-Mixed Benchmarks**:
  - **`NeLID` (Language Identification)**: 12k+ samples for 3-class LID token-level annotation (*Nepali*, *English*, *Undefined*).
  - **`NeSent`**: Code-mixed Nepglish sentiment analysis dataset (Positive, Negative, Neutral).
  - **`NeHate`**: Code-mixed Nepglish hate speech identification dataset.

### 8.3 Native Supervised Benchmark Suite (`NepaliBench` / `MahaNLP` Equivalents)
- **`NepaliSQuAD` (Reading Comprehension & Extractive QA)**:
  - 140k+ context-question-answer triples in Devanagari Nepali for benchmark QA models (`NepaliSQuAD-BERT`).
- **`NepaliNews-MD` (Multi-Domain 12-Class Topic Classification)**:
  - 50k+ short, medium, and long news documents classified into 12 target categories (*Politics*, *Economics*, *Health*, *Crime*, *Sports*, *Agriculture*, *Entertainment*, *Technology*, *Education*, *Culture*, *International*, *Society*).
- **`NepaliNER` & `NepaliSocialNER`**:
  - 25k standard news NER & 18k social media NER with 8 entity classes (*PERSON*, *LOCATION*, *ORGANIZATION*, *EVENT*, *DATE*, *PRODUCT*, *DESIGNATION*, *MISC*).
- **`NepaliHate` & `NepaliHate-4Class`**:
  - 35k+ tweet/comment dataset annotated for 2-class (*Hate* vs *Not*) and 4-class (*Hate*, *Offensive*, *Profane*, *Neutral*).
- **`NepaliSent-MD` (Multi-Domain Sentiment Corpus)**:
  - 60k+ samples across 4 diverse domains (*Nepali Movie Reviews*, *TV/Youtube Subtitles*, *Generic Tweets*, *Political Tweets*).
- **`NepaliSBERT` & `IndicSBERT-Nepali`**:
  - Sentence-BERT models for native Nepali sentence similarity, semantic search, and cross-lingual NLI.
- **`NepaliEmotions` (LLM Synthetic & Human Annotated)**:
  - Multi-label emotion recognition (*Joy*, *Sadness*, *Anger*, *Fear*, *Surprise*, *Disgust*) created via CoTR prompting and LLM synthetic data generation.

### 8.4 Unified Open-Source Ecosystem (`nepaliNLP` Python Package)
- **`pip install nepaliNLP`**:
  - Create a unified Python library providing easy-to-use APIs for POS tagging, NER, Sentiment Analysis, Lemmatization, Hate Speech Detection, and Machine Translation in simple, Pythonic calls:
```python
from nepaliNLP.tokenizer import tokenize
from nepaliNLP.sentiment import analyze_sentiment
from nepaliNLP.ner import get_entities

text = "मलाई नेपाली खाना एकदमै मन पर्छ।"
print(analyze_sentiment(text))
```

---

## 🏛️ 9. KMI-Linguistics Inspired Research: Cyberbullying, Speech Threat, Dialects & Endangered Language Tech

Inspired by the **K.M. Institute of Hindi & Linguistics (`kmi-linguistics`)**, **TRAC** (Trolling, Aggression & Cyberbullying Shared Tasks), and **VarDial** (Variation in Language) benchmarks:

### 9.1 Cyberbullying, Misogyny & Threat Detection (`TRAC-Nepali` & `SpeeD-Nepali`)
- **`TRAC-Nepali` (Aggression & Cyberbullying Identification)**:
  - Benchmark social media dataset annotated for **Aggressive vs. Non-Aggressive** and 3-class **Overtly Aggressive (OAG)**, **Covertly Aggressive (CAG)**, and **Non-Aggressive (NAG)** comments in Devanagari & Nepglish.
- **Misogyny & Gender-Based Violence Detection**:
  - Fine-grained dataset for identifying gendered harassment, misogyny, toxic speech, and online threats targeting women in Nepali social networks (TikTok, Facebook, Twitter, YouTube comments).
- **`speech-aggression-Nepali` (Audio Threat & Acoustic Aggression Analysis)**:
  - Audio speech dataset (Praat acoustic feature extraction + Whisper fine-tuning) to detect verbal threats, aggressive tone, and emotional intensity in spoken Nepali phone calls and audio logs.

### 9.2 Social Media Propaganda & Disinformation (`Propaganda-Nepali`)
- **Nepali Social Media Propaganda Detection**:
  - Corpus annotated for fine-grained propaganda techniques (e.g., *Name Calling*, *Loaded Language*, *Appeal to Fear*, *Flag-Waving*, *Exaggeration*, *Causal Oversimplification*) in Nepali political tweets, online portal headlines, and viral social media posts.

### 9.3 Pragmatic Politeness & Honorific Dynamics (`Nepali-Politeness`)
- **Pragmatic Politeness & Honorific Level Classification**:
  - Multi-turn dialogue corpus annotated for politeness levels across Nepali honorific tiers:
    - **Non-honorific** (`तँ` / *ta~*)
    - **Medial-honorific** (`तिमी` / *timii*)
    - **High-honorific** (`तपाईँ` / *tapaai~*)
    - **Royal-honorific** (`सरकार/मौसुफ` / *sarkaar/mausuph*)
  - Applications in customer care, healthcare, and educational AI assistants.

### 9.4 Regional Languages & Dialects of Nepal (`Nepal-Dialect-LID` & `VarDial-Nepal`)
- **`VarDial-Nepal` (Indo-Aryan & Tibeto-Burman Dialect/Language Identification)**:
  - Dataset for automatic Language/Dialect Identification among regional languages spoken in Nepal:
    - **Indo-Aryan Family**: *Doteli*, *Baitadeli*, *Tharu*, *Bhojpuri*, *Maithili*, *Awadhi*.
    - **Sino-Tibetan / Tamangic / Kiranti / Tibetan Family**: *Gurung*, *Tamang*, *Thakali*, *Magar*, *Kham*, *Kaike*, *Jirel*, *Sherpa*, *Sunwar*, *Khaling*, *Newar*.
- **`EndangeredLanguages-Nepal` (Digital Literacy & Language Preservation)**:
  - Educational tools, Gamified Scrabble/Spellings (`Nepali-mscrabble`), and digital lexicons/dictionaries for low-resource and endangered languages of Nepal (e.g., *Kaike*, *Kusunda*, *Jirel*, *Raute*).

---

## 🇧🇩 10. BUET CSE NLP Inspired Innovations: Generative AI, RAG, Multimodal VLLMs & Code-NLP for Nepali

Inspired by the **BUET CSE NLP Group** (creators of *BanglaBERT*, *BanglaT5*, *BanglaNLG*, *CrossSum*, *XL-Sum*, *CoDesc*, *Text2App*, *IllusionVQA*):

### 10.1 Native Generative Models & Value Alignment (`NepaliT5`, `NepaliGPT` & `RLHF-Nepali`)
- **`NepaliT5` & `NepaliNLG` Benchmarks**:
  - Pre-train sequence-to-sequence Transformer models (`NepaliT5-Base` / `NepaliT5-Large`) specifically for low-resource Nepali Natural Language Generation (NLG).
  - Benchmarks for Nepali abstractive summarization, text simplification, headline generation, and story completion.
- **LLM Human Value Alignment & Contextual Bias Benchmark (`NepaliContextualBias`)**:
  - Empirical study on how context length variations affect gender, caste, ethnicity, and regional biases in Nepali LLMs.
  - RLHF (Reinforcement Learning from Human Feedback) & DPO (Direct Preference Optimization) preference dataset in Devanagari Nepali.

### 10.2 Retrieval-Augmented Generation (`NepaliRAG` & Cross-Lingual Open-Domain QA)
- **`NepaliRAG` Framework & Knowledge Base**:
  - Dense Passage Retrieval (DPR) + RAG system trained on Nepalese legal codes (Muluki Ain), medical guidelines, school curriculum (CDC Nepal), and Wikipedia.
- **Knowledge-Grounded Hallucination Elimination**:
  - Fine-tuning retrieval-augmented LLMs to cite exact paragraph numbers and source documents when answering complex questions in Nepali.

### 10.3 Vision-Enhanced Large Language Models (`NepaliVLLM` & `IllusionVQA-Nepali`)
- **Nepali Multimodal Vision-Language Benchmarks**:
  - Integration of computer vision with Nepali LLMs for visual document understanding (OCR + layout), medical chart interpretation, and Nepalese art/landmark visual QA.
- **Optical Illusion & Cultural Visual Bias Dataset (`IllusionVQA-Nepali`)**:
  - Challenging visual perception test set evaluating whether Multimodal LLMs hallucinate or misinterpret visual cues when prompted in Nepali.

### 10.4 Dual-Teacher Paraphrase Knowledge Distillation (`NepaliParaphrase`)
- **High-Quality Nepali Paraphrase Dataset via MT Distillation**:
  - Synthetic paraphrase dataset generated by distilling forward (English $\rightarrow$ Nepali) and backward (Nepali $\rightarrow$ English) neural translation models into a compact student paraphrase model.

### 10.5 Code-NLP & Natural Language to Code (`Text2App-Nepali` & `CoDesc-Nepali`)
- **`Text2App-Nepali` (Natural Language to App/Code)**:
  - Dataset mapping natural language instructions in Nepali to UI layouts, code scripts, or mobile app structures.
- **`CoDesc-Nepali` (Code-Description Parallel Corpus)**:
  - Parallel dataset of Python/JavaScript function code snippets paired with detailed docstrings and comments in Devanagari Nepali.

---

## ☸️ 11. Samsaadhanii & Paninian Simulator Inspired Innovations: Traditional Grammar AI, Sandhi Splitters & Digital Classics for Nepali

Inspired by **Samsaadhanii (साधनानि)** (Department of Sanskrit Studies, University of Hyderabad led by Prof. Amba Kulkarni & INRIA):

### 11.1 Nepali Traditional Grammar Simulator & Rule Engine (`NepaliGrammarSim`)
- **Nepali Grammar Derivation Simulator**:
  - Rule-engine simulating traditional Nepali grammar rules (*Hemraj Pande's Chandrika*, *Somnath Sigdel's Madhyachandrika*, *Nepali Vyakaran*) step-by-step to display exact derivation paths for nouns, verbs, and compounds.
- **Morphological Generators (`Niyama-Nispadika`)**:
  - Exact rule-based generators for Nepali Nominal Inflections (`नामरूप`), Verbal Tense-Aspect-Mood (`क्रियारूप`), Krt Participles (`कृदन्त`), and Taddhita Suffixes (`तद्धित`).

### 11.2 Nepali Sandhi Splitter & Compound Analyzer (`NepaliSandhi` & `Samasa-Nispadika`)
- **Nepali Sandhi Joiner & Splitter (`NepaliSandhi-Splitter`)**:
  - Tool for automatic segmentation and joining of phonetic sandhi junctions (Svar, Vyanjan, and Visarga sandhi) in classical and modern Nepali literature.
- **Nepali Compound Analysis & Generation (`NepaliSamasa`)**:
  - Compound word generator and parser classifying Nepali compounds (*Tatpurusha*, *Karmadharaya*, *Dvandva*, *Bahuvrihi*, *Avyayibhava*, *Dvigu*) with underlying semantic relation graphs.

### 11.3 Lexicographical Knowledge Networks & Dhatupatha (`NepaliSabdakosh-Net`)
- **`Nepali-Amarakosha-Net` (Semantic Knowledge Network)**:
  - Digital graph representation of traditional Nepali dictionaries (*Nepali Brihat Sabdakosh*, *Samakalin Nepali Sabdakos*) mapping synonyms, hypernyms, hyponyms, and semantic relations into a connected Knowledge Graph.
- **Nepali Verb Root Database (`NepaliDhatupatha`)**:
  - Structured concordance of Nepali verb roots (धातु) with transitive/intransitive classifications, causativization rules, and passive transformations.

### 11.4 Analyzed Classical & Educational E-Books (`Annotated-Nepali-Corpus`)
- **Deeply Annotated Nepali Literary E-Reader (`Savisleshana-Nepali-Grantha`)**:
  - Tokenized, POS-tagged, morphologically parsed, and dependency-analyzed e-books for classic Nepali literature (*Bhanubhakta's Ramayana*, *Laxmi Prasad Devkota's Muna Madan*, *Siddhicharan Shrestha's poems*, *Muluki Ain*).
  - Providing word-by-word glosses, morphological breakdowns, and syntax trees in an interactive dashboard.

### 11.5 Traditional Logic & Argumentation Graph Visualizer (`NepaliNyaya-Graph`)
- **Formal Argumentation & Rhetoric Diagramming**:
  - Semi-automatic visual parser for complex formal logic, legal arguments, and philosophical texts written in Nepali.

---

## 🇮🇳 12. AI4Bharat Inspired Ecosystem: Building `AI4Nepal` & `Bhashini-Nepal` Open-Source Infrastructure

Inspired by **AI4Bharat** (IIT Madras research lab led by Mitesh Khapra, Pratyush Kumar, Anoop Kunchukuttan & Bhashini):

### 12.1 Large-Scale Speech Recognition & Spoken Corpora (`NepalVoices` & `Kathbath-Nepali`)
- **`NepalVoices` (Nationwide District-Level Spoken Speech Corpus)**:
  - 5,000+ hours of transcribed speech collected across all 77 districts of Nepal, capturing diverse accents, age groups, and spoken dialects (Nepali, Maithili, Bhojpuri, Tharu, Tamang, Newar).
- **`Kathbath-Nepali` & `Vistaar-Nepali` (Read & Conversational ASR Benchmark)**:
  - Benchmark datasets for evaluating Whisper, IndicWav2Vec, and Conformer ASR models on spontaneous conversational Nepali speech, noisy environments, and voice queries.
- **`Shrutilipi-Nepali` & `Dhwani` (Mining Speech from Broadcast Media)**:
  - Automated pipeline to mine and align audio-transcript pairs from Nepali news channels, radio broadcasts, podcasts, and government proceedings.

### 12.2 Studio-Quality Expressive Text-to-Speech (`Rasa-Nepali` & `Lahaja`)
- **`Rasa-Nepali` (Studio-Recorded Multi-Voice Expressive TTS Dataset)**:
  - Studio-recorded high-fidelity multi-speaker dataset with professional voice artists across emotions (*Joy*, *Sadness*, *Formal News*, *Storytelling*) in Devanagari Nepali.
- **`IndicOOV-Nepali` & `Lahaja` (Dialectal Pronunciation Lexicon & OOV Handling)**:
  - Grapheme-to-Phoneme (G2P) conversion rules and pronunciation lexicons for Nepali Out-Of-Vocabulary (OOV) and loan words.

### 12.3 Large-Scale Parallel Corpora & Neural Machine Translation (`Samanantar-Nepali` & `BPCC-Nepali`)
- **`Samanantar-Nepali` / `BPCC-Nepali` (Parallel Corpus Collection)**:
  - 5M+ sentence pairs of parallel corpora between English $\leftrightarrow$ Nepali, Hindi $\leftrightarrow$ Nepali, and regional languages of Nepal (Bhojpuri/Maithili $\leftrightarrow$ Nepali).
- **`MQM-Nepali` (Multidimensional Quality Metrics for Translation)**:
  - Expert human evaluations quantifying fluency, adequacy, and terminology errors in English-Nepali machine translations.

### 12.4 Script & Transliteration Engineering (`Aksharantar-Nepali` & `IndicXlit`)
- **`Aksharantar-Nepali` (Large-Scale Roman-to-Devanagari Transliteration)**:
  - 2M+ word pairs for Romanized Nepali to Devanagari transliteration, capturing informal social media spellings, abbreviations, and phonetic variations.
- **`Bhasha-Abhijnaanam-Nepali` (Script & Language Identification)**:
  - Token-level and sentence-level language identification across 12 languages spoken in Nepal.

### 12.5 Large Language Models, Instructions & Benchmark Suites (`Sangraha-Nepali` & `Airavata-Nepali`)
- **`Sangraha-Nepali` & `NepaliCorpV2`**:
  - Massively deduplicated, clean web corpus (1B+ tokens) combining news, literature, government gazettes, Wikipedia, and OCR-scanned historical archives.
- **`NepaliInstruct` & `NepaliAlign` (Instruction & Preference Alignment)**:
  - 100k+ high-quality instruction-following prompts grounded in Nepalese culture, history, geography, law, and local context (`NepaliInstruct`), with preference datasets (`NepaliAlign`) for DPO/RLHF tuning.
- **`NepaliXTREME` & `NepaliGLUE` Benchmark Suite**:
  - Multi-task evaluation suite covering NLI, NER (`Naamapadam-Nepali`), Coreference Resolution, Paraphrase Detection, and QA across diverse Nepalese domains.

### 12.6 Document Layout Parsing & Devanagari OCR (`Pralekha-Nepali`)
- **`Pralekha-Nepali` (Document Layout & Devanagari OCR Dataset)**:
  - Annotated dataset of scanned Nepali documents, newspapers, government notices, and land records (*Lalpurja*) for layout segmentation, bounding box detection, and Devanagari OCR text recognition.

---

## 🏛️ 13. IIIT Hyderabad LTRC & IIT Bombay CFILT Inspired Research: Grammar Correction, Quality Estimation, Disfluency & Medical AI for Nepali

Inspired by **IIIT Hyderabad LTRC** (Language Technologies Research Centre) and **CFILT - IIT Bombay** (led by Prof. Pushpak Bhattacharyya):

### 13.1 Multilingual Grammar Error Correction & Disfluency Parsing (`NepaliGEC` & `NepaliDisfluency`)
- **`NepaliGEC` / `Hi-GEC-Nepali` (Nepali Grammar Error Correction)**:
  - Benchmark dataset and Transformer models for automatically detecting and correcting spelling errors, case marker mismatches (*vibhakti*), subject-verb agreement breaks, and word-order disfluency in written Nepali student essays and web text.
- **`DISCO-Nepali` (Speech Disfluency Correction & Reduplication vs. Hesitation Parsing)**:
  - Dataset distinguishing natural linguistic reduplication (e.g., *"मिठो-मिठो"*, *"साना-साना"*) from speech hesitations, stutters, and repetitions in Nepali spoken audio and ASR transcripts.

### 13.2 Machine Translation Quality Estimation & Automatic Post-Editing (`NepaliQE` & `NepaliAPE`)
- **`NepaliQE` (Quality Estimation for Machine Translation)**:
  - Reference-free Quality Estimation framework predicting translation quality scores ($0-100\%$) for English $\leftrightarrow$ Nepali MT outputs without requiring gold-standard reference translations.
- **`NepaliAPE` (Automatic Post-Editing)**:
  - Post-editing models trained on synthetic & human-edited error patterns to refine and polish raw machine translations into fluent formal Devanagari Nepali.

### 13.3 Knowledge-Infused Medical AI & Radiology Report Generation (`NepaliMedAI` & `KGVL-BART-Nepali`)
- **`NepaliMedAI` (Symptom-to-Disease Diagnosis Virtual Assistant)**:
  - Multi-turn clinical dialogue dataset linking patient symptoms in Nepali to medical knowledge graphs (ICD-10, Ayush, local medicinal plant remedies).
- **`KGVL-BART-Nepali` (Radiology & Medical Report Generation)**:
  - Multimodal model generating structured radiology/x-ray diagnostic reports in Nepali grounded in clinical Knowledge Graphs.

### 13.4 Indian/Nepalese Context Bias & Stereotype Benchmarks (`BharatBBQ-Nepali` & `BIStereo-Nepali`)
- **`BharatBBQ-Nepali` (Multilingual Social Bias Benchmark)**:
  - Question Answering evaluation set designed to detect socio-cultural biases (caste, gender, religion, geographic region, body image stereotypes) in Nepali LLMs.
- **`StereoDetect-Nepali`**:
  - Social psychological framework measuring stereotype vs. anti-stereotype perpetuation in Devanagari language models.

### 13.5 Document-Controlled Code Generation & DSL Constraint Evaluation (`DocCGen-Nepali`)
- **Document-Controlled Code & DSL Generation**:
  - Evaluating LLMs on generating code constrained by domain-specific documentation written in Nepali.

### 13.6 Information Retrieval & Enterprise Search (`NepaliIRSuite`)
- **`IndicIRSuite-Nepali` (Neural Information Retrieval)**:
  - BM25 + Dense Retrieval benchmark for enterprise search, news article retrieval, and legal document search across Devanagari Nepali corpora.

---

## 🏛️ 14. CFILT-IITB Open Resources Inspired Initiatives: WordNets, Cognates, Pragmatics & Cultural Heritage AI for Nepali

Inspired by **CFILT - IIT Bombay Open Resources & Datasets** (IndoWordNet, SentiWordNet, PUB, Cognates & False Friends Challenge):

### 14.1 `NepaliWordNet` & `NepaliSentiWordNet` (Lexical Knowledge Graph & Sentiment Synsets)
- **`NepaliWordNet` (Devanagari Lexical Knowledge Base)**:
  - Interlinked database of Nepali synsets (Nouns, Verbs, Adjectives, Adverbs) aligned with IndoWordNet and Princeton WordNet, mapping hypernymy, hyponymy, meronymy, and antonymy.
- **`NepaliSentiWordNet` & Sense-Annotated Polarity Corpus**:
  - Assigning Positivity, Negativity, and Objectivity scores ($0.0 - 1.0$) to each synset in `NepaliWordNet` across Movie, Tourism, Hospitality, and Product domains.

### 14.2 Cognates & False Friends Identification across Indic Languages (`Cognate-Nepali`)
- **Nepali-Hindi-Sanskrit Cognate & False Friend Challenge Dataset**:
  - Dataset of word pairs identifying true cognates (e.g., *"काम"*, *"जल"*) vs. **False Friends** (words with identical orthography/phonetics but different semantic meanings across Hindi, Nepali, and Marathi, e.g., *"छात्र"*, *"बाटो"*).
  - Neural models for cross-lingual transfer without semantic distortion.

### 14.3 Factoid-to-Full Length Answer Generation (`NepaliAnswerGen`)
- **Natural Full-Length Answer Generation (`Factoid2Full-Nepali`)**:
  - Dataset and seq2seq models transforming short, factual answers (e.g., *"कठमाडौँ"*) into natural, grammatically complete, human-like full sentences (e.g., *"नेपालको राजधानी शहर काठमाडौँ हो।"*).

### 14.4 Cultural & Literary Heritage Digitization (`NepaliLiteraryHeritage`)
- **Nepali Classical Verse & Philosophy Corpora**:
  - Digitized, meter-annotated (*Chhanda*), and sense-aligned corpora for Nepali literary classics (*Bhanubhakta Acharya*, *Laxmi Prasad Devkota*, *Balkrishna Sama*, *Bhairav Aryal's Satire*, *Mundhum*, *Charya Giti*).
  - Automatic *Chhanda* (poetic meter) identification and verse paraphrase generation.

### 14.5 Pragmatics Understanding Benchmark (`PUB-Nepali`)
- **`PUB-Nepali` (Pragmatics & Implicature Evaluation)**:
  - Benchmark testing whether LLMs understand conversational implicatures, sarcasm, indirect requests, and contextual metaphors in Nepali dialogue.

---

## 🌐 15. Indic NLP Catalog Inspired Roadmap: Comprehensive `Nepali-NLP-Catalog` & Himalayan Resource Taxonomy

Inspired by **The Indic NLP Catalog** (AI4Bharat & Anoop Kunchukuttan):

### 15.1 Unified Language Platform & Standards (`ULCA-Nepal` & `Bhashini-Nepal API`)
- **`ULCA-Nepal` (Universal Language Contribution API for Nepal)**:
  - Standardized open platform for discovering, benchmark testing, and uploading Nepali datasets, models, and evaluation metrics across spoken dialects and Devanagari script formats.

### 15.2 Massive Monolingual & Multilingual Web Corpora (`NepaliCorpV3` & `HimalayanCorp`)
- **`NepaliCorpV3` (Multi-Billion Token Monolingual Web Corpus)**:
  - Aggregating web crawls, CommonCrawl subsets, Wikipedia dumps, and digitizing news archives into a 1B+ token Devanagari corpus.
- **`HimalayanCorp` (Multi-Language Corpus of Nepal)**:
  - Text corpora spanning non-scheduled and regional languages of Nepal (e.g., *Doteli*, *Bhojpuri*, *Maithili*, *Tamang*, *Gurung*, *Newar*, *Tharu*, *Limbu*, *Sherpa*).

### 15.3 Large-Scale Parallel Translation & Transliteration Benchmarks (`Nepali-Parallel-Hub`)
- **`Nepali-Parallel-Hub` (Aggregated En-Ne & Regional Parallel Corpora)**:
  - Consolidating and expanding parallel translation datasets (Kathmandu University 1.8M, CLE, NLLB-Mined, BPCC, FLORES-200) into a single 5M+ sentence pair benchmark.
- **`Aksharantar-Nepali` & `IndicXlit-Nepal`**:
  - Expanded Romanized Nepali to Devanagari transliteration corpus (2M+ pairs) covering internet slang, SMS contractions, and phonetic spelling variants.

### 15.4 Speech & Spoken Corpora Expansion (`NepaliVoices-1000` & `OpenSLR-Ne`)
- **`NepaliVoices-1000` (Nationwide Multi-Speaker ASR Corpus)**:
  - Expanding OpenSLR (~157k utterances) and NNC Spoken Corpus into a 1,000+ hour multi-speaker, multi-accent read and spontaneous speech dataset covering all 7 provinces of Nepal.

### 15.5 Unified Open-Source Tooling Suite (`nepali-nlp-toolkit`)
- **`nepali-nlp-toolkit` (Native Python Package)**:
  - Python interface consolidating Unicode normalization, Devanagari-to-Roman transliteration, sentence segmentation, POS tagging, NER, and morphological analysis into a single lightweight dependency:
```python
import nepali_nlp as nn

text = "श्रीमान् रामप्रसादज्यू काठमाडौँ आउनुभयो।"
tokens = nn.tokenize(text)
entities = nn.ner(text)
```

---

## 🔮 16. Frontier AI & Next-Gen Agentic LLM Innovations (2025–2026 Roadmap for Nepali AI)

Inspired by cutting-edge 2025–2026 research in **Agentic Function Calling**, **Cultural Alignment Guardrails (BanglaGuard/UbuntuGuard)**, **Synthetic Data Evol-Instruct**, and **Long-Context Grounded Reasoning**:

### 16.1 Native Nepali Function Calling & Tool-Use Agent Benchmark (`NepaliFuncBench`)
- **`NepaliFuncBench` (BFCL-style Agentic Tool-Use Evaluation)**:
  - Benchmark testing whether LLMs can accurately parse function schemas, generate structured JSON tool parameters, and invoke external APIs given natural language user requests in Devanagari Nepali.
  - Covers single-tool calls, multi-turn tool interaction, parallel function execution, and API error recovery (e.g., searching government registries, weather services, banking transactions in Nepali).

### 16.2 Culturally Grounded Safety & Red-Teaming Guardrails (`NepaliGuard`)
- **`NepaliGuard` (Culturally Aligned Safety & Red-Teaming Benchmark)**:
  - Safety, refusal, and alignment benchmark grounded in Nepalese cultural norms, ethical standards, legal statutes, and social harmony (addressing caste sensitivity, religious respect, and regional harmony).
- **Multi-Turn Adversarial Red-Teaming**:
  - Evaluation suite testing guardrail bypasses, jailbreak vulnerability, and goal hijacking across Devanagari text and Romanized Nepglish social media prompts.

### 16.3 Synthetic Instruction Tuning & Preference Optimization (`EvolInstruct-Nepali`)
- **`EvolInstruct-Nepali` (Synthetic Instruction Augmentation & DPO)**:
  - Pipeline using Self-Instruct and Evol-Instruct (in-depth mutation, constraint addition, multi-step reasoning expansion) to synthetically generate high-quality Devanagari instruction-following datasets.
  - Direct Preference Optimization (DPO) datasets curated with human preference pairs for fine-tuning open LLMs (Gemma, Llama, Qwen).

### 16.4 Long-Context Legal & Policy Reasoning (`MulukiAin-RAG`)
- **Long-Context Legal & Constitutional QA (`MulukiAin-RAG`)**:
  - Benchmark for long-context understanding across Nepalese legal codes (*Civil Code / Muluki Ain*, *Constitution of Nepal 2072*, *Supreme Court Precedents*).
  - Evaluating 32k–128k token context retrieval, paragraph-level legal citation, and reasoning without hallucination.

### 16.5 Agentic Multi-Agent Collaboration Framework for Nepalese Public Services (`NepaliGovAgent`)
- **Multi-Agent Governance & Service Automation**:
  - Framework of specialized AI sub-agents (Taxation Agent, Citizenship Guidance Agent, Agricultural Advisory Agent, Health Assistance Agent) communicating in Devanagari to resolve complex multi-step public service requests.








