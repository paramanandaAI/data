> Source: `sources/multimodal/ocr/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Optical Character Recognition (OCR) & Document AI: Task Guide & Notes

## 🇳🇵 Devanagari Script Complexities
1. **Shirorekha (शिरोरेखा - Top Hanging Line):** Continuous upper horizontal line connects glyphs in a word; segmentation models must handle character ligature boundaries beneath the headline.
2. **Matra Modifiers & Conjuncts (संयुक्ताक्षर):**
   - Superior (ि, े, ै), Inferior (ु, ू, ृ), Pre-base (ि), and Post-base (ा, ी, ो, ौ).
   - Reph (*र्*) and conjunct ligatures (*क्ष, त्र, ज्ञ, द्ध, द्व, ष्ट*).

---

## 🤖 Modern End-to-End OCR (Gemma 4 Vision & ViT/CRNN)
- **Gemma 4 Vision / Nougat-style End-to-End:**
  - Direct image input `<image>` generating markdown or structured JSON text without intermediate character segmentation.
- **Sentence-BERT / Bi-Encoder:**
  - Embed OCR-extracted text for downstream semantic search and document retrieval.

## ⚙️ Related Document AI & OCR Frameworks

| Repository | Focus |
|---|---|
| [`deepdoctection/deepdoctection`](https://github.com/deepdoctection/deepdoctection) | A repo for Document AI — layout analysis, OCR, table recognition |
| [`Unstructured-IO/unstructured`](https://github.com/Unstructured-IO/unstructured) | Convert documents to structured data — open-source ETL for LLMs |
| [`axa-group/Parsr`](https://github.com/axa-group/Parsr) | Transforms PDFs, documents and images into enriched structured data |
| [`microsoft/unilm`](https://github.com/microsoft/unilm) | Large-scale self-supervised pre-training across tasks, languages, and modalities |
| [`enoch3712/ExtractThinker`](https://github.com/enoch3712/ExtractThinker) | Document Intelligence library for LLMs with ORM-style interaction |
| [`yobix-ai/extractous`](https://github.com/yobix-ai/extractous) | Fast unstructured data extraction, written in Rust |
| [`Nishchal-XD/AUTOMATED-DATA-EXTRACTION-FROM-NEPALI-CITIZENSHIP-CARD-USING-OCR-FOR-AUTO-FILLING-BANK-KYC`](https://github.com/Nishchal-XD/AUTOMATED-DATA-EXTRACTION-FROM-NEPALI-CITIZENSHIP-CARD-USING-OCR-FOR-AUTO-FILLING-BANK-KYC) | OCR-based Nepali citizenship data extraction and KYC form filling |
