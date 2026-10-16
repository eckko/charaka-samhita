#!/usr/bin/env python3
"""Build questions.json for Caraka Su. 1 and 2 (all units).

    python3 tools/make_bank.py data questions.json

Verse data (Sanskrit, word split, Hindi, English, notes) comes from the
verse file. Explanations, mnemonics, the card summary and every question
are written by hand in ch1_authored.py.
"""
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from indic_transliteration import sanscript as S  # noqa: E402
import importlib  # noqa: E402
import pkgutil  # noqa: E402
from ch1_authored import AUTHORED, NOTES_HI  # noqa: E402
from sections import section_of  # noqa: E402
from gram_hi import gram_hi  # noqa: E402
from ch1_aids import AIDS, IMAGES, KIND_LABELS, ORDER  # noqa: E402
from metre import split_pada  # noqa: E402
from make_aid_images import render_spec  # noqa: E402

IMAGE_SPECS = {}
CHAPTERS = {
    1: {"title": "दीर्घञ्जीवितीय", "glob": "batch_*.py",
        "A": AUTHORED, "N": NOTES_HI, "AI": AIDS, "IM": IMAGES},
    2: {"title": "अपामार्गतण्डुलीय", "glob": "ch2_batch_*.py",
        "A": {}, "N": {}, "AI": {}, "IM": {}},
    3: {"title": "आरग्वधीय", "glob": "ch3_batch_*.py",
        "A": {}, "N": {}, "AI": {}, "IM": {}},
    4: {"title": "षड्विरेचनशताश्रितीय", "glob": "ch4_batch_*.py",
        "A": {}, "N": {}, "AI": {}, "IM": {}},
}


def load_batches():
    """Merge batch modules (units authored in groups of ~10), per chapter:
    batch_NN.py for chapter 1, ch2_batch_NN.py for chapter 2."""
    here = Path(__file__).resolve().parent
    only = os.environ.get("BATCHES")  # e.g. "batch_03" while authoring
    for ch, st in CHAPTERS.items():
        for mod in sorted(p.stem for p in here.glob(st["glob"])):
            if only and mod not in only.split(","):
                continue
            m = importlib.import_module(mod)
            clash = set(m.AUTHORED) & set(st["A"])
            assert not clash, (mod, clash)
            st["A"].update(m.AUTHORED)
            st["N"].update(m.NOTES_HI)
            for n, kinds in m.AIDS.items():
                st["AI"][n] = kinds
            for key, spec in getattr(m, "IMAGE_SPECS", {}).items():
                IMAGE_SPECS[(ch,) + key] = spec
                st["IM"][key] = (spec["file"], spec["alt"])


def cid_of(n, ch=1):
    whole, _, part = str(n).partition(".")
    return f"su{ch}-{int(whole):03d}" + (f"-{part}" if part else "")

dev = lambda s: S.transliterate(unicodedata.normalize("NFC", s), S.IAST,
                                S.DEVANAGARI)
DIGITS = str.maketrans("0123456789", "०१२३४५६७८९")
MAP = {"ṛ": "ri", "ṝ": "ri", "ś": "sh", "Ś": "Sh", "ṣ": "sh", "Ṣ": "Sh",
       "ṃ": "m", "ḥ": "h", "ṅ": "n", "ñ": "n", "ṭ": "t", "ḍ": "d",
       "ṇ": "n", "ḷ": "l"}
IAST_CH = set("āīūṛṝḷṅñṭḍṇśṣṃḥĀĪŪṚŚṢ")
WORD = re.compile(r"[A-Za-zāīūṛṝḷṅñṭḍṇśṣṃḥĀĪŪṚŚṢ\-]+")
QUOTE = re.compile(r"(?<![\w])[‘'’“\"]([A-Za-zāīūṛṝḷṅñṭḍṇśṣṃḥ\- ]{1,40}?)"
                   r"[’'’”\"](?![\w])")


def fold_char(c):
    if "ऀ" <= c <= "ॿ":
        return c
    c = MAP.get(c, c)
    return "".join(x for x in unicodedata.normalize("NFKD", c)
                   if not unicodedata.combining(x))


def fold(text):
    """English text with plain Latin letters (no diacritics)."""
    return "".join(fold_char(c) for c in unicodedata.normalize("NFC", text))


def devanagari_words(text):
    return WORD.sub(lambda m: dev(m.group()) if set(m.group()) & IAST_CH
                    else m.group(), text)


def clean_note(text):
    text = QUOTE.sub(lambda m: "‘" + dev(m.group(1)) + "’"
                     if len(m.group(1)) > 1 else m.group(0),
                     unicodedata.normalize("NFC", text))
    return fold(devanagari_words(text))


def number(n):
    return n.translate(DIGITS)


def word_form(word):
    return dev(word.replace(" ", ""))


GRAM_OVERRIDE = {
    "स्म": "अव्यय (निपात); ‘ह स्म’ कथन-शैली में, यहाँ लिट् ‘आह’ के साथ",
    "यथा-प्रोक्तम्": "पु. द्वितीया ए.व. (‘आयुर्वेदम्’ का विशेषण); "
                     "यथा + प्रोक्तम्, क्रियाविशेषण रूप में भी पढ़ा जा सकता है",
}


def chip_gram(word, form):
    if form in GRAM_OVERRIDE:
        return GRAM_OVERRIDE[form]
    text = gram_hi(word["gram"])
    if "क्त्वा/ल्यप्" in text:
        text = text.replace("क्त्वा/ल्यप्",
                            "ल्यप्" if form.endswith("्य") else "क्त्वा")
    return text


def split_long(rows, most=30):
    """The template allows at most 30 word chips per row: cut longer rows
    (long prose lines) into near-equal rows."""
    out = []
    for row in rows:
        k = -(-len(row) // most)
        size = -(-len(row) // k)
        out += [row[i:i + size] for i in range(0, len(row), size)]
    return out


def chip_rows(rows):
    rows = split_long(rows)
    return [[{"w": word_form(w["w"]), "gloss": fold(w["gloss"]),
              "gram": chip_gram(w, word_form(w["w"]))} for w in row]
            for row in rows]


def aid_items(n, unit, ch=1):
    """The memory aids of a card, in a fixed order."""
    chosen = dict(CHAPTERS[ch]["AI"].get(n, {}))
    if unit["type"] == "verse":
        parts = [split_pada(line) for line in unit["lines_deva"]]
        if all(parts):
            chosen["metre"] = {
                "text": "हर पंक्ति में ८ + ८ अक्षर (गिनती से)। ‘|’ पाद की "
                        "सीमा है; संधि के कारण वह शब्द के बीच भी पड़ सकती है।",
                "lines": [f"{a} | {b}" for a, b in parts]}
    items = []
    for kind in ORDER:
        if kind not in chosen:
            continue
        content = chosen[kind]
        item = {"aid": kind, "label": KIND_LABELS[kind]}
        if isinstance(content, str):
            item["text"] = content
        else:
            item.update(content)
        if (n, kind) in CHAPTERS[ch]["IM"]:
            name, alt = CHAPTERS[ch]["IM"][(n, kind)]
            item["image"] = {"src": "images/aids/" + name, "alt": alt}
        items.append(item)
    return items


def build(units, ch=1):
    st = CHAPTERS[ch]
    AUTHORED, NOTES_HI = st["A"], st["N"]
    unit_name, unit_title = f"Chapter {ch}", st["title"]
    concepts, questions = [], []
    previous = {}
    last_in_section = {}
    for unit in units:
        sec = section_of(unit["n"], ch)
        previous[unit["n"]] = last_in_section.get(sec)
        last_in_section[sec] = unit["n"]
    for unit in units:
        n = unit["n"]
        if n not in AUTHORED and os.environ.get("PARTIAL"):
            continue  # a batch under construction
        authored = AUTHORED[n]
        cid = cid_of(n, ch)
        section = section_of(n, ch)
        prev = previous[n]
        requires = authored.get("requires",
                                [cid_of(prev, ch)] if prev else [])
        digits = number(n)
        chd = number(str(ch))
        kind = "गद्य" if unit["type"] == "prose" else "श्लोक"
        rows = []
        if "lead_in_tokens" in unit:
            rows.append([w for t in unit["lead_in_tokens"]
                         for w in t["words"]])
        for line in unit["lines"]:
            rows.append([w for t in line["tokens"] for w in t["words"]])
        verse_lines = list(unit["lines_deva"])
        if unit["type"] == "verse":
            verse_lines[-1] += f" ॥ {digits} ॥"
        blocks = [
            {"key": "ref", "label": "संदर्भ",
             "text": (f"चरकसंहिता · सूत्रस्थान · अध्याय {chd} · {kind} {digits}। "
                      "पाठ: SARIT (एक ही स्रोत)। हिन्दी और English: "
                      "AI-रचित, AI-समीक्षित; विद्वान् से जाँच शेष।")},
            {"key": "verse", "label": "श्लोक" if kind == "श्लोक" else "मूल पाठ",
             "study": True, "lines": verse_lines},
            {"key": "words", "label": "पद-विच्छेद", "study": True, "words": chip_rows(rows)},
            {"key": "hindi", "label": "हिन्दी", "study": True, "text": unit["hindi"]},
            {"key": "english", "label": "English", "study": True,
             "text": fold(unit["english"])},
            {"key": "explain", "label": "व्याख्या", "study": True,
             "text": authored["explain_hi"]},
            {"key": "aids", "label": "स्मरण-सहायक", "study": True,
             "aids": aid_items(n, unit, ch)},
        ]
        blocks.append({"key": "note", "label": "पाठ-टिप्पणी", "text": NOTES_HI[n]})
        concept = {
            "id": cid, "unit": unit_name, "unitTitle": unit_title,
            "section": section,
            "title": f"{digits}. {authored['title']}",
            "requires": requires,
            "card": {"blocks": blocks, "rule": authored["rule"],
                     "limits": authored["limits"]},
            "question": authored["question"], "core": authored["core"],
        }
        concepts.append(concept)
        base = {"unit": unit_name, "unitTitle": unit_title,
                "section": section, "concept": cid}
        for question in authored["questions"]:
            q = dict(question)
            q = {k: v for k, v in q.items() if v is not None}
            q.update(base)
            q["id"] = f"{cid}-" + ("p" if q["role"] == "pretest"
                                   else f"r{q['rung']}")
            questions.append(q)
    return concepts, questions


def main():
    source, target = Path(sys.argv[1]), sys.argv[2]
    load_batches()
    concepts, questions = [], []
    for ch in CHAPTERS:
        data = source / f"sutrasthana{ch}_verses.json"
        if not data.exists():
            continue  # chapter not added yet
        units = json.load(open(data, encoding="utf8"))
        c, q = build(units, ch)
        concepts += c
        questions += q
    bank = {
        "id": "caraka-sutra", "book": "चरकसंहिता — सूत्रस्थान",
        "labels": {"unit": "Chapter", "units": "chapters", "topic": "Verse",
                   "whole": "Whole chapter"},
        "summary": ("The Charaka Samhita, Sūtrasthāna chapters 1 to 4: "
                    "how Āyurveda came down from Brahmā to the sages, the "
                    "drugs and gruels of the five cleansing treatments, "
                    "the pastes applied to the skin, and the fifty groups of ten drugs."),
        "genre": "चरकसंहिता", "scrollButtons": True,
        "unitSummaries": {
            "Chapter 1": (
                "How Āyurveda passed from Brahmā to Indra, why the sages "
                "gathered on the Himālaya, and who they were."),
            "Chapter 2": (
                "The drug groups for the five treatments, the twenty-eight "
                "gruels, and the physician who can use them."),
            "Chapter 3": (
                "The thirty-two medicinal pastes (pradeha) and the "
                "conditions of the skin and body they are used for."),
            "Chapter 4": (
                "The six hundred purgative formulas, the five kinds of "
                "preparation, and the fifty groups of ten drugs each.")},
        "concepts": concepts, "questions": questions}
    json.dump(bank, open(target, "w", encoding="utf8"), ensure_ascii=False,
              indent=1)
    print(len(concepts), "concepts,", len(questions), "questions")


if __name__ == "__main__":
    main()
