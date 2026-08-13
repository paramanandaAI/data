import os
import glob
import shutil

old_old_root = r'D:\paramananda\data\old_old'
clean_root = r'D:\paramananda\data'

print("=== Complete Inventory of D:\\paramananda\\data\\old_old ===")
file_list = []
for root, dirs, files in os.walk(old_old_root):
    for f in files:
        fp = os.path.join(root, f)
        rel = os.path.relpath(fp, old_old_root)
        file_list.append((rel, fp, os.path.getsize(fp)))

print(f"Total files in old_old: {len(file_list)}")
print("=" * 80)

# Categorize files by extension & path
exts = {}
for rel, fp, sz in file_list:
    ext = os.path.splitext(rel)[1].lower()
    if ext not in exts:
        exts[ext] = []
    exts[ext].append((rel, sz))

for ext, items in sorted(exts.items()):
    total_sz = sum(s for _, s in items)
    print(f"Extension '{ext}': {len(items)} files, {total_sz / (1024*1024):.2f} MB")
    for r, s in items[:3]:
        print(f"   - {r} ({s/1024:.1f} KB)")
    if len(items) > 3:
        print(f"   ... and {len(items)-3} more files")
