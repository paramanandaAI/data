# Nepali-Roman Transliteration Dataset

## Dataset Summary
- **Source**: [`Saugatkafley/Nepali-Roman-Transliteration`](https://huggingface.co/datasets/Saugatkafley/Nepali-Roman-Transliteration) (Hugging Face)
- **Local File Path**: `data/nepali_roman_word.csv`
- **Total Rows**: 2,397,414
- **File Size**: ~129 MB
- **Format**: UTF-8 Encoded CSV

## Columns
1. `unique_identifier`: Unique row identifier (e.g. `nep1`, `nep2`, ...)
2. `native word`: Nepali Devanagari word (e.g. `मुस्कुराउँदै`)
3. `english word`: Romanized Nepali word (e.g. `muskuraundai`)

## Script Reference
- **Download Script**: `synthetic/scripts/download_word_transliteration.py`
- **Lookup & Transliteration Utility**: `synthetic/word_transliteration.py`
