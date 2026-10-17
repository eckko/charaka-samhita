#!/usr/bin/env python3
"""Stage 2: give every collected line its book ID (PP.CC.V[x]).

Rules (see FORMAT.md; the verse number is the source's own):
- xml:id "Ca.S.A.V" or "Ca.S.A.V.W" ...: part S, chapter A, verse = what
  follows the chapter number ("3", "3-4", "66.1", "2.15" = pada 2, verse 15).
- Lines with the same verse number that follow each other form one verse;
  a verse of several lines gets letters a, b, c ... in order.
- A verse line (<l>) without an xml:id continues the verse above it.
- A prose paragraph (<p>) without an xml:id gets P1, P2 ... in the chapter.
- A colophon (<trailer>) is a paragraph too (kind "trailer").
Nothing is converted here; text is still the source's IAST.
"""
import json
import re
import string
import sys
from collections import Counter

ID_RE = re.compile(r"^Ca\.(\d+)\.(\d+)\.(.+)$")
SHORT_RE = re.compile(r"^Ca\.(\d+)-(\d+)$|^Ca\.(\d+)\.(\d+)-(\d+)$")


def assign(chapters):
    problems = []
    out = []
    for chapter in chapters:
        part, chap = chapter["sthana"], chapter["adhyaya"]
        rows = []          # each: dict(verse, kind, text, ...)
        paragraph = 0
        for line in chapter["lines"]:
            xml_id = (line["xml_id"] or "").strip()
            verse = None
            if xml_id:
                match = ID_RE.match(xml_id)
                short = SHORT_RE.match(xml_id)
                if not match and short and short.group(3):
                    # "Ca.6.12-103" in chapter 6.12: the dot before the verse
                    # number is missing in the source; "Ca.2.7-1" inside 2.6
                    # is verse "7-1" with the chapter number mistyped.
                    second, third = short.group(4), short.group(5)
                    verse = third if int(second) == chap else f"{second}-{third}"
                    problems.append((part, chap, xml_id,
                                     f"malformed id read as verse {verse}"))
                elif not match:
                    problems.append((part, chap, xml_id, "unparsed id"))
                else:
                    if (int(match.group(1)), int(match.group(2))) != (
                            part, chap):
                        problems.append((part, chap, xml_id,
                                         "id does not match its chapter"))
                    verse = match.group(3)
                    verse = re.sub(r"(?<=\d)[a-z]+$", "", verse)
                    verse = verse.replace(".-", "-")
            if verse is None:
                if line["kind"] == "l" and rows and rows[-1]["verse"] and \
                        not rows[-1]["verse"].startswith("P"):
                    verse = rows[-1]["verse"]       # continuation line
                else:
                    paragraph += 1
                    verse = f"P{paragraph}"
            rows.append(dict(line, verse=verse))
        # letters
        i = 0
        while i < len(rows):
            j = i
            while j + 1 < len(rows) and rows[j + 1]["verse"] == rows[i]["verse"] \
                    and not rows[i]["verse"].startswith("P"):
                j += 1
            size = j - i + 1
            for k in range(i, j + 1):
                letter = "" if size == 1 else string.ascii_lowercase[k - i]
                rows[k]["id"] = f"{part:02d}.{chap:02d}.{rows[k]['verse']}{letter}"
            i = j + 1
        by_id = {}
        for r in rows:
            by_id.setdefault(r["id"], []).append(r)
        for line_id, group in by_id.items():
            if len(group) > 1 and all(re.search(r"\d([a-z])$", (g["xml_id"] or "").strip()) for g in group):
                for g in group:
                    suffix = (g["xml_id"] or "").strip()[-1]
                    g["id"] = re.sub(r"[a-z]?$", "", line_id) + suffix
                problems.append((part, chap, line_id,
                                 "source letters kept: " + ", ".join(g["id"] for g in group)))
        seen = Counter(r["id"] for r in rows)
        for line_id, count in seen.items():
            if count > 1:
                problems.append((part, chap, line_id, f"duplicate x{count}"))
        out.append(dict(chapter, rows=rows))
    return out, problems


if __name__ == "__main__":
    chapters = json.load(open(sys.argv[1], encoding="utf8"))
    result, problems = assign(chapters)
    json.dump(result, open(sys.argv[2], "w", encoding="utf8"),
              ensure_ascii=False, indent=1)
    print(sum(len(c["rows"]) for c in result), "rows;",
          len(problems), "problems")
    for problem in problems[:60]:
        print(problem)
