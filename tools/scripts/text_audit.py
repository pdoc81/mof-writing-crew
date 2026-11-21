"""Validate every PDF in manifest and classify pages: text layer present vs needs OCR.
Usage: python -I text_audit.py <pekeliling_root>   -> writes tools/text_audit.json
"""
import json, subprocess, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

def pages(p):
    out = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True)
    if out.returncode: return None
    for l in out.stdout.splitlines():
        if l.startswith("Pages:"): return int(l.split()[1])

def audit(root, d):
    p = root / d["local_path"]; n = pages(p)
    if n is None: return {**d, "valid": False}
    need = []
    for i in range(1, n + 1):
        t = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", str(p), "-"], capture_output=True, text=True, errors="replace").stdout
        letters = sum(c.isalpha() for c in t)
        if letters < 80: need.append(i)
    return {"local_path": d["local_path"], "bidang": d["bidang"], "valid": True, "pages": n, "ocr_pages": need}

root = Path(sys.argv[1]); docs = json.load(open(root / "manifest.json"))
with ThreadPoolExecutor(16) as ex: res = list(ex.map(lambda d: audit(root, d), docs))
json.dump(res, open(root / "tools/text_audit.json", "w"), ensure_ascii=False, indent=1)
bad = [r for r in res if not r["valid"]]; tp = sum(r.get("pages", 0) for r in res); op = sum(len(r.get("ocr_pages", [])) for r in res)
full = [r for r in res if r["valid"] and r["ocr_pages"] and len(r["ocr_pages"]) == r["pages"]]
part = [r for r in res if r["valid"] and r["ocr_pages"] and len(r["ocr_pages"]) < r["pages"]]
print(f"invalid PDFs: {len(bad)}  total pages: {tp}  pages needing OCR: {op} ({op*100//max(tp,1)}%)")
print(f"docs fully text: {len(res)-len(bad)-len(full)-len(part)}  fully scanned: {len(full)}  mixed: {len(part)}")
from collections import Counter
print("scanned/mixed per bidang:", dict(Counter(r['bidang'] for r in full + part)))
