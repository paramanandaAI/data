import os
import glob
import re

root_dir = r'D:\paramananda'
py_files = glob.glob(os.path.join(root_dir, '**', '*.py'), recursive=True)

matches = []

for p in sorted(py_files):
    if 'node_modules' in p:
        continue
    try:
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            for idx, line in enumerate(lines, 1):
                if re.search(r'\b(gradio|streamlit)\b', line, re.IGNORECASE):
                    rel = os.path.relpath(p, root_dir)
                    matches.append({
                        "file": rel,
                        "line_no": idx,
                        "line_content": line.strip()
                    })
    except Exception as e:
        pass

print(f"Found {len(matches)} occurrences of gradio/streamlit across .py files:")
print("=" * 100)

files_found = {}
for m in matches:
    if m['file'] not in files_found:
        files_found[m['file']] = []
    files_found[m['file']].append(m)

for f, occurrences in files_found.items():
    print(f"\nFile: {f} ({len(occurrences)} mentions)")
    for o in occurrences[:5]:
        print(f"  Line {o['line_no']}: {o['line_content']}")
    if len(occurrences) > 5:
        print(f"  ... and {len(occurrences)-5} more mentions")
