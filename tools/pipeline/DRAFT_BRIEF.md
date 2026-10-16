# Brief: sandhi viccheda + Hindi + English for Carakasaṃhitā, Sūtrasthāna 4 (Ṣaḍvirecanaśatāśritīya)

You are drafting study material for ONE chunk of the fourth chapter of the Carakasaṃhitā. The reader wants to
(1) see dense verses broken into individual words (sandhi viccheda, plus compound splitting) so they can understand and
remember them, and (2) have a faithful Hindi and English translation so that errors can be spotted.
Correctness matters far more than elegance. Do not search the web; work from the Sanskrit given and your own knowledge.

## Input
`chunkK_in.json` : a list of records, in order. Fields:
- `n` unit number ("1","2" are prose; units are numbered as in the edition).
- `type` "prose" or "verse".
- `lines_iast` : the Sanskrit as typed in a machine-readable edition (SARIT), one string per line (half-verse). It is
  a single noisy witness: it contains data-entry typos. DO NOT silently fix them.
- `lead_in` (only verse 23): the formula "tatra ślokāḥ" ("here are the verses").
- `notes` : variant readings the edition footnotes (`after` = word it follows, `reading` = variant).
- `flags` : tool warnings (metre problems, stray marks).
- `syllables`/`scan` may be absent. Units 1-22 are PROSE; units 23-29 are verses in anuṣṭubh (16 syllables per printed line, i.e. two pādas of 8; a 'metre' flag here is a real signal).

## Output
Write `chunkK_out.json` (same directory) : a JSON list, one object per input record, same order, same `n`:
```
{
 "n": "3",
 "lines": [                         // one entry per input line, in order
   { "tokens": [                    // one entry per whitespace-separated token of that input line
       { "src": "athāto",           // EXACTLY the input token, character for character (even if you think it is a typo)
         "words": [                 // the token with sandhi undone, original forms restored; compound members joined by "-"
           {"w":"atha", "gloss":"now", "gram":"ind."},
           {"w":"ataḥ", "gloss":"therefore", "gram":"ind."}
         ] },
       ... ] } ],
 "hindi":   "...",                  // Hindi (Devanagari) translation of the whole unit, faithful, clear, standard Hindi
 "english": "...",                  // English translation of the whole unit, faithful
 "text_flags": [                    // suspected errors in the Sanskrit as given; [] if none
   {"src":"daḍrśur", "suggest":"dadṛśur", "why":"..."} ],
 "notes": "...",                    // ambiguity, alternative readings, where commentators differ; "" if none
 "confidence": "high|medium|low"    // your confidence in split + translation of THIS unit
}
```
For verse 23 also add `"lead_in": {"src":"tatra","words":[...]}`-style tokens for "tatra ślokaḥ" under key `lead_in_tokens`
(list of token objects as above) and `lead_in_hindi`, `lead_in_english`.

## Rules for the split (sandhi viccheda)
1. Undo sandhi and restore each word to its dictionary-style inflected form: "bharadvāja upāgamat" -> `bharadvājaḥ`, `upāgamat`;
   "athāto" -> `atha`, `ataḥ`; "'sitaḥ" (written 'a in the source, avagraha) -> `asitaḥ`.
2. Split compounds (samāsa) into members joined by hyphen: `brahma-jñānasya`. For a long compound give every member.
   Put the compound's type or its resolution in `gram` when it helps ("tat-puruṣa", "dvandva", "bahuvrīhi").
3. Use IAST throughout, ṃ for anusvāra, ḥ for visarga, ' only for avagraha in `src`.
4. `gloss` is a short English meaning IN THIS CONTEXT (1 to 5 words). `gram` is a short grammatical tag:
   "m. nom. sg.", "n. acc. sg.", "f. inst. sg.", "gen. pl.", "ind.", "3 sg. pf. √gr̥h", "abs. √budh", "pres. part. √icch", ... Keep it brief.
   If unsure about case or root, say so in `notes` rather than guessing.
5. Every input token must appear in `tokens`, in order. The joined `src` values of a line must equal the input line exactly
   (the checker verifies this). Never merge, drop, reorder or "correct" input tokens.
6. If you believe the input has a typo, keep `src` as given, use the CORRECTED form in `words`, and add an entry to
   `text_flags` (with `why`). Use the metre (verses 23-29: 16 per printed line; prose has no metre), the sense, and parallels within the chunk as evidence.
   If the typo is only suspected, say "possible" in `why`.

## Rules for translation
- Translate what the Sanskrit says; do not import later knowledge, commentary or modern interpretation.
  If a word is ambiguous, give the most literal natural rendering and mention the alternative in `notes`.
- Translate the whole unit as one flowing statement (verses are often one sentence over two lines). Do not translate word by word.
- Hindi: standard literary Hindi in Devanagari, understandable to a modern reader. No Latin letters in `hindi`.
  Keep proper names and technical terms in Devanagari (e.g. भरद्वाज, इन्द्र, आयुर्वेद, वात, पित्त, कफ).
- English: plain, accurate English. Technical terms may stay in IAST with a short gloss the first time they are needed
  in the chunk (e.g. "doṣa (the bodily humours)").
- Consistent renderings across chunks (use these):
  āyurveda = Āyurveda (the science of life); ṛṣi = sage; maharṣi = great sage; bhagavān = the venerable / blessed;
  āyus = life, lifespan; hita = beneficial; ahita = harmful; sukha = happiness/ease; duḥkha = suffering;
  sāmānya = commonality (sāmānya); viśeṣa = distinctiveness (viśeṣa); guṇa = quality (guṇa); dravya = substance (dravya);
  karma = action (karma); samavāya = inherence (samavāya);
  vāta, pitta, kapha / śleṣman = Vāta, Pitta, Kapha (keep the Sanskrit); doṣa = doṣa; dhātu = dhātu (tissue/constituent);
  rasa = taste (when about the six tastes) or rasa; vipāka, vīrya, prabhāva: keep the Sanskrit with a gloss;
  proper names transliterated (Ātreya, Bharadvāja, Agniveśa, Indra, Śakra, Aśvins, Brahmā, Prajāpati, ...).
- Use "the text states" style only in `notes`, never inside the translation.

## Quality bar
This will be checked word by word by an independent reviewer who sees only the Sanskrit and your output.
Prefer a plain, correct answer over a clever one. Mark real uncertainty with `confidence` and `notes`.

## Self-check before finishing
Run: `python3 -I check_chunk.py chunkK_in.json chunkK_out.json` (from the scratchpad directory) and fix every ERROR.
WARNINGs: read them; fix them if they point to real mistakes.
Reply with: units done, number of text_flags, number of low-confidence units, and anything you could not resolve.

## Chapter 4 specifics (READ)
- Units 8-18 are long lists of Ayurvedic drug names. The source writes the names of each group of ten JOINED TOGETHER with no
  separator inside one token (e.g. 'jīvakarṣabhakau' = jīvaka + ṛṣabhakau; 'madhukamadhuparṇīpṛśniparṇyambaṣṭhakī...').
  Split every token into the individual drug names (one entry per drug in `words`; a drug name that is itself a compound, e.g.
  'kṣīra-kākolī', 'kaṭu-rohiṇī', may be given as one entry with its parts joined by '-').
  Use your knowledge of the standard Caraka Su.4 lists to find the boundaries, and COUNT: every group introduced by
  'daśemāni ... bhavanti' must contain exactly ten drugs (some dual/plural pairs count as two, e.g. 'jīvakarṣabhakau' = jīvaka, ṛṣabhaka;
  'mudgaparṇīmāṣaparṇyau' = mudgaparṇī, māṣaparṇī). If your count is not ten, say so in `notes` (that is a text problem or a boundary doubt).
  In `notes` of such a unit list, per group, the ten names you split (so the reviewer can check the count).
- `gloss` for a drug name: give the literal meaning ONLY when the name is transparent (e.g. kṣīra-kākolī 'milk-kākolī', madhuparṇī 'honey-leaved').
  Otherwise write exactly "drug name" (do NOT identify the plant, do NOT say what it is commonly called, do NOT give any effect).
  `gram` for them: "m./f./n. nom. pl." as the sentence requires, or "drug name" collective as you judge; keep short.
- The footnote-style numerals 1-50 that follow 'bhavanti' in the source have already been removed; ignore them.
- Words such as jīvanīya, bṛṃhaṇīya, lekhanīya... are names of the 50 kaṣāya-vargas (classes of ten drugs): translate them as
  literal meaning (e.g. jīvanīya 'life-giving', bṛṃhaṇīya 'bulk-promoting', lekhanīya 'scraping', bhedanīya 'splitting/breaking up', sandhānīya 'joining/uniting',
  dīpanīya 'kindling digestion') and add the Sanskrit in brackets; do not add effects or uses not in the Sanskrit.
- In the translation of a drug list, give the drug names in their Sanskrit form (Devanagari in Hindi, IAST in English); do not translate them into plant names.
- Technical words: kaṣāya here is the class/kind of decoction-type preparation, 'kaṣāya-yoni' = source of kaṣāya; svarasa, kalka, śṛta, śīta, phāṇṭa
  are the five preparations: keep the Sanskrit names with a short gloss (juice, paste, boiled, cold-infusion, hot-infusion) which is the standard meaning.
- Units 4-18 are printed in parentheses in the SARIT edition; just flag-copy that, nothing to do.
