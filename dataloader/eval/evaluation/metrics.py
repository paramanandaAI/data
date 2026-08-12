# -*- coding: utf-8 -*-
"""
Evaluation Metrics for Nepali Denoising: CER, WER, BLEU placeholders
"""

def compute_cer(reference: str, hypothesis: str) -> float:
    """
    Computes Character Error Rate (CER) between reference and hypothesis text.
    """
    if not reference:
        return 0.0 if not hypothesis else 1.0
    
    # Levenshtein distance at character level
    r = list(reference)
    h = list(hypothesis)
    d = [[0] * (len(h) + 1) for _ in range(len(r) + 1)]
    for i in range(len(r) + 1):
        d[i][0] = i
    for j in range(len(h) + 1):
        d[0][j] = j
    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            if r[i - 1] == h[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])
    return d[len(r)][len(h)] / len(r)

def compute_wer(reference: str, hypothesis: str) -> float:
    """
    Computes Word Error Rate (WER) between reference and hypothesis text.
    """
    r = reference.split()
    h = hypothesis.split()
    if not r:
        return 0.0 if not h else 1.0
    
    d = [[0] * (len(h) + 1) for _ in range(len(r) + 1)]
    for i in range(len(r) + 1):
        d[i][0] = i
    for j in range(len(h) + 1):
        d[0][j] = j
    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            if r[i - 1] == h[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])
    return d[len(r)][len(h)] / len(r)
