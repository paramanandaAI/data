import os
import sys

def check_large_files(root_dir, size_limit_mb=50):
    print(f"Scanning '{root_dir}' for files > {size_limit_mb}MB...")
    large_files = []
    size_limit_bytes = size_limit_mb * 1024 * 1024

    for root, dirs, files in os.walk(root_dir):
        # Skip git directory and old_old backup directory
        if '.git' in dirs:
            dirs.remove('.git')
        if 'old_old' in dirs:
            dirs.remove('old_old')
        
        for f in files:
            fp = os.path.join(root, f)
            try:
                size = os.path.getsize(fp)
                if size > size_limit_bytes:
                    large_files.append((fp, size / (1024 * 1024)))
            except Exception as e:
                pass

    if not large_files:
        print(f"No files larger than {size_limit_mb}MB found in clean workspace!")
    else:
        print(f"Found {len(large_files)} large file(s):")
        for fp, size in large_files:
            print(f" - {fp} ({size:.2f} MB)")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    check_large_files(target)
