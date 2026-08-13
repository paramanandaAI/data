> Source: `sources/sft/instruction/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Instruction Tuning & Reasoning: Task Guide & Notes

## 🇳🇵 Nepali Linguistic Nuances
1. **Honorific Registers (आदरार्थी प्रयोग):** Responses must default to high honorific (*हजुर / तपाईँ*) and polite verb inflections (*गर्नुहोस्, भन्नुहुन्छ*), unless explicitly prompted for casual/dialectal registers.
2. **Agglutination & Case Markers (विभक्ति):** Ergative (*-ले*), Genitive (*-को/-का/-की*), Dative (*-लाई*), and Locative (*-मा*) must attach cleanly to nouns without artificial whitespace.
3. **Number Formatting (दक्षिण एसियाली संख्या प्रणाली):** Support standard Nepali numerals (०-९) and South Asian grouping (हजार, लाख, करोड, अरब).

---

## 🤖 Modern Model Adaptation (Gemma 4 & Sentence-BERT)
- **Gemma 4 (Instruction & Function Calling):**
  - Prompt Template: `<start_of_turn>user\n{instruction}\n<end_of_turn>\n<start_of_turn>model\n{response}<end_of_turn>`
  - Loss Masking: Compute cross-entropy loss exclusively on the model response tokens.
- **Sentence-BERT / Bi-Encoder:**
  - Embed user query for dynamic few-shot exemplar retrieval and RAG grounding.

---

## ⚙️ Related LLM Frameworks (Fine-Tuning, Inference, RAG, Agents)

### Fine-Tuning & Training
| Repository | Focus |
|---|---|
| [`adapter-hub/adapters`](https://github.com/adapter-hub/adapters) | Unified library for parameter-efficient and modular transfer learning |
| [`georgian-io/LLM-Finetuning-Toolkit`](https://github.com/georgian-io/LLM-Finetuning-Toolkit) | Toolkit for fine-tuning, ablating and unit-testing open-source LLMs |
| [`tatsu-lab/alpaca_eval`](https://github.com/tatsu-lab/alpaca_eval) | Automatic evaluator for instruction-following language models |
| [`hiyouga/EasyR1`](https://github.com/hiyouga/EasyR1) | Efficient, scalable, multi-modality RL training framework |
| [`mosaicml/llm-foundry`](https://github.com/mosaicml/llm-foundry) | LLM training code for Databricks foundation models |

### Inference & Quantization
| Repository | Focus |
|---|---|
| [`huggingface/text-generation-inference`](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference |
| [`AutoGPTQ/AutoGPTQ`](https://github.com/AutoGPTQ/AutoGPTQ) | LLMs quantization package based on GPTQ algorithm |
| [`bigscience-workshop/petals`](https://github.com/bigscience-workshop/petals) | Run LLMs at home, BitTorrent-style — fine-tuning and inference up to 10x faster |
| [`ModelTC/LightLLM`](https://github.com/ModelTC/LightLLM) | Lightweight LLM inference and serving framework |
| [`neuralmagic/deepsparse`](https://github.com/neuralmagic/deepsparse) | Sparsity-aware deep learning inference runtime for CPUs |

### RAG & Retrieval
| Repository | Focus |
|---|---|
| [`IntelLabs/fastRAG`](https://github.com/IntelLabs/fastRAG) | Efficient Retrieval Augmentation and Generation Framework |
| [`neuml/txtai`](https://github.com/neuml/txtai) | All-in-one AI framework for semantic search and LLM orchestration |
| [`stanford-oval/storm`](https://github.com/stanford-oval/storm) | LLM-powered knowledge curation system with full-length report generation |
| [`DataScienceUIBK/Rankify`](https://github.com/DataScienceUIBK/Rankify) | Comprehensive Python toolkit for retrieval, re-ranking, and RAG |
| [`SylphAI-Inc/AdalFlow`](https://github.com/SylphAI-Inc/AdalFlow) | Library to build & auto-optimize LLM applications |

### Prompting & Reasoning
| Repository | Focus |
|---|---|
| [`thunlp/OpenPrompt`](https://github.com/thunlp/OpenPrompt) | Open-source framework for prompt-learning |
| [`trigaten/Learn_Prompting`](https://github.com/trigaten/Learn_Prompting) | Prompt engineering and generative AI guide |
| [`google-research/prompt-tuning`](https://github.com/google-research/prompt-tuning) | Original implementation of Prompt Tuning (Lester et al., 2021) |
| [`zjunlp/Prompt4ReasoningPapers`](https://github.com/zjunlp/Prompt4ReasoningPapers) | ACL 2023 survey on reasoning with language model prompting |

### Agents & Dialog
| Repository | Focus |
|---|---|
| [`RasaHQ/rasa`](https://github.com/RasaHQ/rasa) | Open source ML framework for text- and voice-based conversations |
| [`SqueezeAILab/LLMCompiler`](https://github.com/SqueezeAILab/LLMCompiler) | ICML 2024 — LLM compiler for parallel function calling |
| [`botpress/botpress`](https://github.com/botpress/botpress) | Open-source hub to build & deploy GPT/LLM agents |
| [`zjunlp/LLMAgentPapers`](https://github.com/zjunlp/LLMAgentPapers) | Must-read papers on LLM agents |

### Domain-Specific LLMs
| Repository | Focus |
|---|---|
| [`AI4Finance-Foundation/FinGPT`](https://github.com/AI4Finance-Foundation/FinGPT) | Open-source financial large language models |
| [`allenai/scispacy`](https://github.com/allenai/scispacy) | Full spaCy pipeline for scientific/biomedical documents |
| [`medspacy/medspacy`](https://github.com/medspacy/medspacy) | Library for clinical NLP with spaCy |
| [`ICLRandD/Blackstone`](https://github.com/ICLRandD/Blackstone) | spaCy pipeline for NLP on unstructured legal text |
| [`github/CodeSearchNet`](https://github.com/github/CodeSearchNet) | Datasets, tools, and benchmarks for code representation learning |
