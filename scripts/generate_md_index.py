import os
import glob
import json

root_dir = r'D:\paramananda'
md_files = glob.glob(os.path.join(root_dir, '**', '*.md'), recursive=True)

out_records = []

for m in sorted(md_files):
    if 'node_modules' in m:
        continue
    rel = os.path.relpath(m, root_dir)
    size = os.path.getsize(m)
    title = "NO TITLE"
    headers = []
    
    try:
        with open(m, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            for line in lines:
                lstr = line.strip()
                if lstr.startswith("#"):
                    headers.append(lstr)
            if headers:
                title = headers[0]
    except Exception as e:
        title = f"ERROR: {e}"

    out_records.append({
        "path": rel,
        "size_kb": round(size / 1024, 2),
        "lines": len(lines) if 'lines' in locals() else 0,
        "title": title,
        "all_headers": headers[:10]
    })

out_path = r'D:\paramananda\data\docs\workspace_md_index.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(out_records, f, indent=2, ensure_ascii=False)

print(f"Indexed {len(out_records)} markdown files to {out_path}")
