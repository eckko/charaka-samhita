#!/usr/bin/env python3
"""Build the Charaka Samhita raw source bank from SARIT's TEI file.

Usage (from reference/charaka-samhita):  python3 -I tools/build.py

Pipeline: sarit_collect -> sarit_ids -> sarit_convert, then writes
  text/ chNN.CC.md or pNN.md   Devanagari lines "ID | text"
  raw/iast/<same name>.tsv     ID, kind, xml:id, the source's own IAST
  toc.md  STATUS.md  ISSUES.md
Nothing is typed by hand into the text files.
"""
import json
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import chapter_english as ce            # noqa: E402
import chapter_names as cn              # noqa: E402
import sarit_collect                    # noqa: E402
import sarit_convert                    # noqa: E402
import sarit_ids                        # noqa: E402

RAW = ROOT / "raw" / "carakasamhita.xml"
PART_FILE_PARTS = {2, 3, 4, 5, 7}       # whole sthana in one file (<1000 lines)
PADA_CHAPTERS = {(6, 1), (6, 2)}
BRANCH = "docs/2026-10-17/version-1"
TODAY = "2026-10-17"


def deva(text):
    return sarit_convert.convert_line(text)[0]


def file_name(part, chap):
    if part in PART_FILE_PARTS:
        return f"p{part:02d}.md"
    return f"ch{part:02d}.{chap:02d}.md"


def verse_of(line_id):
    return line_id.split(".", 2)[2]


def numbering_report(chapter):
    """Gaps and order problems in the plain verse numbers of a chapter."""
    part, chap = chapter["sthana"], chapter["adhyaya"]
    groups = OrderedDict()
    for row in chapter["rows"]:
        v = re.sub(r"(?<=\d)[a-z]$", "", verse_of(row["id"]))
        groups.setdefault(v, None)
    notes = []
    streams = OrderedDict()
    for v in groups:
        if v.startswith("P"):
            continue
        if (part, chap) in PADA_CHAPTERS:
            m = re.match(r"^(\d+)\.(\d+)$", v)
            if m:
                streams.setdefault(m.group(1), []).append(int(m.group(2)))
            continue
        m = re.match(r"^(\d+)(?:-(\d+))?$", v)
        if m:
            low = int(m.group(1))
            high = int(m.group(2)) if m.group(2) else low
            if high < low:           # "4-2" is a sub-paragraph of verse 4
                high = low
            streams.setdefault("", []).extend(range(low, high + 1))
    for key, numbers in streams.items():
        seen = []
        for n in numbers:
            if not seen or n != seen[-1]:
                seen.append(n)
        label = f"pāda {key}: " if key else ""
        expected = 1
        gaps = []
        for n in seen:
            if n > expected:
                gaps.append(f"{expected}-{n - 1}" if n - 1 > expected
                            else str(expected))
            expected = max(expected, n + 1)
        back = sum(1 for a, b in zip(seen, seen[1:]) if b < a)
        if gaps:
            notes.append(f"{label}numbers missing: {', '.join(gaps[:12])}"
                         + (" ..." if len(gaps) > 12 else ""))
        if back:
            notes.append(f"{label}number order goes backwards {back} time(s)")
    return notes


def compress(keys):
    """[(6,9),(6,10),(6,11)] -> '6.9-6.11' style text."""
    out, run = [], []
    for key in keys:
        if run and key[0] == run[-1][0] and key[1] == run[-1][1] + 1:
            run.append(key)
        else:
            if run:
                out.append(run)
            run = [key]
    if run:
        out.append(run)
    return ", ".join(f"{r[0][0]}.{r[0][1]}" if len(r) == 1 else
                     f"{r[0][0]}.{r[0][1]}-{r[-1][0]}.{r[-1][1]}"
                     for r in out)


def main():
    chapters = sarit_collect.collect(str(RAW))
    chapters, id_problems = sarit_ids.assign(chapters)
    issues = []          # (line id, kind, what, source, check)
    stats = {}
    out_text = OrderedDict()   # file -> list of lines
    out_iast = OrderedDict()
    for chapter in chapters:
        part, chap = chapter["sthana"], chapter["adhyaya"]
        key = (part, chap)
        anchors = 0
        dropped = 0
        lines = 0
        name = file_name(part, chap)
        for row in chapter["rows"]:
            text, flags, count = sarit_convert.convert_line(row["text"])
            anchors += count
            if not text:
                dropped += 1
                issues.append((row["id"], "other",
                               "line held only the editor's footnote text; "
                               "left out", "S1", "see raw/iast"))
                continue
            for kind, detail in flags:
                issues.append((row["id"], kind, detail, "S1",
                               "compare with the printed edition"))
            for note in row["notes"]:
                issues.append((row["id"], "variant",
                               f"edition footnote (note element): {note}",
                               "S1", "compare with the printed edition"))
            for lem, rdg in row["app"]:
                issues.append((row["id"], "variant",
                               f"S1 reads '{lem}', Wujastyk's note reads "
                               f"'{rdg}' (app element)", "S1",
                               "compare with the printed edition"))
            out_text.setdefault(name, []).append(f"{row['id']} | {text}")
            out_iast.setdefault(name, []).append(
                "\t".join([row["id"], row["kind"], row["xml_id"] or "-",
                           row["text"]]))
            lines += 1
        verses = []
        kept = {r.split(" | ")[0] for r in out_text.get(name, [])}
        for row in chapter["rows"]:
            if row["id"] not in kept:
                continue
            v = verse_of(row["id"])
            v = re.sub(r"(?<=\d)[a-z]$", "", v) if not v.startswith("P") \
                else v
            if v not in verses:
                verses.append(v)
        nm, how = cn.name_of(chapter)
        stats[key] = dict(lines=lines, verses=len(verses), anchors=anchors,
                          dropped=dropped, file=name, name=nm, how=how,
                          numbering=numbering_report(chapter),
                          opening=next((r["text"] for r in chapter["rows"]
                                        if r["text"].startswith("athā")
                                        and "vyākhyāsyāmaḥ" in r["text"]),
                                       ""))
        for note in stats[key]["numbering"]:
            issues.append((f"{part:02d}.{chap:02d}", "numbering", note,
                           "S1", "compare numbering with the print"))
    for part, chap, xml_id, message in id_problems:
        issues.append((f"{part:02d}.{chap:02d}", "numbering",
                       f"xml:id {xml_id}: {message}", "S1",
                       "check the edition's numbering"))

    # ---- write text and raw/iast
    (ROOT / "text").mkdir(exist_ok=True)
    (ROOT / "raw" / "iast").mkdir(exist_ok=True)
    for old in (ROOT / "text").glob("*.md"):
        old.unlink()
    for old in (ROOT / "raw" / "iast").glob("*.tsv"):
        old.unlink()
    for name, lines in out_text.items():
        (ROOT / "text" / name).write_text("\n".join(lines) + "\n",
                                          encoding="utf8")
    for name, lines in out_iast.items():
        (ROOT / "raw" / "iast" / name.replace(".md", ".tsv")).write_text(
            "\n".join(lines) + "\n", encoding="utf8")

    # ---- toc.md
    dridhabala = [key for key, ch in zip(stats, chapters) if any(
        "dṛḍhabala" in r["text"] for r in ch["rows"]
        if r["kind"] == "trailer")]
    AUTHOR_LINE = (
        "Agniveśa's tantra, revised (pratisaṃskṛta) by Caraka, as the "
        "colophons say (\"agniveśakṛte tantre carakapratisaṃskṛte\"). "
        "The colophons of these chapters also mention Dṛḍhabala's "
        "completion (\"dṛḍhabalasaṃpūrite\", mostly with \"aprāpte\"): "
        + compress(dridhabala) + ". Tradition: Ayurveda (inferred).")
    total_verses = sum(s["verses"] for s in stats.values())
    toc = [
        "# Charaka Samhita (चरकसंहिता)", "",
        "- Author / compiler: " + AUTHOR_LINE,
        "- Subject and purpose of the book: a classical treatise of "
        "Ayurveda (internal medicine). Each chapter opens \"athāto X "
        "vyākhyāsyāmaḥ\" (\"now we shall expound X\"), so every chapter "
        "announces its own topic (column Purpose, text itself).",
        "- Base edition: Yādavaśarman Trivikramātmaja Ācārya, 3rd ed. "
        "Nirnaya Sagar Press, Bombay 1941, with Cakrapāṇidatta's "
        "Āyurvedadīpikā (commentary NOT included in the e-text); e-text by "
        "Yamashita, Muroya, Yamanaka, Madhu K. P. (Kyoto), TEI by Dominik "
        "Wujastyk, as published by SARIT (source S1 in sources.md).",
        "- Mapping: part = sthāna, chapter = adhyāya, verse = verse or prose "
        "paragraph as numbered in the edition (IDs PP.CC.V). In chapters "
        "6.1 and 6.2 (Rasāyana, Vājīkaraṇa) the edition numbers verses "
        "inside four pādas; the pāda is the first part of V: "
        "06.01.2.15 = pāda 2, verse 15. In Sūtrasthāna 1 a verse inserted "
        "in parentheses after verse 66 is 66.1 (and so on). Unnumbered prose "
        "paragraphs are P1, P2, ... in the chapter; each chapter's "
        "colophon is its last P line.",
        f"- Totals: 8 parts, 120 chapters, {total_verses} verse units "
        f"(numbered verses and P paragraphs) extracted; traditional count "
        "unknown (the text states none).", "",
        "Columns Sanskrit name: from the chapter's colophon (final -o written "
        "as -aḥ, avagraha mark dropped), converted to Devanagari. English "
        "name: literal rendering written by the extractor, (inferred), not "
        "from a source. Purpose: the chapter's own opening formula.", ""]
    for part in range(1, 9):
        iast, latin, english = ce.PARTS[part]
        toc += [f"## Part {part:02d}: {deva(iast)} ({latin}: {english}, "
                f"inferred)", "",
                f"Purpose: {english} (inferred from the name)", "",
                "| Part | Chapter | Sanskrit name | English name | Purpose | "
                "Verses (extracted) | Verses (traditional) | File | Status |",
                "|---|---|---|---|---|---|---|---|---|"]
        for (p, c), s in stats.items():
            if p != part:
                continue
            purpose = deva(s["opening"]) if s["opening"] else "-"
            toc.append(
                f"| {p:02d} | {c:02d} | {deva(s['name'])} | "
                f"{ce.ENGLISH[(p, c)]} (inferred) | {purpose} | "
                f"{s['verses']} | unknown | text/{s['file']} | extracted |")
        toc.append("")
    (ROOT / "toc.md").write_text("\n".join(toc), encoding="utf8")

    # ---- STATUS.md
    status = [f"# Status: charaka-samhita", "",
              f"Updated: {TODAY} on branch {BRANCH}. Base source: S1 "
              "(SARIT). Hindi and English translations: not fetched.", "",
              "| Part | Chapter | Sanskrit lines | Source | Hindi | English "
              "| Check | Notes |", "|---|---|---|---|---|---|---|---|"]
    for (p, c), s in stats.items():
        notes = []
        if s["anchors"]:
            notes.append(f"{s['anchors']} footnote anchors (&) removed")
        if s["dropped"]:
            notes.append(f"{s['dropped']} footnote-only line(s) left out")
        if s["how"] != "colophon":
            notes.append(f"name: {s['how']}")
        status.append(f"| {p:02d} | {c:02d} | {s['lines']} | S1 | -- | -- | "
                      f"CHECK | {'; '.join(notes)} |")
    status += ["", "## Next",
               "- Find Hindi and English translations (step 5 of the skill).",
               "- Second source to cross-check S1 (GRETIL is blocked from "
               "this workspace; ask the owner to download it).",
               "- Owner decision: the quiz repo's data/ files for "
               "Sūtrasthāna 1-4 hold a differently segmented version; see "
               "README.md of this folder.", ""]
    (ROOT / "STATUS.md").write_text("\n".join(status), encoding="utf8")

    # ---- ISSUES.md
    order = {"variant": 0, "possible-typo": 1, "numbering": 2, "other": 3}
    issues.sort(key=lambda r: (order.get(r[1], 9), r[0]))
    lines = ["# Issues: charaka-samhita", "",
             "Generated by tools/build.py. Nothing in the text files was "
             "changed because of an issue.", "",
             "| Line ID | Kind | What | Source(s) | Suggested check |",
             "|---|---|---|---|---|"]
    for line_id, kind, what, src, check in issues:
        what = what.replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {line_id} | {kind} | {what} | {src} | {check} |")
    (ROOT / "ISSUES.md").write_text("\n".join(lines) + "\n", encoding="utf8")

    import subprocess
    result = subprocess.run(
        [sys.executable, "-I", str(ROOT.parent / "tools" /
                                   "check_extraction.py"), str(ROOT)],
        capture_output=True, text=True)
    mark = "pass" if result.returncode == 0 else "FAIL"
    path = ROOT / "STATUS.md"
    path.write_text(path.read_text(encoding="utf8").replace("CHECK", mark),
                    encoding="utf8")
    print("checker:", result.stdout.strip().splitlines()[-1])
    print(len(out_text), "text files;", sum(len(v) for v in out_text.values()),
          "lines;", len(issues), "issues;", total_verses, "verse units")
    print(Counter(i[1] for i in issues))


if __name__ == "__main__":
    main()
