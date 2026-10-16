# Charaka Samhita: Sutrasthana, chapters 1 to 4 (test build)

A test of the verse-study quiz, finished for **Su. 1 (Dirghanjivitiya, 141 units), Su. 2
(Apamargatanduliya, 36 units) Su. 3 (Aragvadhiya, 30 units) and Su. 4 (Shadvirecanashatashritiya, 29 units)**: the opening prose lines and every verse (66.1 included). Each
card has the Devanagari text, a tap-to-open word split with grammar, Hindi,
English, an explanation, a block of memory aids (13 kinds: chain, first
letters, यदा–तदा pairs, sandhi rule, who/to whom/why, word families,
diagram, metre, rhythm chunks, picture words, sound-alikes, look-alike
pairs, story), a text note, and a hand-written six-question ladder (1,416
questions in all). Settings has a "Sanskrit cards" section where each kind
and each part of the card can be shown or hidden, and the verse font chosen (all on at first; saved with the book settings and synced to your account when signed in). Hindi, English and all
memory aids are AI-written and AI-reviewed (two independent review passes);
a scholar's check is still pending.

**This repo is a book shell.** `index.html` loads all quiz code from tag
`2.2.1` of `eckko/recall-quiz-site-template` on jsDelivr (move to another
tag with `python3 tools/set_template_tag.py TAG`; the tag must exist). The
book sets its own start theme (Parchment & Teal) in `index.html`.

| Path | What it is |
|---|---|
| `index.html` | Loader: favicon, the book's start-up choices, template tag 2.2.1 |
| `tools/set_template_tag.py` | Moves `index.html` to another exact template tag |
| `questions.json` | The bank for all four chapters (book id `caraka-sutra`), generated from `data/` |
| `data/sutrasthana1_verses.json`, `sutrasthana2_verses.json` | Source data: verse text, word split, Hindi, English, flags, notes |
| `tools/make_bank.py` | Builds `questions.json` (all four chapters) from the data plus the hand-written content (needs `indic_transliteration`) |
| `tools/ch1_authored.py` | Hand-written explanations, hooks, notes and questions for units 1 to 10 (shared helpers) |
| `tools/ch2_batch_02.py` … `ch2_batch_05.py` | The same for Su. 2 (units 1 to 36); its sections are `RANGES_2` in `tools/sections.py` |
| `tools/ch4_batch_02.py` … `ch4_batch_04.py` | The same for Su. 4 (units 1 to 29; prose units 1 to 22, anuṣṭubh verses 23 to 29); its sections are `RANGES_4`. Long prose lines are cut into rows of at most 30 word chips |
| `tools/ch3_batch_02.py` … `ch3_batch_04.py` | The same for Su. 3 (units 1 to 30, Upajāti metre so no metre aid); its sections are `RANGES_3` in `tools/sections.py` |
| `tools/batch_02.py` … `batch_14.py` | The same for Su. 1 units 11 to 140, in batches of about ten; `tools/sections.py` holds the section of every unit; `tools/AUTHORING.md` is the writing guide |
| `docs/HANDOFF.md`, `docs/DATA-CONTEXT.md`, `docs/review-queue.md` | How to continue; the data description to give other AI agents; units needing a look |
| `tools/pipeline/`, `data/sarit_unit_counts.json` | Briefs and scripts for drafting and reviewing new chapters; unit counts of all SARIT chapters |
| `tools/gram_hi.py` | Hindi grammar labels for the word chips |
| `tools/ch1_aids.py`, `tools/metre.py` | Hand-written memory aids; the metre cut (8+8 akṣaras) is computed |
| `tools/make_aid_images.py`, `images/aids/` | The small pictures (drawn as SVG) used by the picture words and diagram aids |

Sanskrit text: SARIT edition of the Carakasamhita (single witness, CC BY-SA 3.0).
Hindi and English are AI-drafted and AI-reviewed, not yet checked by a person.
Rebuild: `python3 tools/make_bank.py data questions.json`.
Sync is the template's (sign in from Settings); the Sanskrit-card choices sync too.

To run it: serve the folder with any static server, or turn on GitHub Pages for this branch.
