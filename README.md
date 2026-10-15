# Charaka Samhita: Sutrasthana, chapter 1 (test build)

A test of the verse-study quiz: 141 verse cards (139 verses and 2 prose lines
of Su. 1, Dirghanjivitiya) with Devanagari text, word-by-word split,
Hindi and English, plus 846 auto-generated practice questions.

**This branch is a self-contained test build.** Unlike the normal book shell
(see the original README in `main`), it carries the quiz code itself
(`css/`, `js/`, `htrab/`) because the verse-study changes are not yet in a
tagged template release. The plan is to tag them in `eckko/recall-quiz-site-template`
and then return this repo to the shell layout (loader `index.html` and
`questions.json` only).

| Path | What it is |
|---|---|
| `index.html`, `css/`, `js/`, `htrab/` | The quiz site (template 2.1.0 plus the verse-study changes) |
| `questions.json` | The Chapter 1 bank, generated from `data/` |
| `data/sutrasthana1_verses.json` | Source data: verse text, word split, Hindi, English, flags, notes |
| `tools/make_bank_from_verses.py` | Builds `questions.json` from the data (needs `indic_transliteration`) |

Sanskrit text: SARIT edition of the Carakasamhita (single witness, CC BY-SA 3.0).
Hindi and English are AI-drafted and AI-reviewed, not yet checked by a person.
Sync is off (`js/sync/sync-config.js`), so progress stays in the browser.

To run it: serve the folder with any static server, or turn on GitHub Pages for this branch.
