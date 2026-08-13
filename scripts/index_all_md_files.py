import os
import glob
import json

root_dir = r'D:\paramananda'
md_files = glob.glob(os.path.join(root_dir, '**', '*.md'), recursive=True)

records = []

for m in sorted(md_files):
    rel = os.path.relpath(m, root_dir)
    if 'node_modules' in rel or '.git' in rel:
        continue
    size = os.path.getsize(m)
    title = "NO TITLE"
    line_count = 0
    
    try:
        with open(m, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            line_count = len(lines)
            for line in lines:
                line_str = line.strip()
                if line_str.startswith("#"):
                    title = line_str
                    break
    except Exception as e:
        title = f"ERROR READING: {e}"

    records.append({
        "path": rel,
        "size": size,
        "lines": line_count,
        "title": title
    })

out_json = os.path.join(root_dir, 'data', 'docs', 'workspace_md_index.json')
os.makedirs(os.path.dirname(out_json), exist_ok=True)
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(records, f, indent=2, ensure_ascii=False)

print(f"Successfully indexed {len(records)} Markdown (.md) files across workspace into '{out_json}'!")
