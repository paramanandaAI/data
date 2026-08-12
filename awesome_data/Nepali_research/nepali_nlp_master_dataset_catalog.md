# Nepali NLP Master Dataset Directory

A data-centric, production-grade catalog of **150+ Nepali and Himalayan language datasets**, text corpora, parallel translation pairs, speech acoustic files, computer vision benchmarks, and instruction-tuning suites for AI/LLM development.

---

## 📌 Pretraining & Large Text Corpora (>100GB Aggregated Data)

| Dataset Name | Primary Domain | Volume / Sample Size | Format & Access | Key Characteristics & Citation |
| :--- | :--- | :--- | :--- | :--- |
| **IRIISNEPAL Nepali Text Corpus** | 99 News Websites | 6.4 Million Articles, 10.1 GB | HuggingFace (`IRIISNEPAL/nepali-text-corpus`) | Pre-training corpus for Devanagari LMs (*IRIIS 2024*) |
| **CC100-Nepali** | Web Common Crawl | 200 GB Uncompressed | MetaText (`cc100-nepali`) | Web text foundation for multilingual Llama/Gemma |
| **OSCAR Corpus Nepali** | Common Crawl Subset | 3.8 GB, 100M+ Sentences | Kaggle (`hsebarp/oscar-corpus-nepali`) | Deduplicated language modeling text |
| **Nepali National Corpus (NNC)** | Written, Spoken, Parallel | 14 Million Words | ELRA Catalogue (`ELRA-W0076`) | Core 15 genres, 802k sample words + 1.4M general web text (*Yadava 2008*) |
| **Lamsal (2020) News Corpus** | Online News Portals | 90 Million Words + 0.5M Vectors | IEEE DataPort | Compiled news text; includes 300D Word2Vec embeddings |
| **LDC-IL Raw Text Corpus** | 6 Domains | 7 Million Words | CIIL LDC-IL | Aesthetics (57.7%), Mass Media (32.2%), Sci-Tech (1.14%) (*Choudhary 2019*) |
| **Nepali News Dataset Large** | 20 Categories | 25,000+ Articles | Kaggle (`ashokpant/nepali-news-dataset-large`) | Cleaned news articles for classification (*Shahi 2018*) |
| **NepaliLinguistic Dataset** | 17 News Categories | 35,651 Documents | IEEE DataPort | High-quality text with supervised codebook vectors (*Sitaula 2021*) |
| **Nepali Wikipedia Articles** | Encyclopedia | 39,000+ Full Articles | Kaggle (`disisbig/nepali-wikipedia-articles`) | Wiki markup stripped Devanagari text |
| **np20ng (Nepali 20 Newsgroup)** | 20 News Categories | 200,000+ Documents | HuggingFace (`Suyogyart/np20ng`) | Adapted from 20 Newsgroups benchmark |

---

## 🏷️ NLU, NER & QA Datasets

| Dataset Name | Task / Annotation Scheme | Size / Instance Count | Access Path | Reference & Description |
| :--- | :--- | :--- | :--- | :--- |
| **NLUE Benchmark** | NLU Suite (9 Classification, 3 Structural) | Multi-task Evaluation | arXiv:2411.19244 | Nepali GLUE-style evaluation framework |
| **EverestNER** | Named Entity Recognition (8 Types) | 50,000+ Sentences | Kaggle (`jeevanchapagain/everestner`) | Devanagari NER dataset |
| **DanfeNER** | Named Entity Recognition (Cultural/Geo) | 25,000+ Sentences | Kaggle (`jeevanchapagain/danfener`) | Cultural and geographical entity focus |
| **NepaliNER (Ebiquity v2)** | NER (PER, LOC, ORG) | 79,087 Entities | GitHub (`oya163/nepali-ner`) | Benchmark NER corpus (*Singh et al. 2019*) |
| **16NepaliNews** | News Classification (16 Classes) | 14,364 Documents | GitHub (`sndsabin/Nepali-News-Classifier`) | Standard news category benchmark (*KU 2021*) |
| **Nepali Health Q&A Corpus** | Extractive Medical QA | 3,000+ Q&A Pairs | Kaggle (`thedevastator/nepali-health-q-a-corpus`) | Health forum medical advice QA |

---

## 🎙️ Speech & Acoustics Datasets (ASR & TTS)

| Dataset Name | Task / Domain | Audio Duration / Clips | Format & Access | Description |
| :--- | :--- | :--- | :--- | :--- |
| **OpenSLR-54** | ASR (Speech-to-Text) | 157,000 Utterances (400+ Hours) | `openslr.org/54` | Google-supported read speech corpus; gold ASR benchmark |
| **OpenSLR-43** | TTS (Text-to-Speech) | Single Speaker High Quality | `openslr.org/43` | Studio recorded single-speaker speech for TTS models |
| **Mozilla Common Voice (Nepali)** | Crowdsourced ASR | 100,000+ Audio Clips | Mozilla Common Voice | Diverse multi-speaker conversational & read speech |
