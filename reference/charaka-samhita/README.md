# Charaka Samhita: raw extracted source bank

Stage 1 (extraction) of a pipeline: verify, review, fix, proofread come next. This folder holds the raw text, not a finished edition. Nothing here has been proofread.

Read, in order: FORMAT.md (file and line format), toc.md (structure), STATUS.md (what is done), sources.md (where text came from and how it was converted), ISSUES.md (known doubts).

Rules for anyone editing here:
- Text lines come only from sources listed in sources.md; never from memory.
- Do not rename files or change line IDs of finished chapters.
- Record every doubt in ISSUES.md; fix text only in a later, explicit proofreading stage.
- Run `python3 reference/tools/check_extraction.py reference/charaka-samhita` before every commit.
- Branch pattern: `docs/YYYY-MM-DD/version-N`; push new branches only; the owner merges.

How the files are made: `python3 -I tools/build.py` (run in this folder) rebuilds text/, raw/iast/, toc.md, STATUS.md and ISSUES.md from raw/carakasamhita.xml. Do not edit those by hand; change the tools and rebuild. The checker in reference/tools/ is the skill's copy with one change (see FORMAT.md section 6).

What is in the text files, in short:
- 19,540 Devanagari lines, 120 chapters of 8 sthānas. Colophons are kept as the last P line of their chapter; verses printed in parentheses in the edition keep their parentheses.
- IDs follow the edition's own numbering. Prose paragraphs the edition does not number are P1, P2, ... in order.
- Lines that were only an editor's footnote typed into the e-text are left out (listed in ISSUES.md).

How to continue: open STATUS.md. Open items: Hindi and English translations (none fetched), a second source to cross-check S1, and the doubts in ISSUES.md. Follow the skill `/extract-vedic-book-web` (or FORMAT.md and sources.md if the skill is not available).
