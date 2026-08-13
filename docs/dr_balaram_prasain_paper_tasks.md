# Dr. Balaram Prasain: Paper Tasks & Data Status

## Task Matrix

| Year | Paper | Primary Task | Data Status | Action Needed |
| :--- | :--- | :--- | :--- | :--- |
| **1999** | `complex_predicates_in_bote_ma_thesis` | Bote Language Complex Predicates | PARTIAL | Need fieldwork data |
| **2000** | `phut_break_verb_analysis` | Intransitive/Transitive Verb Pairs | DONE | - |
| **2003** | `some_light_verbs_in_bote` | Light Verb Construction (LVC) | PARTIAL | Need Bote data |
| **2005** | `notes_on_kusunda_grammar` | Kusunda Language Isolate Notes | PARTIAL | Need Kusunda data |
| **2006** | `finite_state_approach_nepali_pronouns` | Pronoun FST Morphotactics | DONE | - |
| **2007** | `finite_state_approach_nepali_adjectives` | Adjective Agreement FST | DONE | - |
| **2008** | `part_of_speech_tagset_for_nepali` | 91 MPP & 112 Nelralec POS Tagsets | DONE | - |
| **2008** | `computational_analysis_nepali_basic_verbs` | Verb Morphological Paradigm | DONE | - |
| **2011** | `computational_analysis_nepali_morphology_phd` | Two-Level FST Verb Morphotactics | DONE | - |
| **2011** | `grammar_of_baram` | Endangered Baram Grammar | PARTIAL | Need Baram data |
| **2011** | `baram_nepali_english_dictionary` | Trilingual Dictionary Mapping | PARTIAL | Need dictionary data |
| **2017** | `sociolinguistic_survey_dhuleli` | Dialectal & Sociolinguistic Survey | PARTIAL | Need survey data |
| **2023** | `pronunciation_aware_syllable_tokenizer` | Syllable Tokenization ASR | **DATA EXISTS** | Format G2P data |
| **2024** | `strategies_for_corpus_development` | Low-Resource Corpus Strategies | DONE | - |
| **2026** | `neptam_parallel_corpus` | Nepali-Tamang Machine Translation | **DATA EXISTS** | Format parallel pairs |

---

## Data Available (Needs Formatting)

### Syllable Tokenizer Data (2023)
- **Source**: Ghimire, Bal, Prasain, Poudyal (2023)
- **Data**: Grapheme-to-Phoneme (G2P) Devanagari syllable boundaries
- **Status**: Available
- **Action**: Format to instruction pairs
- **Output**: `combined/g2p_instruction_data.jsonl`

### Instruction Format for G2P
```json
{
  "messages": [
    {"role": "system", "content": "तपाईं एक नेपाली फोनेटिक विशेषज्ञ हुनुहुन्छ।"},
    {"role": "user", "content": "यो शब्दलाई सिलेबलमा विभाजन गर्नुहोस्: विश्वविद्यालय"},
    {"role": "assistant", "content": "विश्-व-विद्-या-लय"}
  ],
  "source": "syllable_tokenizer_2023",
  "metadata": {"source": "syllable_tokenizer_2023", "category": "g2p"}
}
```

### NepTam Parallel Corpus (2026)
- **Source**: Ghimire, Subedi, Prasain et al. (2026)
- **Data**: Nepali-Tamang parallel sentence pairs
- **Status**: Available
- **Action**: Format to translation instruction pairs
- **Output**: `combined/neptam_instruction_data.jsonl`

### Instruction Format for MT
```json
{
  "messages": [
    {"role": "system", "content": "तपाईं एक नेपाली-तामाङ अनुवादक हुनुहुन्छ।"},
    {"role": "user", "content": "Translate to Tamang: नमस्ते, तपाईंलाई कस्तो छ?"},
    {"role": "assistant", "content": "नमस्ते, तपाईं कस्तो छ?"}
  ],
  "source": "neptam_2026",
  "metadata": {"source": "neptam_2026", "category": "translation"}
}
```

---

## Endangered Language Data (Fieldwork Needed)

### Baram Language
- **Source**: Kansakar, Yadava, Chalise, Prasain et al. (2011)
- **Data**: Grammar rules, trilingual dictionary
- **Status**: Partial - need to digitize
- **Action**: Contact authors for raw data

### Kusunda Language
- **Source**: Prasain (2005)
- **Data**: Grammar notes, vocabulary
- **Status**: Partial - need to digitize
- **Action**: Contact authors for raw data

### Bote Language
- **Source**: Prasain (1999-2003)
- **Data**: Complex predicates, light verbs
- **Status**: Partial - need to digitize
- **Action**: Contact authors for raw data

---

## Quick Actions

```bash
# Format G2P data
python _inspirations/generate.py --task g2p --ref-file /path/to/g2p_data.jsonl --count 500

# Format NepTam data
python _inspirations/generate.py --task translation --ref-file /path/to/neptam_data.jsonl --count 1000

# Combine all
python _inspirations/combine_dataset.py --input_dir _inspirations --output_file combined/all_data.jsonl
```

---

## Cross-References

- [[dr_bal_krishna_bal_paper_tasks]] - Bal's papers
- [[bal_eval_framework]] - Evaluation framework
- [[papers_list]] - Full bibliography
- [[synthetic_data_generation_guide]] - Generation protocols
