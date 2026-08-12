> Source: `sources/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

## 🐙 5. Open-Source GitHub Repositories & Tooling Registry

| Category | Repository Link | Focus / Capabilities |
|---|---|---|
| **E-Commerce** | [`superryeti/Daraz-online-shopping-data-corpus`](https://github.com/superryeti/Daraz-online-shopping-data-corpus) | Nepali e-commerce product catalog and categories |
| **Wikipedia Dump** | [`shekharkoirala/nepali_wikipedia_curpos`](https://github.com/shekharkoirala/nepali_wikipedia_curpos) | Nepali Wikipedia full article dump scraper |
| **Speech Recognition** | [`ishworrsubedii/nepali_speech-to-text_datasets`](https://github.com/ishworrsubedii/nepali_speech-to-text_datasets) | Audio recordings paired with Devanagari text |
| **Code-Switched Speech** | [`Aadarshttech/nepali-english-codeswitched-whisper`](https://github.com/Aadarshttech/nepali-english-codeswitched-whisper) | Nepali-English code-switched Whisper fine-tuning |
| **Transliteration** | [`Shahil050/romanized_nepali_dataset`](https://github.com/Shahil050/romanized_nepali_dataset) | Parallel Romanized Nepali to Devanagari text |
| **Tamang Translation** | [`binayachaudari/Nepali-Tamang-MT-Data`](https://github.com/binayachaudari/Nepali-Tamang-MT-Data) | Tamang to Nepali machine translation pairs |
| **Named Entity (NER)** | [`nowalab/DanfeNER`](https://github.com/nowalab/DanfeNER) | Nepali tweet Named Entity Recognition tags |
| **POS Tagging** | [`SujilDevkota/NepaliCorpus-POS-Tags`](https://github.com/SujilDevkota/NepaliCorpus-POS-Tags) | Part-of-Speech tagged Devanagari corpus |
| **Bias & Safety** | [`ios-ioe/Nepali-Bias-Language-Dataset`](https://github.com/ios-ioe/Nepali-Bias-Language-Dataset) | Social bias and discrimination evaluation |
| **Vision (Flickr8k)** | [`ShubhaPradhan/Nepali-Flickr8k-Dataset`](https://github.com/ShubhaPradhan/Nepali-Flickr8k-Dataset) | Flickr8k images with translated Nepali captions |
| **Vision (Flickr30k)** | [`bipeshrajsubedi/Flickr30k_Nepali_Dataset`](https://github.com/bipeshrajsubedi/Flickr30k_Nepali_Dataset) | Flickr30k images with translated Nepali captions |
| **License Plates** | [`Alish545/Number-Plate-Project`](https://github.com/Alish545/Number-Plate-Project) | YOLOv8n Nepalese license plate OCR |
| **Handwritten HTR** | [`dahalsweekar/Nepali-Handwritten-Dataset-for-Recognition`](https://github.com/dahalsweekar/Nepali-Handwritten-Dataset-for-Recognition) | Handwritten character image recognition |
| **Poetry & Meter** | [`12-Twelvve/poem_dataset`](https://github.com/12-Twelvve/poem_dataset) | Classical & modern Nepali poetry corpus |

---
## 🏥 6. Domain-Specific NLP Applications — Related Frameworks & Alternatives

> Citations of domain-specific NLP toolkits and models across application areas. These are referenced as comparative alternatives and methodological context — not necessarily Nepali-specific, but demonstrating the breadth of NLP application domains.

### 6.1 Legal NLP

| Repository | Focus | Citation Context |
|---|---|---|
| [`ICLRandD/Blackstone`](https://github.com/ICLRandD/Blackstone) | spaCy pipeline for unstructured legal text | ACL NLLP workshop |
| [`FudanDISC/DISC-LawLLM`](https://github.com/FudanDISC/DISC-LawLLM) | Chinese legal LLM for legal services | Reference for legal domain adaptation |
| [`LexPredict/lexpredict-lexnlp`](https://github.com/LexPredict/lexpredict-lexnlp) | Legal NLP feature extraction | Industry standard for legal text analytics |
| [`Liquid-Legal-Institute/Legal-Text-Analytics`](https://github.com/Liquid-Legal-Institute/Legal-Text-Analytics) | Curated legal text analytics resources | Reference for legal NLP pipeline design |

**Nepali Context:** Nepal legal domain Q&A datasets exist in `sources/sft/domain/legal/`. Constitution of Nepal, Civil Code, and Supreme Court judgments are primary sources.

### 6.2 Medical & Healthcare NLP

| Repository | Focus | Citation Context |
|---|---|---|
| [`medspacy/medspacy`](https://github.com/medspacy/medspacy) | Clinical NLP with spaCy | BioNLP shared tasks |
| [`allenai/scispacy`](https://github.com/allenai/scispacy) | Scientific/biomedical document processing | BioNLP, CLINLP |
| [`neuml/paperai`](https://github.com/neuml/paperai) | AI for medical and scientific papers | Clinical document understanding |
| [`SCIR-HI/Huatuo-Llama-Med-Chinese`](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese) | Chinese medical knowledge LLM | Reference for medical domain fine-tuning |

**Nepali Context:** Nepali medical conversation and health QA datasets exist in `sources/sft/domain/healthcare/`.

### 6.3 Finance & Economics NLP

| Repository | Focus | Citation Context |
|---|---|---|
| [`AI4Finance-Foundation/FinGPT`](https://github.com/AI4Finance-Foundation/FinGPT) | Open-source financial LLM | ACL FinNLP |
| [`The-FinAI/PIXIU`](https://github.com/The-FinAI/PIXIU) | Financial LLM, instruction data, benchmarks | Financial NLP evaluation |

**Nepali Context:** NEPSE share market and retail banking datasets exist in `sources/sft/domain/commerce/`.

### 6.4 Chinese NLP — Comparative Alternatives

> Chinese NLP toolkits are cited as methodological alternatives. Chinese and Nepali share Devanagari/CJK complexity in tokenization, morphology, and script normalization.

| Repository | Focus | Relevance to Nepali |
|---|---|---|
| [`hankcs/HanLP`](https://github.com/hankcs/HanLP) | Comprehensive Chinese NLP (NER, POS, parsing) | Morphologically rich language toolkit reference |
| [`Morizeyao/GPT2-Chinese`](https://github.com/Morizeyao/GPT2-Chinese) | Chinese GPT-2 training with BERT tokenizer | Low-resource LM training methodology |
| [`ymcui/Chinese-LLaMA-Alpaca-2`](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2) | Chinese LLaMA with extended vocabulary | Vocabulary extension methodology for Devanagari |
| [`brightmart/nlp_chinese_corpus`](https://github.com/brightmart/nlp_chinese_corpus) | Large-scale Chinese corpus construction | Corpus curation methodology reference |
| [`ChineseGLUE/ChineseGLUE`](https://github.com/ChineseGLUE/ChineseGLUE) | Chinese language understanding benchmark | Benchmark design reference for Nepali NLUE |
| [`crownpku/Awesome-Chinese-NLP`](https://github.com/crownpku/Awesome-Chinese-NLP) | Curated Chinese NLP resources | Resource curation methodology |
| [`CLUEbenchmark/CLUECorpus2020`](https://github.com/CLUEbenchmark/CLUECorpus2020) | Chinese pre-training corpus (100G) | Large-scale corpus extraction reference |

### 6.5 Text Classification & Sentiment Analysis

| Repository | Focus |
|---|---|
| [`songyouwei/ABSA-PyTorch`](https://github.com/songyouwei/ABSA-PyTorch) | Aspect-based sentiment analysis |
| [`brightmart/text_classification`](https://github.com/brightmart/text_classification) | Text classification models |
| [`yao8839836/text_gcn`](https://github.com/yao8839836/text_gcn) | Graph-based text classification (AAAI 2019) |
| [`bfelbo/DeepMoji`](https://github.com/bfelbo/DeepMoji) | Emotion, sarcasm detection |
| [`yongzhuo/Keras-TextClassification`](https://github.com/yongzhuo/Keras-TextClassification) | Multi-label text classification |

### 6.6 Named Entity Recognition & Information Extraction

| Repository | Focus |
|---|---|
| [`Franck-Dernoncourt/NeuroNER`](https://github.com/Franck-Dernoncourt/NeuroNER) | Neural NER with state-of-the-art results |
| [`princeton-nlp/PURE`](https://github.com/princeton-nlp/PURE) | Entity and relation extraction (NAACL 2021) |
| [`zjunlp/DeepKE`](https://github.com/zjunlp/DeepKE) | Knowledge graph extraction (EMNLP 2022) |
| [`monarch-initiative/ontogpt`](https://github.com/monarch-initiative/ontogpt) | LLM-based ontological extraction |
| [`cocacola-lab/ChatIE`](https://github.com/cocacola-lab/ChatIE) | Chat-based information extraction |

### 6.7 Grammar Error Correction & Text Correction

| Repository | Focus |
|---|---|
| [`grammarly/gector`](https://github.com/grammarly/gector) | GECToR: sequence tagging for GEC (BEA-20) |
| [`neuspell/neuspell`](https://github.com/neuspell/neuspell) | NeuSpell neural spelling correction |
| [`bminixhofer/nlprule`](https://github.com/bminixhofer/nlprule) | Fast low-resource text correction (Rust) |
| [`textlint/textlint`](https://github.com/textlint/textlint) | Pluggable text linter |

### 6.8 Question Answering & Reading Comprehension

| Repository | Focus |
|---|---|
| [`allenai/bi-att-flow`](https://github.com/allenai/bi-att-flow) | BiDAF for machine reading comprehension |
| [`deepset-ai/FARM`](https://github.com/deepset-ai/FARM) | Transfer learning for QA |
| [`PaddlePaddle/RocketQA`](https://github.com/PaddlePaddle/RocketQA) | Dense retrieval for QA |
| [`namisan/mt-dnn`](https://github.com/namisan/mt-dnn) | Multi-task deep neural networks for NLU |

### 6.9 Summarization

| Repository | Focus |
|---|---|
| [`allenai/RL4LMs`](https://github.com/allenai/RL4LMs) | RL fine-tuning for summarization |
| [`DerwenAI/pytextrank`](https://github.com/DerwenAI/pytextrank) | TextRank phrase extraction |
| [`summanlp/textrank`](https://github.com/summanlp/textrank) | TextRank for Python 3 |
| [`xcfcode/Summarization-Papers`](https://github.com/xcfcode/Summarization-Papers) | Summarization paper collection |

### 6.10 Translation & Transliteration

| Repository | Focus |
|---|---|
| [`argosopentech/argos-translate`](https://github.com/argosopentech/argos-translate) | Open-source offline translation |
| [`babylonhealth/fastText_multilingual`](https://github.com/babylonhealth/fastText_multilingual) | Multilingual word vectors (78 languages) |
| [`Unbabel/COMET`](https://github.com/Unbabel/COMET) | Neural MT evaluation framework |
| [`Maluuba/nlg-eval`](https://github.com/Maluuba/nlg-eval) | NLG evaluation metrics |

### 6.11 Dialogue & Conversational AI

| Repository | Focus |
|---|---|
| [`RasaHQ/rasa`](https://github.com/RasaHQ/rasa) | Open-source conversational AI framework |
| [`deeppavlov/DeepPavlov`](https://github.com/deeppavlov/DeepPavlov) | End-to-end dialog systems |
| [`lukalabs/cakechat`](https://github.com/lukalabs/cakechat) | Emotional generative dialog |
| [`uber-archive/plato-research-dialogue-system`](https://github.com/uber-archive/plato-research-dialogue-system) | Flexible dialog system platform |

### 6.12 Topic Modeling

| Repository | Focus |
|---|---|
| [`MilaNLProc/contextualized-topic-models`](https://github.com/MilaNLProc/contextualized-topic-models) | BERT-based contextualized topic models (EACL/ACL 2021) |
| [`MIND-Lab/OCTIS`](https://github.com/MIND-Lab/OCTIS) | Topic model optimization and evaluation (EACL 2021) |
| [`piskvorky/gensim`](https://github.com/piskvorky/gensim) | Topic modelling for humans |

---
## ⚙️ 7. Frameworks & Toolkits — Reference Catalog

> Core NLP frameworks, tokenizers, and embedding toolkits. Referenced for methodology comparison and tool selection.

### 7.1 General NLP Frameworks

| Repository | Focus |
|---|---|
| [`explosion/spaCy`](https://github.com/explosion/spaCy) | Industrial-strength NLP in Python |
| [`stanfordnlp/stanza`](https://github.com/stanfordnlp/stanza) | Stanford NLP Python library |
| [`flairNLP/flair`](https://github.com/flairNLP/flair) | State-of-the-art NLP framework |
| [`allenai/allennlp`](https://github.com/allenai/allennlp) | Open-source NLP research library |
| [`nltk/nltk`](https://github.com/nltk/nltk) | Natural Language Toolkit |
| [`JohnSnowLabs/spark-nlp`](https://github.com/JohnSnowLabs/spark-nlp) | State-of-the-art NLP on Spark |
| [`goru001/inltk`](https://github.com/goru001/inltk) | Natural Language Toolkit for Indic Languages |

### 7.2 Tokenizers

| Repository | Focus |
|---|---|
| [`huggingface/tokenizers`](https://github.com/huggingface/tokenizers) | Fast state-of-the-art tokenizers |
| [`bheinzerling/bpemb`](https://github.com/bheinzerling/bpemb) | Pre-trained BPE subword embeddings (275 languages) |
| [`VKCOM/YouTokenToMe`](https://github.com/VKCOM/YouTokenToMe) | Unsupervised text tokenizer |
| [`nlp-uoregon/trankit`](https://github.com/nlp-uoregon/trankit) | Light-weight multilingual NLP toolkit |
| [`cbaziotis/ekphrasis`](https://github.com/cbaziotis/ekphrasis) | Text processing for social networks |

### 7.3 Embeddings & Similarity

| Repository | Focus |
|---|---|
| [`princeton-nlp/SimCSE`](https://github.com/princeton-nlp/SimCSE) | Contrastive learning of sentence embeddings (EMNLP 2021) |
| [`shibing624/text2vec`](https://github.com/shibing624/text2vec) | Text to vector (Word2Vec, Sentence-BERT, CoSENT) |
| [`explosion/sense2vec`](https://github.com/explosion/sense2vec) | Contextually-keyed word vectors |
| [`MinishLab/model2vec`](https://github.com/MinishLab/model2vec) | Fast state-of-the-art static embeddings |
| [`thunlp/WantWords`](https://github.com/thunlp/WantWords) | Open-source reverse dictionary |

### 7.4 Data Augmentation & Annotation

| Repository | Focus |
|---|---|
| [`argilla-io/argilla`](https://github.com/argilla-io/argilla) | Collaboration tool for dataset building |
| [`jasonwei20/eda_nlp`](https://github.com/jasonwei20/eda_nlp) | Data augmentation for NLP (EMNLP 2019) |
| [`QData/TextAttack`](https://github.com/QData/TextAttack) | Adversarial attacks and data augmentation |
| [`makcedward/nlpaug`](https://github.com/makcedward/nlpaug) | Data augmentation for NLP |

### 7.5 Corpus Collection & Cleaning

| Repository | Focus |
|---|---|
| [`adbar/trafilatura`](https://github.com/adbar/trafilatura) | Web crawling and text extraction |
| [`ChenghaoMou/text-dedup`](https://github.com/ChenghaoMou/text-dedup) | All-in-one text de-duplication |
| [`fhamborg/news-please`](https://github.com/fhamborg/news-please) | News web crawler and extractor |
| [`huggingface/datasets`](https://github.com/huggingface/datasets) | Hub of ready-to-use datasets |

### 7.6 Safety, Privacy & Adversarial

| Repository | Focus |
|---|---|
| [`unitaryai/detoxify`](https://github.com/unitaryai/detoxify) | Toxic comment detection |
| [`thunlp/OpenAttack`](https://github.com/thunlp/OpenAttack) | Textual adversarial attack package |
| [`data-privacy-stack/presidio`](https://github.com/data-privacy-stack/presidio) | PII detection and anonymization |
| [`capitalone/DataProfiler`](https://github.com/capitalone/DataProfiler) | Dataset schema and statistics |

---
## 🇳🇵 8. Nepali HuggingFace Ecosystem — Models & Spaces (split from section 8; datasets moved to Nepali_data/huggingface_dataset_catalog.md)

### 8.2 Nepali Models on HuggingFace (656+)

**Encoder Models (BERT/RoBERTa):**
- [`Rajan/NepaliBERT`](https://huggingface.co/Rajan/NepaliBERT) — Fill-Mask
- [`IRIIS-RESEARCH/RoBERTa_Nepali_125M`](https://huggingface.co/IRIIS-RESEARCH/RoBERTa_Nepali_125M) — 0.1B parameters
- [`nowalab/nepali-bert-npvec1`](https://huggingface.co/nowalab/nepali-bert-npvec1) — Word embeddings based

**Decoder LLMs (92 models):**
- [`Shushant/NepaliGPT`](https://huggingface.co/Shushant/NepaliGPT) — 88.2M parameters
- [`ghimiresunil/nepaliGPT`](https://huggingface.co/ghimiresunil/nepaliGPT) — Nepali GPT
- [`shivam9980/llama2_Nepali`](https://huggingface.co/shivam9980/llama2_Nepali) — 7B parameters
- [`saillab/nepali-llama3-8b-taco`](https://huggingface.co/saillab/nepali-llama3-8b-taco) — LLaMA-3 fine-tuned
### 8.3 Nepali Spaces on HuggingFace (106+)

**Translation:** Nepali Translator, X ALMA 13B, English-Nepali Translator
**ASR:** Nepali Medical AI, Nepali Speech-to-Text
**Sentiment:** Nepali Sentiment Analyzer
**Multimodal:** Nepali Image Captioning, VQA
