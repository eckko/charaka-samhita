# Data context: Charaka Samhita quiz (for AI agents)

Give this file to any AI agent you ask to **build, review, correct or add**
chapter data. It is self-contained. Companion files: `docs/HANDOFF.md`
(project state and pipeline), `docs/review-queue.md` (units that need a
look), `tools/AUTHORING.md`, `tools/pipeline/*_BRIEF.md` (exact briefs).

## 1. Purpose and standing rules
- A personal, non-profit study tool for the Vedic texts. The Charaka Samhita
  (Sutrasthana, SARIT edition) is the proof of concept.
- **Correctness comes first** (Sanskrit text, translations, claims), then
  making the material easy for a person to read and remember.
- Sanskrit on cards is **Devanagari**, never IAST (IAST appears only in
  the source-text fields of `data/`, English prose may use diacritic names).
- Do not search the web for facts; work from the Sanskrit given and
  standard grammar. Do not invent. Where unsure, say so in `notes` and
  lower `confidence`.
- **Never silently change the source text.** The SARIT text is one witness
  with typos: keep tokens exactly as printed and list suspected errors in
  `text_flags` with a suggested reading and the reason.
- Translations are faithful: add nothing (no interpretation, no emphasis
  not in the Sanskrit), drop nothing; no meta comments inside a
  translation; Hindi has no Latin letters; keep Vata/Pitta/Kapha as वात,
  पित्त, कफ in Hindi.
- Plant, drug and preparation names: keep the name; give an identification
  only when standard and secure; never claim what a drug does beyond the verse.
- Counts and totals: state a number only if the text states it.
- Everything is AI-written and AI-reviewed only. A scholar has not checked
  it. Never present it as authoritative.

## 2. Where things are
| Path | Content |
|---|---|
| `data/sutrasthanaN_verses.json` | Verse data, one file per chapter N (1 to 4 done): list of unit records in text order |
| `data/sarit_unit_counts.json` | Unit counts per chapter of all eight Sthanas (key `sthana.chapter`) |
| `tools/chN_batch_NN.py`, `tools/batch_NN.py` | Hand-written card content (explanations, aids, questions) per batch of units |
| `tools/make_bank.py` | Builds `questions.json` from `data/` plus the batch files |
| `questions.json` | The generated quiz bank (do not edit by hand) |
| `tools/pipeline/` | Briefs and scripts for drafting and reviewing a new chapter |
| `images/aids/*.svg` | Small pictures drawn by `tools/make_aid_images.py` |

Source text: https://github.com/sarit/sarit-corpus, file `carakasamhita.xml`
(CC BY-SA 3.0). Unit number `n`: "1", "2", ... in text order; "66.1" is a
verse inserted in parentheses after unit 66 in chapter 1.

## 3. Unit record (`data/sutrasthanaN_verses.json`)
```
{
 "n": "3",
 "type": "prose" | "verse",
 "lines_iast": ["..."],             // source text as printed (SARIT, IAST), one string per line
 "lines_deva": ["..."],             // the same in Devanagari (verse: closing danda/number added by the generator)
 "lines": [ { "tokens": [           // one entry per printed line, one token per printed word
     { "src": "athātaḥ",            // EXACTLY the printed token, even if it looks wrong
       "words": [ {"w": "atha", "gloss": "now", "gram": "ind."},
                  {"w": "ataḥ", "gloss": "therefore", "gram": "ind."} ] } ] } ],
 "hindi": "...", "english": "...",  // translation of the whole unit
 "text_flags": [ {"src": "pajāpatiḥ", "suggest": "prajāpatiḥ", "why": "..."} ],
 "src_flags": [...],                // tool warnings (metre, stray marks)
 "variants": [ {"after": "word", "reading": "variant from the edition footnote"} ],
 "notes": "...",                    // ambiguity, alternative readings, where commentators differ; "" if none
 "confidence": "high" | "medium" | "low",
 "lead_in_tokens"/"lead_in_hindi"/"lead_in_english"   // only the formula "tatra ślokāḥ" (1.136)
}
```
Word rules: `w` is the word with sandhi undone and original forms restored;
compound members are joined with "-" (e.g. `ṣaḍ-virecana-śata-āśritīyam`);
`gloss` is the meaning in context (English); `gram` is a short grammar
label (case, number, gender; tense/person and root for verbs; `ind.` for
indeclinables; `tat-puruṣa`, `dvandva` etc. for compound members).
Common reviewer finds: wrong case label, wrong root, enclitic `me` taken as
ablative, `-au` assumed dual, kṛdanta forms mislabelled.

## 4. Card and question format (what `questions.json` holds)
Bank: `{id: "caraka-sutra", book, labels, summary, genre, scrollButtons,
unitSummaries, concepts[], questions[]}`. One **concept** per unit, id
`suN-NNN`.
```
concept: { id, unit: "Chapter N", unitTitle, section, title, requires[],
           core: bool, question (one-line focus question),
           card: { rule, limits, blocks[] } }
blocks (each has "key" and a Devanagari "label"):
  ref (reference line) · verse (study, lines[]) · words (study, rows of
  {w, gloss, gram}, at most 30 chips a row) · hindi · english · explain
  (Hindi, 3 to 6 sentences) · aids (study, list of aids) · note (Hindi
  textual note: sandhi checked, variants, two-way readings)
aid:   { aid: kind, label, text | steps[] | groups[], image?: {src, alt} }
kinds (13): frame chain diagram letters seesaw story pegs puns anchors
            sandhi contrast chunks metre   (metre is computed, never written)
```
Aid rules: only kinds that really help that unit (3 to 6, never all 13);
`diagram`/`chunks` reproduce the verse's own words in printed order;
`seesaw` only for a true pair of opposites that both occur in this verse;
`pegs` and `puns` are the learner's memory hooks, labelled as made-up
("मेरा बनाया चित्र"), never claims about the verse; picture text is short
Devanagari/Hindi and matches the aid text.

**Six questions per unit**, rungs 0 to 5, roles in order: `pretest`,
`warmup`, `extend`, `discriminate`, `apply`, `transfer`. Kinds:
- `mcq`: `q`, `options[]`, `answer` (index), `optionExplain[]` (one per option);
- `multi`: `q`, `options[]`, `answers[]` (indexes), `optionExplain[]`;
- `match`: `q`, `pairs[[left, right], ...]`;
- `fill`: `q` containing `____`, `accept[]` (every acceptable Devanagari spelling);
- `order`: `q`, `items[]` in the correct order.
Every question also has `explain`, `rule`; `extend` and `transfer` have
`teaches`. At least 3 kinds per unit. Stems 25 words or fewer, one "?".
Wrong options must be plausible but clearly wrong from the card alone;
no counting trivia; a quoted term in a stem must be defined on the card;
transfer questions use a NEW invented example built on a rule taught, valid
Sanskrit with agreeing case, number and gender.

## 5. Tasks you may be given
**A. Build a new chapter.** Follow `docs/HANDOFF.md` section "How a chapter
is built" and the briefs in `tools/pipeline/`. Output: unit records as in
section 3, then batch files for the cards.

**B. Review a chapter (read-only).** Check word by word: split, gloss,
gram, translation faithfulness, text flags, notes, confidence; then each
card claim and each question (keyed answer undeniably right, distractors
undeniably wrong, multi-answer index arithmetic, match pairs, fill
spellings). Reply with JSON (no file edits):
```
{"units":[{"n":"3","verdict":"ok|fix","issues":[
  {"field":"english|hindi|notes|gram|gloss|split|text_flags|explain|aids|question",
   "where":"word or question id","problem":"...","fix":"exact replacement text",
   "severity":"error|minor"}]}],"summary":"..."}
```
Past reviews found real errors every time; be adversarial and concrete.

**C. Correct data.** Apply only fixes you can justify from the Sanskrit
and standard grammar. Edit `data/*.json` (or the batch file), keep a list of
every change (unit, field, old, new, reason), then rebuild and validate:
```
python3 tools/make_bank.py data questions.json
python3 <template checkout>/tools/validate_bank.py questions.json   # 0 errors, 0 warnings
```
Do not edit `questions.json` by hand. If a correction touches the source
text itself, use `text_flags` instead and leave the printed token alone.

**D. Add content** (explanations, aids, questions, pictures): follow
`tools/AUTHORING.md`; add your own `chN_batch_NN.py` and edit nothing else.

## 6. Quality bar (past findings, all real)
Unsupported additions in translations ("fifth", "thus ends", emphasis);
wrong gram labels; invented or invalid Sanskrit in aids and transfer
questions; chunk words that differ from the printed text; contested counts
used as fact; overclaimed identity ("the same X as in ..."); sandhi rules
stated loosely (state the actual rule); explanations that go beyond the
verse. Sentences often run across several verses: say so on the card and
keep each question to what the unit contains.

## 7. Known items still open
See `docs/HANDOFF.md` (chapter 4 list) and `docs/review-queue.md`
(generated: every unit with confidence below high or with text flags).
