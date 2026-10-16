#!/usr/bin/env python3
"""Apply the independent reviewers' fixes to the drafts. Drafts (chunkK_out.json) stay untouched;
results go to chunkK_final.json and every change is logged to changes.json."""
import json, copy

S = '/tmp/claude-0/-home-claude-claude-memory/0cac1b21-6382-56bd-abe4-a207ecd1a4f6/scratchpad'
data = {}
for k in range(1, 6):
    for r in json.load(open(f'{S}/chunk{k}_out.json', encoding='utf8')):
        data[r['n']] = (k, r)
log = []


def rec(n):
    return data[n][1]


def setf(n, field, new, why):
    r = rec(n)
    log.append({'n': n, 'field': field, 'old': r.get(field), 'new': new, 'why': why})
    r[field] = new


def rep(n, field, old, new, why):
    r = rec(n)
    assert old in r[field], f'unit {n} {field}: {old!r} not found in {r[field]!r}'
    setf(n, field, r[field].replace(old, new, 1), why)


def app(n, text, why):
    r = rec(n)
    setf(n, 'notes', (r.get('notes', '') + ' ' + text).strip(), why)


def word(n, match, field, new, why):
    hits = []
    for ln in rec(n)['lines']:
        for t in ln['tokens']:
            for w in t['words']:
                if match(w['w']):
                    hits.append(w)
    assert hits, f'unit {n}: word not found'
    w = hits[0]
    log.append({'n': n, 'field': 'word.' + field, 'word': w['w'], 'old': w.get(field), 'new': new, 'why': why})
    w[field] = new


# ---- chunk 1 ----
app('6', "'brahmacarya-vrata' may also be taken as one item ('the vow of celibacy'); the whole compound may alternatively be read as a bahuvrīhi qualifying śarīriṇām.", 'reviewer: missing alternative')
setf('14', 'english', "repositories of the knowledge of Brahman, of self-restraint and of observances, blazing with the radiance of austerity like sacrificial fires receiving oblations,", 'reviewer ERROR: tapasaḥ goes with tejasā; ca closes the list')
setf('14', 'hindi', "जो ब्रह्मज्ञान, दम और नियम के भण्डार थे, और तप के तेज से ऐसे दीप्त थे जैसे आहुति पाती हुई अग्नियाँ —", 'reviewer ERROR: same construal; smoother Hindi')
setf('14', 'notes', "The edition notes the variant 'yamasya' in place of 'damasya' (giving the pair yama–niyama, 'restraints and observances'). 'tapasaḥ' is better taken with 'tejasā' ('the radiance of austerity'), since 'ca' closes the preceding list; it could also be read as a fourth item after 'nidhayaḥ'. 'brahmajñāna' may also be rendered 'sacred (Vedic) knowledge'.", 'reviewer: note completeness')
setf('15', 'hindi', "वे वहाँ सुखपूर्वक बैठे और उन्होंने यह पुण्य चर्चा की — धर्म, अर्थ, काम और मोक्ष का उत्तम मूल आरोग्य है।", "reviewer: cakruḥ is a plain perfect; removed 'began to'")
rep('19', 'hindi', 'ऋषियों ने उन्हीं को नियुक्त किया', 'ऋषियों ने उन्हें नियुक्त किया', 'reviewer: removed emphatic ही')
app('19', "'niyujyeyam' is a non-classical (ārṣa) form: passive stem with active ending; classical Sanskrit would have 'niyujyeya'.", 'reviewer: irregular form')
rep('20', 'english', 'seated amid', 'amid', "reviewer: 'seated' not in the Sanskrit")
rep('20', 'hindi', 'विराजमान', 'स्थित', "reviewer: 'विराजमान' adds 'seated'")
setf('21', 'hindi', "उस बुद्धिमान् (भरद्वाज) ने पास जाकर, विजय के आशीर्वादों से देवताओं के स्वामी का अभिनन्दन करके, विनयपूर्वक ऋषियों का उत्तम वचन कहा —", 'reviewer: two subjects for one verb')
rep('27', 'english', 'wishing to attain long life', 'wishing to make their life long', 'reviewer: cikīrṣantaḥ = wishing to make')
rep('27', 'hindi', 'दीर्घ आयु प्राप्त करने की इच्छा से', 'अपनी आयु को दीर्घ करने की इच्छा से', 'reviewer: same')
rep('29', 'hindi', 'अविनाशी (दीर्घ) जीवन', 'अनश्वर (चिरस्थायी) जीवन', 'reviewer: अविनाशी overstates anitvara')
rep('29', 'english', 'a life that does not pass away quickly', 'a life that is not transient', "reviewer: 'quickly' is interpretation")
# ---- chunk 2 ----
setf('30', 'hindi', "तब मैत्री-परायण पुनर्वसु ने समस्त प्राणियों पर अनुकम्पा के कारण पुण्य आयुर्वेद छह शिष्यों को प्रदान किया।", "reviewer: removed added 'अपने', 'यह'")
setf('34', 'notes', "'puṇyakarmaṇām' is taken as the agent of 'sūtraṇam' (the composition by those of meritorious deeds, i.e. the disciples); it could alternatively qualify 'arthānām'.", 'reviewer: stated alternative was ungrammatical')
app('35', "'sarvabhūtahitaiṣiṇaḥ' may be acc. pl. agreeing with 'tān' (praised them, who wished the welfare of all beings) rather than nom. pl. with 'sarve'.", 'reviewer: ambiguity')
setf('37', 'hindi', "आकाश में प्राणियों द्वारा हर्ष से उच्चारित 'अहो, साधु!' के स्निग्ध और गम्भीर घोष ने तीनों लोकों को गुंजा दिया।", 'reviewer: verb is causative/transitive')
app('37', "The variant anvanādayat (caus. of √nad) gives the more natural sense 'made resound'; anvavādayat as a causative of anu-√vad is possible but unusual.", 'reviewer: say which reading is preferred')
rep('38', 'hindi', 'जल-सहित दिव्य पुष्पों की वर्षा होने लगी', 'जल-सहित पुष्पों की दिव्य वर्षाएँ होने लगीं', 'reviewer: divyāḥ agrees with vṛṣṭayaḥ')
word('41', lambda w: w.startswith('hita-ahita'), 'gram', 'n. nom. sg.; dvandva', 'reviewer: nominative only')
setf('51', 'english', "That in which actions and qualities reside, and which is the inherent cause, is substance (dravya). Quality (guṇa), on the other hand, is an inhering cause that is devoid of movement.", "reviewer: 'also' not in Sanskrit; tu = contrast")
setf('51', 'hindi', "जिसमें कर्म और गुण आश्रित रहते हैं और जो समवायी कारण है, वह द्रव्य है; गुण तो समवायी, चेष्टा-रहित कारण है।", 'reviewer: same')
rep('52', 'hindi', 'कर्म (संयोग-विभाग के लिए) किसी', 'कर्म किसी', 'reviewer: commentary inside translation')
# ---- chunk 3 ----
setf('60', 'english', "Pitta is unctuous (sa-sneha, literally 'with oiliness'), hot, sharp, liquid, sour, flowing and pungent; it is quickly pacified by substances having the opposite qualities.", "reviewer: 'slightly' comes from the commentary")
setf('60', 'hindi', "पित्त स्नेहयुक्त (सस्नेह), उष्ण, तीक्ष्ण, द्रव, अम्ल, सर और कटु है; यह विपरीत गुणों वाले द्रव्यों से शीघ्र शान्त हो जाता है।", 'reviewer: same')
word('60', lambda w: 'sneha' in w and w.startswith('sa'), 'gloss', 'with unctuousness', 'reviewer: literal gloss')
setf('60', 'notes', "sa-sneha literally 'with unctuousness'; commentators take sa- as 'slightly' (īṣat). sara: 'flowing / mobile', also 'laxative'.", 'reviewer: interpretation moved to notes')
rep('63', 'hindi', 'गुण और कर्म फिर से बताए जाएँगे', 'गुण और कर्म (विस्तार से) बताए जाएँगे', 'reviewer: bhūyaḥ = further, not again')
rep('70', 'hindi', 'मलों (कीट) सहित', 'मल (किट्ट) सहित', 'reviewer ERROR: कीट = insect; किट्ट = dross')
setf('70', 'english', "Gold, the five metals with their dross, together with sand (sikatā), lime (sudhā), realgar (manaḥśilā) and orpiment (āla), gems, salt, red ochre (gairika) and collyrium (añjana) —", 'reviewer: sand was left dangling; follows drafter note')
rep('70', 'hindi', 'पाँच लोह (धातुएँ), बालू (सिकता) सहित, सुधा', 'पाँच लोह (धातुएँ), सिकता (बालू), सुधा', 'reviewer: same')
app('70', "'sasikatāḥ' is read here as sand, a separate item; it could alternatively be adjectival ('with sand') with the preceding metals.", 'reviewer: make the choice explicit')
rep('72', 'hindi', 'जिनमें (बिना पुष्प के) फल होते हैं', 'जिनमें फल होते हैं', "reviewer: '(without flowers)' is commentary (minimal edit, not the reviewer's rewrite)")
rep('76', 'english', 'is a true knower of the science', 'is a knower of the science', "reviewer: 'true' not in Sanskrit")
rep('76', 'hindi', 'वही वेद (आयुर्वेद) का ज्ञाता है', 'वह वेद (आयुर्वेद) का ज्ञाता है', 'reviewer: removed emphasis')
rep('81', 'notes', 'that repetition appears to be genuine, since it is needed for the count in verse 85.',
    'that repetition appears to be genuine, since both occurrences are needed: in 81 the four fruits are members of the list (giving 19 with 82 and 83 line 1); in 83 they begin the list of uses (8 for emesis/āsthāpana + 1 nasal = 9, leaving 10 for purgation, as verse 85 states).',
    'reviewer: complete the count reasoning')
word('81', lambda w: 'ikṣvāku' in w, 'gram', 'n. nom. sg. (fruit; stem usu. f.)', 'reviewer: explain gender')
rep('86', 'english', 'Thus the nineteen fruits', 'The nineteen fruits', "reviewer: 'thus' not in Sanskrit")
rep('86', 'hindi', 'इस प्रकार उन्नीस फल', 'उन्नीस फल', 'reviewer: same')
# ---- chunk 4 ----
word('92', lambda w: w == 'me', 'gram', 'gen. sg. pron. (encl.)', 'reviewer: me is never ablative')
setf('93', 'english', "All those that are taught as the principal ones in Ātreya's teaching: sheep's urine, goat's urine, cow's urine, and that of the buffalo,", 'reviewer: sarvāṇi dropped')
rep('98', 'hindi', 'वायु का अनुलोमन करता है', 'मारुत (वात) का अनुलोमन करता है', 'reviewer: term list says वात')
rep('100', 'hindi', 'पित्त का अविरोधी (पित्त को न बढ़ाने वाला)', 'पित्त का अविरोधी (पित्त के प्रतिकूल नहीं)', 'reviewer: literal sense')
word('100', lambda w: 'avirodhi' in w, 'gloss', 'not antagonistic to Pitta', 'reviewer: literal gloss')
setf('111', 'english', "in disorders of the female genital tract (yoni) and of semen, when urine is scanty, and when the faeces are knotted (hard), it is wholesome for those suffering from disorders of Vāta and Pitta.", 'reviewer: genitive says for whom, not an extra item')
setf('111', 'hindi', "योनि और शुक्र के दोषों में, मूत्र के अल्प होने पर, और मल के गाँठदार (कठिन) होने पर (दूध) वात-पित्त के विकारों से पीड़ितों के लिए पथ्य है।", 'reviewer: same')
setf('113', 'english', "The qualities of the milks, in due order and of each one separately, I shall describe further and in full in the chapter (concerned with) food, drink and the rest (annapāna-ādi).", 'reviewer: -ādi dropped')
word('114', lambda w: 'mūlibhiḥ' in w, 'gram', 'm./n. inst. pl. of phalamūlin (dvandva phala-mūla + poss. -in)', 'reviewer: not a dvandva of phalin + mūlin')
# ---- chunk 5 ----
word('118', lambda w: 'vṛkṣān' in w, 'gram', 'saṃkhyā-pūrva karmadhāraya (or ṣaṭ + vṛkṣān), m. acc. pl.', 'reviewer: dvigu label loose')
setf('121', 'english', "No one can know the highest attainment (i.e. the full understanding) of medicinal plants merely by knowing their names, or again by knowing their form.", "reviewer: 'mastery' is interpretation")
setf('121', 'hindi', "केवल नाम के ज्ञान से, अथवा रूप के ज्ञान से भी, कोई औषधियों की परम प्राप्ति (पूर्ण ज्ञान) को नहीं जान सकता।", 'reviewer: same')
rep('122', 'hindi', 'जो उनके प्रयोग (योग) को जानता है', 'किन्तु जो उनके प्रयोग (योग) को जानता है', 'reviewer: tu was left out')
rep('124', 'english', 'not properly known', 'not (properly) known', "reviewer: 'properly' is an addition")
setf('129', 'hindi', "जो अपने को बुद्धिमान मानने वाला (व्यक्ति) औषध को बिना जाने दुःखी, शय्या पर पड़े, श्रद्धा रखने वाले रोगी को (औषध) देता है —", 'reviewer: aside about the text removed')
setf('129', 'english', "He who, thinking himself wise, gives a medicine without knowing it to a sick person who is suffering, bedridden and trusting (in him) —", 'reviewer: same')
setf('131', 'hindi', "साँप का विष पी लेना, अथवा खौलता हुआ (पिघला) ताँबा पी लेना, अथवा अत्यधिक अग्नि में तपाए हुए लोहे के गोले निगल लेना भी अच्छा है —", 'reviewer: aside about the text removed')
setf('131', 'english', "Better to drink a snake's venom or even boiling (molten) copper, or to swallow iron balls heated in an intense fire —", 'reviewer: same')
rep('133', 'notes', 'Line 1 has 16 syllables but an unusual weight pattern in the odd pāda (positions 5-7 G L L); the sense is clear, so no text flag is raised.',
    'Line 1, odd pāda: syllables 5-7 are G L L, a regular bha-vipulā; the metre is sound.', 'reviewer: metre note was wrong')
rep('135', 'hindi', 'सिद्धि (सफलता) ही सभी', 'सिद्धि (सफलता) सभी', 'reviewer: removed emphatic ही')
rep('135', 'hindi', 'और सिद्धि ही सभी', 'और सिद्धि सभी', 'reviewer: same')
app('140', "Alternatively yatra may refer to a person: '(the physician) in whom all the qualities of physicians reside' (cf. vv. 133-135); a reviewer reports commentators read it so, to be checked against Cakrapāṇi.", 'reviewer: alternative construal (attribution unverified)')
rep('140', 'notes', '"pūrvādhyāye" = "in the first chapter" (pūrva = first/foremost; here this very chapter).',
    '"pūrvādhyāye" = literally "in the foremost/preceding chapter", i.e. this first chapter (an interpretation).', 'reviewer: state as interpretation')

# write finals
for k in range(1, 6):
    out = [r for kk, r in data.values() if kk == k]
    json.dump(out, open(f'{S}/chunk{k}_final.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
json.dump(log, open(f'{S}/changes.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('changes applied:', len(log))
