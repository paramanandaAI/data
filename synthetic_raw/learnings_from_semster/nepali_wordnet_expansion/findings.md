# Findings on Nepali WordNet Expansion

Although this data holds some value, contextual annotation methods are absolutely required. We ultimately realized that no matter how much data we collected and evaluated, we couldn't resolve the novel ambiguities that kept arising. Consequently, **this project is now retired**.

## Future Works & Alternative Approaches
- **Fuzzy IndoWordNet Style:** It might be worth testing a fuzzy IndoWordNet approach, as detailed in a promising paper.
- **Cross-Lingual Vector Alignment:** We attempted cross-lingual vector alignment using FastText (applying word-level fuzziness), but the results were poor due to the inherent low quality of the word embeddings.
- **Lemmatization:** Can we integrate suitable lemmatization later? We worked on this but haven't compressed the word vectors at all.
- **SentiWordNet Expansion:** Expanding in a SentiWordNet style introduces new translational ambiguities, making the task even harder.
- **Contextual Embeddings (Noising/Denoising):** For the noising/denoising concept, we expect that WordNet-like annotations should rather be done using BERT embeddings with contextual data, if possible. We should also use a sampled corpus from the agricultural domain.