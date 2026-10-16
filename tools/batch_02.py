from ch1_authored import mcq, match, order, fill, multi

"""Units 11-20 of Charaka Samhita Su. 1."""

AUTHORED = {}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "साङ्कृत्यो बैजवापिश्च",
    "question": "Which sages does verse 11 add, and what does उभौ say about the last pair?",
    "rule": ("Sāṅkṛtya, Baijavāpi, Kuśika, Bādarāyaṇa, Baḍiśa, Śaraloman, and "
             "both Kāpya and Kātyāyana. The dual -औ plus उभौ ('both') marks the "
             "last two as a pair."),
    "limits": ("The verse only lists names; it says nothing about who these "
               "sages were. The data records no variant readings for this verse."),
    "explain_hi": ("सूची का यह श्लोक छह एकल नामों से चलता है: साङ्कृत्य, बैजवापि, "
                   "कुशिक, बादरायण, बडिश, शरलोमा। अन्त में ‘काप्यकात्यायनौ’ "
                   "द्विवचन का जोड़ा है और उसके बाद ‘उभौ’ (दोनों) उसी जोड़े पर "
                   "बल देता है। ‘काप्यकात्यायनौ + उभौ’ जुड़कर "
                   "‘काप्यकात्यायनावुभौ’ बनता है: औ स्वर से पहले ‘आव्’ हो जाता है।"),
    "hook": "छह अकेले नाम, फिर जोड़ा: साङ्कृत्य · बैजवापि · कुशिक · बादरायण | बडिश · शरलोमा · काप्य–कात्यायन (उभौ = दोनों)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 11 ends …कात्यायनावुभौ. उभौ is a dual word. What do you expect it to say about Kāpya and Kātyāyana?",
            ("That both of them are meant, as a pair",
             "A dual word names exactly two; here it stresses the pair Kāpya and Kātyāyana."),
            [("That only Kāpya is meant",
              "The pair काप्यकात्यायनौ names both; उभौ does not narrow it."),
             ("That many more sages follow them",
              "A dual word is for two, not for many."),
             ("That they are not in the list",
              "They are named in this very line.")],
            "उभौ means 'both' and underlines the pair Kāpya and Kātyāyana.",
            "उभौ = both (two)."),
        match(1, "Match each Devanagari name to its Latin spelling.",
              [["साङ्कृत्यः", "Sāṅkṛtya"], ["बैजवापिः", "Baijavāpi"],
               ["कुशिकः", "Kuśika"], ["बादरायणः", "Bādarāyaṇa"]],
              "Reading these four names of line 1 in Devanagari is the point of this card.",
              "साङ्कृत्यः = Sāṅkṛtya; बैजवापिः = Baijavāpi; कुशिकः = Kuśika; बादरायणः = Bādarāyaṇa."),
        fill(2, "The word that means 'both' in the last line is ____ (type it in Devanagari).",
             ["उभौ"],
             "उभौ closes the verse.",
             "उभौ is a dual word, 'both'. After a dvandva already in the dual (काप्यकात्यायनौ) it stresses that these two are meant together.",
             "उभौ = both, a dual word."),
        mcq("discriminate", 3, "Which is the right split of काप्यकात्यायनावुभौ?",
            ("काप्यकात्यायनौ + उभौ",
             "The ending -औ turns into आव् before a vowel, so काप्यकात्यायनौ + उभौ is written काप्यकात्यायनावुभौ."),
            [("काप्यकात्यायन + आवुभौ", "आवुभौ is not a word."),
             ("काप्यकात्यायना + वुभौ", "वुभौ is not a word."),
             ("काप्यकात्यायनाव् + उभौ", "A bare ending in -व् does not stand as a word.")],
            "काप्यकात्यायनावुभौ = काप्यकात्यायनौ (Kāpya and Kātyāyana) + उभौ (both).",
            "औ + a vowel → आव् + the vowel."),
        multi("apply", 4, "Which of these are single names (not pairs) in verse 11?",
              [("कुशिकः", "Right: one name, with -ः."),
               ("काप्यकात्यायनौ", "A pair: the -औ ending names two."),
               ("बडिशः", "Right: one name, with -ः."),
               ("शरलोमा", "Right: Śaraloman is labelled nominative singular, one person.")],
              [0, 2, 3],
              "Only काप्यकात्यायनौ is a dual pair; the others are single names.",
              "-ः (or nominative singular) = one sage; -औ = two."),
        mcq("transfer", 5,
            "A new line reads वसिष्ठकश्यपावुभौ. By the rule of verse 11, what does it say?",
            ("Both Vasiṣṭha and Kaśyapa",
             "वसिष्ठकश्यपौ + उभौ joins as वसिष्ठकश्यपावुभौ: a pair, stressed by उभौ."),
            [("Vasiṣṭha only", "The dual -औ names both names in the compound."),
             ("Vasiṣṭha, Kaśyapa and one more sage", "A dual is for two, not three."),
             ("Kaśyapa taught Vasiṣṭha", "Nothing here speaks of teaching; it only joins two names.")],
            "The same joining works for any dual pair followed by उभौ.",
            "Dual pair in -औ + उभौ → ...आवुभौ, 'both of them'.",
            teaches="When you meet ...आवुभौ, undo it as ...औ + उभौ and read it as 'both of the two named'."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "काङ्कायनः कैकशेयो",
    "question": "Which sages does verse 12 add, and how do the visarga joins work?",
    "rule": ("Kāṅkāyana, Kaikaśeya, Dhaumya, Mārīca and Kāśyapa, Śarkarākṣa, "
             "Hiraṇyākṣa, Lokākṣa, and also Paiṅgi. अः turns to ओ before "
             "a voiced consonant; इः before a vowel gives इर्."),
    "limits": ("मारीचकाश्यपौ is dual, so two persons; the notes say the pair "
               "is sometimes understood as one, Mārīci Kāśyapa. The -अक्ष "
               "names are left unsplit as proper names."),
    "explain_hi": ("पहली पंक्ति में तीन एकल नाम और एक जोड़ा है: काङ्कायन, कैकशेय, "
                   "धौम्य, और ‘मारीचकाश्यपौ’ (द्विवचन)। दूसरी पंक्ति में "
                   "तीन नाम -अक्ष पर समाप्त होते हैं: शर्कराक्ष, हिरण्याक्ष, "
                   "लोकाक्ष; फिर पैङ्गि। संधि देखें: ‘कैकशेयः’ घोष ‘ध’ से पहले "
                   "‘कैकशेयो’ बनता है; ‘पैङ्गिः + एव’ में इ के बाद विसर्ग स्वर से पहले "
                   "‘र्’ बनकर ‘पैङ्गिरेव’ हो जाता है।"),
    "hook": "का-कै-धौ-मा | श-हि-लो-पै; तीन -अक्ष नाम (शर्कर–हिरण्य–लोक) और अन्त में पैङ्गिरेव च।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Three names in line 2 of verse 12 end in -अक्ष. Which of these is one of them?",
            ("हिरण्याक्षः", "It ends in -अक्ष: Hiraṇyākṣa is in line 2."),
            [("धौम्यः", "Dhaumya ends in -य, and it is in line 1."),
             ("पैङ्गिः", "Paiṅgi ends in -इ."),
             ("कैकशेयः", "Kaikaśeya ends in -य, and it is in line 1.")],
            "शर्कराक्षः, हिरण्याक्षः and लोकाक्षः are the three -अक्ष names.",
            "Line 2 begins with three names in -अक्ष."),
        order(1, "Put these four names in the order of verse 12.",
              ["कैकशेयः", "धौम्यः", "शर्कराक्षः", "लोकाक्षः"],
              "Line 1 gives कैकशेयः then धौम्यः; line 2 gives शर्कराक्षः before लोकाक्षः.",
              "कैकशेय → धौम्य → शर्कराक्ष → लोकाक्ष."),
        fill(2, "पैङ्गिः + एव is written पैङ्गिरेव. Before the vowel ए, the visarga after इ turns into ____ (type it in Devanagari).",
             ["र्", "र"],
             "The visarga becomes र् before a vowel.",
             "After इ (or उ) a visarga followed by a vowel becomes र्: पैङ्गिः + एव → पैङ्गिरेव. Verse 6 (प्रादुः + भूताः → प्रादुर्भूताः) shows the same र् before a voiced consonant.",
             "Visarga after इ/उ + vowel → र्."),
        mcq("discriminate", 3, "Why is कैकशेयः written कैकशेयो before धौम्यः?",
            ("अः becomes ओ before a voiced consonant, here ध",
             "Visarga after अ turns into ओ before voiced consonants such as ध."),
            [("Because कैकशेयो is a dual form", "It is not dual; the ending is simply sandhi."),
             ("Because ध drops out of धौम्यः", "धौम्यः keeps its ध."),
             ("Because a visarga always becomes ओ", "Before च it becomes श्, and after इ before a vowel it becomes र्.")],
            "कैकशेयः + धौम्यः → कैकशेयो धौम्यः (अः → ओ before the voiced ध).",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "Which word in line 1 has the dual ending -औ?",
            ("मारीचकाश्यपौ", "Right: the dual -औ (the notes say it may also be read as one name)."),
            [("काङ्कायनः", "Single name, with -ः."),
             ("कैकशेयो", "Single name; the -ओ comes from the visarga."),
             ("धौम्यो", "Single name; the -ओ comes from the visarga, although it contains औ inside.")],
            "Only मारीचकाश्यपौ ends in the dual -औ.",
            "A name ending in -औ is a pair; -ो from a visarga is not."),
        mcq("transfer", 5,
            "Join अग्निः + एव (अग्नि = fire) by the rule of पैङ्गिरेव. What results?",
            ("अग्निरेव", "After इ, the visarga becomes र् before the vowel ए."),
            [("अग्निएव", "A visarga before a vowel after इ does not simply vanish; it becomes र्."),
             ("अग्निओव", "ओ comes from अः before a voiced consonant, not here."),
             ("अग्निश्चैव", "श् appears only before च.")],
            "The same rule works for any word in -इः before a vowel.",
            "इः + vowel → इर् + vowel.",
            teaches="You can join and split any word ending in -इः or -उः before a vowel: the visarga turns into र्."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "शौनकः शाकुनेयश्च",
    "question": "Who closes the list in verse 13, and which of them are groups?",
    "rule": ("Śaunaka, Śākuneya, Maitreya, Maimatāyani, the Vaikhānasas, the "
             "Vālakhilyas, and likewise other great sages. The -आः plurals "
             "name groups, not single persons."),
    "limits": ("The notes call the Vaikhānasas and Vālakhilyas groups of "
               "ascetics. The verse says nothing more about them. The list "
               "ends with 'other great sages' without names."),
    "explain_hi": ("चार एकल नामों के बाद दो समूह आते हैं: ‘वैखानसाः’ और "
                   "‘वालखिल्याः’, दोनों बहुवचन। पाठ-टिप्पणी के अनुसार ये तपस्वियों के "
                   "समूह हैं, एक-एक व्यक्ति नहीं। अन्त में ‘अन्ये महर्षयः’ "
                   "(अन्य महर्षि) बिना नाम के आते हैं। संधि: ‘महा + ऋषयः’ "
                   "जुड़कर ‘महर्षयः’ बनता है (आ + ऋ → अर्)।"),
    "hook": "चार नाम, फिर दो समूह (वैखानस · वालखिल्य), फिर ‘अन्य महर्षि’: एकवचन ↔ बहुवचन।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 13 names a few sages and then some groups. Which of these is a group?",
            ("वैखानसाः (the Vaikhānasas)", "The plural -आः names a group of ascetics, not one person."),
            [("शौनकः", "A single name, with -ः."),
             ("मैत्रेयः", "A single name."),
             ("मैमतायनिः", "A single name, with -इः.")],
            "वैखानसाः and वालखिल्याः are plural groups.",
            "The plural -आः names a group."),
        match(1, "Match each word of line 2 to its meaning.",
              [["वैखानसाः", "the Vaikhānasas (a group)"],
               ["वालखिल्याः", "the Vālakhilyas (a group)"],
               ["अन्ये", "other"], ["महर्षयः", "great sages"]],
              "Line 2 moves from named groups to unnamed 'other great sages'.",
              "वैखानसाः and वालखिल्याः = groups; अन्ये = other; महर्षयः = great sages."),
        fill(2, "महा + ऋषयः is written महर्षयः. The आ + ऋ turn into ____ (type it in Devanagari).",
             ["अर्", "अर"],
             "आ + ऋ become अर्.",
             "When अ or आ meets ऋ they join as अर्: महा + ऋषयः → महर्षयः. The same happens in सुर + ऋषि → सुरर्षि in verse 20.",
             "अ/आ + ऋ → अर्."),
        mcq("discriminate", 3, "Which is the right split of वालखिल्यास्तथा?",
            ("वालखिल्याः + तथा",
             "A visarga before त becomes स्, so वालखिल्याः + तथा is written वालखिल्यास्तथा."),
            [("वालखिल्या + स्तथा", "स्तथा is not a word."),
             ("वालखिल्य + आस्तथा", "आस्तथा is not a word."),
             ("वालखिल्यास् + तथा", "A bare -स् does not stand as a word-ending; the real ending is the visarga.")],
            "वालखिल्यास्तथा = वालखिल्याः (the Vālakhilyas) + तथा (likewise).",
            "Visarga + त → स् + त."),
        multi("apply", 4, "Which of these words are plural, naming more than one person?",
              [("वैखानसाः", "Right: plural, a group."),
               ("शाकुनेयः", "A single name, with -ः."),
               ("वालखिल्याः", "Right: plural, a group."),
               ("महर्षयः", "Right: plural, 'great sages'.")],
              [0, 2, 3],
              "Three words are plural; शाकुनेयः is one person.",
              "-आः / -अयः plurals name several persons; -ः on a name in -अ is one."),
        mcq("transfer", 5,
            "Join ऋषयः + तथा (ऋषि = sage) by the rule of वालखिल्यास्तथा. What results?",
            ("ऋषयस्तथा", "A visarga before त becomes स्."),
            [("ऋषयोतथा", "ओ appears before voiced consonants; त is unvoiced."),
             ("ऋषयश्तथा", "श् appears only before च."),
             ("ऋषयरतथा", "र् appears before vowels or voiced consonants, not before त.")],
            "The same rule works for any word in a visarga before त.",
            "Visarga + त → स्त.",
            teaches="Any word ending in a visarga followed by त joins with स्: the visarga becomes स्."),
    ],
}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "ब्रह्मज्ञानस्य निधयो",
    "question": "What are the sages repositories of, and what are they compared to?",
    "rule": ("The sages are 'repositories of the knowledge of Brahman, of "
             "self-restraint and of observances', blazing with the radiance of "
             "austerity like fires fed with oblations."),
    "limits": ("The edition notes the variant यमस्य for दमस्य. तपसः is best "
               "taken with तेजसा, but could be a fourth item after निधयः. "
               "ब्रह्मज्ञान may also mean sacred (Vedic) knowledge."),
    "explain_hi": ("यह श्लोक ऋषियों का वर्णन है, कोई क्रिया नहीं देता। वे "
                   "‘निधयः’ (भण्डार) हैं तीन चीज़ों के: ब्रह्मज्ञान के, दम के और "
                   "नियम के। फिर उनकी उपमा है: तप के तेज से वे ऐसे दीप्त हैं जैसे "
                   "आहुति पाती हुई अग्नियाँ (हूयमाना इवाग्नयः)। पाठभेद ‘यमस्य’ भी "
                   "नोट है; ‘तपसः’ को ‘तेजसा’ के साथ पढ़ना अधिक स्वाभाविक है, "
                   "पर यह दो तरह से पढ़ा जा सकता है।"),
    "hook": "भण्डार: ब्रह्मज्ञान · दम · नियम; तप के तेज से दीप्त, आहुति पाती अग्नियों जैसे।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 14 compares the sages to something blazing. What?",
            ("Sacrificial fires being fed oblations", "The verse says हूयमाना इवाग्नयः: like fires receiving oblations."),
            [("Rivers in flood", "No river appears in the verse."),
             ("Stars in the sky", "No star appears in the verse."),
             ("Kings on thrones", "No king appears in the verse.")],
            "The comparison is इव अग्नयः, 'like fires', fed with oblations.",
            "The sages blaze like fires receiving oblations."),
        match(1, "Match each word of verse 14 to its meaning.",
              [["निधयः", "repositories"], ["दमस्य", "of self-restraint"],
               ["नियमस्य", "of observances"], ["तेजसा", "with radiance"]],
              "These words say what the sages hold and what makes them blaze.",
              "निधयः = repositories; दमस्य = of self-restraint; नियमस्य = of observances; तेजसा = with radiance."),
        fill(2, "The word for 'blazing' in line 2 is ____ (type it in Devanagari).",
             ["दीप्ताः", "दीप्ता"],
             "दीप्ताः comes from √दीप्, 'to blaze'.",
             "दीप्ताः is a past participle from √दीप् in the nominative plural, agreeing with निधयः: the sages are the ones who blaze.",
             "दीप्ताः = blazing (nominative plural)."),
        mcq("discriminate", 3, "Which is the right split of तपसस्तेजसा?",
            ("तपसः + तेजसा",
             "A visarga before त becomes स्, so तपसः + तेजसा is written तपसस्तेजसा."),
            [("तपस + स्तेजसा", "स्तेजसा is not a word."),
             ("तपसस् + तेजसा", "The ending is a visarga, not a bare स्."),
             ("तपसा + स्तेजसा", "स्तेजसा is not a word, and तपसा is a different ending.")],
            "तपसस्तेजसा = तपसः (of austerity) + तेजसा (with radiance).",
            "Visarga + त → स् + त."),
        multi("apply", 4, "Which words name things the sages are 'repositories of'?",
              [("ब्रह्मज्ञानस्य", "Right: of the knowledge of Brahman."),
               ("दमस्य", "Right: of self-restraint."),
               ("अग्नयः", "No: the fires are the thing they are compared to."),
               ("नियमस्य", "Right: of observances.")],
              [0, 1, 3],
              "Three genitives name what they hold; the fires are only the comparison.",
              "X-स्य + निधयः = repositories of X."),
        mcq("transfer", 5,
            "A new phrase reads ज्ञानस्य निधयः. By the pattern of verse 14, what does it mean?",
            ("The repositories of knowledge",
             "X-स्य names what is held, and निधयः is plural: repositories."),
            [("Knowledge of the repositories", "That would need the endings the other way round."),
             ("A single repository for knowledge", "निधयः is plural."),
             ("Knowledge that comes from repositories", "The genitive -स्य means 'of', not 'from'.")],
            "The genitive -स्य before निधयः names what the repositories hold.",
            "X-स्य + निधयः = repositories of X.",
            teaches="You can read a phrase 'X-स्य निधयः' as 'repositories of X' for any X."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "सुखोपविष्टास्ते तत्र",
    "question": "What does the sages' discussion begin by saying about health?",
    "rule": ("Seated at ease, they held a holy discussion: health is the "
             "supreme root of dharma, artha, kāma and mokṣa."),
    "limits": ("The quoted speech begins in line 2 of this verse and runs "
               "into the first line of verse 17. The verse only states that "
               "health is the root; the next verse says what threatens it."),
    "explain_hi": ("ऋषि वहाँ सुख से बैठे और उन्होंने यह पुण्य चर्चा की। चर्चा का "
                   "पहला कथन यह है: धर्म, अर्थ, काम और मोक्ष का उत्तम मूल "
                   "आरोग्य है। ‘सुखोपविष्टाः’ = सुख + उपविष्टाः (अ + उ → ओ)। "
                   "‘ते’ का अर्थ वे ही ऋषि हैं जो श्लोक ७ से १४ तक एकत्र हुए "
                   "बताए गए। यहाँ से ऋषियों का सीधा कथन (उद्धरण) शुरू होता है, "
                   "जो श्लोक १७ की पहली पंक्ति तक चलता है।"),
    "hook": "आरोग्य = उत्तम मूल (जड़) : धर्म · अर्थ · काम · मोक्ष की।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does the sages' holy discussion name as the supreme root of the four aims?",
            ("आरोग्यम् (health)", "The verse says आरोग्यं मूलमुत्तमम्."),
            [("तपः (austerity)", "Austerity is named in verse 14, not here as the root."),
             ("अर्थः (wealth)", "Wealth is one of the four aims, not their root."),
             ("मोक्षः (liberation)", "Liberation is one of the four aims, not their root.")],
            "Health is called the supreme root of the four.",
            "आरोग्यं मूलमुत्तमम् = health is the supreme root."),
        match(1, "Match each word of line 1 to its meaning.",
              [["सुखोपविष्टाः", "seated at ease"], ["पुण्याम्", "holy"],
               ["कथाम्", "discussion"], ["तत्र", "there"]],
              "Line 1 sets the scene of the sages' talk.",
              "सुखोपविष्टाः = seated at ease; पुण्याम् = holy; कथाम् = discussion; तत्र = there."),
        fill(2, "The word for 'health' in line 2 is ____ (type it in Devanagari).",
             ["आरोग्यम्", "आरोग्यं", "आरोग्य"],
             "आरोग्यम् is the subject of the claim.",
             "आरोग्यम् ends in -म्, the neuter nominative singular: health is what is said to be the root.",
             "आरोग्यम् = health, called the supreme root."),
        mcq("discriminate", 3, "Which is the right split of सुखोपविष्टाः?",
            ("सुख + उपविष्टाः", "अ + उ join as ओ, so सुख + उपविष्टाः is written सुखोपविष्टाः."),
            [("सुखो + पविष्टाः", "पविष्टाः is not a word."),
             ("सुख + पविष्टाः", "पविष्टाः is not a word."),
             ("सुखे + उपविष्टाः", "ए + उ becomes अव्, not ओ; and सुखे is not the word here.")],
            "सुखोपविष्टाः = सुख ('ease') + उपविष्टाः ('seated').",
            "अ + उ → ओ."),
        multi("apply", 4, "Which of these are among the four aims of which health is called the root?",
              [("धर्म", "Right: dharma, righteousness."),
               ("अर्थ", "Right: artha, wealth."),
               ("काम", "Right: kāma, pleasure."),
               ("मोक्ष", "Right: mokṣa, liberation."),
               ("तपः", "Not in this line: the four are धर्म, अर्थ, काम and मोक्ष.")],
              [0, 1, 2, 3],
              "The four aims are धर्म, अर्थ, काम, मोक्ष; तपः is not one of them in this line.",
              "धर्मार्थकाममोक्षाणाम् names four aims."),
        mcq("transfer", 5,
            "In an invented line विनयो गुणानां मूलम् (विनय = humility, गुण = virtue), what is the root and of what?",
            ("Humility is the root of the virtues",
             "The genitive plural names the group, and the nominative before मूलम् is the root."),
            [("The virtues are the root of humility", "That would need the endings the other way round."),
             ("Humility and virtues are both roots", "Only the nominative is said to be the root."),
             ("Nothing is said to be a root", "मूलम् says that something is a root.")],
            "Same pattern as ...णाम् आरोग्यं मूलम्: [genitive plural] [nominative] मूलम्.",
            "Genitive plural + nominative + मूलम् = the nominative is the root of the genitive group.",
            teaches="In 'X-णाम् Y मूलम्', Y is the root and X are the things it supports."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "रोगास्तस्यापहर्तारः",
    "question": "What do diseases do to health, and what has arisen for humans?",
    "rule": ("Diseases are the destroyers of it (health), of well-being and of "
             "life. This great obstacle has arisen for human beings."),
    "limits": ("तस्य refers to आरोग्यम् of verse 15. The verse names the "
               "obstacle but does not yet say how to remove it."),
    "explain_hi": ("पिछले श्लोक का आरोग्य यहाँ ‘तस्य’ से लौटता है। रोग उसके, "
                   "श्रेयस् (कल्याण) के और जीवन के ‘अपहर्तारः’ (हरने वाले) हैं। "
                   "इसीलिए मनुष्यों के सामने ‘महान् अन्तरायः’ (बड़ी बाधा) "
                   "प्रकट हो गई है। संधि: ‘रोगाः + तस्य’ → ‘रोगास्तस्य’ "
                   "(विसर्ग + त → स्)।"),
    "hook": "रोग = आरोग्य, श्रेयस् और जीवन के हर्ता → मनुष्यों पर बड़ी बाधा आ पड़ी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 15 called health the supreme root. What does verse 16 say diseases do to it?",
            ("They destroy it, together with well-being and life",
             "रोगाः are called its अपहर्तारः, destroyers."),
            [("They strengthen it", "रोगाः are its destroyers, not strengtheners."),
             ("They have nothing to do with it", "तस्य ties them to health as its destroyers."),
             ("They spread it to others", "Nothing in the verse says this.")],
            "रोगास्तस्यापहर्तारः says diseases are the destroyers of health.",
            "Diseases are destroyers of health, well-being and life."),
        match(1, "Match each word of the verse to its meaning.",
              [["रोगाः", "diseases"], ["अपहर्तारः", "destroyers, robbers"],
               ["अन्तरायः", "obstacle"], ["महान्", "great"]],
              "These words carry the main claim.",
              "रोगाः = diseases; अपहर्तारः = destroyers; अन्तरायः = obstacle; महान् = great."),
        fill(2, "तस्य in this verse refers back to the word ____ of verse 15 (type it in Devanagari).",
             ["आरोग्यम्", "आरोग्यं", "आरोग्य"],
             "तस्य means 'of it', and the thing meant is health.",
             "तस्य is the genitive of तद् ('that'); here it picks up आरोग्यम्, the subject of verse 15.",
             "तस्य = of it = of आरोग्य."),
        mcq("discriminate", 3, "Which is the right split of रोगास्तस्यापहर्तारः?",
            ("रोगाः + तस्य + अपहर्तारः",
             "A visarga before त becomes स्, and अ + अ join as आ: रोगाः + तस्य + अपहर्तारः."),
            [("रोगा + स्तस्य + अपहर्तारः", "स्तस्य is not a word."),
             ("रोगाः + तस्या + पहर्तारः", "पहर्तारः is not a word here."),
             ("रोग + आस्तस्य + अपहर्तारः", "आस्तस्य is not a word.")],
            "The chunk joins three words: रोगाः, तस्य, अपहर्तारः.",
            "Visarga + त → स्त; अ + अ → आ."),
        multi("apply", 4, "Which of these does the verse say diseases destroy?",
              [("तस्य (health)", "Right: health, from verse 15."),
               ("श्रेयसः (well-being)", "Right: of well-being."),
               ("जीवितस्य (life)", "Right: of life."),
               ("मनुष्याणाम् (of humans)", "No: humans are those for whom the obstacle arose, not what is destroyed.")],
              [0, 1, 2],
              "Three genitives name what is destroyed; मनुष्याणाम् names who has the trouble.",
              "अपहर्तारः takes the genitives: of it, of well-being, of life."),
        mcq("transfer", 5,
            "In an invented line चोरा धनस्यापहर्तारः (चोर = thief, धन = wealth), who takes what?",
            ("Thieves take wealth",
             "The doers are the nominative plural; धनस्य names what is taken."),
            [("Wealth takes thieves", "The genitive names what is taken, not who takes."),
             ("Thieves give wealth", "अपहर्तारः means those who take away."),
             ("Wealth and thieves are both taken", "Only the genitive is the thing taken.")],
            "The same pattern as रोगाः ... अपहर्तारः.",
            "[nominative plural] + [genitive] + अपहर्तारः = the first take away the second.",
            teaches="With अपहर्तारः, the genitive names what is taken, and the nominative names who takes it."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "कः स्यात्तेषां शमोपाय",
    "question": "What do the sages ask, what do they do, and whom do they see?",
    "rule": ("'What could be the means of curing them?' Having said this, "
             "they entered into meditation. Then, with the eye of meditation, "
             "they saw Śakra as their refuge."),
    "limits": ("The quote ends at इति. The verse says the sages saw Śakra "
               "with the eye of meditation; it does not say he spoke to them "
               "there. The quoted speech began in verse 15."),
    "explain_hi": ("ऋषियों की चर्चा यहाँ प्रश्न पर पहुँचती है: ‘उनका शमन करने का "
                   "उपाय क्या हो?’ ‘इति’ उद्धरण को बन्द करता है। फिर ‘इत्युक्त्वा’ "
                   "(ऐसा कहकर) वे ध्यान में स्थित हो गए। तब उन्होंने ध्यान-चक्षु "
                   "से शक्र को अपना शरण-स्थल देखा। ‘तेषाम्’ का अर्थ रोगों का है। "
                   "‘उक्त्वा’ में उपसर्ग नहीं है, इसलिए ‘-त्वा’ रूप है।"),
    "hook": "प्रश्न → ध्यान → दर्शन: ‘शमोपाय क्या?’ → ध्यान में स्थित → ध्यान-चक्षु से शक्र (शरण)।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The sages first put a question about the means of curing the diseases. What do they do next?",
            ("They enter into meditation", "इत्युक्त्वा ध्यानमास्थिताः: having said this, they entered meditation."),
            [("They go to Indra at once", "First they meditate; only then do they see Śakra."),
             ("They ask Brahmā", "No one is asked in this verse."),
             ("They disperse", "The next words say they entered meditation.")],
            "After the question they sink into meditation.",
            "Question, then meditation, then sight of Śakra."),
        match(1, "Match each word of the verse to its meaning.",
              [["शमोपायः", "means of cure"], ["ध्यानम्", "meditation"],
               ["शरणम्", "refuge"], ["ददृशुः", "they saw"]],
              "These four words carry the sequence of the verse.",
              "शमोपायः = means of cure; ध्यानम् = meditation; शरणम् = refuge; ददृशुः = they saw."),
        fill(2, "इति + उक्त्वा is written ____ (type the joined word in Devanagari).",
             ["इत्युक्त्वा"],
             "इति + उक्त्वा → इत्युक्त्वा.",
             "इ before a different vowel becomes य्, so इति + उक्त्वा joins as इत्युक्त्वा, 'having said this'. उक्त्वा has no prefix, so it takes -त्वा.",
             "इ + उ → य् + उ."),
        mcq("discriminate", 3, "Which is the right split of ददृशुर्ध्यानचक्षुषा?",
            ("ददृशुः + ध्यानचक्षुषा",
             "After उ, a visarga before a voiced consonant like ध appears as र्: ददृशुः + ध्यानचक्षुषा."),
            [("ददृशु + र्ध्यानचक्षुषा", "र्ध्यानचक्षुषा is not a word."),
             ("ददृश + उर्ध्यानचक्षुषा", "उर्ध्यानचक्षुषा is not a word."),
             ("ददृशुर् + ध्यानचक्षुषा", "A bare -र् does not stand as a word-ending; the word is ददृशुः.")],
            "ददृशुर्ध्यानचक्षुषा = ददृशुः (they saw) + ध्यानचक्षुषा (with the eye of meditation).",
            "Visarga after उ + voiced consonant → र्."),
        mcq("apply", 4,
            "ध्यानचक्षुषा ends in the instrumental ending. What does it tell you about how they saw Śakra?",
            ("They saw him by means of the eye of meditation",
             "The instrumental names the means: seeing with the eye of meditation."),
            [("They saw the eye of meditation", "The thing seen is शक्रम्, with -म्."),
             ("They saw him in order to get the eye of meditation", "The instrumental names the means, not the purpose."),
             ("The eye of meditation saw them", "The doers are ते (they); the instrumental is only the means.")],
            "ध्यानचक्षुषा (instrumental) = with the eye of meditation.",
            "Instrumental = the means or tool by which the action is done."),
        mcq("transfer", 5,
            "In an invented line शिष्यो ज्ञानचक्षुषा गुरुं पश्यति (ज्ञान = knowledge, गुरु = teacher, पश्यति = sees), how does the student see?",
            ("With the eye of knowledge",
             "The instrumental in -चक्षुषा names the means, as in ध्यानचक्षुषा."),
            [("He sees the eye of knowledge", "The thing seen is गुरुम्."),
             ("The teacher sees with knowledge", "The doer is शिष्यः."),
             ("He sees for the sake of knowledge", "The instrumental names the means, not the purpose.")],
            "The same pattern as ध्यानचक्षुषा.",
            "X-चक्षुषा = with the eye of X (the means of seeing).",
            teaches="A word in -चक्षुषा names the means of seeing: with the eye of that thing."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "स वक्ष्यति शमोपायं",
    "question": "Who will tell the cure, and what question do the sages put to each other?",
    "rule": ("'He, the lord of the immortals, will tell the means of cure "
             "properly. Who should go to the abode of the thousand-eyed one to "
             "ask the husband of Śacī?'"),
    "limits": ("According to the notes, अमरप्रभुः, सहस्राक्षः and शचीपतिः are "
               "all epithets of Indra. The verse only asks who should go; "
               "the answer comes in verse 19."),
    "explain_hi": ("यह श्लोक ऋषियों की सोच या बात है। ‘सः’ अमरों के प्रभु (इन्द्र) "
                   "हैं, जो उपाय ‘यथावत्’ (ठीक-ठीक) बताएँगे। अगली पंक्ति "
                   "प्रश्न है: ‘सहस्राक्ष के भवन में, शचीपति से पूछने के लिए कौन "
                   "जाए?’ तीनों उपाधियाँ (अमरप्रभु, सहस्राक्ष, शचीपति) "
                   "एक ही इन्द्र के लिए हैं। ‘वक्ष्यति’ भविष्य है और ‘गच्छेत्’ "
                   "विधिलिङ् (चाहिए) का रूप है।"),
    "hook": "वे बताएँगे (वक्ष्यति) — पर कौन जाए (गच्छेत्) पूछने? इन्द्र = अमरप्रभु = सहस्राक्ष = शचीपति।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The verse calls one person 'lord of the immortals', 'thousand-eyed' and 'husband of Śacī'. Who is meant?",
            ("Indra (Śakra)", "The notes say all three are epithets of Indra."),
            [("Brahmā", "Brahmā is not meant by these epithets."),
             ("Bharadvāja", "Bharadvāja is a sage, not the lord of the immortals."),
             ("Ātreya", "Ātreya is a sage named in verse 9, not the lord of the immortals.")],
            "अमरप्रभुः, सहस्राक्षः and शचीपतिः name Indra.",
            "Three epithets, one person: Indra."),
        match(1, "Match each word of the verse to its meaning.",
              [["अमरप्रभुः", "lord of the immortals"],
               ["शचीपतिम्", "husband of Śacī"],
               ["भवनम्", "abode"], ["प्रष्टुम्", "to ask"]],
              "These words give the person and the aim of the journey.",
              "अमरप्रभुः = lord of the immortals; शचीपतिम् = husband of Śacī; भवनम् = abode; प्रष्टुम् = to ask."),
        fill(2, "The word meaning 'will tell' is ____ (type it in Devanagari).",
             ["वक्ष्यति"],
             "वक्ष्यति is from √वच्, 'to speak'.",
             "वक्ष्यति is labelled a future, third person singular: 'he will tell'. The sages expect an answer from Indra.",
             "वक्ष्यति = he will tell (future)."),
        mcq("discriminate", 3, "Which is the right split of यथावदमरप्रभुः?",
            ("यथावत् + अमरप्रभुः",
             "A final त becomes द before a vowel, so यथावत् + अमरप्रभुः is written यथावदमरप्रभुः."),
            [("यथावद + अमरप्रभुः", "A word यथावद would join with अ as आ, giving …दामर…"),
             ("यथावद् + मरप्रभुः", "मरप्रभुः is not a word."),
             ("यथा + वदमरप्रभुः", "वदमरप्रभुः is not a word.")],
            "यथावदमरप्रभुः = यथावत् ('properly') + अमरप्रभुः ('lord of the immortals').",
            "त् + vowel → द् + vowel."),
        mcq("apply", 4,
            "कः ... गच्छेत् is a question. गच्छेत् is the optative of √गम्, 'should go'. What does the question ask?",
            ("Who should go?", "The optative asks about a person who should go."),
            [("Who went?", "गच्छेत् is not a past form."),
             ("Who will certainly go?", "The optative is 'should', not a sure future."),
             ("Why did he go?", "कः asks who, not why.")],
            "कः गच्छेत्? = Who should go?",
            "कः + optative = 'who should…?'."),
        mcq("transfer", 5,
            "An invented line reads ऋषिर्नगरं गच्छेद् राजानं द्रष्टुम् (नगर = city, द्रष्टुम् = to see, राजन् = king). What is the purpose of going?",
            ("To see the king", "The infinitive in -तुम् (here द्रष्टुम्) gives the purpose, as प्रष्टुम् does."),
            [("To build the city", "The purpose is the infinitive: to see."),
             ("To be seen by the king", "द्रष्टुम् is active: to see."),
             ("No purpose is given", "द्रष्टुम् states the purpose.")],
            "The infinitive in -तुम् names the aim of going, as in गच्छेत् प्रष्टुम्.",
            "Verb of going + infinitive in -तुम् = going in order to do that.",
            teaches="An infinitive in -तुम् such as प्रष्टुम् or द्रष्टुम् tells the purpose of the going."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "अहमर्थे नियुज्येयमत्र",
    "question": "Who volunteers, what does he say, and what follows?",
    "rule": ("'Let me be appointed to this task': these were Bharadvāja's "
             "words, spoken first, and so he was appointed by the sages."),
    "limits": ("The notes call नियुज्येयम् a non-classical (ārṣa) form. "
               "Whether Bharadvāja was the only volunteer is not said; the "
               "verse says his was the first word."),
    "explain_hi": ("प्रश्न का उत्तर यहीं मिलता है। भरद्वाज ने सबसे पहले कहा: "
                   "‘इस कार्य में मुझे नियुक्त किया जाए’ (अहमर्थे नियुज्येयमत्र)। "
                   "‘इति’ से उनका कथन बन्द होता है। ‘तस्मात्’ (इसलिए) ऋषियों ने "
                   "उन्हें नियुक्त किया (सः नियोजितः)। संधि: ‘भरद्वाजः + अब्रवीत्’ → "
                   "‘भरद्वाजो ऽब्रवीत्’ (अः + अ → ओ, लुप्त अ का चिह्न ऽ)।"),
    "hook": "प्रथम वचन: ‘अहमर्थे नियुज्येयमत्र’ → इसलिए ऋषियों ने भरद्वाज को नियुक्त किया।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The sages asked who should go to Indra. Who answers first, and what does he say?",
            ("Bharadvāja: 'Let me be appointed to this task'",
             "अहमर्थे नियुज्येयमत्र is his word, spoken first."),
            [("Indra: 'I will tell the cure'", "Indra is not present in this verse."),
             ("Ātreya: 'Let all go together'", "Ātreya is not mentioned in this verse."),
             ("All the sages together, at once", "The verse says the first word was Bharadvāja's.")],
            "Bharadvāja spoke first and was appointed.",
            "Bharadvāja volunteers; the sages appoint him."),
        match(1, "Match each word of the verse to its meaning.",
              [["अहम्", "I"], ["अत्र", "here, in this"],
               ["प्रथमम्", "first"], ["नियोजितः", "appointed"]],
              "These words carry the volunteering and the appointment.",
              "अहम् = I; अत्र = here/in this; प्रथमम् = first; नियोजितः = appointed."),
        fill(2, "अत्र + इति joins as अत्रेति. The अ + इ turn into ____ (type it in Devanagari).",
             ["ए"],
             "अ + इ become ए.",
             "अ or आ followed by इ joins as ए: अत्र + इति → अत्रेति. The इति then closes the quotation.",
             "अ + इ → ए."),
        mcq("discriminate", 3, "Which is the right split of भरद्वाजो ऽब्रवीत्?",
            ("भरद्वाजः + अब्रवीत्",
             "अः before अ becomes ओ, and the dropped अ is shown by ऽ."),
            [("भरद्वाज + उब्रवीत्", "उब्रवीत् is not a word."),
             ("भरद्वा + जोब्रवीत्", "Neither part is a word here."),
             ("भरद्वाजा + अब्रवीत्", "The name ends in -ः, not -आ.")],
            "भरद्वाजो ऽब्रवीत् = भरद्वाजः (Bharadvāja) + अब्रवीत् (spoke).",
            "अः + अ → ओ + ऽ."),
        order(4, "Put the events in the order of verses 18 and 19.",
              ["The sages ask who should go to Indra",
               "Bharadvāja says 'let me be appointed'",
               "The sages appoint Bharadvāja"],
              "The question comes first, then the volunteer's words, then the appointment.",
              "Question → volunteer → appointment.", role="apply"),
        mcq("transfer", 5,
            "An invented line reads अहं गच्छेयमिति शिष्यो ऽब्रवीत् (गच्छेयम् = may I go). What did the student say?",
            ("'May I go'",
             "The words before इति are what he said: अहं गच्छेयम्."),
            [("Nothing", "अब्रवीत् says he spoke."),
             ("'Let the teacher go'", "अहम् means 'I'."),
             ("'Let him be sent'", "The quote is 'may I go'.")],
            "इति closes the quotation, as in …नियुज्येयमत्रेति.",
            "Words before इति + verb of speaking = what was said.",
            teaches="You can find what someone said by reading back from इति to the start of the quoted words."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "स शक्रभवनं गत्वा",
    "question": "Where does he go, and whom does he see there?",
    "rule": ("Having gone to Śakra's abode, he saw the slayer of Bala "
             "(Indra), amid hosts of gods and sages, blazing like fire."),
    "limits": ("सुरर्षि may be 'gods and sages' (two groups) or 'divine "
               "sages'. The verse itself names only the epithet "
               "'slayer of Bala'; the notes explain Bala as a demon."),
    "explain_hi": ("अब भरद्वाज (वही ‘सः’, जिसे श्लोक १९ में नियुक्त किया गया) "
                   "शक्र के भवन पहुँचते हैं। ‘गत्वा’ = जाकर (उपसर्ग के बिना √गम् + "
                   "त्वा)। वहाँ उन्होंने ‘बलहन्तार’ (बल को मारने वाले, यानी इन्द्र) "
                   "को देखा, जो सुरर्षि-गण (देवताओं और ऋषियों के समूह) के बीच थे और "
                   "जलती अग्नि के समान दीप्त थे। ‘सुरर्षि’ दो प्रकार से पढ़ा जा "
                   "सकता है (नोट देखें)।"),
    "hook": "शक्र का भवन → देव–ऋषि समूह के बीच → बलहन्ता, जलती अग्नि जैसे दीप्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "After being appointed, where does Bharadvāja go?",
            ("To Śakra's abode", "शक्रभवनं गत्वा: having gone to Śakra's abode."),
            [("Back to the Himalaya", "The verse sends him to Śakra's abode."),
             ("To Brahmā's world", "Brahmā is not mentioned in this verse."),
             ("To the Aśvins", "The Aśvins are not mentioned in this verse.")],
            "He goes to Śakra's abode.",
            "He goes to Śakra's abode and sees Indra."),
        match(1, "Match each word of the verse to its meaning.",
              [["गत्वा", "having gone"], ["ददर्श", "saw"],
               ["बलहन्तारम्", "slayer of Bala"], ["अनलम्", "fire"]],
              "These words give the journey, the seeing and the comparison.",
              "गत्वा = having gone; ददर्श = saw; बलहन्तारम् = slayer of Bala; अनलम् = fire."),
        fill(2, "The word meaning 'having gone' is ____ (type it in Devanagari).",
             ["गत्वा"],
             "गत्वा comes from √गम्, 'to go'.",
             "गत्वा is a 'having done' word in -त्वा. √गम् has no prefix here, so it takes -त्वा. With a prefix it would take -य, as उपागम्य.",
             "गत्वा = having gone (before ददर्श)."),
        mcq("discriminate", 3, "Which is the right split of दीप्यमानमिवानलम्?",
            ("दीप्यमानम् + इव + अनलम्",
             "अ + अ join as आ, so इव + अनलम् is written इवानलम्; the m before इव joins by sandhi."),
            [("दीप्यमान + मिवानलम्", "मिवानलम् is not a word."),
             ("दीप्यमानमि + वानलम्", "Neither part is a word."),
             ("दीप्यमानम् + इवा + नलम्", "इवा and नलम् are not words.")],
            "दीप्यमानमिवानलम् = दीप्यमानम् (blazing) + इव (like) + अनलम् (fire).",
            "इव + अनलम् → इवानलम्."),
        multi("apply", 4, "Which words describe the one Bharadvāja saw?",
              [("सुरर्षिगणमध्यगम्", "Right: amid the hosts of gods and sages."),
               ("बलहन्तारम्", "Right: slayer of Bala."),
               ("शक्रभवनम्", "No: it is the place he went to."),
               ("दीप्यमानम्", "Right: blazing.")],
              [0, 1, 3],
              "Three accusatives describe the one seen; शक्रभवनम् is the place.",
              "The accusatives of person: amid hosts, slayer of Bala, blazing."),
        mcq("transfer", 5,
            "In an invented line शिष्यो गुरुं दीप्यमानमिव रविं ददर्श (रवि = sun; दीप्यमानम् goes with गुरुम्), what is compared to what?",
            ("The teacher, blazing, is compared to the sun",
             "इव ('like') links the blazing teacher to the sun."),
            [("The sun is compared to the teacher", "दीप्यमानम् describes the teacher."),
             ("The student is compared to the sun", "The student is the one who sees."),
             ("The teacher is said to be the sun itself", "इव means 'like', so it is a comparison, not an identity.")],
            "The same pattern as दीप्यमानमिवानलम्.",
            "X blazing + इव + Y = X blazes like Y.",
            teaches="इव means 'like': it makes a comparison between the one described and the thing named after it."),
    ],
}

# ================================================================= NOTES
NOTES_HI = {
    "11": "इस श्लोक के लिए स्रोत में कोई पाठभेद या चिह्न नहीं है। संधि जाँची: साङ्कृत्यः + बैजवापिः → साङ्कृत्यो बैजवापिः (अः + घोष ब → ओ); बैजवापिः + च → बैजवापिश्च (विसर्ग + च → श्); काप्यकात्यायनौ + उभौ → काप्यकात्यायनावुभौ (औ + स्वर → आव्)। ‘शरलोमा’ का रूप पुंल्लिंग प्रथमा एकवचन है (प्रातिपदिक शरलोमन्)।",
    "12": "‘मारीचकाश्यपौ’ द्विवचन है, इसलिए दो व्यक्ति; पर टिप्पणी के अनुसार इसे कभी ‘मारीचि काश्यप’ एक नाम भी समझा गया है। -अक्ष वाले नाम (शर्कराक्ष, हिरण्याक्ष, लोकाक्ष) स्रोत ने विग्रह किए बिना रखे हैं क्योंकि वे नाम हैं। संधि: पैङ्गिः + एव → पैङ्गिरेव (इः + स्वर → इर्); कैकशेयः/धौम्यः/शर्कराक्षः/हिरण्याक्षः के विसर्ग घोष व्यंजन से पहले ‘ओ’ बने हैं।",
    "13": "टिप्पणी: वैखानस और वालखिल्य बहुवचन में तपस्वियों के समूह हैं, एक-एक व्यक्ति नहीं। संधि जाँची: शाकुनेयः + च → शाकुनेयश्च; मैत्रेयः → मैत्रेयो (म से पहले); वैखानसाः में आः का विसर्ग व से पहले लुप्त; वालखिल्याः + तथा → वालखिल्यास्तथा; च + अन्ये → चान्ये; महा + ऋषयः → महर्षयः।",
    "14": "पाठभेद: ‘दमस्य’ की जगह ‘यमस्य’ (तब यम–नियम की जोड़ी बनती है)। ‘तपसः’ को ‘तेजसा’ के साथ (तप का तेज) पढ़ना अधिक ठीक है, क्योंकि ‘च’ पिछली सूची को बन्द करता है; इसे ‘निधयः’ के बाद चौथा पद भी माना जा सकता है। ‘ब्रह्मज्ञान’ का अर्थ ‘वैदिक ज्ञान’ भी हो सकता है। संधि: हूयमानाः + इव → हूयमाना इव (आः का विसर्ग स्वर से पहले लुप्त); इव + अग्नयः → इवाग्नयः।",
    "15": "यह श्लोक एक वाक्य की भूमिका है: ऋषियों का सीधा कथन इसकी दूसरी पंक्ति से शुरू होकर श्लोक १७ की पहली पंक्ति तक चलता है। ‘ते’ = श्लोक ७–१४ के ऋषि। संधि जाँची: सुख + उपविष्टाः → सुखोपविष्टाः; उपविष्टाः + ते → उपविष्टास्ते (विसर्ग + त → स्); कथाम् + इमाम् → कथामिमाम्; …मोक्षाणाम् + आरोग्यम् → …मोक्षाणामारोग्यम्।",
    "16": "टिप्पणी के अनुसार ‘तस्य’ का अर्थ ‘आरोग्यम्’ (श्लोक १५) है और ‘श्रेयस्’ का अर्थ कल्याण या उच्चतर हित है। संधि जाँची: रोगाः + तस्य → रोगास्तस्य; तस्य + अपहर्तारः → तस्यापहर्तारः; प्रादुर्भूतः → प्रादुर्भूतो (म से पहले); महान् + अयम् → महानयम् (दीर्घ आ के बाद न् का द्वित्व नहीं)।",
    "17": "‘शमोपायः’ के बाद ‘इति’ आने पर विसर्ग लुप्त होता है (शमोपाय इति); ‘तेषाम्’ का अर्थ रोगों का है; ‘शरणं शक्रम्’ में शरणम् विधेय-रूप में है (शक्र को शरण के रूप में)। संधि: इति + उक्त्वा → इत्युक्त्वा; ददृशुः + ध्यानचक्षुषा → ददृशुर्ध्यानचक्षुषा। ऋषियों का उद्धरण ‘इति’ पर समाप्त होता है।",
    "18": "यह ऋषियों का विचार या कथन है। अमरप्रभु, सहस्राक्ष और शचीपति इन्द्र की उपाधियाँ हैं (टिप्पणी)। संधि जाँची: सः का विसर्ग व्यंजन ‘व’ से पहले लुप्त (स वक्ष्यति); शम + उपायम् → शमोपायम्; यथावत् + अमरप्रभुः → यथावदमरप्रभुः। ‘वक्ष्यति’ भविष्यत् है और ‘गच्छेत्’ विधिलिङ् (सम्भावना या ‘चाहिए’)।",
    "19": "टिप्पणी: ‘नियुज्येयम्’ आर्ष रूप है (कर्मवाच्य धातु-अंग के साथ परस्मैपद का प्रत्यय); शास्त्रीय संस्कृत में ‘नियुज्येय’ होता। ‘प्रथमं वचः’ = सबसे पहले (दूसरे ऋषियों से पहले) बोला गया वचन। संधि: अहम् + अर्थे → अहमर्थे; अत्र + इति → अत्रेति; भरद्वाजः + अब्रवीत् → भरद्वाजो ऽब्रवीत्; तस्मात् + ऋषिभिः → तस्मादृषिभिः।",
    "20": "‘सुरर्षि’ दो तरह से पढ़ा जा सकता है: ‘सुर और ऋषि’ (द्वन्द्व) या ‘दिव्य ऋषि’ (कर्मधारय)। बल एक असुर है (टिप्पणी)। ‘सः’ वही है जिसे श्लोक १९ में नियुक्त किया गया। संधि: सुर + ऋषि → सुरर्षि; दीप्यमानम् + इव → दीप्यमानमिव; इव + अनलम् → इवानलम्। ‘गत्वा’ में उपसर्ग नहीं है, इसलिए -त्वा।",
}

# ================================================================= AIDS
AIDS = {
    "11": {
        "letters": "पहली पंक्ति: सा-बै-कु-बा · दूसरी: ब-श-का-का (साङ्कृत्य, बैजवापि, कुशिक, बादरायण | बडिश, शरलोमा, काप्य, कात्यायन)।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["साङ्कृत्य", "बैजवापि", "कुशिक", "बादरायण"]},
            {"label": "दूसरी पंक्ति",
             "items": ["बडिश", "शरलोमा", "काप्य–कात्यायन (जोड़ा)", "उभौ"]}]},
        "puns": "कुशिक ≈ ‘कुशल’ की ध्वनि; शरलोमा ≈ ‘शर + लोम’ की ध्वनि। (केवल सुनने की सहायता; नाम के अर्थ का दावा नहीं।)",
        "sandhi": "औ + स्वर → आव् + स्वर: काप्यकात्यायनौ + उभौ → काप्यकात्यायनावुभौ · विसर्ग + च → श्: बैजवापिः + च → बैजवापिश्च · अः + घोष → ओ: साङ्कृत्यः → साङ्कृत्यो (ब से पहले)।",
        "contrast": "श्लोक ९–१० में जोड़े नाम के अन्त में -औ से बने थे; यहाँ ‘उभौ’ अलग शब्द है जो ‘दोनों’ कहता है और जोड़े पर बल देता है।",
        "chunks": "साङ्कृत्यो | बैजवापिश्च | कुशिको | बादरायणः ‖ बडिशः | शरलोमा च | काप्यकात्यायनावुभौ।",
    },
    "12": {
        "letters": "पहली: का-कै-धौ-मा · दूसरी: श-हि-लो-पै (काङ्कायन, कैकशेय, धौम्य, मारीच–काश्यप | शर्कराक्ष, हिरण्याक्ष, लोकाक्ष, पैङ्गि)।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["काङ्कायन", "कैकशेय", "धौम्य", "मारीच–काश्यप (जोड़ा)"]},
            {"label": "दूसरी पंक्ति",
             "items": ["शर्कराक्ष", "हिरण्याक्ष", "लोकाक्ष", "पैङ्गि"]}]},
        "pegs": "तीन -अक्ष नाम = तीन एक-से सिरे वाली छड़ियाँ: शर्कराक्ष · हिरण्याक्ष · लोकाक्ष (मेरा बनाया चित्र)।",
        "sandhi": "अः + घोष → ओ: कैकशेयः → कैकशेयो (ध से पहले), धौम्यः → धौम्यो (म से पहले) · इः + स्वर → इर्: पैङ्गिः + एव → पैङ्गिरेव।",
        "contrast": "मारीचकाश्यपौ: द्विवचन = दो व्यक्ति (मारीच और काश्यप); टिप्पणी के अनुसार इसे कभी एक नाम ‘मारीचि काश्यप’ भी समझा गया।",
        "chunks": "काङ्कायनः | कैकशेयो | धौम्यो | मारीचकाश्यपौ ‖ शर्कराक्षो | हिरण्याक्षो | लोकाक्षः | पैङ्गिरेव च।",
    },
    "13": {
        "letters": "पहली पंक्ति: शौ-शा-मै-मै · दूसरी: वै-वा-अ-म (शौनक, शाकुनेय, मैत्रेय, मैमतायनि | वैखानस, वालखिल्य, अन्ये, महर्षि)।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["शौनक", "शाकुनेय", "मैत्रेय", "मैमतायनि"]},
            {"label": "दूसरी पंक्ति",
             "items": ["वैखानसाः (समूह)", "वालखिल्याः (समूह)", "तथा", "अन्ये महर्षयः"]}]},
        "sandhi": "विसर्ग + च → श्: शाकुनेयः + च → शाकुनेयश्च · विसर्ग + त → स्: वालखिल्याः + तथा → वालखिल्यास्तथा · अ + अ → आ: च + अन्ये → चान्ये · आ + ऋ → अर्: महा + ऋषयः → महर्षयः।",
        "anchors": "महर्षि = महा + ऋषि (श्लोक ७ में भी) · वैखानस, वालखिल्य: बहुवचन = तपस्वियों के समूह (टिप्पणी)।",
        "chunks": "शौनकः | शाकुनेयश्च | मैत्रेयो | मैमतायनिः ‖ वैखानसा | वालखिल्यास्तथा | चान्ये | महर्षयः।",
    },
    "14": {
        "frame": "कौन: ऋषि (श्लोक ७–१३) · किसके भण्डार: ब्रह्मज्ञान, दम, नियम · कैसे: तप के तेज से दीप्त · उपमा: आहुति पाती अग्नियाँ।",
        "diagram": {"groups": [
            {"label": "किसके निधि",
             "items": ["ब्रह्मज्ञानस्य निधयः", "दमस्य", "नियमस्य च"]},
            {"label": "कैसे",
             "items": ["तपसः तेजसा", "दीप्ताः"]},
            {"label": "उपमा",
             "items": ["हूयमानाः", "इव अग्नयः"]}]},
        "pegs": "अग्नि में आहुति पड़ते ही लपट उठती है: वैसे तप के तेज से ऋषि दीप्त (मेरा बनाया चित्र)।",
        "sandhi": "विसर्ग + त → स्: तपसः + तेजसा → तपसस्तेजसा · अः + घोष → ओ: निधयः → निधयो (द से पहले) · आः + स्वर → विसर्ग लुप्त: हूयमानाः + इव → हूयमाना इव · अ + अ → आ: इव + अग्नयः → इवाग्नयः।",
        "contrast": "दमस्य (दम = आत्म-संयम) ↔ पाठभेद यमस्य: यम से ‘यम–नियम’ की जोड़ी बनती है (पाठ-टिप्पणी)।",
        "chunks": "ब्रह्मज्ञानस्य | निधयो | दमस्य | नियमस्य च ‖ तपसस्तेजसा | दीप्ता | हूयमाना | इवाग्नयः।",
    },
    "15": {
        "frame": "कौन: वे ऋषि · कहाँ: वहाँ, सुख से बैठे · क्या: पुण्य कथा · बात: आरोग्य ही धर्म, अर्थ, काम, मोक्ष का उत्तम मूल।",
        "diagram": {"groups": [
            {"label": "किसका",
             "items": ["धर्म", "अर्थ", "काम", "मोक्ष"]},
            {"label": "क्या",
             "items": ["आरोग्यम्", "मूलम्", "उत्तमम्"]}]},
        "story": "ऋषि सुख से बैठे → पुण्य चर्चा शुरू की → पहला कथन: चारों (धर्म, अर्थ, काम, मोक्ष) का उत्तम मूल आरोग्य है।",
        "pegs": "आरोग्य = पेड़ की जड़, चार = चार शाखाएँ: धर्म · अर्थ · काम · मोक्ष (मेरा बनाया चित्र)।",
        "sandhi": "अ + उ → ओ: सुख + उपविष्टाः → सुखोपविष्टाः · विसर्ग + त → स्: उपविष्टाः + ते → उपविष्टास्ते · म् + स्वर: …मोक्षाणाम् + आरोग्यम् → …मोक्षाणामारोग्यम्।",
        "contrast": "आरोग्यम् (श्लोक १५: मूल) ↔ रोगाः (श्लोक १६: अपहर्तारः): जड़ और उसे हरने वाले।",
        "chunks": "सुखोपविष्टास्ते | तत्र | पुण्यां चक्रुः | कथामिमाम् ‖ धर्मार्थकाममोक्षाणाम् | आरोग्यं | मूलमुत्तमम्।",
    },
    "16": {
        "diagram": {"groups": [
            {"label": "कौन",
             "items": ["रोगाः"]},
            {"label": "किसके हर्ता",
             "items": ["तस्य", "श्रेयसः", "जीवितस्य च"]},
            {"label": "क्या हुआ",
             "items": ["प्रादुर्भूतः", "मनुष्याणाम्", "अन्तरायः", "महान् अयम्"]}]},
        "story": "रोग तीन चीज़ें छीनते हैं: आरोग्य, कल्याण, जीवन → इसलिए मनुष्यों के सामने बड़ी बाधा खड़ी है।",
        "pegs": "रोग = चोर, जो तीन थैले ले जाता है: आरोग्य, श्रेयस्, जीवन (मेरा बनाया चित्र)।",
        "sandhi": "विसर्ग + त → स्: रोगाः + तस्य → रोगास्तस्य · अ + अ → आ: तस्य + अपहर्तारः → तस्यापहर्तारः · अः + घोष → ओ: प्रादुर्भूतः → प्रादुर्भूतो (म से पहले)।",
        "anchors": "अपहर्तारः ← अप + √हृ (हरना) · अन्तराय = बीच में आने वाली रुकावट · प्रादुर्भूत: श्लोक ६ में भी आया।",
        "chunks": "रोगास्तस्यापहर्तारः | श्रेयसो | जीवितस्य च ‖ प्रादुर्भूतो | मनुष्याणाम् | अन्तरायो | महानयम्।",
    },
    "17": {
        "chain": {"steps": ["प्रश्न: कः स्यात् शमोपायः?", "इत्युक्त्वा",
                            "ध्यान में स्थित", "ध्यान-चक्षु से शक्र का दर्शन"]},
        "frame": "कौन: वे ऋषि · क्या किया: ध्यान में स्थित · क्या देखा: शक्र, शरण के रूप में · कैसे: ध्यान-चक्षु से।",
        "pegs": "ध्यान-चक्षु = मन की खिड़की, जिससे दूर बैठे शक्र दिख गए (मेरा बनाया चित्र)।",
        "sandhi": "इ + उ → य् + उ: इति + उक्त्वा → इत्युक्त्वा · अ + उ → ओ: शम + उपायः → शमोपायः · अः + इ → विसर्ग लुप्त: शमोपायः + इति → शमोपाय इति · उः + घोष व्यंजन → उर्: ददृशुः + ध्यानचक्षुषा → ददृशुर्ध्यानचक्षुषा।",
        "contrast": "उक्त्वा (उपसर्ग-रहित √वच् + त्वा → -त्वा) ↔ उपागम्य (उपसर्ग के साथ → -य)।",
        "chunks": "कः स्यात् | तेषां | शमोपाय | इत्युक्त्वा | ध्यानमास्थिताः ‖ अथ ते | शरणं शक्रं | ददृशुः | ध्यानचक्षुषा।",
    },
    "18": {
        "frame": "कौन बताएँगे: अमरों के प्रभु (इन्द्र) · क्या: शमोपाय · कैसे: यथावत् · प्रश्न: उनसे पूछने कौन जाए?",
        "diagram": {"groups": [
            {"label": "वक्ता",
             "items": ["सः"]},
            {"label": "क्या",
             "items": ["वक्ष्यति", "शमोपायम्", "यथावत्"]},
            {"label": "कौन (उपाधि)",
             "items": ["अमरप्रभुः"]},
            {"label": "प्रश्न",
             "items": ["कः", "सहस्राक्षभवनम्", "गच्छेत्", "प्रष्टुम्", "शचीपतिम्"]}]},
        "pegs": "तीन नाम = एक ही व्यक्ति के तीन टैग: प्रभु-टैग, हज़ार-आँख-टैग, शची-टैग (मेरा बनाया चित्र)।",
        "sandhi": "अ + उ → ओ: शम + उपायम् → शमोपायम् · त् → द् (स्वर से पहले): यथावत् + अमरप्रभुः → यथावदमरप्रभुः · सः का विसर्ग व्यंजन से पहले लुप्त: स वक्ष्यति।",
        "contrast": "वक्ष्यति (भविष्य: बताएगा) ↔ गच्छेत् (विधिलिङ्: जाए?)।",
        "chunks": "स वक्ष्यति | शमोपायं | यथावदमरप्रभुः ‖ कः | सहस्राक्षभवनं | गच्छेत् | प्रष्टुं शचीपतिम्।",
    },
    "19": {
        "frame": "कौन: भरद्वाज · क्या कहा: ‘इस कार्य में मुझे नियुक्त किया जाए’ · फल: ऋषियों ने नियुक्त किया।",
        "chain": {"steps": ["प्रश्न: कौन जाए? (श्लोक १८)", "भरद्वाज का प्रथम वचन",
                            "ऋषियों द्वारा नियुक्ति"]},
        "story": "ऋषि पूछते हैं कौन जाए → भरद्वाज सबसे पहले बोलते हैं → इसलिए उन्हें ही नियुक्त किया गया।",
        "sandhi": "अ + इ → ए: अत्र + इति → अत्रेति · अः + अ → ओ + ऽ: भरद्वाजः + अब्रवीत् → भरद्वाजो ऽब्रवीत् · त् → द् (स्वर से पहले): तस्मात् + ऋषिभिः → तस्मादृषिभिः।",
        "anchors": "नियुज्येयम् और नियोजितः दोनों नि + √युज् से: योग, युक्त, संयोजन।",
        "chunks": "अहमर्थे | नियुज्येयमत्रेति | प्रथमं वचः ‖ भरद्वाजो ऽब्रवीत् | तस्मादृषिभिः | स नियोजितः।",
    },
    "20": {
        "chain": {"steps": ["शक्र के भवन जाकर", "देव–ऋषि समूह के बीच",
                            "बलहन्ता को देखा", "जलती अग्नि जैसे दीप्त"]},
        "frame": "कौन: सः (श्लोक १९ का नियुक्त) · कहाँ: शक्र का भवन · क्या देखा: बलहन्ता, समूह के बीच, अग्नि जैसा दीप्त।",
        "diagram": {"groups": [
            {"label": "गया",
             "items": ["सः", "शक्रभवनम्", "गत्वा"]},
            {"label": "कहाँ",
             "items": ["सुरर्षिगणमध्यगम्"]},
            {"label": "देखा",
             "items": ["ददर्श", "बलहन्तारम्"]},
            {"label": "उपमा",
             "items": ["दीप्यमानम्", "इव अनलम्"]}]},
        "pegs": "दीप्यमानमिवानलम् = सभा के बीच धधकती धूनी (मेरा बनाया चित्र)।",
        "anchors": "बलहन्तार ← बल + हन्तृ (मारने वाला) · दीप्यमान और दीप्त (श्लोक १४) दोनों √दीप् से।",
        "sandhi": "अ + ऋ → अर्: सुर + ऋषि → सुरर्षि · अ + अ → आ: इव + अनलम् → इवानलम् · म् + स्वर: दीप्यमानम् + इव → दीप्यमानमिव।",
        "contrast": "गत्वा (उपसर्ग-रहित √गम् + त्वा) ↔ उपागम्य (उपसर्ग के साथ → -य)।",
        "chunks": "स शक्रभवनं गत्वा | सुरर्षिगणमध्यगम् ‖ ददर्श | बलहन्तारं | दीप्यमानमिवानलम्।",
    },
}

# ================================================================= IMAGES
IMAGE_SPECS = {
    ("15", "diagram"): {
        "file": "su1-15-root.svg",
        "alt": ("Two columns: the four aims dharma, artha, kāma and mokṣa on one "
                "side, and आरोग्यम् as the supreme root (मूलम् उत्तमम्) on the other"),
        "type": "split",
        "title": "आरोग्य = उत्तम मूल",
        "cols": [["किसका", ["धर्म", "अर्थ", "काम", "मोक्ष"]],
                 ["क्या", ["आरोग्यम्", "मूलम्", "उत्तमम्"]]],
    },
    ("17", "chain"): {
        "file": "su1-17-chain.svg",
        "alt": ("Four boxes with arrows: the question about the cure, "
                "'having said this', entering meditation, and seeing Śakra "
                "with the eye of meditation"),
        "type": "chain",
        "title": "प्रश्न से दर्शन तक",
        "steps": ["प्रश्न: कः स्यात् शमोपायः?", "इत्युक्त्वा",
                  "ध्यान में स्थित", "ध्यान-चक्षु से शक्र का दर्शन"],
    },
}
