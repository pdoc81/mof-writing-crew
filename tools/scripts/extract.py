"""Extract text from every circular into Markdown with page markers.

Text pages -> pdftotext -layout. Scanned pages (from tools/text_audit.json) -> PaddleOCR PP-StructureV3
(tables kept as HTML tables). Output: <root>/text/<local_path minus .pdf>.md
Per-page OCR results are cached in tools/cache/ocr/<sha256>/pNNNN.md so the run is resumable.

Usage: python -I extract.py <pekeliling_root> [--limit-pages N] [--only SUBSTR]
"""
import argparse, json, os, subprocess, sys, tempfile, time
from pathlib import Path

os.environ.setdefault("PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK", "True")
_pipe = None

def pipeline():
    global _pipe
    if _pipe is None:
        from paddleocr import PPStructureV3
        _pipe = PPStructureV3(lang="ms", enable_mkldnn=os.environ.get("PEKELILING_MKLDNN", "1") == "1", use_doc_orientation_classify=True,
                              use_doc_unwarping=False, use_textline_orientation=False,
                              use_formula_recognition=False, use_seal_recognition=False, use_chart_recognition=False)
    return _pipe

def text_page(pdf, n):
    return subprocess.run(["pdftotext", "-f", str(n), "-l", str(n), "-layout", str(pdf), "-"],
                          capture_output=True, text=True, errors="replace").stdout.rstrip()

def ocr_page(pdf, n, cache):
    f = cache / f"p{n:04d}.md"
    if f.exists():
        return f.read_text()
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-f", str(n), "-l", str(n), "-r", "200", "-png", str(pdf), f"{td}/pg"], check=True)
        img = next(Path(td).glob("pg*.png"))
        md = "\n".join(r.markdown["markdown_texts"] for r in pipeline().predict(str(img))).strip()
    cache.mkdir(parents=True, exist_ok=True); f.write_text(md)
    return md

def yaml_str(s):
    return json.dumps(s, ensure_ascii=False)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("root"); ap.add_argument("--limit-pages", type=int)
    ap.add_argument("--only"); a = ap.parse_args()
    root = Path(a.root); docs = json.load(open(root / "manifest.json"))
    audit = {r["local_path"]: r for r in json.load(open(root / "tools/text_audit.json"))}
    out_root = root / "text"; t0 = time.time(); ocr_done = 0
    total_ocr = sum(len(audit[d["local_path"]]["ocr_pages"]) for d in docs if not a.only or a.only in d["local_path"])
    for i, d in enumerate(docs, 1):
        if a.only and a.only not in d["local_path"]:
            continue
        pdf = root / d["local_path"]; au = audit[d["local_path"]]
        out = out_root / Path(d["local_path"]).with_suffix(".md")
        if out.exists() and f"sha256: {d['sha256']}" in out.read_text()[:2000]:
            ocr_done += len(au["ocr_pages"]); continue
        cache = root / "tools/cache/ocr" / d["sha256"]; parts = []
        for n in range(1, au["pages"] + 1):
            if n in au["ocr_pages"]:
                body, how = ocr_page(pdf, n, cache), "ocr"; ocr_done += 1
                el = time.time() - t0
                print(f"[{i}/{len(docs)}] OCR {ocr_done}/{total_ocr} {d['bidang']} p{n} ({el/60:.1f} min elapsed)", flush=True)
                if a.limit_pages and ocr_done >= a.limit_pages:
                    print("limit reached"); return
            else:
                body, how = text_page(pdf, n), "text"
            parts.append(f"<!-- page {n} ({how}) -->\n\n{body}\n")
        fm = ["---", f"bidang: {d['bidang']}", f"bidang_name: {yaml_str(d['bidang_name'])}", f"topic: {yaml_str(d['topic'])}",
              f"title: {yaml_str(d['title'] or d['label'])}", f"label: {yaml_str(d['label'])}", f"source_url: {d['url']}",
              f"pdf: {yaml_str(d['local_path'])}", f"sha256: {d['sha256']}", f"pages: {au['pages']}",
              f"ocr_pages: {au['ocr_pages']}", f"extracted_at: {time.strftime('%Y-%m-%d')}", "---", ""]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(fm) + f"# {d['title'] or d['label']}\n\n" + "\n".join(parts))
    print(f"done in {(time.time()-t0)/60:.1f} min; OCR pages: {ocr_done}")

if __name__ == "__main__":
    main()
