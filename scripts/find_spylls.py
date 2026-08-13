import os
import glob
import re

root_dir = r'D:\paramananda'
all_files = glob.glob(os.path.join(root_dir, '**', '*'), recursive=True)

matches = []

for p in sorted(all_files):
    if os.path.isdir(p) or 'node_modules' in p or '.git' in p:
        continue
    ext = os.path.splitext(p)[1].lower()
    if ext in ['.py', '.md', '.txt', '.json', '.toml', '.yaml', '.yml']:
        try:
            with open(p, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                for idx, line in enumerate(lines, 1):
                    if 'spylls' in line.lower():
                        rel = os.path.relpath(p, root_dir)
                        matches.append({
                            "file": rel,
                            "line_no": idx,
                            "line_content": line.strip()
                        })
        except Exception as e:
            pass

print(f"Found {len(matches)} occurrences of 'spylls' across workspace:")
print("=" * 100)

files_found = {}
for m in matches:
    if m['file'] not in files_found:
        files_found[m['file']] = []
    files_found[m['file']].append(m)

for f, occurrences in files_found.items():
    print(f"\nFile: {f} ({len(occurrences)} mentions)")
    for o in occurrences[:10]:
        print(f"  Line {o['line_no']}: {o['line_content']}")
    if len(occurrences) > 10:
        print(f"  ... and {len(occurrences)-10} more mentions")
