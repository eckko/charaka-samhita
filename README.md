# Charaka Samhita: Sutrasthana, chapters 1 to 3 (test build)

A test of the verse-study quiz, finished for **Su. 1 (Dirghanjivitiya, 141 units), Su. 2
(Apamargatanduliya, 36 units) and Su. 3 (Aragvadhiya, 30 units)**: the opening prose lines and every verse (66.1 included). Each
card has the Devanagari text, a tap-to-open word split with grammar, Hindi,
English, an explanation, a block of memory aids (13 kinds: chain, first
letters, यदा–तदा pairs, sandhi rule, who/to whom/why, word families,
diagram, metre, rhythm chunks, picture words, sound-alikes, look-alike
pairs, story), a text note, and a hand-written six-question ladder (1,062
questions in all). Settings has a "Sanskrit cards" section where each kind
can be shown or hidden (all on at first; saved in this browser only, never
synced to an account). Hindi, English and all
memory aids are AI-written and AI-reviewed (two independent review passes);
a scholar's check is still pending.

**This branch is a self-contained test build.** Unlike the normal book shell
(see the original README in `main`), it carries the quiz code itself
(`css/`, `js/`, `htrab/`) because the verse-study changes are not yet in a
tagged template release. The plan is to tag them in `eckko/recall-quiz-site-template`
and then return this repo to the shell layout (loader `index.html` and
`questions.json` only).

| Path | What it is |
|---|---|
| `index.html`, `css/`, `js/`, `htrab/` | The quiz site (template 2.1.0 plus the verse-study changes) |
| `questions.json` | The bank for all three chapters (book id `caraka-sutra`), generated from `data/` |
| `data/sutrasthana1_verses.json`, `sutrasthana2_verses.json` | Source data: verse text, word split, Hindi, English, flags, notes |
| `tools/make_bank.py` | Builds `questions.json` (all three chapters) from the data plus the hand-written content (needs `indic_transliteration`) |
| `tools/ch1_authored.py` | Hand-written explanations, hooks, notes and questions for units 1 to 10 (shared helpers) |
| `tools/ch2_batch_02.py` … `ch2_batch_05.py` | The same for Su. 2 (units 1 to 36); its sections are `RANGES_2` in `tools/sections.py` |
| `tools/ch3_batch_02.py` … `ch3_batch_04.py` | The same for Su. 3 (units 1 to 30, Upajāti metre so no metre aid); its sections are `RANGES_3` in `tools/sections.py` |
| `tools/batch_02.py` … `batch_14.py` | The same for Su. 1 units 11 to 140, in batches of about ten; `tools/sections.py` holds the section of every unit; `tools/AUTHORING.md` is the writing guide |
| `tools/gram_hi.py` | Hindi grammar labels for the word chips |
| `tools/ch1_aids.py`, `tools/metre.py` | Hand-written memory aids; the metre cut (8+8 akṣaras) is computed |
| `tools/make_aid_images.py`, `images/aids/` | The small pictures (drawn as SVG) used by the picture words and diagram aids |
| `js/study-aids.js` | The Sanskrit settings card and the show/hide of each aid kind |

Sanskrit text: SARIT edition of the Carakasamhita (single witness, CC BY-SA 3.0).
Hindi and English are AI-drafted and AI-reviewed, not yet checked by a person.
Rebuild: `python3 tools/make_bank.py data questions.json`.
Sync is off (`js/sync/sync-config.js`), so progress stays in the browser.

To run it: serve the folder with any static server, or turn on GitHub Pages for this branch.
