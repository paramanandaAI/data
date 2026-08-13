# -*- coding: utf-8 -*-
"""
Catalog Rebuilder Script (`data/scripts/rebuild_catalog.py`)
Scans all registered dataset YAML specifications and rebuilds data/catalog.jsonl.
"""

import os
import json
from nepalinlplibrary.dataloader import DatasetLoader

DATA_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CATALOG_PATH = os.path.join(DATA_ROOT, "catalog.jsonl")

def rebuild_catalog():
    print(f"Loading dataset specifications from {DATA_ROOT}...")
    loader = DatasetLoader(root_dir=os.path.join(DATA_ROOT, "datasets"))
    specs = loader.discover_specs()
    print(f"Found {len(specs)} dataset specifications.")

    catalog_entries = []
    for spec_id, spec in sorted(specs.items()):
        entry = {
            "id": spec.id,
            "name": spec.name,
            "status": spec.status,
            "quality_tier": spec.quality_tier,
            "modality": spec.modality,
            "task": spec.task,
            "license": spec.license,
            "language": spec.language,
            "script": spec.script,
            "max_rows": spec.max_rows,
            "total_size_mb": spec.total_size_mb,
            "filepath": os.path.relpath(spec.filepath, DATA_ROOT).replace("\\", "/") if spec.filepath else ""
        }
        catalog_entries.append(entry)

    print(f"Writing {len(catalog_entries)} entries to {CATALOG_PATH}...")
    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
        for entry in catalog_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"Successfully rebuilt catalog.jsonl with {len(catalog_entries)} datasets.")

if __name__ == "__main__":
    rebuild_catalog()
