#!/usr/bin/env python3
"""Build a mock questions.json for Caraka Su.1 from sutrasthana1_verses.json."""
import json, random, re, sys, unicodedata
from indic_transliteration import sanscript as S

DATA = json.load(open('sutrasthana1_verses.json', encoding='utf8'))
dev = lambda s: S.transliterate(unicodedata.normalize('NFC', s), S.IAST, S.DEVANAGARI)
DIG = str.maketrans('0123456789.', '०१२३४५६७८९.')
MAP = {'ṛ': 'ri', 'ṝ': 'ri', 'ś': 'sh', 'Ś': 'Sh', 'ṣ': 'sh', 'Ṣ': 'Sh',
       'ṃ': 'm', 'ḥ': 'h', 'ṅ': 'n', 'ñ': 'n', 'ṭ': 't', 'ḍ': 'd', 'ṇ': 'n',
       'ḷ': 'l'}
def fold_char(c):
    if '\u0900' <= c <= '\u097f': return c
    c = MAP.get(c, c)
    return ''.join(x for x in unicodedata.normalize('NFKD', c) if not unicodedata.combining(x))
def fold(s):
    return ''.join(fold_char(c) for c in unicodedata.normalize('NFC', s))
IASTCH = set('āīūṛṝḷṅñṭḍṇśṣṃḥĀĪŪṚŚṢ')
WORDRE = re.compile(r"[A-Za-zāīūṛṝḷṅñṭḍṇśṣṃḥĀĪŪṚŚṢ\-]+")
SKT = {'dvandva', 'dvigu', 'upapada', 'aluk', 'anuloma', 'itaretara'}
QUOTE = re.compile(r"(?<![\w])[‘'’“\"]([A-Za-zāīūṛṝḷṅñṭḍṇśṣṃḥ\- ]{1,40}?)[’'’”\"](?![\w])")
def dev_words(t):
    return WORDRE.sub(lambda m: dev(m.group()) if (set(m.group()) & IASTCH) else m.group(), t)
def clean_note(t):
    t = QUOTE.sub(lambda m: '‘' + dev(m.group(1)) + '’' if len(m.group(1)) > 1 else m.group(0), unicodedata.normalize('NFC', t))
    return fold(dev_words(t))
def gram_dev(g):
    g = QUOTE.sub(lambda m: '‘' + dev(m.group(1)) + '’', unicodedata.normalize('NFC', g))
    def chunk(m):
        c = m.group(0)
        if '√' in c:
            return '√'.join(dev(p) if p else '' for p in c.split('√'))
        if set(c) & IASTCH or c.strip('-') in SKT:
            return dev(c)
        return c
    g = re.sub(r"[A-Za-zāīūṛṝḷṅñṭḍṇśṣṃḥĀĪŪṚŚṢ√\-]+", chunk, g)
    return fold(g)
def dword(w): return dev(w.replace(' ', ''))   # keeps hyphens

rng = random.Random(7)
concepts, questions = [], []
allwords = []     # (unit index, dev word, gloss, gram)
units = []
for u in DATA:
    rows = []
    srcs = u['lines']
    if 'lead_in_tokens' in u:
        rows.append([w for t in u['lead_in_tokens'] for w in t['words']])
    for l in u['lines']:
        rows.append([w for t in l['tokens'] for w in t['words']])
    units.append((u, rows))
for i, (u, rows) in enumerate(units):
    for r in rows:
        for w in r:
            allwords.append((i, dword(w['w']), fold(w['gloss']), fold(w['gram'] if False else w['gram']), w['gram']))

def num(n): return n.translate(DIG)

SECT = {}
def section(idx, n):
    if n in ('1', '2'): return 'प्रस्तावना'
    v = int(float(n)); lo = ((v - 3) // 10) * 10 + 3; hi = min(lo + 9, 139)
    return f'श्लोक {num(str(lo))}–{num(str(hi))}'

def content_words(rows):
    seen, out = set(), []
    for r in rows:
        for w in r:
            g = fold(w['gloss']); d = dword(w['w'])
            if w['gram'].strip() in ('ind.', '') or g in seen or d in seen or len(g) < 3 or '-' in d and False: continue
            if re.search(r'[A-Za-z]', d): continue
            seen.add(g); seen.add(d); out.append((d, g, w['gram']))
    return out

def mc(options, correct):
    opts = options[:]; rng.shuffle(opts); return opts, opts.index(correct)

for i, (u, rows) in enumerate(units):
    n = u['n']; nd = num(n)
    cid = 'su1-' + n.replace('.', '-').rjust(3 if '.' not in n else 3, '0') if False else 'su1-' + ('p' + n if n in ('1','2') else n.replace('.', '-').zfill(3 if '.' not in n else 5))
    first = u['lines_deva'][0].split()
    sec = section(i, n)
    unit, utitle = 'Chapter 1', 'दीर्घञ्जीवितीय'
    english = fold(u['english']); hindi = u['hindi']
    vl = list(u['lines_deva'])
    if u['type'] == 'verse': vl[-1] += f' ॥ {nd} ॥'
    study_lines = ([('तत्र श्लोकाः')] if 'lead_in_tokens' in u else []) + vl
    blocks = [
      {'label': 'संदर्भ', 'text': f"चरकसंहिता, सूत्रस्थान, अध्याय १ — {'गद्य' if u['type']=='prose' else 'श्लोक'} {nd}। पाठ: SARIT संस्करण।"},
      {'label': 'श्लोक' if u['type']=='verse' else 'मूल पाठ', 'study': True, 'lines': study_lines},
      {'label': 'पद-विच्छेद', 'study': True,
       'words': [[{'w': dword(w['w']), 'gloss': fold(w['gloss']), 'gram': gram_dev(w['gram'])} for w in r] for r in rows]},
      {'label': 'हिन्दी', 'study': True, 'text': hindi},
      {'label': 'English', 'study': True, 'text': english}]
    note_bits = []
    for f in u.get('text_flags', []):
        note_bits.append(f"‘{dev(f['src'])}’ → ‘{dev(f['suggest'])}’: {clean_note(f['why'])}")
    if u.get('notes'): note_bits.append(clean_note(u['notes']))
    for v in u.get('variants', []):
        note_bits.append(f"पाठभेद ({dev(v['after'])} के बाद): {dev(v['reading'])}")
    if u['confidence'] != 'high': note_bits.insert(0, 'Medium confidence: split or sense is less certain.')
    if note_bits: blocks.append({'label': 'पाठ-टिप्पणी', 'text': ' '.join(note_bits)})
    if n == '3':
        blocks.append({'label': 'स्मरण-सूत्र', 'study': True, 'text': 'दीर्घ जीवन → भरद्वाज → इन्द्र की शरण। “कौन किसके पास, और क्यों”: आयुर्वेद की शुरुआत एक शिष्य की दीर्घ आयु की खोज से होती है।'})
    concepts.append({
      'id': cid, 'unit': unit, 'unitTitle': utitle, 'section': sec,
      'title': f"{'गद्य' if u['type']=='prose' else 'श्लोक'} {nd}: {' '.join(first[:2])}",
      'requires': [concepts[-1]['id']] if concepts and False else [],
      'card': {'blocks': blocks, 'rule': english,
               'limits': 'This is a translation of the Sanskrit above; where the English and the word split disagree, trust the Sanskrit words.'},
      'question': 'What does this verse say, word by word?' if u['type']=='verse' else 'What does this line say, word by word?',
      'core': i % 4 == 0})
    base = dict(unit=unit, unitTitle=utitle, section=sec, concept=cid)
    cw = content_words(rows)
    if len(cw) < 2:
        cw = cw + [(dword(w['w']), fold(w['gloss']), w['gram']) for r in rows for w in r][:2]
    others = [(d, g) for (j, d, g, _, _) in allwords if j != i and re.search(r'[A-Za-z]', g)]
    pool = [x for x in others if x[1] not in {c[1] for c in cw}]
    def distract(correct_g, k=3):
        out, seen = [], {correct_g}
        for d, g in rng.sample(pool, len(pool)):
            if g not in seen: seen.add(g); out.append((d, g))
            if len(out) == k: break
        return out
    # rung 0 pretest
    d0, g0, gr0 = cw[0]
    ds = distract(g0)
    opts, a = mc([g0] + [g for _, g in ds], g0)
    ex = [f"Right: {d0} means '{g0}' in this verse." if o == g0 else f"'{o}' translates {dict((g, d) for d, g in ds)[o]}, a word of another verse, not {d0}." for o in opts]
    questions.append({**base, 'id': cid + '-p', 'role': 'pretest', 'rung': 0, 'kind': 'mcq',
      'q': f"One word in this verse is {d0}. Which meaning do you expect?",
      'options': opts, 'answer': a, 'optionExplain': ex,
      'explain': f"{d0} means '{g0}' here. The next card shows the whole verse and where this word sits in it.",
      'rule': f"{d0} = {g0}."})
    # rung 1 warmup match
    pairs = [[d, g] for d, g, _ in cw[:4]]
    questions.append({**base, 'id': cid + '-r1', 'role': 'warmup', 'rung': 1, 'kind': 'match',
      'q': 'Match each word of the verse to its meaning.', 'pairs': pairs,
      'explain': 'These are the words as the word split above gives them, with sandhi undone.',
      'rule': '; '.join(f"{d} = {g}" for d, g in pairs[:2]) + '.'})
    # rung 2 extend fill
    d2, g2, gr2 = cw[1] if len(cw) > 1 else cw[0]
    acc = [d2, d2.replace('-', ''), d2.replace('-', ' ')]
    questions.append({**base, 'id': cid + '-r2', 'role': 'extend', 'rung': 2, 'kind': 'fill',
      'q': f"In this verse the word for '{g2}' is ____ (type it in Devanagari).", 'accept': list(dict.fromkeys(acc)),
      'explain': f"The verse has {d2} for '{g2}'; its grammar is {gram_dev(gr2)}.",
      'teaches': f"{d2} is {gram_dev(gr2)}: its ending shows its role in the sentence.",
      'rule': f"{d2} = {g2}."})
    # rung 3 discriminate: sandhi split
    tok = None
    for l in u['lines']:
        for t in l['tokens']:
            if len(t['words']) > 1: tok = t; break
        if tok: break
    if tok:
        ws = [dword(w['w']) for w in tok['words']]
        right = ' + '.join(ws)
        cands = [right, ' + '.join(reversed(ws)),
                 ' + '.join(ws[:-1] + [rng.choice(pool)[0]]),
                 ' + '.join(ws[1:]) if len(ws) > 2 else ' + '.join([rng.choice(pool)[0]] + ws[1:])]
        cands = list(dict.fromkeys(cands))
        while len(cands) < 4: cands.append(' + '.join([rng.choice(pool)[0]] + ws[1:]))
        opts, a = mc(cands[:4], right)
        ex = ['Right: this split restores each word in order.' if o == right else 'This changes the words or their order, so it does not rebuild the written form.' for o in opts]
        questions.append({**base, 'id': cid + '-r3', 'role': 'discriminate', 'rung': 3, 'kind': 'mcq',
          'q': f"Which is the correct split (sandhi viccheda) of {dev(tok['src'])}?", 'options': opts, 'answer': a,
          'optionExplain': ex, 'explain': f"{dev(tok['src'])} splits as {right}.", 'rule': f"{dev(tok['src'])} = {right}."})
    else:
        d3, g3, _ = cw[0]
        ds = distract(g3); opts, a = mc([d3] + [d for d, _ in ds], d3)
        ex = [f"Right: {o} is '{g3}'." if o == d3 else f"{o} is a different word." for o in opts]
        questions.append({**base, 'id': cid + '-r3', 'role': 'discriminate', 'rung': 3, 'kind': 'mcq',
          'q': f"Which of these words means '{g3}'?", 'options': opts, 'answer': a, 'optionExplain': ex,
          'explain': f"{d3} means '{g3}'.", 'rule': f"{d3} = {g3}."})
    # rung 4 apply: translation
    wrong = rng.sample([fold(x['english']) for x in DATA if x['n'] != n and len(x['english']) < 260], 3)
    opts, a = mc([english] + wrong, english)
    ex = ['Right: it matches the words of the verse.' if o == english else 'This is the sense of another verse of the chapter.' for o in opts]
    questions.append({**base, 'id': cid + '-r4', 'role': 'apply', 'rung': 4, 'kind': 'mcq',
      'q': 'Which statement does this verse make?' if u['type']=='verse' else 'Which statement does this line make?',
      'options': opts, 'answer': a, 'optionExplain': ex, 'explain': english, 'rule': english})
    # rung 5 transfer: word from earlier unit
    j, dj, gj, _, grj = rng.choice([x for x in allwords if x[0] != i and re.search(r'[A-Za-z]', x[2]) and x[4].strip() not in ('ind.', '')])
    ds = distract(gj); opts, a = mc([gj] + [g for _, g in ds], gj)
    ex = [f"Right: {dj} is '{gj}'." if o == gj else f"'{o}' belongs to a different word." for o in opts]
    questions.append({**base, 'id': cid + '-r5', 'role': 'transfer', 'rung': 5, 'kind': 'mcq',
      'q': f"The word {dj} comes from another verse of this chapter. What does it mean?", 'options': opts, 'answer': a,
      'optionExplain': ex, 'explain': f"{dj} means '{gj}' and is {gram_dev(grj)}.",
      'teaches': f"{dj} is {gram_dev(grj)}, and means '{gj}'.", 'rule': f"{dj} = {gj}."})

bank = {'id': 'caraka-su1', 'book': 'चरकसंहिता — सूत्रस्थान १',
  'labels': {'unit': 'Chapter', 'units': 'chapters', 'topic': 'Verse', 'whole': 'Whole chapter'},
  'summary': 'Mock-up: the first chapter of the Charaka Samhita, verse by verse.',
  'genre': 'चरकसंहिता', 'concepts': concepts, 'questions': questions}
bank['unitSummaries'] = {'Chapter 1': 'How the science of life came down from Indra to the sages, and what the first chapter sets out.'}
json.dump(bank, open(sys.argv[1], 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(concepts), 'concepts', len(questions), 'questions')
