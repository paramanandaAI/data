import os
import sys

def inspect_app(filepath, name):
    print(f"=== Inspecting {name} ({filepath}) ===")
    if not os.path.exists(filepath):
        print(f"  [X] File not found: {filepath}")
        return
    
    size = os.path.getsize(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    print(f"  [-] Path: {filepath}")
    print(f"  [-] Size: {size / 1024:.2f} KB ({len(lines)} lines)")
    
    imports = [line.strip() for line in lines if line.strip().startswith("import ") or line.strip().startswith("from ")]
    print(f"  [-] Key Imports ({len(imports)}):")
    for imp in imports[:8]:
        print(f"    - {imp}")

root = r'D:\paramananda\demos'
inspect_app(os.path.join(root, 'kiss', 'app.py'), "Gradio Kiss App Suite")
inspect_app(os.path.join(root, 'ocr', 'demo_experiments', 'app', 'main.py'), "DevaOCR Streamlit Multi-Page App")
inspect_app(os.path.join(root, 'test', 'summarizer_app.py'), "Gradio Summarizer App")
inspect_app(os.path.join(root, 'test', 'qa_rag_app.py'), "Gradio RAG Q&A App")
inspect_app(os.path.join(root, 'test', 'keyboard_visualizer_app.py'), "Gradio Keyboard Visualizer App")
