from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}
NOTES_HI = {}
AIDS = {}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "तैलाक्तगात्रस्य कृतानि चूर्णानि",
    "question": "On what kind of body are the powders applied in verse 11, and what comes to rest?",
    "rule": ("The prepared powders are to be applied for dusting (अवचूर्णनार्थम्) on one "
             "whose body is smeared with oil; thus dadru with itching, kiṭibha, pāmā and "
             "vicarcikā come to rest. Which powders is not said here."),
    "limits": ("The verse does not say which powders are meant; the nearest groups are in "
               "the verses just before it. It gives no dose and no method beyond dusting. "
               "The disease names are kept as in the data, not identified further."),
    "explain_hi": ("यह श्लोक पिछले श्लोकों के चूर्णों का प्रयोग बताता है, पर यहाँ यह नहीं लिखा कि "
                   "‘एतानि’ यानी ये कौन-से चूर्ण हैं। शरीर पहले तेल से चुपड़ा हो "
                   "(तैलाक्तगात्रस्य), और चूर्ण ‘अवचूर्णन’ के लिए, यानी ऊपर से छिड़कने के लिए, "
                   "लगाए जाएँ। परिणाम में चार नाम गिनाए गए हैं: खुजली-सहित दद्रु, किटिभ, पामा और "
                   "विचर्चिका; ये ‘शान्ति’ को प्राप्त होते हैं। ‘एति’ क्रिया एकवचन है, पर कर्ता "
                   "की सूची बहुवचन समूह की तरह ली गई है।"),
    "hook": "तेल से चुपड़े शरीर पर चूर्ण छिड़को: दद्रु, किटिभ, पामा, विचर्चिका शान्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "On what kind of body does verse 11 say the powders are to be applied?",
            ("One whose body is smeared with oil",
             "तैलाक्तगात्रस्य = of one whose body (गात्र) is smeared (आक्त) with oil (तैल)."),
            [("One whose body has been bathed in cold water",
              "No water or bath is mentioned; the word is तैल, oil."),
             ("One whose body is covered with ash",
              "Ash is not mentioned in this verse."),
             ("One who has been given an emetic",
              "No emetic or other treatment is named in this verse.")],
            "The first word, तैलाक्तगात्रस्य, gives the condition of the body: smeared with oil.",
            "Verse 11: powders for dusting, on an oil-smeared body."),
        match(1, "Match each word of verse 11 to its meaning.",
              [["तैलाक्तगात्रस्य", "of one whose body is smeared with oil"],
               ["चूर्णानि", "powders"],
               ["अवचूर्णनार्थम्", "for dusting"],
               ["शान्तिम्", "calm, cessation"]],
              "These four words carry the application and the result.",
              "तैलाक्तगात्रस्य = of the oil-smeared body; चूर्णानि = powders; अवचूर्णनार्थम् = for dusting; शान्तिम् = calm."),
        fill(2, "The last disease named in the verse, next to चैव, is ____ (type it in Devanagari).",
             ["विचर्चिका", "विचर्चिकाः"],
             "Line 2 ends the list with पामा विचर्चिका चैव.",
             "The disease names दद्रूः, पामा, विचर्चिका are nominative singular; किटिभानि is neuter plural. They are the subjects that come to rest.",
             "The things that come to rest (शान्तिम् एति) are in the nominative."),
        mcq("discriminate", 3, "Which is the right split of चूर्णान्येतानि?",
            ("चूर्णानि + एतानि",
             "इ before an unlike vowel becomes य्, and the vowel joins it: इ + ए gives ये."),
            [("चूर्णान् + येतानि", "येतानि is not a word."),
             ("चूर्णानि + अतानि", "The second word is एतानि, 'these', not अतानि."),
             ("चूर्ण + अन्येतानि", "अन्येतानि is not a word.")],
            "चूर्णान्येतानि = चूर्णानि ('powders') + एतानि ('these').",
            "इ + असमान स्वर → य् + स्वर: चूर्णानि + एतानि → चूर्णान्येतानि."),
        multi("apply", 4, "Which of these does verse 11 say?",
              [("The powders are for dusting (अवचूर्णनार्थम्)", "Right: दद्यादवचूर्णनार्थम्."),
               ("The body is smeared with oil first", "Right: तैलाक्तगात्रस्य."),
               ("Dadru with itching is among those that come to rest", "Right: दद्रूः सकण्डूः ... शान्तिम्."),
               ("The ingredients of each powder are listed", "The verse lists no ingredients; it points to powders given earlier."),
               ("The powders are ground with buttermilk", "Buttermilk is not mentioned in verse 11.")],
              [0, 1, 2],
              "Line 1 gives the way of use and the condition of the body; line 2 gives the diseases that come to rest.",
              "Verse 11: oil-smeared body, dusting, four diseases come to rest."),
        mcq("transfer", 5,
            "A made-up phrase reads घृताक्तगात्रस्य नरस्य. Following तैलाक्तगात्रस्य, what does it mean?",
            ("Of a man whose body is smeared with ghee",
             "Same compound as तैलाक्तगात्र, with घृत (ghee) in place of तैल (oil)."),
            [("Of a man who eats ghee", "आक्त means smeared, and गात्र means body; eating is not in the compound."),
             ("Of ghee smeared on the body of a man's friend", "The compound describes the man himself: his body is smeared."),
             ("Of a man whose body is smeared with oil", "That is the verse's compound; here the first part is घृत, ghee.")],
            "The compound is X-आक्त-गात्र: 'one whose body is smeared with X'. Only X changes, and the genitive -स्य is kept.",
            "X-आक्तगात्रस्य = of one whose body is smeared with X.",
            teaches="Once you know this compound, any 'X-आक्तगात्र' reads as 'body smeared with X'."),
    ],
}

NOTES_HI["11"] = ("संधियाँ जाँची: चूर्णानि + एतानि → चूर्णान्येतानि (इ → य् असमान स्वर से पहले); दद्यात् + अवचूर्णन… → "
                  "दद्यादवचूर्णनार्थम् (त् → द् स्वर से पहले); अवचूर्णन + अर्थम् → अवचूर्णनार्थम् (अ + अ → आ); "
                  "च + एव → चैव; तथा + एति → तथैति (आ + ए → ऐ)। इस श्लोक में कोई पाठभेद या पाठ-दोष नहीं दिया गया। "
                  "टिप्पणी के अनुसार ‘एतानि’ किन चूर्णों का है, यह यहाँ नहीं कहा गया।")

AIDS["11"] = {
    "frame": "कब: शरीर तेल से चुपड़ा हो · क्या: ये बनाए हुए चूर्ण · कैसे: अवचूर्णन (छिड़कना) · फल: दद्रु, किटिभ, पामा, विचर्चिका शान्त। (कौन-से चूर्ण: यहाँ नहीं कहा।)",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["तैलाक्तगात्रस्य", "कृतानि", "चूर्णान्येतानि", "दद्यादवचूर्णनार्थम्"]},
        {"label": "दूसरी पंक्ति",
         "items": ["दद्रूः", "सकण्डूः", "किटिभानि", "पामा", "विचर्चिका", "चैव", "तथैति", "शान्तिम्"]}]},
    "sandhi": "इ + ए → ये: चूर्णानि + एतानि → चूर्णान्येतानि। त् → द् (स्वर से पहले): दद्यात् + अवचूर्णन… → दद्यादवचूर्णनार्थम्। आ + ए → ऐ: तथा + एति → तथैति; अ + ए → ऐ: च + एव → चैव।",
    "anchors": "तैलाक्तगात्र = तैल + आक्त + गात्र (बहुव्रीहि: ‘जिसका शरीर तेल से चुपड़ा हो’) · अवचूर्णन = अव + चूर्ण (पाउडर) + -न: छिड़कना · शान्तिम् एति = शान्ति को प्राप्त होता है।",
    "chunks": "तैलाक्तगात्रस्य कृतानि | चूर्णान्येतानि दद्यादवचूर्णनार्थम् ‖ दद्रूः सकण्डूः किटिभानि पामा | विचर्चिका चैव तथैति शान्तिम्।",
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "मनःशिलाले मरिचानि तैलम्",
    "question": "What is the first pradeha of verse 12 made of, and what is the second line's 'likewise'?",
    "rule": ("Line 1: manaḥśilā and āla, peppers, oil and arka milk make a pradeha that "
             "removes kuṣṭha. Line 2: tuttha, viḍaṅga, peppers, kuṣṭha and lodhra, likewise, "
             "with manaḥśilā (तद्वत् समनःशिलं स्यात्)."),
    "limits": ("Arka is left unidentified in the data (it has several senses). Line 2 has no "
               "stated subject; pradeha is understood from line 1. The verse gives no "
               "quantity or method."),
    "explain_hi": ("पहली पंक्ति में एक प्रदेह की सामग्री है: मनःशिला और आल (जोड़ा), मरिच, तैल और "
                   "आर्क पयः यानी अर्क का दूध; इसे ‘कुष्ठहरः’ कहा गया है, यानी कुष्ठ को हरने "
                   "वाला। दूसरी पंक्ति ‘तद्वत्’ (उसी प्रकार) से दूसरी सामग्री गिनाती है: तुत्थ, "
                   "विडङ्ग, मरिच, कुष्ठ और लोध्र, ‘समनःशिलम्’ यानी मनःशिला के साथ। ‘स-’ का अर्थ "
                   "यहाँ ‘साथ’ है। दूसरी पंक्ति में कर्ता लिखा नहीं है; ‘प्रदेहः’ पहली पंक्ति से "
                   "समझा जाता है। ‘अर्क’ की पहचान आँकड़े में नहीं दी गई।"),
    "hook": "मनःशिला-आल-मिर्च-तेल-अर्कक्षीर = कुष्ठहर प्रदेह; दूसरी पंक्ति ‘तद्वत्’, ‘स-’ = साथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does line 1 of verse 12 call the preparation of manaḥśilā, āla, peppers, oil and arka milk?",
            ("A pradeha that removes kuṣṭha",
             "कुष्ठहरः प्रदेहः = a pradeha (paste) removing kuṣṭha."),
            [("A gruel that removes thirst", "No gruel is mentioned; the word is प्रदेहः."),
             ("An enema for the lower gut", "No enema is named here."),
             ("A powder to induce vomiting", "Nothing in the verse speaks of vomiting.")],
            "The first line closes with कुष्ठहरः प्रदेहः.",
            "Verse 12, line 1: these ingredients make a kuṣṭha-removing pradeha."),
        order(1, "Put these four items in the order they stand in line 1 of verse 12.",
              ["मनःशिलाले", "मरिचानि", "तैलमार्कं", "पयः"],
              "Line 1 begins मनःशिलाले मरिचानि तैलमार्कं पयः.",
              "मनःशिलाले → मरिचानि → तैलमार्कं → पयः."),
        fill(2, "The word in line 2 meaning 'likewise' is ____ (type it in Devanagari).",
             ["तद्वत्"],
             "Line 2 reads ... लोध्रं च तद्वत् समनःशिलं स्यात्.",
             "तद्वत् is an indeclinable: 'in that way, likewise'. It links the second list to the first pradeha.",
             "तद्वत् = likewise; the second list is made on the pattern of the first."),
        mcq("discriminate", 3, "Which is the right split of समनःशिलम्?",
            ("स + मनःशिलम्",
             "स- as the first part means with: 'with manaḥśilā'."),
            [("सम + नःशिलम्", "नःशिलम् is not a word."),
             ("सा + मनःशिलम्", "There is no long सा here; the prefix is short स."),
             ("समन + शिलम्", "समन is not a word, and शिल alone is not the drug named here.")],
            "समनःशिलम् = स ('with') + मनःशिलम् ('manaḥśilā'): the second list is to be taken with manaḥśilā.",
            "स- + noun = 'with that noun'."),
        multi("apply", 4, "Which of these stand in line 2 of verse 12?",
              [("Tuttha", "Right: तुत्थं opens line 2."),
               ("Lodhra", "Right: लोध्रं च is in line 2."),
               ("Peppers, again", "Right: मरिचानि is named in both lines."),
               ("Oil", "Oil (तैलम्) is in line 1, not line 2."),
               ("Arka milk", "Arka milk (आर्कं पयः) is in line 1, not line 2.")],
              [0, 1, 2],
              "Line 2 names tuttha, viḍaṅga, peppers, kuṣṭha and lodhra, then tells us to take them with manaḥśilā.",
              "Line 2: तुत्थ, विडङ्ग, मरिच, कुष्ठ, लोध्र."),
        mcq("transfer", 5,
            "A made-up phrase reads तुत्थं सलोध्रं स्यात्. Following समनःशिलं स्यात्, what does it say?",
            ("Tuttha should be taken with lodhra",
             "सलोध्रम् = स ('with') + लोध्रम्, just as समनःशिलम् is 'with manaḥśilā'."),
            [("Tuttha should be taken without lodhra", "स- means with, not without."),
             ("Tuttha should be taken in place of lodhra", "सलोध्रम् means with lodhra, not instead of it."),
             ("Tuttha is lodhra", "The phrase joins two drugs; it does not say they are the same.")],
            "स + लोध्रम् gives सलोध्रम् (अ-ending stem, no sandhi change): 'with lodhra'.",
            "सX = with X, so 'A सX स्यात्' = 'A should be with X'.",
            teaches="The स- rule lets you read any 'सX' in a drug list as 'together with X'."),
    ],
}

NOTES_HI["12"] = ("संधियाँ जाँची: तैलम् + आर्कम् → तैलमार्कम् (म् अगले स्वर से सटा); स + मनःशिलम् → समनःशिलम् (कोई बदलाव नहीं)। "
                  "इस श्लोक में कोई पाठभेद या पाठ-दोष नहीं दिया गया। टिप्पणी के अनुसार ‘आर्कं पयः’ का अर्थ अर्क का दूध है, पर ‘अर्क’ की "
                  "पहचान छोड़ी गई है (उसके कई अर्थ हैं)। दूसरी पंक्ति में कर्ता लिखा नहीं; ‘प्रदेहः’ पहली पंक्ति से लिया गया। "
                  "‘मरिचानि’ नपुंसक बहुवचन है: मिर्च या काली मिर्च के दाने।")

AIDS["12"] = {
    "frame": "पहली पंक्ति: मनःशिला-आल, मरिच, तैल, अर्क का दूध = कुष्ठहर प्रदेह · दूसरी पंक्ति: तद्वत् (उसी तरह) तुत्थ, विडङ्ग, मरिच, कुष्ठ, लोध्र, मनःशिला के साथ।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["मनःशिलाले", "मरिचानि", "तैलमार्कं", "पयः", "कुष्ठहरः", "प्रदेहः"]},
        {"label": "दूसरी पंक्ति",
         "items": ["तुत्थं", "विडङ्गं", "मरिचानि", "कुष्ठं", "लोध्रं", "च", "तद्वत्", "समनःशिलं", "स्यात्"]}]},
    "sandhi": "म् + स्वर: तैलम् + आर्कम् → तैलमार्कम् (म् अगले स्वर के साथ लिखा जाता है)। स + मनःशिलम् → समनःशिलम्: ‘स-’ = साथ।",
    "anchors": "कुष्ठहरः = कुष्ठ + हरः (हरने वाला) · समनःशिलम् = स (साथ) + मनःशिलम् · तद्वत् = उसी के समान (-वत् = समान)।",
    "contrast": "कुष्ठहरः में ‘कुष्ठ’ वह है जिसे प्रदेह हरता है ↔ दूसरी पंक्ति में ‘कुष्ठं’ सामग्री की सूची में है। एक ही शब्द, दो जगह दो भूमिकाएँ।",
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "रसाञ्जनं सप्रपुनाडबीजम्",
    "question": "Which two preparations does verse 13 give, and with what liquid is each made?",
    "rule": ("First: rasāñjana with prapunāḍa seeds, mixed with the juice of kapittha, is a "
             "lepa. Second: karañja seeds and eḍagaja with kuṣṭha, ground in cow's urine, "
             "are another pradeha. No disease is named in the verse."),
    "limits": ("परः can mean 'another' or 'excellent'; the data renders it 'another'. "
               "Whether eḍagaja is the plant or its seeds is not decided. The verse names "
               "no disease and gives no quantities."),
    "explain_hi": ("इस श्लोक में दो अलग तैयारियाँ हैं। पहली पंक्ति: प्रपुनाड के बीजों सहित रसाञ्जन, "
                   "‘कपित्थस्य रसेन’ यानी कैथ के रस से मिलाया हुआ, ‘लेप’ है। दूसरी पंक्ति: "
                   "करञ्ज के बीज और एडगज, कुष्ठ के साथ, गोमूत्र में पीसे हुए, एक और प्रदेह हैं। "
                   "‘परः’ का अर्थ ‘दूसरा’ या ‘उत्तम’ दोनों हो सकता है; यहाँ ‘दूसरा’ लिया गया है। "
                   "श्लोक में किसी रोग का नाम नहीं है, इसलिए रोग का दावा इसी श्लोक से नहीं किया जा सकता।"),
    "hook": "रसाञ्जन + प्रपुनाड-बीज + कपित्थ-रस = लेप; करञ्ज-बीज + एडगज + कुष्ठ + गोमूत्र = दूसरा प्रदेह।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In what liquid is the second preparation of verse 13 ground?",
            ("Cow's urine",
             "गोमूत्रपिष्टम् = ground (पिष्ट) in cow's urine (गोमूत्र)."),
            [("The juice of kapittha",
              "Kapittha juice is used for the first preparation, in line 1."),
             ("Buttermilk", "Buttermilk is not mentioned in this verse."),
             ("Milk of arka", "Arka milk is not mentioned in this verse.")],
            "Line 2 says गोमूत्रपिष्टं च परः प्रदेहः: ground in cow's urine, another pradeha.",
            "Verse 13: first preparation with kapittha juice; second ground in cow's urine."),
        match(1, "Match each word of verse 13 to its meaning.",
              [["रसेन", "with the juice"],
               ["लेपः", "plaster, paste"],
               ["सकुष्ठम्", "together with kuṣṭha"],
               ["गोमूत्रपिष्टम्", "ground in cow's urine"]],
              "These four words give the liquids and the way each paste is made.",
              "रसेन = with the juice; लेपः = paste; सकुष्ठम् = with kuṣṭha; गोमूत्रपिष्टम् = ground in cow's urine."),
        fill(2, "Rasāñjana is mixed with the juice of ____ (type the fruit's name in Devanagari).",
             ["कपित्थ", "कपित्थस्य"],
             "Line 1 says युक्तं कपित्थस्य रसेन: mixed with the juice (रस) of kapittha.",
             "कपित्थस्य is genitive singular ('of kapittha'); रसेन is instrumental ('with the juice').",
             "'X-स्य रसेन' = 'with the juice of X': genitive for the source, instrumental for the means."),
        mcq("discriminate", 3, "Which is the right split of करञ्जबीजैडगजम्?",
            ("करञ्जबीज + एडगजम्",
             "अ + ए gives ऐ: करञ्जबीज + एडगजम् is written करञ्जबीजैडगजम्."),
            [("करञ्जबीजै + डगजम्", "डगजम् is not a word."),
             ("करञ्जबीज + ऐडगजम्", "ऐडगजम् is not a word; the drug is एडगज."),
             ("करञ्जबीजः + एडगजम्", "With a visarga the two words would stay apart: करञ्जबीज एडगजम्.")],
            "करञ्जबीजैडगजम् = करञ्जबीज ('karañja seeds') + एडगजम् ('eḍagaja').",
            "अ + ए → ऐ: करञ्जबीज + एडगजम् → करञ्जबीजैडगजम्."),
        multi("apply", 4, "Which of these does verse 13 say?",
              [("Rasāñjana is taken with prapunāḍa seeds", "Right: सप्रपुनाडबीजम्."),
               ("The first preparation is mixed with kapittha juice and is called a lepa", "Right: युक्तं कपित्थस्य रसेन लेपः."),
               ("The second preparation contains karañja seeds, eḍagaja and kuṣṭha", "Right: करञ्जबीजैडगजं सकुष्ठम्."),
               ("The verse names the disease these are for", "No disease is named in verse 13."),
               ("Mustard oil is added to the second preparation", "Mustard oil is not mentioned in this verse.")],
              [0, 1, 2],
              "Line 1 gives the first preparation and its liquid; line 2 gives the second and its liquid.",
              "Verse 13: two preparations, kapittha juice and cow's urine; no disease."),
        mcq("transfer", 5,
            "A made-up phrase reads लोध्रं तक्रपिष्टं च लेपः (तक्र = buttermilk). Following गोमूत्रपिष्टम्, what does it say about the lodhra?",
            ("It is ground in buttermilk",
             "तक्रपिष्टम् = ground (पिष्ट) in buttermilk (तक्र), like गोमूत्रपिष्टम् with cow's urine."),
            [("It is mixed with buttermilk after cooking", "पिष्ट means ground, not cooked."),
             ("It is the buttermilk that has been ground", "In X-पिष्टम्, the thing ground is the noun described (lodhra), and X is the liquid."),
             ("It is ground in cow's urine", "That is the verse's phrase; the made-up one has तक्र, buttermilk.")],
            "X-पिष्ट is a compound 'ground in X'. Here X is तक्र, buttermilk, so lodhra is ground in buttermilk. This is a grammar drill.",
            "X-पिष्टम् = ground in X.",
            teaches="Any 'liquid + पिष्ट' compound in these verses reads as 'ground in that liquid'."),
    ],
}

NOTES_HI["13"] = ("संधियाँ जाँची: रस + अञ्जनम् → रसाञ्जनम् (अ + अ → आ); करञ्जबीज + एडगजम् → करञ्जबीजैडगजम् (अ + ए → ऐ); "
                  "स + प्रपुनाडबीजम्, स + कुष्ठम् (‘साथ’, कोई बदलाव नहीं)। पाठभेद कोई नहीं। टिप्पणी के अनुसार ‘परः’ का अर्थ "
                  "‘दूसरा’ या ‘उत्तम’ हो सकता है; ‘एडगज’ पौधा है या उसके बीज, यह तय नहीं। ‘प्रपुनाड’ वर्तनी संस्करण की है "
                  "(छन्द के लिए ‘पु’ ह्रस्व)।")

AIDS["13"] = {
    "frame": "पहली: रसाञ्जन + प्रपुनाड-बीज, कपित्थ-रस से = लेप · दूसरी: करञ्ज-बीज + एडगज + कुष्ठ, गोमूत्र में पिसा = एक और प्रदेह। (रोग का नाम नहीं।)",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["रसाञ्जनं", "सप्रपुनाडबीजं", "युक्तं", "कपित्थस्य", "रसेन", "लेपः"]},
        {"label": "दूसरी पंक्ति",
         "items": ["करञ्जबीजैडगजं", "सकुष्ठं", "गोमूत्रपिष्टं", "च", "परः", "प्रदेहः"]}]},
    "sandhi": "अ + अ → आ: रस + अञ्जनम् → रसाञ्जनम्। अ + ए → ऐ: करञ्जबीज + एडगजम् → करञ्जबीजैडगजम्।",
    "pegs": "मेरा बनाया चित्र: एक कटोरे में कैथ के रस में मिली लेई (पहली), दूसरे कटोरे में गाय के मूत्र में पिसी बीजों की लुगदी (दूसरी)। केवल याद के लिए।",
    "chunks": "रसाञ्जनं सप्रपुनाडबीजं | युक्तं कपित्थस्य रसेन लेपः ‖ करञ्जबीजैडगजं सकुष्ठं | गोमूत्रपिष्टं च परः प्रदेहः।",
}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "उभे हरिद्रे कुटजस्य बीजम्",
    "question": "What is the verb of verse 14, and what is the lepa mixed with?",
    "rule": ("Both haridrās, kuṭaja seed, karañja seed, sumanas shoots and the bark of "
             "hayamāraka with its middle part are the ingredients (accusatives); one should "
             "prepare (विदध्यात्) a lepa mixed with tila-kṣāra."),
    "limits": ("The identity of hayamāraka ('horse-killer') is left to commentators. "
               "समध्याम् is read as 'with its middle (inner) part' but could mean something "
               "else. Taken as one lepa of all items. No disease and no quantity is named."),
    "explain_hi": ("यहाँ सामग्री द्वितीया विभक्ति में है: ‘उभे हरिद्रे’ (दोनों हरिद्राएँ), कुटज का बीज, "
                   "करञ्ज का बीज, सुमनस् की कोंपलें, और हयमारक की छाल ‘समध्याम्’ यानी उसके मध्य "
                   "भाग सहित। क्रिया ‘विदध्यात्’ है, ‘बनाना चाहिए’, और कर्म ‘लेपम्’ है, जो "
                   "‘तिलक्षारयुतम्’ यानी तिल के क्षार से युक्त हो। ‘हरिद्रे’ में -ए द्विवचन है: दो "
                   "हरिद्राएँ, और ‘उभे’ भी उसी का विशेषण है। हयमारक की पहचान टीकाकारों पर छोड़ी गई है।"),
    "hook": "उभे हरिद्रे + कुटज/करञ्ज बीज + सुमनस् कोंपल + हयमारक छाल → तिलक्षार-युक्त लेप ‘विदध्यात्’।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does verse 14 tell the reader to do with the listed items?",
            ("Prepare a lepa of them, mixed with tila-kṣāra",
             "लेपं तिलक्षारयुतं विदध्यात् = one should prepare a lepa mixed with sesame alkali."),
            [("Cook them into a gruel", "No gruel is mentioned; the object is लेपम्, a paste."),
             ("Give them as an enema", "No enema is mentioned in this verse."),
             ("Burn them to ash and drink the ash", "Nothing is said about burning or drinking.")],
            "The accusative items are the ingredients; the verb विदध्यात् and its object लेपम् give the instruction.",
            "Verse 14: prepare a lepa of these, with tila-kṣāra."),
        match(1, "Match each phrase of verse 14 to its meaning.",
              [["उभे हरिद्रे", "both haridrās"],
               ["कुटजस्य बीजम्", "the seed of kuṭaja"],
               ["सुमनःप्रवालान्", "sumanas shoots"],
               ["तिलक्षारयुतम्", "mixed with sesame alkali"]],
              "Each phrase names one ingredient or the thing it is mixed with.",
              "उभे हरिद्रे = both haridrās; कुटजस्य बीजम् = kuṭaja seed; सुमनःप्रवालान् = sumanas shoots; तिलक्षारयुतम् = mixed with tila-kṣāra."),
        fill(2, "The verb of verse 14, meaning 'one should prepare', is ____ (type it in Devanagari).",
             ["विदध्यात्"],
             "The last word of the verse is विदध्यात्.",
             "विदध्यात् is the third person singular optative of वि-√धा: 'one should prepare'. It governs the object लेपम्.",
             "The optative -यात् gives 'one should'; the accusatives are what is prepared or used."),
        mcq("discriminate", 3, "In उभे हरिद्रे, what does the ending -ए of हरिद्रे show?",
            ("Dual: two haridrās",
             "उभे means 'both' (two); हरिद्रे is accusative dual."),
            [("Singular: one haridrā", "उभे 'both' needs two things."),
             ("Plural: many haridrās", "उभे means both of two, not many."),
             ("Genitive singular: of the haridrā", "The genitive in this verse is कुटजस्य; हरिद्रे is the object, accusative.")],
            "उभे हरिद्रे = the two haridrās (accusative dual feminine).",
            "Feminine -आ stems: dual -ए (nominative/accusative)."),
        multi("apply", 4, "Which of these does verse 14 say?",
              [("Karañja seed is one of the items", "Right: करञ्जबीजम्."),
               ("The bark of hayamāraka is one of the items", "Right: त्वचं हयमारकस्य."),
               ("The lepa is mixed with tila-kṣāra", "Right: तिलक्षारयुतम्."),
               ("The verse says which plant hayamāraka is", "The identity of hayamāraka is not given."),
               ("The verse gives the quantity of each item", "No quantity is named.")],
              [0, 1, 2],
              "Line 1 and the start of line 2 list the ingredients; the end of line 2 gives the mixing and the verb.",
              "Verse 14: ingredients, tila-kṣāra, verb विदध्यात्; no identity and no quantity."),
        mcq("transfer", 5,
            "A made-up phrase reads उभे बले दद्यात्. Following उभे हरिद्रे, what does it say?",
            ("One should give both balās (two)",
             "उभे बले is like उभे हरिद्रे: feminine -आ stem in the dual, accusative."),
            [("One should give one balā", "उभे 'both' shows two."),
             ("One should give many balās", "उभे does not mean many."),
             ("One should give of the balā", "बले is not a genitive; दद्यात् takes an object, here in the dual.")],
            "बला (feminine, -आ) has dual -ए, as हरिद्रा has हरिद्रे. उभे also marks two. This is a grammar drill.",
            "Feminine -आ stems: dual in -ए; उभे = both.",
            teaches="You can now spot a pair of feminine drugs by -ए plus उभे or द्वे."),
    ],
}

NOTES_HI["14"] = ("संधियाँ जाँची: सुमनस् + प्रवालान् → सुमनःप्रवालान् (अन्त के स् का विसर्ग, प से पहले); तिल + क्षार + युतम् सामासिक रूप। "
                  "पाठभेद या पाठ-दोष कोई नहीं दिया गया। टिप्पणी के अनुसार ‘समध्याम्’ को ‘त्वचम्’ के साथ ‘मध्य (भीतरी) भाग सहित छाल’ पढ़ा गया है, "
                  "पर कुछ और भी अर्थ सम्भव है। ‘हयमारक’ का शाब्दिक अर्थ ‘घोड़े को मारने वाला’ है; पहचान टीकाकारों पर छोड़ी गई है। "
                  "सब सामग्री को एक ही लेप की माना गया है।")

AIDS["14"] = {
    "frame": "क्या: उभे हरिद्रे, कुटज-बीज, करञ्ज-बीज, सुमनस् कोंपल, हयमारक की छाल (मध्य सहित) · कैसे: तिलक्षार से युक्त लेप · क्रिया: विदध्यात्।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["उभे", "हरिद्रे", "कुटजस्य", "बीजं", "करञ्जबीजं", "सुमनःप्रवालान्"]},
        {"label": "दूसरी पंक्ति",
         "items": ["त्वचं", "समध्यां", "हयमारकस्य", "लेपं", "तिलक्षारयुतं", "विदध्यात्"]}]},
    "sandhi": "स् → विसर्ग प से पहले: सुमनस् + प्रवालान् → सुमनःप्रवालान्। द्विवचन: उभे हरिद्रे (दोनों -ए, स्त्रीलिंग -आ से)।",
    "anchors": "विदध्यात् ← वि + √धा (विधान, विधि) · तिलक्षारयुतम् = तिल + क्षार + युतम् (युत = मिला हुआ) · समध्याम् = स + मध्याम् (मध्य सहित)।",
    "chunks": "उभे हरिद्रे कुटजस्य बीजं | करञ्जबीजं सुमनःप्रवालान् ‖ त्वचं समध्यां हयमारकस्य | लेपं तिलक्षारयुतं विदध्यात्।",
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "मनःशिला त्वक् कुटजात् सकुष्ठात्",
    "question": "Which items does verse 15 list, and with what are the powders to be prepared?",
    "rule": ("Manaḥśilā; kuṭaja bark with kuṣṭha; karañja with lomaśa and eḍagaja; granthi "
             "and bhaurja; karavīra root: these powders are to be prepared (साध्यानि) with "
             "tuṣodaka, husk-water. Verse 16 refers back to them."),
    "limits": ("The ablative forms in line 1 are unusual; read as 'bark from kuṭaja, with "
               "kuṣṭha'. 'karañja with eḍagaja' could also be 'eḍagaja and karañja'. "
               "साध्यानि may also mean 'to be cooked', and whether tuṣodaka is plain "
               "husk-water or fermented is not said."),
    "explain_hi": ("इस श्लोक में कई औषधों के चूर्ण गिनाए गए हैं: मनःशिला; कुष्ठ-सहित कुटज की छाल; "
                   "लोमश और एडगज के साथ करञ्ज; ग्रन्थि और भौर्ज; और करवीर की जड़। अन्त में बताया है "
                   "कि इनके चूर्ण ‘तुषोदकेन’ यानी भूसी के जल से ‘साध्यानि’ (तैयार किए जाने "
                   "योग्य) हैं। पहली पंक्ति के पञ्चमी रूप (कुटजात्, सकुष्ठात्) असामान्य हैं और "
                   "‘कुटज से छाल, कुष्ठ के साथ’ पढ़े गए हैं। अगले श्लोक (१६) में ‘कर्षोद्धृतानि’ इन्हीं "
                   "चूर्णों की ओर संकेत करता है।"),
    "hook": "मनःशिला, कुटज-छाल+कुष्ठ, करञ्ज+लोमश+एडगज, ग्रन्थि, भौर्ज, करवीर-मूल: चूर्ण तुषोदक से (श्लोक १६ इन्हीं का है)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "With what liquid are the powders of verse 15 to be prepared?",
            ("Husk-water (तुषोदक)",
             "तुषोदकेन = with husk-water (तुष + उदक)."),
            [("Cow's urine", "Cow's urine is in verse 13, not in this verse."),
             ("Buttermilk", "Buttermilk is not named in this verse."),
             ("Mustard oil", "Mustard oil is not named in this verse.")],
            "The last word, तुषोदकेन, is the instrumental of the liquid.",
            "Verse 15: powders prepared with tuṣodaka."),
        order(1, "Put these four items in the order they stand in verse 15.",
              ["सलोमशः", "ग्रन्थिश्च", "भौर्जः", "करवीरमूलं"],
              "सलोमशः stands in line 1 (after सकुष्ठात्); line 2 then runs ग्रन्थिश्च, भौर्जः, करवीरमूलं.",
              "सलोमशः → ग्रन्थिश्च → भौर्जः → करवीरमूलं."),
        fill(2, "The word in line 2 meaning 'to be prepared' is ____ (type it in Devanagari).",
             ["साध्यानि"],
             "It stands in line 2, second word from the end.",
             "साध्यानि is a gerundive, neuter plural, agreeing with चूर्णानि: 'to be prepared'.",
             "साध्यानि = to be prepared (gerundive of √साध्)."),
        mcq("discriminate", 3, "Which is the right split of तुषोदकेन?",
            ("तुष + उदकेन",
             "अ + उ → ओ, so तुष + उदकेन is written तुषोदकेन."),
            [("तुषो + दकेन", "दकेन is not a word."),
             ("तुषोद + केन", "केन is a word ('by what'), but तुषोद is not a word here."),
             ("तुष + ओदकेन", "ओदकेन is not a word.")],
            "तुषोदकेन = तुष ('husk') + उदकेन ('with water').",
            "अ + उ → ओ."),
        multi("apply", 4, "Which of these does verse 15 say?",
              [("Manaḥśilā is among the items", "Right: मनःशिला opens the verse."),
               ("The root of karavīra is among the items", "Right: करवीरमूलम्."),
               ("The powders are to be prepared with tuṣodaka", "Right: चूर्णानि साध्यानि तुषोदकेन."),
               ("The verse names the disease they are for", "No disease is named in verse 15."),
               ("The powders are to be ground with buttermilk", "Buttermilk is not named in this verse.")],
              [0, 1, 2],
              "The verse lists the items, then says the powders are to be prepared with husk-water.",
              "Verse 15: items, powders, husk-water; no disease."),
        mcq("transfer", 5,
            "A made-up compound तिल + उदकेन (sesame-water, with). Using the rule of तुष + उदकेन, how is it written joined?",
            ("तिलोदकेन",
             "अ + उ → ओ, as in तुषोदकेन: तिल + उदकेन → तिलोदकेन."),
            [("तिलौदकेन", "अ + औ gives औ, not अ + उ."),
             ("तिलूदकेन", "ऊ would come from उ + उ, not अ + उ."),
             ("तिलउदकेन", "The two vowels do merge; they are not left side by side.")],
            "तिल ends in short अ; उदकेन starts with उ. अ + उ → ओ. This is a grammar drill with an invented word.",
            "अ + उ → ओ.",
            teaches="The same अ + उ → ओ rule joins any -अ stem to a following उ-word."),
    ],
}

NOTES_HI["15"] = ("संधियाँ जाँची: तुष + उदकेन → तुषोदकेन (अ + उ → ओ); ग्रन्थिः + च → ग्रन्थिश्च (विसर्ग + च → श्); स + एडगजः → "
                  "सैडगजः (अ + ए → ऐ)। पाठभेद या पाठ-दोष कोई नहीं दिया गया। टिप्पणी के अनुसार पहली पंक्ति के पञ्चमी रूप (कुटजात्, सकुष्ठात्) असामान्य हैं; "
                  "‘सैडगजः करञ्जः’ का अर्थ ‘एडगज सहित करञ्ज’ या ‘एडगज और करञ्ज’ दोनों हो सकता है। ‘साध्यानि’ का अर्थ ‘तैयार करने योग्य’ या ‘पकाने योग्य’ भी हो सकता है; "
                  "‘तुषोदक’ सादा भूसी-जल है या किण्वित, यह यहाँ नहीं कहा।")

AIDS["15"] = {
    "frame": "क्या: मनःशिला, कुटज-छाल+कुष्ठ, करञ्ज+लोमश+एडगज, ग्रन्थि, भौर्ज, करवीर-मूल के चूर्ण · कैसे: तुषोदक से साध्य · आगे: श्लोक १६ इन्हीं चूर्णों को लेता है।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["मनःशिला", "त्वक्", "कुटजात्", "सकुष्ठात्", "सलोमशः", "सैडगजः", "करञ्जः"]},
        {"label": "दूसरी पंक्ति",
         "items": ["ग्रन्थिश्च", "भौर्जः", "करवीरमूलं", "चूर्णानि", "साध्यानि", "तुषोदकेन"]}]},
    "sandhi": "अ + उ → ओ: तुष + उदकेन → तुषोदकेन। विसर्ग + च → श्: ग्रन्थिः + च → ग्रन्थिश्च। अ + ए → ऐ: स + एडगजः → सैडगजः।",
    "anchors": "सकुष्ठात्, सलोमशः, सैडगजः: तीनों ‘स-’ (साथ) · साध्यानि ← √साध् (साधना, तैयार करना) · तुषोदक = तुष (भूसी) + उदक (जल)।",
    "chunks": "मनःशिला त्वक् कुटजात् सकुष्ठात् | सलोमशः सैडगजः करञ्जः ‖ ग्रन्थिश्च भौर्जः करवीरमूलं | चूर्णानि साध्यानि तुषोदकेन।",
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "पलाशनिर्दाहरसेन चापि",
    "question": "What name does verse 16 give this lepa, and which earlier verse's powders does it use?",
    "rule": ("With palāśa-nirdāha liquid, measuring an āḍhaka, and with the powders of verse "
             "15 taken by the karṣa, they call this lepa the darvī-pralepa, supreme for "
             "destroying kuṣṭha (कुष्ठनिसूदनाय)."),
    "limits": ("Parsing is uncertain: nirdāha is read as burnt residue (ash), and how the "
               "liquid is made is not said. कर्षोद्धृतानि has no noun here; it is read with "
               "the powders of verse 15. The edition spells निसूदन, possibly for निषूदन. "
               "Darvī is kept as a name."),
    "explain_hi": ("संदर्भ के अनुसार यह श्लोक श्लोक १५ के चूर्णों का उपयोग बताता है: ‘कर्षोद्धृतानि’ नपुंसक बहुवचन है और इस "
                   "श्लोक में उसका कोई संज्ञा-शब्द नहीं है, इसलिए वह पिछले श्लोक के ‘चूर्णानि’ से जुड़ता है। "
                   "तरल है ‘पलाशनिर्दाहरस’ (पलाश के जले अवशेष का रस), ‘आढकसंमित’ यानी आढक की माप का। "
                   "लोग (वे) इस लेप को ‘दर्वीप्रलेप’ कहते हैं (प्रवदन्ति), और इसे ‘कुष्ठनिसूदन’, यानी कुष्ठ के नाश के "
                   "लिए श्रेष्ठ (परम्) बताते हैं। कर्ष और आढक माप हैं; श्लोक में कोई संख्या नहीं दी गई।"),
    "hook": "श्लोक १५ के चूर्ण + पलाश-निर्दाह-रस = ‘दर्वीप्रलेप’, कुष्ठनाश के लिए श्रेष्ठ।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What name does verse 16 give to this application?",
            ("Darvī-pralepa",
             "दर्वीप्रलेपं प्रवदन्ति: they call it the darvī-pralepa."),
            [("Tuṣodaka", "Tuṣodaka is the husk-water of verse 15, not the name of this application."),
             ("Āḍhaka", "Āḍhaka is a measure named in the verse, not the name of the lepa."),
             ("Karṣa", "Karṣa is a measure (a weight) named in the verse, not the name of the lepa.")],
            "The second line says: they call this lepa the darvī-pralepa.",
            "Verse 16: the lepa is named darvī-pralepa."),
        match(1, "Match each word of verse 16 to its meaning.",
              [["प्रवदन्ति", "they call, declare"],
               ["परम्", "supreme, excellent"],
               ["कुष्ठनिसूदनाय", "for destroying kuṣṭha"],
               ["दर्वीप्रलेपम्", "the application named darvī-pralepa"]],
              "These four words carry the naming and the praise.",
              "प्रवदन्ति = they call; परम् = supreme; कुष्ठनिसूदनाय = for destroying kuṣṭha; दर्वीप्रलेपम् = the darvī-pralepa."),
        fill(2, "The last word of verse 16, meaning 'for destroying kuṣṭha', is ____ (type it in Devanagari).",
             ["कुष्ठनिसूदनाय", "कुष्ठनिषूदनाय"],
             "The verse ends परं कुष्ठनिसूदनाय.",
             "-आय is the dative: 'for'. So कुष्ठनिसूदनाय is 'for the destroying of kuṣṭha'. Some texts may spell it with ष (निषूदन).",
             "Dative -आय = for (the purpose of)."),
        mcq("discriminate", 3, "Which is the right split of कर्षोद्धृतानि?",
            ("कर्ष + उद्धृतानि",
             "अ + उ → ओ, so कर्ष + उद्धृतानि is written कर्षोद्धृतानि."),
            [("कर्षो + द्धृतानि", "द्धृतानि is not a word."),
             ("कर्ष + ओद्धृतानि", "ओद्धृतानि is not a word."),
             ("कर्षः + उद्धृतानि", "A visarga would keep the words apart, not join them as ओ.")],
            "कर्षोद्धृतानि = कर्ष ('karṣa') + उद्धृतानि ('taken out').",
            "अ + उ → ओ: कर्ष + उद्धृतानि → कर्षोद्धृतानि."),
        multi("apply", 4, "Which of these does verse 16 say or imply?",
              [("कर्षोद्धृतानि points back to the powders of verse 15", "Right: it is neuter plural with no noun here, and agrees with चूर्णानि of verse 15."),
               ("The lepa is called darvī-pralepa", "Right: दर्वीप्रलेपं प्रवदन्ति."),
               ("It is called supreme for destroying kuṣṭha", "Right: परं कुष्ठनिसूदनाय."),
               ("The verse says how many karṣas to take", "Karṣa and āḍhaka are named as measures; no number is given."),
               ("The powders are ground in cow's urine", "Cow's urine is in verse 13, not here.")],
              [0, 1, 2],
              "Verse 16 uses the powders of 15, names the lepa, and states its purpose.",
              "Verse 16: powders of 15, darvī-pralepa, supreme against kuṣṭha."),
        mcq("transfer", 5,
            "A made-up phrase reads व्रणनिसूदनाय लेपः (व्रण = wound). Following कुष्ठनिसूदनाय, what is the lepa for?",
            ("For destroying wounds",
             "Same dative: व्रण + निसूदनाय = for the destroying of wounds."),
            [("For a wound that destroys", "In the compound, the destroying is aimed at व्रण; व्रण is not the destroyer."),
             ("Because of a wound", "The ending -आय gives purpose, 'for', not cause."),
             ("Against kuṣṭha", "That is the verse's phrase; the made-up one names व्रण.")],
            "X-निसूदनाय is 'for the destroying of X'. Here X is व्रण (wound). This is a grammar drill, not a medical claim.",
            "X-निसूदनाय = for destroying X.",
            teaches="The dative of -निसूदन names the thing to be destroyed in the first member."),
    ],
}

NOTES_HI["16"] = ("संधियाँ जाँची: कर्ष + उद्धृतानि → कर्षोद्धृतानि (अ + उ → ओ); उद्धृतानि + आढक… → उद्धृतान्याढक… (इ → य् + आ); च + अपि → चापि; "
                  "लेपम् + एतम् → लेपमेतम् (म् अगले स्वर से सटा)। पाठ-दोष: संस्करण ‘निसूदन’ लिखता है, जबकि ‘नि’ के बाद सामान्य वर्तनी ‘निषूदन’ (ष) है; यह "
                  "केवल वर्तनी का सम्भावित भेद है। टिप्पणी के अनुसार ‘निर्दाह’ को जला हुआ अवशेष (भस्म) पढ़ा गया है और रस कैसे बनता है यह नहीं कहा; "
                  "‘कर्षोद्धृतानि’ श्लोक १५ के ‘चूर्णानि’ से जुड़ता है; ‘दर्वी’ नाम की तरह रखा गया है।")

AIDS["16"] = {
    "frame": "क्या: श्लोक १५ के चूर्ण (कर्ष-माप से लिए) · किससे: पलाश-निर्दाह का रस, आढक-माप · नाम: दर्वीप्रलेप · प्रशंसा: कुष्ठनाश के लिए परम।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["पलाशनिर्दाहरसेन", "चापि", "कर्षोद्धृतान्याढकसंमितेन"]},
        {"label": "दूसरी पंक्ति",
         "items": ["दर्वीप्रलेपं", "प्रवदन्ति", "लेपमेतं", "परं", "कुष्ठनिसूदनाय"]}]},
    "sandhi": "अ + उ → ओ: कर्ष + उद्धृतानि → कर्षोद्धृतानि। इ + आ → या: उद्धृतानि + आढक… → उद्धृतान्याढक…। म् + स्वर: लेपम् + एतम् → लेपमेतम्।",
    "anchors": "निसूदन = नि + √सूद् (नाश करना) · प्रवदन्ति ← प्र + √वद् (कहना): ‘वे कहते हैं’ · कर्ष और आढक = माप (कर्ष = तौल; आढक = माप)।",
    "chunks": "पलाशनिर्दाहरसेन चापि | कर्षोद्धृतान्याढकसंमितेन ‖ दर्वीप्रलेपं प्रवदन्ति | लेपमेतं परं कुष्ठनिसूदनाय।",
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "पर्णानि पिष्ट्वा चतुरङ्गुलस्य",
    "question": "What is ground first, with what, and what does the main verb tell one to do?",
    "rule": ("Having ground (पिष्ट्वा) the leaves of caturaṅgula with buttermilk, and then the "
             "leaves of kākamācī, one should rub down (उद्वर्तयेत्) the kuṣṭhas of a man with "
             "an oil-anointed body, and also with aśvahana leaves."),
    "limits": ("The three plant names are kept as given; the verse does not identify them. "
               "The second set of leaves is taken as also ground, which is understood. How the "
               "aśvahana leaves are used is not said: only 'also with leaves'. No quantity."),
    "explain_hi": ("इस श्लोक में पहले पूर्वकालिक क्रिया ‘पिष्ट्वा’ (पीसकर) आती है और मुख्य क्रिया "
                   "‘उद्वर्तयेत्’ (उबटन की तरह मले) बाद में। पहले चतुरङ्गुल के पत्ते तक्र (छाछ) के साथ पीसे जाते हैं, "
                   "फिर ‘अथ’ काकमाची के पत्ते; तेल से चुपड़े शरीर वाले मनुष्य के कुष्ठों पर इन्हें मला जाता है। "
                   "‘अश्वहनच्छदैश्च’ यानी अश्वहन के पत्तों से भी, पर उनका प्रयोग-तरीका नहीं बताया गया। इन तीन "
                   "नामों की पहचान श्लोक नहीं देता।"),
    "hook": "पीसकर (पिष्ट्वा) चतुरङ्गुल-पत्ते छाछ से, फिर काकमाची; तेल-चुपड़े शरीर के कुष्ठ पर उद्वर्तन; अश्वहन-पत्ते भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is the main action ordered by उद्वर्तयेत् in verse 17?",
            ("To rub down the kuṣṭhas of an oil-anointed man",
             "कुष्ठान्युद्वर्तयेत् with तैलाक्तगात्रस्य नरस्य: rub the kuṣṭhas of a man whose body is oil-anointed."),
            [("To make him drink buttermilk",
              "Buttermilk is what the leaves are ground with, not something to drink."),
             ("To burn the leaves to ash", "Nothing is said about burning."),
             ("To give an enema", "No enema is named in this verse.")],
            "The main verb is उद्वर्तयेत्; the earlier verb पिष्ट्वा is only the preparation.",
            "Verse 17: grind the leaves, then rub down the kuṣṭhas."),
        order(1, "Put these four items in the order they stand in verse 17.",
              ["चतुरङ्गुलस्य", "तक्रेण", "काकमाच्याः", "अश्वहनच्छदैः"],
              "Line 1 gives caturaṅgula, then buttermilk, then kākamācī; line 2 ends with the aśvahana leaves.",
              "चतुरङ्गुलस्य → तक्रेण → काकमाच्याः → अश्वहनच्छदैः."),
        fill(2, "The word meaning 'with buttermilk' in line 1 is ____ (type it in Devanagari).",
             ["तक्रेण"],
             "Line 1 reads पर्णानि पिष्ट्वा चतुरङ्गुलस्य तक्रेण.",
             "तक्रेण is the instrumental singular: 'with, by means of buttermilk'.",
             "Instrumental -एन/-एण = with, by means of."),
        mcq("discriminate", 3, "पिष्ट्वा ends in -त्वा. What does the form show?",
            ("Having ground, an action done before the main verb",
             "√पिष् has no prefix here, so the absolutive is -त्वा: 'having ground'."),
            [("One should grind, a command", "A command would be an optative like उद्वर्तयेत्; पिष्ट्वा is a different form."),
             ("The ground leaves, a noun", "A noun would not end in -त्वा."),
             ("Is being ground, a passive", "-त्वा does not make a passive.")],
            "पिष्ट्वा is the absolutive of √पिष् (abs. in the data): 'having ground'. The main verb comes later.",
            "-त्वा on a prefix-less root = 'having done'; the main verb follows."),
        multi("apply", 4, "Which of these does verse 17 say?",
              [("The leaves of caturaṅgula are ground with buttermilk", "Right: पर्णानि पिष्ट्वा चतुरङ्गुलस्य तक्रेण."),
               ("The leaves of kākamācī come next (अथ)", "Right: पर्णान्यथ काकमाच्याः."),
               ("The man's body is anointed with oil", "Right: तैलाक्तगात्रस्य नरस्य."),
               ("Caturaṅgula is the same tree as āragvadha", "The verse does not identify the names; that is tradition, not stated here."),
               ("It is stated how the aśvahana leaves are used", "Only 'also with aśvahana leaves' is said; no method.")],
              [0, 1, 2],
              "Line 1 gives the grinding; line 2 gives the condition of the body, the rubbing and the extra leaves.",
              "Verse 17: grind with buttermilk, rub down; no identification, no method for aśvahana."),
        mcq("transfer", 5,
            "A made-up compound लोध्र + छदैः (lodhra leaves, with). Using the rule of अश्वहन + छदैः, how is it written joined?",
            ("लोध्रच्छदैः",
             "A short vowel before छ takes च्: as in अश्वहनच्छदैः."),
            [("लोध्रछदैः", "After a short vowel the छ is not left single; च् is added."),
             ("लोध्रश्छदैः", "श् is added before च, not here; the added letter is च्."),
             ("लोध्रत्छदैः", "The added letter is च्, not त्.")],
            "अश्वहन ends in a short अ; before छदैः, a च् is added: अश्वहन + छदैः → अश्वहनच्छदैः. So लोध्र + छदैः → लोध्रच्छदैः. This is a grammar drill.",
            "Short vowel + छ → च्छ.",
            teaches="You can now see why leaf-names like -च्छद appear with a doubled sound after a short vowel."),
    ],
}

NOTES_HI["17"] = ("संधियाँ जाँची: पर्णानि + अथ → पर्णान्यथ (इ → य्); कुष्ठानि + उद्वर्तयेत् → कुष्ठान्युद्वर्तयेत् (इ → य्, उ जुड़ा); "
                  "उद्वर्तयेत् + अश्वहन… → उद्वर्तयेदश्वहन… (त् → द् स्वर से पहले); अश्वहन + छदैः → अश्वहनच्छदैः (ह्रस्व स्वर के बाद छ → च्छ); "
                  "छदैः + च → छदैश्च (विसर्ग + च → श्)। ‘पिष्ट्वा’ उपसर्ग-रहित धातु का -त्वा रूप है, पर ‘उद्वर्तयेत्’ में उपसर्ग ‘उद्’ क्रिया के साथ है। "
                  "टिप्पणी के अनुसार तीन नामों की पहचान श्लोक में नहीं है; ‘पिष्ट्वा तक्रेण’ केवल पहले पत्तों के लिए भी पढ़ा जा सकता है।")

AIDS["17"] = {
    "frame": "पहले: चतुरङ्गुल के पत्ते + तक्र, पीसकर · फिर: काकमाची के पत्ते · किस पर: तेल-चुपड़े शरीर के कुष्ठ · क्रिया: उद्वर्तन · और: अश्वहन के पत्तों से भी।",
    "chain": {"steps": [
        "चतुरङ्गुल के पत्ते तक्र से पीसे (पिष्ट्वा)",
        "फिर काकमाची के पत्ते (अथ)",
        "तेल-चुपड़े शरीर के कुष्ठ पर उद्वर्तन",
        "अश्वहन के पत्तों से भी (च)"]},
    "sandhi": "इ → य्: पर्णानि + अथ → पर्णान्यथ; कुष्ठानि + उद्वर्तयेत् → कुष्ठान्युद्वर्तयेत्। ह्रस्व स्वर + छ → च्छ: अश्वहन + छदैः → अश्वहनच्छदैः।",
    "anchors": "उद्वर्तयेत् ← उद् + √वृत् (प्रेरणार्थक): ‘मलना, उबटन करना’ · पिष्ट्वा ← √पिष् (पीसना) · चतुरङ्गुल = चतुर् + अङ्गुल (नाम; श्लोक पहचान नहीं देता)।",
    "contrast": "पिष्ट्वा (पीसकर: पहले की क्रिया, -त्वा) ↔ उद्वर्तयेत् (मुख्य क्रिया: ‘मले’, विधिलिङ्)।",
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "कोलं कुलत्थाः सुरदारुरास्ना",
    "question": "For whom is the pradeha of verse 18, and what is said about its state?",
    "rule": ("Kola, kulattha, suradāru, rāsnā, māṣa, atasī, taila-phala, kuṣṭha, vacā, "
             "śatāhvā, barley flour and a sour substance: these, warm (उष्णानि), are a "
             "pradeha for those afflicted with vāta disorders (वातामयिनाम्)."),
    "limits": ("The edition prints तैलफानि, one syllable short for the line; तैलफलानि is "
               "suggested. Whether 'taila-phala' is one drug or 'oil' and 'fruits' is not "
               "decided. The glosses of kola, māṣa, atasī are conventional, not in the verse. "
               "Here कुष्ठम् is a drug, not the disease."),
    "explain_hi": ("यह श्लोक वात-रोगियों (वातामयिनाम्) के लिए प्रदेह की सामग्री देता है: कोल, कुलत्थ, "
                   "सुरदारु, रास्ना, माष, अतसी, तैलफल, कुष्ठ, वचा, शताह्वा, जौ का चूर्ण और अम्ल। "
                   "‘उष्णानि’ नपुंसक बहुवचन है और पूरी सूची के साथ चलता है: ये गरम हों। यहाँ ‘कुष्ठम्’ रोग नहीं, "
                   "सामग्री का एक औषध है; रोग का नाम ‘वात’ है। मुद्रित पाठ ‘तैलफानि’ है, जो छन्द में "
                   "एक अक्षर कम पड़ता है; ‘तैलफलानि’ पाठ सुझाया गया है। सूची के गुण या मात्रा का वर्णन नहीं है।"),
    "hook": "कोल, कुलत्थ, सुरदारु, रास्ना, माष, अतसी, तैलफल, कुष्ठ, वचा, शताह्वा, यव-चूर्ण, अम्ल: गरम, वात-रोगियों का प्रदेह।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "For whom does verse 18 say this pradeha is meant?",
            ("Those afflicted with vāta disorders",
             "वातामयिनाम् = of those afflicted (आमयिन्) with vāta."),
            [("Those with a headache", "Headache is not named in this verse."),
             ("Those who have taken an emetic", "Nothing about an emetic is said here."),
             ("Those with a skin disease only", "The verse names vāta, not a skin disease; कुष्ठम् is a drug in the list.")],
            "The condition is in the second line: वातामयिनां प्रदेहः.",
            "Verse 18: warm ingredients, a pradeha for vāta sufferers."),
        match(1, "Match each word of verse 18 to its meaning.",
              [["वातामयिनाम्", "of those afflicted with vāta disorders"],
               ["उष्णानि", "warm"],
               ["यवचूर्णम्", "barley flour"],
               ["अम्लम्", "a sour substance"]],
              "These four words give the condition and the state of the ingredients.",
              "वातामयिनाम् = of those with vāta disorders; उष्णानि = warm; यवचूर्णम् = barley flour; अम्लम् = a sour substance."),
        fill(2, "The word in line 2 meaning 'warm' (neuter plural) is ____ (type it in Devanagari).",
             ["उष्णानि"],
             "Line 2 reads यवचूर्णमम्लमुष्णानि वातामयिनां प्रदेहः.",
             "उष्णानि is neuter plural and agrees with the whole list of ingredients: all of them are to be warm.",
             "A neuter plural adjective can stand for a whole list."),
        mcq("discriminate", 3, "In verse 18, कुष्ठम् stands inside a list of ingredients. What is it there?",
            ("A drug, one of the ingredients",
             "The condition is named separately as वातामयिनाम्; so कुष्ठम् is a listed drug."),
            [("The disease the pradeha is meant for", "The disease is vāta (वातामयिनाम्), not kuṣṭha."),
             ("A measure of weight", "Measures in this chapter are named differently (e.g. कर्ष, आढक in verse 16)."),
             ("A method of preparing the paste", "No method word stands here; कुष्ठम् is a name in the list.")],
            "कुष्ठम् is nominative singular neuter, in the same list as वचा, शताह्वा, यवचूर्णम्. The data glosses it as the drug.",
            "Same word, two roles: a drug in verse 18, the disease in verse 16."),
        multi("apply", 4, "Which of these does verse 18 say?",
              [("The pradeha is for those afflicted with vāta disorders", "Right: वातामयिनां प्रदेहः."),
               ("The ingredients are to be warm", "Right: उष्णानि."),
               ("Barley flour is among the ingredients", "Right: यवचूर्णम्."),
               ("The pradeha is for headache", "Headache is not named in verse 18."),
               ("The verse gives the dose of each item", "No quantity is named.")],
              [0, 1, 2],
              "The first line and the start of the second give the items; the end of the second line gives the warmth and the purpose.",
              "Verse 18: a list of ingredients, warm, for vāta sufferers; no dose."),
        mcq("transfer", 5,
            "A made-up phrase reads कुष्ठामयिनां प्रदेहः. Following वातामयिनाम्, for whom is it?",
            ("Those afflicted with kuṣṭha (the disease)",
             "Same compound X-आमयिन्, genitive plural: कुष्ठ + आमयिनाम्."),
            [("Those afflicted with vāta", "That is the verse's phrase; here the first part is कुष्ठ."),
             ("Those who make kuṣṭha", "आमयिन् means afflicted, not maker."),
             ("The drug kuṣṭha itself", "The genitive plural names people, those afflicted, not the drug.")],
            "X-आमयिनाम् = of those afflicted with X; अ + आ → आ makes कुष्ठामयिनाम्. This is a grammar drill.",
            "X-आमयिनाम् = of those afflicted with X.",
            teaches="Once you know X-आमयिन्, any 'illness-name + आमयिनाम्' reads as 'for those with that illness'."),
    ],
}

NOTES_HI["18"] = ("संधियाँ जाँची: वात + आमयिनाम् → वातामयिनाम् (अ + आ → आ); माष + अतसी → माषातसी (अ + अ → आ) सामासिक पद के भीतर; "
                  "यवचूर्णम् + अम्लम् → यवचूर्णमम्लम् (म् अगले स्वर से सटा)। पाठ-दोष: संस्करण ‘तैलफानि’ छापता है, जिससे पंक्ति में 21 अक्षर होते हैं (22 चाहिए); "
                  "‘तैलफलानि’ पाठ सुझाया गया है। ‘तैलफल’ एक द्रव्य है या ‘तैल’ और ‘फल’ अलग, यह तय नहीं। कोल, माष, अतसी के अर्थ परम्परागत हैं, श्लोक में नहीं। "
                  "‘उष्णानि’ पूरी सूची के साथ चलता है; ‘कुष्ठम्’ यहाँ औषध है।")

AIDS["18"] = {
    "frame": "किसके लिए: वात-रोगी (वातामयिन्) · क्या: कोल, कुलत्थ, सुरदारु, रास्ना, माष, अतसी, तैलफल, कुष्ठ, वचा, शताह्वा, यव-चूर्ण, अम्ल · कैसे: उष्ण।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["कोलं", "कुलत्थाः", "सुरदारुरास्नामाषातसीतैलफानि", "कुष्ठम्"]},
        {"label": "दूसरी पंक्ति",
         "items": ["वचा", "शताह्वा", "यवचूर्णमम्लमुष्णानि", "वातामयिनां", "प्रदेहः"]}]},
    "sandhi": "अ + आ → आ: वात + आमयिनाम् → वातामयिनाम्। म् + स्वर: यवचूर्णम् + अम्लम् → यवचूर्णमम्लम्। सूची के भीतर: माष + अतसी → माषातसी।",
    "anchors": "वातामयिनाम् = वात + आमयिन् (जिसे रोग/पीड़ा हो) · उष्णानि = गरम (नपुं०, बहु०) · यवचूर्णम् = यव (जौ) + चूर्णम् (आटा)।",
    "contrast": "कुष्ठम् (इस श्लोक में औषध, सूची में) ↔ वात (रोग की श्रेणी जिसके लिए प्रदेह है)। श्लोक १६ में ‘कुष्ठ’ रोग था; श्लोक १८ में औषध।",
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "आनूपमत्स्यामिषवेसवारैः",
    "question": "Which two vāta-removing pradehas does verse 19 give, and with what is each made?",
    "rule": ("Line 1: a pradeha with warm vesavāras of the flesh of marsh-dwelling animals "
             "and fish removes Vāta. Line 2: a pradeha mixed with four fats, daśamūla and "
             "fragrant drugs destroys Vāta."),
    "limits": ("ānūpa-matsya-āmiṣa could be 'flesh of marsh animals and fish' or 'flesh of "
               "marsh fish'. The four fats are not named here. Daśamūla is a standard group "
               "name; its ten roots are not listed. 'pradehaḥ' in line 2 may also be "
               "construed with line 1."),
    "explain_hi": ("इस श्लोक में वात का नाश करने वाले दो प्रदेह हैं। पहली पंक्ति: दलदली (आनूप) प्राणियों "
                   "और मछली के मांस से बने गरम ‘वेसवार’ (मसालेदार हड्डी-रहित मांस की तैयारी) के साथ "
                   "किया प्रदेह ‘पवनापह’ यानी वायु को हरने वाला है। दूसरी पंक्ति: चार स्नेहों, दशमूल और "
                   "सुगन्धित औषधियों से मिश्रित प्रदेह ‘अनिलह’ है। ‘चतुर्भिः’ चार की संख्या बताता है, पर चार स्नेह कौन-से हैं, "
                   "यह श्लोक नहीं कहता, और दशमूल की दस जड़ें भी यहाँ गिनाई नहीं गईं। पहली पंक्ति का समास दो तरह पढ़ा जा सकता है।"),
    "hook": "गरम वेसवार (आनूप-मत्स्य मांस) = पवनापह प्रदेह; चार स्नेह + दशमूल + गन्धौषध = अनिलह प्रदेह।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "With what is the first-line pradeha of verse 19 made?",
            ("Warm vesavāras of the flesh of marsh animals and fish",
             "आनूपमत्स्यामिषवेसवारैः उष्णैः: with warm vesavāras of marsh-animal and fish flesh."),
            [("Barley flour and buttermilk", "Those are in verse 20, not here."),
             ("Husk-water and powders", "Husk-water is in verse 15, not here."),
             ("Milk and wheat flour", "Not named in this verse.")],
            "Line 1 gives the first preparation and says it removes Vāta (पवनापहः).",
            "Verse 19, line 1: warm vesavāras; pradeha removing Vāta."),
        match(1, "Match each word of verse 19 to its meaning.",
              [["उष्णैः", "with warm (ones)"],
               ["चतुर्भिः", "with four"],
               ["दशमूलमिश्रैः", "mixed with daśamūla"],
               ["गन्धौषधैः", "with fragrant drugs"]],
              "These four words in the plural instrumental describe what the pradehas are made with.",
              "उष्णैः = with warm; चतुर्भिः = with four; दशमूलमिश्रैः = mixed with daśamūla; गन्धौषधैः = with fragrant drugs."),
        fill(2, "The compound ending line 2, which means destroying Vāta, is ____ (type it in Devanagari).",
             ["अनिलहः"],
             "Line 2 ends ... गन्धौषधैश्चानिलहः प्रदेहः.",
             "अनिल means wind (here Vāta) and -हः means destroying; the whole describes the pradeha.",
             "X-हः = that which destroys X."),
        mcq("discriminate", 3, "Which is the right split of वेसवारैरुष्णैः?",
            ("वेसवारैः + उष्णैः",
             "The visarga after ऐ becomes र् before a vowel: वेसवारैः + उष्णैः → वेसवारैरुष्णैः."),
            [("वेसवारैर् + उष्णैः", "The word ends in a visarga (-ः); the र् comes from it, not from a separate word."),
             ("वेसवारै + रुष्णैः", "रुष्णैः is not a word."),
             ("वेसवार + ऐरुष्णैः", "ऐरुष्णैः is not a word.")],
            "वेसवारैरुष्णैः = वेसवारैः ('with vesavāras') + उष्णैः ('with warm').",
            "ऐः + स्वर → ऐर् + स्वर: वेसवारैः + उष्णैः → वेसवारैरुष्णैः."),
        multi("apply", 4, "Which of these does verse 19 say?",
              [("A pradeha with warm vesavāras removes Vāta", "Right: उष्णैः प्रदेहः पवनापहः."),
               ("A second pradeha is mixed with daśamūla", "Right: दशमूलमिश्रैः."),
               ("Both pradehas are called Vāta-removers", "Right: पवनापहः and अनिलहः."),
               ("The four fats are named in this verse", "Only चतुर्भिः (four) is said; the fats are not named."),
               ("The ten roots of daśamūla are listed", "Daśamūla is named as a group; its ten roots are not listed.")],
              [0, 1, 2],
              "Each line names a preparation that removes Vāta; line 2 does not name the four fats or the ten roots.",
              "Verse 19: two Vāta-removing pradehas; the four fats and ten roots are not named."),
        mcq("transfer", 5,
            "A made-up pair of words: उष्णैः + अम्लैः. Following वेसवारैः + उष्णैः, how are they joined?",
            ("उष्णैरम्लैः",
             "ऐः before a vowel becomes ऐर्: उष्णैः + अम्लैः → उष्णैरम्लैः."),
            [("उष्णैःअम्लैः", "A visarga before a vowel (after ऐ) changes to र्; it is not left."),
             ("उष्णैश्अम्लैः", "श् appears before च/छ, not before a vowel."),
             ("उष्णैस्अम्लैः", "स् appears before त/थ, not before a vowel.")],
            "After ऐ, a visarga before a vowel becomes र् and moves to the vowel: उष्णैरम्लैः. This is a grammar drill with invented words.",
            "ऐः + स्वर → ऐर् + स्वर.",
            teaches="Plural instrumental words in -ऐः join with a following vowel as -ऐर्."),
    ],
}

NOTES_HI["19"] = ("संधियाँ जाँची: मत्स्य + आमिष → मत्स्यामिष (अ + आ → आ); वेसवारैः + उष्णैः → वेसवारैरुष्णैः (ऐः + स्वर → ऐर्); पवन + अपहः → पवनापहः "
                  "(अ + अ → आ); स्नेहैः + चतुर्भिः → स्नेहैश्चतुर्भिः (विसर्ग + च → श्); मिश्रैः + गन्ध… → मिश्रैर्गन्ध… (ऐः + घोष → ऐर्); "
                  "गन्ध + औषधैः → गन्धौषधैः (अ + औ → औ); गन्धौषधैः + च → गन्धौषधैश्च; च + अनिलहः → चानिलहः। पाठभेद या पाठ-दोष कोई नहीं। "
                  "टिप्पणी के अनुसार ‘आनूप-मत्स्य-आमिष’ दो तरह पढ़ा जा सकता है; चार स्नेह यहाँ नामित नहीं; दूसरी पंक्ति का ‘प्रदेहः’ पहली पंक्ति से भी जुड़ सकता है।")

AIDS["19"] = {
    "frame": "पहली: गरम वेसवार (आनूप-प्राणी और मछली का मांस) → पवनापह प्रदेह · दूसरी: चार स्नेह + दशमूल + गन्धौषध → अनिलह प्रदेह। (चार स्नेह और दस मूल के नाम यहाँ नहीं।)",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["आनूपमत्स्यामिषवेसवारैरुष्णैः", "प्रदेहः", "पवनापहः", "स्यात्"]},
        {"label": "दूसरी पंक्ति",
         "items": ["स्नेहैश्चतुर्भिर्दशमूलमिश्रैर्गन्धौषधैश्चानिलहः", "प्रदेहः"]}]},
    "sandhi": "ऐः + स्वर → ऐर्: वेसवारैः + उष्णैः → वेसवारैरुष्णैः। ऐः + घोष → ऐर्: मिश्रैः + गन्ध… → मिश्रैर्गन्ध…। विसर्ग + च → श्: स्नेहैः + चतुर्भिः → स्नेहैश्चतुर्भिः।",
    "contrast": "पहली पंक्ति: साधन = गरम वेसवार (मांस-आधारित), फल = पवनापह · दूसरी पंक्ति: साधन = चार स्नेह + दशमूल + गन्धौषध, फल = अनिलह। दोनों वात-नाशक, साधन अलग।",
    "anchors": "पवनापहः = पवन (वायु) + अपहः (दूर करने वाला) · अनिलहः = अनिल (वायु) + हः (नाशक) · तृतीया बहुवचन -ऐः: ‘…के साथ’।",
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "तक्रेण युक्तं यवचूर्णमुष्णम्",
    "question": "What does the first half of verse 20 destroy, and what does the second half prescribe in Vāta?",
    "rule": ("Line 1: warm barley flour with buttermilk and alkali (सक्षारम्) would destroy "
             "pain in the abdomen (जठरे). Line 2: in Vāta (वाते) they prescribe kuṣṭha, "
             "śatāhvā with vacā, and barley flour, with oil and something sour."),
    "limits": ("जठरे is read as 'in the abdomen'; it could also be a disease name. The second "
               "half does not say 'pradeha' or 'external application'; it lists substances "
               "and says 'in Vāta'. Verses 18-19 suggest the context but this verse does not "
               "state it."),
    "explain_hi": ("पहली पंक्ति: जौ का गरम चूर्ण, तक्र (छाछ) से युक्त और ‘सक्षार’ (क्षार सहित), ‘जठरे अर्तिम्’ "
                   "यानी उदर की पीड़ा का नाश करे। दूसरी पंक्ति ‘वाते’ (वात में) के लिए सूची देती है: "
                   "कुष्ठ, वचा के साथ शताह्वा, और जौ का चूर्ण, तेल व खट्टे पदार्थ के साथ; क्रिया ‘उशन्ति’ है, "
                   "‘वे अभीष्ट मानते हैं’। ‘जठरे’ और ‘वाते’ दोनों सप्तमी एकवचन हैं: ‘में’। श्लोक में दूसरी पंक्ति "
                   "‘प्रदेह’ या ‘बाहरी लेप’ शब्द नहीं कहती, केवल द्रव्य और ‘वाते’ कहती है।"),
    "hook": "जौ-चूर्ण + छाछ + क्षार (गरम) = उदर-पीड़ा का नाश; वात में: कुष्ठ, शताह्वा+वचा, यव-चूर्ण, तैल, अम्ल।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "According to the first half of verse 20, what does warm barley flour with buttermilk and alkali destroy?",
            ("Pain in the abdomen",
             "सक्षारमर्तिं जठरे निहन्यात्: it would destroy pain in the abdomen."),
            [("Pain in the flank", "Flank pain is in verse 25, not here."),
             ("Headache", "Headache is not named in this verse."),
             ("Skin itching", "Itching is not named in this verse.")],
            "Line 1 ends अर्तिं जठरे निहन्यात्: pain (अर्ति) in the abdomen (जठर).",
            "Verse 20, line 1: barley flour with buttermilk and alkali, warm, for abdominal pain."),
        order(1, "Put these four words in the order they stand in line 1 of verse 20.",
              ["तक्रेण", "यवचूर्णम्", "उष्णम्", "सक्षारम्"],
              "Line 1 begins तक्रेण युक्तं यवचूर्णमुष्णं सक्षारमर्तिं ...",
              "तक्रेण → यवचूर्णम् → उष्णम् → सक्षारम्."),
        fill(2, "The word meaning 'in the abdomen' in line 1 is ____ (type it in Devanagari).",
             ["जठरे"],
             "Line 1 ends अर्तिं जठरे निहन्यात्.",
             "जठरे is the locative singular: 'in the abdomen'. The locative gives the place where the pain is.",
             "Locative -ए (singular) = in, at."),
        mcq("discriminate", 3, "In line 2, वाते is built like जठरे. What does the ending -ए show?",
            ("Locative singular: in Vāta",
             "वाते = 'in Vāta (disorder)', locative singular."),
            [("Dual: two Vātas", "A dual would need a pair; nothing here points to two."),
             ("Plural subject: the Vātas", "A plural subject would not end in -ए here; and no verb agrees with it."),
             ("Instrumental: by Vāta", "The instrumental sense is with -एन; वाते is a place or condition.")],
            "In the data, वाते is locative singular, like जठरे: 'in Vāta'.",
            "-ए can be a locative singular (in) or a dual (two); the sense decides."),
        multi("apply", 4, "Which of these does verse 20 say?",
              [("Barley flour for pain in the abdomen is joined with buttermilk", "Right: तक्रेण युक्तं ... जठरे."),
               ("It is warm and joined with alkali", "Right: उष्णम् and सक्षारम्."),
               ("In Vāta, kuṣṭha and śatāhvā with vacā are prescribed", "Right: कुष्ठं शताह्वां सवचाम् ... वाते."),
               ("The second half calls the preparation a pradeha", "The word प्रदेह does not appear in the second half."),
               ("The second half names headache", "Headache is not named in verse 20.")],
              [0, 1, 2],
              "Line 1 gives barley flour for abdominal pain; line 2 gives the list for Vāta, without the word pradeha.",
              "Verse 20: two statements; the second does not say pradeha."),
        mcq("transfer", 5,
            "A made-up line reads अर्तिं पार्श्वे निहन्यात् (पार्श्व = flank). Following जठरे, what does it say?",
            ("It would destroy pain in the flank",
             "पार्श्वे is a locative singular like जठरे: 'in the flank'."),
            [("It would destroy pain of two flanks", "The ending -ए here is a locative singular, not a dual; the line does not say two."),
             ("It would destroy pain caused by the flank", "-ए gives a place, not a cause."),
             ("It would destroy the flank", "अर्तिम् (pain) is the object, not the flank.")],
            "Same frame as अर्तिं जठरे निहन्यात्: अर्तिम् is destroyed, and the locative gives the place. This is a grammar drill, not a medical claim.",
            "अर्तिं X-ए निहन्यात् = it would destroy pain in X.",
            teaches="The frame 'अर्तिं + locative + निहन्यात्' tells you where the pain is."),
    ],
}

NOTES_HI["20"] = ("संधियाँ जाँची: यवचूर्णम् + उष्णम् → यवचूर्णमुष्णम् (म् अगले स्वर से सटा); सक्षारम् + अर्तिम् → सक्षारमर्तिम्; "
                  "स + तैल + अम्लम् → सतैलाम्लम् (अ + अ → आ); सतैलाम्लम् + उशन्ति → सतैलाम्लमुशन्ति। पाठभेद या पाठ-दोष कोई नहीं दिया गया। "
                  "टिप्पणी के अनुसार ‘जठरे अर्तिम्’ का सीधा अर्थ ‘उदर में पीड़ा’ है; ‘जठर’ रोग का नाम भी हो सकता है। दूसरी पंक्ति में ‘प्रदेह’ या बाहरी प्रयोग का "
                  "शब्द नहीं है; संदर्भ (श्लोक १८-१९) उसे सुझाता है, श्लोक स्वयं नहीं। ‘सक्षारम्’ का अन्वय ‘यवचूर्णम्’ से है।")

AIDS["20"] = {
    "frame": "पहली: जौ-चूर्ण, गरम, तक्र और क्षार के साथ → उदर की पीड़ा का नाश · दूसरी: वात में कुष्ठ, शताह्वा+वचा, यव-चूर्ण, तैल और अम्ल के साथ अभीष्ट।",
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["तक्रेण", "युक्तं", "यवचूर्णमुष्णं", "सक्षारमर्तिं", "जठरे", "निहन्यात्"]},
        {"label": "दूसरी पंक्ति",
         "items": ["कुष्ठं", "शताह्वां", "सवचां", "यवानां", "चूर्णं", "सतैलाम्लमुशन्ति", "वाते"]}]},
    "sandhi": "म् + स्वर: यवचूर्णम् + उष्णम् → यवचूर्णमुष्णम्; सक्षारम् + अर्तिम् → सक्षारमर्तिम्। अ + अ → आ: स + तैल + अम्लम् → सतैलाम्लम्।",
    "contrast": "जठरे (उदर में: पहली पंक्ति, पीड़ा का स्थान) ↔ वाते (वात में: दूसरी पंक्ति, स्थिति)। दोनों सप्तमी एकवचन, दोनों ‘-ए’।",
    "anchors": "सक्षारम् = स (साथ) + क्षारम् · सवचाम् = स + वचाम् · सतैलाम्लम् = स + तैल + अम्लम् · यवचूर्णम् (समास) ↔ यवानां चूर्णम् (षष्ठी): एक ही ‘जौ का चूर्ण’।",
}

IMAGE_SPECS = {
    ("14", "diagram"): {
        "file": "ch3-lepa-14.svg",
        "alt": "Two columns showing the printed words of verse 14: first line has six words (both, haridrās, of kuṭaja, seed, karañja seed, sumanas shoots) and the second line six (bark, with middle, of hayamāraka, lepa, mixed with tila-kṣāra, should prepare)",
        "type": "split",
        "title": "श्लोक १४: सामग्री और क्रिया",
        "cols": [["पहली पंक्ति", ["उभे", "हरिद्रे", "कुटजस्य", "बीजं", "करञ्जबीजं", "सुमनःप्रवालान्"]],
                 ["दूसरी पंक्ति", ["त्वचं", "समध्यां", "हयमारकस्य", "लेपं", "तिलक्षारयुतं", "विदध्यात्"]]],
    },
    ("19", "contrast"): {
        "file": "ch3-vata-19.svg",
        "alt": "Table of verse 19 with two rows: warm vesavaras of marsh-animal and fish flesh give the pradeha that removes Vata; four fats with dashamula and fragrant drugs give the pradeha that destroys Vata",
        "type": "table",
        "title": "श्लोक १९: दो वात-नाशक प्रदेह",
        "heads": ["साधन", "फल"],
        "rows": [["गरम वेसवार (आनूप-मत्स्य मांस)", "पवनापह प्रदेह"],
                 ["चार स्नेह + दशमूल + गन्धौषध", "अनिलह प्रदेह"]],
    },
}
