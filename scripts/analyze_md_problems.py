import json
import os
from collections import defaultdict

json_path = r'D:\paramananda\data\docs\workspace_md_index.json'
with open(json_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

print(f"Total indexed markdown files: {len(records)}")

# 1. Check duplicate titles
title_map = defaultdict(list)
size_map = defaultdict(list)

for r in records:
    if r['title'] != "NO TITLE":
        title_map[r['title']].append(r['path'])
    size_map[(r['size_kb'], r['lines'])].append(r['path'])

duplicates_by_title = {t: paths for t, paths in title_map.items() if len(paths) > 1}
duplicates_by_exact_size = {sz: paths for sz, paths in size_map.items() if len(paths) > 1 and sz[0] > 0.1}

print(f"\n--- DUPLICATE MARKDOWN FILES BY EXACT TITLE ({len(duplicates_by_title)} titles repeated) ---")
for t, paths in list(duplicates_by_title.items())[:15]:
    print(f"\nTitle: '{t}' ({len(paths)} copies)")
    for p in paths:
        print(f"  - {p}")

print(f"\n--- DUPLICATE MARKDOWN FILES BY EXACT SIZE & LINE COUNT ({len(duplicates_by_exact_size)} file shapes repeated) ---")
for (sz, lns), paths in list(duplicates_by_exact_size.items())[:15]:
    print(f"\nShape: {sz} KB, {lns} lines ({len(paths)} copies)")
    for p in paths:
        print(f"  - {p}")

# 2. Check stub/empty files
stubs = [r for r in records if r['lines'] <= 5]
print(f"\n--- STUB / NEARLY EMPTY MARKDOWN FILES ({len(stubs)} files <= 5 lines) ---")
for s in stubs[:20]:
    print(f"  - {s['path']:<70} ({s['lines']} lines, {s['size_kb']} KB)")

# 3. Categorize markdown files by top-level repository
repo_counts = defaultdict(int)
for r in records:
    top = r['path'].split(os.sep)[0]
    repo_counts[top] += 1

print("\n--- MARKDOWN FILE DISTRIBUTION ACROSS REPOS ---")
for repo, count in repo_counts.items():
    print(f" - {repo:<35}: {count} markdown files")
