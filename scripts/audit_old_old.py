import os

old_old_root = r'D:\paramananda\data\old_old'
all_items = []
for root, dirs, files in os.walk(old_old_root):
    for f in files:
        fp = os.path.join(root, f)
        rel = os.path.relpath(fp, old_old_root)
        all_items.append((rel, os.path.getsize(fp)))

print(f"Total files in old_old: {len(all_items)}")
print("Categorization of old_old items:")

top_folders = {}
for rel, size in all_items:
    top = rel.split(os.sep)[0]
    if top not in top_folders:
        top_folders[top] = {'count': 0, 'bytes': 0}
    top_folders[top]['count'] += 1
    top_folders[top]['bytes'] += size

for tf, stat in top_folders.items():
    cnt = stat['count']
    mb = stat['bytes'] / (1024 * 1024)
    print(f" - {tf:<30} | {cnt:<5} files | {mb:.2f} MB")
