#!/usr/bin/env python3
"""Stage 1 of the Charaka extraction: read SARIT's TEI file into plain
records, still in IAST. Nothing is converted or corrected here.

Usage: python3 sarit_collect.py raw/carakasamhita.xml out.json

Output: a list of chapter records
  {"sthana": 1, "adhyaya": 1, "head": "...", "sthana_head": "...",
   "lines": [{"kind": "p"|"l"|"trailer", "xml_id": str|None,
              "text": str, "notes": [str], "app": [[lem, rdg]],
              "pada": int|None}]}
Text of a line = its own words only: <label>, <note> (the edition's
footnote variants) and the <rdg> half of an <app> are left out of the
text and reported in "notes" / "app", never merged in.
"""
import json
import re
import sys
from lxml import etree

TEI = "{http://www.tei-c.org/ns/1.0}"
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"


def squash(text):
    return re.sub(r"\s+", " ", text).strip()


def line_text(element):
    """Own text of an element, plus its notes and apparatus entries."""
    parts, notes, apps = [], [], []

    def walk(node):
        if node.text:
            parts.append(node.text)
        for child in node:
            tag = child.tag
            if tag == TEI + "label":
                pass
            elif tag == TEI + "note":
                notes.append(squash("".join(child.itertext())))
            elif tag == TEI + "app":
                lem = child.find(TEI + "lem")
                rdg = child.find(TEI + "rdg")
                lem_text = "".join(lem.itertext()) if lem is not None else ""
                rdg_text = "".join(rdg.itertext()) if rdg is not None else ""
                parts.append(lem_text)
                apps.append([squash(lem_text), squash(rdg_text)])
            else:
                walk(child)
            if child.tail:
                parts.append(child.tail)

    walk(element)
    return squash("".join(parts)), notes, apps


def collect(path):
    tree = etree.parse(path)
    body = tree.find(".//" + TEI + "body")
    chapters = []
    for sthana in body.findall(TEI + "div"):
        sthana_head = squash("".join(sthana.find(TEI + "head").itertext()))
        for adhyaya in sthana.findall(TEI + "div"):
            head = adhyaya.find(TEI + "head")
            record = {
                "sthana": int(sthana.get("n")),
                "adhyaya": int(adhyaya.get("n")),
                "sthana_head": sthana_head,
                "head": squash("".join(head.itertext())) if head is not None
                else "",
                "lines": [],
            }
            for node in adhyaya.iter(TEI + "p", TEI + "l", TEI + "trailer"):
                if node.tag == TEI + "p" and node.getparent().tag != TEI + "div":
                    continue  # defensive: p inside something else
                text, notes, apps = line_text(node)
                if not text and not notes:
                    continue  # empty spacer element
                pada = None
                ancestor = node.getparent()
                while ancestor is not None and ancestor is not adhyaya:
                    if ancestor.get("subtype") == "pāda":
                        pada = int(ancestor.get("n"))
                    ancestor = ancestor.getparent()
                record["lines"].append({
                    "kind": node.tag.replace(TEI, ""),
                    "xml_id": (node.get(XML_ID) or "").strip() or None,
                    "text": text, "notes": notes, "app": apps,
                    "pada": pada,
                })
            chapters.append(record)
    return chapters


if __name__ == "__main__":
    chapters = collect(sys.argv[1])
    with open(sys.argv[2], "w", encoding="utf8") as handle:
        json.dump(chapters, handle, ensure_ascii=False, indent=1)
    print(len(chapters), "chapters,",
          sum(len(c["lines"]) for c in chapters), "lines")
