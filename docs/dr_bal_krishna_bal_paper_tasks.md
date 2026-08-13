# Dr. Bal Krishna Bal: Paper Tasks & Data Status

## Task Matrix

| Year | Paper | Primary Task | Data Status | Action Needed |
| :--- | :--- | :--- | :--- | :--- |
| **2004** | `morphological_analyzer_and_stemmer` | Morpheme Split & POS | DONE | - |
| **2004** | `nepali_spellchecker_and_thesaurus` | Spelling Error Correction | DONE | - |
| **2007** | `architectural_design_grammar_checker` | Grammar & Agreement | DONE | - |
| **2008** | `corpus_contemporary_nepali_nnc` | POS Tagging (112 Tagset) | DONE | - |
| **2009** | `who_speaks_for_whom_opinions` | Editorial Stance Mining | DONE | - |
| **2014** | `analyzing_opinions_news_editorials` | Discourse & Argumentation | DONE | - |
| **2015** | `detecting_sentiment_bhawanakosh` | SentiWordNet Sentiment | DONE | - |
| **2016** | `improving_nepali_ocr_hybrid` | Devanagari Document OCR | DONE | - |
| **2018** | `comparative_study_smt_nmt` | En-Ne Machine Translation | DONE | - |
| **2020** | `aspect_based_abusive_sentiment` | Abusive Speech & Aspect | DONE | - |
| **2022** | `cnn_transformer_image_captioning` | Image Captioning | DONE | - |
| **2023** | `devanagari_license_plate_ocr` | ALPR & Vehicle OCR | DONE | - |
| **2023** | `transformer_based_nepali_tts` | Phonetic TTS Synthesis | **DATA EXISTS** | Format to chat JSONL |
| **2024** | `llms_for_low_resource_ner_pos` | LLM Few-Shot Probing | DONE | - |
| **2025** | `nepconformer_asr_system` | Conformer ASR | **DATA EXISTS** | OpenSLR-54, Common Voice |
| **2025** | `speech_personalization_peft` | ASR Personalization | **DATA EXISTS** | Format speaker data |
| **2026** | `rag_nepali_legal_domain_qa` | Legal Question Answering | PARTIAL | Need legal texts |
| **2026** | `nepal_script_ancient_artifacts` | Ancient Script Recognition | PARTIAL | Need artifact images |
| **2026** | `standard_benchmark_nepali_ir` | Information Retrieval | PARTIAL | Need query-doc pairs |
| **2026** | `nepali_asr_system` | ASR System | **DATA EXISTS** | Format transcripts |

---

## ASR Data Available (Needs Formatting)

### OpenSLR-54
- **Location**: `openslr.org/54`
- **Size**: 157,000 utterances, 400+ hours
- **Format**: WAV + Transcripts
- **Action**: Convert to instruction format
- **Output**: `combined/asr_instruction_data.jsonl`

### Mozilla Common Voice Nepali
- **Location**: `commonvoice.mozilla.org`
- **Size**: 100K+ clips
- **Format**: MP3 + Transcripts
- **Action**: Download and format
- **Output**: `combined/asr_commonvoice_data.jsonl`

### Instruction Format for ASR
```json
{
  "messages": [
    {"role": "system", "content": "तपाईं एक स्पीच टेक्स्ट पहिचान विशेषज्ञ हुनुहुन्छ।"},
    {"role": "user", "content": "यो अडियोको ट्रान्सक्रिप्ट लेख्नुहोस्। [audio_id: openslr54_00123]"},
    {"role": "assistant", "content": "ट्रान्सक्रिप्ट: नमस्ते, तपाईंलाई कस्तो छ?"}
  ],
  "source": "openslr_54",
  "metadata": {"source": "openslr_54", "category": "asr", "audio_id": "openslr54_00123"}
}
```

---

## TTS Data Available (Needs Formatting)

### Transformer-Based TTS (2023)
- **Source**: Dongol & Bal (2023)
- **Data**: Text-phoneme pairs for Nepali TTS
- **Action**: Format to instruction pairs
- **Output**: `combined/tts_instruction_data.jsonl`

### Instruction Format for TTS
```json
{
  "messages": [
    {"role": "system", "content": "तपाईं एक नेपाली TTS विशेषज्ञ हुनुहुन्छ।"},
    {"role": "user", "content": "यो वाक्यलाई फोनेटिक सिलेबलमा विभाजन गर्नुहोस्: काठमाडौँ"},
    {"role": "assistant", "content": "का-ठ-मा-डौँ"}
  ],
  "source": "transformer_tts_2023",
  "metadata": {"source": "transformer_tts_2023", "category": "tts"}
}
```

---

## Quick Actions

```bash
# Check available ASR data
ls -la /path/to/openslr54/
ls -la /path/to/common_voice/

# Format ASR data to instruction format
python _inspirations/generate.py --task asr --ref-file /path/to/openslr54/transcripts.jsonl --count 1000

# Combine all
python _inspirations/combine_dataset.py --input_dir _inspirations --output_file combined/all_data.jsonl
```
