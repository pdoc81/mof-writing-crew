"""Download every document in manifest.json into <root>/<BIDANG - NAME>/<NN - TOPIC>/<NN - LABEL>.pdf

Usage: python -I download.py <pekeliling_root>
Resumable: skips files already present with a matching sha256 in the manifest.
"""
import hashlib, json, re, sys, time, urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (X11; Linux x86_64) pekeliling-mirror/1.0"

def safe(s, n=110):
    s = re.sub(r'[\\/:*?"<>|\x00-\x1f]', "-", s).strip(" .")
    return re.sub(r"\s+", " ", s)[:n].rstrip(" .")

def topic_dir(topic, topic_no):
    m = re.match(r"^\s*(\d+)\s*\.\s*(.*)$", topic)
    if m:
        return f"{int(m.group(1)):02d} - {safe(m.group(2))}"
    return f"00 - {safe(re.sub(r'^[*.\s]+', '', topic))}"

def main(root):
    root = Path(root); mf = root / "manifest.json"
    docs = json.load(open(mf)); ok = skip = fail = 0
    for i, d in enumerate(docs, 1):
        rel = Path(f"{d['bidang']} - {d['bidang_name'].title()}") / topic_dir(d["topic"], d["topic_no"]) / f"{d['item_no']:02d} - {safe(d['label'])}.pdf"
        d["local_path"] = str(rel); dest = root / rel
        if dest.exists() and d.get("sha256") == hashlib.sha256(dest.read_bytes()).hexdigest():
            skip += 1; continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            req = urllib.request.Request(d["url"], headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read(); ctype = r.headers.get("Content-Type", "")
            data = data.lstrip(b"\r\n\t \x00\xef\xbb\xbf")  # server prepends a stray newline
            if not data.startswith(b"%PDF"):
                raise ValueError(f"not a PDF (Content-Type {ctype}, {len(data)} bytes)")
            dest.write_bytes(data)
            d.update(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data),
                     downloaded_at=time.strftime("%Y-%m-%dT%H:%M:%S%z")); d.pop("error", None); ok += 1
        except Exception as e:
            d["error"] = str(e); fail += 1; print(f"FAIL [{i}] {rel}: {e}", file=sys.stderr)
        if i % 25 == 0:
            print(f"{i}/{len(docs)}", flush=True); json.dump(docs, open(mf, "w"), ensure_ascii=False, indent=1)
        time.sleep(0.5)
    json.dump(docs, open(mf, "w"), ensure_ascii=False, indent=1)
    print(f"done: downloaded {ok}, skipped {skip}, failed {fail}")

if __name__ == "__main__":
    main(sys.argv[1])
