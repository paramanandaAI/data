import os
import glob

toclean_root = r'D:\paramananda\local_nogit\data_1\toclean_scripts'

py_files = glob.glob(os.path.join(toclean_root, '**', '*.py'), recursive=True)
non_node = [p for p in py_files if 'node_modules' not in p]

print(f"Total Python scripts in toclean_scripts (excluding node_modules): {len(non_node)}")
print("=" * 80)

for p in non_node:
    rel = os.path.relpath(p, toclean_root)
    size = os.path.getsize(p)
    print(f" - {rel:<70} ({size} bytes)")
