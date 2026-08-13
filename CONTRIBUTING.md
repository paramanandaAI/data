# Contributing to Paramananda Data Registry

Thank you for your interest in contributing to the **Paramananda Devanagari & Nepali Dataset Registry**! This guide outlines the submission requirements and standards for registering new dataset YAML contracts, benchmark evaluation sets, and raw data samples.

---

## 1. Dataset Quality & Verification Criteria

Before submitting a new dataset contract, ensure it meets our quality standards:

1. **Devanagari Unicode Character Purity**:
   - The dataset text must maintain a minimum Devanagari character ratio ($\text{U}+0900$ to $\text{U}+097\text{F}$) of **80% ($\ge 0.80$)**:
     $$\text{Purity Ratio} = \frac{\sum \text{Devanagari Characters}}{\text{Total String Length}} \ge 0.80$$
2. **License Transparency**:
   - Only open-access, citable, or permissible licenses are accepted (e.g., CC-BY-4.0, Apache-2.0, MIT, Open Data Commons).
   - Datasets with unverified, non-commercial restrictions, or unknown origins must be flagged under `status: candidate`.
3. **No Fabricated Data**:
   - Synthetic data generated via LLMs must be explicitly labeled (`modality: synthetic` or `quality_tier: synthetic_candidate`).

---

## 2. YAML Dataset Contract Template

All dataset specifications live in `data/datasets/candidate/` or `data/datasets/verified/` structured by task category (`sft/`, `pretrain/`, `eval/`, `multimodal/`):

```yaml
id: my_dataset_id
name: "Human Readable Dataset Title"
status: candidate # candidate | verified | todo
quality_tier: raw # raw | verified_human_reviewed | synthetic_candidate
modality: text # text | audio | image_text | sign_language
language: ne # ne | [en, ne] | new
script: Devanagari
task: denoising # denoising | translation | classification | qa | etc.
license: cc-by-4.0
source_url: "https://huggingface.co/datasets/example/my-dataset"
upstream_citation: "Author et al. (2026). Paper Title. Conference/Journal."

size_stats:
  max_rows: 10000
  download_rows_default: 100
  total_size_mb: 25.4

export_templates:
  t5:
    task_prefix: "denoise nepali: "
    source_text: "{noisy_text}"
    target_text: "{clean_text}"

samples:
  sample_path: "samples/sft/denoising/my_dataset_sample.csv"
```

---

## 3. Submission Workflow

1. **Fork the Repository**: Create a new feature branch for your dataset contract (`git checkout -b add-my-dataset-spec`).
2. **Add YAML Contract & Sample**:
   - Place YAML spec file under `data/datasets/candidate/<category>/<task>/my_dataset_spec.yaml`.
   - Place a 100-row sample extractions under `data/samples/<category>/<task>/my_dataset_sample.csv` (max 5 MB).
3. **Rebuild Catalog Index**:
   ```bash
   python data/scripts/rebuild_catalog.py
   ```
4. **Submit Pull Request**: Open a Pull Request on GitHub. The automated catalog validator will check YAML schema syntax and Devanagari purity ratio.
