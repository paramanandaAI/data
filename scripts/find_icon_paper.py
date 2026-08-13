import json

with open(r'D:\paramananda\data\docs\workspace_md_index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== Searching for ICON / CHiPSAL / Paper Submission references ===")
for item in data:
    t = item['title'].lower()
    p = item['path'].lower()
    if 'icon' in t or 'icon' in p or 'chipsal' in t or 'chipsal' in p:
        print(f"Path: {item['path']}")
        print(f"Title: {item['title']}\n")
