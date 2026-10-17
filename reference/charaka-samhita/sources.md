# Sources: charaka-samhita

| ID | Name | URL | Edition / editor / year | Script | Licence | Covers | Fetched how | Quality note | Role |
|---|---|---|---|---|---|---|---|---|---|
| S1 | SARIT: Carakasaṃhitā (carakasamhita.xml) | https://github.com/sarit/sarit-corpus (file carakasamhita.xml); fetched from https://raw.githubusercontent.com/sarit/sarit-corpus/master/carakasamhita.xml | Yādavaśarman Trivikramātmaja Ācārya, 3rd ed. Nirnaya Sagar Press, Bombay 1941 (4th ed. Munshiram Manoharlal 1981), with Cakrapāṇidatta's Āyurvedadīpikā; commentary text not in the e-text. E-text by T. Yamashita, Y. Muroya, Y. Yamanaka, Madhu K. P. (Kyoto); TEI by D. Wujastyk | IAST with the e-text's own markers (see below) | CC BY-SA 3.0 (SARIT) | all 8 sthānas, 120 chapters | curl from raw.githubusercontent.com, sha256 9f8c1730ff16265b909236539eebcfaa6ddb365fb67c0e07ff4d406b1b583c71, copy in raw/carakasamhita.xml | typed e-text with editorial markers (footnote anchors, restored sandhi, inline footnote texts) and a few typos; header says some footnotes are missing | primary (only source so far) |

Not used: GRETIL (gretil.sub.uni-goettingen.de answers 403 to the shell; the owner would have to download the file), Sanskrit Documents, Wikisource, DCS: not tested in this run. No Hindi or English translation was fetched (step 5 of the skill is still open).

## Conversion notes (tools/sarit_convert.py)

SARIT's header says: initial vowel elision for avagraha is reversed and marked with an apostrophe (`prathamo 'adhyāyaḥ`); external sandhi is undone and marked with a plus sign; the ampersand anchors a footnote in the printed edition; text division follows the Devanagari print. To get the printed form back, the converter:

1. leaves out editor's text typed into a line (footnote readings like `` `x' iti pā-. ``, `{...}`, `[&'...'iti pā+]`, `(=Sū.sū.45.142cd)`) and reports each in ISSUES.md as a variant;
2. removes `&` anchors (counts per chapter in STATUS.md);
3. restores sandhi: o/e + a gives ऽ, ā + a and ā + ā give ā, a + a gives ā; other cases are kept and reported;
4. reads other apostrophes as quotation marks, `/` as ।, `//` as ॥, drops the chapter number in `//2//`, writes other digits in Devanagari;
5. reads capital `Y` as ṝ and capital `O` as o (both reported);
6. transliterates IAST to Devanagari with indic_transliteration.

The untouched IAST of every line is in raw/iast/ (tab separated: ID, element, xml:id, text) and the whole file in raw/carakasamhita.xml, so every conversion can be audited.

Known differences from the earlier data/ files of the quiz repo (Sūtrasthāna 1-4, same SARIT file, different pipeline): those files leave out colophons, `tatra ślokāḥ` lead-ins and parenthesised verses and join some sandhi differently. Here everything in S1 is kept (parenthesised verses with their parentheses).
