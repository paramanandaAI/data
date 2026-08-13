import os
import shutil
import glob

clean_root = r'D:\paramananda\data'
old_old = r'D:\paramananda\data\old_old'

print("=== Executing Final Migration & Ingestion into Clean data/ Hub ===")

# 1. Copy research paper PDF 2505.14553v2.pdf to docs/
pdf_src = os.path.join(old_old, r'raw_data_archive\learnings_from_semster\hindi-nepali-translation\2505.14553v2.pdf')
pdf_dst = os.path.join(clean_root, r'docs\2505.14553v2.pdf')
if os.path.exists(pdf_src):
    shutil.copy2(pdf_src, pdf_dst)
    print("[-] Copied NMT Research PDF to docs/2505.14553v2.pdf")

# 2. Copy instruction_templates.jsonl to docs/
inst_src = os.path.join(old_old, 'instruction_templates.jsonl')
inst_dst = os.path.join(clean_root, r'docs\instruction_templates.jsonl')
if os.path.exists(inst_src):
    shutil.copy2(inst_src, inst_dst)
    print("[-] Copied instruction_templates.jsonl to docs/instruction_templates.jsonl")

# 3. Copy toxicity review document to docs/toxicity_dataset_review.md
tox_review_src = os.path.join(old_old, r'dataloader\train\synthetic\toxicity_data\translation_review.md')
tox_review_dst = os.path.join(clean_root, r'docs\toxicity_dataset_review.md')
if os.path.exists(tox_review_src):
    shutil.copy2(tox_review_src, tox_review_dst)
    print("[-] Copied toxicity_dataset_review.md to docs/toxicity_dataset_review.md")

# 4. Create sample audio directory & copy 5 sample WAV files to samples/audio/
audio_src_dir = os.path.join(old_old, r'dataloader\train\multimodal\asr\audio')
audio_dst_dir = os.path.join(clean_root, r'samples\audio')
os.makedirs(audio_dst_dir, exist_ok=True)
if os.path.exists(audio_src_dir):
    wav_files = glob.glob(os.path.join(audio_src_dir, '*.wav'))[:5]
    for w in wav_files:
        shutil.copy2(w, os.path.join(audio_dst_dir, os.path.basename(w)))
    print(f"[-] Copied {len(wav_files)} sample WAV files to samples/audio/")

# 5. Create sample OCR images directory & copy 3 sample JPEGs to samples/ocr/
ocr_src_dir = os.path.join(old_old, r'library_test\ocr\thorough_evaluation')
ocr_dst_dir = os.path.join(clean_root, r'samples\ocr')
os.makedirs(ocr_dst_dir, exist_ok=True)
if os.path.exists(ocr_src_dir):
    jpg_files = glob.glob(os.path.join(ocr_src_dir, '*.jpg'))[:3]
    for j in jpg_files:
        shutil.copy2(j, os.path.join(ocr_dst_dir, os.path.basename(j)))
    print(f"[-] Copied {len(jpg_files)} sample OCR JPEGs to samples/ocr/")

print("Migration completed successfully!")
