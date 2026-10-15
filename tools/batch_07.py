from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "गुरुशीतमृदुस्निग्धमधुरस्थिरपिच्छिलाः",
    "question": "Which qualities does the verse give to Kapha, and what calms them?",
    "rule": ("Kapha's qualities are heavy, cold, soft, unctuous, sweet, stable "
             "and slimy; they go to rest (are pacified) by opposite qualities."),
    "limits": ("The verse does not list the opposite qualities, and it does "
               "not name the substances that carry them; a word like "
               "'substances' has to be understood from the earlier verses."),
    "explain_hi": ("यह श्लोक श्लेष्मा (कफ) के गुण गिनाता है: गुरु, शीत, मृदु, "
                   "स्निग्ध, मधुर, स्थिर और पिच्छिल। ये सातों नाम एक समास में हैं और ‘गुणाः’ का "
                   "विशेषण हैं। नियम वही है जो वात और पित्त के श्लोकों में था: "
                   "‘विपरीतगुणैः’, यानी उलटे गुणों से, ये गुण ‘प्रशमं यान्ति’ "
                   "(शान्ति को प्राप्त होते हैं)। यहाँ ‘द्रव्यैः’ अलग से नहीं "
                   "लिखा; पिछले श्लोकों से समझा जाता है।"),
    "hook": "कफ के गुण: गुरु-शीत-मृदु-स्निग्ध-मधुर-स्थिर-पिच्छिल → शान्त होते हैं विपरीत गुणों से।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verses 59 and 60 gave qualities of Vāta and Pitta. Which quality do you expect in the list for Kapha?",
            ("गुरु (heavy)", "गुरु opens the list of Kapha's qualities."),
            [("रूक्ष (rough, dry)", "रूक्ष is the first quality of Vāta in verse 59."),
             ("उष्ण (hot)", "उष्ण is a quality of Pitta in verse 60."),
             ("चल (mobile)", "चल is a quality of Vāta in verse 59.")],
            "Kapha's list begins गुरु, शीत, मृदु; the other three words belong to the lists of Vāta and Pitta.",
            "Kapha's qualities: गुरु, शीत, मृदु, स्निग्ध, मधुर, स्थिर, पिच्छिल."),
        match(1, "Match each quality in Kapha's list to its meaning.",
              [["गुरु", "heavy"], ["मृदु", "soft"], ["स्थिर", "stable"],
               ["पिच्छिल", "slimy"]],
              "These four words are among the seven qualities of Kapha.",
              "गुरु = heavy; मृदु = soft; स्थिर = stable; पिच्छिल = slimy."),
        fill(2, "In this verse the quality meaning 'slimy' is ____ (type it in Devanagari).",
             ["पिच्छिलाः", "पिच्छिल"],
             "पिच्छिल is the last quality of the list.",
             "The note on verse 59 gives विशद ('clear, non-slimy') as the opposite of पिच्छिल: Vāta's list and Kapha's list hold a pair of opposites.",
             "पिच्छिल = slimy, the opposite of विशद in Vāta's list."),
        mcq("discriminate", 3, "Which is the right split of विपरीतगुणैर्गुणाः?",
            ("विपरीतगुणैः + गुणाः",
             "A visarga after -ऐ before the voiced ग becomes र्, so विपरीतगुणैः + गुणाः is written विपरीतगुणैर्गुणाः."),
            [("विपरीतगुणैर् + अगुणाः", "The second word is गुणाः, with no initial अ."),
             ("विपरीत + गुणैर्गुणाः", "गुणैर्गुणाः is not a single word."),
             ("विपरीतगुणैः + णाः", "णाः is not a word.")],
            "विपरीतगुणैर्गुणाः = विपरीतगुणैः ('by opposite qualities') + गुणाः ('the qualities').",
            "विपरीतगुणैर्गुणाः = विपरीतगुणैः + गुणाः."),
        mcq("apply", 4,
            "A patient's troubles are heavy, cold and slimy. Whose list of qualities in verses 59-61 do these match?",
            ("Kapha's: गुरु, शीत and पिच्छिल are all in it",
             "All three words stand in the list of verse 61."),
            [("Vāta's: it has the quality शीत", "Vāta's list has शीत but also लघु (light) and विशद (non-slimy), not गुरु or पिच्छिल."),
             ("Pitta's: it has the quality सस्नेह", "Pitta's list has उष्ण (hot), which does not fit cold."),
             ("None, since the lists never share a quality", "Kapha's list holds all three.")],
            "The three qualities together point to Kapha's list in verse 61.",
            "Match a set of qualities to the list that holds them all."),
        mcq("transfer", 5,
            "An invented substance is light, hot and dry. Which doṣa's qualities in verse 61 are these three opposite to?",
            ("Kapha's: light, hot and dry are opposite to heavy, cold and unctuous",
             "These are opposites of गुरु, शीत and स्निग्ध, which stand in Kapha's list."),
            [("Vāta's: it is light and dry too", "Light and dry are Vāta's own qualities (verse 59), not opposites of them."),
             ("Pitta's: it is hot too", "Hot is Pitta's own quality (verse 60), not an opposite."),
             ("Nobody's: only substances with a taste can oppose", "The verse speaks only of opposite qualities.")],
            "Light, hot and dry are the reverse of heavy, cold and unctuous, so the substance stands opposite to Kapha's qualities.",
            "Opposite qualities calm; qualities shared with a list do not make a substance opposite to it.",
            teaches="To test a substance against a doṣa, compare its qualities with that doṣa's list: the verse names opposite qualities as what calms."),
    ],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "विपरीतगुणैर्देशमात्राकालोपपादितैः",
    "question": "Which disorders turn back, by what medicines, and with what care?",
    "rule": ("Disorders regarded as curable (साध्य) are removed by medicines of "
             "opposite qualities, given with due regard to place, dose and time."),
    "limits": ("देश may mean the locality or the patient's body-site; the card "
               "keeps 'place'. The verse speaks only of disorders regarded as "
               "curable and says nothing here about the others."),
    "explain_hi": ("यह श्लोक पिछले तीन श्लोकों का सार बाँधता है: विपरीत गुणों वाले "
                   "भेषज (औषध) विकारों को दूर करते हैं। साथ में शर्त है: औषध "
                   "‘देश, मात्रा और काल’ के अनुसार दी जाए (‘उपपादित’ = ठीक से "
                   "प्रयुक्त)। यह केवल ‘साध्यसंमताः’ विकारों के लिए कहा गया है, "
                   "यानी जो साध्य माने गए हैं। ‘विनिवर्तन्ते’ का अर्थ है लौट "
                   "जाते हैं, हट जाते हैं।"),
    "hook": "विपरीत गुण + देश-मात्रा-काल से दी औषधि → साध्य विकार हटते हैं।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 62 says medicines of opposite qualities remove disorders. Which disorders does it say this about?",
            ("Those regarded as curable (साध्य)",
             "साध्यसंमताः limits the statement to disorders regarded as curable."),
            [("Every disorder without exception", "The word साध्यसंमताः narrows the claim."),
             ("Only the disorders of the mind", "The verse does not mention the mind."),
             ("Only disorders of Vāta", "No single doṣa is named in this verse.")],
            "The verse speaks of विकाराः साध्यसंमताः, disorders regarded as curable.",
            "विकाराः साध्यसंमताः = disorders regarded as curable."),
        match(1, "Match each word of the verse to its meaning.",
              [["देश", "place"], ["मात्रा", "dose"], ["काल", "time"],
               ["भेषजैः", "by medicines"]],
              "Three conditions and the medicine itself carry the verse.",
              "देश = place; मात्रा = dose; काल = time; भेषजैः = by medicines."),
        fill(2, "The verse's word for 'disorders' is ____ (type it in Devanagari).",
             ["विकाराः", "विकार"],
             "विकाराः is the subject of विनिवर्तन्ते.",
             "विकाराः ends in -आः, the nominative plural of a masculine name in -अ: the disorders are the ones that turn back.",
             "विकाराः = disorders (the subject)."),
        mcq("discriminate", 3, "Which is the right split of कालोपपादितैः?",
            ("काल + उपपादितैः", "अ + उ joins as ओ, so काल + उपपादितैः is written कालोपपादितैः."),
            [("कालो + पपादितैः", "पपादितैः is not a word."),
             ("काल + अपपादितैः", "The second word begins with उ (उपपादित), not अ."),
             ("कालोप + पादितैः", "कालोप is not a word.")],
            "कालोपपादितैः = काल ('time') + उपपादितैः ('administered'): given at the right time.",
            "कालोपपादितैः = काल + उपपादितैः."),
        multi("apply", 4, "Which of these does the verse say must be taken into account when giving the medicine?",
              [("The place (देश)", "Right: देश is the first of the three."),
               ("The dose (मात्रा)", "Right: मात्रा is the second."),
               ("The time (काल)", "Right: काल is the third."),
               ("The caste of the patient", "Not in the verse."),
               ("The fee of the physician", "Not in the verse.")],
              [0, 1, 2],
              "देशमात्राकाल names exactly place, dose and time; nothing else is added.",
              "The medicine is given with regard to place, dose and time."),
        mcq("transfer", 5,
            "An invented physician gives a medicine of the right opposite qualities, but in a double dose and in the wrong season. What does verse 62 say is lacking?",
            ("Due regard to dose and time",
             "The verse puts मात्रा and काल beside opposite quality as conditions."),
            [("Opposite qualities in the medicine", "The medicine already has them."),
             ("A medicine at all", "A medicine has been given."),
             ("Nothing: opposite qualities alone are enough", "The verse adds देश, मात्रा and काल after the opposite qualities.")],
            "Right quality is not enough; the verse joins it with place, dose and time.",
            "Opposite qualities + place, dose, time together.",
            teaches="A medicine of the right quality still has to be given in the right measure, time and place, as the verse joins them."),
    ],
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "साधनं न त्वसाध्यानाम्",
    "question": "What does the verse leave out, and what does it promise next?",
    "rule": ("Treatment is not taught for incurable diseases. From here on the "
             "qualities and actions (guṇa and karma) will be stated substance "
             "by substance."),
    "limits": ("The verse does not say why incurable diseases are left out. "
               "भूयः may also mean 'in more detail', and वक्ष्यते can be read "
               "impersonally ('it will be told')."),
    "explain_hi": ("पिछले श्लोक में साध्य रोगों की बात थी; यहाँ पहली पंक्ति सीमा "
                   "बाँधती है: असाध्य व्याधियों का ‘साधन’ (चिकित्सा) नहीं "
                   "बताया जाता। ‘उपदिश्यते’ वर्तमान, कर्मवाच्य है। दूसरी पंक्ति "
                   "आगे का विषय खोलती है: ‘भूयः अतः’, यानी अब आगे ‘यथाद्रव्यम्’ "
                   "प्रत्येक द्रव्य के अनुसार गुण और कर्म ‘वक्ष्यते’ (कहे "
                   "जाएँगे, भविष्यत्)।"),
    "hook": "असाध्य का साधन नहीं बताते · आगे: द्रव्य-द्रव्य के गुण और कर्म।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 62 covered curable disorders. What do you expect verse 63 to say about treatment of incurable diseases?",
            ("It is not taught", "न … उपदिश्यते says treatment is not taught for them."),
            [("A stronger medicine is taught for them", "The verse teaches no treatment for them."),
             ("They are said not to exist", "The verse speaks of them as असाध्य, not as non-existent."),
             ("Their treatment follows in the next verse", "The next announcement is about qualities and actions of substances.")],
            "साधनं न उपदिश्यते असाध्यानां व्याधीनाम्: treatment is not taught for incurable diseases.",
            "असाध्य व्याधि: no treatment taught."),
        match(1, "Match each word of the verse to its meaning.",
              [["साधनम्", "treatment"], ["असाध्यानाम्", "of incurable (ones)"],
               ["व्याधीनाम्", "of diseases"], ["वक्ष्यते", "will be stated"]],
              "These words carry the limit and the promise.",
              "साधनम् = treatment; असाध्यानाम् = of incurable; व्याधीनाम् = of diseases; वक्ष्यते = will be stated."),
        fill(2, "The verse's word for 'treatment' is ____ (type it in Devanagari).",
             ["साधनम्", "साधनं", "साधन"],
             "साधनम् is what is not taught for incurable diseases.",
             "साधनम् ends in -म्: neuter, nominative singular, the subject of उपदिश्यते.",
             "साधनम् = treatment (the subject)."),
        mcq("discriminate", 3, "Which is the right split of न त्वसाध्यानाम्?",
            ("न + तु + असाध्यानाम्", "उ before a vowel becomes व्, so तु + असाध्यानाम् is written त्वसाध्यानाम्."),
            [("न + तु + साध्यानाम्", "The word begins with अ (असाध्य, incurable); this split would turn the meaning round."),
             ("न + त्व + असाध्यानाम्", "The particle is तु ('but'); त्व is only what तु becomes before a vowel."),
             ("नत् + वसाध्यानाम्", "वसाध्यानाम् is not a word.")],
            "न त्वसाध्यानाम् = न ('not') + तु ('but') + असाध्यानाम् ('of the incurable').",
            "त्वसाध्यानाम् = तु + असाध्यानाम्."),
        mcq("apply", 4,
            "उपदिश्यते is present passive; वक्ष्यते is future. What does this say about the two halves of the verse?",
            ("The first half states what the text does not teach; the second promises what it will state",
             "Present 'is taught' (negated) in line 1; future 'will be stated' in line 2."),
            [("Both halves refer to the past", "Neither verb is a past form."),
             ("Both halves promise future teaching", "Line 1 negates a teaching; it is not a promise."),
             ("The first half is future and the second present", "It is the other way round.")],
            "The tenses divide the verse: a limit in the present, a promise for what follows.",
            "Present = what holds in this text; future = what is yet to come."),
        mcq("transfer", 5,
            "An invented teacher says यथाशिष्यं पाठान् दास्यामि. By the pattern of यथाद्रव्यम्, what is his plan?",
            ("To give lessons pupil by pupil, each as suits that pupil",
             "यथा- + a noun = 'according to each X', as यथाद्रव्यम् = substance by substance."),
            [("To give the same lesson to all together", "यथा- + noun means 'according to each', not one lesson for all."),
             ("To teach only one pupil", "The pattern is 'according to each', not 'only one'."),
             ("To give no lessons", "दास्यामि says he will give them.")],
            "यथाद्रव्यम् = substance by substance; so यथाशिष्यम् = according to each pupil.",
            "यथा- + noun = according to each such thing.",
            teaches="A word of the form यथा + noun (यथाद्रव्यम्) means 'according to each X', so you can read similar words you have not met."),
    ],
}

# ---------------------------------------------------------------- unit 64
AUTHORED["64"] = {
    "title": "रसनार्थो रसस्तस्य",
    "question": "What is taste (rasa), what is its material basis, and what causes it?",
    "rule": ("Taste (rasa) is the object of the tongue; its material basis "
             "(dravya) is water and earth; the three beginning with ether "
             "are the causes in its production and its differentiation."),
    "limits": ("The verse does not name the three that begin with ether; the "
               "notes suggest ether, air and fire, but the text does not say "
               "so. निर्वृत्ति and विशेष may also be read together as "
               "'manifestation and variety'."),
    "explain_hi": ("यहाँ से रस का विषय खुलता है। रस ‘रसनार्थः’ है, यानी रसना "
                   "(जिह्वा) का विषय। उसका ‘द्रव्य’ (भौतिक आधार) आपः और क्षिति "
                   "है, यानी जल और पृथ्वी। ‘निर्वृत्ति’ (उत्पत्ति) और ‘विशेष’ "
                   "(भेद) में ‘खादयः त्रयः’, यानी आकाश से आरम्भ होने वाले तीन, "
                   "कारण हैं। उन तीनों के नाम श्लोक में नहीं दिए गए।"),
    "hook": "रस = रसना का विषय · आधार: जल + पृथ्वी · कारण: ख (आकाश) आदि तीन।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Taste (rasa) is the object of one sense organ. Which organ do you expect the verse to name?",
            ("The tongue (रसना)", "रसनार्थः means 'object of the tongue'."),
            [("The eye", "The eye is not named in this verse."),
             ("The ear", "The ear is not named in this verse."),
             ("The skin", "The skin is not named in this verse.")],
            "रसनार्थः रसः: taste is what the tongue takes in.",
            "रसनार्थः = object of the tongue."),
        match(1, "Match each word of the verse to its meaning.",
              [["रसनार्थः", "object of the tongue"], ["द्रव्यम्", "material basis"],
               ["आपः", "water"], ["क्षितिः", "earth"]],
              "These words say what taste is and what it rests on.",
              "रसनार्थः = object of the tongue; द्रव्यम् = material basis; आपः = water; क्षितिः = earth."),
        fill(2, "The verse's word for 'water' is ____ (type it in Devanagari).",
             ["आपः", "आप"],
             "आपः and क्षितिः together are the material basis of taste.",
             "आपः is feminine and plural in form (the gram label is f. nom. pl.) even though it means water.",
             "आपः = water, plural in form."),
        mcq("discriminate", 3, "Which is the right split of रसस्तस्य?",
            ("रसः + तस्य", "A visarga before the unvoiced त becomes स्, so रसः + तस्य is written रसस्तस्य."),
            [("रस + स्तस्य", "स्तस्य is not a word."),
             ("रसो + तस्य", "The ending becomes ो only before a voiced sound; त is unvoiced."),
             ("रसस् + अस्य", "The word is तस्य ('its'), which begins with त.")],
            "रसस्तस्य = रसः ('taste') + तस्य ('its').",
            "रसस्तस्य = रसः + तस्य."),
        multi("apply", 4, "Which of these does the verse give as the material basis (dravya) of taste?",
              [("आपः (water)", "Right: named as the basis."),
               ("क्षितिः (earth)", "Right: named as the basis."),
               ("ख (ether)", "Ether is named only as the first of the three causes of production and differentiation."),
               ("रसना (the tongue)", "The tongue is the organ whose object taste is, not its basis.")],
              [0, 1],
              "द्रव्यम् आपः क्षितिः तथा: water and earth are the basis; the three beginning with ether are the causes.",
              "Basis = water and earth; causes = the three beginning with ether."),
        mcq("transfer", 5,
            "An invented line calls sound श्रवणार्थः (श्रवण = hearing). By the pattern of रसनार्थः, what is sound called?",
            ("The object of hearing",
             "X-अर्थः = object of X, as रसनार्थः = object of the tongue."),
            [("The organ of hearing", "The organ is श्रवण itself; -अर्थः names its object."),
             ("The one who hears", "-अर्थः names the thing perceived, not the hearer."),
             ("The cause of hearing in the ear", "The compound only says sound is what hearing takes in.")],
            "In रसनार्थः the first member is the sense, the second its object; श्रवणार्थः works the same way.",
            "X-अर्थः = the object of X.",
            teaches="In a compound like रसनार्थः the first member names the sense and -अर्थः its object, so you can read similar compounds."),
    ],
}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "स्वादुरम्लो ऽथ लवणः",
    "question": "Which six tastes does the verse list, and in what order?",
    "rule": ("Sweet (स्वादु), sour (अम्ल), salty (लवण), pungent (कटुक), "
             "bitter (तिक्त) and astringent (कषाय): this group of six is "
             "known as the summary (संग्रह) of the tastes."),
    "limits": ("The verse only names the six; it does not describe them or "
               "say what each does. Their effects on the doṣas come in the "
               "verses that follow."),
    "explain_hi": ("छह रसों की गणना: स्वादु (मधुर), अम्ल, लवण, कटुक, तिक्त और "
                   "कषाय। क्रम यही है। ‘षट्कः’ का अर्थ है छह का समूह, और "
                   "‘संग्रहः’ का अर्थ है सार या समूह। ‘स्मृतः’ का अर्थ है "
                   "‘माना गया है’। श्लोक में स्वादु को ही नाम दिया है; हिन्दी "
                   "में इसे मधुर कहते हैं। आगे के श्लोकों में इन्हीं छह की "
                   "बात दोषों के साथ होगी।"),
    "hook": "स्वादु · अम्ल · लवण · कटुक · तिक्त · कषाय: छह रसों का संग्रह।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The verse lists the tastes (rasa). Which of these is one of the six it names?",
            ("तिक्त (bitter)", "तिक्त is the fifth taste of the list."),
            [("उष्ण (hot)", "उष्ण is a quality of Pitta in verse 60, not a taste of this list."),
             ("गुरु (heavy)", "गुरु is a quality of Kapha in verse 61, not a taste."),
             ("द्रव (liquid)", "द्रव is a quality listed for Pitta in verse 60, not a taste.")],
            "The six tastes are स्वादु, अम्ल, लवण, कटुक, तिक्त, कषाय; the other words are qualities (guṇa).",
            "Six tastes; qualities such as उष्ण, गुरु, द्रव are not among them."),
        order(1, "Put the six tastes in the order the verse names them.",
              ["स्वादुः", "अम्लः", "लवणः", "कटुकः", "तिक्तः", "कषायः"],
              "The verse runs sweet, sour, salty, pungent, bitter, astringent.",
              "स्वादु → अम्ल → लवण → कटुक → तिक्त → कषाय."),
        fill(2, "The verse's word for 'bitter' is ____ (type it in Devanagari).",
             ["तिक्तः", "तिक्त"],
             "तिक्तः is the fifth taste, named just before कषायः.",
             "तिक्तः ends in -ः, the nominative singular of a masculine word in -अ (तिक्त).",
             "तिक्त = bitter."),
        mcq("discriminate", 3, "How do the first two words of स्वादुरम्लो ऽथ split before sandhi?",
            ("स्वादुः + अम्लः", "A visarga after -उ before a vowel becomes र्, so स्वादुः + अम्लः is written स्वादुरम्लः; before ऽथ the second word shows as अम्लो."),
            [("स्वादु + रम्लः", "रम्लः is not a word."),
             ("स्वादुर + अम्लः", "The first word is स्वादुः, ending in -उ."),
             ("स्वादु + लम्लः", "There is no ल्; the join is made with र्.")],
            "स्वादुरम्लो = स्वादुः ('sweet') + अम्लः ('sour'), and the -ः of अम्लः becomes ो before the next word's अ.",
            "स्वादुरम्लो = स्वादुः + अम्लः (+ अथ)."),
        mcq("apply", 4,
            "What does the second line say with षट्कोऽयं रसानां संग्रहः स्मृतः?",
            ("This group of six is known as the summary of the tastes",
             "षट्कः = group of six, रसानाम् = of tastes, संग्रहः = summary, स्मृतः = is known."),
            [("Each taste has six varieties", "षट्कः names the group of six tastes, not six varieties of each."),
             ("Each of the six tastes belongs to one doṣa", "The line names no doṣa."),
             ("The six are one taste under six names", "The six are listed as six separate tastes.")],
            "The line closes the list: these six are the summary of tastes.",
            "षट्कः … संग्रहः = a group of six, the summary."),
        mcq("transfer", 5,
            "An invented line ends पञ्चकोऽयं गुणानां संग्रहः. By the pattern of षट्कः, what is a पञ्चकः?",
            ("A group of five",
             "A number + -क names a group of that many, as षट्कः = group of six."),
            [("The fifth one in a list", "The fifth would be a different form; -कः here names the group."),
             ("Five times over", "-कः here makes a group, not a repeat."),
             ("A group of fifty", "पञ्च is five, not fifty.")],
            "षट्कः is six + -क = a group of six; पञ्चकः is five + -क = a group of five.",
            "Number + -क = a group of that number.",
            teaches="A number with -क can name a group of that size, so you can read similar words (षट्कः, पञ्चकः) without a gloss."),
    ],
}

# ---------------------------------------------------------------- unit 66
AUTHORED["66"] = {
    "title": "स्वाद्वम्ललवणा वायुम्",
    "question": "Which three tastes overcome Vāta, Pitta and Kapha?",
    "rule": ("Sweet, sour, salty overcome Vāta; astringent, sweet, bitter "
             "overcome Pitta; astringent, pungent, bitter overcome Kapha."),
    "limits": ("The verse says only 'overcome' (जयन्ति), one verb for all "
               "three groups. It does not say how, nor what the other "
               "tastes do to each doṣa; the converse is the parenthetical "
               "verse that follows."),
    "explain_hi": ("छह रसों को तीन दोषों से जोड़ा गया है, तीन-तीन करके। मधुर, "
                   "अम्ल, लवण वायु को जीतते हैं; कषाय, मधुर, तिक्त पित्त को; "
                   "कषाय, कटु, तिक्त श्लेष्मा को। ‘जयन्ति’ क्रिया एक बार आई "
                   "है और तीनों समूहों के साथ पढ़ी जाती है। ‘कषाय’ और ‘तिक्त’ "
                   "दो सूचियों में हैं (पित्त और कफ); ‘मधुर’ भी दो में है (वात "
                   "और पित्त)।"),
    "hook": "वात: मधुर-अम्ल-लवण · पित्त: कषाय-मधुर-तिक्त · कफ: कषाय-कटु-तिक्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The verse names three tastes for each doṣa. Which doṣa do sweet, sour and salty overcome?",
            ("Vāta", "स्वाद्वम्ललवणाः (sweet, sour, salty) go with वायुम्, Vāta."),
            [("Pitta", "Pitta's tastes are astringent, sweet and bitter."),
             ("Kapha", "Kapha's tastes are astringent, pungent and bitter."),
             ("All three alike", "Each doṣa has its own three tastes.")],
            "Sweet, sour and salty overcome Vāta.",
            "वायु ← स्वादु, अम्ल, लवण."),
        match(1, "Match each group of tastes to what it overcomes.",
              [["स्वाद्वम्ललवणाः", "Vāta"],
               ["कषायस्वादुतिक्तकाः", "Pitta"],
               ["कषायकटुतिक्तकाः", "Kapha"],
               ["जयन्ति", "they overcome"]],
              "Three groups of three tastes, and the one verb they share.",
              "स्वादु-अम्ल-लवण → Vāta; कषाय-स्वादु-तिक्त → Pitta; कषाय-कटु-तिक्त → Kapha; जयन्ति = they overcome."),
        fill(2, "The verb that means overcome, in its plural form, is ____ (type it in Devanagari).",
             ["जयन्ति"],
             "जयन्ति stands once and serves all three groups.",
             "जयन्ति ends in -न्ति, the third person plural: it agrees with the plural groups of tastes, and it is read again with each of them.",
             "जयन्ति = they overcome (one verb for three groups)."),
        mcq("discriminate", 3, "Which is the right split of स्वाद्वम्ललवणाः?",
            ("स्वादु + अम्ल + लवणाः", "उ before a vowel becomes व्, so स्वादु + अम्ल is written स्वाद्वम्ल."),
            [("स्वाद्व + अम्ल + लवणाः", "स्वाद्व is not the word here; the taste is स्वादु."),
             ("स्वाद + वम्ल + लवणाः", "Neither स्वाद nor वम्ल is a taste of the list."),
             ("स्वादु + वम्ल + लवणाः", "वम्ल is not a word; the taste is अम्ल.")],
            "स्वाद्वम्ललवणाः = स्वादु ('sweet') + अम्ल ('sour') + लवणाः ('salty').",
            "स्वाद्वम्ल = स्वादु + अम्ल."),
        multi("apply", 4, "Which tastes overcome both Pitta and Kapha, according to the verse?",
              [("कषाय (astringent)", "Right: in the list of Pitta and in the list of Kapha."),
               ("तिक्त (bitter)", "Right: in the list of Pitta and in the list of Kapha."),
               ("स्वादु (sweet)", "In the lists of Vāta and Pitta, not of Kapha."),
               ("कटु (pungent)", "In the list of Kapha only."),
               ("अम्ल (sour)", "In the list of Vāta only.")],
              [0, 1],
              "Only कषाय and तिक्त appear in both the Pitta line and the Kapha line.",
              "Pitta ∩ Kapha = कषाय, तिक्त."),
        mcq("transfer", 5,
            "An invented line says लवणस्वादुतिक्ताः पित्तं जयन्ति. Compared with verse 66, which taste does not belong in the list for Pitta?",
            ("लवण (salty)", "Salty is not among the three tastes named for Pitta in this verse."),
            [("स्वादु (sweet)", "Sweet is one of Pitta's three tastes."),
             ("तिक्त (bitter)", "Bitter is one of Pitta's three tastes."),
             ("पित्तम् (Pitta)", "The doṣa is the one the line is about; the question is about a taste.")],
            "Pitta's three tastes in verse 66 are कषाय, स्वादु, तिक्त; the line swaps कषाय for salty.",
            "Check each taste against the three the verse names for that doṣa.",
            teaches="You can test any claimed pairing of taste and doṣa by looking it up in the three-taste list the verse gives for that doṣa."),
    ],
}

# --------------------------------------------------------------- unit 66.1
AUTHORED["66.1"] = {
    "title": "कट्वम्ललवणाः पित्तम्",
    "question": "Which tastes aggravate Pitta, Kapha and Vāta?",
    "rule": ("Pungent, sour, salty aggravate Pitta; sweet, sour, salty "
             "aggravate Kapha; pungent, bitter, astringent aggravate "
             "Vāta (samīraṇa)."),
    "limits": ("The edition prints this verse in parentheses, as possibly "
               "interpolated or alternative; it states the converse of verse "
               "66. The text has a slip (स्वद्वम्ल for स्वाद्वम्ल), noted in "
               "the text note."),
    "explain_hi": ("यह कोष्ठक में छपा श्लोक है और श्लोक ६६ का उलटा पक्ष कहता है: "
                   "कौन-से रस दोष को ‘कोपयन्ति’ (कुपित करते) हैं। कटु, अम्ल, "
                   "लवण पित्त को; मधुर, अम्ल, लवण कफ को; कटु, तिक्त, कषाय "
                   "समीरण (वायु) को। यहाँ वायु का नाम ‘समीरण’ आया है, जबकि "
                   "श्लोक ६६ में ‘वायु’ था। एक ही दोष के जीतने वाले और बढ़ाने "
                   "वाले रस छहों को आपस में बाँट देते हैं (तीन और तीन)।"),
    "hook": "कुपित करते हैं: पित्त ← कटु-अम्ल-लवण · कफ ← मधुर-अम्ल-लवण · वात ← कटु-तिक्त-कषाय।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 66 used जयन्ति, 'overcome'. This verse uses कोपयन्ति. What do you expect it to mean?",
            ("They provoke, aggravate", "कोपयन्ति is the causative of √कुप् (to be angry): they provoke, aggravate, the converse of overcoming."),
            [("They overcome again", "That is जयन्ति, the verb of verse 66."),
             ("They digest", "The verb has no sense of digesting."),
             ("They taste", "The verb does not mean tasting.")],
            "The causative of √कुप् means to make angry: they aggravate the doṣa.",
            "कोपयन्ति = they aggravate."),
        match(1, "Match each group of tastes to the doṣa it aggravates in this verse.",
              [["कटु-अम्ल-लवण", "Pitta"], ["स्वादु-अम्ल-लवण", "Kapha"],
               ["कटु-तिक्त-कषाय", "Vāta"], ["कोपयन्ति", "they aggravate"]],
              "Three groups of three tastes, and the verb they share.",
              "कटु-अम्ल-लवण → Pitta; स्वादु-अम्ल-लवण → Kapha; कटु-तिक्त-कषाय → Vāta (समीरण); कोपयन्ति = they aggravate."),
        fill(2, "The word this verse uses for Vāta, instead of वायु, is ____ (type it in Devanagari).",
             ["समीरणम्", "समीरणं", "समीरण"],
             "समीरणम् closes the verse.",
             "समीरणम् ends in -म्, the accusative: Vāta is what is aggravated. The same doṣa can have different names (वायु in verse 66).",
             "समीरण = Vāta."),
        mcq("discriminate", 3, "Which is the right split of कटुतिक्तकषायाश्च?",
            ("कटुतिक्तकषायाः + च", "A visarga before च becomes श्, so कटुतिक्तकषायाः + च is written कटुतिक्तकषायाश्च."),
            [("कटुतिक्तकषाया + श्च", "श्च is not a word."),
             ("कटुतिक्तकषायाः + श्च", "The joining word is च, not श्च."),
             ("कटुतिक्तकषाय + आश्च", "आश्च is not a word.")],
            "कटुतिक्तकषायाश्च = कटुतिक्तकषायाः ('pungent, bitter, astringent') + च ('and').",
            "कटुतिक्तकषायाश्च = कटुतिक्तकषायाः + च."),
        multi("apply", 4, "Which tastes aggravate both Pitta and Kapha, according to this verse?",
              [("अम्ल (sour)", "Right: in the list of Pitta and in the list of Kapha."),
               ("लवण (salty)", "Right: in the list of Pitta and in the list of Kapha."),
               ("कटु (pungent)", "In the lists of Pitta and Vāta, not of Kapha."),
               ("स्वादु (sweet)", "In the list of Kapha only."),
               ("तिक्त (bitter)", "In the list of Vāta only.")],
              [0, 1],
              "Only sour and salty are in both the Pitta line and the Kapha line.",
              "Pitta ∩ Kapha (aggravating) = अम्ल, लवण."),
        mcq("transfer", 5,
            "An invented herb has only the sweet taste. Reading verses 66 and 66.1 together, what do they say it does?",
            ("It overcomes Vāta and Pitta and aggravates Kapha",
             "Sweet is in the lists of Vāta and Pitta in verse 66, and in Kapha's aggravating list here."),
            [("It overcomes all three doṣas", "Sweet aggravates Kapha in this verse."),
             ("It aggravates Vāta and Pitta and overcomes Kapha", "That is the reverse of what the verses say."),
             ("It overcomes Kapha only", "Sweet is not in Kapha's overcoming list in verse 66.")],
            "Look the taste up in every doṣa's list in both verses: sweet overcomes Vāta and Pitta and aggravates Kapha.",
            "One taste can overcome one doṣa and aggravate another.",
            teaches="To read a taste's whole effect, look it up in every doṣa's list in both verses; the same taste can calm one doṣa and aggravate another."),
    ],
}

# ---------------------------------------------------------------- unit 67
AUTHORED["67"] = {
    "title": "किंचिद्दोषप्रशमनम्",
    "question": "Into which three kinds is substance (dravya) divided here?",
    "rule": ("Some substance pacifies the doṣas, some vitiates the dhātus "
             "(tissues), some is regarded as useful in maintaining health: "
             "thus dravya is said to be threefold."),
    "limits": ("The verse gives no examples and does not say which "
               "substance belongs where. It sorts by what a substance does, "
               "not by where it comes from; that is the next verse."),
    "explain_hi": ("नया विषय: द्रव्य। यहाँ द्रव्य को उसके काम के अनुसार तीन "
                   "भागों में बाँटा गया है: कोई दोषों का शमन करता है, कोई "
                   "धातुओं को दूषित करता है, और कोई स्वस्थवृत्त (स्वस्थ व्यक्ति "
                   "की चर्या) में उपयोगी माना गया है। ‘किंचित्’ तीन बार आया "
                   "है, हर बार ‘कोई-सा द्रव्य’। ‘मतम्’ का अर्थ यहाँ ‘उपयोगी "
                   "माना गया’ है। अन्त में ‘त्रिविधम् द्रव्यम् उच्यते’ सार देता "
                   "है।"),
    "hook": "द्रव्य तीन तरह: दोष-शमन · धातु-दूषण · स्वस्थवृत्त में उपयोगी।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 67 sorts substances (dravya) into three kinds. By what do you expect it to sort them?",
            ("By what the substance does",
             "The three kinds are pacifying doṣas, vitiating dhātus, and maintaining health."),
            [("By taste: sweet, sour and the rest", "The tastes were in verses 65-66."),
             ("By origin: animal, plant, earthly", "Origin is the sorting of verse 68, the next verse."),
             ("By the season in which it is gathered", "No season is mentioned.")],
            "The sorting is by function: दोषप्रशमन, धातुप्रदूषण, स्वस्थवृत्ति.",
            "Three kinds of dravya, by what each does."),
        match(1, "Match each word of the verse to its meaning.",
              [["दोषप्रशमनम्", "pacifying the doṣas"],
               ["धातुप्रदूषणम्", "vitiating the dhātus"],
               ["स्वस्थवृत्तौ", "in maintaining health"],
               ["त्रिविधम्", "threefold"]],
              "These four words carry the whole division.",
              "दोषप्रशमनम् = pacifying the doṣas; धातुप्रदूषणम् = vitiating the dhātus; स्वस्थवृत्तौ = in maintaining health; त्रिविधम् = threefold."),
        fill(2, "The verse's word for 'substance' is ____ (type it in Devanagari).",
             ["द्रव्यम्", "द्रव्यं", "द्रव्य"],
             "द्रव्यम् is the subject of उच्यते.",
             "द्रव्यम् is neuter singular, and the repeated किंचित् ('some') is neuter too, agreeing with it.",
             "द्रव्यम् = substance (neuter subject)."),
        mcq("discriminate", 3, "Which is the right split of किंचिद्दोषप्रशमनम्?",
            ("किंचित् + दोषप्रशमनम्", "त् before the voiced द becomes द्, so किंचित् + दोष… is written किंचिद्दोष…."),
            [("किंचि + द्दोषप्रशमनम्", "द्दोषप्रशमनम् is not a word."),
             ("किंचिद् + ओषप्रशमनम्", "The second word begins with द: दोष, not ओष."),
             ("किंचिद्दो + षप्रशमनम्", "षप्रशमनम् is not a word.")],
            "किंचिद्दोषप्रशमनम् = किंचित् ('some') + दोषप्रशमनम् ('pacifying the doṣas').",
            "किंचिद्दोष… = किंचित् + दोष…."),
        mcq("apply", 4,
            "An invented line calls an herb धातुप्रदूषणम्. What does that say about it?",
            ("It vitiates the dhātus (tissues)",
             "धातुप्रदूषणम् = vitiating the dhātus."),
            [("It pacifies the doṣas", "That is दोषप्रशमनम्."),
             ("It helps maintain health", "That is स्वस्थवृत्तौ मतम्."),
             ("It comes from animals", "Origin is not what this word says.")],
            "धातुप्रदूषणम् names the second kind: a substance that vitiates the tissues.",
            "धातुप्रदूषणम् = vitiating the dhātus."),
        mcq("transfer", 5,
            "An invented line reads किंचिद्गुरु किंचिल्लघु किंचिन्मृदु द्रव्यमुच्यते. By the pattern of verse 67, what does it say?",
            ("Some substance is heavy, some light, some soft: one subject sorted into three",
             "Repeated किंचित् gives 'some … some … some', as in verse 67."),
            [("One substance is heavy, light and soft at once", "Repeated किंचित् separates the kinds, it does not merge them."),
             ("Three named substances are described", "No names are given, only किंचित्."),
             ("The substance has no qualities", "Three qualities are named.")],
            "A repeated किंचित् splits one subject (द्रव्यम्) into 'some … some … some'.",
            "किंचित् … किंचित् … किंचित् = some … some … some.",
            teaches="When किंचित् is repeated before one subject, it sorts that subject into groups, as verse 67 sorts द्रव्यम् by what it does."),
    ],
}

# ---------------------------------------------------------------- unit 68
AUTHORED["68"] = {
    "title": "तत् पुनस्त्रिविधं प्रोक्तम्",
    "question": "How is substance divided again, and what list begins?",
    "rule": ("That substance is again declared threefold: animal (जङ्गम), "
             "plant (औद्भिद) and earthly (पार्थिव). Line 2 begins a list: "
             "honeys, cow products, bile, fat, marrow, blood, flesh."),
    "limits": ("This verse does not say whose list line 2 is: it continues in "
               "verse 69, which ends 'are used from animals'. Whether the "
               "second threefold split cuts across the first or divides it "
               "is not stated."),
    "explain_hi": ("द्रव्य का दूसरा तीन-भाग: उत्पत्ति के अनुसार जङ्गम (प्राणिज), "
                   "औद्भिद (वनस्पतिज) और पार्थिव (पृथ्वी से)। ‘जङ्गमौद्भिदपार्थिवम्’ "
                   "एक समाहार द्वन्द्व है; इसमें ‘-औ’ संधि से बना है "
                   "(जङ्गम + औद्भिद), द्विवचन नहीं। दूसरी पंक्ति से सूची शुरू "
                   "होती है: मधु, गोरस, पित्त (प्राणी का पित्त, bile), वसा, मज्जा, असृक् और आमिष। यह "
                   "सूची अगले श्लोक में चलती है, और वहीं बताया गया है कि ये "
                   "जङ्गम से लिए जाते हैं।"),
    "hook": "उत्पत्ति से तीन: जङ्गम · औद्भिद · पार्थिव; आगे सूची: मधु, गोरस, पित्त, वसा, मज्जा, असृक्, आमिष।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 67 sorted substances by function. Verse 68 sorts them again. By what do you expect it to sort?",
            ("By origin: animal, plant, earthly",
             "जङ्गम, औद्भिद, पार्थिव name three sources of substances."),
            [("By taste: sweet, sour and the rest", "The tastes belong to verses 65-66."),
             ("By dose: large, medium, small", "No dose is mentioned in this verse."),
             ("By the season of use", "No season is mentioned in this verse.")],
            "The three words name the animal, plant and earthly sources of substances.",
            "जङ्गम (animal), औद्भिद (plant), पार्थिव (earthly)."),
        match(1, "Match each word of the verse to its meaning.",
              [["जङ्गमम्", "animal"], ["औद्भिदम्", "plant"],
               ["पार्थिवम्", "earthly"], ["त्रिविधम्", "threefold"]],
              "These words give the three sources and the count.",
              "जङ्गम = animal; औद्भिद = plant; पार्थिव = earthly; त्रिविधम् = threefold."),
        fill(2, "The verse's word for 'honeys' is ____ (type it in Devanagari).",
             ["मधूनि", "मधु"],
             "मधूनि opens the list in line 2.",
             "मधूनि is the neuter nominative plural of मधु: the list begins with 'honeys', in the plural.",
             "मधूनि = honeys (neuter plural)."),
        mcq("discriminate", 3, "Which is the right split of तत् पुनस्त्रिविधम्?",
            ("तत् + पुनः + त्रिविधम्", "A visarga before the unvoiced त becomes स्, so पुनः + त्रिविधम् is written पुनस्त्रिविधम्."),
            [("तत् + पुन + स्त्रिविधम्", "स्त्रिविधम् is not a word; the word is त्रिविधम्."),
             ("तत् + पुनस् + रिविधम्", "रिविधम् is not a word."),
             ("तत् + पुनो + त्रिविधम्", "ो appears only before a voiced sound; त is unvoiced.")],
            "पुनस्त्रिविधम् = पुनः ('again') + त्रिविधम् ('threefold').",
            "पुनस्त्रिविधम् = पुनः + त्रिविधम्."),
        mcq("apply", 4,
            "Line 2 lists honeys, cow products, bile, fat, marrow, blood and flesh. Where does the text say what they are?",
            ("Not in this verse: the list continues and verse 69 ends 'used from animals'",
             "Verse 68 breaks off mid-list; जङ्गमेभ्यः प्रयुज्यन्ते comes in verse 69."),
            [("In the word मधूनि itself", "A single item does not name the source."),
             ("In line 1, which calls all of them earthly", "Line 1 only names the three sources."),
             ("In this verse, which says they are plants", "This verse does not say so; the list is completed in verse 69.")],
            "The list is tied to animals only by verse 69; verse 68 begins it without saying whose it is.",
            "A list that continues across verses: read on before assigning it."),
        mcq("transfer", 5,
            "An invented word is रसौषधम्. Is its -औ a dual ending, as in a pair of names?",
            ("No: it comes from रस + औषधम् by sandhi",
             "A final -अ plus a word beginning with औ gives औ; no pair is meant."),
            [("Yes: it names two tastes", "The -औ comes from joining two words; the word is not dual."),
             ("Yes: it names two medicines", "रसौषधम् ends in -म्; a dual would end differently."),
             ("It cannot be told", "Splitting the word shows the sandhi.")],
            "As in जङ्गमौद्भिद = जङ्गम + औद्भिद, the औ arises from अ + औ; check the split before reading it as a dual.",
            "Inside a word, -औ may come from अ + औ sandhi, not from the dual.",
            teaches="Before reading -औ as a dual ending, try splitting the word: अ + औ also gives औ, as in जङ्गमौद्भिद."),
    ],
}

# ---------------------------------------------------------------- unit 69
AUTHORED["69"] = {
    "title": "विण्मूत्रचर्मरेतोस्थिस्नायुशृङ्गनखाः",
    "question": "Which animal products does verse 69 add, and how is the list closed?",
    "rule": ("Feces, urine, skin, semen, bone, sinew, horn, nails, hooves, head "
             "hair, body hair and rocanā: these are used from animals "
             "(जङ्गमेभ्यः), completing the list begun in verse 68."),
    "limits": ("रोचना is usually taken as gorocanā (a concretion of cattle), "
               "but the text says only रोचनाः. This verse is a continuation: "
               "its first half of the list sits in verse 68, line 2."),
    "explain_hi": ("यह श्लोक श्लोक ६८ की सूची पूरी करता है। पहली पंक्ति में आठ नाम "
                   "एक द्वन्द्व में हैं (विट्, मूत्र, चर्म, रेतस्, अस्थि, "
                   "स्नायु, शृङ्ग, नख), फिर ‘खुराः’; दूसरी पंक्ति में ‘केशाः, "
                   "लोमानि, रोचनाः’। सूची का मालिक यहीं बताया गया है: "
                   "‘जङ्गमेभ्यः प्रयुज्यन्ते’, यानी ये प्राणियों से लिए और "
                   "प्रयोग में आते हैं। इसलिए श्लोक ६८ की सूची (मधु से आमिष "
                   "तक) और यह सूची मिलकर जङ्गम द्रव्यों की हैं।"),
    "hook": "श्लोक ६८ की सूची का अन्त: विट्-मूत्र-चर्म-रेतस्-अस्थि-स्नायु-शृङ्ग-नख, खुर, केश, लोम, रोचना → जङ्गम से।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 68 began a list of materials without naming its source. Verse 69 ends जङ्गमेभ्यः प्रयुज्यन्ते. Which source is that?",
            ("Animals (जङ्गम)", "जङ्गमेभ्यः means 'from animals'."),
            [("Plants (औद्भिद)", "The plant source is औद्भिद, not named here."),
             ("The earth (पार्थिव)", "The earthly source is पार्थिव, not named here."),
             ("All three sources together", "The verse names one source.")],
            "जङ्गमेभ्यः is the ablative plural of जङ्गम: the items are used from animals.",
            "जङ्गमेभ्यः = from animals."),
        match(1, "Match each word of the verse to its meaning.",
              [["चर्म", "skin"], ["अस्थि", "bone"], ["शृङ्ग", "horn"],
               ["खुराः", "hooves"]],
              "These four are among the animal products named.",
              "चर्म = skin; अस्थि = bone; शृङ्ग = horn; खुराः = hooves."),
        fill(2, "The verse's word for 'body hair' is ____ (type it in Devanagari).",
             ["लोमानि", "लोम"],
             "लोमानि comes just after केशाः, 'head hair'.",
             "लोमानि is neuter plural (-आनि), while केशाः beside it is masculine plural: the list mixes genders.",
             "लोमानि = body hair (neuter plural)."),
        mcq("discriminate", 3, "How does रेतोस्थि in the first compound split?",
            ("रेतः + अस्थि", "After अ, a visarga before अ becomes ो and the अ is dropped (अः + अ → ोऽ), so रेतः + अस्थि is written रेतोस्थि."),
            [("रेत + उस्थि", "There is no word उस्थि."),
             ("रेतो + स्थि", "स्थि is not a word."),
             ("रेतः + स्थि", "स्थि is not a word; the second word is अस्थि.")],
            "रेतोस्थि = रेतः ('semen') + अस्थि ('bone'); the edition prints it without a mark for the dropped अ.",
            "रेतोस्थि = रेतः + अस्थि."),
        multi("apply", 4, "Which of these are named in verse 69 itself, not in verse 68?",
              [("खुराः (hooves)", "Right: named in verse 69."),
               ("नखाः (nails)", "Right: named in verse 69."),
               ("मधूनि (honeys)", "Named in verse 68, line 2."),
               ("मज्जा (marrow)", "Named in verse 68, line 2.")],
              [0, 1],
              "Hooves and nails are in verse 69; honeys and marrow are in the list's first half in verse 68.",
              "Verse 68 line 2 and verse 69 together form one list."),
        mcq("transfer", 5,
            "An invented line reads वृक्षेभ्यः पत्राणि प्रयुज्यन्ते. By the pattern of जङ्गमेभ्यः प्रयुज्यन्ते, what does it say?",
            ("Leaves are used from trees",
             "The model जङ्गमेभ्यः प्रयुज्यन्ते gives the -एभ्यः word as the source, and the plural nominative names what is used."),
            [("Trees are used from leaves", "The source is the -एभ्यः word, trees."),
             ("Trees are used to make leaves", "The verb is passive and the -एभ्यः word is the source, so trees are not the thing used."),
             ("Trees use leaves", "The verb is passive: things are used, they do not use.")],
            "The -एभ्यः word is the source and the nominative plural is what is used: so leaves from trees.",
            "X-एभ्यः + nominative + प्रयुज्यन्ते = (things) are used from X.",
            teaches="In a line like जङ्गमेभ्यः प्रयुज्यन्ते, the -एभ्यः word is the source and the nominative plural is what is used from it."),
    ],
}


NOTES_HI = {
    "61": "‘श्लेष्मणः’ षष्ठी एकवचन है (श्लेष्मन्, पुल्लिंग), जबकि श्लोक ६६ का ‘श्लेष्माणम्’ द्वितीया एकवचन। ‘विपरीतगुणैर्गुणाः’ में ऐः + ग → ैर्ग (विसर्ग → र्)। ‘द्रव्यैः’ पाठ में नहीं है, पिछले श्लोकों से समझा गया है (डेटा-नोट के अनुसार)। पाठभेद या पाठ-दोष दर्ज नहीं।",
    "62": "‘विपरीतगुणैर्देश…’ में विपरीतगुणैः + देश… (विसर्ग → र्)। ‘कालोपपादितैः’ में काल + उपपादितैः (अ + उ → ओ)। ‘भेषजैर्विनिवर्तन्ते’ में भेषजैः + वि- (विसर्ग → र्)। ‘देश’ का अर्थ स्थान या शरीर-स्थान दोनों हो सकता है; कार्ड ‘स्थान’ रखता है। ‘साध्यसंमताः’ को ‘साध्य माने गए’ पढ़ा गया है।",
    "63": "‘न त्वसाध्यानाम्’ में तु + असाध्यानाम् → त्वसाध्यानाम् (उ → व्)। ‘भूयश्चातो’ में भूयः + च + अतः (विसर्ग + च → श्; अ + अ → आ; फिर अतः + य → अतो य)। ‘वक्ष्यते’ एकवचन है जबकि कर्ता ‘गुणकर्माणि’ बहुवचन; इसे भाववाच्य (‘कहा जाएगा’) भी पढ़ा जा सकता है। ‘भूयः’ का अर्थ ‘विस्तार से’ भी हो सकता है।",
    "64": "‘खादयस्त्रयः’ (ख + आदयः + त्रयः) में तीनों के नाम पाठ में नहीं हैं; टिप्पणी में केवल अनुमान है। ‘निर्वृत्तौ च विशेषे च’ को अलग-अलग (उत्पत्ति और भेद) या साथ (प्रकट होना और भिन्नता) पढ़ा जा सकता है। ‘रसनार्थो’ = रसन + अर्थः (अ + अ → आ; फिर विसर्ग → ओ); ‘रसस्तस्य’ में विसर्ग → स्।",
    "65": "‘स्वादुरम्लो ऽथ’ में स्वादुः + अम्लः (विसर्ग → र्) और अम्लः + अथ → अम्लो ऽथ। ‘कषायश्चेति’ = कषायः + च + इति (विसर्ग + च → श्; अ + इ → ए)। ‘षट्को ऽयम्’ में षट्कः + अयम्। पाठभेद दर्ज नहीं है; कोई सन्देहास्पद पाठ नहीं।",
    "66": "‘स्वाद्वम्ललवणा’ में स्वादु + अम्ल (उ → व्)। ‘वायुं’ और ‘श्लेष्माणं’ द्वितीया एकवचन हैं; ‘जयन्ति’ तीनों समूहों के साथ पढ़ा जाता है। ‘कषायस्वादुतिक्तकाः’ और ‘कषायकटुतिक्तकाः’ में -क- अतिरिक्त प्रत्यय है, अर्थ वही (कषाय, स्वादु, तिक्त)। कोई पाठभेद दर्ज नहीं।",
    "66.1": "यह श्लोक सम्पादित पाठ में कोष्ठक में छपा है (प्रक्षिप्त या वैकल्पिक)। पाठ में ‘स्वद्वम्ललवणाः’ छपा है; ‘स्वादु’ में दीर्घ ‘आ’ चाहिए, इसलिए ‘स्वाद्वम्ललवणाः’ अपेक्षित है (छन्द नहीं बदलता; टंकण की चूक लगती है)। कार्ड सही वर्तनी रखता है। ‘कटुतिक्तकषायाश्च’ = …कषायाः + च (विसर्ग → श्)। ‘समीरणम्’ = वायु।",
    "67": "‘किंचिद्दोषप्रशमनम्’ और ‘किंचिद्धातुप्रदूषणम्’ में किंचित् + द/ध (त् → द् घोष से पहले); ‘किंचित्त्रिविधम्’ में त् + त्र जैसा का तैसा। ‘मतम्’ का भाव ‘उपयोगी माना गया’ है। ‘स्वस्थवृत्तौ’ सप्तमी है: ‘स्वास्थ्य-रक्षा में’। कोई पाठभेद दर्ज नहीं।",
    "68": "यह श्लोक वाक्य के बीच में रुकता है: सूची (मधूनि … आमिषम्) श्लोक ६९ में पूरी होती है। ‘जङ्गमौद्भिदपार्थिवम्’ में -औ संधि से है (अ + औ → औ), द्विवचन नहीं; समाहार द्वन्द्व नपुंसक एकवचन में है। ‘मज्जा ऽसृगामिषम्’ = मज्जा + असृक् + आमिषम् (ऽ अ का लोप)। ‘पुनस्त्रिविधम्’ में विसर्ग → स्। दूसरा तीन-भाग पहले को बाँटता है या काटता है, श्लोक नहीं कहता।",
    "69": "‘रेतोस्थि’ = रेतः + अस्थि; स्रोत में अवग्रह नहीं छपा, समास के भीतर यह चलता है। ‘विण्मूत्र’ में विट् का ट् म् से पहले ण् बना है। ‘रोचनाः’ को गोरोचना माना जाता है, पर पाठ केवल ‘रोचनाः’ कहता है। यह श्लोक ६८ की सूची की निरन्तरता है। अंग्रेज़ी अनुवाद की ‘a yellow concretion’ वाली व्याख्या पाठ से आगे की व्याख्या है।",
}


AIDS = {
    "61": {
        "seesaw": "गुणाः ↔ विपरीतगुणैः: कफ के सात गुण एक पलड़े पर, उनके उलटे गुण दूसरे पर; उलटे से ये शान्त होते हैं। (श्लोक ५९ की वात-सूची में पिच्छिल का उलटा विशद है; यह केवल टिप्पणी है।)",
        "diagram": {"groups": [
            {"label": "कफ के गुण",
             "items": ["गुरु", "शीत", "मृदु", "स्निग्ध", "मधुर", "स्थिर",
                       "पिच्छिल"]},
            {"label": "किसके", "items": ["श्लेष्मणः"]},
            {"label": "क्या होता है", "items": ["प्रशमं यान्ति"]},
            {"label": "किनसे और कर्ता", "items": ["विपरीतगुणैः", "गुणाः"]}]},
        "contrast": "शीत दो सूचियों में है: वात (श्लोक ५९) और कफ (श्लोक ६१); पित्त की सूची में उसकी जगह उष्ण है (श्लोक ६०)। इसलिए अकेला ‘शीत’ पहचान नहीं देता; गुरु या पिच्छिल देखें।",
        "sandhi": "विसर्ग → र् (घोष व्यंजन से पहले): विपरीतगुणैः + गुणाः → विपरीतगुणैर्गुणाः।",
        "chunks": "गुरुशीतमृदुस्निग्ध | मधुरस्थिरपिच्छिलाः ‖ श्लेष्मणः | प्रशमं यान्ति | विपरीतगुणैर्गुणाः।",
    },
    "62": {
        "frame": "किससे: भेषज (विपरीत गुण वाले) · कैसे: देश, मात्रा, काल का ध्यान रखकर · किस पर: साध्य माने गए विकार · फल: विनिवृत्ति (हटना)।",
        "diagram": {"groups": [
            {"label": "औषध के गुण", "items": ["विपरीतगुणैः"]},
            {"label": "कैसे दी, किससे", "items": ["देश", "मात्रा", "काल", "उपपादितैः", "भेषजैः"]},
            {"label": "परिणाम", "items": ["विनिवर्तन्ते", "विकाराः"]},
            {"label": "किनके", "items": ["साध्यसंमताः"]}]},
        "letters": "दे-मा-का: देश, मात्रा, काल (तीन शर्तें, श्लोक के क्रम में)।",
        "sandhi": "अ + उ → ओ: काल + उपपादितैः → कालोपपादितैः · विसर्ग → र् (घोष से पहले): विपरीतगुणैः + देश… → विपरीतगुणैर्देश… · विसर्ग → र् (घोष से पहले): भेषजैः + विनिवर्तन्ते → भेषजैर्विनिवर्तन्ते।",
        "chunks": "विपरीतगुणैर्देशमात्राकालोपपादितैः ‖ भेषजैर्विनिवर्तन्ते | विकाराः | साध्यसंमताः।",
    },
    "63": {
        "diagram": {"groups": [
            {"label": "नहीं बताया जाता", "items": ["साधनं न", "असाध्यानाम्", "व्याधीनाम्", "उपदिश्यते"]},
            {"label": "आगे", "items": ["भूयः", "अतः", "यथाद्रव्यम्", "गुणकर्माणि", "वक्ष्यते"]}]},
        "sandhi": "उ + स्वर → व् + स्वर: तु + असाध्यानाम् → त्वसाध्यानाम् · विसर्ग + च → श्: भूयः + च → भूयश्च।",
        "anchors": "साधन ← √साध् (सिद्ध करना, उपाय) · असाध्य = अ + साध्य (जो साधा न जा सके) · गुणकर्माणि = गुण + कर्म (जोड़ा हुआ द्वन्द्व)।",
        "chunks": "साधनं न | त्वसाध्यानाम् | व्याधीनामुपदिश्यते ‖ भूयश्चातो | यथाद्रव्यं | गुणकर्माणि वक्ष्यते।",
    },
    "64": {
        "frame": "विषय: रस · इन्द्रिय: रसना · आधार (द्रव्य): जल और पृथ्वी · कारण (उत्पत्ति और भेद में): ख आदि तीन।",
        "diagram": {"groups": [
            {"label": "रस क्या है", "items": ["रसनार्थः", "रसः"]},
            {"label": "आधार", "items": ["द्रव्यम्", "आपः", "क्षितिः"]},
            {"label": "कारण", "items": ["निर्वृत्तौ", "विशेषे", "प्रत्ययाः", "खादयः", "त्रयः"]}]},
        "sandhi": "अ + अ → आ: रसन + अर्थः → रसनार्थः (फिर विसर्ग → ओ, घोष र से पहले) · विसर्ग → स् (त से पहले): रसः + तस्य → रसस्तस्य · म् + आ: द्रव्यम् + आपः → द्रव्यमापः।",
        "anchors": "रसनार्थः = रसन + अर्थः (रसना का विषय) · खादयः = ख + आदयः (ख = आकाश, और उससे आरम्भ होने वाले) · निर्वृत्ति = उत्पत्ति, विशेष = भेद।",
        "chunks": "रसनार्थो रसस्तस्य | द्रव्यमापः | क्षितिस्तथा ‖ निर्वृत्तौ च विशेषे च | प्रत्ययाः | खादयस्त्रयः।",
    },
    "65": {
        "chain": {"steps": ["स्वादु (मीठा)", "अम्ल (खट्टा)", "लवण (नमकीन)",
                            "कटुक (चरपरा)", "तिक्त (कड़वा)", "कषाय (कसैला)"]},
        "diagram": {"groups": [
            {"label": "पहली पंक्ति", "items": ["स्वादुः", "अम्लः", "अथ", "लवणः", "कटुकः", "तिक्तः"]},
            {"label": "दूसरी पंक्ति", "items": ["कषायः", "षट्कः", "रसानाम्", "संग्रहः", "स्मृतः"]}]},
        "letters": "स्वा-अ-ल-क-ति-क: स्वादु, अम्ल, लवण, कटुक, तिक्त, कषाय (नामों के पहले अक्षर; मेरा बनाया क्रम-सूत्र)।",
        "sandhi": "विसर्ग → र् (स्वर से पहले): स्वादुः + अम्लः → स्वादुरम्लः · अः + अ → ओ ऽ: अम्लः + अथ → अम्लो ऽथ · विसर्ग + च → श्: कषायः + च → कषायश्च।",
        "chunks": "स्वादुरम्लो ऽथ लवणः | कटुकस्तिक्त एव च ‖ कषायश्चेति | षट्को ऽयं | रसानां संग्रहः स्मृतः।",
    },
    "66": {
        "diagram": {"groups": [
            {"label": "वायु को जीतते", "items": ["स्वादु", "अम्ल", "लवण"]},
            {"label": "पित्त को जीतते", "items": ["कषाय", "स्वादु", "तिक्त"]},
            {"label": "श्लेष्मा को जीतते", "items": ["कषाय", "कटु", "तिक्त"]}]},
        "letters": "वात: स्वा-अ-ल · पित्त: क-स्वा-ति · कफ: क-क-ति (रसों के पहले अक्षर; मेरा बनाया क्रम-सूत्र)।",
        "contrast": "पित्त और कफ की सूचियाँ दो रस साझा करती हैं: कषाय और तिक्त; पित्त में तीसरा स्वादु है, कफ में कटु। वात की सूची में केवल स्वादु पित्त के साथ साझा है।",
        "sandhi": "उ + अ → व् + अ: स्वादु + अम्ल → स्वाद्वम्ल (स्वाद्वम्ललवणाः) · आः + घोष (व) → आ: लवणाः + वायुम् → लवणा वायुम् (विसर्ग लुप्त)।",
        "chunks": "स्वाद्वम्ललवणा वायुं | कषायस्वादुतिक्तकाः ‖ जयन्ति पित्तं | श्लेष्माणं | कषायकटुतिक्तकाः।",
    },
    "66.1": {
        "diagram": {"groups": [
            {"label": "पित्त को कुपित करते", "items": ["कटु", "अम्ल", "लवण"]},
            {"label": "कफ को कुपित करते", "items": ["स्वादु", "अम्ल", "लवण"]},
            {"label": "समीरण (वायु) को कुपित करते", "items": ["कटु", "तिक्त", "कषाय"]}]},
        "contrast": "वही दोष, दो श्लोक: वात को जीतते हैं स्वादु-अम्ल-लवण (६६), कुपित करते हैं कटु-तिक्त-कषाय (६६.१); पित्त और कफ के लिए भी दोनों सूचियाँ मिलकर छहों रस बाँटती हैं।",
        "anchors": "कोपयन्ति ← √कुप् (क्रोध करना, कुपित होना; णिच् से ‘कुपित कराना’) · कोप = क्रोध · समीरण = वायु (श्लोक ६६ में ‘वायु’)।",
        "sandhi": "विसर्ग + च → श्: कटुतिक्तकषायाः + च → कटुतिक्तकषायाश्च · उ + अ → व्: कटु + अम्ल → कट्वम्ल।",
        "chunks": "कट्वम्ललवणाः पित्तं | स्वाद्वम्ललवणाः कफम् ‖ कटुतिक्तकषायाश्च | कोपयन्ति | समीरणम्।",
    },
    "67": {
        "frame": "क्या: द्रव्य · कितनी तरह: तीन · किस आधार पर: काम के अनुसार (दोष-शमन, धातु-दूषण, स्वस्थवृत्त में उपयोगी)।",
        "diagram": {"groups": [
            {"label": "पहला", "items": ["किंचित्", "दोषप्रशमनम्"]},
            {"label": "दूसरा", "items": ["किंचित्", "धातुप्रदूषणम्"]},
            {"label": "तीसरा", "items": ["स्वस्थवृत्तौ", "मतम्", "किंचित्"]},
            {"label": "सार", "items": ["त्रिविधम्", "द्रव्यम्", "उच्यते"]}]},
        "letters": "दो-धा-स्व: दोषप्रशमन, धातुप्रदूषण, स्वस्थवृत्ति (तीनों के पहले अक्षर; मेरा बनाया क्रम-सूत्र)।",
        "sandhi": "त् → द् (घोष व्यंजन से पहले): किंचित् + दोष… → किंचिद्दोष…; किंचित् + धातु… → किंचिद्धातु… · त् + त्र: किंचित् + त्रिविधम् → किंचित्त्रिविधम् (त् जैसा का तैसा)।",
        "contrast": "श्लोक ६७ में तीन भाग काम के अनुसार हैं (दोष-शमन, धातु-दूषण, स्वस्थवृत्त); श्लोक ६८ में तीन भाग उत्पत्ति के अनुसार (जङ्गम, औद्भिद, पार्थिव)। दो अलग छँटाइयाँ।",
        "chunks": "किंचिद्दोषप्रशमनं | किंचिद्धातुप्रदूषणम् ‖ स्वस्थवृत्तौ मतं किंचित् | त्रिविधं द्रव्यमुच्यते।",
    },
    "68": {
        "diagram": {"groups": [
            {"label": "उत्पत्ति से तीन", "items": ["जङ्गम", "औद्भिद", "पार्थिवम्"]},
            {"label": "सूची शुरू", "items": ["मधूनि", "गोरसाः", "पित्तं", "वसा", "मज्जा", "असृक्", "आमिषम्"]}]},
        "pegs": "मेरा बनाया चित्र: जङ्गम = चलता हुआ पशु · औद्भिद = धरती से उगता अंकुर · पार्थिव = मिट्टी का ढेला। तीनों एक पंक्ति में खड़े।",
        "anchors": "जङ्गम ← √गम् (चलने वाला) · औद्भिद ← उद्भिद (उगने वाला) · पार्थिव ← पृथिवी (धरती) · त्रिविध = त्रि + विध (तीन तरह का)।",
        "sandhi": "अ + औ → औ: जङ्गम + औद्भिद → जङ्गमौद्भिद (द्विवचन नहीं) · विसर्ग → स् (त से पहले): पुनः + त्रिविधम् → पुनस्त्रिविधम् · आ + अ → आ: मज्जा + असृक् → मज्जा ऽसृक्।",
        "chunks": "तत् पुनस्त्रिविधं प्रोक्तं | जङ्गमौद्भिदपार्थिवम् ‖ मधूनि गोरसाः पित्तं | वसा मज्जा ऽसृगामिषम्।",
    },
    "69": {
        "frame": "क्या: जंगम द्रव्यों की सूची का अन्त · कहाँ से: जङ्गमेभ्यः (प्राणियों से) · क्या होता है: प्रयुज्यन्ते (प्रयोग में लिए जाते हैं) · शुरू कहाँ: श्लोक ६८ पंक्ति २।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["विट्", "मूत्र", "चर्म", "रेतः", "अस्थि", "स्नायु",
                       "शृङ्ग", "नख", "खुराः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["जङ्गमेभ्यः", "प्रयुज्यन्ते", "केशाः", "लोमानि",
                       "रोचनाः"]}]},
        "anchors": "जङ्गमेभ्यः ← जङ्गम (श्लोक ६८) · प्रयुज्यन्ते ← प्र + √युज् (प्रयोग) · केश = सिर के बाल, लोम = शरीर के बाल।",
        "sandhi": "विसर्ग → ओ (अ से पहले), अ का लोप: रेतः + अस्थि → रेतोस्थि · ट् → ण् (नासिक्य म से पहले): विट् + मूत्र → विण्मूत्र।",
        "chunks": "विण्मूत्रचर्मरेतोस्थि | स्नायुशृङ्गनखाः खुराः ‖ जङ्गमेभ्यः प्रयुज्यन्ते | केशा लोमानि रोचनाः।",
    },
}

IMAGE_SPECS = {
    ("65", "chain"): {
        "file": "six-tastes-65.svg",
        "alt": "A vertical chain of six boxes, the six tastes in the order of the verse: sweet, sour, salty, pungent, bitter, astringent",
        "type": "chain",
        "title": "छह रस, श्लोक के क्रम में",
        "steps": ["स्वादु (मीठा)", "अम्ल (खट्टा)", "लवण (नमकीन)",
                  "कटुक (चरपरा)", "तिक्त (कड़वा)", "कषाय (कसैला)"],
    },
}
