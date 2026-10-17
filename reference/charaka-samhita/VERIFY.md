# VERIFY: charaka-samhita

Dated log of the verification stage (skill verify-vedic-book-reference). Appended to through the run. text/ is changed by nobody in this stage.

## 2026-10-18 inventory
- Base: reference/charaka-samhita/text/ (76 files in "ID | Devanagari" format; S1 = SARIT, see sources.md). Branch docs/2026-10-17/version-1 continued (unmerged).
- raw/carakasamhita.xml = the SARIT source file, kept as the raw copy; raw/iast/ = its per-line IAST (audit trail). Both are inputs of the extraction, not used as the base here.
- tools/*.py = the extraction tools written for this book; reference/tools/check_extraction.py = checker. Not book text.
- text/p03.md was reported "binary-or-unknown-encoding" by inventory.py: false alarm. The file is valid UTF-8 (checked); the tool decodes only the first 200,000 bytes and cuts a multi-byte character in half. Not changed.
- Second edition: not available. Translations: none exist yet.
