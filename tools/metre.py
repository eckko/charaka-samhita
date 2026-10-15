"""Count akṣaras of a Devanagari verse line and cut it into pādas."""
import re

CONS = re.compile("[\u0915-\u0939]")
MATRA = re.compile("[\u093e-\u094c\u0949\u094a\u0962\u0963]")
INDEP = re.compile("[\u0905-\u0914\u0960\u0961]")
VIRAMA = "्"
JOINERS = "ंःँ"
CROSS_WORD_JOINS = ("न्भ", "स्त")


def syllable_ends(line):
    """Indexes (exclusive) where each akṣara ends, in order."""
    ends = []
    i, n = 0, len(line)
    while i < n:
        c = line[i]
        if INDEP.match(c):
            j = i + 1
            while j < n and line[j] in JOINERS:
                j += 1
            ends.append(j)
            i = j
        elif CONS.match(c):
            j = i + 1
            # a conjunct: consonant + virama + consonant ...
            while j + 1 < n and line[j] == VIRAMA and CONS.match(line[j + 1]):
                j += 2
            if j < n and line[j] == VIRAMA:      # dead final consonant
                i = j + 1
                continue
            if j < n and MATRA.match(line[j]):
                j += 1
            while j < n and line[j] in JOINERS:
                j += 1
            ends.append(j)
            i = j
        else:
            i += 1
    return ends


def split_pada(line):
    """(first pāda, second pāda) when the line has 16 akṣaras, else None."""
    ends = syllable_ends(line)
    if len(ends) != 16:
        return None
    cut = ends[7]
    # A word-final consonant joined to the next word (अन्विच्छन्|भरद्वाज,
    # भरद्वाजस्|तस्मात्) stays with the pāda before. Only these joins are
    # known; a conjunct inside a word (ब्र in ब्रह्मचर्य) is never moved.
    if line[cut:cut + 3] in CROSS_WORD_JOINS:
        cut += 2
    return line[:cut].strip(), line[cut:].strip()


if __name__ == "__main__":
    import json
    for u in json.load(open("sutrasthana1_verses.json", encoding="utf8"))[2:10]:
        for l in u["lines_deva"]:
            print(len(syllable_ends(l)), split_pada(l))
