from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}


def _g(label, line):
    """A diagram group made of the printed words of one line, in order."""
    return {"label": label, "items": line.split()}


# --------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "उभे शताह्वे मधुकं मधूकम्",
    "question": "For which condition does verse 21 give a pradeha, and what is it made from?",
    "rule": ("उभे शताह्वे … घृतं विदारीं च सितोपलां च कुर्यात् प्रदेहं पवने सरक्ते = "
             "With both śatāhvās, madhuka, madhūka, balā, priyāla, kaśeruka, ghee, "
             "vidārī and rock sugar, one should make a pradeha in Vāta accompanied "
             "by blood."),
    "limits": ("The verse does not name the two śatāhvās, gives no quantities, and "
               "does not tie सरक्ते to any named disease. Plant names are kept "
               "unidentified; madhuka and madhūka are two different words."),
    "explain_hi": ("यह श्लोक रक्त-सहित वात (‘पवने सरक्ते’) के लिए प्रदेह की औषध-सूची "
                   "देता है। प्रदेह शरीर पर लगाया जाने वाला औषधीय लेप है; अध्याय का "
                   "अन्तिम श्लोक इन्हें ‘चूर्ण-प्रदेह’ कहता है। सूची के सारे नाम द्वितीया "
                   "(कर्म-रूप) में हैं और क्रिया ‘कुर्यात्’ (करे) दूसरी पंक्ति में आती "
                   "है। ‘उभे शताह्वे’ का अर्थ ‘दोनों शताह्वा’ है; श्लोक उनके नाम नहीं "
                   "बताता। ‘मधुकं’ (छोटा उ) और ‘मधूकं’ (दीर्घ ऊ) अलग शब्द हैं। "
                   "‘सरक्ते’ = स + रक्त, ‘रक्त के साथ’; यह ‘पवने’ का विशेषण है।"),
    "hook": "रक्त-सहित वात → प्रदेह: दोनों शताह्वा, मधुक, मधूक, बला, प्रियाल, कशेरुक, घृत, विदारी, मिश्री।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 21 ends कुर्यात् प्रदेहं पवने सरक्ते. For which condition is the pradeha made?",
            ("Vāta accompanied by blood",
             "पवने सरक्ते = in Vāta accompanied by blood (rakta)."),
            [("Pain in the head",
              "Head pain (शिरोरुजा) is the subject of verses 23 and 24."),
             ("Poison",
              "Poison is the subject of verse 28."),
             ("Bad smell of the body",
              "Body smell is the subject of verse 29.")],
            "The pradeha is made in Vāta accompanied by blood.",
            "कुर्यात् प्रदेहं + locative = make a pradeha in that condition."),
        match(1, "Match each word of verse 21 to its meaning.",
              [["कुर्यात्", "one should make"], ["प्रदेहम्", "pradeha"],
               ["पवने", "in Vāta"], ["सितोपलाम्", "rock sugar (white crystal)"]],
              "These words give the action, what is made, and where.",
              "कुर्यात् = one should make; प्रदेहम् = pradeha; पवने = in Vāta; सितोपलाम् = rock sugar."),
        fill(2, "The word for 'ghee' in the first word of line 2 is ____ (type it in Devanagari).",
             ["घृतं", "घृतम्"],
             "Line 2 opens with घृतं, the ghee.",
             "घृतम् is neuter accusative singular, one of the things the pradeha is made with.",
             "घृतम् = ghee, one of the listed items."),
        mcq("discriminate", 3, "Which is the right split of सितोपलां?",
            ("सित + उपलां: अ + उ joins as ओ",
             "The first word सित means white; अ + उ gives ओ, so सित + उपलां is written सितोपलां."),
            [("सितो + पलां", "पलां is not a word in this verse."),
             ("सित + पलां", "That loses the उ of उपलां."),
             ("सिते + उपलां", "ए + उ would not give सितोपलां.")],
            "सितोपलां = सित (white) + उपलां (crystal, lump): rock sugar.",
            "अ + उ → ओ: सित + उपला → सितोपला."),
        mcq("apply", 4,
            "उभे शताह्वे: the ending -ए and the word उभे show what about the śatāhvās?",
            ("Two kinds of śatāhvā are meant",
             "On a word like शताह्वा, the dual ending is -ए, and उभे means 'both'."),
            [("Only one śatāhvā is meant",
              "A singular would not be joined by उभे, 'both'."),
             ("Many kinds of śatāhvā are meant",
              "The plural of such a word ends in -आः, not -ए."),
             ("The two kinds are named in the verse",
              "The verse names neither of the two; it only says 'both'.")],
            "Dual -ए with उभे = the two śatāhvās, which the verse leaves unnamed.",
            "Feminine word in -आ: dual ending -ए = two."),
        mcq("transfer", 5,
            "An invented line reads कुर्यात् प्रदेहं ज्वरे (ज्वर = fever). By the pattern of verse 21, what does it say?",
            ("One should make a pradeha in fever",
             "A locative like पवने or ज्वरे names the condition in which it is made."),
            [("Fever should make a pradeha",
              "The doer of 'make' is not ज्वरे; its ending -ए marks a place or condition."),
             ("One should make fever with a pradeha",
              "प्रदेहं (-म्) is what is made, not ज्वरे."),
             ("A pradeha is made of fever",
              "The locative -ए says 'in', not 'of'.")],
            "The pattern is: कुर्यात् + प्रदेहं (what is made) + locative (the condition).",
            "Locative -ए = the condition in which the pradeha is made.",
            teaches="After कुर्यात् प्रदेहं, a locative word names the condition, as पवने does in verse 21."),
    ],
}

# --------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "रास्ना गुडूची मधुकं बले द्वे",
    "question": "What pain does the pradeha of verse 22 drive out, and which drugs and fats does it list?",
    "rule": ("रास्ना … रक्तानिलार्तिं प्रणुदेत् प्रदेहः = The pradeha of rāsnā, guḍūcī, "
             "madhuka, the two balās, with jīvaka and ṛṣabhaka, milk and cooked "
             "ghee joined with madhuśeṣa would drive out the pain of blood and Vāta."),
    "limits": ("मधुशेष is uncertain (literally 'remainder of honey'). The verse does "
               "not say with what the ghee is cooked. The compound रक्तानिलार्ति may "
               "also be read as pain 'from' blood and Vāta."),
    "explain_hi": ("यह श्लोक एक और प्रदेह की सूची है, जिसका फल दूसरी पंक्ति के अन्त में "
                   "है: ‘प्रणुदेत्’ (दूर करे) और कर्म ‘रक्तानिलार्तिम्’। इस समास में "
                   "रक्त + अनिल (वायु, वात) + आर्ति (पीड़ा) हैं। ‘बले द्वे’ का अर्थ "
                   "‘दोनों बला’ है। ‘सजीवकं सर्षभकं’ में ‘स-’ का अर्थ ‘सहित’ है: जीवक "
                   "और ऋषभक के साथ। ‘सिद्धं’ का अर्थ पका हुआ/तैयार किया हुआ है; "
                   "श्लोक नहीं बताता कि घृत किनके साथ पकाया जाए। ‘मधुशेषयुक्तं’ में "
                   "मधुशेष का अर्थ अनिश्चित है।"),
    "hook": "रास्ना–गुडूची–मधुक–दोनों बला (जीवक, ऋषभक सहित) + दूध + सिद्ध घृत → रक्त और वात की पीड़ा दूर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 22 ends रक्तानिलार्तिं प्रणुदेत् प्रदेहः. What pain would this pradeha drive out?",
            ("Pain of blood and Vāta (anila)",
             "रक्त = blood and अनिल = wind, Vāta; आर्ति = pain."),
            [("Pain of the head",
              "Head pain is in verses 23 and 24."),
             ("Pain of the flank",
              "Flank pain is in verse 25."),
             ("Pain from poison",
              "Poison is in verse 28.")],
            "रक्तानिलार्तिं = the pain (आर्ति) of blood (रक्त) and Vāta (अनिल).",
            "रक्त-अनिल-आर्ति = pain of blood and Vāta."),
        order(1, "Put the first four items of verse 22 in the order of the verse.",
              ["रास्ना", "गुडूची", "मधुकं", "बले द्वे"],
              "The verse opens with these four items.",
              "रास्ना → गुडूची → मधुकं → बले द्वे."),
        fill(2, "The word meaning 'cooked, prepared' that describes the ghee is ____ (type it in Devanagari).",
             ["सिद्धं", "सिद्धम्"],
             "Line 2 reads घृतं च सिद्धं: the ghee that has been cooked.",
             "सिद्धम् is a 'having been done' word (past participle of √सिध्) in the neuter singular, agreeing with घृतम्.",
             "सिद्धम् = cooked, prepared; it describes the ghee."),
        mcq("discriminate", 3, "Which is the right split of पयश्च?",
            ("पयः + च: a visarga before च becomes श्",
             "पयः is 'milk'; ः + च is written श्च."),
            [("पय + श्च", "श्च is not a word."),
             ("पयश् + च", "पयश् is not a word; the word is पयः."),
             ("पया + श्च", "The word is पयः, not पया.")],
            "पयश्च = पयः (milk) + च (and).",
            "Visarga + च → श्च."),
        mcq("apply", 4,
            "सजीवकं सर्षभकं: the prefix स- is 'with'. What does this say about jīvaka and ṛṣabhaka?",
            ("They go with the listed drugs",
             "सजीवकम् = with jīvaka; सर्षभकम् = with ṛṣabhaka: they are joined to the list."),
            [("They are left out of the pradeha",
              "'With' adds them; it does not remove them."),
             ("They replace the milk",
              "The milk is named separately with पयश्च."),
             ("They are the diseases treated",
              "The diseases are in रक्तानिलार्तिम्.")],
            "A स- word in this list adds an item together with the others.",
            "स- + name = together with that item."),
        mcq("transfer", 5,
            "An invented line has सदुग्धं चूर्णम् (दुग्ध = milk, चूर्ण = powder). By the pattern of सजीवकम्, what does it mean?",
            ("Powder together with milk",
             "स- means 'with', so सदुग्धम् is 'with milk'."),
            [("Powder without milk",
              "'Without' would be a different prefix; स- means 'with'."),
             ("Milk made of powder",
              "सदुग्धम् describes the powder, saying it comes with milk."),
             ("Powder for the milk-drinker",
              "Nothing in the word names a person.")],
            "The स- prefix works with any name: स + name = with that thing.",
            "स- = with, in verse 22 and in new examples.",
            teaches="स- before a name makes an adjective 'together with that': सजीवकम् 'with jīvaka', सदुग्धम् 'with milk'."),
    ],
}

# --------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "वाते सरक्ते सघृतं प्रदेहः",
    "question": "Which two conditions does verse 23 give a pradeha for, and from what?",
    "rule": ("वाते सरक्ते … गोधूमचूर्णं छगलीपयश्च = in Vāta with blood, a pradeha of "
             "wheat flour with ghee, and goat's milk; नतोत्पलं … शिरोरुजायां "
             "सघृतं प्रदेहः = in head pain, nata and utpala joined with candana "
             "and kuṣṭha, with ghee."),
    "limits": ("Each half has its own condition and no verb of its own; the verb is "
               "understood. नतोत्पलं can be nata + utpala (two drugs) or one named "
               "drug; the card reads it as two."),
    "explain_hi": ("एक श्लोक में दो प्रदेह हैं। पहला आधा: रक्त-सहित वात में गेहूँ के आटे का "
                   "घृत-सहित प्रदेह, और बकरी का दूध (‘छगलीपयश्च’)। दूसरा आधा: सिर के "
                   "दर्द (‘शिरोरुजायाम्’) में नत और उत्पल, चन्दन और कुष्ठ से युक्त, घृत "
                   "सहित प्रदेह। दोनों आधों में ‘सघृतम्’ (घृत सहित) आता है। रोग का नाम "
                   "सप्तमी में है (‘वाते’, ‘शिरोरुजायाम्’), और क्रिया आगे-पीछे से समझी "
                   "जाती है। ‘नत’ को यहाँ औषध का नाम माना गया है।"),
    "hook": "दो आधे: रक्त-सहित वात → गेहूँ का आटा + बकरी का दूध + घृत · सिर-दर्द → नत, उत्पल, चन्दन, कुष्ठ + घृत।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 23 gives pradehas for two conditions. Which pair is it?",
            ("Vāta with blood, and head pain",
             "वाते सरक्ते in the first half and शिरोरुजायाम् in the second."),
            [("Flank pain, and poison",
              "Flank pain is verse 25 and poison is verse 28."),
             ("Head pain, and body smell",
              "Body smell is in verse 29, not here."),
             ("Poison, and Vāta with blood",
              "Poison is in verse 28, not here.")],
            "The first half is for Vāta with blood; the second is for head pain.",
            "वाते सरक्ते + शिरोरुजायाम् = the two conditions of verse 23."),
        match(1, "Match each word of verse 23 to its meaning.",
              [["वाते सरक्ते", "in Vāta with blood"],
               ["शिरोरुजायाम्", "in head pain"],
               ["गोधूमचूर्णम्", "wheat flour"],
               ["छगलीपयः", "goat's milk"]],
              "Two words give the conditions, two give the base materials of the first half.",
              "वाते सरक्ते = in Vāta with blood; शिरोरुजायाम् = in head pain; गोधूमचूर्णम् = wheat flour; छगलीपयः = goat's milk."),
        fill(2, "The word for 'with ghee' in the verse is ____ (type it in Devanagari).",
             ["सघृतं", "सघृतम्"],
             "सघृतम् occurs in both halves.",
             "सघृतम् = स + घृतम्: the prefix स- means 'with', so it is 'together with ghee'.",
             "सघृतम् = with ghee."),
        mcq("discriminate", 3, "Which is the right split of नतोत्पलं?",
            ("नत + उत्पलं: अ + उ joins as ओ",
             "नत and उत्पल are the two names; अ + उ is written ओ."),
            [("नतो + त्पलं", "त्पलं is not a word."),
             ("नत + ओत्पलं", "The second name is उत्पल, not ओत्पल."),
             ("नति + उत्पलं", "That would not give नतोत्पलं.")],
            "नतोत्पलं = नत + उत्पलं, read as two drugs.",
            "अ + उ → ओ: नत + उत्पल → नतोत्पल."),
        multi("apply", 4,
              "Which items does the second half name for the head-pain pradeha?",
              [("नतोत्पलं (read as nata + utpala)", "Right: the card reads it as the pair nata and utpala."),
               ("चन्दन", "Right: it is joined with candana."),
               ("कुष्ठ", "Right: it is joined with kuṣṭha."),
               ("गोधूमचूर्ण", "Wheat flour belongs to the first half."),
               ("छगलीपयः", "Goat's milk belongs to the first half.")],
              [0, 1, 2],
              "The second half names nata, utpala, candana and kuṣṭha (with ghee). Wheat flour and goat's milk are in the first half.",
              "First half: Vāta with blood; second half: head pain with nata, utpala, candana, kuṣṭha."),
        mcq("transfer", 5,
            "An invented half-line: ज्वरे सघृतं प्रदेहो यवचूर्णम् (ज्वर = fever, यव = barley). By the pattern of verse 23, what does it say?",
            ("In fever, a pradeha of barley flour with ghee",
             "Locative = condition; सघृतम् = with ghee; चूर्णम् = the flour."),
            [("In barley flour, a pradeha for fever",
              "ज्वरे is the condition; यवचूर्णम् is the material."),
             ("Fever is made from barley flour",
              "The locative -ए says 'in', so it names the condition."),
             ("A pradeha of ghee without barley flour",
              "सघृतम् is 'with ghee', and the flour is named.")],
            "As in the first half of verse 23: condition (locative) + सघृतं प्रदेहः + the flour.",
            "Condition in locative + सघृतं प्रदेहः + material.",
            teaches="A half-line of this verse has the shape: condition (locative), pradeha 'with ghee', and the material in the nominative."),
    ],
}

# --------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "प्रपौण्डरीकं सुरदारु कुष्ठम्",
    "question": "What is the pradeha of verse 24 for, and which drug names does it list?",
    "rule": ("प्रपौण्डरीकं … शिरोरुजायां सघृतः प्रदेहः = In head pain, a pradeha "
             "with ghee of prapauṇḍarīka, suradāru, kuṣṭha, yaṣṭi-named drug, elā, "
             "kamala and utpala, and with loha, erakā, padmaka and coraka."),
    "limits": ("The edition's text flag says लोह (loha) may be an error for लोध्र "
               "(lodhra); this card keeps the printed word. The last pāda has no "
               "verb of its own and is read as more ingredients. Plants are not "
               "identified."),
    "explain_hi": ("यह सिर-दर्द (‘शिरोरुजायाम्’) का दूसरा प्रदेह है; पहला श्लोक २३ के "
                   "दूसरे आधे में था। पहली पंक्ति में नाम गिनाए गए हैं; ‘यष्ट्याह्वम्’ "
                   "का अर्थ ‘यष्टि नाम वाला (द्रव्य)’ है। ‘कमलोत्पले’ द्विवचन है: कमल "
                   "और उत्पल। अन्तिम चरण ‘लोहैरका…चोरकैश्च’ तृतीया बहुवचन है और इसे "
                   "‘और इनके साथ’ पढ़ा गया है। पाठ-टिप्पणी में ‘लोह’ पर संशय दर्ज है "
                   "(सम्भवतः ‘लोध्र’), इसलिए इस कार्ड में कोई प्रश्न उस शब्द पर नहीं टिका।"),
    "hook": "सिर-दर्द → प्रपौण्डरीक, सुरदारु, कुष्ठ, यष्टि-नामक, एला, कमल–उत्पल, और लोह, एरका, पद्मक, चोरक के साथ, घृत सहित।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 24 has शिरोरुजायां सघृतः प्रदेहः. What is its pradeha for?",
            ("Pain in the head",
             "शिरोरुजायाम् = in head pain (शिरः = head, रुजा = pain)."),
            [("Pain in the flank",
              "Flank pain is in verse 25."),
             ("Vāta with blood",
              "That is in verses 21 to 23."),
             ("Body smell",
              "That is in verse 29.")],
            "The pradeha of verse 24 is made for head pain.",
            "शिरोरुजायाम् = in head pain."),
        match(1, "Match each word of verse 24 to its meaning.",
              [["शिरोरुजायाम्", "in head pain"], ["सघृतः", "with ghee"],
               ["कमलोत्पले", "kamala and utpala"], ["प्रदेहः", "pradeha"]],
              "These words give the condition, the ghee, a pair of drugs and the preparation.",
              "शिरोरुजायाम् = in head pain; सघृतः = with ghee; कमलोत्पले = kamala and utpala; प्रदेहः = pradeha."),
        fill(2, "कमलोत्पले ends in -ए. This ending shows the ____ number (singular, dual or plural).",
             ["dual", "Dual", "द्विवचन"],
             "The dual ending -ए on a neuter word means two.",
             "On neuter words in -अ, the dual nominative ends in -ए. कमलोत्पले joins two names, कमल and उत्पल.",
             "Neuter -अ word + dual -ए = two items."),
        mcq("discriminate", 3, "Which is the right split of यष्ट्याह्वमेला?",
            ("यष्टि + आह्वम् + एला: इ + आ becomes या",
             "इ before a different vowel becomes य्, so यष्टि + आह्वम् is written यष्ट्याह्वम्."),
            [("यष्ट्या + ह्वम् + एला", "ह्वम् is not a word."),
             ("यष्टि + अह्वम् + एला", "The middle word is आह्वम्, 'named'."),
             ("यष्टि + आह्वमे + ला", "ला is not a word here.")],
            "यष्ट्याह्वमेला = यष्टि + आह्वम् + एला: 'the one named yaṣṭi' and elā.",
            "इ + आ → या: यष्टि + आह्वम् → यष्ट्याह्वम्."),
        mcq("apply", 4,
            "The last pāda ends -कैश्च, an instrumental plural. On this card's reading, how does it relate to the list?",
            ("It adds further ingredients: 'and with these'",
             "The instrumental 'with' adds loha, erakā, padmaka and coraka to the list."),
            [("It names a second disease",
              "No disease is named in that pāda."),
             ("It supplies the verb 'apply'",
              "It is a list of names in the instrumental, not a verb."),
             ("It names the place of application",
              "No part of the body is named there.")],
            "The instrumental -ऐः / -कैः means 'with'; the pāda gives more ingredients.",
            "Instrumental plural = 'with these'."),
        mcq("transfer", 5,
            "In verse 24, प्रदेहः is printed प्रदेहो before a voiced letter. By the same sandhi, how is प्रदेहः + मृदुः (मृदु = soft) written?",
            ("प्रदेहो मृदुः",
             "After अ, a visarga before a voiced consonant becomes ओ."),
            [("प्रदेहर्मृदुः",
              "र् replaces a visarga after इ or उ, not after अ."),
             ("प्रदेहा मृदुः",
              "The visarga after अ does not become आ."),
             ("प्रदेहः मृदुः",
              "Before a voiced consonant the visarga after अ is changed to ओ.")],
            "The same rule gives प्रदेहो in verse 24 and प्रदेहो मृदुः here.",
            "अः + voiced consonant → ओ (after अ).",
            teaches="A word ending in -अः followed by a voiced consonant turns into -ओ, as in प्रदेहो in verse 24."),
    ],
}

# --------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "रास्ना हरिद्रे नलदं शताह्वे",
    "question": "What is the application of verse 25 for, and how is it applied?",
    "rule": ("रास्ना हरिद्रे … जीवन्तिमूलं सघृतं सतैलमालेपनं पार्श्वरुजासु कोष्णम् = "
             "Rāsnā, the two haridrās, nalada, the two śatāhvās, devadārus, rock "
             "sugar and the root of jīvantī, with ghee and oil: a lukewarm "
             "application for pains of the flank."),
    "limits": ("द्वे देवदारूणि is read as 'devadārus' (several kinds), not as 'two', "
               "because the form is plural; another reading takes 'two'. The "
               "verse gives no quantities and does not name the two haridrās or "
               "śatāhvās."),
    "explain_hi": ("यह पार्श्व (बगल/पसलियों) के दर्द के लिए आलेपन है, और यहाँ रूप का नाम "
                   "‘प्रदेह’ नहीं, ‘आलेपनम्’ है। ‘सघृतं सतैलम्’ का अर्थ घृत और तेल सहित है। "
                   "‘कोष्णम्’ = क + उष्ण, यानी थोड़ा गर्म (गुनगुना)। ‘हरिद्रे’ और "
                   "‘शताह्वे’ द्विवचन हैं: दो-दो प्रकार, जिनके नाम नहीं दिए गए। "
                   "‘देवदारूणि’ नपुंसक बहुवचन है। ‘पार्श्वरुजासु’ सप्तमी बहुवचन है: "
                   "पार्श्व के दर्दों में।"),
    "hook": "पार्श्व के दर्द में गुनगुना आलेपन: रास्ना, दो हरिद्रा, नलद, दो शताह्वा, देवदारु, मिश्री, जीवन्ती की जड़ + घृत + तेल।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 25 ends पार्श्वरुजासु. Pains of which part of the body is the application for?",
            ("The flank (side)",
             "पार्श्व = flank or side; रुजा = pain."),
            [("The head",
              "Head pain is in verses 23 and 24."),
             ("The skin",
              "Skin is not named in verse 25."),
             ("The throat",
              "The throat is not named in verse 25.")],
            "पार्श्वरुजासु = in pains of the flank.",
            "पार्श्व-रुजा = flank pain."),
        match(1, "Match each word of verse 25 to its meaning.",
              [["हरिद्रे", "the two haridrās"],
               ["पार्श्वरुजासु", "in pains of the flank"],
               ["जीवन्तिमूलम्", "root of jīvantī"],
               ["सतैलम्", "with oil"]],
              "These words give two of the ingredients, the oil, and the condition.",
              "हरिद्रे = the two haridrās; पार्श्वरुजासु = in pains of the flank; जीवन्तिमूलम् = root of jīvantī; सतैलम् = with oil."),
        fill(2, "The word meaning 'application, anointing' is ____ (type it in Devanagari).",
             ["आलेपनं", "आलेपनम्"],
             "The line reads सतैलमालेपनं, which is सतैलम् + आलेपनम्.",
             "आलेपनम् names the preparation. Here it takes the place of the word प्रदेह used in the other verses.",
             "आलेपनम् = application, anointing."),
        mcq("discriminate", 3, "Which is the right split of कोष्णम्?",
            ("क + उष्णम्: अ + उ joins as ओ",
             "क is a prefix meaning 'a little' and उष्ण is 'warm'; अ + उ is written ओ."),
            [("को + ष्णम्", "ष्णम् is not a word."),
             ("कु + उष्णम्", "उ + उ would give कूष्णम्."),
             ("क + ओष्णम्", "The second word is उष्ण, not ओष्ण.")],
            "कोष्णम् = क (slightly) + उष्णम् (warm): lukewarm.",
            "क + उष्ण → कोष्ण = slightly warm."),
        mcq("apply", 4,
            "Which two fats does verse 25 name for the application?",
            ("Ghee and oil",
             "सघृतं सतैलम् = with ghee, with oil."),
            [("Ghee only",
              "सतैलम् adds oil to the ghee."),
             ("Oil and milk",
              "Milk is not named in verse 25 and ghee is."),
             ("Milk and honey",
              "Neither is named in verse 25.")],
            "सघृतं सतैलम् = with ghee and with oil.",
            "सघृतम् + सतैलम् = ghee and oil."),
        mcq("transfer", 5,
            "An invented phrase: जानुरुजासु (जानु = knee). Compared with शिरोरुजायाम्, what does the ending -सु show?",
            ("Several pains: 'in knee pains'",
             "-सु is the locative plural, as in पार्श्वरुजासु 'in pains of the flank'."),
            [("A single pain: 'in one knee pain'",
              "The single form would end like शिरोरुजायाम्."),
             ("The doer of the action",
              "A doer would be in the nominative, not -सु."),
             ("The thing made, not a condition",
              "-सु is a locative, which gives the condition.")],
            "-आयाम् is the singular locative, -आसु the plural: शिरोरुजायाम् 'in head pain' against पार्श्वरुजासु 'in pains of the flank'.",
            "Locative singular -आयाम्; locative plural -आसु.",
            teaches="Feminine words in -आ end the locative in -आयाम् (one) and -आसु (several): 'in a pain' against 'in pains'."),
    ],
}

# --------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "शैवालपद्मोत्पलवेत्रतुङ्ग",
    "question": "What kind of pradeha is verse 26, and from which drug names?",
    "rule": ("शैवाल … चन्दनानि निर्वापणः स्यात् सघृतः प्रदेहः = With śaivāla, padma, "
             "utpala, vetra, tuṅga, prapauṇḍarīka, mṛṇāla, lodhra, priyaṅgu, "
             "kāleyaka and candana, a pradeha with ghee would be nirvāpaṇa "
             "(cooling, quenching)."),
    "limits": ("The long first word has an extra अ in -काण्यमृणाल-; the text flag "
               "suggests prapauṇḍarīkāṇi + mṛṇāla-lodhram, and this card reads it "
               "so. The verse names no condition and no quantities."),
    "explain_hi": ("यह प्रदेह ‘निर्वापण’ है, यानी शीतल करने वाला/ताप शान्त करने वाला। "
                   "श्लोक किसी रोग का नाम नहीं लेता; उसका फल केवल ‘निर्वापणः स्यात्’ "
                   "(होगा) है। पहली पंक्ति एक ही लम्बे समास-शब्द की है, जिसमें "
                   "शैवाल, पद्म, उत्पल, वेत्र, तुङ्ग, प्रपौण्डरीक, मृणाल और लोध्र आते "
                   "हैं। ‘सघृतः’ पुल्लिङ्ग एकवचन है और ‘प्रदेहः’ का विशेषण है। "
                   "‘काण्यमृणाल’ में एक अतिरिक्त ‘अ’ पाठ-टिप्पणी में दर्ज है।"),
    "hook": "निर्वापण (शीतल) प्रदेह: शैवाल–पद्म–उत्पल–वेत्र–तुङ्ग–प्रपौण्डरीक–मृणाल–लोध्र–प्रियङ्गु–कालेयक–चन्दन + घृत।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 26 ends निर्वापणः स्यात् सघृतः प्रदेहः. What kind of pradeha is it said to be?",
            ("Cooling, quenching (निर्वापण)",
             "निर्वापण = cooling, quenching, as the data glosses it."),
            [("Lukewarm, like the application in verse 25",
              "कोष्ण, 'lukewarm', is the word in verse 25."),
             ("A poison-destroyer, like verse 28",
              "Poison is the subject of verse 28."),
             ("A remover of body smell, like verse 29",
              "Body smell is the subject of verse 29.")],
            "The verse calls this ghee pradeha निर्वापण: cooling.",
            "निर्वापणः = cooling, quenching."),
        match(1, "Match each word of verse 26 to its meaning.",
              [["निर्वापणः", "cooling, quenching"], ["सघृतः", "with ghee"],
               ["स्यात्", "it would be"], ["प्रदेहः", "pradeha"]],
              "These four words make up the closing clause of the verse.",
              "निर्वापणः = cooling; सघृतः = with ghee; स्यात् = it would be; प्रदेहः = pradeha."),
        fill(2, "The word meaning 'it would be' is ____ (type it in Devanagari).",
             ["स्यात्"],
             "The clause is निर्वापणः स्यात् सघृतः प्रदेहः.",
             "स्यात् is the third person singular optative of √अस्: 'it would be, it may be'. The verse says what the pradeha would be.",
             "स्यात् = it would be (optative of √अस्)."),
        mcq("discriminate", 3,
            "सघृतः is masculine, nominative singular. Which word in verse 26 does it describe?",
            ("प्रदेहः",
             "Both are masculine nominative singular: the pradeha comes with ghee."),
            [("चन्दनानि",
              "चन्दनानि is neuter plural, so it does not match."),
             ("प्रियङ्गुकालेयकचन्दनानि",
              "This compound is neuter plural, so it does not match."),
             ("स्यात्",
              "स्यात् is a verb, not a describing word.")],
            "A describing word copies the gender, number and case of its noun: सघृतः goes with प्रदेहः.",
            "Describing word and noun agree in gender, number and case."),
        mcq("apply", 4,
            "Verses 24 and 26 both name prapauṇḍarīka and utpala. What does each verse give for its own pradeha?",
            ("Verse 24: head pain. Verse 26: cooling",
             "24 ends शिरोरुजायाम्; 26 ends निर्वापणः स्यात्."),
            [("Verse 24: cooling. Verse 26: head pain",
              "The two are the wrong way round."),
             ("Both are for head pain",
              "Verse 26 names no condition, only निर्वापण."),
             ("Both are cooling",
              "Verse 24 names head pain.")],
            "The shared names do not make the two pradehas the same: each verse states its own purpose.",
            "Same drug names, different stated purpose: read the verse's own ending."),
        mcq("transfer", 5,
            "An invented line: लेपो मृदुः स्यात् (लेप = paste, मृदु = soft). By the pattern of निर्वापणः स्यात्, what does it say?",
            ("The paste would be soft",
             "स्यात् = it would be, as in निर्वापणः स्यात्."),
            [("The paste was soft",
              "स्यात् is optative, not a past form."),
             ("Make the paste soft",
              "An order would use another verb form."),
             ("The paste is not soft",
              "Nothing in the line negates it.")],
            "स्यात् states what something would be: निर्वापणः स्यात् 'would be cooling', लेपो मृदुः स्यात् 'the paste would be soft'.",
            "X स्यात् = X would be.",
            teaches="स्यात् with a describing word says what the thing would be; the word before it names the quality."),
    ],
}

# --------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "सितालतावेतसपद्मकानि",
    "question": "What does verse 27 say about its list, and which roots does it name?",
    "rule": ("सितालता … निर्वापणः स्याज्जलमेरका च = Sitālatā, vetasa, padmaka, the "
             "yaṣṭi-named drug, aindrī, nalinas, dūrvā, the root of yavāsa, of "
             "kuśa and of kāśa, water and erakā would be nirvāpaṇa (cooling)."),
    "limits": ("The verse has no noun for the application; प्रदेह is understood from "
               "the neighbouring verses. जलम् is read as 'water' but could be a "
               "drug named jala. सितालता may also split as सिता + लता."),
    "explain_hi": ("यह भी निर्वापण (शीतल करने वाली) सूची है, पर इसमें ‘प्रदेह’ शब्द नहीं आया; "
                   "पुल्लिङ्ग ‘निर्वापणः’ के कारण वही शब्द पिछले श्लोकों से समझा जाता है। "
                   "‘कुशकाशयोः’ षष्ठी द्विवचन है: कुश और काश की (जड़)। ‘यवासमूलं’ यवास "
                   "की जड़ है। ‘स्याज्जलमेरका’ में स्यात् + जलम् + एरका जुड़े हैं: "
                   "त् के बाद ‘ज’ आने पर त् ज् बन जाता है। ‘जलम्’ को पानी पढ़ा गया है; "
                   "यह औषध का नाम भी हो सकता है।"),
    "hook": "शीतल सूची: सितालता, वेतस, पद्मक, यष्टि-नामक, ऐन्द्री, नलिन, दूर्वा, यवास-कुश-काश की जड़, जल, एरका।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 27 contains निर्वापणः, the word also found in verse 26. Which effect does it name?",
            ("Cooling, quenching",
             "निर्वापण = cooling, quenching."),
            [("Warming, like कोष्ण in verse 25",
              "Warming is the opposite of निर्वापण."),
             ("Destroying poison, like verse 28",
              "Poison is the subject of verse 28."),
             ("Relieving pain of the flank",
              "That is verse 25.")],
            "The list closes with निर्वापणः स्यात्: it would be cooling.",
            "निर्वापणः = cooling."),
        match(1, "Match each word of verse 27 to its meaning.",
              [["निर्वापणः", "cooling, quenching"], ["मूलम्", "root"],
               ["कुशकाशयोः", "of kuśa and of kāśa"], ["स्यात्", "it would be"]],
              "These words carry the closing statement and the roots.",
              "निर्वापणः = cooling; मूलम् = root; कुशकाशयोः = of kuśa and of kāśa; स्यात् = it would be."),
        fill(2, "कुशकाशयोः names kuśa and kāśa; its ending -ओः marks the ____ number (singular, dual or plural).",
             ["dual", "Dual", "द्विवचन", "द्वि"],
             "-ओः on a name in -अ is the genitive dual: 'of the two'.",
             "-ओः is the genitive (and locative) dual ending of words in -अ. कुशकाशयोः means 'of kuśa and of kāśa'.",
             "-ओः on a word in -अ = dual: of two."),
        mcq("discriminate", 3, "Which is the right split of स्याज्जलमेरका?",
            ("स्यात् + जलम् + एरका: त् before ज becomes ज्",
             "त् + ज is written ज्ज; म् + ए is written मे."),
            [("स्या + ज्जलमेरका", "ज्जलमेरका is not a word."),
             ("स्यात् + जलम् + अरका", "The last name is एरका."),
             ("स्याज् + जलमेरका", "स्याज् is not a word.")],
            "स्याज्जलमेरका = स्यात् ('would be') + जलम् ('water') + एरका.",
            "Final त् + ज → ज्ज."),
        mcq("apply", 4,
            "निर्वापणः is masculine singular, and the verse has no noun for it. Which word is understood?",
            ("प्रदेहः",
             "प्रदेहः is masculine singular, like निर्वापणः, and the neighbouring verses use it."),
            [("जलम्",
              "जलम् is neuter, so it could not take the masculine निर्वापणः."),
             ("एरका",
              "एरका is feminine, so it does not match."),
             ("दूर्वा",
              "दूर्वा is feminine, so it does not match.")],
            "A describing word needs a noun of the same gender and number: the understood noun is प्रदेहः.",
            "निर्वापणः (masculine) agrees with an understood प्रदेहः."),
        mcq("transfer", 5,
            "An invented phrase: यवगोधूमयोश्चूर्णम् (यव = barley, गोधूम = wheat). By the pattern of कुशकाशयोश्च, what does it mean?",
            ("Flour of barley and of wheat",
             "-योः is 'of the two': the flour belongs to both barley and wheat."),
            [("Flour for the barley and wheat eaters",
              "No eaters are named; -योः is 'of the two things'."),
             ("Barley and wheat made of flour",
              "चूर्णम् is the flour; barley and wheat are in the genitive."),
             ("Flour of barley alone",
              "-योः names two things, so wheat is included.")],
            "Genitive dual + a noun = 'of the two': यवगोधूमयोः + चूर्णम्, joined by visarga + च → श्च.",
            "Name + name in -योः = of the two.",
            teaches="A genitive dual in -योः joins two names: 'of kuśa and of kāśa', 'of barley and of wheat'."),
    ],
}

# --------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "शैलेयमेलागुरुणी सकुष्ठे",
    "question": "What does the cool pradeha of verse 28 destroy, and how quickly?",
    "rule": ("शैलेयमेलागुरुणी सकुष्ठे … शीतं निहन्यादचिरात् प्रदेहो विषं = With "
             "śaileya, elā, the two agurus with kuṣṭha, caṇḍā, nata, tvak, suradāru "
             "and rāsnā, the pradeha, applied cool, would quickly destroy poison; "
             "and so would śirīṣa with sindhuvāra."),
    "limits": ("शीतम् is read as 'cool(ly)'. शिरीषस्तु ससिन्धुवारः has no verb and may "
               "also be read as the next pradeha. 'The two agurus with kuṣṭha' has "
               "other readings. Plants are not identified."),
    "explain_hi": ("इस श्लोक का फल ‘विषं निहन्यात्’ है: प्रदेह शीघ्र (‘अचिरात्’) विष का नाश "
                   "करे। ‘शीतम्’ को क्रियाविशेषण (ठण्डा लगाया हुआ) पढ़ा गया है। "
                   "‘निहन्यादचिरात्’ में निहन्यात् + अचिरात् है: त् स्वर से पहले द् बन "
                   "जाता है। ‘शिरीषस्तु ससिन्धुवारः’ में शिरीषः + तु है; ‘सिन्धुवार’ "
                   "के साथ शिरीष को भी वही फल देने वाला समझा गया है। ‘ससिन्धुवारः’ में "
                   "‘स-’ सहित का अर्थ देता है। कई स्थानों पर अन्वय के दो पाठ सम्भव हैं "
                   "(पाठ-टिप्पणी)।"),
    "hook": "शीतल प्रदेह → शीघ्र विष का नाश; और शिरीष + सिन्धुवार।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 28 says the pradeha would quickly destroy something (निहन्यात्). What is it?",
            ("Poison (विष)",
             "विषं निहन्यात् = it would destroy poison."),
            [("Body smell",
              "Body smell is in verse 29."),
             ("Pain in the head",
              "Head pain is in verses 23 and 24."),
             ("Pain in the flank",
              "Flank pain is in verse 25.")],
            "The object of निहन्यात् is विषम्, poison.",
            "विषं निहन्यात् = would destroy poison."),
        match(1, "Match each word of verse 28 to its meaning.",
              [["विषम्", "poison"], ["अचिरात्", "quickly"],
               ["निहन्यात्", "it would destroy"], ["सकुष्ठे", "with kuṣṭha"]],
              "These words carry the main statement.",
              "विषम् = poison; अचिरात् = quickly; निहन्यात् = it would destroy; सकुष्ठे = with kuṣṭha."),
        fill(2, "Without sandhi, निहन्यादचिरात् is निहन्यात् + ____ (type the second word in Devanagari).",
             ["अचिरात्"],
             "निहन्यादचिरात् = निहन्यात् + अचिरात्.",
             "A final त् before a vowel becomes द्: निहन्यात् + अचिरात् is written निहन्यादचिरात्.",
             "Final त् + vowel → द् + vowel."),
        mcq("discriminate", 3, "Which is the right split of शिरीषस्तु?",
            ("शिरीषः + तु: a visarga before त becomes स्",
             "ः + त is written स्त."),
            [("शिरीष + स्तु", "स्तु is not a word."),
             ("शिरीषो + तु", "ओ appears before a voiced consonant, and त is not voiced."),
             ("शिरीषर् + तु", "र् replaces a visarga after इ or उ, not after अ.")],
            "शिरीषस्तु = शिरीषः + तु: 'but, and' joined to śirīṣa.",
            "Visarga + त → स्त."),
        mcq("apply", 4,
            "ससिन्धुवारः has the prefix स-. What does it say about śirīṣa?",
            ("It goes together with sindhuvāra",
             "स- means 'with': śirīṣa with sindhuvāra."),
            [("It replaces sindhuvāra",
              "'With' joins; it does not replace."),
             ("It is the opposite of sindhuvāra",
              "Nothing in the word says opposite."),
             ("It is a disease named sindhuvāra",
              "सिन्धुवार is listed beside śirīṣa as a drug name.")],
            "ससिन्धुवारः = स + सिन्धुवारः: with sindhuvāra.",
            "स- + name = together with that thing."),
        mcq("transfer", 5,
            "An invented line: ज्वरं निहन्यादयं लेपः (ज्वर = fever, अयम् = this). By the pattern of विषं निहन्यात् प्रदेहः, what is destroyed?",
            ("The fever",
             "ज्वरं ends in -म्, the thing acted on, like विषम्; लेपः is the doer."),
            [("The paste",
              "लेपः ends in -ः, the doer."),
             ("Nothing, since this is a question",
              "The line is a statement."),
             ("The physician",
              "No physician is named.")],
            "Masculine nominative -ः names the doer (प्रदेहः, लेपः); neuter accusative -म् names the thing acted on (विषम्, ज्वरम्).",
            "Accusative names what is destroyed; nominative names what destroys.",
            teaches="With निहन्यात्, the accusative (-म् on neuter -अ nouns, as विषम्) names what is destroyed; the nominative (-ः on masculine -अ nouns, as प्रदेहः, लेपः) names what destroys."),
    ],
}

# --------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "शिरीषलामज्जकहेमलोध्रैः",
    "question": "What do the two halves of verse 29 remove, and by what means?",
    "rule": ("शिरीष… प्रघर्षः = a rubbing (pragharṣa) with śirīṣa, lāmajjaka, hema "
             "and lodhra removes skin disorders and sweating; पत्र… प्रदेहः = a "
             "pradeha of patra, ambu, lodhra, abhaya and candana removes body "
             "smell."),
    "limits": ("The first half can also be read as 'removes sweat-related skin "
               "defects'. Lodhra appears in both halves. अम्बु and हेम "
               "have more than one possible sense, and the verse does not choose."),
    "explain_hi": ("इस श्लोक में दो आधे हैं और दो अलग प्रयोग-विधियाँ (प्रघर्ष और प्रदेह)। पहला आधा: शिरीष, लामज्जक, हेम "
                   "और लोध्र से ‘प्रघर्ष’ (रगड़ना) त्वचा के दोष और पसीने को हरता है। "
                   "दूसरा आधा: पत्र, अम्बु, लोध्र, अभया और चन्दन का ‘प्रदेह’ शरीर की "
                   "दुर्गन्ध हरता है। ‘हरः’ का अर्थ ‘हरने वाला’ है और वह समास के अन्त "
                   "में आता है। ‘त्वग्दोष’ में क् घोष द् से पहले ग् हो गया है। "
                   "‘लोध्र’ दोनों आधों में आता है।"),
    "hook": "रगड़ना (शिरीष, लामज्जक, हेम, लोध्र) → त्वचा-दोष और पसीना · प्रदेह (पत्र, अम्बु, लोध्र, अभया, चन्दन) → शरीर की दुर्गन्ध।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 29, the pradeha of patra, ambu, lodhra, abhaya and candana removes what?",
            ("Body smell (शरीरदौर्गन्ध्य)",
             "The second half ends शरीरदौर्गन्ध्यहरः प्रदेहः: remover of body smell."),
            [("Poison",
              "Poison is in verse 28."),
             ("Pain in the head",
              "Head pain is in verses 23 and 24."),
             ("Pain in the flank",
              "Flank pain is in verse 25.")],
            "The second half is for body smell.",
            "शरीरदौर्गन्ध्यहरः = remover of body smell."),
        order(1, "Put the four items of the first half in the order of the verse.",
              ["शिरीष", "लामज्जक", "हेम", "लोध्र"],
              "The first half lists these four, ending with lodhra in the instrumental.",
              "शिरीष → लामज्जक → हेम → लोध्र."),
        fill(2, "The first half names its means with a word meaning 'rubbing': ____ (type it in Devanagari).",
             ["प्रघर्षः", "प्रघर्ष"],
             "The first half ends प्रघर्षः, the second half प्रदेहः.",
             "प्रघर्षः (rubbing) is the means of the first half; the second half uses प्रदेहः. The verse uses two different words for the two applications.",
             "प्रघर्षः = rubbing (first half); प्रदेहः = pradeha (second half)."),
        mcq("discriminate", 3, "Which is the right split of त्वग्दोष?",
            ("त्वक् + दोष: क् before the voiced द becomes ग्",
             "त्वक् is 'skin'; क् + द is written ग्द."),
            [("त्वग + दोष", "The first word is त्वक्, ending in a consonant."),
             ("त्वक् + शोष", "The second word is दोष."),
             ("त्व + ग्दोष", "ग्दोष is not a word.")],
            "त्वग्दोष = त्वक् (skin) + दोष (disorder).",
            "Final क् + voiced consonant → ग्."),
        mcq("apply", 4,
            "Which pairing matches the two halves of verse 29?",
            ("Rubbing: skin disorders and sweating. Pradeha: body smell",
             "The first half ends प्रघर्षः, the second ends प्रदेहः."),
            [("Rubbing: body smell. Pradeha: skin disorders and sweating",
              "That swaps the two halves."),
             ("Rubbing: poison. Pradeha: sweating",
              "Poison is in verse 28."),
             ("Both halves remove body smell",
              "The first half names skin disorders and sweating.")],
            "Each half has its own means and its own effect.",
            "First half: प्रघर्ष → skin and sweat; second: प्रदेह → body smell."),
        mcq("transfer", 5,
            "An invented phrase: दाहहरः प्रदेहः (दाह = burning). By the pattern of शरीरदौर्गन्ध्यहरः, what is it?",
            ("A pradeha that removes burning",
             "A compound ending in -हरः means 'remover of the first part'."),
            [("A pradeha that causes burning",
              "-हरः means removing, not causing."),
             ("A burning that removes the pradeha",
              "The pradeha is the subject, and burning is what is removed."),
             ("A pradeha for the remover",
              "-हरः is the last part of the compound, not a person addressed.")],
            "X-हरः = remover of X: शरीरदौर्गन्ध्यहरः 'remover of body smell', दाहहरः 'remover of burning'.",
            "X-हरः = removing X.",
            teaches="A compound ending in -हरः names what is removed in its first part."),
    ],
}

# --------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "इहात्रिजः सिद्धतमानुवाच",
    "question": "Who declares what in the closing verse of the chapter, and for what purpose?",
    "rule": ("इहात्रिजः … आरग्वधीये जगतो हितार्थम् = Here in the Āragvadhīya, Ātreya, "
             "revered by siddhas and great sages, has declared, for the benefit of "
             "the world, thirty-two most effective powder pradehas that destroy "
             "various diseases."),
    "limits": ("The verse gives the number thirty-two; it does not list them, and "
               "this card does not count them. सिद्धमहर्षिपूज्यः could also mean "
               "'revered by perfected great sages'. The lead-in तत्र श्लोकः is "
               "singular although two lines follow."),
    "explain_hi": ("यह अध्याय का सारांश-श्लोक है; इसके पहले ‘तत्र श्लोकः’ (यहाँ श्लोक है) "
                   "आता है। आत्रेय (‘आत्रिजः’), जो सिद्धों और महर्षियों से पूजनीय हैं, "
                   "आरग्वधीय अध्याय में जगत् के हित के लिए बत्तीस चूर्ण-प्रदेह कह चुके "
                   "हैं, जो अनेक रोगों का नाश करने वाले हैं। ‘सिद्धतमान्’ ‘सबसे सिद्ध/"
                   "प्रमाणित’ है और ‘चूर्णप्रदेहान्’ का विशेषण है। ‘द्वात्रिंशतम्’ का अर्थ "
                   "बत्तीस है। ‘हितार्थम्’ का अर्थ ‘हित के लिए’ है।"),
    "hook": "आत्रेय ने आरग्वधीय में जगत् के हित के लिए बत्तीस चूर्ण-प्रदेह कहे, जो अनेक रोगों का नाश करें।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 30 sums up the chapter. Who is said to have declared the pradehas?",
            ("Ātreya, the son of Atri (आत्रिजः)",
             "इहात्रिजः = इह + आत्रिजः; आत्रिजः is the son of Atri, Ātreya, who said (उवाच) them."),
            [("A physician of a later age, not named in the verse",
              "The verse names the speaker: आत्रिजः."),
             ("The pupil who asks the questions",
              "No pupil is named in this verse."),
             ("The world (जगत्)",
              "जगतः is the world, for whose benefit they are declared, not the speaker.")],
            "आत्रिजः is the subject of उवाच: Ātreya declared the pradehas.",
            "आत्रिजः (nominative) + उवाच = Ātreya said."),
        match(1, "Match each word of verse 30 to its meaning.",
              [["इह", "here"], ["उवाच", "said, declared"],
               ["जगतः", "of the world"], ["हितार्थम्", "for the benefit"]],
              "These words say where, who did what, and why.",
              "इह = here; उवाच = said, declared; जगतः = of the world; हितार्थम् = for the benefit."),
        fill(2, "The word meaning 'thirty-two' is ____ (type it in Devanagari).",
             ["द्वात्रिंशतं", "द्वात्रिंशतम्"],
             "Line 1 has द्वात्रिंशतं.",
             "द्वात्रिंशतम् is a number word in the accusative singular, standing beside the plural चूर्णप्रदेहान्: 'the thirty-two (pradehas)'.",
             "द्वात्रिंशतम् = thirty-two."),
        mcq("discriminate", 3,
            "सिद्धतमान् ends in -आन्, an accusative plural. Which word of the verse does it describe?",
            ("चूर्णप्रदेहान्",
             "Both are accusative plural masculine: 'the most effective powder pradehas'."),
            [("द्वात्रिंशतम्",
              "द्वात्रिंशतम् is singular, so it does not match."),
             ("जगतः",
              "जगतः is a genitive singular, so it does not match."),
             ("आत्रिजः",
              "आत्रिजः is a nominative singular, so it does not match.")],
            "A describing word copies the case and number of its noun: सिद्धतमान् goes with चूर्णप्रदेहान्.",
            "सिद्धतमान् + चूर्णप्रदेहान् = the most effective powder pradehas."),
        multi("apply", 4,
              "Which statements does verse 30 itself make about the pradehas?",
              [("There are thirty-two of them", "Right: द्वात्रिंशतम्."),
               ("They are in powder form", "Right: चूर्ण-प्रदेहान्."),
               ("They destroy various diseases", "Right: विविधामयघ्नान्."),
               ("They are declared for the benefit of the world", "Right: जगतो हितार्थम्."),
               ("Each one cures exactly one named disease", "The verse says 'various diseases' and names none."),
               ("They were first taught by Indra", "Indra is not named in this verse.")],
              [0, 1, 2, 3],
              "The verse gives the number, the powder form, the effect on various diseases, and the purpose.",
              "Verse 30: 32 powder pradehas, destroying various diseases, for the world's benefit."),
        mcq("transfer", 5,
            "An invented phrase: जनानां सुखार्थम् (जन = people, सुख = happiness). By the pattern of जगतो हितार्थम्, what does it mean?",
            ("For the happiness of the people",
             "-अर्थम् means 'for the sake of'; the genitive names whose benefit it is."),
            [("From the happiness of the people",
              "'From' would need a different ending."),
             ("The people who make happiness",
              "-अर्थम् does not name a doer."),
             ("The happiness of people has no purpose",
              "-अर्थम् states a purpose, not its absence.")],
            "Genitive + X-अर्थम् = for the sake of X, for those people: जगतः + हितार्थम्, जनानाम् + सुखार्थम्.",
            "Genitive + X-अर्थम् = for X of those.",
            teaches="A word ending in -अर्थम् states a purpose: 'for the sake of' what comes before it."),
    ],
}


NOTES_HI = {
    "21": ("पाठ-संशय नहीं है। ‘मधुकं’ (छोटा उ) और ‘मधूकं’ (दीर्घ ऊ) अलग शब्द छपे हैं। "
           "‘सितोपलां’ = सित + उपलां (अ + उ → ओ)। ‘सरक्ते’ = स + रक्ते, बहुव्रीहि; ‘पवने’ के साथ "
           "सप्तमी में मेल खाता है, और टिप्पणी के अनुसार इसे किसी नामित रोग से नहीं जोड़ा गया। "
           "‘उभे शताह्वे’: दोनों शताह्वा, जिनके नाम श्लोक में नहीं हैं।"),
    "22": ("पाठ-संशय नहीं है। ‘मधुशेष’ का अर्थ अनिश्चित है (शाब्दिक: मधु का बचा हुआ भाग); इसे शाब्दिक रखा "
           "गया है। ‘सिद्धम्’ से यह नहीं पता चलता कि घृत किसके साथ पकाया जाए। ‘रक्तानिलार्तिम्’ = "
           "रक्त + अनिल + आर्ति (अ + अ → आ, अ + आ → आ); ‘रक्त और वात की पीड़ा’ या ‘रक्त और वात से "
           "पीड़ा’ दोनों पढ़ा जा सकता है। ‘पयश्च’ = पयः + च (विसर्ग + च → श्च); ‘सर्षभकं’ = स + ऋषभकं (अ + ऋ → अर्)।"),
    "23": ("पाठ-संशय नहीं है। ‘नत’ विशेषण (‘झुका’) भी हो सकता है, पर औषध-सूची में इसे नाम माना गया। "
           "‘नतोत्पलं’ को नत + उत्पल (द्वन्द्व) पढ़ा गया है; दोनों मिलकर एक नाम भी हो सकते हैं। "
           "‘प्रदेहो गोधूमचूर्णं’ में प्रदेहः + गोधूम… (अः + घोष → ओ)। दोनों आधों में क्रिया "
           "अनकही है; पहले आधे में ‘सघृतम्’ गेहूँ के आटे के साथ जुड़ा है।"),
    "24": ("पाठ-संकेत (text_flag): ‘लोहैरका…’ में ‘लोह’ के स्थान पर ‘लोध्र’ (लोध्रैरका…) सम्भव है, क्योंकि "
           "ऐसी सूचियों में लोध्र सामान्य है और ‘लोह’ औषध-नाम के रूप में संदिग्ध है; दोनों के अक्षर "
           "बराबर हैं, इसलिए छन्द निर्णय नहीं देता। ‘लोह’ + ‘एरका’ → ‘लोहैरका’ (अ + ए → ऐ)। तृतीया "
           "बहुवचन का कोई क्रियापद नहीं है; उसे आगे की सामग्री पढ़ा गया है। ‘यष्ट्याह्वम्’ = यष्टि + "
           "आह्वम्: श्लोक में ‘यष्टि’ नामक द्रव्य का कोई पहचान नहीं दी गई।"),
    "25": ("पाठ-संशय नहीं है। ‘द्वे’ स्त्रीलिङ्ग द्विवचन है और ‘शताह्वे’ से मेल खाता है; ‘देवदारूणि’ "
           "नपुंसक बहुवचन है, इसलिए उसके साथ ‘द्वे’ नहीं चल सकता। इसे ‘कई देवदारु’ पढ़ा गया है; "
           "‘दो देवदारु’ वाला पाठ व्याकरण में खिंचा हुआ है। ‘कोष्णम्’ = क + उष्णम् (अ + उ → ओ)। "
           "‘आलेपनम्’ यहाँ तैयार वस्तु का नाम है। ‘सतैलमालेपनं’ = सतैलम् + आलेपनम्।"),
    "26": ("पाठ-संकेत (text_flag): पहली पंक्ति के एक ही शब्द में ‘प्रपौण्डरीकाण्यमृणाल…’ है। सामान्य सन्धि "
           "में ‘प्रपौण्डरीकाणि मृणाललोध्रम्’ होता; छपे पाठ में अतिरिक्त ‘अ’ है और ‘अमृणाल’ का कोई "
           "स्पष्ट अर्थ नहीं है, इसलिए पाठ-दोष सम्भव है। छन्द (२२ अक्षर) निर्णय नहीं देता। यहाँ "
           "‘प्रपौण्डरीकाणि + मृणाललोध्रम्’ पढ़ा गया है। ‘मृणाल’ का अर्थ (कमल की डण्डी/तन्तु) पक्का है। "
           "‘निर्वापण’ = शीतल करने वाला, ताप शान्त करने वाला।"),
    "27": ("पाठ-संशय नहीं है। श्लोक में ‘प्रदेह’ शब्द नहीं है; पुल्लिङ्ग ‘निर्वापणः’ पास के श्लोकों से "
           "‘प्रदेहः’ की ओर इशारा करता है। ‘कुशकाशयोश्च’ = कुशकाशयोः + च, षष्ठी द्विवचन; ‘मूलम्’ उसी के "
           "साथ पढ़ा गया है। ‘स्याज्जलमेरका’ = स्यात् + जलम् + एरका। ‘जलम्’ पानी भी हो सकता है और "
           "‘जल’ नाम का द्रव्य भी। ‘सितालता’ को ‘सिता-लता’ भी पढ़ा जा सकता है।"),
    "28": ("पाठ-संशय नहीं है, पर कई अन्वय खुले हैं। (१) ‘अगुरुणी’ और ‘सकुष्ठे’ नपुंसक द्विवचन हैं: ‘दो "
           "अगरु, कुष्ठ सहित’। ‘सकुष्ठे’ सप्तमी एकवचन नहीं हो सकता। (२) ‘शीतम्’ नपुंसक है, इसलिए क्रिया-"
           "विशेषण (ठण्डा) पढ़ा गया; ‘प्रदेहः’ से मेल के लिए ‘शीतः’ चाहिए था। (३) ‘शिरीषस्तु "
           "ससिन्धुवारः’ में क्रिया नहीं है; इसे ‘शिरीष भी सिन्धुवार सहित (विष का नाश करे)’ पढ़ा गया, पर "
           "इसे अगला स्वतन्त्र प्रदेह भी पढ़ा जा सकता है। ‘निहन्यादचिरात्’ = निहन्यात् + अचिरात्; "
           "‘शिरीषस्तु’ = शिरीषः + तु।"),
    "29": ("पाठ-संशय नहीं है। ‘त्वग्दोषसंस्वेदहरः’ को ‘त्वचा के दोष और पसीने का हरने वाला’ पढ़ा गया; "
           "‘पसीने से हुए त्वचा-दोष को हरने वाला’ भी सम्भव है। ‘लोध्रैस्त्वग्…’ = लोध्रैः + त्वक्… "
           "(विसर्ग + त → स्त); ‘त्वग्दोष’ में क् → ग्। ‘पत्राम्बुलोध्राभयचन्दनानि’ में अ + अ → आ दो बार। "
           "अम्बु और हेम के अर्थ श्लोक से तय नहीं होते। ‘लोध्र’ दोनों आधों में है।"),
    "30": ("पाठ-संशय नहीं है। ‘सिद्धतमान्’ (द्वितीया बहुवचन) दूसरी पंक्ति के ‘चूर्णप्रदेहान्’ से अन्वित है। "
           "‘द्वात्रिंशतम्’ द्वितीया एकवचन संख्या-वाचक है जो बहुवचन संज्ञा के साथ समानाधिकरण में "
           "आया है। ‘सिद्धमहर्षिपूज्यः’: सिद्धों और महर्षियों से पूज्य (द्वन्द्व), या ‘सिद्ध महर्षियों "
           "से पूज्य’ - दोनों पाठ सम्भव हैं। ‘इहात्रिजः’ = इह + आत्रिजः (अ + आ → आ); ‘सिद्धतमानुवाच’ = "
           "सिद्धतमान् + उवाच; ‘तत्र श्लोकः’ एकवचन है, यद्यपि दो पंक्तियाँ आती हैं।"),
}


AIDS = {
    "21": {
        "frame": "क्या बनाएँ: प्रदेह (कुर्यात्) · किनसे: दोनों शताह्वा, मधुक, मधूक, बला, प्रियाल, कशेरुक, घृत, विदारी, मिश्री · किसमें: रक्त-सहित वात (पवने सरक्ते)।",
        "diagram": {"groups": [
            _g("पंक्ति १", "उभे शताह्वे मधुकं मधूकं बलां प्रियालं च कशेरुकं च"),
            _g("पंक्ति २", "घृतं विदारीं च सितोपलां च कुर्यात् प्रदेहं पवने सरक्ते")]},
        "sandhi": "अ + उ → ओ: सित + उपलां → सितोपलां · बाकी शब्द अलग छपे हैं; ‘बलां प्रियालं’ में अनुस्वार (म्) शब्द के अन्त में है।",
        "chunks": "उभे शताह्वे मधुकं मधूकं | बलां प्रियालं च कशेरुकं च ‖ घृतं विदारीं च सितोपलां च | कुर्यात् प्रदेहं पवने सरक्ते।",
    },
    "22": {
        "frame": "किनसे: रास्ना, गुडूची, मधुक, दोनों बला (जीवक, ऋषभक सहित), दूध, सिद्ध घृत, मधुशेष · क्या करे: प्रदेह दूर करे (प्रणुदेत्) · क्या: रक्त और वात की पीड़ा।",
        "diagram": {"groups": [
            _g("पंक्ति १", "रास्ना गुडूची मधुकं बले द्वे सजीवकं सर्षभकं पयश्च"),
            _g("पंक्ति २", "घृतं च सिद्धं मधुशेषयुक्तं रक्तानिलार्तिं प्रणुदेत् प्रदेहः")]},
        "pegs": "मेरा बनाया चित्र: एक कटोरे में दूध और घी, उसके पास दो छोटी पुड़ियाँ (जीवक, ऋषभक) जो ‘सहित’ का निशान लिए हैं, और एक तीर जो पीड़ा को बाहर धकेलता है (प्रणुदेत्)। केवल याद के लिए।",
        "sandhi": "विसर्ग + च → श्च: पयः + च → पयश्च · अ + ऋ → अर्: स + ऋषभकं → सर्षभकं · अ + अ → आ और अ + आ → आ: रक्त + अनिल + आर्ति → रक्तानिलार्ति।",
        "chunks": "रास्ना गुडूची मधुकं बले द्वे | सजीवकं सर्षभकं पयश्च ‖ घृतं च सिद्धं मधुशेषयुक्तं | रक्तानिलार्तिं प्रणुदेत् प्रदेहः।",
    },
    "23": {
        "frame": "दो आधे, दो रोग: (१) वाते सरक्ते → घृत सहित गेहूँ का आटा और बकरी का दूध · (२) शिरोरुजायाम् → नत, उत्पल, चन्दन, कुष्ठ, घृत सहित।",
        "diagram": {"groups": [
            _g("पंक्ति १", "वाते सरक्ते सघृतं प्रदेहो गोधूमचूर्णं छगलीपयश्च"),
            _g("पंक्ति २", "नतोत्पलं चन्दनकुष्ठयुक्तं शिरोरुजायां सघृतं प्रदेहः")]},
        "contrast": "रक्त-सहित वात: गेहूँ का आटा, बकरी का दूध, घृत ↔ सिर-दर्द: नत, उत्पल, चन्दन, कुष्ठ, घृत।",
        "sandhi": "अः + घोष → ओ (अ के बाद): प्रदेहः + गोधूमचूर्णं → प्रदेहो गोधूमचूर्णं · अ + उ → ओ: नत + उत्पलं → नतोत्पलं · विसर्ग + च → श्च: पयः + च → पयश्च।",
        "chunks": "वाते सरक्ते सघृतं प्रदेहो | गोधूमचूर्णं छगलीपयश्च ‖ नतोत्पलं चन्दनकुष्ठयुक्तं | शिरोरुजायां सघृतं प्रदेहः।",
    },
    "24": {
        "frame": "रोग: सिर-दर्द (शिरोरुजायाम्) · प्रदेह: घृत सहित · सूची: प्रपौण्डरीक, सुरदारु, कुष्ठ, यष्टि-नामक, एला, कमल–उत्पल, और लोह, एरका, पद्मक, चोरक के साथ।",
        "diagram": {"groups": [
            _g("पंक्ति १", "प्रपौण्डरीकं सुरदारु कुष्ठं यष्ट्याह्वमेला कमलोत्पले च"),
            _g("पंक्ति २", "शिरोरुजायां सघृतः प्रदेहो लोहैरकापद्मकचोरकैश्च")]},
        "sandhi": "इ + आ → या: यष्टि + आह्वम् → यष्ट्याह्वम् · अ + उ → ओ: कमल + उत्पले → कमलोत्पले · अः + घोष → ओ: प्रदेहः + लोहैरका… → प्रदेहो लोहैरका… · अ + ए → ऐ: लोह + एरका → लोहैरका · विसर्ग + च → श्च: चोरकैः + च → चोरकैश्च।",
        "chunks": "प्रपौण्डरीकं सुरदारु कुष्ठं | यष्ट्याह्वमेला कमलोत्पले च ‖ शिरोरुजायां सघृतः प्रदेहो | लोहैरकापद्मकचोरकैश्च।",
    },
    "25": {
        "frame": "रोग: पार्श्व के दर्द (पार्श्वरुजासु) · रूप: गुनगुना आलेपन, घृत और तेल सहित · सूची: रास्ना, दो हरिद्रा, नलद, दो शताह्वा, देवदारु, मिश्री, जीवन्ती की जड़।",
        "diagram": {"groups": [
            _g("पंक्ति १", "रास्ना हरिद्रे नलदं शताह्वे द्वे देवदारूणि सितोपला च"),
            _g("पंक्ति २", "जीवन्तिमूलं सघृतं सतैलमालेपनं पार्श्वरुजासु कोष्णम्")]},
        "sandhi": "क + उष्णम् → कोष्णम् (अ + उ → ओ) · सतैलम् + आलेपनम् → सतैलमालेपनम् (म् + आ जुड़कर मा) · सित + उपला → सितोपला (अ + उ → ओ)।",
        "chunks": "रास्ना हरिद्रे नलदं शताह्वे | द्वे देवदारूणि सितोपला च ‖ जीवन्तिमूलं सघृतं | सतैलमालेपनं पार्श्वरुजासु कोष्णम्।",
    },
    "26": {
        "frame": "फल: निर्वापण (शीतल करने वाला) · रूप: घृत सहित प्रदेह · सूची: शैवाल, पद्म, उत्पल, वेत्र, तुङ्ग, प्रपौण्डरीक, मृणाल, लोध्र, प्रियङ्गु, कालेयक, चन्दन। कोई रोग नहीं।",
        "diagram": {"groups": [
            _g("पंक्ति १ (एक लम्बा शब्द)", "शैवालपद्मोत्पलवेत्रतुङ्गप्रपौण्डरीकाण्यमृणाललोध्रम्"),
            _g("पंक्ति २", "प्रियङ्गुकालेयकचन्दनानि निर्वापणः स्यात् सघृतः प्रदेहः")]},
        "sandhi": "अ + उ → ओ: पद्म + उत्पल → पद्मोत्पल · पाठ-संकेत: ‘प्रपौण्डरीकाण्यमृणाल’ में अतिरिक्त ‘अ’; सामान्य रूप ‘प्रपौण्डरीकाणि मृणाल…’ होता · बाकी शब्द अलग छपे हैं।",
        "chunks": "शैवाल | पद्म | उत्पल | वेत्र | तुङ्ग | प्रपौण्डरीक | मृणाल | लोध्र ‖ प्रियङ्गु कालेयक चन्दन | निर्वापणः स्यात् सघृतः प्रदेहः (पहला शब्द इन भागों में बँटा है; छपे शब्द में पद्मोत्पल और प्रपौण्डरीकाण्य… हैं)।",
    },
    "27": {
        "frame": "फल: निर्वापण (शीतल करने वाला) · रूप: प्रदेह (अनकहा) · सूची: सितालता, वेतस, पद्मक, यष्टि-नामक, ऐन्द्री, नलिन, दूर्वा, यवास-कुश-काश की जड़, जल, एरका।",
        "diagram": {"groups": [
            _g("पंक्ति १", "सितालतावेतसपद्मकानि यष्ट्याह्वमैन्द्री नलिनानि दूर्वा"),
            _g("पंक्ति २", "यवासमूलं कुशकाशयोश्च निर्वापणः स्याज्जलमेरका च")]},
        "sandhi": "विसर्ग + च → श्च: कुशकाशयोः + च → कुशकाशयोश्च · त् + ज → ज्ज: स्यात् + जलम् → स्याज्जलम् · म् + ए → मे: जलम् + एरका → जलमेरका · इ + आ → या: यष्टि + आह्वम् → यष्ट्याह्वम्।",
        "chunks": "सितालतावेतसपद्मकानि | यष्ट्याह्वमैन्द्री नलिनानि दूर्वा ‖ यवासमूलं कुशकाशयोश्च | निर्वापणः स्याज्जलमेरका च।",
    },
    "28": {
        "frame": "क्या हरे: विष (निहन्यात्) · कैसे: ठण्डा लगाया प्रदेह, शीघ्र (अचिरात्) · सूची: शैलेय, एला, दो अगरु (कुष्ठ सहित), चण्डा, नत, त्वक्, सुरदारु, रास्ना; और शिरीष सिन्धुवार सहित।",
        "diagram": {"groups": [
            _g("पंक्ति १", "शैलेयमेलागुरुणी सकुष्ठे चण्डा नतं त्वक् सुरदारु रास्ना"),
            _g("पंक्ति २", "शीतं निहन्यादचिरात् प्रदेहो विषं शिरीषस्तु ससिन्धुवारः")]},
        "sandhi": "त् + स्वर → द्: निहन्यात् + अचिरात् → निहन्यादचिरात् · अः + घोष → ओ: प्रदेहः + विषं → प्रदेहो विषं · विसर्ग + त → स्त: शिरीषः + तु → शिरीषस्तु · आ + अ → आ: एला + अगुरुणी → एलागुरुणी।",
        "chunks": "शैलेयमेलागुरुणी सकुष्ठे | चण्डा नतं त्वक् सुरदारु रास्ना ‖ शीतं निहन्यादचिरात् प्रदेहो | विषं शिरीषस्तु ससिन्धुवारः।",
    },
    "29": {
        "diagram": {"groups": [
            _g("पंक्ति १", "शिरीषलामज्जकहेमलोध्रैस्त्वग्दोषसंस्वेदहरः प्रघर्षः"),
            _g("पंक्ति २", "पत्राम्बुलोध्राभयचन्दनानि शरीरदौर्गन्ध्यहरः प्रदेहः")]},
        "contrast": "प्रघर्ष (शिरीष, लामज्जक, हेम, लोध्र) → त्वचा-दोष और पसीना ↔ प्रदेह (पत्र, अम्बु, लोध्र, अभया, चन्दन) → शरीर की दुर्गन्ध।",
        "sandhi": "विसर्ग + त → स्त: लोध्रैः + त्वक् → लोध्रैस्त्वक् · क् + घोष → ग्: त्वक् + दोष → त्वग्दोष · अ + अ → आ: पत्र + अम्बु → पत्राम्बु, लोध्र + अभय → लोध्राभय।",
        "chunks": "शिरीषलामज्जकहेमलोध्रैः | त्वग्दोषसंस्वेदहरः प्रघर्षः ‖ पत्राम्बुलोध्राभयचन्दनानि | शरीरदौर्गन्ध्यहरः प्रदेहः (छपा रूप: ‘…लोध्रैस्त्वग्दोष…’)।",
    },
    "30": {
        "frame": "कौन: आत्रेय (आत्रिजः), सिद्धों और महर्षियों से पूजित · कहाँ: आरग्वधीय में · क्या: बत्तीस चूर्ण-प्रदेह, अनेक रोगों का नाश करने वाले · क्यों: जगत् के हित के लिए।",
        "diagram": {"groups": [
            _g("पंक्ति १", "इहात्रिजः सिद्धतमानुवाच द्वात्रिंशतं सिद्धमहर्षिपूज्यः"),
            _g("पंक्ति २", "चूर्णप्रदेहान् विविधामयघ्नानारग्वधीये जगतो हितार्थम्")]},
        "sandhi": "अ + आ → आ: इह + आत्रिजः → इहात्रिजः · न् + उ: सिद्धतमान् + उवाच → सिद्धतमानुवाच (अन्तिम न् स्वर से जुड़ता है) · न् + आ: विविधामयघ्नान् + आरग्वधीये → विविधामयघ्नानारग्वधीये।",
        "chunks": "इहात्रिजः सिद्धतमानुवाच | द्वात्रिंशतं सिद्धमहर्षिपूज्यः ‖ चूर्णप्रदेहान् विविधामयघ्नान् | आरग्वधीये जगतो हितार्थम्।",
    },
}


IMAGE_SPECS = {
    ("23", "contrast"): {
        "file": "ch3-two-conditions-23.svg",
        "alt": "Table of verse 23 with two rows: Vāta with blood uses wheat flour, goat's milk and ghee; head pain uses nata, utpala, candana, kuṣṭha and ghee.",
        "type": "table",
        "title": "श्लोक २३: दो रोग, दो प्रदेह",
        "heads": ["रोग", "द्रव्य"],
        "rows": [["रक्त-सहित वात", "गेहूँ का आटा, बकरी का दूध, घृत"],
                 ["सिर-दर्द", "नत, उत्पल, चन्दन, कुष्ठ, घृत"]],
    },
    ("29", "contrast"): {
        "file": "ch3-two-halves-29.svg",
        "alt": "Table of verse 29 with two rows: a rubbing with shirisha, lamajjaka, hema and lodhra removes skin disorders and sweating; a pradeha of patra, ambu, lodhra, abhaya and candana removes body smell.",
        "type": "table",
        "title": "श्लोक २९: प्रघर्ष और प्रदेह",
        "heads": ["क्या हरे", "द्रव्य"],
        "rows": [["प्रघर्ष: त्वचा-दोष, पसीना", "शिरीष, लामज्जक, हेम, लोध्र"],
                 ["प्रदेह: शरीर की दुर्गन्ध", "पत्र, अम्बु, लोध्र, अभया, चन्दन"]],
    },
}
