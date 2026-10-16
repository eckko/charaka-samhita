from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}

# ---------------------------------------------------------------- unit 70
AUTHORED["70"] = {
    "title": "सुवर्णं समलाः पञ्च लोहाः",
    "question": "What earthly (mineral) substances does this verse list?",
    "rule": ("Gold, five metals with their dross, sands, lime, realgar and "
             "orpiment, gems, salt, red ochre and collyrium. The list "
             "carries on into the first line of verse 71."),
    "limits": ("The verse does not name the five metals; whether ससिकताः "
               "means 'with sands' (a separate item) or 'the metals with "
               "sand' is a reading choice; the verse does not say what any "
               "item is used for."),
    "explain_hi": ("यह श्लोक खनिज द्रव्यों की सूची है; सूची का नाम (भौम "
                   "औषध) अगले श्लोक की पहली पंक्ति में आता है। सुवर्ण, "
                   "मल-सहित पाँच लोह, सिकता, सुधा (चूना), मणियाँ और लवण "
                   "एकवचन या बहुवचन में गिनाए गए हैं। ‘मनःशिलाले’ और "
                   "‘गैरिकाञ्जने’ में अन्त का -ए द्विवचन है: दो-दो वस्तुएँ "
                   "(मनःशिला और आल; गैरिक और अञ्जन)। पाँच लोह के नाम श्लोक "
                   "में नहीं दिए गए हैं।"),
    "hook": ("सोना · पाँच लोह · बालू · चूना · हरताल-मनःशिला (जोड़ा) · मणि · "
             "नमक · गेरू-अञ्जन (जोड़ा)।"),
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 70 lists gold, metals, lime, gems and salt. What kind of substances do these belong to?",
            ("Mineral (earthly) substances",
             "These come from the earth; verse 71 line 1 closes the list as भौम, earthly."),
            [("Animal products", "Animal products were listed in verse 69: dung, skin, horn and so on."),
             ("Plant products", "Plant parts come later, from verse 73."),
             ("Kinds of water", "No water is named in this verse.")],
            "The list is of earthly (mineral) substances; verse 71 line 1 says they are the earthly medicines.",
            "Gold, metals, lime, gems, salt: earthly (mineral) medicines."),
        match(1, "Match each word of the verse to its meaning.",
              [["सुवर्णम्", "gold"], ["सुधा", "lime"], ["लवणम्", "salt"],
               ["मणयः", "gems"]],
              "These four items sit in the list of earthly substances.",
              "सुवर्णम् = gold; सुधा = lime; लवणम् = salt; मणयः = gems."),
        fill(2, "The word for 'gems' is ____ (type it in Devanagari).",
             ["मणयः", "मणयो", "मणय"],
             "मणयः is the plural of मणि, a gem.",
             "मणयः is a plural, so several gems are meant. Items in -इ take -अयः in the plural.",
             "मणयः = gems (plural of मणि)."),
        mcq("discriminate", 3, "Which is the right split of गैरिकाञ्जने?",
            ("गैरिक + अञ्जन, with the dual ending -ए: two items",
             "अ + अ gives आ, and the -ए at the end marks two items (red ochre and collyrium)."),
            [("गैरिकाञ् + जने", "Neither part is a word."),
             ("गैरिक + आञ्जने", "आञ्जने is not a word in this verse."),
             ("गैरिकः + अञ्जनम्", "This would be written गैरिकोऽञ्जनम्, and would not end in -ए.")],
            "गैरिकाञ्जने = गैरिक (red ochre) + अञ्जन (collyrium), a pair joined into one word.",
            "गैरिकाञ्जने = गैरिक + अञ्जन, two items."),
        multi("apply", 4, "Which of these are named in verse 70 itself?",
              [("सुवर्णम्", "Right: gold opens the verse."),
               ("लवणम्", "Right: salt is in the second line."),
               ("मणयः", "Right: gems are in the second line."),
               ("मधूनि", "Honeys are in verse 68, an animal product."),
               ("केशाः", "Head hair is in verse 69, an animal product.")],
              [0, 1, 2],
              "Gold, salt and gems are in this verse; honeys and hair belong to the earlier animal lists.",
              "Verse 70 names gold, salt and gems; honeys and hair come earlier."),
        mcq("transfer", 5,
            "In a list of metals, the joined word रजतताम्रे is a neuter dual like गैरिकाञ्जने. How many items does it name?",
            ("Two",
             "Like गैरिकाञ्जने, the -ए on a neuter pair joined into one word marks two items."),
            [("One", "One item would not take the paired ending."),
             ("Three", "The ending is for two."),
             ("Five", "Five is the count of the metals in the verse, not a dual.")],
            "A dual ending on a joined word means a pair, here रजत and ताम्र.",
            "Neuter dual compound in -ए = two items.",
            teaches="A joined neuter word in dual -ए, as in मनःशिलाले and गैरिकाञ्जने, names two things."),
    ],
}

# ---------------------------------------------------------------- unit 71
AUTHORED["71"] = {
    "title": "भौममौषधमुद्दिष्टम्",
    "question": "How does the verse close the earthly list and divide plant medicine?",
    "rule": ("Those listed are the earthly (भौम) medicines; plant (औद्भिद) "
             "medicine, however, is fourfold: वनस्पति, वीरुध्, वानस्पत्य "
             "and ओषधि."),
    "limits": ("The verse only names the four classes; how each is told "
               "apart comes in verse 72. The first line closes the list "
               "begun in verse 70."),
    "explain_hi": ("पहली पंक्ति पिछली सूची को बन्द करती है: गिनाए गए पदार्थ "
                   "‘भौम’ औषध कहे गए हैं। दूसरी पंक्ति में ‘तु’ (किन्तु) के साथ "
                   "औद्भिद औषध की ओर मुड़ती है, जो ‘चतुर्विध’ (चार प्रकार का) "
                   "है। चार नाम हैं: वनस्पति, वीरुध्, वानस्पत्य, ओषधि। "
                   "पहचान अगले श्लोक में आती है। ‘वीरुद्वानस्पत्यः’ में "
                   "वीरुत् का त् घोष ‘व’ से पहले द् बन गया है।"),
    "hook": "भौम (सूची बन्द) · औद्भिद = चार: वनस्पति, वीरुध्, वानस्पत्य, ओषधि।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "After the earthly medicines, the verse turns to plant medicine (औद्भिद). How does it divide plant medicine?",
            ("Into four classes",
             "The verse says औद्भिदं तु चतुर्विधम्: plant medicine is fourfold."),
            [("Into two classes", "Two is not what the verse says."),
             ("Into three classes", "Threefold is how substance is divided in verse 68 (animal, plant, earthly), not plant medicine."),
             ("Into five classes", "Five is not what the verse says.")],
            "चतुर्विधम् means fourfold: four classes of plant medicine.",
            "Plant medicine is fourfold."),
        match(1, "Match each Devanagari name to its Latin spelling.",
              [["वनस्पतिः", "vanaspati"], ["वीरुत्", "vīrut"],
               ["वानस्पत्यः", "vānaspatya"], ["ओषधिः", "oṣadhi"]],
              "These are the four classes named in the verse.",
              "वनस्पतिः = vanaspati; वीरुत् = vīrut;वानस्पत्यः = vānaspatya; ओषधिः = oṣadhi."),
        fill(2, "The word for 'fourfold' is ____ (type it in Devanagari).",
             ["चतुर्विधम्", "चतुर्विधं"],
             "चतुर्विधम् = चतुर् (four) + विध (kind).",
             "A number followed by -विध means 'of that many kinds': त्रिविधम् in verse 68 is 'threefold', चतुर्विधम् 'fourfold'.",
             "चतुर्विधम् = fourfold."),
        mcq("discriminate", 3, "Which is the right split of वीरुद्वानस्पत्यः?",
            ("वीरुत् + वानस्पत्यः",
             "Final त् becomes द् before the voiced व, so वीरुत् + वानस्पत्यः is written वीरुद्वानस्पत्यः."),
            [("वीरुः + वानस्पत्यः", "A visarga before व would give वीरुर्वानस्पत्यः."),
             ("वीरु + द्वानस्पत्यः", "द्वानस्पत्यः is not a word."),
             ("वीरुद् + आनस्पत्यः", "आनस्पत्यः is not a word.")],
            "वीरुत् (a creeper class, the nominative of वीरुध्) and वानस्पत्यः are two of the four.",
            "वीरुद्वानस्पत्यः = वीरुत् + वानस्पत्यः."),
        mcq("apply", 4,
            "A learner lists the plant classes as वनस्पति, वीरुत्, वानस्पत्य and जङ्गम. Which entry does not belong?",
            ("जङ्गम: it is the animal class of verse 68, not a plant class",
             "The fourth plant class in verse 71 is ओषधि."),
            [("वनस्पति: it is not named in verse 71", "It is the first of the four."),
             ("वीरुत्: it is not named in verse 71", "It is named in line 2."),
             ("वानस्पत्य: it is not named in verse 71", "It is named in line 2.")],
            "जङ्गम belongs to the threefold division of substance (animal, plant, earthly); the plant classes are the four named here.",
            "Plant classes: वनस्पति, वीरुध्, वानस्पत्य, ओषधि."),
        mcq("transfer", 5,
            "An invented line says पार्थिवं तु द्विविधम्, like औद्भिदं तु चतुर्विधम्. What does it say?",
            ("Earthly (substance), however, is twofold",
             "द्वि + विधम् = twofold, and तु marks the turn to a new group."),
            [("Earthly substance has four kinds", "द्वि is two, not four."),
             ("Earthly substance is the same as plants", "तु marks a contrast, not sameness."),
             ("Earthly substance has no kinds", "विधम् names kinds; द्वि gives their number.")],
            "Number + -विधम् gives 'n-fold'; तु signals a turn to a different group.",
            "द्विविधम् = twofold; तु = however.",
            teaches="Number + -विध gives 'n-fold' (द्वि = two, त्रि = three, चतुर् = four), and तु turns the sentence to a new topic."),
    ],
}

# ---------------------------------------------------------------- unit 72
AUTHORED["72"] = {
    "title": "फलैर्वनस्पतिः पुष्पैर्वानस्पत्यः",
    "question": "How does the verse tell the four plant classes apart?",
    "rule": ("Vanaspati is known by fruits; vānaspatya by flowers and also "
             "fruits; oṣadhis end with the ripening of the fruit; vīrudhs "
             "are known by their spreading shoots."),
    "limits": ("The verse does not say that a vanaspati has no flowers; "
               "that is a natural contrast but is not stated. 'Ending with "
               "fruit-ripening' is read as the plant's life ending, as the "
               "Hindi gloss does."),
    "explain_hi": ("पिछले श्लोक के चार नामों की पहचान यहाँ मिलती है। ‘फलैः’, "
                   "‘पुष्पैः’, ‘प्रतानैः’ तृतीया बहुवचन हैं: ‘से’। वनस्पति "
                   "फल से पहचाना जाता है; वानस्पत्य पुष्प से और फल से भी; "
                   "ओषधि ‘फलपाकान्त’ है, यानी फल पकने पर जिसका अन्त हो "
                   "जाता है; वीरुध् ‘प्रतान’ (फैलती शाखाओं) से पहचानी जाती है। "
                   "वनस्पति में पुष्प नहीं होता, यह श्लोक नहीं कहता; वह तुलना "
                   "से समझा जाता है। ‘फलैर्वनस्पतिः’ में विसर्ग घोष ‘व’ से "
                   "पहले र् बना है।"),
    "hook": ("वनस्पति = फल · वानस्पत्य = पुष्प + फल · ओषधि = फल पकने पर अन्त · "
             "वीरुध् = प्रतान (लता)।"),
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which of the four classes does verse 72 say is known by its spreading shoots?",
            ("वीरुध् (creeper)",
             "प्रतानैर्वीरुधः स्मृताः: vīrudhs are known by spreading shoots."),
            [("ओषधि", "Oṣadhis are tied to the ripening of the fruit."),
             ("वनस्पति", "Vanaspatis are known by fruits."),
             ("वानस्पत्य", "Vānaspatyas are known by flowers and also fruits.")],
            "The mark of the वीरुध् is the spreading shoot (प्रतान).",
            "वीरुध् = spreading shoots."),
        match(1, "Match each class to the mark the verse gives for it.",
              [["वनस्पतिः", "known by fruits"],
               ["वानस्पत्यः", "known by flowers and also fruits"],
               ["ओषध्यः", "end with the ripening of the fruit"],
               ["वीरुधः", "known by spreading shoots"]],
              "Each class has one mark in the verse.",
              "वनस्पतिः = fruits; वानस्पत्यः = flowers and fruits; ओषधयः = end when fruit ripens; वीरुधः = spreading shoots."),
        fill(2, "The word for 'by flowers' is ____ (type it in Devanagari).",
             ["पुष्पैः", "पुष्पैर्"],
             "पुष्पैः is the instrumental plural of पुष्प, 'by flowers'.",
             "The ending -ऐः on a word in -अ is the instrumental plural, 'by (them)'. Here it names the mark by which a class is known; before व the visarga turns to र् (पुष्पैर्वानस्पत्यः).",
             "पुष्पैः = by flowers (instrumental plural)."),
        mcq("discriminate", 3, "Which is the right split of फलैरपि?",
            ("फलैः + अपि",
             "A visarga before a vowel becomes र्, so फलैः + अपि is written फलैरपि."),
            [("फलैर + पि", "पि is not a word."),
             ("फलै + अरपि", "अरपि is not a word."),
             ("फलैः + आपि", "आपि is not the word in the verse; the word is अपि, 'also'.")],
            "फलैरपि = फलैः (by fruits) + अपि (also), the 'also fruits' of the vānaspatya.",
            "फलैरपि = फलैः + अपि."),
        mcq("apply", 4,
            "A plant's life ends when its fruit ripens. Which class does verse 72 give it?",
            ("ओषधि",
             "ओषध्यः फलपाकान्ताः: oṣadhis are those whose end is the ripening of the fruit."),
            [("वनस्पति", "Vanaspatis are known by fruits; nothing is said of their end."),
             ("वानस्पत्य", "Vānaspatyas are known by flowers and also fruits."),
             ("वीरुध्", "Vīrudhs are known by spreading shoots.")],
            "फलपाकान्ताः = those whose end (अन्त) is the ripening (पाक) of the fruit (फल).",
            "Life ends at fruit-ripening: ओषधि."),
        mcq("transfer", 5,
            "An invented line says पत्रैः क्षुपः स्मृतः, built like फलैर्वनस्पतिः. By what is a क्षुप known?",
            ("By leaves",
             "पत्रैः is 'by leaves', the same pattern as फलैः 'by fruits': the class is known by that mark."),
            [("By fruits", "The mark named is पत्रैः, leaves."),
             ("By flowers", "Flowers are पुष्पैः, a different word."),
             ("By spreading shoots", "That is प्रतानैः, the mark of the वीरुध्.")],
            "Mark in -ऐः (by ...) + class name + स्मृतः (is known) = the class is known by that mark.",
            "X-ऐः Y स्मृतः = Y is known by X.",
            teaches="A word in -ऐः names the mark 'by which' a class is known; with स्मृतः it reads 'is known by'."),
    ],
}

# ---------------------------------------------------------------- unit 73
AUTHORED["73"] = {
    "title": "मूलत्वक्सारनिर्यास…",
    "question": "Which parts and products of plants does the verse list?",
    "rule": ("Root, bark, heartwood, exudate, stalk, expressed juice, tender "
             "leaves; alkalis, latex, fruit, flower, ash, oils, thorns. The "
             "list continues into verse 74."),
    "limits": ("The verse only lists the parts; 'plant group' is named in "
               "verse 74, which also adds leaves, buds, tubers and sprouts. "
               "The edition notes the variant -नाडस्व- for -नालस्व-."),
    "explain_hi": ("औद्भिद (वनस्पतिज) द्रव्य के अंगों और उत्पादों की सूची "
                   "शुरू होती है। पहली पंक्ति में सात नाम एक ही लम्बे शब्द में "
                   "जुड़े हैं: मूल, त्वक्, सार, निर्यास, नाल, स्वरस, पल्लव। "
                   "दूसरी पंक्ति में क्षार, क्षीर (दूध-जैसा रस), फल, पुष्प, "
                   "भस्म, तैल और कण्टक हैं। वाक्य यहाँ पूरा नहीं होता; "
                   "‘औद्भिदो गणः’ अगले श्लोक में आता है। पाठभेद ‘नाड’ का अर्थ "
                   "वही खोखला डंठल है।"),
    "hook": ("पहली पंक्ति: मूल · त्वक् · सार · निर्यास · नाल · स्वरस · पल्लव; "
             "दूसरी: क्षार · क्षीर · फल · पुष्प · भस्म · तैल · कण्टक।"),
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 73 begins a list of parts of plants used as medicine. Which of these would you expect in it?",
            ("Root",
             "मूल, root, opens the list."),
            [("Hooves", "Hooves belong to the animal list in verse 69."),
             ("Bile", "Bile belongs to the animal list in verse 68."),
             ("Gold", "Gold belongs to the earthly list in verse 70.")],
            "The list is of plant parts; the root opens it.",
            "Verse 73 lists plant parts, starting with root."),
        match(1, "Match each word of the verse to its meaning.",
              [["त्वक्", "bark"], ["सारः", "heartwood"],
               ["पल्लवाः", "tender leaves"], ["कण्टकाः", "thorns"]],
              "These four are part of the first and second lines.",
              "त्वक् = bark; सारः = heartwood; पल्लवाः = tender leaves; कण्टकाः = thorns."),
        fill(2, "The word for 'flower' in the second line is ____ (type it in Devanagari).",
             ["पुष्पम्", "पुष्पं"],
             "पुष्पम् sits between फलम् (fruit) and भस्म (ash).",
             "पुष्पम् ends in -म्: a neuter singular, one item in a list of separate words.",
             "पुष्पम् = flower."),
        mcq("discriminate", 3,
            "The edition notes a variant -नाडस्व- for -नालस्व- in the first line. What does the card say about it?",
            ("Same sense: नाड and नाल both mean the hollow stalk",
             "The note says नाड ~ नाल, 'hollow stalk': the meaning does not change."),
            [("नाड is a different part, such as the root", "The root is already named, as मूल."),
             ("The verse is then about animals", "Nothing in the variant changes the plant list."),
             ("The list then has one item fewer", "The variant replaces a word with a near-equivalent; it adds or removes nothing.")],
            "A variant that means the same thing does not change the list.",
            "नाल/नाड = hollow stalk; no change in sense."),
        multi("apply", 4, "Which of these are named in verse 73 itself?",
              [("मूलम् (root)", "Right: the list begins with मूल."),
               ("निर्यासः (exudate)", "Right: it is in the first line."),
               ("कण्टकाः (thorns)", "Right: it closes the second line."),
               ("कन्दाः (tubers)", "Tubers come in verse 74."),
               ("शुङ्गाः (leaf-buds)", "Leaf-buds come in verse 74.")],
              [0, 1, 2],
              "Root, exudate and thorns are in verse 73; tubers and leaves come in verse 74, where the list ends.",
              "Verse 73: root, exudate, thorns; verse 74: tubers, leaves."),
        mcq("transfer", 5,
            "An invented verse reads पर्णं मूलं फलं पुष्पम् and stops, with no verb. By the pattern of verse 73, what should a reader expect?",
            ("The sentence goes on in the next verse",
             "Verse 73 also gives only a list; its closing words come in verse 74."),
            [("The verse is damaged", "A list that runs on into the next verse is normal here."),
             ("The verse is a complete prayer", "A bare list is not a prayer."),
             ("The words mean nothing without a verb", "The list says what the items are; the verse that follows says what group they form.")],
            "Verse 73 lists the items; verse 74 supplies the closing words 'this is the plant group'.",
            "A verse may be only a list, completed in the next.",
            teaches="A list may fill a whole verse and be completed by words in the next; when a verse has no verb, look at the one after."),
    ],
}

# ---------------------------------------------------------------- unit 74
AUTHORED["74"] = {
    "title": "पत्राणि शुङ्गाः कन्दाश्च",
    "question": "How does the verse close the plant list and give the mūlinī and phalinī counts?",
    "rule": ("Leaves, leaf-buds, tubers and sprouts end the list: this is "
             "the plant group. Mūlinīs (root-drugs) are sixteen; phalinīs "
             "(fruit-drugs) are twenty less one."),
    "limits": ("The verse gives the counts but not the names; the names of "
               "the mūlinīs follow in verses 77-78. षोडशैकोना is split so "
               "that षोडश goes with मूलिन्यः and एकोना with विंशतिः."),
    "explain_hi": ("पहली पंक्ति श्लोक ७३ की सूची पूरी करती है: पत्र, शुंग, कन्द "
                   "और प्ररोह भी, और इन सबको ‘औद्भिद गण’ (वनस्पति-वर्ग) कहती है। "
                   "दूसरी पंक्ति गिनती देती है। ‘मूलिनी’ वे पौधे हैं जिनकी जड़ "
                   "प्रयुक्त होती है, ‘फलिनी’ जिनका फल। मूलिनी सोलह हैं। फलिनी "
                   "‘विंशतिः एकोना’ हैं, यानी बीस में एक कम (उन्नीस)। ‘षोडशैकोना’ = "
                   "षोडश + एकोना, जिसमें अ + ए मिलकर ऐ बनता है।"),
    "hook": ("औद्भिद गण: पत्र · शुंग · कन्द · प्ररोह। मूलिनी = १६; "
             "फलिनी = २० − १ = १९।"),
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The verse names two kinds of drug-plants, मूलिनी and फलिनी. What do their names point to?",
            ("The part used: root (मूल) and fruit (फल)",
             "मूलिनी is built on मूल, root; फलिनी on फल, fruit."),
            [("The leaf and the flower", "Leaves and flowers are not what the names are built on."),
             ("The bark and the sap", "Bark and sap are not what the names are built on."),
             ("The tuber and the sprout", "Those are named as parts of the plant group in line 1.")],
            "मूलिनी = root-drug; फलिनी = fruit-drug.",
            "मूलिनी = root used; फलिनी = fruit used."),
        match(1, "Match each word of the verse to its meaning.",
              [["मूलिन्यः", "root-drugs"], ["फलिन्यः", "fruit-drugs"],
               ["कन्दाः", "tubers"], ["शुङ्गाः", "leaf-buds"]],
              "The first two are the drug-plants counted in line 2; the others close the list in line 1.",
              "मूलिन्यः = root-drugs; फलिन्यः = fruit-drugs; कन्दाः = tubers; शुङ्गाः = leaf-buds."),
        fill(2, "The word for 'tubers' is ____ (type it in Devanagari).",
             ["कन्दाः", "कन्दा"],
             "कन्दाः are the tubers, the third item of the first line.",
             "कन्दाः is a masculine plural; च follows it and joins it with the next item, प्ररोहाः.",
             "कन्दाः = tubers."),
        mcq("discriminate", 3,
            "On the card's reading of षोडशैकोना, how does the verse give the number of फलिनी?",
            ("Twenty less one (nineteen)",
             "फलिन्यो विंशतिः … एकोना: twenty, less by one."),
            [("Exactly twenty", "एकोना takes one away from twenty."),
             ("Sixteen less one", "षोडश (sixteen) goes with the मूलिनी; एकोना goes with twenty."),
             ("Twenty-one", "एकोना means 'less by one', not 'plus one'.")],
            "षोडश goes with मूलिन्यः, and एकोना with विंशतिः; so 16 mūlinīs and 19 phalinīs.",
            "मूलिनी 16; फलिनी 20 − 1 = 19."),
        multi("apply", 4, "Which of these items are named in verse 74 itself?",
              [("पत्राणि (leaves)", "Right: it opens the verse."),
               ("कन्दाः (tubers)", "Right: it is in line 1."),
               ("प्ररोहाः (sprouts)", "Right: it ends the list."),
               ("कण्टकाः (thorns)", "Thorns are the last item of verse 73."),
               ("क्षीरम् (latex)", "Latex is in verse 73.")],
              [0, 1, 2],
              "Verse 74 names leaves, tubers and sprouts (and leaf-buds); thorns and latex are in verse 73.",
              "Verse 74 line 1: पत्र, शुंग, कन्द, प्ररोह."),
        mcq("transfer", 5,
            "An invented line has मूलिन्यः त्रिंशदेकोनाः, built like एकोना विंशतिः. By that pattern, how many mūlinīs?",
            ("Twenty-nine",
             "त्रिंशत् (thirty) with एकोन (less by one) gives 29."),
            [("Thirty-one", "एकोन takes away one."),
             ("Thirty", "एकोन takes away one."),
             ("Twenty-one", "One is taken from thirty, not nine.")],
            "Number + एकोन(ा) = that number less one.",
            "त्रिंशदेकोन = 30 − 1 = 29.",
            teaches="एकोन / एकोना after a number means 'that number less one', as in विंशतिः एकोना = nineteen."),
    ],
}

# ---------------------------------------------------------------- unit 75
AUTHORED["75"] = {
    "title": "महास्नेहाश्च चत्वारः",
    "question": "Which four groups does the verse count, and how many in each?",
    "rule": ("Four mahāsnehas (great unctuous substances), five salts, "
             "eight urines and eight milks are enumerated."),
    "limits": ("The verse only gives counts; it does not name the "
               "items in any group."),
    "explain_hi": ("यह श्लोक चार वर्गों की गिनती देता है: महास्नेह चार, "
                   "लवण पाँच, मूत्र आठ और पयस् (दूध) आठ। केवल गिनती है; "
                   "नाम इस श्लोक में नहीं हैं। ‘पञ्चैव’ = पञ्च + एव (अ + ए → ऐ); "
                   "‘अष्टावेव’ = अष्टौ + एव, जहाँ औ स्वर से पहले आव् बन जाता है। "
                   "‘एव’ यहाँ बल देता है: ‘ठीक पाँच’, ‘उतने ही आठ’।"),
    "hook": "महास्नेह ४ · लवण ५ · मूत्र ८ · दूध ८ (केवल गिनती)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 75 counts four groups of medicinal substances. Which of these is NOT counted there?",
            ("Gems",
             "Gems (मणयः) are in verse 70, in the earthly list; verse 75 does not count them."),
            [("Salts", "Salts are counted as five."),
             ("Urines", "Urines are counted as eight."),
             ("Milks", "Milks are counted as eight.")],
            "Verse 75 counts mahāsnehas, salts, urines and milks.",
            "Counted: mahāsneha, salts, urines, milks."),
        match(1, "Match each word of the verse to its meaning.",
              [["महास्नेहाः", "great unctuous substances"],
               ["लवणानि", "salts"], ["मूत्राणि", "urines"],
               ["पयांसि", "milks"]],
              "These are the four groups counted.",
              "महास्नेहाः = great unctuous substances; लवणानि = salts; मूत्राणि = urines; पयांसि = milks."),
        fill(2, "The word for 'four' is ____ (type it in Devanagari).",
             ["चत्वारः", "चत्वार"],
             "चत्वारः goes with महास्नेहाः.",
             "चत्वारः is the masculine plural of 'four', agreeing with the masculine plural महास्नेहाः.",
             "चत्वारः = four."),
        mcq("discriminate", 3, "Which is the right split of पञ्चैव?",
            ("पञ्च + एव",
             "अ + ए joins as ऐ, so पञ्च + एव is written पञ्चैव."),
            [("पञ्चै + व", "व is not a word."),
             ("पञ्च + ऐव", "ऐव is not a word; the word is एव."),
             ("पञ्चे + एव", "ए + ए would not give ऐ.")],
            "पञ्चैव = पञ्च (five) + एव (just), 'just five'.",
            "पञ्चैव = पञ्च + एव."),
        mcq("apply", 4,
            "A learner says the verse gives eight salts. What is the correction?",
            ("Salts are five; eight is the count of urines and of milks",
             "पञ्चैव लवणानि: five salts; अष्टौ मूत्राणि … अष्टावेव पयांसि: eight urines and eight milks."),
            [("The verse gives salts as four", "Four is the count of the mahāsnehas."),
             ("The verse gives no count for salts", "It says पञ्चैव लवणानि."),
             ("Eight is correct", "Salts are five.")],
            "Counts in verse 75: mahāsneha 4, salts 5, urines 8, milks 8.",
            "Salts = five."),
        mcq("transfer", 5,
            "Join नौ + एव by the rule seen in अष्टौ + एव → अष्टावेव. What is the result?",
            ("नावेव",
             "Final औ before a vowel becomes आव्, as in अष्टावेव."),
            [("नौएव", "The two words are joined by sandhi, not simply set side by side."),
             ("नवेव", "औ becomes आव्, not अव्."),
             ("नैव", "That is न + एव, a different word.")],
            "औ before a vowel becomes आव्.",
            "औ + vowel → आव् + vowel.",
            teaches="Final -औ before a vowel turns into आव्, so अष्टौ + एव is अष्टावेव."),
    ],
}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "शोधनार्थाश्च षड् वृक्षाः",
    "question": "What does the verse add, and who does it call a knower of the science?",
    "rule": ("Six trees for purification were pointed out by Punarvasu. "
             "He who knows how to apply these in disorders is a "
             "वेदवित्, a knower of the science."),
    "limits": ("The six trees are not named here; 'these' (एतान्) most "
               "naturally covers the items listed since verse 74, but the "
               "verse does not mark the exact limit; वेद here is read as "
               "the medical science."),
    "explain_hi": ("सूची के अन्त में एक और वर्ग जुड़ता है: शोधन (शुद्धि) के लिए छह "
                   "वृक्ष, जो पुनर्वसु द्वारा बताए गए हैं। पाठ-टिप्पणी पुनर्वसु को "
                   "आत्रेय कहती है। फिर श्लोक वैद्य की कसौटी देता है: जो इन सबको "
                   "विकारों में प्रयोग करना जानता है, वही ‘वेदवित्’ है। कसौटी केवल "
                   "सूची जानना नहीं, ‘संयोक्तुम्’ यानी ठीक प्रयोग करना है। "
                   "‘षड् वृक्षाः’ में षट् का ट् घोष ‘व’ से पहले ड् बना है।"),
    "hook": "छह शोधन-वृक्ष (पुनर्वसु) · जो विकारों में प्रयोग जाने = वेदवित्।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "A verse praises someone who knows how to use remedies in disorders. What title do you expect it to give him?",
            ("A knower of the science",
             "The verse says स वेदवित्, he is a knower of the science."),
            [("A king", "Nothing in the verse concerns a king."),
             ("A patient", "He applies the remedies; he is not the one treated."),
             ("A student only", "The verse speaks of knowing how to apply, not of studying.")],
            "वेदवित् = veda-vit, 'knower of the science'.",
            "Knowing how to apply remedies in disorders = वेदवित्."),
        match(1, "Match each word of the verse to its meaning.",
              [["शोधनार्थाः", "meant for purification"],
               ["वृक्षाः", "trees"], ["विकारेषु", "in disorders"],
               ["संयोक्तुम्", "how to apply"]],
              "These four carry the point of the verse.",
              "शोधनार्थाः = meant for purification; वृक्षाः = trees; विकारेषु = in disorders; संयोक्तुम् = how to apply."),
        fill(2, "The word for 'knower of the science' is ____ (type it in Devanagari).",
             ["वेदवित्", "वेदवित"],
             "वेदवित् = वेद (science) + वित् (knower).",
             "-वित् at the end of a compound means 'one who knows': वेदवित् is 'one who knows the science'.",
             "वेदवित् = knower of the science."),
        mcq("discriminate", 3, "Which is the right split of षड् वृक्षाः?",
            ("षट् + वृक्षाः",
             "Final ट् becomes ड् before the voiced व, so षट् + वृक्षाः is written षड् वृक्षाः."),
            [("षः + वृक्षाः", "That would be written षो वृक्षाः."),
             ("षड् + ऋक्षाः", "The word in the verse is वृक्षाः, trees."),
             ("षण् + वृक्षाः", "The number is षट्, six.")],
            "षट् (six) + वृक्षाः (trees): six trees.",
            "षड् वृक्षाः = षट् + वृक्षाः."),
        mcq("apply", 4,
            "By verse 76, who is a वेदवित्?",
            ("One who knows how to apply these in disorders",
             "यो वेत्ति संयोक्तुं विकारेषु स वेदवित्."),
            [("One who can recite the whole list", "The verse speaks of applying, not of reciting."),
             ("One who owns the six trees", "Owning is not mentioned."),
             ("Only Punarvasu", "The verse speaks of anyone who knows how to apply them.")],
            "The test is knowing how to apply (संयोक्तुम्) in disorders (विकारेषु).",
            "Knowing how to apply, not just the list."),
        mcq("transfer", 5,
            "An invented line says स वेत्ति पठितुम्, built like वेत्ति संयोक्तुम्. What does it mean?",
            ("He knows how to read",
             "वेत्ति + a word in -तुम् (the infinitive) = 'knows how to ...'."),
            [("He read yesterday", "वेत्ति is present, 'knows', and -तुम् is not a past ending."),
             ("He does not know the text", "Nothing negates वेत्ति."),
             ("He wished to read", "That would need a verb of wishing; वेत्ति is 'knows'.")],
            "वेत्ति plus the infinitive in -तुम् means 'knows how to'.",
            "वेत्ति + -तुम् = knows how to.",
            teaches="A verb of knowing with an infinitive in -तुम् reads 'knows how to ...', as in वेत्ति संयोक्तुम्."),
    ],
}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "हस्तिदन्ती हैमवती",
    "question": "Which plant names open the list of the sixteen mūlinīs?",
    "rule": ("Hastidantī, haimavatī, śyāmā, trivṛt, adhoguḍā, saptalā, the "
             "one named śvetā, pratyakśreṇī and gavākṣī: the first nine "
             "names; the list continues in verse 78."),
    "limits": ("The verse gives names only. That they are the sixteen "
               "mūlinīs rests on the neighbouring verses (74, 78); the text "
               "gives no botanical identification."),
    "explain_hi": ("श्लोक ७४ ने मूलिनी की संख्या सोलह बताई थी; अब उनके नाम शुरू "
                   "होते हैं (सूची श्लोक ७८ तक चलती है)। इस श्लोक में नौ नाम हैं: "
                   "हस्तिदन्ती, हैमवती, श्यामा, त्रिवृत्, अधोगुडा, सप्तला, श्वेता, "
                   "प्रत्यक्श्रेणी, गवाक्षी। ‘श्वेतनामा’ का अर्थ है ‘श्वेता नाम "
                   "वाली’। ‘त्रिवृदधोगुडा’ में त्रिवृत् का त् स्वर ‘अ’ से पहले द् बन "
                   "गया है। नामों की वनस्पति-पहचान श्लोक नहीं देता।"),
    "hook": "हस्तिदन्ती · हैमवती · श्यामा · त्रिवृत् · अधोगुडा · सप्तला · श्वेता · प्रत्यक्श्रेणी · गवाक्षी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 74 counted sixteen mūlinīs (root-drugs) without naming them. What do you expect verse 77 to give?",
            ("The first names of the sixteen mūlinīs",
             "The names begin here and run on into verse 78."),
            [("The names of the five salts", "The five salts are only counted, in verse 75."),
             ("The eight urines", "Only the count of the urines is given, in verse 75."),
             ("The four mahāsnehas", "Only the count is given, in verse 75.")],
            "Verse 74 gives the count; verses 77-78 give the names.",
            "Verse 77 begins the names of the sixteen mūlinīs."),
        order(1, "Put these four plant names in the order of verse 77.",
              ["हस्तिदन्ती", "हैमवती", "श्यामा", "त्रिवृत्"],
              "These are the first four names of the verse.",
              "हस्तिदन्ती → हैमवती → श्यामा → त्रिवृत्."),
        fill(2, "The plant named right after त्रिवृत् is ____ (type it in Devanagari).",
             ["अधोगुडा", "त्रिवृदधोगुडा"],
             "In the verse the two are written together: त्रिवृदधोगुडा.",
             "The word space is lost by sandhi: त्रिवृत् + अधोगुडा → त्रिवृदधोगुडा.",
             "त्रिवृत् is followed by अधोगुडा."),
        mcq("discriminate", 3, "Which is the right split of त्रिवृदधोगुडा?",
            ("त्रिवृत् + अधोगुडा",
             "Final त् becomes द् before a vowel, so त्रिवृत् + अधोगुडा is written त्रिवृदधोगुडा."),
            [("त्रिवृद् + धोगुडा", "धोगुडा is not a word."),
             ("त्रिवृ + दधोगुडा", "दधोगुडा is not a word."),
             ("त्रिवृः + अधोगुडा", "A visarga before अ would give त्रिवृरधोगुडा, not द.")],
            "Two plant names: त्रिवृत् and अधोगुडा.",
            "त्रिवृदधोगुडा = त्रिवृत् + अधोगुडा."),
        multi("apply", 4, "Which of these names are in verse 77 itself?",
              [("श्यामा", "Right: the third name."),
               ("सप्तला", "Right: the sixth name."),
               ("गवाक्षी", "Right: it closes the verse."),
               ("बिम्बी", "बिम्बी is named in verse 78."),
               ("क्षीरिणी", "क्षीरिणी is named in verse 78.")],
              [0, 1, 2],
              "The first nine names are in verse 77; बिम्बी and क्षीरिणी follow in verse 78.",
              "श्यामा, सप्तला, गवाक्षी are in verse 77."),
        mcq("transfer", 5,
            "A new text names a plant सुवृत् followed by अमला. By the rule in त्रिवृत् + अधोगुडा, how is it written?",
            ("सुवृदमला",
             "Final त् becomes द् before a vowel, as in त्रिवृदधोगुडा."),
            [("सुवृतमला", "त् should become द् before the vowel."),
             ("सुवृधमला", "The change is to द्, not ध्."),
             ("सुवृत् अमला", "In sandhi the two are joined into one word.")],
            "Final त् before a vowel becomes द्.",
            "त् + vowel → द् + vowel.",
            teaches="A word ending in त् changes it to द् when a vowel follows, so त्रिवृत् + अधोगुडा is त्रिवृदधोगुडा."),
    ],
}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "ज्योतिष्मती च बिम्बी च",
    "question": "Which seven names complete the sixteen mūlinīs?",
    "rule": ("Jyotiṣmatī, bimbī, śaṇapuṣpī, viṣāṇikā, ajagandhā, dravantī "
             "and kṣīriṇī, the sixteenth here."),
    "limits": ("Names only, no botanical identification. षोडशी, 'the "
               "sixteenth', is the word that closes the count with verse "
               "77's nine."),
    "explain_hi": ("यह श्लोक सूची पूरी करता है: ज्योतिष्मती, बिम्बी, शणपुष्पी, "
                   "विषाणिका, अजगन्धा, द्रवन्ती, और क्षीरिणी। ‘षोडशी’ का अर्थ "
                   "‘सोलहवीं’ है, यानी क्षीरिणी इस सूची में सोलहवें स्थान पर है। "
                   "श्लोक ७७ के नौ और यहाँ के सात मिलकर सोलह होते हैं, जो श्लोक ७४ "
                   "की संख्या से मेल खाता है। ‘क्षीरिणी चात्र’ = क्षीरिणी च + अत्र, "
                   "जहाँ च और अत्र का अ मिलकर आ बनता है।"),
    "hook": "ज्योतिष्मती · बिम्बी · शणपुष्पी · विषाणिका · अजगन्धा · द्रवन्ती · क्षीरिणी (सोलहवीं)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "A list of sixteen names ends with क्षीरिणी चात्र षोडशी. What does the last word do?",
            ("It marks क्षीरिणी as the sixteenth item, closing the list",
             "षोडशी = 'the sixteenth' (feminine, like क्षीरिणी)."),
            [("It begins a second list of sixteen", "The sixteenth item closes this list."),
             ("It says क्षीरिणी is a disease", "षोडशी is a number word, not a disease."),
             ("It names क्षीरिणी as the first of sixteen", "षोडशी is the sixteenth, not the first.")],
            "षोडशी is the ordinal 'sixteenth', and it agrees with क्षीरिणी.",
            "षोडशी = the sixteenth."),
        match(1, "Match each Devanagari name to its Latin spelling.",
              [["ज्योतिष्मती", "Jyotiṣmatī"], ["बिम्बी", "Bimbī"],
               ["शणपुष्पी", "Śaṇapuṣpī"], ["विषाणिका", "Viṣāṇikā"]],
              "Reading these names in Devanagari is the point.",
              "ज्योतिष्मती = Jyotiṣmatī; बिम्बी = Bimbī; शणपुष्पी = Śaṇapuṣpī; विषाणिका = Viṣāṇikā."),
        fill(2, "The last plant named in the verse is ____ (type it in Devanagari).",
             ["क्षीरिणी"],
             "क्षीरिणी is the sixteenth, closing the list.",
             "The ordinal षोडशी ('sixteenth') is attached to it.",
             "क्षीरिणी = the last, sixteenth plant."),
        mcq("discriminate", 3, "Which is the right split of चात्र?",
            ("च + अत्र",
             "अ + अ joins as आ, so च + अत्र is written चात्र."),
            [("चा + त्र", "त्र is not a word."),
             ("च + आत्र", "आत्र is not a word here; the word is अत्र, 'here'."),
             ("चात + र", "Neither part is a word.")],
            "चात्र = च (and) + अत्र (here).",
            "चात्र = च + अत्र."),
        multi("apply", 4, "Which of these names are in verse 78 itself?",
              [("बिम्बी", "Right: the second name."),
               ("अजगन्धा", "Right: the fifth name."),
               ("द्रवन्ती", "Right: the sixth name."),
               ("हैमवती", "हैमवती is named in verse 77."),
               ("गवाक्षी", "गवाक्षी is named in verse 77.")],
              [0, 1, 2],
              "Verse 78 gives the last seven names; हैमवती and गवाक्षी are in verse 77.",
              "बिम्बी, अजगन्धा, द्रवन्ती are in verse 78."),
        mcq("transfer", 5,
            "By the rule in च + अत्र → चात्र, join च + अस्ति. What is the result?",
            ("चास्ति",
             "अ + अ gives आ, as in चात्र."),
            [("चअस्ति", "The two words are joined by sandhi."),
             ("चेस्ति", "अ + अ gives आ, not ए."),
             ("चौस्ति", "अ + अ gives आ, not औ.")],
            "A final अ and an initial अ merge into आ.",
            "अ + अ → आ.",
            teaches="When a word ending in अ meets one beginning with अ, the two merge into one long आ."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "शणपुष्पी च बिम्बी च",
    "question": "Which of the mūlinīs are for emesis and which for head-purgation?",
    "rule": ("Śaṇapuṣpī, bimbī and haimavatī are used in emesis; śvetā "
             "and jyotiṣmatī are to be used in head-purgation "
             "(śīrṣavirecana)."),
    "limits": ("'Are used' is supplied from the single form योज्या; the "
               "verse does not say why each plant suits its treatment."),
    "explain_hi": ("अब पिछली सूची के पाँच पौधों का प्रयोग बताया जाता है (श्लोक ८० बाकी ग्यारह को विरेचन में रखता है)। छर्दन (वमन) में "
                   "शणपुष्पी, बिम्बी और हैमवती; शीर्षविरेचन (सिर का शोधन) में "
                   "श्वेता और ज्योतिष्मती। ‘छर्दने’ और ‘शीर्षविरेचने’ सप्तमी हैं: "
                   "‘में’। ‘योज्या’ का अर्थ ‘प्रयोग की जानी चाहिए’ है। ‘च्छर्दने’ में "
                   "च + छर्दने के बीच छ दुगुना हो जाता है, और ‘हैमवत्यपि’ = "
                   "हैमवती + अपि, जहाँ ई यण् होकर य् बनती है।"),
    "hook": "वमन: शणपुष्पी · बिम्बी · हैमवती। शीर्षविरेचन: श्वेता · ज्योतिष्मती।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 79 the word छर्दने names a treatment. Which one?",
            ("Emesis (vomiting)",
             "छर्दन is emesis; छर्दने is its locative, 'in emesis'."),
            [("Head-purgation", "That is शीर्षविरेचने, in the second line."),
             ("Purgation of the bowels", "That is विरेचन, named in verse 80."),
             ("Bathing", "No bathing is mentioned.")],
            "छर्दने = in emesis; शीर्षविरेचने = in head-purgation.",
            "छर्दने = in emesis."),
        match(1, "Match each word of the verse to its meaning.",
              [["छर्दने", "in emesis"],
               ["शीर्षविरेचने", "in head-purgation"],
               ["योज्या", "to be used"],
               ["श्वेता", "a plant, śvetā"]],
              "These words carry the use of each plant.",
              "छर्दने = in emesis; शीर्षविरेचने = in head-purgation; योज्या = to be used; श्वेता = a plant."),
        fill(2, "The word for 'in emesis' is ____ (type it in Devanagari).",
             ["छर्दने", "च्छर्दने"],
             "छर्दने is the locative of छर्दन, written च्छर्दने after च.",
             "A word in -ए can be a locative, 'in (a treatment)'. After च the initial छ is doubled, so the verse writes च्छर्दने.",
             "छर्दने = in emesis."),
        mcq("discriminate", 3, "Which is the right split of च्छर्दने?",
            ("च + छर्दने",
             "After च the initial छ doubles, so च + छर्दने is written च्छर्दने."),
            [("च्छ + र्दने", "र्दने is not a word."),
             ("चि + छर्दने", "चि is not the word in the verse; it is च, 'and'."),
             ("च + चर्दने", "The word is छर्दने, with छ.")],
            "च्छर्दने = च ('and') + छर्दने ('in emesis').",
            "च्छर्दने = च + छर्दने."),
        mcq("apply", 4,
            "A physician needs a plant for head-purgation. Which one does verse 79 give?",
            ("ज्योतिष्मती",
             "श्वेता ज्योतिष्मती चैव योज्या शीर्षविरेचने."),
            [("बिम्बी", "Bimbī is for emesis."),
             ("शणपुष्पी", "Śaṇapuṣpī is for emesis."),
             ("हैमवती", "Haimavatī is for emesis.")],
            "Head-purgation: śvetā and jyotiṣmatī; the other three are for emesis.",
            "Head-purgation: श्वेता, ज्योतिष्मती."),
        mcq("transfer", 5,
            "An invented line says बला च पटोली च विरेचने योज्ये. By the pattern of verse 79, what does विरेचने tell you?",
            ("The treatment in which the two plants are to be used",
             "A locative in -ए names the treatment, as छर्दने does in verse 79."),
            [("The name of a third plant", "A word in -ए after the plants names where they are used."),
             ("Who uses the plants", "A locative names a situation, not a person."),
             ("When the plants grow", "Nothing in the pattern gives a growing season.")],
            "Plants + treatment in -ए + योज्य = plants to be used in that treatment.",
            "Locative -ए = the treatment in which they are used.",
            teaches="A locative in -ए beside योज्य names the treatment in which the plants are to be used."),
    ],
}


NOTES_HI = {
    "70": "विश्वास: मध्यम। ‘ससिकताः’ को अलग वस्तु ‘बालू’ पढ़ा गया है; यह ‘बालू-सहित (लोह)’ विशेषण भी हो सकता है। ‘पञ्च लोहाः’ के नाम श्लोक में नहीं हैं (परम्परा से चाँदी, ताँबा, सीसा, रांगा, लोहा माने जाते हैं, पर वह इस श्लोक का कथन नहीं)। ‘आल’ = हरताल। ‘मनःशिलाले’ और ‘गैरिकाञ्जने’ द्विवचन के जोड़े हैं। सूची श्लोक ७१ की पहली पंक्ति तक चलती है।",
    "71": "‘भौममौषधम्’ = भौमम् + औषधम् (म् बाद के औ से जुड़ा)। ‘वीरुद्वानस्पत्यः’ = वीरुत् + वानस्पत्यः; वीरुत् ‘वीरुध्’ का प्रथमा एकवचन है (धकारान्त का अन्तिम ध् यहाँ त् बना)। ‘तथौषधिः’ = तथा + ओषधिः (आ + ओ → औ)। पहली पंक्ति श्लोक ७० की सूची बन्द करती है; चारों वर्गों की पहचान श्लोक ७२ में है।",
    "72": "वनस्पति के पुष्प-रहित होने का भाव तुलना से निकलता है, श्लोक में सीधे नहीं लिखा। ‘फलपाकान्ताः’ बहुव्रीहि है: फल के पकने पर जिनका अन्त है। ‘प्रतान’ = फैलने वाली शाखाएँ/लताएँ। ‘वानस्पत्यः फलैरपि’ में ‘अपि’ से दोनों लगते हैं: पुष्प भी, फल भी। विसर्ग का र् बनना: फलैः + वनस्पतिः (घोष से पहले), फलैः + अपि (स्वर से पहले)।",
    "73": "पाठभेद: ‘-नालस्व-’ की जगह ‘-नाडस्व-’; अर्थ वही, खोखला डंठल। ‘क्षीर’ यहाँ पौधे का दूध-जैसा रस है। पहली पंक्ति का लम्बा शब्द इतरेतर द्वन्द्व है। वाक्य श्लोक ७४ में ‘औद्भिदो गणः’ पर पूरा होता है।",
    "74": "‘षोडशैकोना’ = षोडश + एकोना (अ + ए → ऐ)। षोडश मूलिन्यः के साथ और एकोना विंशतिः के साथ पढ़ा गया है, यानी १६ मूलिनी और १९ फलिनी; यह पढ़ना पाठ-टिप्पणी पर टिका है और श्लोक ७७-७८ में सोलह नाम पूरे गिन जाते हैं। ‘शुङ्ग’ = कोंपल; ‘प्ररोह’ = अंकुर या हवाई जड़।",
    "75": "‘पञ्चैव’ = पञ्च + एव (अ + ए → ऐ); ‘अष्टावेव’ = अष्टौ + एव (औ → आव्); ‘संख्यातान्यष्टावेव’ में संख्यातानि + अष्टौ (इ + अ → य)। श्लोक में केवल गिनती है, किसी वर्ग के नाम नहीं। ‘पञ्च’ और ‘अष्टौ’ विशेषण हैं, बहुवचन के साथ आते हैं।",
    "76": "‘एतान्’ सम्भवतः श्लोक ७४-७६ की सब वस्तुओं (मूलिनी, फलिनी, स्नेह, लवण, मूत्र, दूध, वृक्ष) के लिए है, पर श्लोक सीमा नहीं बताता। पाठ-टिप्पणी पुनर्वसु को आत्रेय कहती है। ‘शोधनार्थाश्च’ = शोधनार्थाः + च (विसर्ग + च → श्)। ‘वेदवित्’ का शाब्दिक अर्थ ‘वेद का ज्ञाता’; यहाँ चिकित्सा-शास्त्र के सन्दर्भ में आयुर्वेद पढ़ा गया है।",
    "77": "‘श्वेतनामा’ = ‘श्वेता नाम वाली’; श्लोक ७९ में वही केवल ‘श्वेता’ कहलाती है। ‘त्रिवृदधोगुडा’ = त्रिवृत् + अधोगुडा; ‘गवाक्ष्यपि’ = गवाक्षी + अपि (ई + अ → य्, यण् सन्धि); ‘प्रत्यक्श्रेणी’ एक समस्त नाम है। नामों की वनस्पति-पहचान श्लोक में नहीं और अनिश्चित है।",
    "78": "यहाँ सात नाम हैं (क्रम १०-१६); श्लोक ७७ के नौ के साथ ठीक सोलह। ‘क्षीरिणी चात्र’ = क्षीरिणी च + अत्र (अ + अ → आ)। ‘षोडशी’ स्त्रीलिङ्ग क्रमवाचक है, जो क्षीरिणी के साथ चलता है। नामों के अर्थ या पहचान श्लोक नहीं देता।",
    "79": "‘च्छर्दने’ में च + छर्दने के बीच छ का द्वित्व (च्छ) हुआ है। ‘हैमवत्यपि’ = हैमवती + अपि (ई + अ → य्)। ‘योज्या’ एकवचन है; ‘प्रयोग की जाती हैं’ दोनों पंक्तियों में समझा गया है, इसलिए इसे दोनों समूहों पर लगाया गया है। ‘चैव’ = च + एव (अ + ए → ऐ)।",
}


AIDS = {
    "70": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["सुवर्णम्", "समलाः पञ्च लोहाः", "ससिकताः", "सुधा"]},
            {"label": "दूसरी पंक्ति",
             "items": ["मनःशिला–आल (जोड़ा)", "मणयः", "लवणम्",
                       "गैरिक–अञ्जन (जोड़ा)"]}]},
        "pegs": "मेरा बनाया चित्र: सोने की थाली पर पाँच धातुओं के बर्तन, उनके नीचे बालू, "
                "चूने की सफ़ेदी, मणियों की माला, नमक की डली और दो रंग (गेरू-अञ्जन)।",
        "anchors": "सुवर्ण = सु + वर्ण (सुन्दर रंग) · लवण (नमक) → लावण्य के पास "
                   "का शब्द · मणि = रत्न।",
        "sandhi": "अ + अ → आ: गैरिक + अञ्जन → गैरिकाञ्जने; आ + आ → आ: मनःशिला + आल → "
                  "मनःशिलाल, जो नपुंसक द्विवचन में मनःशिलाले (दो वस्तुएँ)।",
        "chunks": "सुवर्णं | समलाः पञ्च लोहाः | ससिकताः सुधा ‖ मनःशिलाले | मणयो | लवणं | "
                  "गैरिकाञ्जने।",
    },
    "71": {
        "diagram": {"groups": [
            {"label": "पिछली सूची का अन्त",
             "items": ["भौमम्", "औषधम्", "उद्दिष्टम्"]},
            {"label": "औद्भिद चतुर्विधम्",
             "items": ["वनस्पतिः", "वीरुत्", "वानस्पत्यः", "ओषधिः"]}]},
        "letters": "व-वी-वा-ओ: वनस्पति, वीरुध्, वानस्पत्य, ओषधि (नामों के पहले अक्षर)।",
        "pegs": "मेरा बनाया चित्र: चार पौधे एक कतार में: ऊँचा पेड़, लता, फूल वाला पेड़ और छोटी "
                "बूटी। (केवल याद के लिए; श्लोक में पहचान अगले श्लोक में है।)",
        "anchors": "ओषधि और औषध एक ही शब्द-परिवार के हैं · चतुर्विध = चतुर् (चार) + विध (प्रकार) · "
                   "औद्भिद ← उद्भिद् (उगने वाला)।",
        "sandhi": "त् → द् (घोष ‘व’ से पहले): वीरुत् + वानस्पत्यः → वीरुद्वानस्पत्यः · "
                  "आ + औ → औ: तथा + ओषधिः → तथौषधिः।",
        "chunks": "भौमम् औषधम् उद्दिष्टम् ‖ औद्भिदं तु चतुर्विधम् | वनस्पतिः तथा वीरुत् | "
                  "वानस्पत्यः तथौषधिः।",
    },
    "72": {
        "diagram": {"groups": [
            {"label": "फल",
             "items": ["फलैः", "वनस्पतिः"]},
            {"label": "पुष्प और फल",
             "items": ["पुष्पैः", "वानस्पत्यः", "फलैः अपि"]},
            {"label": "फल पकने पर अन्त",
             "items": ["ओषध्यः", "फलपाकान्ताः"]},
            {"label": "फैलती शाखाएँ",
             "items": ["प्रतानैः", "वीरुधः", "स्मृताः"]}]},
        "contrast": "वनस्पति ↔ वानस्पत्य: फल से पहचान ↔ पुष्प और फल दोनों से। ओषधि ↔ वीरुध्: "
                    "फल पकने पर अन्त ↔ प्रतान (फैलती शाखा)।",
        "letters": "फ-पु-फ-प्र: फल (वनस्पति), पुष्प-फल (वानस्पत्य), फल-पाक (ओषधि), प्रतान (वीरुध्)।",
        "pegs": "मेरा बनाया चित्र: वनस्पति = फल लदा पेड़ · वानस्पत्य = फूल और फल दोनों वाला · "
                "ओषधि = फल पकते ही सूखती बूटी · वीरुध् = दीवार पर चढ़ती लता।",
        "sandhi": "विसर्ग → र् (घोष व्यंजन या स्वर से पहले): फलैः + वनस्पतिः → फलैर्वनस्पतिः; "
                  "पुष्पैः + वानस्पत्यः → पुष्पैर्वानस्पत्यः; फलैः + अपि → फलैरपि; "
                  "प्रतानैः + वीरुधः → प्रतानैर्वीरुधः।",
        "chunks": "फलैर्वनस्पतिः | पुष्पैर्वानस्पत्यः फलैरपि ‖ ओषध्यः फलपाकान्ताः | "
                  "प्रतानैर्वीरुधः स्मृताः।",
    },
    "73": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति (एक लम्बा शब्द)",
             "items": ["मूल", "त्वक्", "सार", "निर्यास", "नाल", "स्वरस", "पल्लवाः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["क्षाराः", "क्षीरम्", "फलम्", "पुष्पम्", "भस्म", "तैलानि",
                       "कण्टकाः"]}]},
        "pegs": "मेरा बनाया चित्र: पेड़ को नीचे से ऊपर पढ़ें: मूल (जड़), त्वक् (छाल), सार (भीतरी "
                "लकड़ी), फिर निर्यास (गोंद), नाल (डंठल), स्वरस (निचोड़ा रस), पल्लव (कोंपल)।",
        "anchors": "निर्यास = पेड़ से निकला गोंद-सा रस · स्वरस = निचोड़ा हुआ रस · "
                   "क्षीर = दूध-जैसा रस · भस्म = राख।",
        "chunks": "मूलत्वक्सारनिर्यास | नालस्वरसपल्लवाः ‖ क्षाराः क्षीरं फलं पुष्पं | "
                  "भस्म तैलानि कण्टकाः।",
    },
    "74": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["पत्राणि", "शुङ्गाः", "कन्दाः", "प्ररोहाः", "औद्भिदो गणः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["मूलिन्यः", "षोडश", "एकोना", "फलिन्यः", "विंशतिः"]}]},
        "frame": "गण: औद्भिद = पत्र, शुंग, कन्द, प्ररोह · मूलिनी: षोडश (१६) · फलिनी: "
                 "विंशतिः एकोना (२०−१ = १९)।",
        "letters": "प-शु-क-प्र: पत्र, शुंग, कन्द, प्ररोह।",
        "sandhi": "अ + ए → ऐ: षोडश + एकोना → षोडशैकोना।",
        "anchors": "मूलिनी ← मूल (जड़) · फलिनी ← फल · षोडश = सोलह · विंशति = बीस · "
                   "एकोन = एक + ऊन (एक कम)।",
        "chunks": "पत्राणि शुङ्गाः | कन्दाश्च प्ररोहाश्च | औद्भिदो गणः ‖ मूलिन्यः "
                  "षोडशैकोना | फलिन्यो विंशतिः स्मृताः।",
    },
    "75": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["महास्नेहाः", "चत्वारः", "पञ्च एव", "लवणानि"]},
            {"label": "दूसरी पंक्ति",
             "items": ["अष्टौ", "मूत्राणि", "संख्यातानि", "अष्टौ एव", "पयांसि"]}]},
        "frame": "वर्ग · गिनती: महास्नेह ४ · लवण ५ · मूत्र ८ · दूध (पयांसि) ८।",
        "pegs": "मेरा बनाया चित्र: चार कलश (स्नेह), पाँच नमक की डलियाँ, आठ बर्तन मूत्र के, आठ "
                "दूध के। (केवल गिनती याद रखने के लिए।)",
        "sandhi": "अ + ए → ऐ: पञ्च + एव → पञ्चैव · औ + स्वर → आव्: अष्टौ + एव → "
                  "अष्टावेव।",
        "chunks": "महास्नेहाश्च चत्वारः | पञ्चैव लवणानि च ‖ अष्टौ मूत्राणि | "
                  "संख्यातान्यष्टावेव पयांसि च।",
    },
    "76": {
        "frame": "क्या: छह वृक्ष, शोधन के लिए · किसने बताए: पुनर्वसु · कसौटी: जो उन्हें "
                 "विकारों में प्रयोग करना जाने वह वेदवित्।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["शोधनार्थाः", "च", "षट्", "वृक्षाः", "पुनर्वसुनिदर्शिताः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["यः", "एतान्", "वेत्ति", "संयोक्तुम्", "विकारेषु", "सः",
                       "वेदवित्"]}]},
        "pegs": "मेरा बनाया चित्र: छह वृक्ष छह कुर्सियों जैसे; जो उन पर ठीक वस्तु बैठाना जाने, "
                "वही वेदवित्।",
        "anchors": "शोधन ← √शुध् (शुद्ध करना) · वेदवित् = वेद + वित् (ज्ञाता) · विकार = रोग/बिगाड़ · "
                   "संयोक्तुम् ← सम् + √युज् (जोड़ना, प्रयोग करना); संयोजन उसी धातु से।",
        "sandhi": "ट् → ड् (घोष ‘व’ से पहले): षट् + वृक्षाः → षड् वृक्षाः · विसर्ग + च → श्च: "
                  "शोधनार्थाः + च → शोधनार्थाश्च।",
        "chunks": "शोधनार्थाश्च षड् वृक्षाः | पुनर्वसुनिदर्शिताः ‖ य एतान् वेत्ति "
                  "संयोक्तुं | विकारेषु स वेदवित्।",
    },
    "77": {
        "letters": "ह-है-श्या-त्रि-अ-स-श्वे-प्र-ग (हस्तिदन्ती, हैमवती, श्यामा, त्रिवृत्, अधोगुडा, "
                   "सप्तला, श्वेता, प्रत्यक्श्रेणी, गवाक्षी)।",
        "diagram": {"groups": [
            {"label": "पहली तिकड़ी",
             "items": ["हस्तिदन्ती", "हैमवती", "श्यामा"]},
            {"label": "दूसरी तिकड़ी",
             "items": ["त्रिवृत्", "अधोगुडा", "सप्तला"]},
            {"label": "तीसरी तिकड़ी",
             "items": ["श्वेतनामा", "प्रत्यक्श्रेणी", "गवाक्षी"]}]},
        "pegs": "मेरा बनाया चित्र: हस्तिदन्ती = हाथी का दाँत · सप्तला = सात तालों वाला बक्सा · "
                "गवाक्षी = गाय-आँख वाली खिड़की।",
        "puns": "हस्तिदन्ती ≈ हाथी-दाँत, गवाक्षी ≈ गवाक्ष (खिड़की): केवल सुनने की सहायता, पौधे की पहचान नहीं।",
        "sandhi": "त् → द् (स्वर से पहले): त्रिवृत् + अधोगुडा → त्रिवृदधोगुडा।",
        "chunks": "हस्तिदन्ती हैमवती श्यामा | त्रिवृदधोगुडा | सप्तला श्वेतनामा च | "
                  "प्रत्यक्श्रेणी गवाक्ष्यपि।",
    },
    "78": {
        "letters": "ज्यो-बि-श-वि-अ-द्र-क्षी: ज्योतिष्मती, बिम्बी, शणपुष्पी, विषाणिका, अजगन्धा, "
                   "द्रवन्ती, क्षीरिणी।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["ज्योतिष्मती", "बिम्बी", "शणपुष्पी", "विषाणिका"]},
            {"label": "दूसरी पंक्ति",
             "items": ["अजगन्धा", "द्रवन्ती", "क्षीरिणी", "अत्र षोडशी"]}]},
        "puns": "द्रवन्ती ≈ द्रव (बहना) और अजगन्धा ≈ अज + गन्ध (बकरी की गन्ध): केवल सुनने की "
                "सहायता, पौधे की पहचान नहीं।",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र (क्षीरिणी चात्र)।",
        "chunks": "ज्योतिष्मती च बिम्बी च | शणपुष्पी विषाणिका ‖ अजगन्धा द्रवन्ती च | "
                  "क्षीरिणी चात्र षोडशी।",
    },
    "79": {
        "contrast": "वमन (छर्दन): शणपुष्पी · बिम्बी · हैमवती ↔ शीर्षविरेचन: श्वेता · ज्योतिष्मती।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["शणपुष्पी", "बिम्बी", "छर्दने", "हैमवती"]},
            {"label": "दूसरी पंक्ति",
             "items": ["श्वेता", "ज्योतिष्मती", "योज्या", "शीर्षविरेचने"]}]},
        "letters": "श-बि-हैं | श्वे-ज्यो: वमन के लिए श-बि-है, सिर के लिए श्वे-ज्यो।",
        "sandhi": "छ का द्वित्व: च + छर्दने → च्छर्दने · ई + अ → य्+अ: हैमवती + अपि → हैमवत्यपि · "
                  "अ + ए → ऐ: च + एव → चैव।",
        "chunks": "शणपुष्पी च बिम्बी च | च्छर्दने हैमवत्यपि ‖ श्वेता ज्योतिष्मती चैव | "
                  "योज्या शीर्षविरेचने।",
    },
}

IMAGE_SPECS = {
    ("72", "contrast"): {
        "file": "su1_72_plant_classes.svg",
        "alt": "Table of the four plant classes of verse 72 and the mark of each: vanaspati by fruit, vanaspatya by flower and fruit, oshadhi ends when the fruit ripens, virudh by spreading shoots.",
        "type": "table",
        "title": "चार वर्ग और उनकी पहचान",
        "heads": ["वर्ग", "पहचान"],
        "rows": [["वनस्पति", "फल"],
                 ["वानस्पत्य", "पुष्प और फल"],
                 ["ओषधि", "फल पकने पर अन्त"],
                 ["वीरुध्", "प्रतान (फैलती शाखा)"]],
    },
    ("79", "contrast"): {
        "file": "su1_79_uses.svg",
        "alt": "Two columns from verse 79: for emesis three plants (shanapushpi, bimbi, haimavati); for head-purgation two plants (shveta, jyotishmati).",
        "type": "split",
        "title": "किसका प्रयोग किसमें",
        "cols": [["वमन (छर्दन)", ["शणपुष्पी", "बिम्बी", "हैमवती"]],
                 ["शीर्षविरेचन", ["श्वेता", "ज्योतिष्मती"]]],
    },
}
