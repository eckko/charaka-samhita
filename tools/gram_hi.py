"""Hindi grammar labels for the word chips (the data uses English tags)."""
import re
import unicodedata
from indic_transliteration import sanscript as S

dev = lambda s: S.transliterate(unicodedata.normalize("NFC", s), S.IAST,
                                S.DEVANAGARI)
IAST = "āīūṛṝḷṅñṭḍṇśṣṃḥĀĪŪṚŚṢ"
PHRASES = [
    ("pres. pass. part.", "कर्मवाच्य शानच्"),
    ("past act. part.", "क्तवतु"), ("agent noun", "कर्तृवाचक संज्ञा"),
    ("periphr. pf.", "आम्-लिट्"), ("pres. part.", "शतृ"), ("title adj. from", "नाम-विशेषण, इससे बना:"),
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
    "ppp.": "क्त", "pass.": "कर्मवाच्य", "opt.": "विधिलिङ्", "pp.": "क्त",
    "rel.": "सम्बन्धवाचक", "pron.": "सर्वनाम", "caus.": "णिजन्त",
    "part.": "कृदन्त", "impf.": "लङ्", "gerundive": "कृत्य",
    "inf.": "तुमुन्", "impv.": "लोट्", "superl.": "अतिशयार्थ",
    "num.": "संख्यावाचक", "adverbial": "क्रियाविशेषण",
    "interr.": "प्रश्नवाचक", "encl.": "अनुदात्त रूप", "desid.": "सन्नन्त",
    "denom.": "नामधातु", "collective": "समाहार", "indef.": "अनिश्चयवाचक",
    "voc.": "सम्बोधन", "pres.": "लट्", "act.": "कर्तृवाच्य",
}
WORDS.update({"tad": "तद्", "idam": "इदम्", "payas": "पयस्", "tvac": "त्वच्"})
GRAM_EXACT = {
    "m. acc. sg.; upapada tat-puruṣa (-ga 'being in')": "पु. द्वितीया ए.व.; उपपद तत्पुरुष (-ग = ‘में स्थित’)",
    "m. acc. sg. (with āyurvedam); dvandva in tat-puruṣa / bahuvrīhi": "पु. द्वितीया ए.व. (‘आयुर्वेदम्’ के साथ); तत्पुरुष के भीतर द्वन्द्व / बहुव्रीहि",
    "m. acc. sg.; dvandva in tat-puruṣa / bahuvrīhi": "पु. द्वितीया ए.व.; तत्पुरुष के भीतर द्वन्द्व / बहुव्रीहि",
    "loc. sg. of div": "सप्तमी ए.व. (दिव् का)",
    "m. nom. sg.; dvandva within tat-puruṣa": "पु. प्रथमा ए.व.; तत्पुरुष के भीतर द्वन्द्व",
    "ind.; dvigu + -vat": "अव्यय; द्विगु + -वत्",
    "n. inst. pl.; bahuvrīhi with dvandva": "नपुं. तृतीया ब.व.; द्वन्द्व सहित बहुव्रीहि",
    "m. nom. pl.; dvandva (qualifying guṇāḥ)": "पु. प्रथमा ब.व.; द्वन्द्व (‘गुणाः’ का विशेषण)",
    "n. inst. pl.; tat-puruṣa with dvandva": "नपुं. तृतीया ब.व.; द्वन्द्व सहित तत्पुरुष",
    "f. nom. sg.; tat-puruṣa (with viṃśatiḥ)": "स्त्री. प्रथमा ए.व.; तत्पुरुष (‘विंशतिः’ के साथ)",
    "n. nom. sg. (fruit; stem usu. f.)": "नपुं. प्रथमा ए.व. (फल; मूल शब्द प्रायः स्त्रीलिंग)",
    "dvandva + artham (ind. 'for the sake of')": "द्वन्द्व + अर्थम् (अव्यय ‘के लिए’)",
    "ind. (-tas) from yoga": "अव्यय (-तस्, योग से)",
    "m. nom. pl., tat-puruṣa (bala-upacaya dvandva)": "पु. प्रथमा ब.व., तत्पुरुष (बल-उपचय द्वन्द्व)",
    "m. nom. pl., tat-puruṣa (dvandva + apaha)": "पु. प्रथमा ब.व., तत्पुरुष (द्वन्द्व + अपह)",
    "n. nom. sg. (a- + rūkṣa)": "नपुं. प्रथमा ए.व. (अ- + रूक्ष)",
    "n. nom. sg., upapada tat-puruṣa (dvandva first)": "नपुं. प्रथमा ए.व., उपपद तत्पुरुष (पहले द्वन्द्व)",
    "gen. pl., dvandva of tat-puruṣas": "षष्ठी ब.व., तत्पुरुषों का द्वन्द्व",
    "n. nom. sg., tat-puruṣa (dvandva first)": "नपुं. प्रथमा ए.व., तत्पुरुष (पहले द्वन्द्व)",
    "avyayībhāva + -tas": "अव्ययीभाव + -तस्",
    "3 pl. fut. √vac (passive sense)": "प्र.पु. ब.व. लृट् √वच् (कर्मवाच्य अर्थ)",
    "m. loc. pl., tat-puruṣa (dvandva first)": "पु. सप्तमी ब.व., तत्पुरुष (पहले द्वन्द्व)",
    "ind. (-tas)": "अव्यय (-तस्)",
    "m./n. inst. pl. of phalamūlin (dvandva phala-mūla + poss. -in)": "पु./नपुं. तृतीया ब.व. (फलमूलिन् का; द्वन्द्व फल-मूल + -इन्)",
    "f. nom. sg.; name (bahuvrīhi)": "स्त्री. प्रथमा ए.व.; नाम (बहुव्रीहि)",
    "saṃkhyā-pūrva karmadhāraya (or ṣaṭ + vṛkṣān), m. acc. pl.": "संख्यापूर्व कर्मधारय (या षट् + वृक्षान्), पु. द्वितीया ब.व.",
    "m. acc. sg. (repeated: distributive)": "पु. द्वितीया ए.व. (दोहराव: वीप्सा)",
    "abl. sg. as ind.": "पञ्चमी ए.व., अव्यय की तरह",
    "tat-puruṣa (with dvandva), m. inst. sg.": "तत्पुरुष (द्वन्द्व सहित), पु. तृतीया ए.व.",
    "neg. abs. a-vi-√jñā": "नञ्-समास, ल्यप् (अ-वि-√ज्ञा)",
    "tat-puruṣa, n. nom. sg. (āśīviṣa: bahuvrīhi 'poison-fanged', snake)": "तत्पुरुष, नपुं. प्रथमा ए.व. (आशीविष: बहुव्रीहि ‘विष-दन्त वाला’, साँप)",
    "superl. (-tama), m. acc. sg.": "अतिशयार्थ (-तम), पु. द्वितीया ए.व.",
    "bahuvrīhi, m. nom. pl. (tvac)": "बहुव्रीहि, पु. प्रथमा ब.व. (त्वच्)",
}
PERSON = {"1": "उ.पु.", "2": "म.पु.", "3": "प्र.पु."}


def gram_hi(text):
    if text in GRAM_EXACT:
        return GRAM_EXACT[text]
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
