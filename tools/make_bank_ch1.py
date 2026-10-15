#!/usr/bin/env python3
"""Build questions.json for Caraka Su. 1, units 1-10.

    python3 tools/make_bank_ch1.py data/sutrasthana1_verses.json questions.json

Verse data (Sanskrit, word split, Hindi, English, notes) comes from the
verse file. Explanations, mnemonics, the card summary and every question
are written by hand in ch1_authored.py.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from indic_transliteration import sanscript as S  # noqa: E402
from ch1_authored import AUTHORED, NOTES_HI  # noqa: E402
from gram_hi import gram_hi  # noqa: E402
from ch1_aids import AIDS, IMAGES, KIND_LABELS, ORDER  # noqa: E402
from metre import split_pada  # noqa: E402

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
UNITS = 10


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


def chip_rows(rows):
    return [[{"w": word_form(w["w"]), "gloss": fold(w["gloss"]),
              "gram": chip_gram(w, word_form(w["w"]))} for w in row]
            for row in rows]


def aid_items(n, unit):
    """The memory aids of a card, in a fixed order."""
    chosen = dict(AIDS.get(n, {}))
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
        if (n, kind) in IMAGES:
            name, alt = IMAGES[(n, kind)]
            item["image"] = {"src": "images/aids/" + name, "alt": alt}
        items.append(item)
    return items


def build(units):
    concepts, questions = [], []
    for unit in units[:UNITS]:
        n = unit["n"]
        authored = AUTHORED[n]
        cid = f"su1-{int(n):03d}"
        digits = number(n)
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
            {"label": "संदर्भ",
             "text": (f"चरकसंहिता · सूत्रस्थान · अध्याय १ · {kind} {digits}। "
                      "पाठ: SARIT (एक ही स्रोत)। हिन्दी और English: "
                      "AI-रचित, AI-समीक्षित; विद्वान् से जाँच शेष।")},
            {"label": "श्लोक" if kind == "श्लोक" else "मूल पाठ",
             "study": True, "lines": verse_lines},
            {"label": "पद-विच्छेद", "study": True, "words": chip_rows(rows)},
            {"label": "हिन्दी", "study": True, "text": unit["hindi"]},
            {"label": "English", "study": True,
             "text": fold(unit["english"])},
            {"label": "व्याख्या", "study": True,
             "text": authored["explain_hi"]},
            {"label": "स्मरण-सहायक", "study": True,
             "aids": aid_items(n, unit)},
        ]
        blocks.append({"label": "पाठ-टिप्पणी", "text": NOTES_HI[n]})
        concept = {
            "id": cid, "unit": "Chapter 1", "unitTitle": "दीर्घञ्जीवितीय",
            "section": authored["section"],
            "title": f"{digits}. {authored['title']}",
            "requires": authored.get("requires", []),
            "card": {"blocks": blocks, "rule": authored["rule"],
                     "limits": authored["limits"]},
            "question": authored["question"], "core": authored["core"],
        }
        concepts.append(concept)
        base = {"unit": "Chapter 1", "unitTitle": "दीर्घञ्जीवितीय",
                "section": authored["section"], "concept": cid}
        for question in authored["questions"]:
            q = dict(question)
            q = {k: v for k, v in q.items() if v is not None}
            q.update(base)
            q["id"] = f"{cid}-" + ("p" if q["role"] == "pretest"
                                   else f"r{q['rung']}")
            questions.append(q)
    return concepts, questions


def main():
    source, target = sys.argv[1], sys.argv[2]
    units = json.load(open(source, encoding="utf8"))
    concepts, questions = build(units)
    bank = {
        "id": "caraka-su1", "book": "चरकसंहिता — सूत्रस्थान १",
        "labels": {"unit": "Chapter", "units": "chapters", "topic": "Verse",
                   "whole": "Whole chapter"},
        "summary": ("The opening of the Charaka Samhita, Sūtrasthāna 1: the "
                    "chapter's announcement, Bharadvāja's search for long "
                    "life, the line of Āyurveda from Brahmā to Indra, and "
                    "the sages who gathered on the Himālaya. Units 1 to 10."),
        "genre": "चरकसंहिता",
        "unitSummaries": {"Chapter 1": (
            "How Āyurveda passed from Brahmā to Indra, why the sages "
            "gathered on the Himālaya, and who they were.")},
        "concepts": concepts, "questions": questions}
    json.dump(bank, open(target, "w", encoding="utf8"), ensure_ascii=False,
              indent=1)
    print(len(concepts), "concepts,", len(questions), "questions")


if __name__ == "__main__":
    main()
