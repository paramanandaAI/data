> Source: `sources/multimodal/retrieval/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Multimodal Retrieval: Cross-Modal Search & Document Understanding

## 🔍 Cross-Modal Retrieval Types

### 1. Text → Image Retrieval
- Query: text description → Retrieve: matching images
- Use case: Find images in Nepali documents that match a query

### 2. Image → Text Retrieval
- Query: image → Retrieve: matching text passages
- Use case: Find text descriptions of images in documents

### 3. Text → Table Retrieval
- Query: text question → Retrieve: relevant tables
- Use case: Find data tables in Nepali reports

### 4. Document Layout Retrieval
- Query: text → Retrieve: documents with specific layout
- Use case: Find legal documents, forms, certificates

---

## 🤖 Models for Multimodal Retrieval

### CLIP (Contrastive Language-Image Pre-training)
- **Architecture:** Image encoder (ViT) + Text encoder (Transformer)
- **Training:** Contrastive learning on image-text pairs
- **Use case:** Zero-shot image-text retrieval
- **Limitation:** English-centric, limited multilingual support

### ColPali (Retrieval with Vision Language Models)
- **Architecture:** Vision Language Model (VLM) for document retrieval
- **Input:** Document page images + query
- **Output:** Relevance score
- **Advantage:** Handles visual layout, tables, figures
- **Use case:** Retrieve document pages by visual content

### LayoutLM / LayoutLMv3
- **Architecture:** Text + layout + image features
- **Training:** Document understanding tasks
- **Use case:** Form understanding, table extraction
- **Limitation:** Supervised, needs labeled data

---

## 🇳🇵 Nepali Document Retrieval Challenges

### Devanagari Script
- OCR quality varies across document types
- Font diversity (printed vs handwritten)
- Mixed script (Nepali + English in same document)

### Document Types
- Government forms (census, legal, administrative)
- News articles (with images, tables)
- Academic papers (with figures, equations)
- Handwritten documents (historical, administrative)

### Pipeline
1. **OCR:** Extract text from scanned documents
2. **Layout Analysis:** Identify text blocks, tables, figures
3. **Image Captioning:** Generate descriptions for figures/tables
4. **Indexing:** Create multimodal index (text + image + layout)
5. **Retrieval:** Query across all modalities

---

## 🔗 Cross-References

| Resource | Location | Usage |
|---|---|---|
| OCR | `sources/multimodal/ocr/NOTES.md` | Document text extraction |
| Document AI | `sources/multimodal/ocr/NOTES.md` | Layout analysis |
| ColPali | Faysse et al. (2024) | Document page retrieval |
| CLIP | Radford et al. (2021) | Image-text retrieval |
| Vision-Language | `sources/multimodal/vision/NOTES.md` | VLM frameworks |
| IR Benchmark | `bal_eval/ir_information_retrieval/` | Retrieval evaluation |
