# Paramananda NLP — Data Repository (`data`)

An open-source, agent-friendly dataset hub and benchmark specification repository for **Nepali NLP**, Devanagari OCR, Speech Recognition (ASR), Text-to-Speech (TTS), and Multimodal learning.

> Companion dataset repository for [nepalinlplibrary](file:///d:/paramananda/nepalinlplibrary).

---

## 📁 Repository Architecture

```tree
data/
├── awesome_data/                        # CENTRAL CATALOG, RESEARCH & GUIDES
│   ├── DATA_SCHEMA.md                   # Canonical JSONL record schema specifications
│   ├── PIPELINE.md                      # Data ingestion workflow & status lifecycle guide
│   ├── DOMAIN_ADAPTATION_GUIDE.md       # Paramananda domain adaptation framework specification
│   ├── Nepali_data/                     # Categorized Dataset YAML Contracts & Index
│   │   ├── catalog.jsonl                # Consolidated JSONL dataset catalog index
│   │   ├── dataset_catalog.md           # Dataset metadata inventory
│   │   ├── pretrain/                    # Monolingual web, Wikipedia, parallel pretraining YAMLs
│   │   ├── sft/                         # Domain SFT (legal, health, agro, finance), GEC, NER, POS, QA, MT
│   │   ├── similarity/                  # NLI, STS, and passage reranking YAMLs
│   │   ├── multimodal/                  # ASR, OCR, TTS, Vision, Sign Language YAMLs
│   │   └── eval/                        # Safety, toxicity, and classification evaluation YAMLs
│   ├── Nepali_research/                 # Academic literature surveys & paper bibliographies (`balkbal_publications.md`, `hf_datasets_catalog.md`)
│   ├── nlp_notes/                       # Task guides, framework tables, and evaluation metrics (`guide.md`)
│   └── INDEX.md                         # Master Inventory & Mapping Specification
│
├── dataloader/                          # EVALUATION & TRAINING PIPELINE DATA
│   ├── eval/                            # Held-out evaluation benchmark suites (GLUE-Nepali, SQuAD-Nepali)
│   ├── train/                           # Pre-processed training split corpora
│   └── yaml/                            # YAML contract redirect note
│
├── hindi_nepali_test/                   # Parallel Hindi-Nepali translation test corpora
├── library_test/                        # Factual test sets (OCR sample images, transliteration CSVs)
└── synthetic_raw/                       # Raw domain adaptation & Nepali WordNet expansion data
```

---

## ⚡ Integration with `nepalinlplibrary.dataloader`

All dataset contract YAML files inside `awesome_data/Nepali_data/` are parsed and loaded by the `nepalinlplibrary.dataloader` Python package.

### Quickstart Usage

```python
from nepalinlplibrary.dataloader import DatasetLoader, DatasetSpec

# Initialize loader pointing to awesome_data/Nepali_data
loader = DatasetLoader()

# Discover verified dataset contracts
verified_specs = loader.list_datasets(verified_only=True)
print(f"Verified datasets: {len(verified_specs)}")

# Load a specific dataset spec and format records for Gemma 4 or T5
spec = loader.get_spec("huggingface_Bibek1129_nepali_SQuAD")
records = loader.load_dataset_records(
    dataset_id="huggingface_Bibek1129_nepali_SQuAD",
    user_requested_rows=5000,
    template_type="gemma4"
)
```

### Command Line Interface (CLI)

```bash
# Set PYTHONPATH to nepalinlplibrary
$env:PYTHONPATH="d:\paramananda\nepalinlplibrary"

# List all discovered datasets with status and modality
python -m dataloader.cli list --root d:\paramananda\data\awesome_data\Nepali_data

# Inspect specific dataset metadata
python -m dataloader.cli info huggingface_Bibek1129_nepali_SQuAD --root d:\paramananda\data\awesome_data\Nepali_data

# Re-generate catalog.jsonl
python -m dataloader.cli catalog d:\paramananda\data\awesome_data\Nepali_data\catalog.jsonl --root d:\paramananda\data\awesome_data\Nepali_data
```

---

## 📜 Dataset YAML Contract Schema

Dataset specifications in `awesome_data/Nepali_data/<category>/` adhere to the enhanced schema:

```yaml
id: huggingface_Bibek1129_nepali_SQuAD
name: Bibek1129/nepali_SQuAD
source_url: https://huggingface.co/datasets/Bibek1129/nepali_SQuAD
task: sft/qa
status: verified         # 'verified' (gold/silver datasets) or 'todo' (unverified specs)
quality_tier: gold       # gold, silver, bronze, raw
modality: text           # text, audio, image_text, sign_language, multimodal
license: cc-by-4.0
language: ne
script: Devanagari

languages:
  ne: 10000              # Row count breakdown by ISO language code

size_stats:
  max_rows: 10000        # Maximum dataset capacity
  total_size_mb: 45.2    # Download size in MB
  download_rows_default: 10000  # Default fetch count (user-configurable subset)

column_mapping:
  context: context
  question: question
  answers: answers

export_templates:
  t5:
    task_prefix: "nepali reading comprehension qa: "
    source_text: "प्रसङ्ग: {context} | प्रश्न: {question}"
    target_text: "{answers}"
  gemma4:
    messages:
      - role: "user"
        content: "दिएको सन्दर्भ पढेर प्रश्नको सही उत्तर दिनुहोस्:\n\nसन्दर्भ: {context}\n\nप्रश्न: {question}"
      - role: "model"
        content: "{answers}"

validation:
  min_devanagari_ratio: 0.70
  drop_duplicates: true
```

---

## 🔒 Contamination Guardrail

All evaluation benchmarks in `dataloader/eval/` (GLUE-Nepali, SQuAD-Nepali, ASR evaluation sets, LLM benchmarks) are strictly held-out. Any training text with $\ge 80\%$ n-gram overlap with evaluation benchmarks is purged during data preprocessing.

---

## 🙏 Acknowledgments & Data Sources

- **Himalaya AI**: Nepali SFT, Devanagari OCR graphemes, NepVoice, honorific bench.
- **AI4Bharat**: IndicTrans2 English-Nepali parallel translation corpus.
- **ILPRL (Kathmandu University)**: Nwacha Muna Newari ASR, NepTam parallel corpus.
- **Saugat Kafley**: Nepali-Roman transliteration dataset (~2.4M pairs).
- **Biraj Bhusal et al.**: Rakshak toxicity and safety benchmark.
- **Sumit Aryal**: Nepali Grammatical Error Correction (GEC) datasets.
