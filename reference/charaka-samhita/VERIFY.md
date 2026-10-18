# VERIFY: charaka-samhita

Dated log of the verification stage (skill verify-vedic-book-reference). Appended to through the run. text/ is changed by nobody in this stage.

## 2026-10-18 inventory
- Base: reference/charaka-samhita/text/ (76 files in "ID | Devanagari" format; S1 = SARIT, see sources.md). Branch docs/2026-10-17/version-1 continued (unmerged).
- raw/carakasamhita.xml = the SARIT source file, kept as the raw copy; raw/iast/ = its per-line IAST (audit trail). Both are inputs of the extraction, not used as the base here.
- tools/*.py = the extraction tools written for this book; reference/tools/check_extraction.py = checker. Not book text.
- text/p03.md was reported "binary-or-unknown-encoding" by inventory.py: false alarm. The file is valid UTF-8 (checked); the tool decodes only the first 200,000 bytes and cuts a multi-byte character in half. Not changed.
- Second edition: not available. Translations: none exist yet.

## 2026-10-18 completeness and checks
- structure_check.py: no flags (8 sthānas, 120 chapters, 19,540 lines). check_extraction.py: 0 errors, 0 warnings (ID_RE widened for dotted verse numbers, see FORMAT.md §6).
- word_check.py run (checks/word_check.md, stray.tsv 168, typos.tsv 90, metre.tsv 1806). Second edition: not available, skipped.
- Hyphen/bracket characters inside Sanskrit lines were left as the source has them.
- proofread_pack.py: 37 packs, one agent each, 2,178 items answered; 568 proposals; sample error rate 13/114 = 11.4%. Summary in ISSUES.md. Memory-sourced suggestions and neighbouring-line typos are noted there as unverified.
- text/ unchanged. Nothing is called "verified" beyond these checks.

## 2026-10-18 correction: dotted verse numbers
- vtext.ID_RE (skill tools) did not accept IDs like 01.01.66.1a. chapters() skipped them without a message, so structure_check, word_check, proofread packs and plan_work had left out 849 lines / 416 units. Not changed in the skill repo; a private copy of the tools with the pattern widened was used for the re-run and for write_layers/plan_work. Suggested fix for the skill: widen `verse` to `P?\d+(?:\.\d+)?(?:-\d+)?` in vtext.py and make chapters() report skipped IDs.
- Re-run: structure_check (no flags), word_check, plan (10,716 units), proofreading packs 38–39 for the new flagged lines (100 items). Summary in ISSUES.md.
- Layers: Sūtrasthāna ch 1 written (5 chunks, draft→check→independent review→applied; manual note: unit 41 token split fixed by hand). All layers are reviewed AI drafts, not read by a person.
