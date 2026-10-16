from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}
NOTES_HI = {}
AIDS = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथात आरग्वधीयमध्यायम्",
    "question": "How does this chapter announce itself, and what is it called?",
    "rule": ("अथात आरग्वधीयमध्यायं व्याख्यास्यामः = 'Now, therefore, we shall "
             "expound the chapter called Āragvadhīya.' The title आरग्वधीय "
             "means 'relating to āragvadha'; the data says it is named after "
             "the first drug mentioned."),
    "limits": ("This is only the opening formula. It names the chapter and "
               "promises an exposition; it lists no drug and gives no "
               "teaching yet. That the name comes from the first drug of the "
               "chapter is the data's note, not something this sentence says."),
    "explain_hi": ("यह अध्याय का आरम्भ-वाक्य है, एक मानक साँचा (डेटा की टिप्पणी)। "
                   "‘अथ’ का अर्थ ‘अब’ और ‘अतः’ का अर्थ ‘इसलिए’ है; दोनों मिलकर ‘अथातः’ बनते हैं "
                   "और छपे पाठ में विसर्ग ‘आरग्वधीयम्’ से पहले लुप्त होकर ‘अथात आरग्वधीयम्…’ दिखता है। "
                   "‘आरग्वधीयम्’ अध्याय का नाम है (‘आरग्वध से सम्बन्धित’), और ‘व्याख्यास्यामः’ का अर्थ है "
                   "‘हम समझाएँगे’। नाम पहली औषधि आरग्वध से आया बताया गया है।"),
    "hook": "अथ – अतः – व्याख्यास्यामः: ‘अब – इसलिए – हम समझाएँगे’; नाम = आरग्वधीय।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The sentence अथात आरग्वधीयमध्यायं व्याख्यास्यामः opens a chapter. What does it announce?",
            ("The chapter named Āragvadhīya will now be expounded",
             "आरग्वधीयम् names the chapter and व्याख्यास्यामः promises the exposition."),
            [("A royal command to start a journey", "Nothing in the sentence concerns a king or a journey."),
             ("A list of drugs and their doses", "No drug and no dose is named in this sentence."),
             ("A prayer to a god", "No god is addressed; the sentence introduces a chapter.")],
            "अध्यायम् (chapter) and व्याख्यास्यामः (we shall expound) show that a chapter is being introduced.",
            "The opening sentence names the chapter and promises to explain it."),
        match(1, "Match each word of the opening sentence to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["आरग्वधीयम्", "the chapter's name, relating to āragvadha"],
               ["व्याख्यास्यामः", "we shall expound"]],
              "These words carry the whole announcement.",
              "अथ = now; अतः = therefore; आरग्वधीयम् = the title; व्याख्यास्यामः = we shall expound."),
        fill(2, "The word for 'chapter' in the sentence is ____ (type it in Devanagari).",
             ["अध्यायम्", "अध्यायं"],
             "The sentence says अध्यायम् for 'chapter'.",
             "अध्यायम् ends in -म् (accusative): the chapter is what is to be expounded, the object of the verb.",
             "अध्यायम् = chapter, the thing expounded."),
        mcq("discriminate", 3, "Which is the right split of अथातः?",
            ("अथ + अतः", "अ + अ gives आ, so अथ + अतः is written अथातः."),
            [("अथा + तः", "There is no word तः here."),
             ("अथ + आतः", "आतः is not a word in this sentence."),
             ("अ + थातः", "थातः is not a word.")],
            "अथातः is अथ ('now') + अतः ('therefore') joined by sandhi.",
            "अथातः = अथ + अतः (अ + अ → आ)."),
        multi("apply", 4, "Which of these statements about the opening sentence are right?",
              [("व्याख्यास्यामः is first person plural: 'we shall expound'",
                "Right: -मः marks 'we', and the data labels it first person plural future."),
               ("आरग्वधीयम् is the name of the chapter",
                "Right: it stands before अध्यायम् and names the chapter."),
               ("अथ means 'now'", "Right: the data glosses अथ as 'now'."),
               ("The sentence says the speaker is Bhagavān Ātreya",
                "The speaker is named in verse 2, not in this sentence."),
               ("The sentence names the first drug of the chapter",
                "The sentence names only the chapter; the drug is not stated here.")],
              [0, 1, 2],
              "The first three statements are in the sentence; the last two are not.",
              "Verse 1: the formula, the title आरग्वधीयम् and the promise to expound."),
        mcq("transfer", 5,
            "A made-up chapter opens अथातो नवौषधीयमध्यायं व्याख्यास्यामः. Which word names that chapter?",
            ("नवौषधीयम्", "The title stands before अध्यायम्, as आरग्वधीयम् does here."),
            [("व्याख्यास्यामः", "That is the verb 'we shall expound'."),
             ("अध्यायम्", "That is the word for 'chapter', not its name."),
             ("अथातः", "That is the opening 'now, therefore'.")],
            "In this frame the title sits just before अध्यायम्; the rest of the sentence is the same formula.",
            "The opening frame is shared; the chapter's name stands before अध्यायम्.",
            teaches="Once you know the frame, you can find a chapter's title by looking at the word before अध्यायम्."),
    ],
}

NOTES_HI["1"] = ("संधियाँ जाँची: अथ + अतः → अथातः (अ + अ → आ); अथातः के बाद ‘आरग्वधीयम्’ (भिन्न स्वर) से पहले विसर्ग लुप्त → "
                 "छपा रूप ‘अथात आरग्वधीयम्’; आरग्वधीयम् + अध्यायम् → आरग्वधीयमध्यायम् (म् अगले स्वर से सटा)। "
                 "‘अध्यायं’ अनुस्वार वाला छपा रूप है, ‘अध्यायम्’ वही है। इस श्लोक में कोई पाठभेद या पाठ-दोष नहीं दिया गया। "
                 "नाम की व्याख्या (पहली औषधि आरग्वध से) डेटा की टिप्पणी है, वाक्य की नहीं।")

AIDS["1"] = {
    "frame": "क्या: अध्याय का आरम्भ-वाक्य · नाम: आरग्वधीय · क्रिया: व्याख्यास्यामः (हम समझाएँगे)।",
    "diagram": {"groups": [
        {"label": "वाक्य",
         "items": ["अथात", "आरग्वधीयमध्यायं", "व्याख्यास्यामः"]}]},
    "sandhi": "अ + अ → आ: अथ + अतः → अथातः। अथातः + आरग्वधीयम्: भिन्न स्वर से पहले विसर्ग लुप्त → अथात आरग्वधीयम्। म् + स्वर: आरग्वधीयम् + अध्यायम् → आरग्वधीयमध्यायम्।",
    "anchors": "आरग्वधीयम् = आरग्वध + ईय (‘आरग्वध से सम्बन्धित’) · व्याख्यास्यामः = वि-आ-√ख्या का उत्तम पुरुष बहुवचन भविष्य: ‘हम समझाएँगे’।",
    "chunks": "अथात आरग्वधीयमध्यायं | व्याख्यास्यामः।",
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "इति ह स्माह भगवानात्रेयः",
    "question": "Who is said to have spoken, and what do the small words इति ह स्म do?",
    "rule": ("इति ह स्माह भगवानात्रेयः = 'Thus, indeed, spoke the venerable "
             "Ātreya.' इति ह स्माह is a fixed formula of reported speech; the "
             "speaker भगवान् आत्रेयः is in the nominative."),
    "limits": ("The verse names the speaker and nothing else: no teaching "
               "and no drug. The data says the particles ह and स्म add no "
               "separate sense beyond 'indeed, (so) said'."),
    "explain_hi": ("यह छोटा-सा सूत्र-वाक्य बताता है कि आगे का उपदेश किसने कहा: ‘भगवान् आत्रेय’। "
                   "‘इति ह स्माह’ एक बँधा हुआ साँचा है, ‘ऐसा निश्चय ही कहा’। ‘ह’ और ‘स्म’ निपात हैं; "
                   "डेटा के अनुसार वे ‘निश्चय ही’ से अधिक कोई अलग अर्थ नहीं जोड़ते। ‘आह’ क्रिया है (‘उसने कहा’), "
                   "और ‘भगवान् आत्रेयः’ कर्ता है, प्रथमा एकवचन।"),
    "hook": "इति ह स्माह = ‘ऐसा निश्चय ही कहा’; कर्ता = भगवान् आत्रेय।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In इति ह स्माह भगवानात्रेयः, who is the speaker?",
            ("The venerable Ātreya", "भगवान् आत्रेयः is the subject of आह, 'said'."),
            [("The physician who applies the pastes", "No physician is mentioned in this verse."),
             ("A pupil asking a question", "No pupil or question appears here."),
             ("The reader of the chapter", "The reader is not named; the speaker is Ātreya.")],
            "आह is the verb 'said' and भगवान् आत्रेयः is its subject.",
            "Verse 2: the speaker is named as भगवान् आत्रेयः."),
        match(1, "Match each word of verse 2 to its meaning.",
              [["इति", "thus"], ["ह", "indeed"], ["आह", "said"], ["भगवान्", "the venerable"]],
              "The four words give 'Thus indeed said the venerable Ātreya'.",
              "इति = thus; ह = indeed; आह = said; भगवान् = the venerable."),
        fill(2, "The verb meaning 'said' in verse 2 is ____ (type it in Devanagari, without स्म).",
             ["आह"],
             "The verb is आह, which joins the particle स्म to give स्माह.",
             "आह is third person singular perfect of √अह्; the speaker is in the nominative.",
             "आह = he said; the subject stands in the nominative."),
        mcq("discriminate", 3, "Which is the right split of भगवानात्रेयः?",
            ("भगवान् + आत्रेयः", "The final न् of भगवान् stands before the vowel आ and simply joins it."),
            [("भगवा + नात्रेयः", "नात्रेयः is not a word."),
             ("भगवान् + अत्रेयः", "The name is Ātreya with long आ, not Atreya."),
             ("भगवानः + आत्रेयः", "भगवान् is the nominative singular; it has no visarga ending here.")],
            "भगवानात्रेयः is two words, भगवान् ('the venerable') and आत्रेयः.",
            "भगवानात्रेयः = भगवान् + आत्रेयः."),
        mcq("apply", 4, "What does स्माह combine?",
            ("स्म + आह, with अ + आ → आ", "The particle स्म ends in -अ, and आह begins with आ; the two join as आ."),
            [("स्मा + अह", "अह is not the form here; the verb is आह."),
             ("सु + माह", "माह is not a word."),
             ("स्म + याह", "याह is not a word.")],
            "स्माह is the particle स्म joined to the verb आह.",
            "अ + आ → आ: स्म + आह → स्माह."),
        mcq("transfer", 5,
            "A made-up line reads इति ह स्माह वैद्यः. Which word is the speaker?",
            ("वैद्यः", "Like आत्रेयः here, it is the nominative subject of आह."),
            [("आह", "That is the verb 'said'."),
             ("इति", "That means 'thus'."),
             ("ह", "That is the particle 'indeed'.")],
            "The frame इति ह स्माह is followed by the speaker in the nominative: here वैद्यः.",
            "After इति ह स्माह the speaker's name follows in the nominative.",
            teaches="You can find the speaker of any such report by looking for the nominative after आह."),
    ],
}

NOTES_HI["2"] = ("संधियाँ जाँची: स्म + आह → स्माह (अ + आ → आ); भगवान् + आत्रेयः → भगवानात्रेयः (अन्तिम न् अगले स्वर से सट जाता है, कोई परिवर्तन नहीं)। "
                 "डेटा की टिप्पणी: ‘इति ह स्माह’ बँधा हुआ साँचा है और ‘ह’, ‘स्म’ अलग अर्थ नहीं जोड़ते। "
                 "इस श्लोक में कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["2"] = {
    "frame": "क्या कहा: (आगे का उपदेश) · किसने: भगवान् आत्रेय · साँचा: इति ह स्माह = ऐसा निश्चय ही कहा।",
    "diagram": {"groups": [
        {"label": "वाक्य",
         "items": ["इति", "ह", "स्माह", "भगवानात्रेयः"]}]},
    "sandhi": "अ + आ → आ: स्म + आह → स्माह। न् + स्वर: भगवान् + आत्रेयः → भगवानात्रेयः (न् अगले स्वर से सटा)।",
    "anchors": "इति = ऐसा · ह स्म = निपात (‘निश्चय ही’) · आह = उसने कहा · भगवान् आत्रेयः = कर्ता (प्रथमा एकवचन)।",
    "chunks": "इति ह स्माह | भगवानात्रेयः।",
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "आरग्वधः सैडगजः करञ्जो वासा",
    "question": "What kind of verse is verse 3, and what does the form हरिद्रे show?",
    "rule": ("Verse 3 is a drug list with no verb: two printed lines, each a "
             "drug group, to be completed by verse 6. हरिद्रे is a feminine "
             "dual: 'the two haridrās'."),
    "limits": ("Only names: no use, no disease, no dose, no verb. The verse "
               "does not say which two haridrās; श्र्याह्वः and सुराह्वः are "
               "descriptive names ('called Śrī', 'called Sura') whose "
               "identification is left to commentators. सैडगजः may belong to "
               "āragvadha or be read with karañja (the data marks it two-way)."),
    "explain_hi": ("यह श्लोक केवल औषधों की सूची है; इसमें कोई क्रिया नहीं है, वाक्य श्लोक ६ में पूरा होगा "
                   "(छह आधे-श्लोक = छह चूर्ण-समूह; यहाँ की दो पंक्तियाँ दो समूह हैं)। नाम हैं: आरग्वध (एडगज के साथ), करञ्ज, वासा, "
                   "गुडूची, मदन, दोनों हरिद्राएँ; ‘श्री’ नामक, ‘सुर’ नामक, खदिर, धव, निम्ब, विडङ्ग और करवीरक की छाल। "
                   "‘हरिद्रे’ द्विवचन है: दो हरिद्राएँ, पर कौन-सी दो, यह श्लोक नहीं बताता। "
                   "‘सैडगजः’ का ‘एडगज’ आरग्वध के साथ भी पढ़ा जा सकता है और करञ्ज के साथ भी; डेटा दोनों पाठ मानता है।"),
    "hook": "श्लोक ३: केवल नाम, क्रिया नहीं; हरिद्रे = दो हरिद्राएँ; पूर्ति श्लोक ६ में।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 3 mainly contain?",
            ("A list of drug names with no verb; the sentence is finished in verse 6",
             "Every item is a drug name or a drug part, and no verb appears."),
            [("A dose for each drug", "The verse gives no dose."),
             ("The diseases the drugs remove", "Diseases are named in verse 7, not here."),
             ("A prayer to Ātreya", "Ātreya is named in verse 2; this verse is a list.")],
            "The verse runs from आरग्वधः to करवीरकत्वक् as a plain list.",
            "Verse 3: a list of drug names, completed by verse 6."),
        match(1, "Match each word of verse 3 to its meaning.",
              [["हरिद्रे", "the two haridrās"],
               ["श्र्याह्वः", "the one named Śrī"],
               ["सुराह्वः", "the one named Sura"],
               ["करवीरकत्वक्", "bark of karavīraka"]],
              "These four items are descriptive or grammatical, not just plant names.",
              "हरिद्रे = the two haridrās; श्र्याह्वः = the one named Śrī; सुराह्वः = the one named Sura; करवीरकत्वक् = bark of karavīraka."),
        fill(2, "The word in the last compound of verse 3 for 'bark' is ____ (type the final word of करवीरकत्वक् in Devanagari).",
             ["त्वक्", "त्वच्", "त्वच", "त्वचा"],
             "The compound is करवीरक + त्वक्, 'bark of karavīraka'.",
             "In करवीरकत्वक् the first part names the plant and the last part names the part used: 'bark of karavīraka'.",
             "X-त्वक् = bark of X."),
        mcq("discriminate", 3, "Why is the printed form करञ्जो वासा and not करञ्जः वासा?",
            ("अः before a voiced consonant (here व) becomes ओ", "The visarga after अ turns into ओ before a voiced sound."),
            [("The visarga is dropped before any consonant", "The visarga does not drop here; it turns into ओ."),
             ("ज becomes ओ before वासा", "Only the visarga changes, not the ज."),
             ("करञ्ज is a feminine word and takes ओ", "करञ्जः is nominative singular masculine; the ओ is sandhi, not a case ending.")],
            "करञ्जः + वासा → करञ्जो वासा. The same rule gives खदिरो धवः and निम्बो विडङ्गम्.",
            "अः + घोष (voiced sound) → ओ."),
        multi("apply", 4, "Which of these statements are right for verse 3?",
              [("It has no verb", "Right: it only lists names."),
               ("हरिद्रे is a dual form", "Right: the data labels it feminine nominative dual."),
               ("It names the disease each drug serves", "Diseases are named in verse 7."),
               ("It gives the dose of each drug", "No dose appears in this verse."),
               ("Each of its two printed lines is one drug group", "Right: the data says each printed line is one group, six groups in all with verses 4 and 5.")],
              [0, 1, 4],
              "Verse 3 is a bare list of two drug groups; the verbs and the uses come later.",
              "Verse 3: two drug groups, no verb, no use, no dose."),
        mcq("transfer", 5,
            "A made-up line lists लते शुष्के as subjects, nominative case (लता = creeper, feminine in -आ). By the pattern of हरिद्रे, how many creepers?",
            ("Two (a dual)", "-आ nouns form a feminine nominative dual in -ए, as हरिद्रा gives हरिद्रे."),
            [("One", "The singular would be लता."),
             ("Many", "The plural would be लताः."),
             ("None", "The word names creepers; it does not negate them.")],
            "The pair लते शुष्के has the dual ending -ए on both words: 'two dry creepers'.",
            "Feminine -आ stem, nominative dual: -ए (हरिद्रा → हरिद्रे).",
            teaches="You can spot a dual of a feminine -आ noun by the ending -ए."),
    ],
}

NOTES_HI["3"] = ("संधियाँ जाँची: एडगजः → सैडगजः (स + एडगज: अ + ए → ऐ); करञ्जः + वासा → करञ्जो वासा, खदिरः + धवः → खदिरो धवः, निम्बः + विडङ्गम् → निम्बो विडङ्गम् "
                 "(अः + घोष → ओ); धवः + च → धवश्च (विसर्ग + च → श्); श्री + आह्वः → श्र्याह्वः (ई + आ → या); सुर + आह्वः → सुराह्वः (अ + आ → आ)। "
                 "द्विधा पाठ: ‘सैडगजः’ आरग्वध के साथ भी चल सकता है और करञ्ज के साथ भी (डेटा की टिप्पणी)। ‘हरिद्रे’ द्विवचन है पर कौन-सी दो, श्लोक नहीं कहता। "
                 "कोई पाठभेद या पाठ-दोष डेटा में नहीं दिया गया।")

AIDS["3"] = {
    "frame": "क्या: औषधों की सूची (कोई क्रिया नहीं) · दो पंक्तियाँ = दो चूर्ण-समूह · पूर्ति: श्लोक ६ · हरिद्रे = द्विवचन।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["आरग्वधः", "सैडगजः", "करञ्जो", "वासा", "गुडूची", "मदनं", "हरिद्रे"]},
        {"label": "दूसरी पंक्ति",
         "items": ["श्र्याह्वः", "सुराह्वः", "खदिरो", "धवश्च", "निम्बो", "विडङ्गं", "करवीरकत्वक्"]}]},
    "sandhi": "अः + घोष → ओ: करञ्जः + वासा → करञ्जो वासा; खदिरः + धवः → खदिरो धवः; निम्बः + विडङ्गम् → निम्बो विडङ्गम्। विसर्ग + च → श्च: धवः + च → धवश्च। ई + आ → या: श्री + आह्वः → श्र्याह्वः।",
    "contrast": "हरिद्रा (एक, स्त्रीलिंग एकवचन) ↔ हरिद्रे (दो, द्विवचन): अन्त के -आ की जगह -ए।",
    "anchors": "श्र्याह्वः = श्री नामक, सुराह्वः = सुर नामक (बहुव्रीहि; पहचान टीकाकारों पर छोड़ी गई) · करवीरकत्वक् = करवीरक + त्वक् (करवीरक की छाल)।",
    "chunks": "आरग्वधः सैडगजः करञ्जो | वासा गुडूची मदनं हरिद्रे ‖ श्र्याह्वः सुराह्वः खदिरो | धवश्च निम्बो विडङ्गं करवीरकत्वक्।",
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "ग्रन्थिश्च भौर्जो लशुनः शिरीषः",
    "question": "What is verse 4, and what do the endings in वत्सकसप्तपर्णौ show?",
    "rule": ("Verse 4 continues the drug list of verse 3 with no verb. "
             "वत्सकसप्तपर्णौ is a dual pair (vatsaka and saptaparṇa) and "
             "गुग्गुलुकृष्णगन्धे is read as the dual pair guggulu and "
             "kṛṣṇagandhā."),
    "limits": ("Names only: no use, no dose. The data keeps many names "
               "(granthi, bhaurja, lomaśa and others) untranslated, with "
               "meanings uncertain. सलोमशः (sa + lomaśa or 'hairy') and the "
               "gender of गुग्गुलुकृष्णगन्धे are open; no question here "
               "depends on them."),
    "explain_hi": ("यह श्लोक श्लोक ३ की सूची को आगे बढ़ाता है; अब भी कोई क्रिया नहीं है और वाक्य श्लोक ६ में पूरा होगा। "
                   "नाम हैं: ग्रन्थि, भौर्ज, लहसुन, शिरीष, लोमश के साथ, गुग्गुलु और कृष्णगन्धा, फणिज्झक, वत्सक और सप्तपर्ण, पीलु, कुष्ठ तथा सुमनस् की कोंपलें। "
                   "‘वत्सकसप्तपर्णौ’ में -औ द्विवचन है: ‘वत्सक और सप्तपर्ण’, दो नाम जुड़े हुए। "
                   "‘पीलूनि’ नपुंसक बहुवचन है। डेटा कहता है कि कई नाम (ग्रन्थि, भौर्ज, लोमश आदि) वैसे ही रखे गए हैं, उनका अर्थ टीका के बिना अनिश्चित है।"),
    "hook": "श्लोक ४: सूची जारी; -औ द्विवचन = दो नाम (वत्सक-सप्तपर्णौ)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 4 mainly contain?",
            ("More drug names, continuing the list of verse 3, with no verb",
             "Verse 4 continues the list; the sentence is finished in verse 6."),
            [("The diseases that the drugs remove", "Diseases come in verse 7."),
             ("How the drugs are soaked in cow's bile", "That is verse 6, not verse 4."),
             ("A new chapter title", "The title was given in verse 1.")],
            "The verse runs on from ग्रन्थिः to सुमनःप्रवालाः as a plain list.",
            "Verse 4: the drug list goes on; no verb, use or dose."),
        match(1, "Match each word of verse 4 to its meaning.",
              [["वत्सकसप्तपर्णौ", "vatsaka and saptaparṇa (a pair)"],
               ["गुग्गुलुकृष्णगन्धे", "guggulu and kṛṣṇagandhā (a pair)"],
               ["पीलूनि", "pīlus (neuter plural)"],
               ["सुमनःप्रवालाः", "sumanas shoots"]],
              "Two of these are dual pairs; the others are a plural and a compound.",
              "वत्सकसप्तपर्णौ and गुग्गुलुकृष्णगन्धे are dual pairs; पीलूनि is a neuter plural; सुमनःप्रवालाः = sumanas + shoots."),
        fill(2, "In सुमनःप्रवालाः the word meaning 'shoots' is ____ (type the stem or the printed word in Devanagari).",
             ["प्रवालाः", "प्रवाल", "प्रवालः"],
             "The compound is सुमनस् + प्रवालाः, 'sumanas shoots'.",
             "The last member प्रवालाः is plural; it names the part used, as त्वक् does in verse 3.",
             "X-प्रवालाः = shoots of X."),
        mcq("discriminate", 3, "Why is the first word printed ग्रन्थिश्च?",
            ("ग्रन्थिः + च: a visarga before च becomes श्", "The visarga of ग्रन्थिः turns to श् before च."),
            [("ग्रन्थि + श्च: the word श्च means 'and'", "The word for 'and' is च; श्च is not a word."),
             ("ग्रन्थि + शच: शच is a drug", "शच is not a word in this verse."),
             ("ग्रन्थिस् + च: the visarga turns to स्", "Before च the visarga becomes श्, not स्.")],
            "ग्रन्थिः + च → ग्रन्थिश्च; the same rule gives धवः + च → धवश्च in verse 3.",
            "Visarga + च → श् + च."),
        multi("apply", 4, "Which of these appear in verse 4 itself?",
              [("वत्सकसप्तपर्णौ", "Right: it is in the second line."),
               ("कुष्ठम्", "Right: कुष्ठं is in the second line."),
               ("लशुनः", "Right: लशुनः is in the first line."),
               ("करवीरकत्वक्", "Not in verse 4; it is the last item of verse 3 (also in verse 10)."),
               ("मनःशिलाले", "Not in verse 4; it is in verse 5 (also in verse 10).")],
              [0, 1, 2],
              "The first three are in verse 4; the last two belong to verses 3 and 5.",
              "Know which list each name belongs to: verse 3, 4 or 5."),
        mcq("transfer", 5,
            "A made-up compound पुत्रशिष्यौ joins पुत्र (son) and शिष्य (pupil). By the pattern of वत्सकसप्तपर्णौ, what does it name?",
            ("A son and a pupil, a pair", "The ending -औ marks two members, as in वत्सक and सप्तपर्ण."),
            [("A single person who is both son and pupil", "A dual pair names two members, not one person."),
             ("Many sons and pupils", "The plural would end in -आः."),
             ("A son of a pupil", "-औ marks two, so a singular 'a son of a pupil' does not fit.")],
            "In a pair of masculine -अ words, the dual ends in -औ: पुत्र + शिष्य → पुत्रशिष्यौ.",
            "Dvandva of two masculine -अ stems, nominative dual: -औ.",
            teaches="Reading -औ at the end of a joined pair as 'the two, A and B' gives the list sense."),
    ],
}

NOTES_HI["4"] = ("संधियाँ जाँची: ग्रन्थिः + च → ग्रन्थिश्च (विसर्ग + च → श्); भौर्जः + लशुनः → भौर्जो लशुनः, सलोमशः + गुग्गुलु… → सलोमशो गुग्गुलु…, "
                 "फणिज्झकः + वत्सक… → फणिज्झको वत्सक… (अः + घोष → ओ); सुमनः + प्रवालाः में विसर्ग प से पहले बना रहता है। "
                 "डेटा के अनुसार संदिग्ध: ‘सलोमशः’ को स + लोमश पढ़ा गया है, पर वह ‘रोमवाला’ विशेषण भी हो सकता है; ‘गुग्गुलुकृष्णगन्धे’ को द्विवचन द्वन्द्व पढ़ा गया है, "
                 "लिंग (नपुंसक या स्त्री) अनिश्चित। ‘पीलूनि’ नपुंसक बहुवचन है। कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["4"] = {
    "frame": "क्या: औषधों की सूची जारी (श्लोक ३ से) · कोई क्रिया नहीं · पूर्ति श्लोक ६ · दो द्विवचन जोड़े: गुग्गुलु-कृष्णगन्धे, वत्सक-सप्तपर्णौ।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["ग्रन्थिश्च", "भौर्जो", "लशुनः", "शिरीषः", "सलोमशो", "गुग्गुलुकृष्णगन्धे"]},
        {"label": "दूसरी पंक्ति",
         "items": ["फणिज्झको", "वत्सकसप्तपर्णौ", "पीलूनि", "कुष्ठं", "सुमनःप्रवालाः"]}]},
    "sandhi": "विसर्ग + च → श्च: ग्रन्थिः + च → ग्रन्थिश्च। अः + घोष → ओ: भौर्जः + लशुनः → भौर्जो लशुनः; फणिज्झकः + वत्सक… → फणिज्झको वत्सक…। सुमनः + प्रवालाः: विसर्ग बना रहता है।",
    "contrast": "वत्सक (एक) ↔ वत्सकसप्तपर्णौ (वत्सक और सप्तपर्ण, दो): अन्त का -औ द्विवचन।",
    "anchors": "वत्सकसप्तपर्णौ, गुग्गुलुकृष्णगन्धे में अन्त का -औ / -ए द्विवचन है (इन दोनों शब्दों में) · पीलूनि = नपुंसक बहुवचन · सुमनःप्रवालाः = सुमनस् + कोंपलें।",
    "chunks": "ग्रन्थिश्च भौर्जो लशुनः | शिरीषः सलोमशो गुग्गुलुकृष्णगन्धे ‖ फणिज्झको वत्सकसप्तपर्णौ | पीलूनि कुष्ठं सुमनःप्रवालाः।",
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "वचा हरेणुस्त्रिवृता निकुम्भः",
    "question": "How does verse 5 close the drug list begun in verse 3, and how is its long final compound built?",
    "rule": ("Verse 5 finishes the three drug verses (3 to 5) with no verb. "
             "Its last word काशीसलोध्रार्जुनमुस्तसर्जाः is a long compound "
             "of drug names, and गृहधूम is literally 'house-smoke'."),
    "limits": ("Names only: no use, no dose. The data understands गृहधूम as "
               "soot and reads मनःशिलाले as a dual pair (manaḥśilā and āla), "
               "but marks both as readings; it also says काशीस is one word, "
               "not काशी + स. No question here rests on those readings."),
    "explain_hi": ("यह श्लोक ३ और ४ की सूची को आगे बढ़ाकर पूरा करता है; अब भी कोई क्रिया नहीं है, क्रिया श्लोक ६ में है। "
                   "नाम हैं: वचा, हरेणु, त्रिवृता, निकुम्भ, भल्लातक, गैरिक, अञ्जन, मनःशिला और आल, गृहधूम, एला, "
                   "और अन्त में एक लम्बा समास ‘काशीसलोध्रार्जुनमुस्तसर्जाः’ (काशीस, लोध्र, अर्जुन, मुस्त, सर्ज)। "
                   "‘गृहधूम’ का शाब्दिक अर्थ ‘घर का धुआँ’ है; डेटा इसे कालिख के अर्थ में लेता है। "
                   "‘हरेणुस्त्रिवृता’ में विसर्ग त से पहले स् बन जाता है।"),
    "hook": "श्लोक ५: सूची का तीसरा श्लोक, सूची पूरी; लम्बा समास = पाँच नाम; हरेणुः + त्रिवृता → हरेणुस्त्रिवृता।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 5 contain?",
            ("The last drug names of the three-verse list; no verb",
             "Verse 5 only lists names; the verb comes in verse 6."),
            [("The diseases that the drugs remove", "Diseases are named in verse 7."),
             ("The soaking in cow's bile and the mustard oil", "That is verse 6."),
             ("A statement of equal powders", "Equal powders are in verse 8.")],
            "The verse runs from वचा to सर्जाः as a plain list.",
            "Verse 5: the list of verses 3 to 5 ends; no verb."),
        order(1, "Put these words of the second line of verse 5 in verse order.",
              ["मनःशिलाले", "गृहधूम", "एला", "काशीसलोध्रार्जुनमुस्तसर्जाः"],
              "The second line begins with मनःशिलाले and ends with the long compound.",
              "Second line: मनःशिलाले, गृहधूम, एला, then the final compound."),
        fill(2, "In गृहधूम the part meaning 'house' is ____ (type it in Devanagari).",
             ["गृह", "गृहः", "गृहं", "गृहम्"],
             "गृहधूम = गृह (house) + धूम (smoke).",
             "गृहधूम is a compound whose first part is 'house' and last part is 'smoke'.",
             "गृह + धूम = house-smoke."),
        mcq("discriminate", 3, "Which is the right split of हरेणुस्त्रिवृता?",
            ("हरेणुः + त्रिवृता", "A visarga before त is written as स्, so हरेणुः + त्रिवृता → हरेणुस्त्रिवृता."),
            [("हरेणु + स्त्रिवृता", "स्त्रिवृता is not a word."),
             ("हरेणुस् + रिवृता", "रिवृता is not a word."),
             ("हरेणुः + स्त्रिवृता", "The second word is त्रिवृता; the स् comes from the visarga.")],
            "हरेणुः + त्रिवृता → हरेणुस्त्रिवृता.",
            "Visarga + त → स् + त."),
        multi("apply", 4, "Which of these names are in verse 5 itself?",
              [("वचा", "Right: it opens the verse."),
               ("भल्लातकम्", "Right: it is in the first line."),
               ("मुस्त", "Right: it is inside the final compound."),
               ("निम्बः", "That is in verse 3."),
               ("लशुनः", "That is in verse 4.")],
              [0, 1, 2],
              "The first three are in verse 5; निम्बः and लशुनः belong to verses 3 and 4.",
              "Know which list each name belongs to: verse 3, 4 or 5."),
        mcq("transfer", 5,
            "A made-up compound is मूलफलपत्राणि (मूल root, फल fruit, पत्र leaf). Read like the final compound of verse 5, what is it?",
            ("A list: root, fruit and leaf, in the neuter plural", "Only the last member carries the ending, as with सर्जाः."),
            [("The leaf of the fruit of the root", "That would be a chain of 'of'-links, not a list."),
             ("One single thing named मूलफलपत्र", "The three parts are separate items, as in verse 5's compound."),
             ("A root that bears fruit and leaf", "The compound lists three parts; it does not describe a root.")],
            "In a long list compound, the parts are joined without endings and the last one takes the ending.",
            "Dvandva: A + B + C, with the ending only on the last member.",
            teaches="A long unbroken string of names with one ending at the end can be read as a list 'A, B and C'."),
    ],
}

NOTES_HI["5"] = ("संधियाँ जाँची: हरेणुः + त्रिवृता → हरेणुस्त्रिवृता (विसर्ग + त → स्); निकुम्भः + भल्लातकम् → निकुम्भो भल्लातकम् (अः + घोष → ओ); "
                 "गैरिकम् + अञ्जनम् → गैरिकमञ्जनम् (म् अगले स्वर से सटा); गृहधूमः + एला → गृहधूम एला (अः + भिन्न स्वर: विसर्ग लुप्त); "
                 "लोध्र + अर्जुन → लोध्रार्जुन (अ + अ → आ)। डेटा की टिप्पणी: ‘मनःशिलाले’ को द्विवचन द्वन्द्व (मनःशिला और आल) पढ़ा गया है, "
                 "‘गृहधूम’ = घर का धुआँ (कालिख के अर्थ में), ‘काशीस’ एक ही शब्द है (काशी + स नहीं)। कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["5"] = {
    "frame": "क्या: औषधों की सूची का अन्त (श्लोक ३–५) · कोई क्रिया नहीं · पूर्ति श्लोक ६ · अन्त में लम्बा समास।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["वचा", "हरेणुस्त्रिवृता", "निकुम्भो", "भल्लातकं", "गैरिकमञ्जनं", "च"]},
        {"label": "दूसरी पंक्ति",
         "items": ["मनःशिलाले", "गृहधूम", "एला", "काशीसलोध्रार्जुनमुस्तसर्जाः"]}]},
    "sandhi": "विसर्ग + त → स्त: हरेणुः + त्रिवृता → हरेणुस्त्रिवृता। अः + घोष → ओ: निकुम्भः + भल्लातकम् → निकुम्भो भल्लातकम्। अ + अ → आ: लोध्र + अर्जुन → लोध्रार्जुन।",
    "anchors": "गृहधूम = गृह (घर) + धूम (धुआँ) · काशीसलोध्रार्जुनमुस्तसर्जाः = काशीस, लोध्र, अर्जुन, मुस्त, सर्ज: अन्तिम पद पर ही विभक्ति (-आः)।",
    "chunks": "वचा हरेणुस्त्रिवृता निकुम्भो | भल्लातकं गैरिकमञ्जनं च ‖ मनःशिलाले गृहधूम एला | काशीसलोध्रार्जुनमुस्तसर्जाः।",
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "इत्यर्धरूपैर्विहिताः षडेते",
    "question": "How does verse 6 finish the sentence begun in verse 3, and how are the six groups to be prepared?",
    "rule": ("Verse 6 closes the list of verses 3 to 5: these six groups "
             "(six half-verse forms) are soaked in cow's bile, ground again, "
             "prepared, combined with mustard oil, and applied by the "
             "physician as powder-pastes (cūrṇa-pradeha)."),
    "limits": ("The verse gives no soaking time, no amounts and no method of "
               "preparing. सिद्ध (prepared, cooked, finished) is ambiguous, "
               "and परम् may mean 'afterwards' (as read) or 'excellent'. "
               "The six are the six printed lines of verses 3 to 5, per the "
               "data's note."),
    "explain_hi": ("यह श्लोक ३ से शुरू हुई सूची का वाक्य पूरा करता है: ‘इत्यर्धरूपैर्विहिताः षडेते’, यानी आधे-आधे श्लोक के रूप में बताए गए ये छह "
                   "समूह (श्लोक ३ से ५ की छह पंक्तियाँ)। इन्हें गोपित्त में भिगोया जाए (गोपित्तपीताः), फिर पीसा जाए (पुनरेव पिष्टाः), "
                   "तैयार किया जाए (सिद्धाः), फिर सरसों के तेल से मिलाया जाए (सर्षपतैलयुक्ताः), और वैद्य द्वारा "
                   "‘चूर्ण-प्रदेह’ के रूप में प्रयोग किया जाए। ‘प्रदेह’ का अर्थ यहाँ लेप है, जो चूर्ण से बना है। मात्रा, समय या विधि श्लोक में नहीं दी गई।"),
    "hook": "छह समूह: गोपित्त में भिगोना → फिर पीसना → सिद्ध → सरसों का तेल → वैद्य द्वारा चूर्ण-प्रदेह।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In verse 6, what is said to be done to the six drug groups first?",
            ("They are soaked in cow's bile (गोपित्तपीताः)", "गोपित्तपीताः comes first among the processes the verse names."),
            [("They are given a fixed dose", "No dose is given in this verse."),
             ("They are burned to ash", "Nothing in the verse speaks of burning."),
             ("They are mixed with buttermilk", "Buttermilk (तक्र) appears in verse 9, not here.")],
            "The verse lists the processes in this order: soaked in cow's bile, ground again, prepared, combined with mustard oil.",
            "Verse 6: soaked in cow's bile → ground again → prepared → mustard oil."),
        match(1, "Match each word or phrase of verse 6 to its meaning.",
              [["गोपित्तपीताः", "soaked in cow's bile"],
               ["पिष्टाः", "ground"],
               ["सर्षपतैलयुक्ताः", "combined with mustard oil"],
               ["भिषजा", "by the physician"]],
              "These four pieces carry the preparation and the one who applies.",
              "गोपित्तपीताः = soaked in cow's bile; पिष्टाः = ground; सर्षपतैलयुक्ताः = combined with mustard oil; भिषजा = by the physician."),
        fill(2, "The word for 'powder-pastes' in verse 6 is चूर्ण + ____ (type the second part in Devanagari).",
             ["प्रदेह", "प्रदेहाः", "प्रदेहा"],
             "The compound is चूर्णप्रदेहाः = चूर्ण (powder) + प्रदेह (paste).",
             "चूर्णप्रदेहाः are pastes (pradeha) made from powder (cūrṇa).",
             "चूर्ण + प्रदेह = powder-paste."),
        mcq("discriminate", 3, "Which is the right split of इत्यर्धरूपैः?",
            ("इति + अर्धरूपैः", "इ before an unlike vowel becomes य्: इति + अर्ध… → इत्यर्ध…."),
            [("इत्य + र्धरूपैः", "र्धरूपैः is not a word."),
             ("इति + र्धरूपैः", "र्धरूपैः is not a word."),
             ("इत + यर्धरूपैः", "यर्धरूपैः is not a word.")],
            "इत्यर्धरूपैः is इति ('thus') + अर्धरूपैः ('by half-verse forms').",
            "इ + असमान स्वर → य् + स्वर: इति + अर्ध… → इत्यर्ध…."),
        order(4, "Put these steps of verse 6 in the order the verse states them.",
              ["soaked in cow's bile", "ground again", "prepared", "combined with mustard oil", "applied by the physician"],
              "The verse names the processes in this order; the last is the physician's application.",
              "गोपित्तपीताः → पुनरेव पिष्टाः → सिद्धाः → सर्षपतैलयुक्ताः → भिषजा प्रयोज्याः.",
              role="apply"),
        mcq("transfer", 5,
            "A made-up line reads तिलतैलयुक्तानि चूर्णानि प्रयोज्यानि (तिल sesame, तैल oil). What does it say?",
            ("Powders combined with sesame oil are to be applied", "-युक्ताः means 'combined with' and प्रयोज्याः 'to be applied', as in verse 6."),
            [("Powders free of sesame oil are to be applied", "-युक्ताः means 'combined with', not 'free of'."),
             ("Sesame oil is to be ground from powders", "The line combines powders with oil; it does not make oil from powders."),
             ("Powders must not be applied with sesame oil", "प्रयोज्याः is a gerundive 'to be applied', not a prohibition.")],
            "The frame is X-तैलयुक्तानि चूर्णानि प्रयोज्यानि: 'powders combined with X-oil are to be applied'. This is a grammar drill, not a medical statement.",
            "X-तैलयुक्तानि + प्रयोज्यानि = combined with X-oil, to be applied.",
            teaches="Once the frame is clear, you can read 'combined with … oil, to be applied' in any similar line."),
    ],
}

NOTES_HI["6"] = ("संधियाँ जाँची: इति + अर्धरूपैः → इत्यर्धरूपैः (इ + अ → य); अर्धरूपैः + विहिताः → अर्धरूपैर्विहिताः (ऐः + घोष → ऐर्); "
                 "षट् + एते → षडेते (ट् → ड् स्वर से पहले); पुनः + एव → पुनरेव (उः + स्वर → र्); युक्ताः + चूर्ण… → युक्ताश्चूर्ण… (विसर्ग + च → श्); "
                 "चूर्णप्रदेहाः + भिषजा → चूर्णप्रदेहा भिषजा (आः के बाद विसर्ग लुप्त)। डेटा की टिप्पणी: ‘सिद्ध’ द्विधा है (पका, तैयार, पूर्ण); "
                 "‘परम्’ का अर्थ ‘उसके बाद’ लिया गया है, ‘उत्तम’ भी सम्भव। ‘पीत’ का शाब्दिक अर्थ ‘पिया हुआ’, यानी भिगोया हुआ। "
                 "मात्रा, भिगोने का समय या विधि श्लोक में नहीं है। कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["6"] = {
    "frame": "कौन: ये छह समूह (श्लोक ३–५) · कैसे: गोपित्त में भिगोए, फिर पीसे, सिद्ध, सरसों के तेल से युक्त · किस रूप में: चूर्ण-प्रदेह · किससे: वैद्य द्वारा।",
    "chain": {"steps": ["गोपित्त में भिगोना (गोपित्तपीताः)", "फिर पीसना (पुनरेव पिष्टाः)", "सिद्ध करना (सिद्धाः)",
                        "सरसों का तेल (सर्षपतैलयुक्ताः)", "वैद्य द्वारा प्रयोग (भिषजा प्रयोज्याः)"]},
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["इत्यर्धरूपैर्विहिताः", "षडेते", "गोपित्तपीताः", "पुनरेव", "पिष्टाः"]},
        {"label": "दूसरी पंक्ति",
         "items": ["सिद्धाः", "परं", "सर्षपतैलयुक्ताश्चूर्णप्रदेहा", "भिषजा", "प्रयोज्याः"]}]},
    "sandhi": "इ + अ → य: इति + अर्ध… → इत्यर्ध…। ऐः + घोष → ऐर्: अर्धरूपैः + विहिताः → अर्धरूपैर्विहिताः। ट् → ड्: षट् + एते → षडेते। उः + स्वर → र्: पुनः + एव → पुनरेव।",
    "anchors": "गोपित्तपीताः = गोपित्त में भीगे · पिष्टाः = पिसे · -युक्ताः = से युक्त · भिषजा = वैद्य द्वारा (तृतीया) · प्रयोज्याः = प्रयोग किए जाने योग्य (कृत्य प्रत्यय)।",
    "chunks": "इत्यर्धरूपैर्विहिताः षडेते | गोपित्तपीताः पुनरेव पिष्टाः ‖ सिद्धाः परं | सर्षपतैलयुक्ताश्चूर्णप्रदेहा भिषजा प्रयोज्याः।",
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "कुष्ठानि कृच्छ्राणि नवं किलासम्",
    "question": "Which troubles does verse 7 say the applied pastes would destroy, and how quickly?",
    "rule": ("The six powder-pastes, applied, 'would quickly destroy' (हन्युः, "
             "optative) in people: difficult kuṣṭhas, recent kilāsa, "
             "sureśalupta, kiṭibha with dadru, bhagandara, arśas, and apacī "
             "with pāmā."),
    "limits": ("The disease names are kept in Sanskrit and the glosses are "
               "conventional, not stated in the verse. The subject (the six "
               "pastes) is carried over from verse 6. नवम् is singular and "
               "taken with kilāsa; कृच्छ्राणि is plural and goes with "
               "कुष्ठानि. The verse says 'would destroy', not a guarantee."),
    "explain_hi": ("यह श्लोक श्लोक ६ के वाक्य को आगे बढ़ाता है; कर्ता वही छह चूर्ण-प्रदेह हैं। प्रयोग किए जाने पर वे मनुष्यों के इन विकारों को "
                   "शीघ्र नष्ट कर सकते हैं (‘हन्युः’, विधिलिङ्): कठिन कुष्ठ, नया किलास, सुरेशलुप्त, दद्रु-सहित किटिभ, भगन्दर, अर्श, "
                   "और पामा-सहित अपची। ‘नवम्’ एकवचन है, इसलिए वह ‘किलासम्’ के साथ जाता है, और ‘कृच्छ्राणि’ बहुवचन है, इसलिए ‘कुष्ठानि’ के साथ। "
                   "‘सदद्रु’, ‘सपामाम्’ में ‘स-’ का अर्थ ‘के साथ’ है। रोगों की पहचान परम्परागत है, श्लोक में नहीं बताई गई।"),
    "hook": "श्लोक ७: प्रयोग किए जाने पर शीघ्र नष्ट (हन्युः) · स- = साथ (सदद्रु, सपामाम्)।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does verse 7 say the applied pastes would do?",
            ("Quickly destroy the named troubles in people", "हन्युः means 'they would destroy' and अचिरात् 'quickly'."),
            [("Give no result for a long time", "The verse says अचिरात्, 'quickly'."),
             ("Cause the troubles they name", "The verb is हन्युः, 'would destroy'."),
             ("Give the dose for each trouble", "No dose is given in this verse.")],
            "The verse names the troubles as objects of हन्युः and says अचिरात् for the speed.",
            "Verse 7: applied, they would quickly destroy the named troubles."),
        match(1, "Match each word of verse 7 to its meaning.",
              [["कृच्छ्राणि", "difficult (with कुष्ठानि)"],
               ["अचिरात्", "quickly"],
               ["हन्युः", "they would destroy"],
               ["सपामाम्", "together with pāmā"]],
              "These four words carry the force of the verse.",
              "कृच्छ्राणि = difficult; अचिरात् = quickly; हन्युः = they would destroy; सपामाम् = together with pāmā."),
        fill(2, "The word in verse 7 for 'quickly' is ____ (type the form with त् or the printed form in Devanagari).",
             ["अचिरात्", "अचिरान्"],
             "The word is अचिरात्; in the printed text it appears as अचिरान् before नराणाम्.",
             "अचिरात् is an ablative used as an adverb: 'quickly'. Before the न of नराणाम् its त् becomes न्.",
             "अचिरात् + नराणाम् → अचिरान्नराणाम्."),
        mcq("discriminate", 3, "Which is the right split of अचिरान्नराणाम्?",
            ("अचिरात् + नराणाम्", "त् + न → न्न, so अचिरात् + नराणाम् is written अचिरान्नराणाम्."),
            [("अचिर + अन्नराणाम्", "अन्नराणाम् is not a word."),
             ("अचिरा + नराणाम्", "That would leave a single न; the printed form has न्न."),
             ("अचिरान् + राणाम्", "राणाम् is not a word.")],
            "अचिरात् ('quickly') + नराणाम् ('of men') → अचिरान्नराणाम्.",
            "त् before न becomes न्: अचिरात् + न… → अचिरान्न…."),
        multi("apply", 4, "Which of these are said by verse 7?",
              [("The pastes would quickly destroy the troubles in people", "Right: हन्युः … अचिरात् … नराणाम्."),
               ("Kuṣṭhas are listed, and they are called difficult", "Right: कुष्ठानि कृच्छ्राणि."),
               ("Kiṭibha is listed together with dadru", "Right: किटिभं सदद्रु."),
               ("The pastes are soaked in cow's bile", "That is verse 6."),
               ("The pastes are fixed at one dose", "No dose appears in the verse.")],
              [0, 1, 2],
              "The first three follow from verse 7; the soaking is in verse 6 and no dose is given anywhere here.",
              "Verse 7: the troubles and the speed; the preparation is in verse 6."),
        mcq("transfer", 5,
            "A made-up line reads सकण्डूं पिडकां हन्युः (कण्डू itching, पिडका boil). By the pattern of सपामाम्, what would they destroy?",
            ("A boil together with itching", "सकण्डूम् means 'together with itching', as सपामाम् means 'together with pāmā'."),
            [("A boil in place of itching", "स- means 'together with', not 'in place of'."),
             ("Itching without any boil", "The line destroys the boil; the itching is joined to it."),
             ("A boil that comes after itching", "The prefix स- gives 'together with', not an order in time.")],
            "स- before a noun gives 'together with'. This is a grammar drill, not a medical statement.",
            "स-X = together with X (सदद्रु, सपामाम्).",
            teaches="The prefix स- turns a name into 'together with that name' in lists of troubles."),
    ],
}

NOTES_HI["7"] = ("संधियाँ जाँची: भगन्दर + अर्शांसि → भगन्दरार्शांसि (अ + अ → आ); अर्शांसि + अपचीम् → अर्शांस्यपचीम् (इ + अ → य); "
                 "प्रयुक्ताः + तु → प्रयुक्तास्तु (विसर्ग + त → स्); तु + अचिरात् → त्वचिरात् (उ + अ → व); अचिरात् + नराणाम् → अचिरान्नराणाम् (त् + न → न्न)। "
                 "‘हन्युः’ विधिलिङ् (3 बहुवचन) है, इसलिए ‘नष्ट कर सकते हैं’ अर्थ लिया गया है, पक्का वादा नहीं। "
                 "डेटा की टिप्पणी: ‘नवम्’ एकवचन है और किलास के साथ जाता है; ‘कृच्छ्राणि’ बहुवचन है और कुष्ठानि के साथ; ‘सुरेशलुप्त’ = इन्द्रलुप्त (सुर-ईश = इन्द्र)। "
                 "रोगों के अर्थ परम्परागत हैं, श्लोक में नहीं बताए गए। कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["7"] = {
    "frame": "कर्ता: छह चूर्ण-प्रदेह (श्लोक ६ से) · क्रिया: हन्युः (नष्ट कर सकें) · कैसे: प्रयुक्त होने पर, शीघ्र · किसके रोग: मनुष्यों के · कौन-से: कुष्ठ, किलास, सुरेशलुप्त, किटिभ, दद्रु, भगन्दर, अर्श, अपची, पामा।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["कुष्ठानि", "कृच्छ्राणि", "नवं", "किलासं", "सुरेशलुप्तं", "किटिभं", "सदद्रु"]},
        {"label": "दूसरी पंक्ति",
         "items": ["भगन्दरार्शांस्यपचीं", "सपामां", "हन्युः", "प्रयुक्तास्त्वचिरान्नराणाम्"]}]},
    "sandhi": "त् + न → न्न: अचिरात् + नराणाम् → अचिरान्नराणाम्। विसर्ग + त → स्त: प्रयुक्ताः + तु → प्रयुक्तास्तु। उ + अ → व: तु + अचिरात् → त्वचिरात्। इ + अ → य: अर्शांसि + अपचीम् → अर्शांस्यपचीम्।",
    "anchors": "स- = साथ (सदद्रु, सपामाम्) · कृच्छ्राणि (बहुवचन) ↔ कुष्ठानि · नवम् (एकवचन) ↔ किलासम् · हन्युः = हन् का विधिलिङ् ‘नष्ट कर सकें/करें’ · अचिरात् = शीघ्र।",
    "chunks": "कुष्ठानि कृच्छ्राणि नवं किलासं | सुरेशलुप्तं किटिभं सदद्रु ‖ भगन्दरार्शांस्यपचीं सपामां | हन्युः प्रयुक्तास्त्वचिरान्नराणाम्।",
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "कुष्ठं हरिद्रे सुरसं पटोलम्",
    "question": "What does verse 8 instruct, and what is said about the amounts?",
    "rule": ("Verse 8 begins a second formulation: one should make equal "
             "powders (चूर्णानि समानि कुर्यात्) of the drugs listed. It says "
             "'equal' only; it gives no quantity."),
    "limits": ("The verse names the drugs and says the powders are equal; "
               "it gives no weight and no further method. तुम्बुरुधान्यवन्यम् "
               "is read as a three-member list, but वन्य ('wild') might "
               "instead qualify dhānya; the data marks this as needing a "
               "commentary. Grinding with buttermilk and rubbing come in "
               "verse 9."),
    "explain_hi": ("यहाँ दूसरा योग शुरू होता है। पहली पंक्ति और दूसरी पंक्ति में औषधों के नाम हैं और अन्त में क्रिया है ‘कुर्यात्’: "
                   "‘चूर्णानि समानि कुर्यात्’, यानी इनके समान चूर्ण बनाने चाहिए। ‘समानि’ का अर्थ ‘बराबर’ है, पर बराबर कितना, यह श्लोक "
                   "नहीं बताता। नामों में तीन द्विवचन जोड़े हैं: ‘हरिद्रे’, ‘निम्बाश्वगन्धे’ (निम्ब और अश्वगन्धा) और ‘सुरदारुशिग्रू’ (सुरदारु और शिग्रु)। "
                   "‘ससर्षपम्’ का अर्थ ‘सरसों के साथ’ है। मट्ठे में पीसने और उद्वर्तन का वर्णन अगले श्लोक ९ में है।"),
    "hook": "दूसरा योग: औषध-नाम + ‘चूर्णानि समानि कुर्यात्’ (बराबर चूर्ण बनाओ); मात्रा नहीं दी गई।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 8 tell one to do with the drugs it lists?",
            ("Make equal powders of them (चूर्णानि समानि कुर्यात्)", "The verb कुर्यात् means 'one should make' and समानि 'equal'."),
            [("Burn them to ash", "Nothing in the verse speaks of burning."),
             ("Soak them in cow's bile", "The soaking is in verse 6, a different formulation."),
             ("Boil them in oil", "The verse names no boiling and no oil.")],
            "The last words of the second line state the instruction: equal powders are to be made.",
            "Verse 8: make equal powders of the listed drugs."),
        match(1, "Match each form in verse 8 to its meaning.",
              [["हरिद्रे", "the two haridrās"],
               ["निम्बाश्वगन्धे", "nimba and aśvagandhā (a pair)"],
               ["चूर्णानि", "powders"],
               ["समानि", "equal"]],
              "Two of these are dual pairs; the other two are the neuter plurals of the instruction.",
              "हरिद्रे and निम्बाश्वगन्धे are dual; चूर्णानि = powders; समानि = equal."),
        fill(2, "The verb meaning 'one should make' in verse 8 is ____ (type it in Devanagari).",
             ["कुर्यात्"],
             "The verb is कुर्यात्, third person singular optative of √कृ.",
             "कुर्यात् is an optative: 'one should make'. It is the verb that governs चूर्णानि समानि.",
             "कुर्यात् = one should make."),
        mcq("discriminate", 3, "Which is the right split of निम्बाश्वगन्धे?",
            ("निम्ब + अश्वगन्धे", "अ + अ gives आ, so निम्ब + अश्वगन्धे is written निम्बाश्वगन्धे."),
            [("निम्बा + श्वगन्धे", "श्वगन्धे is not a word."),
             ("निम्बः + अश्वगन्धे", "निम्बः + अश्वगन्धे would give निम्बोऽश्वगन्धे, not निम्बाश्वगन्धे."),
             ("निम्ब + आश्वगन्धे", "The second word is अश्वगन्धे with short अ.")],
            "निम्बाश्वगन्धे is a joined pair, निम्ब and अश्वगन्धे.",
            "अ + अ → आ: निम्ब + अश्वगन्धे → निम्बाश्वगन्धे."),
        multi("apply", 4, "Which of these does verse 8 say?",
              [("The powders are to be made equal", "Right: चूर्णानि समानि."),
               ("The instruction is in the optative: 'one should make'", "Right: कुर्यात्."),
               ("Mustard is named together with the other drugs", "Right: ससर्षपम् means 'together with mustard'."),
               ("The weight of each drug is given", "The verse says only 'equal', with no weight."),
               ("The powders are ground with buttermilk", "Buttermilk is in verse 9.")],
              [0, 1, 2],
              "The first three are in verse 8; the weight is nowhere given, and the buttermilk comes next.",
              "Verse 8: equal powders; no weight; the buttermilk is in verse 9."),
        mcq("transfer", 5,
            "A made-up line reads चूर्णानि सूक्ष्माणि कुर्यात् (सूक्ष्म = fine). What does it say?",
            ("One should make the powders fine", "सूक्ष्माणि agrees with चूर्णानि like समानि, and कुर्यात् is 'one should make'."),
            [("One should not make the powders fine", "कुर्यात् says 'one should make', not a prohibition."),
             ("One should make fine ones out of the powders", "सूक्ष्माणि describes the powders; it is not a new product."),
             ("The powders have made it fine", "कुर्यात् is the optative 'one should make', not a statement of a past result.")],
            "The frame is चूर्णानि X कुर्यात्: the adjective X agrees with चूर्णानि and the verb says 'one should make'. This is a grammar drill, not a medical statement.",
            "चूर्णानि + adjective + कुर्यात् = one should make the powders X.",
            teaches="An adjective that agrees with चूर्णानि (neuter plural) says what the powders should be like."),
    ],
}

NOTES_HI["8"] = ("संधियाँ जाँची: निम्ब + अश्वगन्धे → निम्बाश्वगन्धे (अ + अ → आ); ‘सुरदारुशिग्रू’ में सुरदारु और शिग्रु दो नाम जुड़े हैं, अन्तिम पद पर द्विवचन -ऊ; "
                 "चण्डाम् + च → चण्डां च (अनुस्वार वाला छपा रूप)। डेटा की टिप्पणी: ‘तुम्बुरुधान्यवन्यम्’ को तीन पदों का द्वन्द्व पढ़ा गया है, "
                 "पर ‘वन्य’ (जंगली) ‘धान्य’ का विशेषण भी हो सकता है; ‘समानि’ (बराबर) की मात्रा नहीं दी गई; ‘सुरदारु’ शाब्दिक रूप से ‘देव-काष्ठ’ है। "
                 "डेटा के अनुसार यहाँ से दूसरा योग शुरू होता है। कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["8"] = {
    "frame": "क्या: दूसरा योग · औषध-नाम (तीन द्विवचन जोड़े) · क्रिया: कुर्यात् (बनाओ) · क्या बनाओ: समान चूर्ण · मात्रा: नहीं दी गई।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["कुष्ठं", "हरिद्रे", "सुरसं", "पटोलं", "निम्बाश्वगन्धे", "सुरदारुशिग्रू"]},
        {"label": "दूसरी पंक्ति",
         "items": ["ससर्षपं", "तुम्बुरुधान्यवन्यं", "चण्डां", "च", "चूर्णानि", "समानि", "कुर्यात्"]}]},
    "sandhi": "अ + अ → आ: निम्ब + अश्वगन्धे → निम्बाश्वगन्धे। द्विवचन ‘-े’ और ‘-ू’: हरिद्रे, निम्बाश्वगन्धे, सुरदारुशिग्रू (हर जोड़ा दो नाम)।",
    "contrast": "समानि (बराबर) ↔ मात्रा: श्लोक में बराबर कहा है, पर कितनी मात्रा, नहीं बताई।",
    "anchors": "ससर्षपम् = स- (साथ) + सरसों · समानि चूर्णानि = बराबर चूर्ण (नपुंसक बहुवचन, एक-दूसरे के बराबर) · कुर्यात् = ‘करना चाहिए’ (विधिलिङ्)।",
    "chunks": "कुष्ठं हरिद्रे सुरसं पटोलं | निम्बाश्वगन्धे सुरदारुशिग्रू ‖ ससर्षपं तुम्बुरुधान्यवन्यं | चण्डां च चूर्णानि समानि कुर्यात्।",
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "तैस्तक्रपिष्टैः प्रथमं शरीरम्",
    "question": "What does verse 9 say to do with the powders of verse 8, and what are said to subside?",
    "rule": ("With those powders (of verse 8) ground with buttermilk, one "
             "should first strive to rub (उद्वर्तन) the oil-smeared body; "
             "by that, the person's itching, boils with koṭha, kuṣṭhas and "
             "swellings go to rest."),
    "limits": ("तैः points back to the powders of verse 8 at least. The verse "
               "gives no amount, no rubbing time and no further method. "
               "कोठ is kept as a name for a rash of raised wheals. कण्डूः is "
               "singular with a plural verb because the subject is a list."),
    "explain_hi": ("यह श्लोक श्लोक ८ के चूर्णों के प्रयोग की विधि बताता है। पहले तेल से लिप्त (तेल लगे) शरीर को (तैलाक्तम्), "
                   "मट्ठे (तक्र) में पीसे हुए उन चूर्णों से उद्वर्तन, यानी रगड़ने, का प्रयत्न किया जाए (‘यतेत’, विधिलिङ्)। "
                   "उससे इस (रोगी) की खुजली, कोठ-सहित फुंसियाँ, कुष्ठ और सूजन शान्त हो जाते हैं (‘शमं व्रजन्ति’)। "
                   "‘तैः’ पीछे के चूर्णों की ओर संकेत करता है। ‘कण्डूः’ एकवचन है पर क्रिया बहुवचन, क्योंकि कर्ता एक सूची है।"),
    "hook": "तैल लगा शरीर → मट्ठे में पिसे चूर्णों से उद्वर्तन → खुजली, फुंसियाँ, कुष्ठ, सूजन शान्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In verse 9, what is the body like before the rubbing, and with what are the powders ground?",
            ("Smeared with oil; the powders are ground with buttermilk", "तैलाक्तम् is 'smeared with oil' and तक्रपिष्टैः 'ground with buttermilk'."),
            [("Dry and bare; the powders are ground with cow's bile", "Cow's bile belongs to verse 6, and the body is oil-smeared here."),
             ("Smeared with oil; the powders are ground with mustard", "The grinding is with buttermilk (तक्र)."),
             ("Washed with water; the powders are ground with milk", "Neither washing nor milk appears in the verse.")],
            "तैलाक्तं शरीरम् is the oil-smeared body, and तक्रपिष्टैः says the powders are ground with buttermilk.",
            "Verse 9: oil-smeared body; powders ground with buttermilk."),
        match(1, "Match each word of verse 9 to its meaning.",
              [["तक्रपिष्टैः", "ground with buttermilk"],
               ["तैलाक्तम्", "smeared with oil"],
               ["उद्वर्तयितुम्", "to rub or scrub"],
               ["शमम्", "calm or subsidence"]],
              "These four words carry the method and the result.",
              "तक्रपिष्टैः = ground with buttermilk; तैलाक्तम् = smeared with oil; उद्वर्तयितुम् = to rub; शमम् = calm."),
        fill(2, "In तक्रपिष्टैः the part meaning 'buttermilk' is ____ (type it in Devanagari).",
             ["तक्र", "तक्रं", "तक्रम्"],
             "तक्रपिष्टैः = तक्र (buttermilk) + पिष्टैः (ground).",
             "The compound तक्रपिष्टैः says what the powders are ground with: buttermilk.",
             "तक्र + पिष्टैः = ground with buttermilk."),
        mcq("discriminate", 3, "Which is the right split of तैस्तक्रपिष्टैः?",
            ("तैः + तक्रपिष्टैः", "A visarga before त is written as स्, so तैः + तक्र… → तैस्तक्र…."),
            [("ते + स्तक्रपिष्टैः", "स्तक्रपिष्टैः is not a word."),
             ("तै + स्तक्रपिष्टैः", "स्तक्रपिष्टैः is not a word."),
             ("तैस + तक्रपिष्टैः", "तैस is not a word; the pronoun is तैः.")],
            "तैः is 'by those' (instrumental plural), joined to तक्रपिष्टैः.",
            "Visarga + त → स् + त."),
        multi("apply", 4, "Which of these are said to subside (शमं व्रजन्ति) in verse 9?",
              [("The itching", "Right: कण्डूः."),
               ("Swellings", "Right: शोफाः."),
               ("Kuṣṭhas", "Right: कुष्ठानि."),
               ("Bhagandara", "Bhagandara is in verse 7, not in this verse."),
               ("Apacī", "Apacī is in verse 7, not in this verse.")],
              [0, 1, 2],
              "Verse 9 names the itching, boils with koṭha, kuṣṭhas and swellings.",
              "Know which list each trouble belongs to: verse 7 or verse 9."),
        mcq("transfer", 5,
            "A made-up phrase is घृताक्तं पात्रम् (घृत ghee, पात्र vessel). By the pattern of तैलाक्तम्, what is it?",
            ("A vessel smeared with ghee", "-अक्त means 'smeared with', as तैलाक्तम् (तैल + अक्तम्) is 'smeared with oil'."),
            [("A vessel filled with ghee", "अक्त means smeared, not filled."),
             ("A vessel free of ghee", "अक्त does not mean 'free of'."),
             ("Ghee made for a vessel", "The phrase describes the vessel, not what the ghee is for.")],
            "X + अक्तम् reads 'smeared with X'. This is a grammar drill, not a medical statement.",
            "घृत + अक्तम् → घृताक्तम्; X-अक्त = smeared with X (अ + अ → आ).",
            teaches="Once -अक्त is clear, you can read any 'smeared with X' phrase like तैलाक्तम्."),
    ],
}

NOTES_HI["9"] = ("संधियाँ जाँची: तैः + तक्रपिष्टैः → तैस्तक्रपिष्टैः (विसर्ग + त → स्); तैल + अक्तम् → तैलाक्तम् (अ + अ → आ); "
                 "तैलाक्तम् + उद्वर्तयितुम् → तैलाक्तमुद्वर्तयितुम् (म् अगले स्वर से सटा); तेन + अस्य → तेनास्य (अ + अ → आ); शोफाः + च → शोफाश्च (विसर्ग + च → श्)। "
                 "डेटा की टिप्पणी: ‘तैः’ पिछले चूर्णों (कम से कम श्लोक ८) की ओर संकेत करता है; ‘अस्य’ रोगी का ‘इसका’ है; ‘कोठ’ को नाम के रूप में रखा गया है; "
                 "‘कण्डूः’ एकवचन और क्रिया बहुवचन, क्योंकि कर्ता सूची है। कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["9"] = {
    "frame": "किससे: श्लोक ८ के चूर्ण, मट्ठे में पिसे · किस पर: तेल लगा शरीर · क्या करे: उद्वर्तन का प्रयत्न · फल: खुजली, फुंसियाँ (कोठ सहित), कुष्ठ, सूजन शान्त।",
    "chain": {"steps": ["तैल लगा शरीर (तैलाक्तम्)", "मट्ठे में पिसे चूर्ण (तक्रपिष्टैः)", "उद्वर्तन का प्रयत्न (उद्वर्तयितुं यतेत)",
                        "रोग शान्त (शमं व्रजन्ति)"]},
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["तैस्तक्रपिष्टैः", "प्रथमं", "शरीरं", "तैलाक्तमुद्वर्तयितुं", "यतेत"]},
        {"label": "दूसरी पंक्ति",
         "items": ["तेनास्यकण्डूः", "पिडकाः", "सकोठाः", "कुष्ठानि", "शोफाश्च", "शमं", "व्रजन्ति"]}]},
    "sandhi": "विसर्ग + त → स्त: तैः + तक्र… → तैस्तक्र…। अ + अ → आ: तैल + अक्तम् → तैलाक्तम्। विसर्ग + च → श्च: शोफाः + च → शोफाश्च। अ + अ → आ: तेन + अस्य → तेनास्य।",
    "anchors": "तक्रपिष्टैः = तक्र (मट्ठा) + पिष्टैः (पिसे हुए) · तैलाक्तम् = तैल + अक्त (तेल से लिपटा) · सकोठाः = स- (साथ) + कोठाः · शमं व्रजन्ति = शान्ति को पहुँचते हैं।",
    "chunks": "तैस्तक्रपिष्टैः प्रथमं शरीरं | तैलाक्तमुद्वर्तयितुं यतेत ‖ तेनास्यकण्डूः पिडकाः सकोठाः | कुष्ठानि शोफाश्च शमं व्रजन्ति।",
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "कुष्ठामृतासङ्गकटङ्कटेरी",
    "question": "What is verse 10, and how do सर्जरसः and करवीरकत्वक् name plant parts?",
    "rule": ("Verse 10 is another drug list, again with no verb. It opens "
             "with a long compound running from कुष्ठ to लोध्राः and ends "
             "with सौगन्धिकम्, सर्जरसः, विडङ्गम्, मनःशिलाले and "
             "करवीरकत्वक्."),
    "limits": ("Low confidence in the data. Names only: no use, no dose, "
               "no verb. अमृतासङ्ग is kept as one name; it could be split "
               "amṛtā + saṅga, which is uncertain. सौगन्धिक is not "
               "identified. Verse 11 speaks of dusting powders, but the "
               "data says which powders it means is not stated."),
    "explain_hi": ("यह श्लोक फिर औषधों की सूची है, बिना क्रिया के; डेटा इसे कम विश्वास वाला मानता है। "
                   "शुरू का लम्बा समास ‘कुष्ठामृतासङ्गकटङ्कटेरीकासीसकम्पिल्लकमुस्तलोध्राः’ कुष्ठ से लेकर लोध्र तक के नाम एक साथ जोड़ता है "
                   "(‘अमृतासङ्ग’ को एक नाम रखा गया है; उसे अमृता + सङ्ग भी तोड़ा जा सकता है, जो अनिश्चित है)। फिर सौगन्धिक, सर्ज का रस, विडङ्ग, "
                   "मनःशिला और आल, और करवीरक की छाल हैं। ‘सर्जरसः’ का अर्थ ‘सर्ज का रस’ है। "
                   "मात्रा, उपयोग या क्रिया श्लोक में नहीं है।"),
    "hook": "श्लोक १०: लम्बा समास (कुष्ठ … लोध्राः) + सौगन्धिक, सर्जरस, विडङ्ग, मनःशिला-आल, करवीरक की छाल; क्रिया नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 10 mainly contain?",
            ("A list of drug names, with no verb", "The verse is a long compound of names plus five more items."),
            [("A rule for making powders equal", "That is verse 8."),
             ("The troubles that subside", "Troubles are named in verses 7 and 9."),
             ("The speaker's name", "The speaker is named in verse 2.")],
            "The verse runs from कुष्ठ… to करवीरकत्वक् as a plain list.",
            "Verse 10: a list of drug names; no verb, use or dose."),
        match(1, "Match each item of verse 10 to its meaning.",
              [["सर्जरसः", "resin or sap of sarja"],
               ["करवीरकत्वक्", "bark of karavīraka"],
               ["मनःशिलाले", "manaḥśilā and āla (a pair)"],
               ["सौगन्धिकम्", "saugandhika, a fragrant drug (name kept)"]],
              "Two items are 'X-of' compounds, one is a pair, one is a name kept as it is.",
              "सर्जरसः = sap of sarja; करवीरकत्वक् = bark of karavīraka; मनःशिलाले = manaḥśilā and āla; सौगन्धिकम् = saugandhika."),
        fill(2, "In सर्जरसः the second part, meaning resin or sap, is ____ (type it in Devanagari).",
             ["रसः", "रस", "रसं", "रसम्"],
             "सर्जरसः = सर्ज + रसः, 'the resin or sap of sarja'.",
             "सर्जरसः names a part of the sarja plant; the second member रस is the sap or resin.",
             "सर्ज + रस = sap of sarja."),
        mcq("discriminate", 3, "Why is the printed form सर्जरसो विडङ्गम् and not सर्जरसः विडङ्गम्?",
            ("अः before a voiced consonant (here व) becomes ओ", "The visarga after अ turns into ओ before a voiced sound."),
            [("The visarga drops before any consonant", "It does not drop here; it turns into ओ."),
             ("स becomes ओ before विडङ्गम्", "Only the visarga changes, not the स."),
             ("सर्जरस is a feminine word and takes ओ", "सर्जरसः is nominative singular masculine; the ओ is sandhi.")],
            "सर्जरसः + विडङ्गम् → सर्जरसो विडङ्गम्; the same rule gives करञ्जो वासा in verse 3.",
            "अः + घोष (voiced sound) → ओ."),
        multi("apply", 4, "Which of these items appear in verse 10 itself?",
              [("विडङ्गम्", "Right: it is in the second line."),
               ("करवीरकत्वक्", "Right: it ends the verse."),
               ("मुस्त", "Right: it is inside the opening compound."),
               ("तक्रम्", "Buttermilk is in verse 9."),
               ("सर्षपतैलम्", "Mustard oil is in verse 6.")],
              [0, 1, 2],
              "The first three are in verse 10; buttermilk and mustard oil are in other verses.",
              "Know which verse each name belongs to."),
        mcq("transfer", 5,
            "A made-up phrase is इक्षुरसः (इक्षु sugarcane). By the pattern of सर्जरसः, what is it?",
            ("The juice of sugarcane", "X-रसः reads 'sap or juice of X', as सर्जरसः is the sap of sarja."),
            [("A sugarcane made of juice", "The phrase names the juice of the cane, not a cane made of juice."),
             ("The bark of sugarcane", "Bark is त्वक्, as in करवीरकत्वक्; this phrase ends in रसः."),
             ("Sugarcane without juice", "रसः is not negated here.")],
            "The compound pairs a plant with its sap: X-रसः. This is a grammar drill, not a medical statement.",
            "X-रसः = sap or juice of X; X-त्वक् = bark of X.",
            teaches="Plant-part compounds like सर्जरसः and करवीरकत्वक् read 'the part of the plant'."),
    ],
}

NOTES_HI["10"] = ("विश्वास: कम (डेटा में)। संधियाँ जाँची: कुष्ठ + अमृता… → कुष्ठामृता… (अ + अ → आ); सर्जरसः + विडङ्गम् → सर्जरसो विडङ्गम् (अः + घोष → ओ)। "
                  "डेटा की टिप्पणी: ‘अमृतासङ्ग’ को एक नाम रखा गया है, उसे अमृता + सङ्ग भी तोड़ा जा सकता है (अनिश्चित); ‘सर्जरस’ = सर्ज का रस/राल; "
                  "‘सौगन्धिक’ की पहचान नहीं की गई। श्लोक ११ में चूर्ण छिड़कने की बात है, पर कौन-से चूर्ण, डेटा के अनुसार वहाँ स्पष्ट नहीं। "
                  "कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["10"] = {
    "frame": "क्या: औषधों की सूची · कोई क्रिया नहीं · शुरू में लम्बा समास (कुष्ठ … लोध्राः) · अन्त में सर्जरस, मनःशिला-आल, करवीरक की छाल।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["कुष्ठामृतासङ्गकटङ्कटेरीकासीसकम्पिल्लकमुस्तलोध्राः"]},
        {"label": "दूसरी पंक्ति",
         "items": ["सौगन्धिकं", "सर्जरसो", "विडङ्गं", "मनःशिलाले", "करवीरकत्वक्"]}]},
    "sandhi": "अ + अ → आ: कुष्ठ + अमृता… → कुष्ठामृता…। अः + घोष → ओ: सर्जरसः + विडङ्गम् → सर्जरसो विडङ्गम्।",
    "anchors": "सर्जरसः = सर्ज + रस (सर्ज का रस) · करवीरकत्वक् = करवीरक + त्वक् (करवीरक की छाल) · मनःशिलाले = मनःशिला और आल (द्विवचन, पढ़ा गया रूप)।",
    "chunks": "कुष्ठामृतासङ्गकटङ्कटेरीकासीसकम्पिल्लकमुस्तलोध्राः ‖ सौगन्धिकं सर्जरसो विडङ्गं | मनःशिलाले करवीरकत्वक्।",
}

IMAGE_SPECS = {
    ("3", "diagram"): {
        "file": "ch3-drugs-3.svg",
        "alt": "Two columns showing the printed words of verse 3 line by line: seven words in the first line (āragvadha, saiḍagaja, karañja, vāsā, guḍūcī, madana, haridre) and seven in the second (śryāhvaḥ, surāhvaḥ, khadira, dhava, nimba, viḍaṅga, karavīraka bark)",
        "type": "split",
        "title": "श्लोक ३: औषधों की सूची",
        "cols": [["पहली पंक्ति", ["आरग्वधः", "सैडगजः", "करञ्जो", "वासा", "गुडूची", "मदनं", "हरिद्रे"]],
                 ["दूसरी पंक्ति", ["श्र्याह्वः", "सुराह्वः", "खदिरो", "धवश्च", "निम्बो", "विडङ्गं", "करवीरकत्वक्"]]],
    },
    ("6", "chain"): {
        "file": "ch3-prep-6.svg",
        "alt": "A chain of five boxes in the verse's order: soaked in cow's bile, ground again, prepared, combined with mustard oil, applied by the physician",
        "type": "chain",
        "title": "श्लोक ६: छह चूर्ण-प्रदेह कैसे",
        "steps": ["गोपित्त में भिगोना (गोपित्तपीताः)", "फिर पीसना (पुनरेव पिष्टाः)", "सिद्ध करना (सिद्धाः)",
                  "सरसों का तेल (सर्षपतैलयुक्ताः)", "वैद्य द्वारा प्रयोग (भिषजा प्रयोज्याः)"],
    },
    ("9", "chain"): {
        "file": "ch3-rub-9.svg",
        "alt": "A chain of four boxes: oil-smeared body, powders ground with buttermilk, the attempt to rub, the troubles go to rest",
        "type": "chain",
        "title": "श्लोक ९: उद्वर्तन का क्रम",
        "steps": ["तैल लगा शरीर (तैलाक्तम्)", "मट्ठे में पिसे चूर्ण (तक्रपिष्टैः)", "उद्वर्तन का प्रयत्न (उद्वर्तयितुं यतेत)",
                  "रोग शान्त (शमं व्रजन्ति)"],
    },
}
