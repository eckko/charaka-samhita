#!/usr/bin/env python3
"""Build clean verse records for Carakasamhita Sutrasthana 1 from the SARIT TEI file.

Output: verses.json  (list of records, source order)
Nothing is silently corrected: marks are removed only where their meaning is certain
(avagraha written 'a -> '), everything else is kept and flagged.
"""
import json, re, sys
from xml.etree import ElementTree as ET
from indic_transliteration import sanscript

SRC = sys.argv[1]
OUT = sys.argv[2]
T = '{http://www.tei-c.org/ns/1.0}'
X = '{http://www.w3.org/XML/1998/namespace}id'

root = ET.parse(SRC).getroot()
body = root.find('.//' + T + 'body')
sthana1 = [d for d in body.iter(T + 'div') if d.get('type') == 'level1'][0]
CH = int(sys.argv[3]) if len(sys.argv) > 3 else 1
ch = [d for d in sthana1 if d.get('type') == 'level2'][CH - 1]


import unicodedata


def squash(s):
    # NFC so that decomposed diacritics (s + combining acute etc.) compare equal to precomposed ones
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', s)).strip()


def line_text(l):
    """text of a <l>/<p>, dropping <label>; <note> returned separately with the word before it"""
    out, notes = [], []

    def walk(e):
        if e.tag == T + 'label':
            return
        if e.tag == T + 'note':
            before = squash(''.join(out)).split(' ')[-1] if out else ''
            notes.append({'after': before, 'reading': squash(''.join(e.itertext()))})
            return
        if e.text:
            out.append(e.text)
        for c in e:
            walk(c)
            if c.tail:
                out.append(c.tail)

    walk(l)
    return squash(''.join(out)), notes


def clean(s):
    flags = []
    if '(' in s or ')' in s:
        flags.append('printed in parentheses in the edition (interpolated or alternative verse)')
        s = s.replace('(', '').replace(')', '')
    s = squash(s)
    s = re.sub(r'\s*/+\s*$', '', s)             # trailing danda(s)
    s = s.replace('//', '').replace(' / ', ' ')  # inner dandas
    s = re.sub(r"'a", "'", s)                   # avagraha written 'a  (e.g. 'sitah) -> '
    if '&' in s:
        flags.append('source has stray "&" before a word; removed, check word division')
        s = s.replace('&', '')
    if '+' in s:
        flags.append('source has "+" mark')
    s = squash(s)
    return s, flags


def devanagari(s):
    s = s.replace("'", "ऽ_")  # placeholder so the library does not choke
    d = sanscript.transliterate(s.replace('ऽ_', "'"), sanscript.IAST, sanscript.DEVANAGARI)
    return d.replace("'", 'ऽ')


# ---------------- metre: syllable count + weight ----------------
DIGRAPH = ['kh', 'gh', 'ch', 'jh', 'ṭh', 'ḍh', 'th', 'dh', 'ph', 'bh']
VOW = ['ai', 'au', 'ā', 'ī', 'ū', 'ṝ', 'ḹ', 'a', 'i', 'u', 'ṛ', 'ḷ', 'e', 'o']
LONG = {'ai', 'au', 'ā', 'ī', 'ū', 'ṝ', 'ḹ', 'e', 'o'}


def tokens(text):
    # tokenise word by word: a word-final vowel never forms a diphthong with the next word's first vowel
    toks = []
    for w in text.split():
        toks += _tokens_word(w)
    return toks


def _tokens_word(s):
    s = re.sub(r"[^a-zāīūṛṝḷḹṅñṭḍṇśṣḥṃ]", '', s.lower())
    i, toks = 0, []
    while i < len(s):
        for v in VOW:
            if s.startswith(v, i):
                toks.append(('V', v)); i += len(v); break
        else:
            for d in DIGRAPH:
                if s.startswith(d, i):
                    toks.append(('C', d)); i += 2; break
            else:
                c = s[i]
                toks.append(('M' if c in 'ṃḥ' else 'C', c)); i += 1
    return toks


def scan(s):
    t = tokens(s)
    out = []
    for idx, (k, v) in enumerate(t):
        if k != 'V':
            continue
        w = 'G' if v in LONG else 'L'
        j, cons = idx + 1, 0
        while j < len(t) and t[j][0] != 'V':
            if t[j][0] == 'M':
                w = 'G'
            else:
                cons += 1
            j += 1
        if cons >= 2:
            w = 'G'
        out.append(w)
    return ''.join(out)


records = []
for el in ch:
    tag = el.tag.replace(T, '')
    if tag == 'p' and el.get(X):
        txt, notes = line_text(el)
        txt, fl = clean(txt)
        nid = re.sub(r'(ab|cd)$', '', el.get(X)).replace('Ca.1.%d.' % CH, '')
        records.append({'n': nid, 'type': 'prose', 'lines_iast': [txt], 'notes': notes, 'flags': fl})
    elif tag == 'lg':
        ls = el.findall(T + 'l')
        ids = [l.get(X) for l in ls if l.get(X)]
        nid = re.sub(r'(ab|cd)$', '', ids[0]).replace('Ca.1.%d.' % CH, '')
        lines, notes, fl, lead = [], [], [], None
        for l in ls:
            txt, n = line_text(l)
            txt, f = clean(txt)
            if not txt:                      # empty <l/> placeholder in the source encoding
                continue
            if re.fullmatch(r'tatra \S*lok\S*( -+)?', txt):   # lead-in formula "tatra ślokāḥ", not a verse line
                lead = re.sub(r' -+$', '', txt)
                continue
            lines.append(txt); notes += n; fl += f
        rec = {'n': nid, 'type': 'verse', 'lines_iast': lines, 'notes': notes, 'flags': fl}
        if lead:
            rec['lead_in'] = lead
        rec['scan'] = [scan(x) for x in lines]
        rec['syllables'] = [len(x) for x in rec['scan']]
        # anushtubh half-line = 16 syllables (2 x 8)
        bad = [i + 1 for i, n in enumerate(rec['syllables']) if n != 16]
        if bad:
            rec['flags'].append('metre: line(s) %s do not have 16 syllables (counts %s): other metre or a possible typo'
                                % (bad, rec['syllables']))
        records.append(rec)

for r in records:
    r['lines_deva'] = [devanagari(x) for x in r['lines_iast']]

json.dump(records, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('records:', len(records),
      'prose:', sum(r['type'] == 'prose' for r in records),
      'verse:', sum(r['type'] == 'verse' for r in records),
      'flagged:', sum(bool(r['flags']) for r in records))
