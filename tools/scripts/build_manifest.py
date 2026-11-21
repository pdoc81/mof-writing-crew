"""Parse a saved copy of https://ppp.treasury.gov.my/ into manifest.json.

Usage: python -I build_manifest.py <saved_homepage.html> <out_manifest.json>
"""
import json, sys
from bs4 import BeautifulSoup

BASE = "https://ppp.treasury.gov.my/loadpdf/{type}/{uuid}"
BIDANG = {"PB": "PENGURUSAN BELANJAWAN", "PK": "PEROLEHAN KERAJAAN", "WP": "PENGURUSAN WANG AWAM",
          "AM": "PENGURUSAN ASET", "PS": "TADBIR URUS KEWANGAN", "PA": "PELABURAN STRATEGIK",
          "LB": "SYARIKAT TERSENARAI BUMIPUTERA"}

def clean(s):
    return " ".join((s or "").split())

def main(src, out):
    soup = BeautifulSoup(open(src, "rb").read(), "lxml")  # HTML comments are ignored by the parser
    docs = []
    for code, name in BIDANG.items():
        pane = soup.find(id=f"tab{code}")
        if pane is None:
            print(f"WARN: tab{code} not found", file=sys.stderr); continue
        for t_i, header in enumerate(pane.select(".accordion-header"), 1):
            title_el = header.select_one(".accordion-title > div") or header.select_one(".accordion-title")
            topic = clean(title_el.get_text()).lstrip(". ").strip()
            content = header.find_next_sibling(class_="accordion-content")
            if content is None:
                continue
            for li_i, li in enumerate(content.select("li.list-group-item"), 1):
                label = clean((li.select_one(".col-9") or li).get_text())
                for b in li.select("[data-uuid]"):
                    uuid, typ = b.get("data-uuid"), b.get("data-type")
                    if not uuid or not b.get("data-path"):
                        continue
                    docs.append({"bidang": code, "bidang_name": name, "topic_no": t_i, "topic": topic,
                                 "item_no": li_i, "label": label, "title": clean(b.get("data-title")),
                                 "type": typ, "uuid": uuid, "server_path": b.get("data-path"),
                                 "url": BASE.format(type=typ, uuid=uuid)})
    # de-duplicate by uuid within same bidang/topic
    seen, uniq = set(), []
    for d in docs:
        k = (d["bidang"], d["topic_no"], d["uuid"])
        if k not in seen:
            seen.add(k); uniq.append(d)
    json.dump(uniq, open(out, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    c = Counter(d["bidang"] for d in uniq); tp = Counter(d["type"] for d in uniq)
    print("docs:", len(uniq), "unique uuids:", len({d['uuid'] for d in uniq}))
    print("per bidang:", dict(c)); print("types:", dict(tp))
    print("topics:", {b: len({d['topic_no'] for d in uniq if d['bidang']==b}) for b in BIDANG})

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
