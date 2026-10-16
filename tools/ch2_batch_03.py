from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "पीलून्यारग्वधं द्राक्षाम्",
    "question": "Which drugs does verse 10 name for purgation, and when are they to be used?",
    "rule": ("Pīlu, āragvadha, grape, dravantī and nicula are to be "
             "administered for purgation (विरेकार्थम्) when the doṣa has "
             "gone to the pakvāśaya, the lower gut. Verses 9 and 10 form one "
             "sentence."),
    "limits": ("The verse names the drugs, the purpose and the condition "
               "only. It gives no dose and no method, and for dravantī and "
               "nicula the data says only 'a medicinal plant, name kept'. "
               "Verse 9 is the first part of this sentence."),
    "explain_hi": ("श्लोक ९ और १० मिलकर एक ही वाक्य हैं; यहाँ वह पूरा होता है। "
                   "पाँच नाम गिनाए गए हैं: पीलु, आरग्वध, द्राक्षा, द्रवन्ती और "
                   "निचुल। इनका प्रयोग ‘विरेकार्थम्’ यानी विरेचन के लिए कहा "
                   "गया है, और शर्त है ‘पक्वाशयगते दोषे’: जब दोष पक्वाशय "
                   "(निचले आन्त्र, पचे हुए मल के स्थान) में पहुँच गया हो। "
                   "क्रिया ‘प्रयोजयेत्’ है: ‘देना चाहिए’। मात्रा या विधि का "
                   "कोई वर्णन इस श्लोक में नहीं है।"),
    "hook": "पीलु-आरग्वध-द्राक्षा-द्रवन्ती-निचुल: दोष पक्वाशय में हो तो विरेचन के लिए।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 10 names drugs to be administered for which treatment?",
            ("Purgation (विरेक)",
             "विरेकार्थम् means 'for the purpose of purgation'."),
            [("Emesis", "The verse does not use the word for emesis; it says विरेक."),
             ("Head-purging", "Nothing in the verse mentions the head; the condition is the pakvāśaya, the lower gut."),
             ("Oil enema", "The oil enema (अनुवासन) is not named in this verse.")],
            "विरेकार्थं प्रयोजयेत् = one should administer for purgation.",
            "Verse 10: these drugs are for purgation, when the doṣa is in the pakvāśaya."),
        match(1, "Match each word of verse 10 to its meaning.",
              [["विरेकार्थम्", "for the purpose of purgation"],
               ["पक्वाशयगते", "gone to the pakvāśaya (lower gut)"],
               ["दोषे", "when the doṣa"],
               ["प्रयोजयेत्", "one should administer"]],
              "These four words of the second line carry the condition and the instruction.",
              "विरेकार्थम् = for purgation; पक्वाशयगते = gone to the lower gut; दोषे = when the doṣa; प्रयोजयेत् = one should administer."),
        fill(2, "The word in verse 10 for 'purgation' is ____ (type the stem in Devanagari, without the ending -अर्थम्).",
             ["विरेक", "विरेकः", "विरेकं", "विरेकम्"],
             "The compound is विरेकार्थम् = विरेक + अर्थम्.",
             "-अर्थम् at the end of a compound gives 'for the purpose of'; so विरेकार्थम् is 'for purgation'.",
             "विरेक + अर्थम् → विरेकार्थम् (अ + अ → आ) = for the purpose of purgation."),
        mcq("discriminate", 3, "Which is the right split of पीलून्यारग्वधम्?",
            ("पीलूनि + आरग्वधम्",
             "इ before an unlike vowel becomes य्, and the vowel joins it: इ + आ gives या."),
            [("पीलून् + यारग्वधम्", "यारग्वधम् is not a word."),
             ("पीलूनि + अरग्वधम्", "The second word is आरग्वधम् with long आ; with short अ it would be written पीलून्यरग्वधम्."),
             ("पीलुनी + आरग्वधम्", "The plural of पीलु here is पीलूनि; पीलुनी is not the form in the verse.")],
            "पीलून्यारग्वधम् = पीलूनि (pīlu fruits) + आरग्वधम् (āragvadha).",
            "इ + असमान स्वर → य् + स्वर: पीलूनि + आरग्वधम् → पीलून्यारग्वधम्."),
        multi("apply", 4, "Which of these does verse 10 say?",
              [("The drugs are for purgation", "Right: विरेकार्थम्."),
               ("They are used when the doṣa has gone to the pakvāśaya", "Right: पक्वाशयगते दोषे."),
               ("Grape (द्राक्षा) is one of the drugs named", "Right: द्राक्षां is in the first line."),
               ("They are used in udāvarta", "Udāvarta is named in verse 13, for another list."),
               ("They are given in a fixed dose", "The verse gives no dose.")],
              [0, 1, 2],
              "The first line names the drugs; the second line gives the condition and the purpose.",
              "Verse 10: five drugs; condition = doṣa in the pakvāśaya; purpose = purgation."),
        mcq("transfer", 5,
            "A made-up practice line reads पक्वाशयगते दोषे वमनार्थं प्रयोजयेत्, with वमन meaning emesis. What does it say?",
            ("Administer for emesis when the doṣa has gone to the pakvāśaya",
             "Same frame as verse 10: only the purpose word changes, विरेक → वमन."),
            [("Administer for purgation when the doṣa has gone to the pakvāśaya", "That is verse 10; here the purpose word is वमन."),
             ("Administer for emesis after the doṣa has left the pakvāśaya", "-गते means 'gone to', not 'left'."),
             ("Do not administer for emesis when the doṣa has gone to the pakvāśaya", "प्रयोजयेत् says 'one should administer', not a prohibition.")],
            "The frame '… गते दोषे … अर्थं प्रयोजयेत्' reads 'when the doṣa has gone to …, administer for …'. This is a grammar drill, not a medical statement.",
            "X-गते दोषे Y-अर्थं प्रयोजयेत् = administer for Y when the doṣa has gone to X.",
            teaches="Once the frame is clear, you can read the condition and purpose of any similar line by the words before -गते and -अर्थम्."),
    ],
}

NOTES_HI = {}
AIDS = {}

NOTES_HI["10"] = ("संधियाँ जाँची: पीलूनि + आरग्वधम् → पीलून्यारग्वधम् (इ का य्, फिर आ जुड़ा); पक्व + आशय → पक्वाशय (अ + आ → आ); "
                  "विरेक + अर्थम् → विरेकार्थम् (अ + अ → आ)। इस श्लोक में कोई पाठभेद या पाठ-दोष नहीं दिया गया। ‘विरेकार्थम्’ का रूप "
                  "क्रियाविशेषण की तरह (‘के लिए’) लिया गया है। ‘पक्वाशय’ का सामान्य अर्थ निचला आन्त्र है। श्लोक ९ और १० एक वाक्य हैं।")

AIDS["10"] = {
    "frame": "कौन से द्रव्य: पीलु, आरग्वध, द्राक्षा, द्रवन्ती, निचुल · कब: जब दोष पक्वाशय में पहुँच गया हो · किसलिए: विरेचन। (श्लोक ९ से चलता वाक्य।)",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["पीलून्यारग्वधं", "द्राक्षां", "द्रवन्तीं", "निचुलानि", "च"]},
        {"label": "दूसरी पंक्ति",
         "items": ["पक्वाशयगते", "दोषे", "विरेकार्थं", "प्रयोजयेत्"]}]},
    "sandhi": "इ + आ → या: पीलूनि + आरग्वधम् → पीलून्यारग्वधम्। अ + आ → आ: पक्व + आशय → पक्वाशय; विरेक + अर्थम् → विरेकार्थम्।",
    "anchors": "विरेकार्थम् = विरेक (विरेचन) + अर्थम् (के लिए) · पक्वाशय = पक्व + आशय · गते = गया हुआ (सप्तमी: ‘दोषे’ के साथ) · प्रयोजयेत् ← प्र + √युज् (प्रेरणार्थक): ‘प्रयोग में दे’।",
    "chunks": "पीलून्यारग्वधं द्राक्षां | द्रवन्तीं निचुलानि च ‖ पक्वाशयगते दोषे | विरेकार्थं प्रयोजयेत्।",
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "पाटलां चाग्निमन्थं च",
    "question": "What does verse 11 contain, and where does its sentence finish?",
    "rule": ("Verse 11 is a list of drug names, all objects of a verb that "
             "does not appear here: pāṭalā, agnimantha, bilva, śyonāka, "
             "kāśmarya, śālaparṇī, pṛśniparṇī, nidigdhikā. The verb is "
             "युञ्ज्यात् in verse 13."),
    "limits": ("The verse names drugs only: no use, no condition, no dose. "
               "One edition footnote offers the reading पाटलिं for पाटलां. "
               "The identifications in the glosses are conventional."),
    "explain_hi": ("श्लोक ११ से १३ तक एक ही सूची चलती है, जिसकी क्रिया "
                   "‘युञ्ज्यात्’ (प्रयोग करे) श्लोक १३ में आती है। इसलिए यहाँ केवल "
                   "औषधों के नाम हैं, सब द्वितीया (कर्म) में: पाटला, अग्निमन्थ, "
                   "बिल्व, श्योनाक, काश्मर्य, शालपर्णी, पृश्निपर्णी और निदिग्धिका। "
                   "इस श्लोक में न रोग बताया है, न प्रयोग का तरीका। संस्करण की "
                   "टिप्पणी में ‘पाटलां’ की जगह ‘पाटलिं’ पाठ भी दिया गया है।"),
    "hook": "श्लोक ११: केवल नाम (कर्म); ‘युञ्ज्यात्’ आएगा श्लोक १३ में।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 11 mainly contain?",
            ("A list of drug names; the verb comes in verse 13",
             "Every name in it is a drug, and the list is completed by युञ्ज्यात् in verse 13."),
            [("A list of diseases", "No disease is named in this verse."),
             ("A list of doses", "No quantity is named."),
             ("A list of the sages who taught", "The names are all drugs, not teachers.")],
            "The verse is a list of accusative drug names whose verb comes later.",
            "Verse 11: drug names only; the verb is in verse 13."),
        order(1, "Put these four drugs in the order of verse 11.",
              ["पाटलां", "अग्निमन्थं", "बिल्वं", "श्योनाकम्"],
              "These four make up the first line, in this order.",
              "पाटला → अग्निमन्थ → बिल्व → श्योनाक."),
        fill(2, "The first drug of the second line is ____ (type it in Devanagari).",
             ["काश्मर्यं", "काश्मर्यम्", "काश्मर्य"],
             "The second line opens with काश्मर्यं.",
             "In this verse each name is accusative singular (-म्/-ं masculine, -ाम्/-ीम् feminine): the drug is the object of the verb that comes later, in verse 13.",
             "Here the accusative singular names are objects of the verb still to come."),
        mcq("discriminate", 3, "Which is the right split of चाग्निमन्थम्?",
            ("च + अग्निमन्थम्", "अ + अ gives आ, so च + अग्निमन्थम् is written चाग्निमन्थम्."),
            [("चा + अग्निमन्थम्", "There is no word चा here."),
             ("च + आग्निमन्थम्", "The drug is अग्निमन्थ with short अ; the long आ comes from the join."),
             ("चाग् + निमन्थम्", "निमन्थम् is not a word in this verse.")],
            "चाग्निमन्थम् = च (and) + अग्निमन्थम्.",
            "च + अग्निमन्थम् → चाग्निमन्थम् (अ + अ → आ)."),
        multi("apply", 4, "Which of these statements about verse 11 are right?",
              [("It names bilva", "Right: बिल्वं is in the first line."),
               ("It names śālaparṇī and pṛśniparṇī", "Right: both are in the second line."),
               ("Its list is governed by the verb युञ्ज्यात् of verse 13", "Right: the sentence runs on to verse 13."),
               ("It names barley (यव)", "Barley is named in verse 12."),
               ("It says which disease each drug is for", "No disease is named here.")],
              [0, 1, 2],
              "Verse 11 only names drugs; the use is given later in the same sentence.",
              "Verse 11 = names; use = verse 13."),
        mcq("transfer", 5,
            "A made-up verse reads only बलां च बिल्वं च, and the next verse ends with युञ्ज्यात्. Is the first verse a complete statement?",
            ("No; its two names are objects of the verb in the next verse",
             "Like verse 11, it is a list waiting for its verb."),
            [("Yes; two drug names alone say how to use them", "A bare list says nothing about use."),
             ("Yes; च च means 'one should use'", "च means 'and' and is not a verb."),
             ("No; बलां and बिल्वं are verbs", "Both are nouns.")],
            "Verse 11 and this made-up verse are both lists; the verb arrives later, as युञ्ज्यात् does in verse 13.",
            "A list of accusatives is completed by a verb in a later verse.",
            teaches="When a verse is only a list of accusative names, look ahead for the verb that governs it."),
    ],
}

NOTES_HI["11"] = ("संधियाँ जाँची: च + अग्निमन्थम् → चाग्निमन्थम् (अ + अ → आ); श्योनाकम् + एव → श्योनाकमेव (म् अगले स्वर से सटा)। "
                  "पाठभेद: संस्करण की टिप्पणी ‘पाटलां’ की जगह ‘पाटलिं’ देती है। सूची श्लोक १३ की क्रिया ‘युञ्ज्यात्’ से पूरी होती है। "
                  "‘श्योनाकमेव च’ में ‘एव’ केवल बलाघात है (‘श्योनाक भी’)। औषधों की पहचान परम्परागत है।")

AIDS["11"] = {
    "frame": "क्या: औषधों की सूची (आठ नाम) · कर्म-रूप में · क्रिया ‘युञ्ज्यात्’ श्लोक १३ में · पाठभेद: ‘पाटलिं’।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["पाटलां", "चाग्निमन्थं", "च", "बिल्वं", "श्योनाकमेव", "च"]},
        {"label": "दूसरी पंक्ति",
         "items": ["काश्मर्यं", "शालपर्णीं", "च", "पृश्निपर्णीं", "निदिग्धिकाम्"]}]},
    "sandhi": "अ + अ → आ: च + अग्निमन्थम् → चाग्निमन्थम्। म् + स्वर: श्योनाकम् + एव → श्योनाकमेव (म् अगले स्वर से सट जाता है)।",
    "anchors": "सभी नाम द्वितीया एकवचन: -म् / -ं (पुं०, नपुं०), -ाम् / -ीम् (स्त्री०)। ये ‘युञ्ज्यात्’ (श्लोक १३) के कर्म हैं।",
    "chunks": "पाटलां चाग्निमन्थं च | बिल्वं श्योनाकमेव च ‖ काश्मर्यं शालपर्णीं च | पृश्निपर्णीं निदिग्धिकाम्।",
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "बलां श्वदंष्ट्रां बृहतीम्",
    "question": "What does verse 12 add to the list, and what does सपुनर्नवम् say about the castor?",
    "rule": ("The list goes on: balā, śvadaṃṣṭrā, bṛhatī, castor together "
             "with punarnavā (सपुनर्नवम्), barley, horse gram, jujube "
             "fruits, guḍūcī and madana fruits. The verb is युञ्ज्यात् in "
             "verse 13."),
    "limits": ("Still only names: no use, no condition, no dose. सपुनर्नवम् "
               "is read as 'castor together with punarnavā'; the notes say "
               "other ways of reading it give the same sense. Confidence is "
               "medium, and the glosses are conventional."),
    "explain_hi": ("सूची श्लोक ११ से चलती हुई यहाँ आगे बढ़ती है; क्रिया अब भी "
                   "श्लोक १३ में है। नाम हैं: बला, श्वदंष्ट्रा, बृहती, एरण्ड "
                   "(‘सपुनर्नवम्’, यानी पुनर्नवा के साथ), यव, कुलत्थ, कोल, "
                   "गुडूची और मदन के फल। सब द्वितीया में हैं, पर लिंग-वचन अलग: "
                   "‘यवान्, कुलत्थान्’ पुँल्लिंग बहुवचन, ‘कोलानि, मदनानि’ "
                   "नपुंसक बहुवचन, ‘बलाम्, गुडूचीम्’ स्त्रीलिंग एकवचन। "
                   "‘सपुनर्नवम्’ में ‘स-’ का अर्थ ‘साथ’ है।"),
    "hook": "श्लोक १२: सूची जारी; ‘स-’ = साथ (सपुनर्नवम्); क्रिया फिर भी श्लोक १३ में।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which of these is named in verse 12?",
            ("Barley (यव)", "यवान् is in the second line."),
            [("Grape (द्राक्षा)", "Grape is named in verse 10, in the purgation list."),
             ("Bilva", "Bilva is named in verse 11."),
             ("Salts (लवण)", "Salts are named in verse 13.")],
            "Verse 12 names barley as यवान् in the second line.",
            "Each verse of the list adds new names; barley is in verse 12."),
        match(1, "Match each word of verse 12 to its form.",
              [["यवान्", "masculine plural accusative (barley)"],
               ["कोलानि", "neuter plural accusative (jujube fruits)"],
               ["बलाम्", "feminine singular accusative"],
               ["एरण्डम्", "masculine singular accusative (castor)"]],
              "All four are accusative; they differ in gender and number.",
              "यवान् = m. acc. pl.; कोलानि = n. acc. pl.; बलाम् = f. acc. sg.; एरण्डम् = m. acc. sg."),
        fill(2, "The word meaning 'together with punarnavā' is ____ (type it in Devanagari).",
             ["सपुनर्नवम्", "सपुनर्नवं"],
             "The first line ends with सपुनर्नवम्.",
             "स- at the start of a compound means 'together with': सपुनर्नवम् describes the castor, 'with punarnavā'.",
             "स- + noun = 'together with that noun' (a sahārtha bahuvrīhi)."),
        mcq("discriminate", 3, "Which is the right split of बृहतीमेरण्डम्?",
            ("बृहतीम् + एरण्डम्", "The final म् of बृहतीम् simply joins the vowel that follows."),
            [("बृहती + एरण्डम्", "That would be written बृहत्येरण्डम्, because ई becomes य् before a different vowel."),
             ("बृहतीम् + रण्डम्", "रण्डम् is not a word; the castor is एरण्ड."),
             ("बृहती + मेरण्डम्", "मेरण्डम् is not a word.")],
            "बृहतीमेरण्डम् = बृहतीम् (bṛhatī) + एरण्डम् (castor).",
            "म् + स्वर: the म् is carried over onto the next vowel without any change."),
        multi("apply", 4, "Which forms in verse 12 are neuter plural?",
              [("कोलानि", "Right: n. acc. pl., ending -आनि."),
               ("मदनानि", "Right: n. acc. pl., ending -आनि."),
               ("यवान्", "Masculine plural, ending -आन्."),
               ("कुलत्थान्", "Masculine plural, ending -आन्."),
               ("एरण्डम्", "Singular, not plural.")],
              [0, 1],
              "Neuter plural accusative ends in -आनि; masculine plural accusative ends in -आन्.",
              "-आनि = neuter plural; -आन् = masculine plural."),
        mcq("transfer", 5,
            "In a made-up phrase वृक्षं सफलम्, what does सफलम् add about the tree?",
            ("The tree together with fruit",
             "स- means 'together with', as in सपुनर्नवम्, and agrees with वृक्षम्."),
            [("The tree without fruit", "Without would need a negating अ-, not स-."),
             ("A second thing, the fruit, besides the tree", "सफलम् is one describing word agreeing with वृक्षम्, not a separate item."),
             ("Only the fruit, not the tree", "वृक्षं is the main word; सफलम् describes it.")],
            "सफलम् = स + फलम्, an adjective of वृक्षम्: the same pattern as सपुनर्नवम् describing एरण्डम्.",
            "स- + noun, agreeing with a noun = 'together with'.",
            teaches="A स- + noun compound that agrees with a main noun (the sahārtha type of सपुनर्नवम्) tells you what the main noun comes with."),
    ],
}

NOTES_HI["12"] = ("विश्वास: मध्यम। ‘सपुनर्नवम्’ को ‘पुनर्नवा सहित एरण्ड’ पढ़ा गया है (बहुव्रीहि, एरण्डम् का विशेषण); टिप्पणी के अनुसार "
                  "‘पुनर्नवा के साथ वाला एरण्ड’ पढ़ने पर भी अर्थ वही रहता है। संधि: बृहतीम् + एरण्डम् → बृहतीमेरण्डम् (म् सटा)। "
                  "‘यवान् कुलत्थान्’ में न् बिना परिवर्तन के रहता है (क से पहले)। पाठभेद कोई नहीं। पहचानें परम्परागत हैं। "
                  "सूची की क्रिया श्लोक १३ में है।")

AIDS["12"] = {
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["बलां", "श्वदंष्ट्रां", "बृहतीमेरण्डं", "सपुनर्नवम्"]},
        {"label": "दूसरी पंक्ति",
         "items": ["यवान्", "कुलत्थान्", "कोलानि", "गुडूचीं", "मदनानि", "च"]}]},
    "sandhi": "म् + स्वर: बृहतीम् + एरण्डम् → बृहतीमेरण्डम् (म् अगले स्वर से सट जाता है)। स- = साथ: स + पुनर्नवम् → सपुनर्नवम्।",
    "anchors": "सभी द्वितीया · पुं० बहुवचन -आन्: यवान्, कुलत्थान् · नपुं० बहुवचन -आनि: कोलानि, मदनानि · स्त्री० एकवचन: बलाम्, श्वदंष्ट्राम्, बृहतीम्, गुडूचीम्।",
    "chunks": "बलां श्वदंष्ट्रां बृहतीमेरण्डं सपुनर्नवम् ‖ यवान् कुलत्थान् कोलानि गुडूचीं मदनानि च।",
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "पलाशं कत्तृणं चैव",
    "question": "What closes the list in verse 13, and in which conditions does it say to use the drugs?",
    "rule": ("Palāśa, kattṛṇa, oils/fats and salts end the list. The verb "
             "युञ्ज्यात् ('one should use') governs verses 11 to 13: in "
             "udāvarta, in vibandha (obstructions), and in āsthāpana "
             "enemas."),
    "limits": ("'In āsthāpana' may also be read 'for āsthāpana enemas'. "
               "Vibandha is rendered 'obstructions' (retention of stool or "
               "wind). The verse does not say which drug suits which "
               "condition, and gives no dose."),
    "explain_hi": ("यह श्लोक सूची को पूरा करता है और वाक्य की क्रिया देता है। "
                   "आख़िरी नाम हैं पलाश, कत्तृण, स्नेह (तेल-घी आदि) और "
                   "लवण। फिर कहा गया है ‘युञ्ज्यात्’: प्रयोग करे: उदावर्त "
                   "में, विबन्ध (मल या वायु के रुकने) में, और आस्थापन में। "
                   "‘आस्थापन’ काढ़े की बस्ति है; ‘आस्थापनेषु’ को ‘आस्थापन के "
                   "लिए’ भी पढ़ा जा सकता है। यह क्रिया श्लोक ११ और १२ की सूचियों "
                   "पर भी लागू होती है।"),
    "hook": "श्लोक १३: सूची का अन्त + क्रिया ‘युञ्ज्यात्’: उदावर्त, विबन्ध, आस्थापन में।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In which conditions does verse 13 say to use the drugs?",
            ("In udāvarta, in obstructions (vibandha) and in āsthāpana enemas",
             "उदावर्ते, विबन्धेषु and आस्थापनेषु name them."),
            [("When the doṣa has gone to the pakvāśaya, for purgation", "That is the condition of verse 10."),
             ("In weak digestion and in pain", "Those are the effects of the gruel of verse 18, not the conditions here."),
             ("In every disease", "The verse names only these conditions.")],
            "The second line gives the conditions: उदावर्ते, विबन्धेषु, आस्थापनेषु.",
            "Verse 13: use in udāvarta, in vibandha and in āsthāpana."),
        match(1, "Match each word of verse 13 to its meaning.",
              [["उदावर्ते", "in upward-moving wind (udāvarta)"],
               ["विबन्धेषु", "in obstructions"],
               ["आस्थापनेषु", "in decoction enemas (āsthāpana)"],
               ["युञ्ज्यात्", "one should use"]],
              "These four words of the second line carry the conditions and the instruction.",
              "उदावर्ते = in udāvarta; विबन्धेषु = in obstructions; आस्थापनेषु = in āsthāpana; युञ्ज्यात् = one should use."),
        fill(2, "The verb of the sentence in verses 11 to 13 is ____ (type the base form 'one should use' in Devanagari).",
             ["युञ्ज्यात्", "युञ्ज्याद्"],
             "The second line has युञ्ज्यादास्थापनेषु = युञ्ज्यात् + आस्थापनेषु.",
             "युञ्ज्यात् is a third person singular optative: 'one should use'. Its final त् becomes द् before the vowel आ.",
             "युञ्ज्यात् + आस्थापनेषु → युञ्ज्यादास्थापनेषु."),
        mcq("discriminate", 3, "स्नेहांश्च is स्नेहान् + च. What happens at the join?",
            ("न् becomes an anusvāra and श् is added before च", "न् + च gives ंश्च, as in स्नेहांश्च."),
            [("न् becomes म् before च", "The change is to an anusvāra with श् added; there is no म् in स्नेहांश्च."),
             ("A visarga becomes श् before च", "There is no visarga: स्नेहान् ends in न्."),
             ("Nothing changes except that the space is closed", "The न् changes to ंश्.")],
            "स्नेहांश्च = स्नेहान् (oils/fats, acc. pl.) + च.",
            "-आन् + च → -ांश्च."),
        multi("apply", 4, "Which of these are named in verse 13 as conditions or uses?",
              [("Udāvarta", "Right: उदावर्ते."),
               ("Vibandha, obstructions", "Right: विबन्धेषु."),
               ("Āsthāpana enemas", "Right: आस्थापनेषु."),
               ("The doṣa gone to the pakvāśaya", "That is the condition of verse 10."),
               ("The oil enema (anuvāsana)", "The oil enema is named in verse 14.")],
              [0, 1, 2],
              "Verse 13 names three: udāvarta, vibandha and āsthāpana.",
              "Verse 13 gives the verb युञ्ज्यात् and the three places of use."),
        mcq("transfer", 5,
            "A made-up line ends विबन्धे शूले च प्रयोजयेत् (शूल = pain). By the pattern of verse 13, how do you read विबन्धे and शूले?",
            ("'In obstruction and in pain': the -ए ending shows the condition",
             "Like उदावर्ते and विबन्धेषु, the locative gives the condition in which to use."),
            [("'From obstruction and pain': they are the source", "Source would need the ablative, ending -आत्."),
             ("'By obstruction and pain': they are the means", "Means would be the instrumental, ending -एन."),
             ("'Of obstruction and pain': they belong to something", "That would be the genitive, ending -स्य.")],
            "-ए (singular) and -एषु (plural) of a masculine noun give 'in …', as in उदावर्ते and विबन्धेषु.",
            "Locative -ए / -एषु = 'in …': the condition in which to use.",
            teaches="Reading the ending of a word for a disorder tells you whether it is the condition, the means or the source."),
    ],
}

NOTES_HI["13"] = ("संधियाँ जाँची: च + एव → चैव (अ + ए → ऐ); स्नेहान् + च → स्नेहांश्च (न् + च → ंश्च); "
                  "युञ्ज्यात् + आस्थापनेषु → युञ्ज्यादास्थापनेषु (त् → द् स्वर से पहले)। पाठभेद कोई नहीं। ‘विबन्धेषु’ का अनुवाद ‘रुकावट’ "
                  "(मल या वायु का रुकना) है। ‘आस्थापनेषु’ को ‘आस्थापन में’ और ‘आस्थापन के लिए’ दोनों तरह पढ़ा जा सकता है। "
                  "क्रिया ‘युञ्ज्यात्’ श्लोक ११ और १२ की सूचियों पर भी लागू होती है।")

AIDS["13"] = {
    "frame": "क्या: पलाश, कत्तृण, स्नेह, लवण (सूची का अन्त) · क्रिया: युञ्ज्यात् (श्लोक ११–१३ पर) · कहाँ: उदावर्त, विबन्ध, आस्थापन में।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["पलाशं", "कत्तृणं", "चैव", "स्नेहांश्च", "लवणानि", "च"]},
        {"label": "दूसरी पंक्ति",
         "items": ["उदावर्ते", "विबन्धेषु", "युञ्ज्यादास्थापनेषु", "च"]}]},
    "sandhi": "न् + च → ंश्च: स्नेहान् + च → स्नेहांश्च। त् → द् (स्वर से पहले): युञ्ज्यात् + आस्थापनेषु → युञ्ज्यादास्थापनेषु। अ + ए → ऐ: च + एव → चैव।",
    "contrast": "आस्थापन = काढ़े की बस्ति (यहीं, श्लोक १३) ↔ अनुवासन = तैल की बस्ति (अगला श्लोक १४)। दोनों नाम अलग हैं; इस श्लोक में केवल आस्थापन आया है।",
    "chunks": "पलाशं कत्तृणं चैव | स्नेहांश्च लवणानि च ‖ उदावर्ते विबन्धेषु | युञ्ज्यादास्थापनेषु च।",
}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "अत एवौषधगणात्",
    "question": "What does verse 14 say is prepared from the same group of drugs, and what does it say has been stated?",
    "rule": ("From this same group of drugs the anuvāsana (oil enema) is "
             "to be prepared, one that destroys wind (मारुतघ्नम्). Thus has "
             "been stated the compendium relating to the five procedures "
             "(पाञ्चकर्मिकः संग्रहः)."),
    "limits": ("मारुतघ्नम् is taken with अनुवासनम्; it could also be read as "
               "a separate remark, with the same sense. 'This same group' "
               "refers back to a group already named; the data does not say "
               "which verses it covers, and the verse gives no dose."),
    "explain_hi": ("श्लोक १४ दो बातें कहता है। पहली: ‘अत एव औषधगणात्’, इसी "
                   "औषधगण से अनुवासन (तैलबस्ति) की कल्पना करनी चाहिए "
                   "(संकल्प्यम्), जो ‘मारुतघ्न’ यानी वात का नाश करने वाला "
                   "है। दूसरी: ‘इति प्रोक्तः संग्रहः पाञ्चकर्मिकः’, इस तरह "
                   "पञ्चकर्म से सम्बन्धित संग्रह कहा गया। ‘पाञ्चकर्मिक’ का "
                   "अर्थ है ‘पाँच कर्मों से सम्बन्ध रखने वाला’। श्लोक में न "
                   "मात्रा है, न विधि।"),
    "hook": "इसी औषधगण से अनुवासन (वातनाशक); इति पञ्चकर्म का संग्रह पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 14 say is to be prepared from the same group of drugs?",
            ("The anuvāsana, the oil enema",
             "संकल्प्यमनुवासनम् = the anuvāsana is to be prepared."),
            [("A gruel (यवागू)", "Gruels are announced in verse 17."),
             ("An emetic", "No emetic is mentioned in this verse."),
             ("A purgative", "Purgation was the purpose in verse 10, not here.")],
            "अत एव औषधगणात् संकल्प्यम् अनुवासनम्: from this very group, the oil enema is to be prepared.",
            "Verse 14: the oil enema, anuvāsana, comes from the same drug group."),
        order(1, "Put these phrases in the order of verse 14.",
              ["अत एवौषधगणात्", "संकल्प्यमनुवासनम्", "मारुतघ्नमिति", "प्रोक्तः संग्रहः पाञ्चकर्मिकः"],
              "The first line gives the source and the enema; the second line the quality and the closing words.",
              "अत एवौषधगणात् → संकल्प्यमनुवासनम् → मारुतघ्नमिति → प्रोक्तः संग्रहः पाञ्चकर्मिकः."),
        fill(2, "The oil enema is called ____ in the verse (type its name in Devanagari).",
             ["अनुवासनम्", "अनुवासनं", "अनुवासन"],
             "The first line ends with संकल्प्यमनुवासनम्.",
             "अनुवासनम् ends in -म् as the subject (nominative) of 'is to be prepared': संकल्प्यम् अनुवासनम्.",
             "अनुवासन = oil enema, here the thing to be prepared."),
        mcq("discriminate", 3, "Which is the right split of एवौषधगणात्?",
            ("एव + औषधगणात्", "अ + औ gives औ, so एव + औषध… is written एवौषध…."),
            [("एव + उषधगणात्", "The word is औषध, with औ, not उषध."),
             ("एवो + औषधगणात्", "There is no word एवो."),
             ("ए + वौषधगणात्", "वौषधगणात् is not a word.")],
            "एवौषधगणात् = एव + औषध-गणात्, 'from the very group of drugs'.",
            "अ + औ → औ: एव + औषध → एवौषध."),
        multi("apply", 4, "Which statements fit verse 14?",
              [("The oil enema is prepared from the same drug group", "Right: अत एव औषधगणात्."),
               ("The oil enema is called wind-destroying", "Right: मारुतघ्नम्."),
               ("The compendium relating to the five procedures has been stated", "Right: प्रोक्तः संग्रहः पाञ्चकर्मिकः."),
               ("The verse gives the dose of the oil", "No dose is given."),
               ("The verse says to use the drugs in udāvarta", "Udāvarta is named in verse 13.")],
              [0, 1, 2],
              "The first line gives the source and the enema; the second line the quality and the closing words.",
              "Verse 14: anuvāsana from the same group; wind-destroying; compendium of the five procedures stated."),
        mcq("transfer", 5,
            "A made-up line calls a drug ज्वरघ्नम् (ज्वर = fever). Following मारुतघ्नम्, what does it say?",
            ("It destroys fever", "-घ्न at the end of a compound means 'destroying', as in मारुतघ्नम्."),
            [("It causes fever", "-घ्न destroys; it does not cause."),
             ("It resembles fever", "There is no word for 'resembling' in the compound."),
             ("It is made from fever", "The first member names what is destroyed.")],
            "मारुत-घ्नम् = wind-destroying, so ज्वर-घ्नम् = fever-destroying.",
            "X-घ्न = destroying X.",
            teaches="The last part -घ्न tells what the thing does; the first part names what it acts on."),
    ],
}

NOTES_HI["14"] = ("संधियाँ जाँची: अतः + एव → अत एव (अः के बाद भिन्न स्वर: विसर्ग लुप्त); एव + औषधगणात् → एवौषधगणात् (अ + औ → औ); "
                  "संकल्प्यम् + अनुवासनम् → संकल्प्यमनुवासनम् और मारुतघ्नम् + इति → मारुतघ्नमिति (म् अगले स्वर से सटा)। "
                  "टिप्पणी: ‘मारुतघ्नम्’ अनुवासनम् का विशेषण (यहाँ लिया गया) या अलग कथन, दोनों पढ़े जा सकते हैं, अर्थ वही। पाठभेद कोई नहीं। "
                  "‘पाञ्चकर्मिकः’ = पञ्चकर्म से सम्बन्धित (तद्धित -इक)।")

AIDS["14"] = {
    "frame": "कहाँ से: इसी औषधगण से · क्या बने: अनुवासन (तैलबस्ति) · कैसा: वातनाशक · अन्त: पञ्चकर्म का संग्रह कहा गया।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["अत", "एवौषधगणात्", "संकल्प्यमनुवासनम्"]},
        {"label": "दूसरी पंक्ति",
         "items": ["मारुतघ्नमिति", "प्रोक्तः", "संग्रहः", "पाञ्चकर्मिकः"]}]},
    "sandhi": "अतः + एव → अत एव (अः के बाद भिन्न स्वर: विसर्ग लुप्त)। अ + औ → औ: एव + औषध → एवौषध। म् + स्वर: संकल्प्यम् + अनुवासनम् → संकल्प्यमनुवासनम्।",
    "contrast": "आस्थापन = काढ़े की बस्ति (श्लोक १३) ↔ अनुवासन = तैल की बस्ति (श्लोक १४, ‘मारुतघ्न’)। यहाँ अनुवासन उसी औषधगण से बनता है।",
    "chunks": "अत एवौषधगणात् | संकल्प्यमनुवासनम् ‖ मारुतघ्नमिति प्रोक्तः | संग्रहः पाञ्चकर्मिकः।",
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "तान्युपस्थितदोषाणाम्",
    "question": "What does verse 15 tell the physician to do for those whose doṣas are aroused?",
    "rule": ("For those whose doṣas are aroused (उपस्थितदोष), by providing "
             "oleation and sudation (स्नेहस्वेद), one should perform the "
             "five procedures (पञ्चकर्माणि), considering dose and time "
             "(मात्राकालौ)."),
    "limits": ("The verse does not name the five procedures and gives no "
               "dose or time. The case of तानि (drugs as means or as "
               "objects) is open in the notes, and 'after' oleation and "
               "sudation is an interpretation of the instrumental, which "
               "literally means 'by means of providing'. Confidence: medium."),
    "explain_hi": ("यह श्लोक बताता है कि पाँचों कर्म किनके लिए और किस तैयारी "
                   "के साथ करने हैं। जिनके दोष ‘उपस्थित’ (उभरे हुए) हैं, उनके "
                   "लिए ‘स्नेहस्वेदोपपादनैः’, यानी स्नेहन और स्वेदन के प्रबन्ध "
                   "से, पञ्चकर्म ‘कुर्वीत’ (करे)। साथ ही ‘मात्राकालौ विचारयन्’: "
                   "मात्रा और काल का विचार करता हुआ। ‘तानि’ = वे (द्रव्य); उसकी विभक्ति टिप्पणी में खुली रखी गई "
                   "है। पाँच कर्मों के नाम यहाँ नहीं दिए गए।"),
    "hook": "दोष उभरें → स्नेहन-स्वेदन के साथ पञ्चकर्म, मात्रा और काल देखते हुए।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which two things does verse 15 tell the physician to consider?",
            ("Dose and time", "मात्राकालौ विचारयन् = considering dose and time."),
            [("Season and place", "Neither is named in the verse."),
             ("Strength and age", "Neither is named in the verse."),
             ("Weight and height", "Neither is named in the verse.")],
            "मात्राकालौ is the pair 'dose and time'; विचारयन् is 'considering'.",
            "Verse 15: consider dose (मात्रा) and time (काल)."),
        match(1, "Match each word of verse 15 to its meaning.",
              [["उपस्थितदोषाणाम्", "of those whose doṣas are aroused"],
               ["स्नेहस्वेदोपपादनैः", "by providing oleation and sudation"],
               ["पञ्चकर्माणि", "the five procedures"],
               ["विचारयन्", "considering"]],
              "Each word carries one part of the instruction.",
              "उपस्थितदोषाणाम् = of those with aroused doṣas; स्नेहस्वेदोपपादनैः = by providing oleation and sudation; पञ्चकर्माणि = the five procedures; विचारयन् = considering."),
        fill(2, "The verb meaning 'should perform' is ____ (type it in Devanagari).",
             ["कुर्वीत"],
             "The second line has पञ्चकर्माणि कुर्वीत.",
             "कुर्वीत is a third person singular optative (middle voice) of √कृ: 'one should do'.",
             "कुर्वीत = one should perform."),
        mcq("discriminate", 3, "Which is the right split of तान्युपस्थितदोषाणाम्?",
            ("तानि + उपस्थितदोषाणाम्", "इ before an unlike vowel becomes य्: इ + उ gives यु."),
            [("तान् + युपस्थितदोषाणाम्", "युपस्थित… is not a word."),
             ("ताना + उपस्थितदोषाणाम्", "The word is तानि, the neuter plural of 'that'."),
             ("तानि + पस्थितदोषाणाम्", "The word is उपस्थित, with its उ.")],
            "तानि (those) + उपस्थित-दोषाणाम् (of those with aroused doṣas).",
            "इ + उ → यु: तानि + उपस्थित → तान्युपस्थित."),
        multi("apply", 4, "Which statements fit verse 15?",
              [("Oleation and sudation are provided", "Right: स्नेहस्वेदोपपादनैः."),
               ("The five procedures are to be performed", "Right: पञ्चकर्माणि कुर्वीत."),
               ("Dose and time are to be considered", "Right: मात्राकालौ विचारयन्."),
               ("The five procedures are named one by one", "They are not named in this verse."),
               ("The dose is fixed at a quantity", "No quantity is given.")],
              [0, 1, 2],
              "The verse gives the preparation, the action and the care to be taken.",
              "Verse 15: oleation and sudation; five procedures; consider dose and time."),
        mcq("transfer", 5,
            "A made-up phrase reads बलकालौ विचारयन् (बल = strength). What does it say?",
            ("Considering strength and time",
             "The ending -औ of a pair joined by 'and' marks two things, as in मात्राकालौ."),
            [("Considering strength alone", "Two words are joined, and -औ marks two."),
             ("Considering two strengths", "बल and काल are different words."),
             ("Considering a strong time", "That would need a describing word, not a pair ending in -औ.")],
            "बलकालौ = बल + काल, a pair 'strength and time', like मात्राकालौ 'dose and time'.",
            "A pair joined into one word ending in -औ = 'X and Y' (two things).",
            teaches="A compound of two nouns with the ending -औ names two things together."),
    ],
}

NOTES_HI["15"] = ("विश्वास: मध्यम। संधियाँ जाँची: तानि + उपस्थित… → तान्युपस्थित… (इ + उ → यु); स्वेद + उपपादनैः → स्वेदोपपादनैः (अ + उ → ओ)। "
                  "‘तानि’ की विभक्ति अनिश्चित है (द्रव्य साधन या कर्म), टिप्पणी में ‘इनका प्रयोग करके’ लिया गया है; "
                  "‘स्नेहस्वेदोपपादनैः’ का ‘के बाद’ अर्थ व्याख्या है, शाब्दिक अर्थ ‘प्रबन्ध द्वारा’ है। ‘मात्राकालौ’ द्विवचन है (द्वन्द्व, -औ)। "
                  "पाठभेद कोई नहीं। पाँच कर्मों के नाम श्लोक में नहीं हैं।")

AIDS["15"] = {
    "frame": "किसके लिए: जिनके दोष उपस्थित हैं · कैसे: स्नेहन-स्वेदन के प्रबन्ध से · क्या: पाँच कर्म · ध्यान: मात्रा और काल।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["तान्युपस्थितदोषाणां", "स्नेहस्वेदोपपादनैः"]},
        {"label": "दूसरी पंक्ति",
         "items": ["पञ्चकर्माणि", "कुर्वीत", "मात्राकालौ", "विचारयन्"]}]},
    "sandhi": "इ + उ → यु: तानि + उपस्थित → तान्युपस्थित। अ + उ → ओ: स्वेद + उपपादनैः → स्वेदोपपादनैः।",
    "anchors": "पञ्चकर्माणि = पञ्च + कर्माणि (पाँच कर्म) · मात्राकालौ = मात्रा + काल, द्विवचन (-औ = ‘दो’) · उपस्थितदोष = जिसके दोष उपस्थित (उभरे) हों · विचारयन् = विचार करता हुआ।",
    "chunks": "तान्युपस्थितदोषाणां | स्नेहस्वेदोपपादनैः ‖ पञ्चकर्माणि कुर्वीत | मात्राकालौ विचारयन्।",
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "मात्राकालाश्रया युक्तिः",
    "question": "What does yukti rest on, where is success established, and who stands above whom?",
    "rule": ("Yukti (rational planning) rests on dose and time; success is "
             "established in yukti; the one who knows yukti stands above "
             "those who have knowledge of substances."),
    "limits": ("The verse does not define yukti beyond saying it rests on "
               "dose and time. 'Stands above' is figurative; the verse does "
               "not say that knowing substances is useless. The edition "
               "prints a stray comma after युक्तिः (a text flag); it "
               "does not change the sense."),
    "explain_hi": ("यह श्लोक युक्ति का सूत्र देता है। ‘मात्राकालाश्रया "
                   "युक्तिः’: युक्ति (विचारपूर्वक योजना) मात्रा और काल पर "
                   "आश्रित है। ‘सिद्धिर्युक्तौ प्रतिष्ठिता’: सफलता युक्ति "
                   "में टिकी है। ‘तिष्ठत्युपरि युक्तिज्ञः’: जो युक्ति जानता है "
                   "वह द्रव्यों का ज्ञान रखने वालों से ऊपर रहता है। श्लोक यह "
                   "नहीं कहता कि द्रव्य-ज्ञान बेकार है; वह केवल तुलना करता "
                   "है। छपे पाठ में ‘युक्तिः’ के बाद एक फालतू अल्पविराम है।"),
    "hook": "मात्रा-काल → युक्ति → सिद्धि; युक्ति जानने वाला द्रव्य जानने वालों से ऊपर।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "According to verse 16, what does yukti rest on?",
            ("Dose and time", "मात्राकालाश्रया युक्तिः = yukti has dose and time as its basis."),
            [("Knowledge of substances alone", "Knowledge of substances is what the lower group has, not the basis of yukti."),
             ("Success", "It is success (सिद्धि) that is established in yukti, not the reverse."),
             ("The patient's wishes", "Nothing like this is named in the verse.")],
            "The first words say it: मात्रा and काल are the basis (आश्रय) of yukti.",
            "Verse 16: yukti rests on dose and time."),
        order(1, "Put these in the order of the verse's chain, starting from the base.",
              ["मात्रा और काल", "युक्ति", "सिद्धि"],
              "Yukti rests on dose and time; success is established in yukti.",
              "मात्रा-काल → युक्ति → सिद्धि."),
        fill(2, "Success (सिद्धिः) is established in ____ (type the Devanagari word).",
             ["युक्तौ", "युक्ति", "युक्तिः"],
             "The verse says सिद्धिर्युक्तौ प्रतिष्ठिता.",
             "युक्तौ is the locative singular of युक्ति, 'in yukti'. Here -औ is not a dual ending.",
             "-औ can be a locative singular ending of a feminine noun in -इ, not only a dual."),
        mcq("discriminate", 3, "सिद्धिर्युक्तौ comes from सिद्धिः + युक्तौ. Which change happened?",
            ("The visarga after इ became र् before the voiced sound य",
             "After इ / उ, a visarga before a voiced sound becomes र्."),
            [("The visarga became ओ", "ओ appears only when the visarga follows अ."),
             ("The visarga dropped", "A visarga after इ does not drop before य; it becomes र्."),
             ("The visarga became श्", "श् appears before च / छ, not before य.")],
            "सिद्धिः + युक्तौ → सिद्धिर्युक्तौ.",
            "इः + घोष → इर् + घोष."),
        multi("apply", 4, "Which statements fit verse 16?",
              [("Yukti rests on dose and time", "Right: मात्राकालाश्रया युक्तिः."),
               ("Success is established in yukti", "Right: सिद्धिर्युक्तौ प्रतिष्ठिता."),
               ("The one who knows yukti stands above those with knowledge of substances", "Right: तिष्ठत्युपरि युक्तिज्ञः …."),
               ("Knowledge of substances is useless", "The verse only compares; it does not call it useless."),
               ("Yukti is the name of a drug", "Yukti is rational planning, not a drug.")],
              [0, 1, 2],
              "Each half-line of the verse gives one of the three right statements.",
              "Verse 16: yukti on dose and time; success in yukti; yukti-knower above substance-knowers."),
        mcq("transfer", 5,
            "Physician A knows many substances; physician B knows yukti, planning by dose and time. By this verse, who stands above?",
            ("Physician B, who knows yukti", "युक्तिज्ञः stands above those with knowledge of substances."),
            [("Physician A, who knows many substances", "Those with knowledge of substances stand below the yukti-knower."),
             ("Both equally", "The verse puts the yukti-knower above."),
             ("Neither; the verse does not compare them", "The verse does compare: तिष्ठत्युपरि युक्तिज्ञः.")],
            "The verse ranks the yukti-knower above those who have knowledge of substances.",
            "युक्तिज्ञ stands above द्रव्यज्ञानवत्.",
            teaches="Use the verse's comparison: the person who plans by dose and time ranks above one who only knows substances."),
    ],
}

NOTES_HI["16"] = ("पाठ-दोष (text_flag): छपे पाठ में ‘युक्तिः,’ के साथ एक फालतू अल्पविराम है; सुझाव ‘युक्तिः’। संधियाँ जाँची: "
                  "मात्राकाल + आश्रया → मात्राकालाश्रया (अ + आ → आ); सिद्धिः + युक्तौ → सिद्धिर्युक्तौ (इः + घोष → इर्); "
                  "तिष्ठति + उपरि → तिष्ठत्युपरि (इ + उ → यु); युक्तिज्ञः + द्रव्य… → युक्तिज्ञो द्रव्य… (अः + घोष → ओ)। "
                  "‘युक्तौ’ का -औ सप्तमी एकवचन है, द्विवचन नहीं। ‘द्रव्यज्ञानवताम्’ का शाब्दिक अर्थ ‘द्रव्य-ज्ञान रखने वालों के’ है।")

AIDS["16"] = {
    "chain": {"steps": ["मात्रा और काल (आधार)", "युक्ति (इन पर आश्रित)", "सिद्धि (युक्ति में प्रतिष्ठित)"]},
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["मात्राकालाश्रया", "युक्तिः", "सिद्धिर्युक्तौ", "प्रतिष्ठिता"]},
        {"label": "दूसरी पंक्ति",
         "items": ["तिष्ठत्युपरि", "युक्तिज्ञो", "द्रव्यज्ञानवतां", "सदा"]}]},
    "contrast": "युक्तिज्ञ (युक्ति जानने वाला) ↔ द्रव्यज्ञानवान् (द्रव्यों का ज्ञान रखने वाला): श्लोक पहले को ऊपर रखता है। यह नहीं कहा गया कि द्रव्य-ज्ञान व्यर्थ है।",
    "sandhi": "इः + घोष → इर्: सिद्धिः + युक्तौ → सिद्धिर्युक्तौ। अः + घोष → ओ: युक्तिज्ञः + द्रव्य… → युक्तिज्ञो द्रव्य…। इ + उ → यु: तिष्ठति + उपरि → तिष्ठत्युपरि।",
    "anchors": "मात्राकालाश्रया = मात्रा + काल + आश्रया (‘इन पर आश्रित’) · युक्तिज्ञ = युक्ति + ज्ञ (जानने वाला) · द्रव्यज्ञानवताम् = द्रव्य-ज्ञान + -वत् (रखने वाला), षष्ठी बहुवचन · सिद्धि = सफलता।",
    "chunks": "मात्राकालाश्रया युक्तिः | सिद्धिर्युक्तौ प्रतिष्ठिता ‖ तिष्ठत्युपरि युक्तिज्ञो | द्रव्यज्ञानवतां सदा।",
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "अत ऊर्ध्वं प्रवक्ष्यामि",
    "question": "What topic does the speaker announce in verse 17?",
    "rule": ("After this (अत ऊर्ध्वम्) the speaker will describe gruels "
             "(यवागू) made with various drugs, for the relief (निवृत्तये) "
             "of the various disorders curable by them (तत्साध्य)."),
    "limits": ("The verse names no gruel, no drug and no disorder; it only "
               "announces the topic. तत् is read as 'those gruels', and "
               "ऊर्ध्वम् as 'after this'. It does not say that gruels cure "
               "every disorder, only those curable by them."),
    "explain_hi": ("यह श्लोक नया विषय खोलता है। ‘अत ऊर्ध्वं प्रवक्ष्यामि’: इसके "
                   "बाद मैं कहूँगा। विषय है ‘यवागूः विविधौषधाः’, यानी अनेक "
                   "औषधों से बनी यवागू (gruel), और उद्देश्य है "
                   "‘विविधानां विकाराणां तत्साध्यानां निवृत्तये’: उन यवागुओं से "
                   "साध्य अनेक विकारों की निवृत्ति के लिए। श्लोक में कोई "
                   "यवागू, औषध या रोग नाम से नहीं आया; यह केवल घोषणा है। "
                   "अगला श्लोक १८ एक यवागू का वर्णन करता है।"),
    "hook": "अब यवागू: अनेक औषधों वाली, उनसे साध्य विकारों की निवृत्ति के लिए।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What topic does verse 17 begin?",
            ("Gruels made with various drugs, for disorders curable by them",
             "यवागूः विविधौषधाः … तत्साध्यानां निवृत्तये."),
            [("More drugs for enemas", "The enema lists ended in verse 14."),
             ("The dose and time of the five procedures", "That is the topic of verses 15 and 16."),
             ("A list of the sages", "No sage is named in this verse.")],
            "The speaker announces gruels with various drugs for the relief of the disorders they can cure.",
            "Verse 17: announcement of the gruels."),
        match(1, "Match each word of verse 17 to its meaning.",
              [["ऊर्ध्वम्", "after this"],
               ["प्रवक्ष्यामि", "I shall describe"],
               ["यवागूः", "gruels"],
               ["निवृत्तये", "for the cessation (relief)"]],
              "These four words carry the whole announcement.",
              "ऊर्ध्वम् = after this; प्रवक्ष्यामि = I shall describe; यवागूः = gruels; निवृत्तये = for the cessation."),
        fill(2, "The word for 'gruels' in the first line is ____ (type it in Devanagari).",
             ["यवागू", "यवागूः", "यवागूर्"],
             "The first line has यवागूर्विविधौषधाः = यवागूः + विविधौषधाः.",
             "यवागू is a feminine noun; here the plural is meant, 'gruels'.",
             "यवागूः = gruels (here accusative plural, the object of प्रवक्ष्यामि)."),
        mcq("discriminate", 3, "अत ऊर्ध्वम् comes from अतः + ऊर्ध्वम्. What happened to the visarga?",
            ("It dropped, because it follows अ and a different vowel comes next",
             "अः before a vowel other than अ loses the visarga, leaving अत ऊ…."),
            [("It became ओ", "अः becomes ओ before a voiced consonant or a short अ; before ऊ the visarga simply drops."),
             ("It became र्", "र् appears after इ / उ, not after अ."),
             ("It became स्", "स् does not appear here.")],
            "अतः + ऊर्ध्वम् → अत ऊर्ध्वम्.",
            "अः + भिन्न स्वर → अ + स्वर (विसर्ग लुप्त)."),
        multi("apply", 4, "Which statements fit verse 17?",
              [("The gruels are made with various drugs", "Right: विविधौषधाः."),
               ("The gruels are for disorders curable by them", "Right: तत्साध्यानां विकाराणाम्."),
               ("The speaker says 'I shall describe'", "Right: प्रवक्ष्यामि."),
               ("The verse names the first gruel and its drugs", "That comes in verse 18."),
               ("Gruels cure every disorder", "The verse says only those curable by them.")],
              [0, 1, 2],
              "The verse announces a topic and sets its limit; it does not yet describe a gruel.",
              "Verse 17: gruels with various drugs, for the disorders they can cure."),
        mcq("transfer", 5,
            "A made-up line reads अत ऊर्ध्वं वक्ष्यन्ति. Following प्रवक्ष्यामि, who will speak?",
            ("They (several others) will speak",
             "-अन्ति marks 'they', as -आमि in प्रवक्ष्यामि marks 'I'."),
            [("I shall speak", "'I' would end in -आमि."),
             ("You (singular) will speak", "'You' would end in -असि."),
             ("He spoke", "-स्य- marks the future and -अन्ति is plural.")],
            "प्रवक्ष्यामि = 'I shall describe' (first person, future); वक्ष्यन्ति = 'they will say'.",
            "Future endings: -आमि = I, -अन्ति = they.",
            teaches="The ending of a future verb shows who will do it: -आमि is 'I', -अन्ति is 'they'."),
    ],
}

NOTES_HI["17"] = ("संधियाँ जाँची: अतः + ऊर्ध्वम् → अत ऊर्ध्वम् (अ के बाद भिन्न स्वर से पहले विसर्ग लुप्त); यवागूः + विविध… → यवागूर्विविधौषधाः "
                  "(ऊः + घोष → ऊर्); विविध + औषधाः → विविधौषधाः (अ + औ → औ)। ‘यवागूः’ यहाँ द्वितीया बहुवचन है (‘प्रवक्ष्यामि’ का कर्म)। "
                  "‘तत्साध्यानाम्’ में ‘तत्’ का अर्थ ‘उन (यवागुओं) से’ लिया गया है। ‘प्रवक्ष्यामि’ उत्तम पुरुष एकवचन भविष्यत् है। पाठभेद कोई नहीं।")

AIDS["17"] = {
    "frame": "क्या: यवागू (अनेक औषधों वाली) · किसलिए: उनसे साध्य अनेक विकारों की निवृत्ति · कौन: ‘प्रवक्ष्यामि’ = मैं · आगे: श्लोक १८ एक यवागू बताता है।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["अत", "ऊर्ध्वं", "प्रवक्ष्यामि", "यवागूर्विविधौषधाः"]},
        {"label": "दूसरी पंक्ति",
         "items": ["विविधानां", "विकाराणां", "तत्साध्यानां", "निवृत्तये"]}]},
    "sandhi": "अतः + ऊर्ध्वम् → अत ऊर्ध्वम् (अ के बाद भिन्न स्वर: विसर्ग लुप्त)। ऊः + घोष → ऊर्: यवागूः + विविध… → यवागूर्विविधौषधाः। अ + औ → औ: विविध + औषधाः → विविधौषधाः।",
    "anchors": "प्रवक्ष्यामि ← प्र + √वच्, भविष्यत्, ‘मैं कहूँगा’ · -आमि = मैं, -अन्ति = वे · तत्साध्य = तत् + साध्य (उनसे ठीक होने योग्य) · निवृत्तये = चतुर्थी, ‘के लिए’।",
    "chunks": "अत ऊर्ध्वं प्रवक्ष्यामि | यवागूर्विविधौषधाः ‖ विविधानां विकाराणां | तत्साध्यानां निवृत्तये।",
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "पिप्पलीपिप्पलीमूलचव्यचित्रकनागरैः",
    "question": "Which drugs does the gruel of verse 18 contain, and what two effects does the verse give it?",
    "rule": ("A gruel prepared with pippalī, pippalīmūla, cavya, citraka "
             "and nāgara (dry ginger) is dīpanīyā (kindles digestion) and "
             "śūlaghnī (relieves pain). Frame: 'gruel prepared with these "
             "drugs does this'."),
    "limits": ("The verse names five drugs and two effects, with no dose, "
               "no liquid, no method of cooking and no disease name. "
               "'Appetizer' renders दीपनीया (digestive-kindling). The "
               "verb is स्यात् 'would be'; उपसाधिता is a participle."),
    "explain_hi": ("श्लोक १७ की घोषणा के बाद यह एक यवागू का वर्णन है, और इसी साँचे पर आगे की यवागुएँ "
                   "चलती हैं: ‘इन द्रव्यों (तृतीया) से बनी यवागू यह करती है’। "
                   "पाँच द्रव्य एक लम्बे समास में हैं: पिप्पली, पिप्पलीमूल, "
                   "चव्य, चित्रक और नागर (सोंठ), पूरा समास तृतीया बहुवचन (‘-ऐः’, "
                   "‘इनसे’) में है। ‘उपसाधिता’ = बनाई हुई। फल दो हैं: "
                   "‘दीपनीया’ (पाचन-अग्नि जगाने वाली) और ‘शूलघ्नी’ (पीड़ा "
                   "हरने वाली)। श्लोक में न मात्रा है, न पकाने की विधि।"),
    "hook": "पाँच द्रव्य (पिप्पली से सोंठ तक) से बनी यवागू: अग्नि जगाए, शूल हरे।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which two effects does verse 18 give for this gruel?",
            ("It kindles digestion and relieves pain",
             "दीपनीया = kindling digestion; शूलघ्नी = pain-relieving."),
            [("It purges and induces vomiting", "Neither purging nor vomiting is mentioned."),
             ("It removes fever and cough", "Neither fever nor cough is named."),
             ("It cools and strengthens", "Neither effect is named.")],
            "The second line gives the two effects: दीपनीया and शूलघ्नी.",
            "Verse 18: the gruel is दीपनीया and शूलघ्नी."),
        match(1, "Match each word of verse 18 to its meaning.",
              [["यवागूः", "gruel"],
               ["दीपनीया", "appetizer, kindling digestion"],
               ["शूलघ्नी", "pain-relieving"],
               ["उपसाधिता", "prepared"]],
              "These four words of the second line carry the subject and the effects.",
              "यवागूः = gruel; दीपनीया = kindling digestion; शूलघ्नी = pain-relieving; उपसाधिता = prepared."),
        fill(2, "The word meaning 'pain-relieving' is ____ (type it in Devanagari, without the preceding स्यात्).",
             ["शूलघ्नी", "शूलघ्न", "स्याच्छूलघ्नी"],
             "The verse has स्याच्छूलघ्नी = स्यात् + शूलघ्नी.",
             "शूल-घ्नी = pain-destroying, feminine to agree with the feminine यवागूः; the same -घ्न as in मारुतघ्नम् of verse 14.",
             "X-घ्न(ी) = destroying X; the ending agrees with the noun it describes."),
        mcq("discriminate", 3, "स्याच्छूलघ्नी is स्यात् + शूलघ्नी. Which change happened?",
            ("त् became च् and श् became छ्", "त् before श gives च्छ."),
            [("त् became द् and श् stayed", "द् appears before voiced sounds; श is not voiced."),
             ("Nothing changed", "त् + श is written च्छ, not त्श."),
             ("त् became स् before श", "स् does not appear here.")],
            "स्यात् + शूलघ्नी → स्याच्छूलघ्नी.",
            "त् + श → च्छ."),
        multi("apply", 4, "Which of these are named among the drugs of verse 18?",
              [("Pippalī", "Right: पिप्पली."),
               ("Cavya", "Right: चव्य."),
               ("Nāgara (dry ginger)", "Right: नागर."),
               ("Bilva", "Bilva is named in verse 11."),
               ("Grape (द्राक्षा)", "Grape is named in verse 10.")],
              [0, 1, 2],
              "The five drugs of the first line are the only drugs named here.",
              "Verse 18: pippalī, pippalīmūla, cavya, citraka, nāgara."),
        mcq("transfer", 5,
            "A made-up line says बिल्वपिप्पलीनागरैर्यवागूः शूलघ्नी स्यात्. By the pattern of verse 18, what does it say?",
            ("A gruel prepared with bilva, pippalī and nāgara would relieve pain",
             "-ऐः marks 'with / by' the drugs, as in verse 18; शूलघ्नी gives the effect."),
            [("Bilva, pippalī and nāgara are the ailments the gruel relieves", "-ऐः names the means (the drugs), not what is relieved."),
             ("The gruel causes pain", "शूलघ्नी means pain-relieving."),
             ("Three gruels, one for each drug", "यवागूः is singular; the three drugs are for one gruel.")],
            "बिल्वपिप्पलीनागरैः = with bilva, pippalī and nāgara (instrumental plural), and the gruel is pain-relieving. This is a grammar drill, not a medical claim.",
            "Drugs in -ऐः + यवागूः + effect = a gruel with these drugs has this effect.",
            teaches="The frame 'drugs in -ऐः, यवागूः, effect' lets you read any gruel verse: the instrumental names the drugs it is prepared with."),
    ],
}

NOTES_HI["18"] = ("संधियाँ जाँची: यवागूः + दीपनीया → यवागूर्दीपनीया (ऊः + घोष → ऊर्); स्यात् + शूलघ्नी → स्याच्छूलघ्नी (त् + श → च्छ); "
                  "च + उपसाधिता → चोपसाधिता (अ + उ → ओ)। पहली पंक्ति एक ही लम्बा द्वन्द्व समास है (पाँच सदस्य, तृतीया बहुवचन -ऐः); "
                  "क्रिया ‘स्यात्’ है और ‘उपसाधिता’ कृदन्त। ‘दीपनीया’ का अनुवाद ‘अग्नि को जगाने वाली’ है। पाठभेद या पाठ-दोष कोई नहीं।")

AIDS["18"] = {
    "frame": "कौन: यवागू · किनसे बनी: पिप्पली, पिप्पलीमूल, चव्य, चित्रक, नागर (सोंठ) · असर: दीपनीया (अग्नि जगाने वाली) और शूलघ्नी (पीड़ा हरने वाली)।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["पिप्पलीपिप्पलीमूलचव्यचित्रकनागरैः"]},
        {"label": "दूसरी पंक्ति",
         "items": ["यवागूर्दीपनीया", "स्याच्छूलघ्नी", "चोपसाधिता"]}]},
    "letters": "पि-पि-च-चि-ना: पिप्पली, पिप्पलीमूल, चव्य, चित्रक, नागर (सोंठ): नामों के पहले अक्षर।",
    "sandhi": "ऊः + घोष → ऊर्: यवागूः + दीपनीया → यवागूर्दीपनीया। त् + श → च्छ: स्यात् + शूलघ्नी → स्याच्छूलघ्नी। अ + उ → ओ: च + उपसाधिता → चोपसाधिता।",
    "anchors": "पूरा समास तृतीया बहुवचन ‘-ऐः’ में है: ‘इनसे’ · शूलघ्नी = शूल + घ्नी (पीड़ा हरने वाली), वही -घ्न जो श्लोक १४ के ‘मारुतघ्नम्’ में है · उपसाधिता = बनाई गई।",
    "chunks": "पिप्पलीपिप्पलीमूल | चव्यचित्रकनागरैः ‖ यवागूर्दीपनीया | स्याच्छूलघ्नी चोपसाधिता।",
}

IMAGE_SPECS = {
    ("11", "diagram"): {
        "file": "ch2-drugs-11.svg",
        "alt": "Two columns showing the printed words of verse 11: the first line (pāṭalā, cāgnimantha, ca, bilva, śyonākameva, ca) and the second line (kāśmarya, śālaparṇī, ca, pṛśniparṇī, nidigdhikā)",
        "type": "split",
        "title": "श्लोक ११: औषधों की सूची",
        "cols": [["पहली पंक्ति", ["पाटलां", "चाग्निमन्थं", "च", "बिल्वं", "श्योनाकमेव", "च"]],
                 ["दूसरी पंक्ति", ["काश्मर्यं", "शालपर्णीं", "च", "पृश्निपर्णीं", "निदिग्धिकाम्"]]],
    },
    ("16", "chain"): {
        "file": "ch2-yukti-16.svg",
        "alt": "A chain of three boxes: dose and time, then yukti resting on them, then success established in yukti",
        "type": "chain",
        "title": "श्लोक १६: युक्ति की कड़ी",
        "steps": ["मात्रा और काल (आधार)", "युक्ति (इन पर आश्रित)", "सिद्धि (युक्ति में प्रतिष्ठित)"],
    },
}
