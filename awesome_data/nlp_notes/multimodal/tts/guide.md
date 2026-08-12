> Source: `sources/multimodal/tts/NOTES.md` · split by content type
> Section kept: guide
> Do NOT edit content — pending web verification.

# Text to Speech (TTS) & Prosodic Synthesis: Task Guide & Notes

## 🇳🇵 Grapheme-to-Phoneme (G2P) & Prosodic Timing
1. **Schwa Deletion (अ-लोप नियम):** In spoken Nepali, the inherent short vowel /ʌ/ in word-final consonants is typically deleted (*राम = /raːm/* not */raːmʌ/*), but preserved in conjuncts and Sanskrit tatsama words.
2. **Stress & Pitch Contours:** Syllable weight (Laghu/Guru) dictates natural prosody and cadence.

---

## 🤖 Modern End-to-End TTS Adaptation
- **End-to-End Neural TTS (VITS / Parler-TTS):**
  - Train directly on (Devanagari text, audio waveform) pairs using learned alignment without hand-crafted phone lexicons.
