import os
import glob
import re

root_dir = r'D:\paramananda'
target_repos = ['nepalinlplibrary', 'data', 'baleval', 'demos', 'local_nogit']

matches = []

for repo in target_repos:
    rpath = os.path.join(root_dir, repo)
    if not os.path.exists(rpath): continue
    for p in glob.glob(os.path.join(rpath, '**', '*'), recursive=True):
        if os.path.isdir(p) or 'node_modules' in p or '.git' in p or '__pycache__' in p:
            continue
        ext = os.path.splitext(p)[1].lower()
        if ext in ['.py', '.md', '.toml', '.json', '.yaml']:
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

print(f"Found {len(matches)} occurrences of 'spylls' across target repos:")
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
