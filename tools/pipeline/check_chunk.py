#!/usr/bin/env python3
"""Check a drafted chunk against its input. usage: check_chunk.py in.json out.json"""
import json, re, sys, unicodedata
from difflib import SequenceMatcher

inp = json.load(open(sys.argv[1], encoding='utf8'))
out = json.load(open(sys.argv[2], encoding='utf8'))
nfc = lambda s: unicodedata.normalize('NFC', s)
errors, warnings = [], []

if [r['n'] for r in inp] != [r.get('n') for r in out]:
    errors.append('unit numbers differ: input %s.. output %s..' % ([r['n'] for r in inp][:3], [r.get('n') for r in out][:3]))

deva = re.compile(r'[ऀ-ॿ]')
latin = re.compile(r'[A-Za-z]')


def check_tokens(label, tokens, src_line):
    joined = ' '.join(nfc(t['src']) for t in tokens)
    if joined != nfc(src_line):
        errors.append('%s: tokens do not reproduce the input line.\n   input : %s\n   joined: %s' % (label, src_line, joined))
    for t in tokens:
        if not t.get('words'):
            errors.append('%s: token %r has no words' % (label, t.get('src')))
            continue
        flat = ''.join(w['w'].replace('-', '').replace(' ', '') for w in t['words'])
        for w in t['words']:
            if not w.get('w') or not w.get('gloss'):
                errors.append('%s: word missing w/gloss in token %r' % (label, t['src']))
            if not w.get('gram'):
                warnings.append('%s: no gram for %r' % (label, w.get('w')))
        a = re.sub(r"['\-\s]", '', nfc(t['src']))
        r = SequenceMatcher(None, a, flat).ratio()
        if r < 0.6:
            warnings.append('%s: split of %r -> %r looks very different (ratio %.2f)' % (label, t['src'], '+'.join(w['w'] for w in t['words']), r))


by_n = {r.get('n'): r for r in out}
for rec in inp:
    n = rec['n']
    o = by_n.get(n)
    if o is None:
        errors.append('unit %s missing in output' % n); continue
    if len(o.get('lines', [])) != len(rec['lines_iast']):
        errors.append('unit %s: %d lines in output, %d in input' % (n, len(o.get('lines', [])), len(rec['lines_iast'])))
    else:
        for i, (ln, src) in enumerate(zip(o['lines'], rec['lines_iast'])):
            check_tokens('unit %s line %d' % (n, i + 1), ln.get('tokens', []), src)
    if 'lead_in' in rec:
        if not o.get('lead_in_tokens'):
            errors.append('unit %s: lead_in_tokens missing' % n)
        else:
            check_tokens('unit %s lead_in' % n, o['lead_in_tokens'], rec['lead_in'])
        for k in ('lead_in_hindi', 'lead_in_english'):
            if not o.get(k):
                errors.append('unit %s: %s missing' % (n, k))
    h, e = o.get('hindi', ''), o.get('english', '')
    if not h or not deva.search(h):
        errors.append('unit %s: hindi missing or not Devanagari' % n)
    elif latin.search(h):
        errors.append('unit %s: Latin letters in hindi: %r' % (n, latin.findall(h)[:5]))
    if not e or deva.search(e):
        errors.append('unit %s: english missing or contains Devanagari' % n)
    if o.get('confidence') not in ('high', 'medium', 'low'):
        errors.append('unit %s: confidence must be high|medium|low' % n)
    for f in o.get('text_flags', []):
        if not (f.get('src') and f.get('suggest') and f.get('why')):
            errors.append('unit %s: malformed text_flag %r' % (n, f))
    # tool-flagged metre problems must be addressed (flag, or an explanation in notes)
    if any(x.startswith('metre') for x in rec.get('flags', [])) and not (o.get('text_flags') or o.get('notes')):
        warnings.append('unit %s: input has a metre flag but output has no text_flag/notes' % n)

print('ERRORS: %d   WARNINGS: %d   units: %d' % (len(errors), len(warnings), len(out)))
for x in errors:
    print('ERROR  ', x)
for x in warnings[:40]:
    print('WARNING', x)
if len(warnings) > 40:
    print('... %d more warnings' % (len(warnings) - 40))
sys.exit(1 if errors else 0)
