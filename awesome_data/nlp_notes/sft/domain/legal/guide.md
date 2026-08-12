> Source: `sources/sft/domain/legal/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Nepali Legal Domain (कानूनी भाषा): Research & Linguistic Guide

## 🇳🇵 Nepali Legal Linguistics & Terminology
1. **Archaic & Perso-Arabic Loanwords:** Nepali legal statutes (मुलुकी देवानी संहिता, मुलुकी फौजदारी संहिता) retain formal Perso-Arabic terminology:
   - *मुद्दा* (Lawsuit), *फैसला* (Verdict), *बयान* (Testimony), *मिसिल* (Case dossier), *हदम्याद* (Statute of limitations), *पुनरावेदन* (Appeal).
2. **Statutory Syntax Patterns:** Legal provisions follow rigid conditional clausal structures:
   - *"...भएमा ... सजाय हुनेछ।"* (If ..., then punishment shall be ...).
   - Modal auxiliaries: *हुनेछ* (Shall be), *सकिनेछ* (May be), *हुने छैन* (Shall not be).

---

## 🤖 LLM Generation & Hallucination Guardrails
- **Section/Article Hallucination:** LLMs frequently invent nonexistent section numbers (दफा). Fine-tuning data must pair legal queries with explicit grounded context spans.
- **System Prompt Framing:** Always enforce: `"नेपालको प्रचलित कानून (मुलुकी संहिता तथा संविधान) को आधारमा मात्र जवाफ दिनुहोस्।"`
