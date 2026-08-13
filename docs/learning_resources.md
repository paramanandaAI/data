> Source: `sources/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

## 📖 9. Learning Resources & Demo Suggestions

> Curated entry points for students, pulled from awesome lists and course catalogs. Each level suggests concrete demos.

### 9.1 Beginner (Week 1–2): Understand the Landscape

**Read:**
1. Shahi & Sitaula (2021) — "Natural Language Processing for Nepali Text: A Review"
2. Explore [`himalaya-ai/nepali-corpus-compile`](https://huggingface.co/datasets/himalaya-ai/nepali-corpus-compile) on HuggingFace

**Demo:**
- Load NepBERTa and run sentiment analysis on Nepali tweets
- Use spaCy with Nepali tokenizer for basic NER
- Explore the Nepali National Corpus structure

**Resources:**
- [`keon/awesome-nlp`](https://github.com/keon/awesome-nlp) — Curated NLP resources
- [`explosion/spacy-course`](https://github.com/explosion/spacy-course) — Advanced NLP with spaCy
- [`huggingface/course`](https://github.com/huggingface/course) — HuggingFace Transformers course

### 9.2 Intermediate (Week 3–4): Build Task-Specific Models

**Projects:**
1. Fine-tune NepBERTa on Nepali news classification (use `mteb/NepaliNewsClassification`)
2. Build GEC pipeline using sumitaryal dataset (error detection → correction)
3. Train a Nepali NER model using DanfeNER dataset

**Demo:**
- Nepali-English translation with IndicTrans2
- Nepali summarization using XL-Sum BBC dataset
- Aspect-based sentiment analysis on Nepali product reviews

**Resources:**
- [`fastai/course-nlp`](https://github.com/fastai/course-nlp) — Code-first NLP introduction
- [`datawhalechina/learn-nlp-with-transformers`](https://github.com/datawhalechina/learn-nlp-with-transformers) — Transformers usage guide
- [`cedrickchee/awesome-transformer-nlp`](https://github.com/cedrickchee/awesome-transformer-nlp) — Transformer NLP resources

### 9.3 Advanced (Week 5+): Multimodal & LLM Training

**Projects:**
1. Train a small NepaliGPT from scratch on monolingual corpus
2. Build multimodal OCR pipeline for Devanagari documents
3. Fine-tune Whisper for Nepali ASR

**Demo:**
- Nepali meme hate speech detection (CHIPSAL 2026 shared task)
- Nepali question answering on legal/medical domain
- Multimodal VQA on Nepali image captions

**Resources:**
- [`NirDiamant/RAG_Techniques`](https://github.com/NirDiamant/RAG_Techniques) — Advanced RAG techniques
- [`datawhalechina/base-llm`](https://github.com/datawhalechina/base-llm) — NLP to LLM full-stack tutorial
- [`hiyouga/LlamaFactory`](https://github.com/hiyouga/LlamaFactory) — Unified efficient fine-tuning (ACL 2024)

### 9.4 Awesome Lists — Quick Access

| List | Focus | Best For |
|---|---|---|
| [`keon/awesome-nlp`](https://github.com/keon/awesome-nlp) | General NLP | Starting point |
| [`cedrickchee/awesome-transformer-nlp`](https://github.com/cedrickchee/awesome-transformer-nlp) | Transformers, BERT, GPT | Architecture deep-dive |
| [`Separius/awesome-sentence-embedding`](https://github.com/Separius/awesome-sentence-embedding) | Sentence embeddings | Similarity tasks |
| [`mathsyouth/awesome-text-summarization`](https://github.com/mathsyouth/awesome-text-summarization) | Summarization | Summarization projects |
| [`seriousran/awesome-qa`](https://github.com/seriousran/awesome-qa) | Question answering | QA systems |
| [`roomylee/awesome-relation-extraction`](https://github.com/roomylee/awesome-relation-extraction) | Relation extraction | Knowledge graphs |
| [`haiker2011/awesome-nlp-sentiment-analysis`](https://github.com/haiker2011/awesome-nlp-sentiment-analysis) | Sentiment analysis | Sentiment projects |
| [`tstanislawek/awesome-document-understanding`](https://github.com/tstanislawek/awesome-document-understanding) | Document understanding | Document AI |
| [`CryptoAILab/Awesome-LM-SSP`](https://github.com/CryptoAILab/Awesome-LM-SSP) | LLM safety, security, privacy | Safety research |
| [`luban-agi/Awesome-Domain-LLM`](https://github.com/luban-agi/Awesome-Domain-LLM) | Domain-specific LLMs | Vertical adaptation |

---
