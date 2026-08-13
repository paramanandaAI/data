import os
import glob
import json

def check_data_files():
    print("=== Checking Key Datasets in old_old/dataloader ===")
    
    # 1. Check Dr. Prasain publications jsonl count
    pub_dir = r'D:\paramananda\data\old_old\dataloader\train\linguistics\prasain_publications'
    if os.path.exists(pub_dir):
        files = glob.glob(os.path.join(pub_dir, '*.jsonl'))
        total_rows = 0
        for f in files:
            with open(f, 'r', encoding='utf-8') as fp:
                total_rows += sum(1 for _ in fp)
        print(f"Dr. Prasain Publications JSONL files: {len(files)} files, {total_rows} total instruction rows.")

    # 2. Check toxicity datasets in old_old/dataloader/train/synthetic/toxicity_data
    tox_dir = r'D:\paramananda\data\old_old\dataloader\train\synthetic\toxicity_data'
    if os.path.exists(tox_dir):
        for f in os.listdir(tox_dir):
            if f.endswith('.csv'):
                fp = os.path.join(tox_dir, f)
                with open(fp, 'r', encoding='utf-8') as fp_in:
                    lines = len(fp_in.readlines())
                print(f"Toxicity dataset '{f}': {lines} rows.")

    # 3. Check trekking and translation jsonl files in old_old/dataloader/train/synthetic_insturction_todo
    syn_dir = r'D:\paramananda\data\old_old\dataloader\train\synthetic_insturction_todo'
    if os.path.exists(syn_dir):
        for root, dirs, files_in_dir in os.walk(syn_dir):
            for f in files_in_dir:
                if f.endswith('.jsonl'):
                    fp = os.path.join(root, f)
                    rel = os.path.relpath(fp, syn_dir)
                    with open(fp, 'r', encoding='utf-8') as fp_in:
                        lines = sum(1 for _ in fp_in)
                    print(f"Synthetic instruction '{rel}': {lines} rows.")

check_data_files()
