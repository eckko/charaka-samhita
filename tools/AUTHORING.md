# Authoring guide: Charaka Samhita Su. 1, batch of ~10 units

Directory (all your work happens here):
`/tmp/claude-0/-home-claude/0cac1b21-6382-56bd-abe4-a207ecd1a4f6/scratchpad/ch1/`
Read `ch1_authored.py` (units 1-10: the helpers `mcq match order fill multi`
and ten finished examples) and `ch1_aids.py` (aids + KIND_LABELS + ORDER)
first. Match their quality, voice and structure exactly. Look at 3-4 finished
units (3, 5, 9, 10) in full before writing.

## Deliverable
Create ONE file `batch_NN.py` (NN given in your task) that starts with
`from ch1_authored import mcq, match, order, fill, multi` and defines:
- `AUTHORED = {"11": {...}, ...}` keys are unit numbers as STRINGS
  (as in `data n`, e.g. "66.1"). Fields: title (Devanagari, the verse's
  opening words or a short topic), question (English, one line),
  rule (English, <=40 words), limits (English: what the verse does NOT say /
  where the reading is uncertain), explain_hi (Hindi, 3-6 sentences),
  hook (Hindi one-liner), core (True/False; ~1 in 3 units True: key
  teaching verses), optional requires (list of concept ids like "su1-014";
  OMIT it unless a real earlier dependency exists; the generator defaults to
  the previous unit of the same section), questions (list of 6).
  Do NOT write "section": it comes from `sections.py`.
- `NOTES_HI = {"11": "..."}` Hindi, hand-written textual note per unit:
  sandhi joins you checked, variants listed in the unit's `variants`/`notes`
  data, readings that could go two ways, `text_flags`. If the data has
  nothing to flag, give a short honest note on a grammatical point (never
  empty, never invented variants).
- `AIDS = {"11": {kind: content}}` memory aids, only kinds that REALLY help
  that verse (typically 3-6 kinds, never all 13). Kinds: frame chain diagram
  letters seesaw story pegs puns anchors sandhi contrast chunks (metre is
  automatic; do not write it). Content: a Hindi string, or
  {"steps":[2-8 strings]}, or {"groups":[{"label":..,"items":[<=12]}]}.
  Rules: one per kind per unit; "diagram" groups must reproduce the verse's
  own words in verse order; pegs/puns are YOUR memory hooks, say so in the
  text ("मेरा बनाया चित्र"/"केवल सुनने की सहायता"), never as claims about the
  verse; seesaw = a pair of opposites in the verse (यदा/तदा, X ↔ Y).
- `IMAGE_SPECS = {("11","diagram"): {...}}` optional, at most ~1 picture per
  3 units, only where a picture truly helps (a list/sequence of items, a
  pair of opposites, a table). Spec keys: file (unique "name.svg"), alt
  (English, accurate, mentions counts/items), type, and:
  - type "chain": title, steps [..]  (vertical boxes with arrows)
  - type "table": title, heads [a,b], rows [[a,b],..]
  - type "split": title, cols [[head, [items]],[head,[items]]]
  - type "mountain": title, top [..], bottom [..]
  The (unit, kind) must exist in that unit's AIDS (kind is one of
  diagram/pegs/seesaw/chain/contrast). Text in the picture must be
  Devanagari/Hindi, short (<=34 chars per item), and the same content as the
  aid text.

## Questions (exactly 6 per unit, rungs 0..5)
Order and roles: pretest(rung 0), warmup(1), extend(2), discriminate(3),
apply(4), transfer(5), same as units 1-10 (see them). Use >=3 distinct
kinds per unit across the six (mcq plus at least match/fill/order/multi).
- Stems <=25 words, exactly one "?" where a question; fill stems contain
  "____" and `accept` lists every acceptable Devanagari spelling.
- mcq/multi need optionExplain for every option (the helper `mcq(...)` takes
  (text, why) pairs); `explain` and `rule` on every question; `teaches` on
  extend and transfer questions.
- Any term in quotes in a stem must be defined in the card (explanation,
  chips or aids).
- Questions test what the verse and card actually say. No counting
  questions ("how many words..."), no questions whose answer depends on an
  ambiguous split, no trivia about the editor, no questions answerable
  without the card. Transfer questions must use a NEW invented example
  built on a rule taught in this or an earlier unit, with `teaches`.
- Wrong options must be plausible but clearly wrong from the verse/card;
  do not make two options both defensible. Vary answer positions: the
  helper rotates automatically, do not fight it.
- Sanskrit in Devanagari only (no IAST in Sanskrit). English prose may use
  diacritic names (Bharadvāja); the generator folds English to plain Latin.
- Hindi for explain_hi/hook/NOTES_HI/aids. Natural Hindi, not word-for-word.

## Truth rules (most important)
1. Source-bound: every factual claim must follow from the unit's own data
   (`sutrasthana1_verses.json`: lines_deva, words with gloss/gram, hindi,
   english, notes, variants, text_flags) or from standard grammar. No outside
   claims about identity, dates, doctrine beyond the verse. If the verse is
   cryptic or a doctrine is disputed, say "the verse says...", hedge in
   `limits`, and do not build a question on the disputed point.
2. Read each unit's data first (`python3 -c` to print it). Check the Hindi
   and English translations in the data against the Sanskrit; if you find
   them wrong, do NOT silently change them: list it in your final report.
3. Known pitfalls from earlier reviews: sandhi explanations must be exact
   (state the actual rule: विसर्ग → ओ before घोष, अ + इ → ए, etc.); -औ is
   not always dual; -त्वा (before a prefix-less root) vs -ल्य/-य (with prefix);
   do not overclaim identity ("this is the same X as in..."); a listed
   item belongs only if the verse names it; Sanskrit compound readings may be
   two-way, mark them; do not call a form "future" or "past" without
   checking the gram label in the data.
4. Prose units and units that continue a sentence: say so, and tie
   questions to the part this unit contains.

## Self-check before reporting (mandatory)
Run (use your own output path):
```
cd <dir above>
BATCHES=batch_NN PARTIAL=1 python3 make_bank_ch1.py sutrasthana1_verses.json /tmp/chk/qNN.json
python3 /tmp/claude-0/-home-claude-claude-memory/0cac1b21-6382-56bd-abe4-a207ecd1a4f6/scratchpad/tpl/work/tools/validate_bank.py /tmp/chk/qNN.json
python3 make_aid_images.py /tmp/chk/imgNN   # only if you added IMAGE_SPECS; then
                                            # open the SVG(s) via Read? (text only: check the file exists and is sane)
```
Must be 0 errors and 0 warnings for your units (the "concepts" total only
counts units in your batch plus 1-10). Then re-read every question as a
student: is the keyed answer undeniably right and every distractor wrong,
by the card alone? Fix before reporting.
Do NOT edit any file except your own `batch_NN.py`. Do not run git.
Final report (<=200 words): units done, validator result, any translation
problems found in the data, any section boundary that looks wrong, any
verse you are unsure about.
