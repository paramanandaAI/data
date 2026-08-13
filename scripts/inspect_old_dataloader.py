import os
import glob

old_old_root = r'D:\paramananda\data\old_old'

# Check dataloader subfolder in old_old
dataloader_path = os.path.join(old_old_root, 'dataloader')
if os.path.exists(dataloader_path):
    print("Files in old_old/dataloader:")
    for root, dirs, files in os.walk(dataloader_path):
        for f in files:
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, dataloader_path)
            size = os.path.getsize(fp)
            print(f" - {rel:<60} ({size/(1024*1024):.2f} MB)")
