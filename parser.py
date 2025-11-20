import os
import re
from typing import List, Dict

# try to import PyPDF2; if not available, PDF parsing will be skipped gracefully
try:
    import PyPDF2
except Exception:
    PyPDF2 = None

def _read_txt(path: str) -> str:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def _read_pdf(path: str) -> str:
    if PyPDF2 is None:
        return ''
    text = []
    try:
        with open(path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for p in reader.pages:
                try:
                    text.append(p.extract_text() or '')
                except Exception:
                    continue
    except Exception:
        return ''
    return '\n'.join(text)

def parse_resumes(folder: str) -> List[Dict]:
    """Parse all resumes in a folder. Supports .txt and .pdf (if PyPDF2 installed)."""
    data = []
    if not os.path.isdir(folder):
        print(f"Resumes folder '{folder}' not found. Returning empty list.")
        return data
    for fname in os.listdir(folder):
        path = os.path.join(folder, fname)
        if os.path.isfile(path):
            name, ext = os.path.splitext(fname)
            ext = ext.lower()
            content = ''
            if ext == '.txt':
                content = _read_txt(path)
            elif ext == '.pdf':
                content = _read_pdf(path)
            else:
                # skip unsupported file types but include filename
                continue
            data.append({'name': name, 'path': path, 'content': content.lower()})
    return data
