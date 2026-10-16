# Independent review of a drafted chunk (Carakasaṃhitā Sūtrasthāna 4)
Dir: /tmp/claude-0/-home-claude-claude-memory/0cac1b21-6382-56bd-abe4-a207ecd1a4f6/scratchpad/ch4/
You see `chunkK_in.json` (SARIT Sanskrit, a noisy single witness) and the draft `chunkK_out.json`
(sandhi split with gloss/gram per word, Hindi, English, text_flags, notes, confidence). Read BRIEF.md
for the rules the drafter followed. Do not search the web. Do not edit chunkK_out.json.
Check every unit word by word, adversarially:
- split correct (sandhi undone, compounds split, restored forms right), gloss right in context,
  gram label right (case/number/gender/tense/root); wrong case labels and wrong roots are the common errors;
- Hindi and English faithful: nothing added (no interpretation, no 'properly', no emphasis ही unless
  in the Sanskrit), nothing dropped, constructions right (what governs what; which verb ends the sentence),
  no meta-comments inside translations, Hindi has no Latin letters;
- plant/drug/preparation names: no invented identification; where the draft names an identification,
  it must be standard and secure, else it must be left as a name;
- text_flags / typos missed or wrongly raised; notes accurate; confidence honest.
Output: write `chunkK_review.json` in the same directory as
{"units":[{"n":"3","verdict":"ok|fix","issues":[{"field":"english|hindi|notes|gram|gloss|split|text_flags",
"where":"...","problem":"...","fix":"exact replacement text","severity":"error|minor"}]}],"summary":"..."}
(every unit listed). Reply with a 60-word summary: counts of error and minor issues.
