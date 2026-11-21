"""Add Arahan Perbendaharaan (from mof.gov.my) to manifest.json as bidang "AP".

Usage: python -I add_ap.py <saved_mof_ap_page.html> <pekeliling_root>
Fetch the page first:  curl -sL -A Mozilla/5.0 https://www.mof.gov.my/portal/ms/arahan-perbendaharaan -o mof_ap.html
Idempotent: replaces existing AP entries; keeps sha256 of unchanged URLs so download.py skips them.
"""
import json, re, sys, urllib.parse, urllib.request
from bs4 import BeautifulSoup

PAGE = "https://www.mof.gov.my/portal/ms/arahan-perbendaharaan"
UA = "Mozilla/5.0 (X11; Linux x86_64) pekeliling-mirror/1.0"
T_MAIN, T_SE, T_TEKS = "1. ARAHAN PERBENDAHARAAN (PINDAAN 2023)", "2. SURAT EDARAN PINDAAN AP", "3. TEKS AP YANG DIPINDA"

def clean(s): return " ".join((s or "").split())

def main(src, root):
    soup = BeautifulSoup(open(src, "rb").read(), "lxml"); docs = []
    # main AP book: flipbook folder -> settings.js -> source pdf
    flip = next((a["href"] for a in soup.find_all("a", href=True) if re.search(r"/ap20\d\d/?$", a["href"])), None)
    if flip:
        flip = urllib.parse.urljoin(PAGE, flip.rstrip("/") + "/")
        js = urllib.request.urlopen(urllib.request.Request(flip + "settings.js", headers={"User-Agent": UA}), timeout=60).read().decode("utf-8", "replace")
        m = re.search(r'source:\s*"([^"]+\.pdf)"', js)
        if m:
            docs.append((T_MAIN, "ARAHAN PERBENDAHARAAN (PINDAAN 2023)", urllib.parse.urljoin(flip, m.group(1))))
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href.lower().endswith(".pdf"): continue
        url = urllib.parse.urljoin(PAGE, href); fn = url.rsplit("/", 1)[1]
        if "/senarai-pindaan/" in url:
            docs.append((T_TEKS, "TEKS PINDAAN " + re.sub(r"(?i)^AP(\d+)([a-z]*)\.pdf$", lambda m: f"AP {m.group(1)}{('(' + m.group(2) + ')') if m.group(2) else ''}", fn).upper(), url))
        elif "pemilikan" in fn.lower():
            docs.append((T_MAIN, "SENARAI PEMILIKAN ARAHAN PERBENDAHARAAN (PINDAAN 2023)", url))
        else:  # surat edaran: label = nearest preceding heading text
            lab = next((clean(t) for t in a.find_all_previous(string=True) if re.match(r"(?i)(surat edaran|pindaan arahan)", clean(t))), fn)
            docs.append((T_SE, lab.upper(), url))
    seen, out = set(), []
    for topic, label, url in docs:
        if url in seen: continue
        seen.add(url); out.append((topic, label, url))
    mf = f"{root}/manifest.json"; man = json.load(open(mf))
    old = {d["url"]: d for d in man if d["bidang"] == "AP"}
    man = [d for d in man if d["bidang"] != "AP"]
    topics = [T_MAIN, T_SE, T_TEKS]; counters = {}
    for topic, label, url in sorted(out, key=lambda x: (topics.index(x[0]), x[1])):
        counters[topic] = counters.get(topic, 0) + 1
        rec = {"bidang": "AP", "bidang_name": "ARAHAN PERBENDAHARAAN", "topic_no": topics.index(topic) + 1, "topic": topic,
               "item_no": counters[topic], "label": label, "title": label, "type": "ap", "uuid": None,
               "server_path": None, "url": url, "source_page": PAGE}
        if url in old:
            for k in ("sha256", "bytes", "downloaded_at", "local_path"):
                if k in old[url]: rec[k] = old[url][k]
        man.append(rec)
    json.dump(man, open(mf, "w"), ensure_ascii=False, indent=1)
    for t in topics:
        print(t); [print("   ", r[1], "|", r[2].rsplit("/", 1)[1]) for r in out if r[0] == t]

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
