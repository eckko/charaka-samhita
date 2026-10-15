from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो ऽपामार्गतण्डुलीयम्",
    "question": "How does Chapter 2 announce itself, and what is it called?",
    "rule": ("अथातो … अध्यायं व्याख्यास्यामः = 'Now, therefore, we shall expound "
             "the chapter called Apāmārgataṇḍulīya.' The title is "
             "अपामार्ग + तण्डुल + the ending -ईय ('relating to')."),
    "limits": ("The data says the exact sense of तण्डुल in the title is "
               "uncertain. The sentence only announces the chapter; it does "
               "not say what the chapter contains."),
    "explain_hi": ("यह दूसरे अध्याय का आरम्भ-वाक्य है। ‘अथ’ आरम्भ बताता है, ‘अतः’ का अर्थ ‘इस कारण’ है, और "
                   "‘व्याख्यास्यामः’ का अर्थ ‘हम समझाएँगे’। अध्याय का नाम "
                   "‘अपामार्गतण्डुलीय’ है: अपामार्ग + तण्डुल + ‘-ईय’ (सम्बन्धी)। "
                   "छपे पाठ में ‘अतो ऽपामार्ग…’ है: अतः का विसर्ग ‘ओ’ बना और "
                   "आगे के ‘अ’ की जगह ‘ऽ’ लगा।"),
    "hook": "अथ – अतः – व्याख्यास्यामः · नाम = अपामार्ग + तण्डुल + ईय।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The sentence अथातो ऽपामार्गतण्डुलीयमध्यायं व्याख्यास्यामः opens Chapter 2. What does it announce?",
            ("A chapter called Apāmārgataṇḍulīya will now be expounded",
             "अध्यायं and व्याख्यास्यामः show a chapter is named and promised."),
            [("A list of gruels and their cures",
              "No gruel or cure is named in this sentence."),
             ("A story of sages meeting on a mountain",
              "No sages or mountain appear here; the sentence only introduces a chapter."),
             ("A prayer to a god",
              "No god is addressed.")],
            "अध्यायम् (chapter) and व्याख्यास्यामः (we shall expound) show that a chapter is being introduced.",
            "The opening sentence names the chapter and promises to explain it."),
        match(1, "Match each word of the opening sentence to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["अध्यायम्", "chapter"],
               ["व्याख्यास्यामः", "we shall expound"]],
              "These four words carry the whole announcement.",
              "अथ = now; अतः = therefore; अध्यायम् = chapter; व्याख्यास्यामः = we shall expound."),
        fill(2, "The word for 'we shall expound' is ____ (type it in Devanagari).",
             ["व्याख्यास्यामः", "व्याख्यास्याम", "व्याख्यास्यामः।"],
             "The sentence ends with व्याख्यास्यामः.",
             "व्याख्यास्यामः is first person plural, future: वि + आ + √ख्या with the ending -मः, 'we'.",
             "-मः on a verb = 'we'; the future sense gives 'we shall'."),
        mcq("discriminate", 3,
            "The text prints अतो ऽपामार्ग…. What happens to अतः before the next word?",
            ("The visarga becomes ओ before a voiced sound; the following अ is shown by ऽ",
             "अः + अ gives ओ, and the sign ऽ marks the अ that follows."),
            [("The visarga is dropped and the vowel stays अ",
              "The visarga does not drop after short अ; it turns into ओ here."),
             ("The visarga becomes श् before the next word",
              "श् appears before च or छ, not before अ."),
             ("Nothing changes; ओ and ऽ are misprints",
              "It is a regular sandhi change, not a misprint.")],
            "अतः + अपामार्ग… is printed अतो ऽपामार्ग…: the visarga turns to ओ, and ऽ marks the dropped-looking अ.",
            "अः + voiced sound → ओ; ऽ marks the following अ."),
        mcq("apply", 4,
            "The title अपामार्गतण्डुलीय ends in -ईय. According to the card, what does this ending do?",
            ("It makes an adjective, 'relating to' the two names before it",
             "The word breakdown reads it as: relating to अपामार्ग and तण्डुल (title)."),
            [("It makes the verb first person plural",
              "That is the job of -मः in व्याख्यास्यामः."),
             ("It makes the word plural",
              "The title is singular, matching अध्यायम्."),
             ("It turns the title into a god's name",
              "Nothing in the data says that.")],
            "The title is a descriptive adjective: relating to अपामार्ग and तण्डुल; it agrees with अध्यायम्.",
            "-ईय makes an adjective 'relating to'."),
        mcq("transfer", 5,
            "A made-up chapter title is अभ्यङ्गीयम्. Which is the correct joined form of अतः before it?",
            ("अतो ऽभ्यङ्गीयम्", "अः + अ gives ओ with ऽ, as in अतो ऽपामार्गतण्डुलीयम्."),
            [("अताभ्यङ्गीयम्", "अथ + अतः gives आ, but a visarga before अ does not give आ."),
             ("अतःभ्यङ्गीयम्", "The visarga does not stay before a vowel here."),
             ("अतुभ्यङ्गीयम्", "The result of अः + अ is ओ, not उ.")],
            "Same rule as in the opening sentence: अतः + अ… → अतो ऽ….",
            "अतः + अ-initial title → अतो ऽ-….",
            teaches="Any title beginning with अ after अतः is printed with ओ and ऽ."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "इति ह स्माह भगवानात्रेयः",
    "question": "Who speaks, and how is the speech reported?",
    "rule": ("इति ह स्माह भगवानात्रेयः = 'Thus, indeed, said the venerable "
             "Ātreya.' आह = said; स्म + आह → स्माह; भगवान् and आत्रेयः are both "
             "nominative singular: the speaker."),
    "limits": ("The data calls ह स्म with the perfect a traditional formula of "
               "reported speech. The verse names the speaker only as "
               "Ātreya; it says nothing more about him."),
    "explain_hi": ("यह गद्य-वाक्य बताता है कि आगे की बात किसने कही: भगवान् आत्रेय "
                   "ने। ‘इति ह स्म’ के साथ ‘आह’ (कहा) का प्रयोग कही हुई बात बताने "
                   "का पारम्परिक साँचा है। ‘आह’ लिट् लकार, प्रथम पुरुष एकवचन है: "
                   "एक वक्ता। ‘स्माह’ = स्म + आह (अ + आ → आ), और ‘भगवानात्रेयः’ = "
                   "भगवान् + आत्रेयः, जहाँ न् सीधे अगले स्वर से जुड़ गया।"),
    "hook": "इति ह स्माह = ऐसा कहा · वक्ता: भगवान् आत्रेय।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In इति ह स्माह भगवानात्रेयः, who is named as the speaker?",
            ("The venerable Ātreya", "भगवान् आत्रेयः is the subject of आह."),
            [("The sage Bharadvāja", "Bharadvāja is not named in this sentence."),
             ("The physician's student", "No student is named."),
             ("The author of the chapter, speaking of himself",
              "The sentence names Ātreya, not a speaker in the first person.")],
            "आह (said) has भगवान् आत्रेयः as its subject.",
            "The speaker is भगवान् आत्रेयः."),
        match(1, "Match each word of the sentence to its meaning.",
              [["इति", "thus"], ["ह", "indeed (particle)"],
               ["आह", "said"], ["भगवान्", "the venerable"]],
              "These four words carry the whole sentence.",
              "इति = thus; ह = indeed; आह = said; भगवान् = the venerable."),
        fill(2, "The speaker's name in the sentence is ____ (type it in Devanagari, with ending as printed).",
             ["आत्रेयः", "आत्रेय", "भगवानात्रेयः"],
             "The last word is आत्रेयः, 'Ātreya'.",
             "आत्रेयः is nominative singular: the one who speaks. भगवान् 'the venerable' goes with it.",
             "आत्रेयः = Ātreya, the speaker."),
        mcq("discriminate", 3, "Which is the right split of स्माह?",
            ("स्म + आह", "अ + आ gives आ, so स्म + आह is written स्माह."),
            [("स्मा + अह", "स्मा is not a word; the particle is स्म."),
             ("सम् + आह", "The particle is स्म, not सम्."),
             ("स्मा + आह", "स्मा is not a word; the particle is स्म.")],
            "स्म (a particle marking the past) + आह (said) → स्माह.",
            "स्माह = स्म + आह."),
        mcq("apply", 4,
            "आह is a third person singular perfect of √अह्. What does that tell us?",
            ("One person spoke, in the past: 'he said'",
             "The singular third person names one speaker; the perfect is a past form."),
            [("Many sages spoke together",
              "A plural would need a plural ending; आह is singular."),
             ("The speaker says 'I shall speak'",
              "That would be first person future, as in व्याख्यास्यामः."),
             ("A command: 'say it!'",
              "आह is not a command form.")],
            "The data labels आह '3 sg. pf.': one speaker, past.",
            "आह = he said (3rd singular, perfect)."),
        mcq("transfer", 5,
            "A made-up line needs अथ + आह joined. Which is the correct form?",
            ("अथाह", "अ + आ gives आ, as in स्म + आह → स्माह."),
            [("अथआह", "The two vowels must be joined by sandhi."),
             ("अथोह", "अ + आ does not give ओ."),
             ("अथेह", "अ + आ does not give ए.")],
            "The rule that gave स्माह also gives अथाह.",
            "अ/आ + आ → आ.",
            teaches="Any word ending in अ followed by आह is joined with a long आ."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "अपामार्गस्य बीजानि पिप्पलीर्मरिचानि च",
    "question": "What does verse 3 list, and where is its verb?",
    "rule": ("Verse 3 starts a list: अपामार्ग seeds, long pepper, black pepper, "
             "विडङ्ग, शिग्रु, mustard, तुम्बुरु. It has no verb; दद्यात् comes in verse 5."),
    "limits": ("Verses 3 to 5 are one sentence, so verse 3 alone does not say "
               "what the drugs are for. The data notes that बीजानि is taken "
               "with अपामार्ग only; the grammar allows it with all the items. "
               "Plant identities are those in the data's glosses."),
    "explain_hi": ("यह श्लोक एक लम्बे वाक्य की सूची का आरम्भ है; श्लोक ३ से ५ "
                   "मिलकर एक वाक्य हैं और क्रिया ‘दद्यात्’ श्लोक ५ में आती है। यहाँ "
                   "अपामार्ग के बीज, पिप्पली, मरिच, विडङ्ग, शिग्रु, सर्षप और "
                   "तुम्बुरु के नाम हैं। संधियाँ: पिप्पलीः + मरिचानि → "
                   "पिप्पलीर्मरिचानि (ई के बाद विसर्ग घोष म् से पहले र् बना); "
                   "विडङ्गानि + अथ → विडङ्गान्यथ (इ → य् स्वर से पहले); "
                   "सर्षपान् + तुम्बुरूणि → सर्षपांस्तुम्बुरूणि।"),
    "hook": "श्लोक ३: केवल सूची: बीज, पिप्पली, मरिच, विडङ्ग, शिग्रु, सर्षप, तुम्बुरु; क्रिया आगे।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 3 names seeds, peppers, mustard and more. Which statement about it is true?",
            ("No verb: the verb दद्यात् comes in verse 5",
             "Verses 3 to 5 are one sentence; verse 3 gives only the items."),
            [("The verb दद्यात्, 'one should give'",
              "दद्यात् is in verse 5, not here."),
             ("The treatment these drugs are for",
              "The treatment is named in verse 5."),
             ("A dose for each drug",
              "No quantity is given anywhere in the verse.")],
            "The verse is a list of accusative-type items; the governing verb is in verse 5.",
            "Verse 3 = list only; the verb comes later."),
        match(1, "Match each drug name in verse 3 to its meaning.",
              [["पिप्पलीः", "long pepper"], ["मरिचानि", "black pepper"],
               ["सर्षपान्", "mustard"], ["शिग्रूणि", "drumstick tree"]],
              "These four names are glossed in the data.",
              "पिप्पली = long pepper; मरिच = black pepper; सर्षप = mustard; शिग्रु = drumstick tree."),
        fill(2, "पिप्पलीः + मरिचानि is printed पिप्पली____मरिचानि. Type the missing letter with its virāma, in Devanagari.",
             ["र्", "र"],
             "The printed word is पिप्पलीर्मरिचानि.",
             "After ई the visarga turns into र् before a voiced sound such as म.",
             "Visarga after ई/उ + voiced sound → र्."),
        mcq("discriminate", 3, "Which is the right split of विडङ्गान्यथ?",
            ("विडङ्गानि + अथ", "इ becomes य् before a vowel, so विडङ्गानि + अथ → विडङ्गान्यथ."),
            [("विडङ्ग + अन्यथ", "The verse has विडङ्गानि (plural) before अथ; the split must end in the particle अथ."),
             ("विडङ्गा + न्यथ", "न्यथ is not a word."),
             ("विडङ्गान्य + थ", "थ alone is not a word; the particle is अथ.")],
            "विडङ्गानि (neuter plural) + अथ (and/now) → विडङ्गान्यथ.",
            "Final इ + vowel → य् + vowel."),
        multi("apply", 4, "Which of these does verse 3 name?",
              [("Black pepper (मरिच)", "Right: मरिचानि."),
               ("Mustard (सर्षप)", "Right: सर्षपान्."),
               ("Long pepper (पिप्पली)", "Right: पिप्पलीः."),
               ("Cumin (अजाजी)", "Cumin is named in verse 4."),
               ("Garlic (लशुन)", "Garlic is named in verse 5.")],
              [0, 1, 2],
              "Verse 3 names seven items; cumin and garlic belong to the following verses.",
              "Verse 3: अपामार्ग seeds, पिप्पली, मरिच, विडङ्ग, शिग्रु, सर्षप, तुम्बुरु."),
        mcq("transfer", 5,
            "A made-up line has हरीतकीः + गृह्णीयात्. Which is the correct joined form?",
            ("हरीतकीर्गृह्णीयात्", "After ई the visarga turns to र् before a voiced sound like ग."),
            [("हरीतकीगृह्णीयात्", "The visarga drops after आ, not after ई."),
             ("हरीतकीःगृह्णीयात्", "A visarga cannot stay before a voiced ग in this join."),
             ("हरीतकीशृह्णीयात्", "श् appears before च or छ, not before ग.")],
            "Same rule as पिप्पलीः + मरिचानि → पिप्पलीर्मरिचानि.",
            "Visarga after ई + voiced sound → र्.",
            teaches="Any plural in -ईः followed by a voiced sound takes र् in place of the visarga."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "अजाजीं चाजगन्धां च",
    "question": "What does verse 4 add to the list, and what does the edition footnote say?",
    "rule": ("Verse 4 continues the list: cumin, अजगन्धा, पीलु fruits, cardamom, "
             "हरेणुका, पृथ्वीका, सुरसा, श्वेता, and the pair कुठेरक-फणिज्झक. "
             "The verb is still to come in verse 5."),
    "limits": ("The edition footnote offers अजमोदा in place of अजगन्धा; the "
               "card does not choose between them. Plants glossed 'name kept' "
               "are not identified here. The sentence runs on from verse 3."),
    "explain_hi": ("सूची आगे बढ़ती है: जीरा, अजगन्धा, पीलु के फल, इलायची, "
                   "हरेणुका, पृथ्वीका, सुरसा, श्वेता और कुठेरक-फणिज्झक। क्रिया अब भी नहीं आई "
                   "(श्लोक ५ में आएगी)। पाठ-टिप्पणी में एक दूसरा पाठ है: "
                   "‘च अजमोदां च’, ‘च अजगन्धां च’ की जगह। संधियाँ: च + अजगन्धाम् → "
                   "चाजगन्धाम्; पीलूनि + एलाम् → पीलून्येलाम्। ‘कुठेरकफणिज्झकौ’ "
                   "में अन्त का -औ यहाँ द्वन्द्व का द्विवचन है (डेटा के अनुसार)।"),
    "hook": "श्लोक ४: जीरा, अजगन्धा, पीलु, इलायची … कुठेरक-फणिज्झक; क्रिया अब भी आगे।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 4 lists cumin, cardamom and other drugs. Which verse supplies its verb?",
            ("Verse 5, with दद्यात्", "Verses 3 to 5 form one sentence; the verb comes at its end."),
            [("Verse 4 itself", "Verse 4 has only names, no verb."),
             ("Verse 3", "Verse 3 is also a list without a verb."),
             ("Verse 6", "Verse 6 gives conditions, after the verb has come.")],
            "The sentence of verses 3 to 5 ends with दद्यात् in verse 5.",
            "Verse 4 is part of the list; the verb is in verse 5."),
        match(1, "Match each word of verse 4 to its meaning.",
              [["अजाजीम्", "cumin"], ["एलाम्", "cardamom"],
               ["सुरसाम्", "a basil (surasā)"], ["पीलूनि", "pīlu fruits"]],
              "These four are glossed in the data.",
              "अजाजी = cumin; एला = cardamom; सुरसा = a basil; पीलूनि = pīlu fruits."),
        fill(2, "चाजगन्धां splits into च + ____. Type the plant's name in Devanagari.",
             ["अजगन्धां", "अजगन्धाम्", "अजगन्धा"],
             "चाजगन्धां = च + अजगन्धां.",
             "अ + अ gives आ: the च joins the following अजगन्धां into one written word.",
             "च + अजगन्धाम् → चाजगन्धाम्."),
        mcq("discriminate", 3, "Which is the right split of पीलून्येलां?",
            ("पीलूनि + एलाम्", "इ becomes य् before the vowel, so पीलूनि + एलाम् → पीलून्येलाम्."),
            [("पीलून्य + एलाम्", "That would leave an extra य्; the plural form is पीलूनि."),
             ("पीलून + इएलाम्", "There is no word इएलाम्."),
             ("पीलून्ये + लाम्", "लाम् is not a word here.")],
            "पीलूनि (neuter plural) + एलाम् (cardamom) → पीलून्येलाम्.",
            "Final इ + vowel → य् + vowel."),
        multi("apply", 4, "Which statements about verse 4 are right?",
              [("It names drugs but has no verb", "Right: the verb comes in verse 5."),
               ("The edition footnote gives another reading for अजगन्धां", "Right: अजमोदां."),
               ("कुठेरकफणिज्झकौ names a pair of plants", "Right: a dvandva in the dual."),
               ("It says what the drugs are used for", "No use is named until verse 5.")],
              [0, 1, 2],
              "The verse is list and footnote only; the use comes in verse 5.",
              "Verse 4 = more names, one variant, no verb, no use."),
        mcq("transfer", 5,
            "A made-up phrase has च + अश्वगन्धाम्. Which is the correct joined form?",
            ("चाश्वगन्धाम्", "अ + अ gives आ, as in च + अजगन्धाम् → चाजगन्धाम्."),
            [("चअश्वगन्धाम्", "The two अ must be joined by sandhi."),
             ("चोश्वगन्धाम्", "अ + अ does not give ओ."),
             ("चैश्वगन्धाम्", "अ + अ does not give ऐ.")],
            "The rule that gave चाजगन्धाम् gives चाश्वगन्धाम्.",
            "अ + अ → आ.",
            teaches="च before a word beginning with अ is joined into चा-."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "शिरीषबीजं लशुनं दद्याच्छीर्षविरेचने",
    "question": "What do verses 3 to 5 say to give, and for which treatment?",
    "rule": ("Verses 3-5 end here: 'one should give (दद्यात्) these in head-purging "
             "(शीर्षविरेचन)'. This verse adds शिरीष seed, garlic, the two haridrās, the pair "
             "of salts, ज्योतिष्मती and dry ginger."),
    "limits": ("The verse names the treatment but gives no dose and no "
               "pharmacology. 'Two haridrās' and 'pair of salts' are not "
               "named here; the data says only that tradition names them."),
    "explain_hi": ("यह श्लोक तीन श्लोकों वाले वाक्य को पूरा करता है। अन्तिम सूची: "
                   "शिरीष के बीज, लहसुन, दो हल्दियाँ, दो नमक, ज्योतिष्मती और सोंठ। "
                   "क्रिया है ‘दद्यात्’ (देना चाहिए) और प्रयोग का स्थान ‘शीर्षविरेचने’, "
                   "यानी शिरोविरेचन में। सारे श्लोक ३ से ५ के द्रव्य इसी के लिए हैं। "
                   "संधि: दद्यात् + शीर्षविरेचने → दद्याच्छीर्षविरेचने (त् + श → च्छ)।"),
    "hook": "श्लोक ३–५ का निचोड़: ये द्रव्य दद्यात् = दें, शीर्षविरेचने = शिरोविरेचन में।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 5 ends दद्याच्छीर्षविरेचने. For which treatment does it say to give these drugs?",
            ("Head-purging (शीर्षविरेचन)", "शीर्षविरेचने is the locative: 'in head-purging'."),
            [("Emesis", "Emesis is named in verse 8, for another list of drugs."),
             ("Purgation", "Purgation comes with the drugs of verses 9 and 10."),
             ("A bath", "No bath is mentioned.")],
            "The verb दद्यात् with शीर्षविरेचने says: give these in head-purging.",
            "Verses 3-5: drugs for head-purging."),
        match(1, "Match each word of verse 5 to its meaning.",
              [["लशुनम्", "garlic"], ["नागरम्", "dry ginger"],
               ["हरिद्रे", "the two turmerics"], ["लवणद्वयम्", "the pair of salts"]],
              "These four are glossed in the data.",
              "लशुन = garlic; नागर = dry ginger; हरिद्रे = the two haridrās; लवणद्वयम् = the pair of salts."),
        fill(2, "The verb meaning 'one should give' is ____ (type it in Devanagari).",
             ["दद्यात्", "दद्याद्", "दद्यात"],
             "दद्यात् is in the second line of verse 5.",
             "दद्यात् is third person singular optative of √दा: 'one should give'. It governs the lists of verses 3 to 5.",
             "दद्यात् = one should give."),
        mcq("discriminate", 3, "Which is the right split of दद्याच्छीर्षविरेचने?",
            ("दद्यात् + शीर्षविरेचने", "त् + श becomes च्छ, so दद्यात् + शीर्ष… is printed दद्याच्छीर्ष…."),
            [("दद्याच् + छीर्षविरेचने", "छीर्ष is not a word."),
             ("दद्या + च्छीर्षविरेचने", "च्छीर्ष is not a word."),
             ("दद्यात् + सीर्षविरेचने", "The word is शीर्ष, with श.")],
            "दद्यात् + शीर्षविरेचने → दद्याच्छीर्षविरेचने.",
            "त् + श → च्छ."),
        multi("apply", 4, "Which of these does verse 5 itself name?",
              [("Garlic", "Right: लशुनम्."),
               ("Dry ginger", "Right: नागरम्."),
               ("The pair of salts", "Right: लवणद्वयम्."),
               ("Mustard", "Mustard is in verse 3."),
               ("Cumin", "Cumin is in verse 4.")],
              [0, 1, 2],
              "The last list is in verse 5; mustard and cumin came earlier in the same sentence.",
              "Verse 5: शिरीष seed, garlic, two haridrās, pair of salts, ज्योतिष्मती, dry ginger."),
        mcq("transfer", 5,
            "A made-up line reads लशुनं सर्षपांश्च दद्याच्छीर्षविरेचने. What does it say?",
            ("Give garlic and mustard in head-purging", "The list is the objects of दद्यात्; the locative names the treatment."),
            [("Garlic and mustard are given in emesis", "शीर्षविरेचने names head-purging, not emesis."),
             ("Garlic and mustard were given yesterday", "दद्यात् is 'should give', not a past tense."),
             ("Garlic and mustard must never be given", "Nothing forbids; दद्यात् advises giving.")],
            "The frame is: drugs + दद्यात् + the treatment in the locative.",
            "Drug list + दद्यात् + treatment (locative) = 'give these in that treatment'.",
            teaches="Read any such line by its frame: the list is what to give, the locative at the end is the treatment."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "गौरवे शिरसः शूले पीनसे",
    "question": "In which conditions does verse 6 say the head-purging drugs are used?",
    "rule": ("Verse 6 lists conditions, almost all in the locative ('in …'; शिरसः is genitive, 'of the head'): heaviness, pain, "
             "पीनस, half-headache, worm disease, epilepsy, loss of smell, "
             "प्रमोहक. It continues verse 5; it has no verb of its own."),
    "limits": ("The verse names conditions but no dose and no mechanism. Whether "
               "शिरसः goes with both गौरवे and शूले or only with शूले is not "
               "settled by the Sanskrit. प्रमोहक is rendered literally; "
               "the verse does not define it."),
    "explain_hi": ("यह श्लोक श्लोक ५ से आगे चलता है: ये उन रोगों की सूची है "
                   "जिनमें शिरोविरेचन के द्रव्य दिए जाते हैं। शिरसः (षष्ठी: ‘सिर का’) "
                   "को छोड़कर सभी शब्द सप्तमी में हैं (‘…में’): भारीपन, शूल, पीनस, अर्धावभेदक, कृमिरोग, अपस्मार, "
                   "घ्राणनाश और प्रमोहक। संधियाँ: पीनसे ऽर्धावभेदके (ए + अ → ए, अ की जगह ऽ); "
                   "क्रिमिव्याधौ + अपस्मारे → क्रिमिव्याधावपस्मारे (औ + स्वर → आव्)।"),
    "hook": "श्लोक ६: इन रोगों में (शिरसः छोड़कर सप्तमी): भारीपन, शूल, पीनस, अर्धावभेदक, कृमि, अपस्मार, घ्राणनाश, प्रमोहक।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 6 is a list of conditions, nearly all in the 'in …' ending. What is it the list of?",
            ("The conditions for the head-purging drugs of verse 5",
             "The data notes: it continues verse 5 and names the conditions for those drugs."),
            [("More drugs to be added to the list",
              "These are disease names, not drugs."),
             ("The doses of the drugs of verse 5",
              "No quantity is given."),
             ("Rules for the physician's conduct",
              "The verse names conditions, not conduct.")],
            "Locatives ('in …') list the conditions in which the drugs of verse 5 are used.",
            "Verse 6 = conditions for the head-purging drugs of verse 5."),
        match(1, "Match each word of verse 6 to its meaning.",
              [["शूले", "in pain"], ["अपस्मारे", "in epilepsy"],
               ["घ्राणनाशे", "in loss of smell"],
               ["क्रिमिव्याधौ", "in worm disease"]],
              "These four are glossed in the data.",
              "शूले = in pain; अपस्मारे = in epilepsy; घ्राणनाशे = in loss of smell; क्रिमिव्याधौ = in worm disease."),
        fill(2, "The word for 'in epilepsy' is ____ (type it in Devanagari).",
             ["अपस्मारे", "अपस्मार", "क्रिमिव्याधावपस्मारे"],
             "The second line has क्रिमिव्याधावपस्मारे: worm disease and epilepsy run together.",
             "अपस्मारे is locative singular: 'in epilepsy'. The -ए ending is the locative of a word in -अ.",
             "अपस्मारे = in epilepsy (locative)."),
        mcq("discriminate", 3, "Which is the right split of क्रिमिव्याधावपस्मारे?",
            ("क्रिमिव्याधौ + अपस्मारे", "औ + vowel becomes आव् + vowel, so क्रिमिव्याधौ + अपस्मारे → क्रिमिव्याधावपस्मारे."),
            [("क्रिमिव्याधा + वपस्मारे", "वपस्मारे is not a word."),
             ("क्रिमिव्याधाव + अपस्मारे", "क्रिमिव्याधाव is not a word."),
             ("क्रिमिव्याधु + अपस्मारे", "Before a vowel, -उ would give -व् (क्रिमिव्याध्वपस्मारे), not -आव्; the locative of क्रिमिव्याधि is -औ.")],
            "क्रिमिव्याधौ (in worm disease) + अपस्मारे (in epilepsy) → क्रिमिव्याधावपस्मारे.",
            "औ + vowel → आव् + vowel."),
        multi("apply", 4, "Which of these conditions does verse 6 name?",
              [("Loss of smell", "Right: घ्राणनाशे."),
               ("Epilepsy", "Right: अपस्मारे."),
               ("Half-headache", "Right: अर्धावभेदके."),
               ("Fever", "Fever is not named in the verse."),
               ("Loss of hearing", "Hearing is not mentioned.")],
              [0, 1, 2],
              "The verse names eight conditions; fever and loss of hearing are not among them.",
              "Verse 6: heaviness, pain, पीनस, half-headache, worm disease, epilepsy, loss of smell, प्रमोहक."),
        mcq("transfer", 5,
            "A made-up phrase needs व्याधौ + अस्मिन् joined. Which is the correct form?",
            ("व्याधावस्मिन्", "औ + vowel becomes आव् + vowel, as in क्रिमिव्याधावपस्मारे."),
            [("व्याधौस्मिन्", "The औ must change before the vowel."),
             ("व्याधास्मिन्", "औ + vowel gives आव्, not just आ."),
             ("व्याधेस्मिन्", "औ + vowel does not give ए.")],
            "The rule is the same as in क्रिमिव्याधावपस्मारे.",
            "औ + vowel → आव् + vowel.",
            teaches="A locative in -औ before a vowel is written -आव्; look for it when splitting."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "मदनं मधुकं निम्बं जीमूतं",
    "question": "What does verse 7 list, and where does its sentence end?",
    "rule": ("Verse 7 starts the list for the next treatment: मदन, मधुक, neem, जीमूत, "
             "कृतवेधन, पिप्पली, कुटज, इक्ष्वाकु, cardamom, धामार्गव. "
             "The sentence is completed in verse 8."),
    "limits": ("The verse names drugs but not their use; the use is in verse 8. "
               "Names glossed 'name kept' are not identified. The data reads "
               "पिप्पलीकुटजेक्ष्वाकूणि as one compound of three names; "
               "that reading is the data's, the plants are not identified here."),
    "explain_hi": ("एक और सूची शुरू होती है: मदन, मधुक, नीम, जीमूत, कृतवेधन, "
                   "पिप्पली, कुटज, इक्ष्वाकु, इलायची और धामार्गव। वाक्य यहाँ पूरा "
                   "नहीं होता; क्रिया और प्रयोग श्लोक ८ में हैं। संधियाँ: कुटज + "
                   "इक्ष्वाकूणि → कुटजेक्ष्वाकूणि (अ + इ → ए); "
                   "पिप्पलीकुटजेक्ष्वाकूणि + एलाम् → …ूण्येलाम् (इ → य् स्वर से पहले)।"),
    "hook": "श्लोक ७: मदन, मधुक, नीम … धामार्गव: केवल नाम; प्रयोग श्लोक ८ में।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 7 lists madana, neem, cardamom and more. Where does the sentence get its verb?",
            ("In verse 8, with प्रयुञ्जीत",
             "Verse 8 completes the sentence: one should administer."),
            [("In verse 7 itself", "Verse 7 only lists names."),
             ("In verse 5, with दद्यात्", "That verb belongs to the earlier list for head-purging."),
             ("There is no verb in the whole sentence", "प्रयुञ्जीत in verse 8 is the verb.")],
            "The data notes: the sentence is completed in verse 8.",
            "Verse 7 = list; verb in verse 8."),
        order(1, "Put these four names in the order they are printed in verse 7.",
              ["मदनं", "मधुकं", "निम्बं", "जीमूतं"],
              "These are the first four names of the first line.",
              "मदनं → मधुकं → निम्बं → जीमूतं."),
        fill(2, "The word for 'neem' in verse 7 is ____ (type it in Devanagari).",
             ["निम्बं", "निम्बम्", "निम्ब"],
             "निम्बं is the third name of the verse.",
             "निम्बम् ends in -म्, an accusative singular, one item in the list.",
             "निम्ब = neem."),
        mcq("discriminate", 3,
            "In पिप्पलीकुटजेक्ष्वाकूणि, which join gives the -जे- before क्ष्वा?",
            ("अ + इ → ए: कुटज + इक्ष्वाकूणि", "अ + इ gives ए, so कुटज + इ… is written कुटजे…."),
            [("अ + इ → ई", "अ + इ does not give ई."),
             ("अ + इ → ऐ", "ऐ comes from अ + ए or अ + ऐ."),
             ("अ + इ → ओ", "ओ comes from अ + उ.")],
            "कुटज + इक्ष्वाकूणि → कुटजेक्ष्वाकूणि.",
            "अ + इ → ए."),
        multi("apply", 4, "Which of these does verse 7 name?",
              [("Neem (निम्ब)", "Right: निम्बम्."),
               ("Cardamom (एला)", "Right: एलाम्."),
               ("Kuṭaja", "Right: inside the compound पिप्पलीकुटजेक्ष्वाकूणि."),
               ("Garlic (लशुन)", "Garlic is in verse 5."),
               ("Trivṛt", "Trivṛt is in verse 9.")],
              [0, 1, 2],
              "The verse names ten items; garlic and trivṛt belong to other verses.",
              "Verse 7: मदन, मधुक, neem, जीमूत, कृतवेधन, पिप्पली, कुटज, इक्ष्वाकु, cardamom, धामार्गव."),
        mcq("transfer", 5,
            "A made-up phrase needs नव + इदम् joined. Which is the correct form?",
            ("नवेदम्", "अ + इ gives ए, as in कुटज + इ… → कुटजे…."),
            [("नवीदम्", "अ + इ does not give ई."),
             ("नवैदम्", "अ + इ does not give ऐ."),
             ("नविदम्", "The two vowels must join.")],
            "The rule that made कुटजेक्ष्वाकूणि also gives नवेदम्.",
            "अ + इ → ए.",
            teaches="A word ending in अ before इ-/ई- is joined with ए."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "उपस्थिते श्लेष्मपित्ते वमनार्थं प्रयुञ्जीत",
    "question": "When does verse 8 say to use the drugs of verse 7, and for what?",
    "rule": ("Verse 8: when Kapha and Pitta are aroused and the disease is seated in the "
             "stomach (आमाशय), the physician should administer these for emesis "
             "(वमन), without harming the body."),
    "limits": ("The verb has no stated object; the drugs of verse 7 are "
               "understood. The verse gives no dose and does not say how "
               "emesis works."),
    "explain_hi": ("श्लोक ७ की सूची का वाक्य यहाँ पूरा होता है: जब कफ और पित्त उभरे "
                   "हों और रोग आमाशय में टिका हो, तब वैद्य शरीर को हानि पहुँचाए "
                   "बिना वमन के लिए (उन द्रव्यों का) प्रयोग करे। ‘उपस्थिते’ और "
                   "‘श्लेष्मपित्ते’ एक साथ स्थिति बताते हैं। संधियाँ: व्याधौ + "
                   "आमाशयाश्रये → व्याधावामाशयाश्रये; भिषक् + देहम् + अदूषयन् → "
                   "भिषग्देहमदूषयन् (क् → ग् घोष द से पहले)।"),
    "hook": "कफ-पित्त उभरे + रोग आमाशय में → वमन के लिए प्रयोग, शरीर को हानि बिना।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 8 says वमनार्थं प्रयुञ्जीत. For which treatment are the drugs of verse 7 used?",
            ("Emesis (वमन)", "वमनार्थम् = for the purpose of emesis."),
            [("Head-purging", "Head-purging is the treatment of verse 5."),
             ("Purgation", "Purgation is named later, with the drugs of verses 9 and 10."),
             ("Bathing", "No bath is mentioned.")],
            "वमनार्थम् is a compound meaning 'for the purpose of emesis'.",
            "Verses 7-8: these drugs are for emesis."),
        match(1, "Match each word of verse 8 to its meaning.",
              [["उपस्थिते", "being present, aroused"], ["व्याधौ", "in disease"],
               ["भिषक्", "physician"], ["देहम्", "body"]],
              "These four are glossed in the data.",
              "उपस्थिते = present/aroused; व्याधौ = in disease; भिषक् = physician; देहम् = body."),
        fill(2, "The verse says the disease has the ____ as its seat (type the Devanagari word for 'stomach').",
             ["आमाशय", "आमाशये", "आमाशयाश्रये", "आमाशयः"],
             "आमाशयाश्रये = आमाशय + आश्रये: having the stomach as seat.",
             "आमाशय-आश्रय is a compound: the stomach is the seat (आश्रय) of the disease.",
             "आमाशयाश्रये = having the stomach as seat."),
        mcq("discriminate", 3, "Which is the right split of भिषग्देहमदूषयन्?",
            ("भिषक् + देहम् + अदूषयन्", "क् becomes ग् before the voiced द; म् joins the vowel अ unchanged."),
            [("भिषग् + देहमद + ऊषयन्", "ऊषयन् is not a word here."),
             ("भिष + गदेहम् + अदूषयन्", "The physician is भिषक्, with a क्."),
             ("भिषक् + देह + मदूषयन्", "मदूषयन् is not a word.")],
            "भिषक् (physician) + देहम् (body) + अदूषयन् (not harming) run together.",
            "Final क् + voiced sound → ग्."),
        mcq("apply", 4,
            "A patient has Kapha and Pitta aroused and the disease seated in the stomach. What does verse 8 say?",
            ("Administer the drugs for emesis, without harming the body",
             "That is the instruction of the verse."),
            [("Administer them for head-purging",
              "The verse says वमनार्थम्, for emesis."),
             ("Wait until the disease has moved elsewhere",
              "The verse gives no instruction to wait."),
             ("Administer them for purgation",
              "The verse says emesis, not purgation.")],
            "उपस्थिते श्लेष्मपित्ते + आमाशयाश्रये व्याधौ → वमनार्थं प्रयुञ्जीत.",
            "Kapha-Pitta aroused + disease in the stomach → administer for emesis."),
        mcq("transfer", 5,
            "A made-up phrase needs भिषक् + जानाति joined. Which is the correct form?",
            ("भिषग्जानाति", "क् becomes ग् before a voiced sound like ज, as in भिषग्देहम्."),
            [("भिषक्जानाति", "The क् is voiceless and must turn voiced before ज."),
             ("भिषख्जानाति", "ख् is not the voiced partner of क्."),
             ("भिषकजानाति", "The stop must be written with its virāma, not as क.")],
            "The same rule gave भिषग्देहम्.",
            "Final क् + voiced sound → ग्.",
            teaches="A final voiceless stop becomes voiced before a voiced sound: क् → ग्."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "त्रिवृतां त्रिफलां दन्तीं",
    "question": "What does verse 9 list, and where does its sentence end?",
    "rule": ("Verse 9 starts the list for the next treatment: त्रिवृत्, the "
             "three myrobalans, दन्ती, नीलिनी, सप्तला, वचा, कम्पिल्लक, गवाक्षी, "
             "क्षीरिणी, उदकीर्यका. The sentence is completed in verse 10."),
    "limits": ("The verse names drugs but not their use; the use is in verse 10. "
               "The data says several identifications are disputed, so names "
               "are kept. उदकीर्यकाम् is read as one plant (उदकीर्या + क)."),
    "explain_hi": ("द्रव्यों की सूची शुरू होती है (श्लोक १० के अनुसार विरेचन के लिए): त्रिवृत्, त्रिफला, दन्ती, "
                   "नीलिनी, सप्तला, वचा, कम्पिल्लक, गवाक्षी, क्षीरिणी और उदकीर्यका। "
                   "कई पौधों की पहचान विवादित है, इसलिए नाम वैसे ही रखे गए हैं। वाक्य "
                   "यहाँ पूरा नहीं होता; उसकी क्रिया और प्रयोग श्लोक १० में हैं। "
                   "संधि: क्षीरिणीम् + उदकीर्यकाम् → क्षीरिणीमुदकीर्यकाम् "
                   "(म् सीधे स्वर से जुड़ा)।"),
    "hook": "श्लोक ९: त्रिवृत्, त्रिफला, दन्ती … उदकीर्यका: केवल नाम; प्रयोग श्लोक १० में।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 9 lists trivṛt, triphalā and more. In which verse is its sentence completed?",
            ("Verse 10", "The data notes: the sentence is completed in verse 10."),
            [("Verse 9 itself", "Verse 9 only names the drugs."),
             ("Verse 8", "Verse 8 completes the earlier sentence about emesis."),
             ("Verse 5", "Verse 5 completes the sentence for head-purging.")],
            "Verses 9 and 10 form one sentence; the verb comes in verse 10.",
            "Verse 9 = list; verb in verse 10."),
        order(1, "Put these four names in the order they are printed in verse 9.",
              ["त्रिवृतां", "त्रिफलां", "दन्तीं", "नीलिनीं"],
              "These are the first four names of the first line.",
              "त्रिवृतां → त्रिफलां → दन्तीं → नीलिनीं."),
        fill(2, "The plant named right after सप्तलां is ____ (type it in Devanagari).",
             ["वचां", "वचाम्", "वचा"],
             "The first line ends सप्तलां वचाम्.",
             "वचाम् is an accusative singular; the glosses call it sweet flag.",
             "वचा follows सप्तला."),
        mcq("discriminate", 3, "Which is the right split of क्षीरिणीमुदकीर्यकाम्?",
            ("क्षीरिणीम् + उदकीर्यकाम्", "म् joins the following vowel without change: two names."),
            [("क्षीरिणी + मुदकीर्यकाम्", "मुदकीर्यकाम् is not a word."),
             ("क्षीरिणीमु + दकीर्यकाम्", "दकीर्यकाम् is not a word."),
             ("क्षीर + इणीमुदकीर्यकाम्", "इणीमुदकीर्यकाम् is not a word.")],
            "क्षीरिणीम् (kṣīriṇī) + उदकीर्यकाम् (udakīryakā) are two names run together.",
            "Final म् + vowel: म् joins the vowel without change."),
        multi("apply", 4, "Which of these does verse 9 name?",
              [("Trivṛt", "Right: त्रिवृताम्."),
               ("Vacā (sweet flag)", "Right: वचाम्."),
               ("Kampillaka", "Right: कम्पिल्लकम्."),
               ("Āragvadha", "Āragvadha is in verse 10."),
               ("Dravantī", "Dravantī is in verse 10.")],
              [0, 1, 2],
              "Verse 9 names ten items; āragvadha and dravantī belong to verse 10.",
              "Verse 9: त्रिवृत्, त्रिफला, दन्ती, नीलिनी, सप्तला, वचा, कम्पिल्लक, गवाक्षी, क्षीरिणी, उदकीर्यका."),
        mcq("transfer", 5,
            "A made-up phrase needs वचाम् + उक्ताम् joined. Which is the correct form?",
            ("वचामुक्ताम्", "म् before a vowel joins it unchanged, as in क्षीरिणीमुदकीर्यकाम्."),
            [("वचोक्ताम्", "That would be वचा + उक्ताम्; here the म् stays."),
             ("वचाम्मुक्ताम्", "No extra म् appears."),
             ("वचानुक्ताम्", "म् does not turn into न् before a vowel.")],
            "The rule that gave क्षीरिणीमुदकीर्यकाम् also gives वचामुक्ताम्.",
            "म् + vowel: म् stays and joins the vowel.",
            teaches="A final म् before a vowel simply joins it in writing."),
    ],
}

NOTES_HI = {
    "1": "‘अतो ऽपामार्ग…’ में विसर्ग → ओ और अगले ‘अ’ का चिह्न ऽ। अथ + अतः → अथातः। शीर्षक का ‘तण्डुल’ किस अर्थ में है, यह डेटा के अनुसार अनिश्चित है; पाठ में कोई पाठभेद नहीं दिया गया।",
    "2": "‘इति ह स्माह’: डेटा के अनुसार ‘ह स्म’ के साथ लिट् का प्रयोग कथन बताने का पारम्परिक साँचा है। स्म + आह → स्माह (अ + आ → आ); भगवान् + आत्रेयः → भगवानात्रेयः (न् सीधे स्वर से जुड़ा)। कोई पाठभेद नहीं।",
    "3": "श्लोक ३ से ५ एक वाक्य हैं; क्रिया ‘दद्यात्’ श्लोक ५ में है। डेटा के अनुसार ‘बीजानि’ अपामार्ग के साथ लिया गया है, पर व्याकरण उसे सभी नामों के साथ भी जोड़ने देता है; विश्वास: मध्यम। संधियाँ जाँची: पिप्पलीः + मरिचानि → पिप्पलीर्मरिचानि; विडङ्गानि + अथ → विडङ्गान्यथ; सर्षपान् + तुम्बुरूणि → सर्षपांस्तुम्बुरूणि। कोई पाठभेद नहीं।",
    "4": "विश्वास: मध्यम। पाठ-टिप्पणी: ‘च अजगन्धां च’ की जगह ‘चाजमोदां च’ भी पढ़ा गया है। अजगन्धा, हरेणुका, पृथ्वीका, श्वेता, कुठेरक, फणिज्झक के नाम बिना पहचान के रखे गए हैं। संधियाँ: च + अजगन्धाम् → चाजगन्धाम्; पीलूनि + एलाम् → पीलून्येलाम्। ‘कुठेरकफणिज्झकौ’ को डेटा द्वन्द्व का द्विवचन मानता है।",
    "5": "‘दो हल्दियाँ’ और ‘दो नमक’ के नाम श्लोक में नहीं दिए; परम्परा से वे बताए जाते हैं (डेटा की टिप्पणी)। दद्यात् श्लोक ३, ४ और ५ की सूचियों का क्रियापद है। संधि: दद्यात् + शीर्षविरेचने → दद्याच्छीर्षविरेचने (त् + श → च्छ)। कोई पाठभेद नहीं।",
    "6": "श्लोक ५ से चलता है; ये शिरोविरेचन-द्रव्यों के प्रयोग के रोग हैं। ‘शिरसः’ केवल ‘शूले’ के साथ है या ‘गौरवे’ के साथ भी, यह संस्कृत से तय नहीं होता। ‘प्रमोहक’ शब्दार्थ से लिया गया है, परिभाषा श्लोक में नहीं। संधियाँ: पीनसे ऽर्धावभेदके; क्रिमिव्याधौ + अपस्मारे → क्रिमिव्याधावपस्मारे।",
    "7": "विश्वास: मध्यम। वाक्य श्लोक ८ में पूरा होता है (वमनार्थं प्रयुञ्जीत)। डेटा ‘पिप्पलीकुटजेक्ष्वाकूणि’ को तीन नामों का समास मानता है; मधुक, जीमूत, कृतवेधन, धामार्गव के नाम बिना पहचान के रखे गए हैं। संधियाँ: कुटज + इक्ष्वाकूणि → कुटजेक्ष्वाकूणि; …ूणि + एलाम् → …ूण्येलाम्।",
    "8": "‘प्रयुञ्जीत’ का कर्म श्लोक में नहीं है; श्लोक ७ के द्रव्य सन्दर्भ से समझे जाते हैं। ‘श्लेष्मपित्ते’ द्वन्द्व (समाहार) है; ‘आमाशयाश्रये’ बहुव्रीहि है। संधियाँ: व्याधौ + आमाशयाश्रये → व्याधावामाशयाश्रये; आमाशय + आश्रये → आमाशयाश्रये; भिषक् + देहम् + अदूषयन् → भिषग्देहमदूषयन्। कोई पाठभेद नहीं।",
    "9": "विश्वास: मध्यम। कई पौधों की पहचान विवादित है, नाम रखे गए हैं। ‘उदकीर्यकाम्’ को उदकीर्या + क (वही पौधा) पढ़ा गया है। वाक्य श्लोक १० में पूरा होता है (विरेकार्थं प्रयोजयेत्)। संधि: क्षीरिणीम् + उदकीर्यकाम् → क्षीरिणीमुदकीर्यकाम्। कोई पाठभेद नहीं।",
}

AIDS = {
    "1": {
        "frame": "क्या: नया अध्याय · नाम: अपामार्गतण्डुलीय · क्रिया: व्याख्यास्यामः (हम समझाएँगे)।",
        "sandhi": "अः + अ → ओ + ऽ: अतः + अपामार्ग… → अतो ऽपामार्ग…। अ + अ → आ: अथ + अतः → अथातः।",
        "anchors": "व्याख्यास्यामः ← वि + आ + √ख्या · अध्याय · अपामार्ग + तण्डुल + ईय: ‘…सम्बन्धी’।",
        "chunks": "अथातो ऽपामार्गतण्डुलीयमध्यायं | व्याख्यास्यामः।",
    },
    "2": {
        "frame": "वक्ता: भगवान् आत्रेय · क्रिया: आह (कहा) · ढाँचा: इति ह स्म।",
        "sandhi": "अ + आ → आ: स्म + आह → स्माह। न् + आ सटे: भगवान् + आत्रेयः → भगवानात्रेयः।",
        "pegs": "मेरा बनाया चित्र: एक गुरु हाथ उठाकर बोल रहा है और उसके मुँह के आगे एक उद्धरण-चिह्न (”) लटक रहा है: ‘इति’।",
        "chunks": "इति ह | स्माह | भगवानात्रेयः।",
    },
    "3": {
        "frame": "क्या: द्रव्यों की सूची · क्रिया: अभी नहीं (श्लोक ५ में दद्यात्) · प्रयोग: अभी नहीं।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["अपामार्गस्य", "बीजानि", "पिप्पलीर्मरिचानि", "च"]},
            {"label": "दूसरी पंक्ति",
             "items": ["विडङ्गान्यथ", "शिग्रूणि", "सर्षपांस्तुम्बुरूणि", "च"]}]},
        "sandhi": "ई-विसर्ग + घोष → र्: पिप्पलीः + मरिचानि → पिप्पलीर्मरिचानि। इ → य्: विडङ्गानि + अथ → विडङ्गान्यथ। न् + त → ंस्त: सर्षपान् + तुम्बुरूणि → सर्षपांस्तुम्बुरूणि।",
        "letters": "अ-पि-म-वि-शि-स-तु: अपामार्ग, पिप्पली, मरिच, विडङ्ग, शिग्रु, सर्षप, तुम्बुरु (नामों के पहले अक्षर)।",
        "chunks": "अपामार्गस्य बीजानि | पिप्पलीर्मरिचानि च ‖ विडङ्गान्यथ शिग्रूणि | सर्षपांस्तुम्बुरूणि च।",
    },
    "4": {
        "frame": "क्या: सूची जारी · क्रिया: अब भी नहीं (श्लोक ५) · पाठ-टिप्पणी: अजगन्धा की जगह अजमोदा।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["अजाजीं", "चाजगन्धां", "च", "पीलून्येलां", "हरेणुकाम्"]},
            {"label": "दूसरी पंक्ति",
             "items": ["पृथ्वीकां", "सुरसां", "श्वेतां", "कुठेरकफणिज्झकौ"]}]},
        "sandhi": "अ + अ → आ: च + अजगन्धाम् → चाजगन्धाम्। इ → य्: पीलूनि + एलाम् → पीलून्येलाम्।",
        "contrast": "पाठ: ‘चाजगन्धां च’ ↔ पाठ-टिप्पणी: ‘चाजमोदां च’। कार्ड दोनों में से चुनता नहीं।",
        "chunks": "अजाजीं चाजगन्धां च | पीलून्येलां हरेणुकाम् ‖ पृथ्वीकां सुरसां श्वेतां | कुठेरकफणिज्झकौ।",
    },
    "5": {
        "frame": "क्या: शिरीष-बीज आदि छह · क्रिया: दद्यात् (दें) · कहाँ: शीर्षविरेचने (शिरोविरेचन में)।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["शिरीषबीजं", "लशुनं", "हरिद्रे", "लवणद्वयम्"]},
            {"label": "दूसरी पंक्ति",
             "items": ["ज्योतिष्मतीं", "नागरं", "च", "दद्याच्छीर्षविरेचने"]}]},
        "sandhi": "त् + श → च्छ: दद्यात् + शीर्षविरेचने → दद्याच्छीर्षविरेचने।",
        "pegs": "मेरा बनाया चित्र: सिर पर एक बड़ा लहसुन की गाँठ, उसके नीचे दो हल्दी की गाँठें और दो नमक की डलियाँ: ‘सिर के लिए’ याद रखने को।",
        "story": "वाक्य श्लोक ३ से चला: बीज, मिर्च, सरसों, जीरा, इलायची … और अन्त में ‘ये सब दें, शिरोविरेचन में’।",
        "chunks": "शिरीषबीजं लशुनं | हरिद्रे लवणद्वयम् ‖ ज्योतिष्मतीं नागरं च | दद्याच्छीर्षविरेचने।",
    },
    "6": {
        "frame": "क्या: रोगों की सूची (शिरसः छोड़कर सप्तमी: ‘…में’) · किसके लिए: श्लोक ५ के द्रव्य · क्रिया: श्लोक ५ से चलती।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["गौरवे", "शिरसः", "शूले", "पीनसे", "ऽर्धावभेदके"]},
            {"label": "दूसरी पंक्ति",
             "items": ["क्रिमिव्याधावपस्मारे", "घ्राणनाशे", "प्रमोहके"]}]},
        "sandhi": "औ + स्वर → आव्: क्रिमिव्याधौ + अपस्मारे → क्रिमिव्याधावपस्मारे। ए + अ → ए ऽ: पीनसे ऽर्धावभेदके।",
        "pegs": "मेरा बनाया चित्र: एक सिर और उस पर आठ छोटे दरवाज़े, हर दरवाज़े पर एक रोग का नाम लिखा; सभी ‘…में’ (-ए) पर खुलते हैं।",
        "anchors": "शूल = पीड़ा · अपस्मार = मिर्गी (श्लोक का अनुवाद) · घ्राण = नाक/गन्ध · नाश = न रहना।",
        "chunks": "गौरवे शिरसः शूले | पीनसे ऽर्धावभेदके ‖ क्रिमिव्याधावपस्मारे | घ्राणनाशे प्रमोहके।",
    },
    "7": {
        "frame": "क्या: दस नामों की सूची · क्रिया: श्लोक ८ में · प्रयोग: श्लोक ८ में।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["मदनं", "मधुकं", "निम्बं", "जीमूतं", "कृतवेधनम्"]},
            {"label": "दूसरी पंक्ति",
             "items": ["पिप्पलीकुटजेक्ष्वाकूण्येलां", "धामार्गवाणि", "च"]}]},
        "sandhi": "अ + इ → ए: कुटज + इक्ष्वाकूणि → कुटजेक्ष्वाकूणि। इ → य्: …ूणि + एलाम् → …ूण्येलाम्।",
        "letters": "म-म-नि-जी-कृ-पि-कु-इ-ए-धा: मदन, मधुक, निम्ब, जीमूत, कृतवेधन, पिप्पली, कुटज, इक्ष्वाकु, एला, धामार्गव।",
        "chunks": "मदनं मधुकं निम्बं | जीमूतं कृतवेधनम् ‖ पिप्पलीकुटजेक्ष्वाकूण्येलां | धामार्गवाणि च।",
    },
    "8": {
        "frame": "कब: कफ-पित्त उभरे + रोग आमाशय में · क्या करें: प्रयोग करें · किसलिए: वमन · कैसे: शरीर को हानि बिना।",
        "chain": {"steps": ["कफ और पित्त उभरे हों (उपस्थिते श्लेष्मपित्ते)",
                            "रोग का आश्रय आमाशय हो",
                            "वैद्य वमन के लिए प्रयोग करे (वमनार्थं प्रयुञ्जीत)",
                            "शरीर को हानि न पहुँचाए (देहमदूषयन्)"]},
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["उपस्थिते", "श्लेष्मपित्ते", "व्याधावामाशयाश्रये"]},
            {"label": "दूसरी पंक्ति",
             "items": ["वमनार्थं", "प्रयुञ्जीत", "भिषग्देहमदूषयन्"]}]},
        "sandhi": "औ + आ → आव्: व्याधौ + आमाशयाश्रये → व्याधावामाशयाश्रये। क् → ग्: भिषक् + देहम् + अदूषयन् → भिषग्देहमदूषयन्।",
        "chunks": "उपस्थिते श्लेष्मपित्ते | व्याधावामाशयाश्रये ‖ वमनार्थं प्रयुञ्जीत | भिषग्देहमदूषयन्।",
    },
    "9": {
        "frame": "क्या: द्रव्यों के दस नाम (विरेचन: श्लोक १० के अनुसार) · क्रिया: श्लोक १० में · प्रयोग: श्लोक १० में।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["त्रिवृतां", "त्रिफलां", "दन्तीं", "नीलिनीं", "सप्तलां", "वचाम्"]},
            {"label": "दूसरी पंक्ति",
             "items": ["कम्पिल्लकं", "गवाक्षीं", "च", "क्षीरिणीमुदकीर्यकाम्"]}]},
        "sandhi": "म् + स्वर सटते हैं: क्षीरिणीम् + उदकीर्यकाम् → क्षीरिणीमुदकीर्यकाम्।",
        "letters": "त्रि-त्रि-द-नी-स-व-क-ग-क्षी-उ: त्रिवृत्, त्रिफला, दन्ती, नीलिनी, सप्तला, वचा, कम्पिल्लक, गवाक्षी, क्षीरिणी, उदकीर्यका।",
        "chunks": "त्रिवृतां त्रिफलां दन्तीं | नीलिनीं सप्तलां वचाम् ‖ कम्पिल्लकं गवाक्षीं च | क्षीरिणीमुदकीर्यकाम्।",
    },
}

IMAGE_SPECS = {
    ("5", "diagram"): {
        "file": "ch2-drugs-5.svg",
        "alt": "Two columns showing verse 5 line by line: first line has four items (शिरीष seed, garlic, two haridrās, pair of salts); second line has jyotiṣmatī, dry ginger, च and the closing words दद्याच्छीर्षविरेचने",
        "type": "split",
        "title": "श्लोक ५: शीर्षविरेचन के द्रव्य",
        "cols": [["पहली पंक्ति", ["शिरीषबीजं", "लशुनं", "हरिद्रे", "लवणद्वयम्"]],
                 ["दूसरी पंक्ति", ["ज्योतिष्मतीं", "नागरं", "च", "दद्याच्छीर्षविरेचने"]]],
    },
    ("6", "diagram"): {
        "file": "ch2-conditions-6.svg",
        "alt": "Two columns showing verse 6 line by line: five words in the first line (heaviness, of the head, pain, pīnasa, half-headache) and three in the second (worm disease with epilepsy, loss of smell, pramohaka)",
        "type": "split",
        "title": "श्लोक ६: रोग",
        "cols": [["पहली पंक्ति", ["गौरवे", "शिरसः", "शूले", "पीनसे", "ऽर्धावभेदके"]],
                 ["दूसरी पंक्ति", ["क्रिमिव्याधावपस्मारे", "घ्राणनाशे", "प्रमोहके"]]],
    },
    ("9", "diagram"): {
        "file": "ch2-purge-9.svg",
        "alt": "Two columns showing verse 9 line by line: six drug names in the first line (trivṛt, triphalā, dantī, nīlinī, saptalā, vacā) and four in the second (kampillaka, gavākṣī, च, kṣīriṇī with udakīryakā)",
        "type": "split",
        "title": "श्लोक ९: विरेचन के द्रव्य",
        "cols": [["पहली पंक्ति", ["त्रिवृतां", "त्रिफलां", "दन्तीं", "नीलिनीं", "सप्तलां", "वचाम्"]],
                 ["दूसरी पंक्ति", ["कम्पिल्लकं", "गवाक्षीं", "च", "क्षीरिणीमुदकीर्यकाम्"]]],
    },
}
