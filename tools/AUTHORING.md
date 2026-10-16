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
BATCHES=batch_NN PARTIAL=1 python3 make_bank.py ../data /tmp/chk/qNN.json
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


---
# CHAPTER 2 (Apāmārgataṇḍulīya, Su. 2) differences — these override the above
- Work in the repo: /home/claude/charaka-samhita/tools/ (not the scratchpad copy). Data:
  /home/claude/charaka-samhita/data/sutrasthana2_verses.json (36 units, keys "1".."36").
  Study finished examples in ch1_authored.py (units 3, 5, 9, 10) and batch_08.py, batch_11.py
  (list-heavy verses), which already passed independent review.
- Your file is `ch2_batch_NN.py` in tools/, starting with `from ch1_authored import mcq, match, order, fill, multi`.
  Keys of AUTHORED/NOTES_HI/AIDS are the unit numbers "1".."36". Do not write "section"
  (tools/sections.py RANGES_2 supplies it). Concept ids are su2-NNN; use those in any `requires`
  (omit `requires` normally).
- Picture file names MUST start with "ch2-" (e.g. "ch2-drugs-5.svg"); IMAGE_SPECS keys are (unit, kind) as before.
- Self-check from tools/:
  `BATCHES=ch2_batch_NN PARTIAL=1 python3 make_bank.py ../data /tmp/chk/c2NN.json` then
  `python3 /tmp/claude-0/-home-claude-claude-memory/0cac1b21-6382-56bd-abe4-a207ecd1a4f6/scratchpad/tpl/work/tools/validate_bank.py /tmp/chk/c2NN.json`
  (0 errors, 0 warnings except the 'requires … not an earlier concept' batch-edge error), and for pictures
  `python3 make_aid_images.py /tmp/chk/img2NN`. Delete `tools/__pycache__` afterwards. Edit only your own file.
- Subject: drug groups and gruels for the five treatments. The verse lists names and uses; it gives no dose,
  no pharmacology and no modern identification beyond the data's glosses. Never identify a plant beyond the
  card data; never state what a drug "does" except what the verse says; never build a question on a plant's
  identity or on a contested construal. Good question types here: which treatment a list is for (head-purging /
  emesis / purgation / enemas), which condition a gruel is for, match gruel-feature to its effect, order of
  the five procedures as the verse states them, what the compound/sandhi form is, and transfer questions on
  the sentence frame ("X gruel cooked in Y removes Z"). Verses 3-5, 7-8, 9-10, 11-14 form sentences that run
  over several verses: say so on the card and keep each question to what this unit contains.
- Pitfalls the chapter-1 reviews found (all became fixes): seesaw only for a true pair of opposites that
  both appear in THIS verse; diagram/chunks must reproduce the printed words in printed order (incl. repeated
  words, and printed sandhi like ऽ); sandhi rules stated exactly (अः+घोष → ओ only after अ; इः/उः → र्; after आ the
  visarga drops); an invented transfer sentence must be valid Sanskrit with agreeing case/number/gender;
  fill `accept` lists every spelling a learner may type (with/without anusvāra form, printed sandhi form);
  stems <=25 words with a single "?"; no "listed in verses X-Y" claims unless checked; do not add
  etymologies or interpretations not in the data; say "my own picture" for pegs; keep claims about the
  edition's typos tied to the data's text_flags.


---
# CHAPTER 3 (Āragvadhīya, Su. 3) differences — these override the above, and the Chapter 2 notes apply with these changes
- Data: /home/claude/charaka-samhita/data/sutrasthana3_verses.json (30 units, keys "1".."30"). Your file is
  `ch3_batch_NN.py` in tools/; concept ids are su3-NNN; picture file names start with "ch3-"; sections are
  RANGES_3 in tools/sections.py. Self-check: `BATCHES=ch3_batch_NN PARTIAL=1 python3 make_bank.py ../data /tmp/chk/c3NN.json`
  then the validator, then `python3 make_aid_images.py /tmp/chk/img3NN`; delete tools/__pycache__.
- Metre: these verses are Upajāti (22 syllables per printed line, two pādas of 11), not anuṣṭubh. The generator adds
  no automatic metre aid here. Do NOT write a "metre" aid and do not say 8+8 anywhere.
- Subject: the chapter lists drugs for medicinal powder-pastes (pradeha/lepa) for skin disease, vāta, headache, etc.,
  and verse 30 says 32 such pradehas. Ch.2 rules on drug claims apply fully: no identification of a plant beyond the
  data glosses, no effect or dosage claim beyond the verse, no question on a plant's identity or on contested
  construals (the data notes mark many). Good question types: which condition a drug list serves, which verse's
  list is for which purpose, sandhi and compound splits (long drug compounds), case/number (dual -ए/-औ forms such as
  haridre, śatāhve), the pradeha frame sentences, and transfer on that frame. Many verses are lists that continue
  from the previous unit; say so and keep each question within the unit.
- Verse 16 refers to the drugs of verse 15 and verse 6 closes the list begun in verse 3: state such links on the card.


---
# CHAPTER 4 (Ṣaḍvirecanaśatāśritīya, Su. 4) differences — these override the above; Chapter 2 and 3 notes apply with these changes
- Data: /home/claude/charaka-samhita/data/sutrasthana4_verses.json (29 units, keys "1".."29"). Your file is
  `ch4_batch_NN.py` in tools/; concept ids are su4-NNN; picture file names start with "ch4-"; sections are RANGES_4 in
  tools/sections.py. Self-check: `BATCHES=ch4_batch_NN PARTIAL=1 python3 make_bank.py ../data /tmp/chk/c4NN.json`, then the
  validator, then `python3 make_aid_images.py /tmp/chk/img4NN`; delete tools/__pycache__.
- Units 1-22 are PROSE (no metre); units 23-29 are anuṣṭubh verses (the generator adds the metre aid automatically; never write a
  "metre" aid). Unit 23 carries the lead-in "tatra ślokāḥ". Prose units have no "who/whom" frame; use chain/diagram/chunks/contrast/
  letters/anchors/sandhi kinds as fits.
- Subject: the chapter says there are 600 purgative formulas, their six sources (kṣīra, mūla, tvak, patra, puṣpa, phala), the
  five kinds of kaṣāya "source", the five preparations (svarasa, kalka, śṛta, śīta, phāṇṭa — the text says "five" but lists
  six names incl. kaṣāya; say so on the card, do not resolve it), the 50 mahākaṣāya classes of ten drugs each (units 8-18), the
  exchange where Agniveśa objects that the 500 do not fill up and Ātreya replies (21-22), and a verse summary (23-29).
- Drug-name lists: the data's `notes` list the ten names of every group as split by the draft and checked by a second reviewer.
  RULES: (1) no identification of any plant, no effect, no dose beyond what the Sanskrit says; (2) the name of a class
  (jīvanīya, bṛṃhaṇīya ...) is a LABEL given by the text: gloss literally as the data does; (3) good questions use the STRUCTURE:
  how many drugs a group has ("daśemāni"), which class a list belongs to by its closing label, how many classes in a section (unit 8:
  6,4,6,4,7,3,5,5,5,5 = 50), order of classes, sandhi/compound splits of printed tokens, the frame sentence "daśemāni X bhavanti",
  and transfer on that frame; (4) you MAY ask whether a drug name is in a group only for names that the data prints as a clean
  separate token or whose split carries no flag/doubt in `notes`, never for names marked doubtful (list of doubtful units:
  9, 10, 11, 12, 13, 14, 15, 17, 18 have boundary doubts; read each unit's `notes`/`text_flags`); (5) never build a question
  on a contested number: unit 4's "133" is inferred (ask only what the unit says in words: the total 600, the number of
  sources), unit 17 group 3 has eleven names as printed, unit 15 group 2 is 11 as split, unit 7 says five but lists six;
  (6) a list continues across units 9-18: state "this is classes X-Y of 50" on the card and keep each question within the unit;
  (7) typos flagged in text_flags (e.g. 'rśoghraḥ for 'rśoghnaḥ) go in NOTES_HI as flags, never as questions.
- Pictures: list-heavy units may have a chain/table/split image (e.g. the 50 classes by size of section in unit 8: a table),
  at most ~1 picture per 3 units; text in pictures must equal the aid text and be Devanagari.
