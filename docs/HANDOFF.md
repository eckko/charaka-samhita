# Handoff: how to continue the Charaka Samhita quiz

Written 2026-10-16 at the end of a long Claude Code session, so a new
session (or a person) can carry on without the old conversation.
Read this first; `docs/DATA-CONTEXT.md` describes the data for other AI
agents; `docs/review-queue.md` lists units that need a human look.

## What this project is
Rahul's personal, non-profit study quiz for the Vedic texts. The Charaka
Samhita is the proof of concept; more texts follow later. Per verse the
card has Devanagari text, sandhi viccheda (word split with gloss and
grammar), Hindi, English, explanation, memory aids (13 kinds) and a
six-question ladder. **Correctness of text, translation and information
comes first**, then presentation that a person can remember. Sanskrit is
always Devanagari on the cards. Sources are public domain; the SARIT TEI
edition is the single source text so far. Hindi/English/aids are AI-written
and AI-reviewed only: no scholar has checked them yet.

## State (2026-10-16)
| Chapter (Sutrasthana) | Units | Status |
|---|---|---|
| 1 Dirghanjivitiya | 141 (66.1 is an inserted verse) | done, reviewed |
| 2 Apamarga-tanduliya | 36 | done, reviewed |
| 3 Aragvadhiya | 30 | done, reviewed |
| 4 Shadvirecanashatashritiya | 29 | done, reviewed |
| 5 to 30 | about 1,716 units in SARIT | not started |

`questions.json`: 236 concepts, 1,416 questions, validator 0 errors and
0 warnings. Chapters 5 onward are not started; later Sthanas (Nidana,
Vimana, Sarira, Indriya, Cikitsa, Kalpa, Siddhi) are also in SARIT, counts
in `data/sarit_unit_counts.json` (key = sthana.chapter).

## Repos and releases
- **This repo** (`eckko/charaka-samhita`) is a *book shell*: `index.html`
  (loader), `questions.json`, `images/` and `tools/`, plus `data/`. It
  carries no template code. `index.html` loads the quiz from tag `2.2.1`
  of `eckko/recall-quiz-site-template` on jsDelivr and sets the book's own
  start-up choices (theme Parchment & Teal, home layout) in
  `window.RecallQuizBookDefaults`. Move to a newer template with
  `python3 tools/set_template_tag.py TAG` (exact tag, never a branch).
- **Template** (`eckko/recall-quiz-site-template`, tags 2.2.0 and 2.2.1,
  merged by the owner): Sanskrit-card settings (each of 8 card parts and
  13 aid kinds can be hidden; verse font dropdown with a live sample;
  settings v3 synced to the account), 15 Vedic/Ayurveda themes, opt-in
  scroll buttons (`scrollButtons: true` in the bank), the
  `RecallQuizBookDefaults` hook, `make_book_index.py --defaults`. Its
  `ai-context/` folder has the data formats and the pitfalls.
- **Claude memory repo** (`eckko/claude-memory`) mirrors skills and project
  memory files; see "Memory" below.
- Branch rules from the owner: push new branches only; the owner merges and
  sets defaults. Commits end with the two Claude trailers. Run
  `git update-ref refs/remotes/origin/<branch> HEAD` after a push (the
  proxy does not update tracking refs). Tags cannot be pushed from Claude
  sessions: ask the owner to tag.
- A branch that already exists on GitHub can be rejected on a second push
  ("protected branch hook"); push follow-ups to a new branch name.

## How a chapter is built (the pipeline)
Briefs and scripts are in `tools/pipeline/` (they still contain absolute
paths of the old session; edit the paths first).
1. **Source units.** `sarit_units.py`/`sarit_stats.py` count units in the
   SARIT file; `build_verses.py SRC OUT CH` turns one chapter of
   `carakasamhita.xml` (from https://github.com/sarit/sarit-corpus, needs
   `indic_transliteration`) into verse records (IAST lines, variants,
   metre flags). Nothing is silently corrected: typos are kept and flagged.
2. **Chunk and draft.** Cut the units into chunks of 20 to 60 units
   (`chunkK_in.json`). A drafting agent follows `DRAFT_BRIEF.md` and writes
   `chunkK_out.json`: per token the sandhi split, gloss and grammar, plus
   Hindi, English, text flags, notes, confidence. `check_chunk.py IN OUT`
   checks structure (tokens equal the input, no Latin in Hindi, ...).
3. **Independent review.** A second agent follows `REVIEW_BRIEF.md` and
   writes `chunkK_review.json` (issues with exact fixes). Reviewers found
   real errors every time: unsupported additions in translations, wrong
   case labels or roots, invented Sanskrit, contested counts used as fact.
   `apply_review.py` is the pattern for applying fixes into
   `chunkK_final.json` and logging every change; then merge the finals
   into `data/sutrasthanaN_verses.json` (add `lines_deva`, keep `variants`).
4. **Author the cards.** For each unit write explanation, hook, note,
   memory aids, optional picture specs and six questions, in
   `tools/chN_batch_NN.py` files (10 to 15 units each). Rules:
   `tools/AUTHORING.md` (its chapter-1 paths are stale; the chapter 2 and
   later notes at the end override). Add the chapter to `CHAPTERS` in
   `tools/make_bank.py`, ranges to `tools/sections.py`, and a
   `unitSummaries` line.
5. **Review the authored batches** with `AUTHOR_REVIEW_BRIEF.md` (reviewers
   found 13 to 18 real problems per 10 units in chapter 1), fix, rebuild:
   `python3 tools/make_bank.py data questions.json`.
6. **Validate.** `python3 <template>/tools/validate_bank.py questions.json`
   must show 0 errors and 0 warnings (needs a checkout of the template at
   the tag in use). Then look at a few cards in a browser.
7. Update `README.md`, push a new branch, let the owner merge.

Lessons that cost time: word chips are capped at 30 per row (`split_long`
in make_bank.py cuts long prose lines); keep `src` tokens exactly as
printed; Hindi must not contain Latin letters; do not state a plant
identification beyond the data; never state counts the text itself does
not give; a quoted term in a question stem must be defined on the card.

## Open items and decisions
- **Scholar check** of Sanskrit, Hindi, English and aids is still pending;
  SARIT is a single witness. The owner can supply more editions and
  translations to be combined into one reliable text; none were used yet.
- Chapter 4 items to confirm: source typos `'rśoghraḥ` (unit 8),
  `kṣīrakālolī` and `viḍaṅgśigru` (13), `yavayaṣṭiko` (14),
  `gairikarpiyaṅgu` (18), `mahākaṣāyeṣvati` (21); unit 4's 133/110 split is
  inferred from the stated total of 600; unit 7 says "five" but lists six;
  unit 17 group 3 has 11 names and unit 15 group 2 is 11 as split.
  Other chapters: see `docs/review-queue.md`.
- `questions.json` is 3.7 MB (about 510 KB gzipped). No chunking needed.
  Revisit if it passes roughly 10 MB.
- Bank id is `caraka-sutra`; progress saved under older ids does not carry
  over. GitHub Pages must be on for the shell repo.
- The repo will later be made private and encrypted (owner's plan); the
  template supports encrypted media but the bank is plain today.
- The cards in all sessions share one renderer, so the Sanskrit settings
  apply everywhere; the owner read "sync to session" that way.

## Environment notes (Claude Code on the web)
- Python needs `indic_transliteration`; Playwright and Chromium are
  pre-installed (do not run `playwright install`).
- Google Fonts is not reachable from the sandbox, so screenshots show
  fallback fonts; check the real fonts on a phone.
- The template tests use port 8765: do not leave another server there.
- Long waits: run in the background and poll; do not chain `sleep`.
- Git proxy: at most two concurrent operations on the template repo.

## Memory
Claude's memory for this project lives in the claude.ai Project "learning
helper" (file `areas/charaka-samhita-quiz.md`) and is mirrored to
`eckko/claude-memory`. The standing preferences are copied in this file and
in `docs/DATA-CONTEXT.md`, so a session without that memory still has them.
