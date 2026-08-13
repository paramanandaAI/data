# Awesome Nepali NLP & Devanagari Tools

Curated catalog of software libraries, preprocessors, tokenizers, and annotation toolkits for Nepali computational linguistics.

---

## 1. Libraries & Frameworks

| Tool Name | Core Capability | Repository / Package |
| :--- | :--- | :--- |
| `nepalinlplibrary` | Agent-first NLP library (`ne_noise`, dataloader, agent skills) | [`nepalinlplibrary/`](../nepalinlplibrary) |
| `baleval` | Benchmark evaluation engine & probing harness | [`baleval/`](../baleval) |
| `demos/kiss` | Human-in-the-Loop visual/text annotation canvas | [`demos/kiss/`](../demos/kiss) |
| `ne_noise` | Synthetic Devanagari text perturbation engine | `nepalinlplibrary/noising_denoising_toolkit` |
| `YamlQL` | DuckDB-backed SQL over YAML sidecars | `demos/kiss/third_party/YamlQL` |

---

## 2. Preprocessors & Tokenizers

- **Devanagari Purity Validator**: Calculates Unicode Devanagari character ratio ($\text{U}+0900$ to $\text{U}+097\text{F}$).
- **Postposition Detacher / Joiner**: Programmatic joining of detached postpositions (`सरकार ले -> सरकारले`).
- **Chhanda Prosody Scanner**: Sylable classification into Laghu (ह्रस्व) and Guru (दीर्घ) for classical Sanskrit/Nepali meters.
