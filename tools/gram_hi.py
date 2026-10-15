"""Hindi grammar labels for the word chips (the data uses English tags)."""
import re
import unicodedata
from indic_transliteration import sanscript as S

dev = lambda s: S.transliterate(unicodedata.normalize("NFC", s), S.IAST,
                                S.DEVANAGARI)
IAST = "āīūṛṝḷṅñṭḍṇśṣṃḥĀĪŪṚŚṢ"
PHRASES = [
    ("pres. part.", "शतृ"), ("title adj. from", "नाम-विशेषण, इससे बना:"),
    ("(abl. of tad)", "(तद् का पञ्चमी)"),
    ("avyayībhāva-type adv. +", "अव्ययीभाव-सदृश क्रि.वि. +"),
    ("with present gives past", "वर्तमान के साथ भूतार्थ"),
    ("emphatic", "बलवाचक"), ("tat-puruṣa", "तत्पुरुष"),
]
WORDS = {
    "m.": "पु.", "f.": "स्त्री.", "n.": "नपुं.",
    "nom.": "प्रथमा", "acc.": "द्वितीया", "inst.": "तृतीया",
    "dat.": "चतुर्थी", "abl.": "पञ्चमी", "gen.": "षष्ठी", "loc.": "सप्तमी",
    "sg.": "ए.व.", "du.": "द्वि.व.", "pl.": "ब.व.",
    "ind.": "अव्यय", "abs.": "क्त्वा/ल्यप्", "ppp": "क्त",
    "aor.": "लुङ्", "pf.": "लिट्", "fut.": "लृट्", "mid.": "आत्मने.",
    "adv.": "क्रि.वि.", "adj.": "विशेषण",
}
PERSON = {"1": "उ.पु.", "2": "म.पु.", "3": "प्र.पु."}


def gram_hi(text):
    g = unicodedata.normalize("NFC", text)
    g = re.sub(r"(?<![\w])[‘'’“\"]([^'’”\"]{2,40}?)[’'’”\"](?![\w])",
               lambda m: "‘" + dev(m.group(1)) + "’", g)
    for old, new in PHRASES:
        g = g.replace(old, new)
    g = re.sub(r"\b([123]) ", lambda m: PERSON[m.group(1)] + " ", g)

    def piece(m):
        c = m.group(0)
        if c in WORDS:
            return WORDS[c]
        if "√" in c:
            return "√".join(dev(p) if p else "" for p in c.split("√"))
        if set(c) & set(IAST) or c.strip("-") in (
                "dvandva", "dvigu", "bahuvrīhi", "karmadhāraya", "aluk",
                "upapada", "anuloma", "itaretara"):
            return dev(c)
        return c
    g = re.sub(r"[A-Za-zāīūṛṝḷṅñṭḍṇśṣṃḥĀĪŪṚŚṢ√\-]+\.?", piece, g)
    return unicodedata.normalize("NFC", g)


if __name__ == "__main__":
    import json
    seen = set()
    for u in json.load(open("sutrasthana1_verses.json", encoding="utf8"))[:10]:
        for l in u["lines"]:
            for t in l["tokens"]:
                for w in t["words"]:
                    if w["gram"] not in seen:
                        seen.add(w["gram"])
                        out = gram_hi(w["gram"])
                        flag = " <<LATIN" if re.search("[A-Za-z]", out) else ""
                        print(w["gram"], "=>", out, flag)
