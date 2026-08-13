import os
import glob
import json
import yaml

def build_catalog(datasets_dir, output_jsonl):
    print(f"Building master dataset catalog from '{datasets_dir}'...")
    yaml_files = glob.glob(os.path.join(datasets_dir, "**", "*.yaml"), recursive=True)
    records = []

    for ypath in sorted(yaml_files):
        try:
            with open(ypath, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                if not isinstance(data, dict):
                    continue
                
                # Standardize entry for catalog.jsonl
                rec = {
                    "id": data.get("id", os.path.basename(ypath).replace(".yaml", "")),
                    "name": data.get("name", ""),
                    "task": data.get("task", ""),
                    "status": data.get("status", "todo"),
                    "quality_tier": data.get("quality_tier", "silver"),
                    "modality": data.get("modality", "text"),
                    "max_rows": data.get("size_stats", {}).get("max_rows", 0) if isinstance(data.get("size_stats"), dict) else 0,
                    "languages": data.get("languages", {"ne": 0}),
                    "source_url": data.get("source_url", ""),
                    "filepath": os.path.relpath(ypath, os.path.dirname(output_jsonl)).replace("\\", "/")
                }
                records.append(rec)
        except Exception as e:
            print(f"Error parsing {ypath}: {e}")

    with open(output_jsonl, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"Successfully generated '{output_jsonl}' with {len(records)} dataset entries!")

if __name__ == "__main__":
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ds_dir = os.path.join(repo_root, "datasets")
    out_file = os.path.join(repo_root, "catalog.jsonl")
    build_catalog(ds_dir, out_file)
