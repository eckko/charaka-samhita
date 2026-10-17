#!/usr/bin/env python3
"""Stage 3: SARIT IAST (with the e-text's own markers) -> Devanagari.

convert_line(text) -> (devanagari, flags). Only documented rewrites are
done; whatever cannot be decided is kept and reported in `flags`
(kind, detail) so it lands in ISSUES.md. The untouched IAST stays in
raw/iast/ and raw/carakasamhita.xml.

SARIT's own header says: initial vowel elision for avagraha is reversed
and marked with ', external sandhi is undone and marked with +, the
ampersand anchors an editorial footnote, and text division follows the
Devanagari print. Rules:
 1. Editor's insertions typed into the line (footnote readings such as
    `...' iti pā-., {braces}, [&'...' pā+], (=Sū.sū.45.142cd)) are not the
    root text: left out and reported as variants.
 2. "&" anchors are removed (their count is reported).
 3. Sandhi markers go back to the printed form: o/e + a -> ऽ ; ā + a -> ā ;
    ā + ā -> ā ; a + a -> ā. Other combinations are kept and reported.
 4. Remaining apostrophes are quotation marks (‘ ’); a backtick opens one.
 5. "/" -> "।", "//" -> "॥"; the chapter number between slashes in a
    colophon ("//2//") is dropped; other digits become Devanagari digits.
 6. Y -> ṝ (SARIT's ASCII spelling in pitṝn, nṝṇām, duhitṝr); the one
    capital O (hetuyuktijO jitātmā, a typo for o) is read as o and reported.
 7. IAST letters -> Devanagari (indic_transliteration), NFC.
"""
import re
import unicodedata

from indic_transliteration import sanscript

LETTER = "A-Za-zāīūṛṝḷṅñṭḍṇśṣṃḥ"
DIGITS = str.maketrans("0123456789", "०१२३४५६७८९")

FOOTNOTE_RES = [
    (re.compile(r"&?\s*`[^`']*'(?:\s*iti)?\s*(?:,\s*)?(?:pā[-+]?\.?)?"),
     "footnote typed into the line"),
    (re.compile(r"&?\{[^}]*\}"), "variant in braces"),
    (re.compile(r"\[&?'[^\]]*\]"), "footnote in brackets"),
    (re.compile(r"\(=[^)]*\)"), "editor's cross reference"),
]
PLUS_RE = re.compile("([" + LETTER + r"])(\++)([" + LETTER + "])")


def resolve_plus(match, flags):
    """One X+Y sandhi marker. Y is the restored vowel (a marker)."""
    left, pluses, right = match.groups()
    if right == "a" and left in "oe":
        return left + "ऽ\x00"          # \x00 stands for the dropped a
    if right == "a" and left == "ā":
        return left + "\x00"
    if right == "ā" and left == "ā":
        return left + "\x00"
    if right == "a" and left == "a":
        return "ā\x00"
    flags.append(("other", f"'+' sandhi marker not resolved: "
                  f"{left}{pluses}{right}"))
    return left + right


def fix_apostrophes(s, flags):
    out = []
    i, n = 0, len(s)
    while i < n:
        if s[i] != "'":
            out.append(s[i])
            i += 1
            continue
        j = len(out) - 1
        spaced = j >= 0 and out[j] == " "
        if spaced:
            j -= 1
        prev = out[j] if j >= 0 else ""
        nxt = s[i + 1] if i + 1 < n else ""
        word_follows = bool(re.match("[" + LETTER + "]", nxt))
        closes_later = "'" in s[i + 1:]
        # a quotation mark spaced from the previous word and closed later
        # on the line is a quote, not an avagraha
        looks_like_quote = spaced and closes_later and nxt != "a"
        if word_follows and not looks_like_quote:
            if prev in ("o", "e"):
                del out[j + 1:]
                out.append("ऽ")
                if nxt == "a":
                    i += 1          # the restored a is not printed
                else:
                    flags.append(("other", "avagraha without a restored a: "
                                  + s[max(0, i - 14):i + 10]))
                i += 1
                continue
            if prev == "ā":
                del out[j + 1:]
                i += 2 if nxt == "a" else 1
                continue
            if prev == "a" and spaced and nxt == "a":
                del out[j:]
                out.append("ā")
                flags.append(("other", "a + 'a joined as ā (sandhi restored "
                              "to the printed form): " + s[max(0, i - 14):i + 10]))
                i += 2
                continue
            if prev == "ḥ" and spaced and nxt == "a":
                flags.append(("other", "avagraha after a visarga; sandhi "
                              "not restored: " + s[max(0, i - 14):i + 10]))
                out.append("ऽ")
                i += 2
                continue
        opening = (not out) or out[-1] in " (-‘`" or prev in ("", "-", "(")
        out.append("‘" if (opening and word_follows) else "’")
        i += 1
    return "".join(out)


def convert_line(text):
    flags = []
    s = text
    for pattern, label in FOOTNOTE_RES:
        def cut(match, label=label):
            flags.append(("variant", f"{label}, left out of the text: "
                          f"{match.group(0).strip()}"))
            return ""
        s = pattern.sub(cut, s)
    anchors = s.count("&")
    s = s.replace("&", "")
    s = PLUS_RE.sub(lambda m: resolve_plus(m, flags), s)
    s = s.replace("\x00", "")
    s = fix_apostrophes(s, flags)
    s = s.replace("`", "‘")
    s = re.sub(r"/\s*/?\s*\d+\s*/\s*/?", "//", s)
    s = re.sub(r"//+", "॥", s)
    s = s.replace("/", "।")
    s = s.translate(DIGITS)
    if "Y" in s:
        flags.append(("possible-typo", "capital Y in the source (ASCII "
                      "spelling of ṝ, e.g. pitYn); read as ṝ"))
        s = s.replace("Y", "ṝ")
    if "O" in s:
        flags.append(("possible-typo", "capital O in the source "
                      "(hetuyuktijO jitātmā); read as o"))
        s = s.replace("O", "o")
    if re.search("[" + "A-Z" + "]", s):
        flags.append(("possible-typo", "capital letter left in the source"))
    s = re.sub("[" + LETTER + "]+",
               lambda m: sanscript.transliterate(
                   m.group(0), sanscript.IAST, sanscript.DEVANAGARI), s)
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s, flags, anchors


if __name__ == "__main__":
    import sys
    for line in sys.argv[1:]:
        print(convert_line(line))
