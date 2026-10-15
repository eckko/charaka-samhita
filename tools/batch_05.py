"""Units 41-50 of Charaka Samhita Su. 1 (batch 05)."""
from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}

# --------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "हिताहितं सुखं दुखम्",
    "question": "What does verse 41 say Āyurveda is, and what must be stated in it?",
    "rule": ("Āyurveda is that in which are stated: life as beneficial or "
             "harmful, happy or unhappy; what is wholesome and unwholesome "
             "for it; its measure; and life itself."),
    "limits": ("The verse defines Āyurveda by the topics stated in it; it "
               "does not list the topics of any later chapter. The printed "
               "दुखम् is probably a slip for दुःखम्."),
    "explain_hi": ("यह श्लोक आयुर्वेद की परिभाषा देता है: आयुर्वेद वह है जिसमें "
                   "आयु के चार रूप (हित, अहित, सुख, दुःख), उस आयु के लिए क्या "
                   "हितकर और क्या अहितकर है, आयु का मान (परिमाण) और स्वयं आयु "
                   "कहे गए हों। ‘यत्र’ का अर्थ ‘जहाँ, जिसमें’ है और ‘उक्तम्’ का "
                   "‘कहा गया’; अन्त में ‘सः उच्यते’ = ‘वह कहलाता है’। यानी "
                   "आयुर्वेद का नाम ‘आयु का वेद’ इसी विषय-सूची से समझ में आता है।"),
    "hook": "आयुर्वेद = जहाँ ये कहे जाएँ: आयु के हित-अहित, सुख-दुःख · क्या हितकर, क्या अहितकर · मान · और स्वयं आयु।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 41 says Āyurveda is the science in which certain things about life are stated. Which do you expect to be among them?",
            ("What is wholesome and unwholesome for life",
             "The verse names what is good and bad for life, and also its measure."),
            [("The names of the kings of a country",
              "Kings are not mentioned in this verse."),
             ("The rules of a fire sacrifice",
              "No sacrifice is mentioned in this verse."),
             ("The mountains of the Himalaya",
              "The mountains were only the place of the meeting in verse 7.")],
            "The verse lists life, its happy and unhappy kinds, its measure and what is good or bad for it.",
            "Āyurveda is where life and what is wholesome or unwholesome for it are stated."),
        match(1, "Match each word of the verse to its meaning.",
              [["हिताहितम्", "beneficial and harmful"], ["तस्य", "its, for it"],
               ["सुखम्", "happy"], ["मानम्", "measure"]],
              "These four words describe life and what is stated about it.",
              "हिताहितम् = beneficial and harmful; तस्य = its, for it; सुखम् = happy; मानम् = measure."),
        fill(2, "In the last line the word for 'is stated' is ____ (type it in Devanagari, as it is written before the sandhi).",
             ["उक्तम्", "उक्तं"],
             "The line is यत्र + उक्तम्, joined as यत्रोक्तम्: 'where it is stated'.",
             "उक्तम् is the past participle of √वच् ('to say'): said, stated. The same root gives उच्यते, 'is called', at the end of the verse.",
             "उक्तम् = said, stated (√वच्)."),
        mcq("discriminate", 3, "Which is the right split of यत्रोक्तम्?",
            ("यत्र + उक्तम्", "अ + उ join as ओ, so यत्र + उक्तम् is written यत्रोक्तम्."),
            [("यत्रो + क्तम्", "क्तम् is not a word."),
             ("यत् + रोक्तम्", "रोक्तम् is not a word."),
             ("यत्र + ओक्तम्", "The second word begins with उ, not ओ.")],
            "यत्रोक्तम् = यत्र ('where') + उक्तम् ('stated').",
            "अ + उ → ओ: यत्र + उक्तम् = यत्रोक्तम्."),
        multi("apply", 4, "Which of these does verse 41 say are stated in Āyurveda?",
              [("Happy and unhappy life", "Right: sukham and duḥkham are named."),
               ("The measure of life", "Right: mānam is named."),
               ("What is wholesome and unwholesome for life", "Right: tasya hitāhitam is named."),
               ("The names of medicinal herbs", "No herb is named in this verse."),
               ("The genealogy of the sages", "The verse says nothing of any genealogy.")],
              [0, 1, 2],
              "The verse names life, its happy and unhappy kinds, its measure, and what is wholesome or unwholesome for it.",
              "Verse 41 lists the topics of Āyurveda: life, its kinds, its measure, its wholesome and unwholesome things."),
        mcq("transfer", 5,
            "An invented line reads यत्र पाकविधिरुक्तस्तत्पाकशास्त्रमुच्यते (पाकविधि cooking method, शास्त्र science). By the pattern of verse 41, what does it say?",
            ("The science of cooking is that in which the cooking method is stated",
             "यत्र … उक्तम् … उच्यते: 'where it is stated, that is called'. This is the same frame as the definition of Āyurveda."),
            [("The science of cooking is named after a place called Yatra",
              "यत्र is 'where', not a place name."),
             ("The cooking method will be stated tomorrow",
              "उक्त is a past form: 'stated', not a future."),
             ("The cooking method is a secret that is not stated",
              "उक्तः means it is stated.")],
            "The frame 'where X is stated, that is called Y' defines a science by its contents.",
            "यत्र … उक्तम् … उच्यते = where … is stated, that is called ….",
            teaches="You can read a new definition built on the frame यत्र … उक्तम् … उच्यते: the thing named at the end is the science that states the listed contents."),
    ],
}

# --------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "शरीरेन्द्रियसत्त्वात्मसंयोगः",
    "question": "What is life (āyus), and by what other names is it called?",
    "rule": ("Life = the union (saṃyoga) of body, sense faculties, mind "
             "(sattva) and self; its synonyms are dhāri, jīvita, nityaga "
             "and anubandha."),
    "limits": ("The verse gives the four synonyms without explaining each; "
               "nityaga is read as 'ever-moving' or 'ever-present', anubandha "
               "as 'continuity'. Those are glosses, not stated in the verse."),
    "explain_hi": ("यह आयु की परिभाषा है: शरीर, इन्द्रिय, सत्त्व (मन) और आत्मा "
                   "का संयोग ही आयु है; इनमें से कोई एक अकेला नहीं। दूसरी "
                   "पंक्ति में उसके पर्यायवाची नाम हैं: धारि, जीवित, नित्यग "
                   "और अनुबन्ध। ‘पर्यायैः’ का अर्थ है ‘पर्यायवाची शब्दों "
                   "से’। श्लोक ४१ में ‘आयुः’ जिसकी बात थी, उसकी परिभाषा यहाँ "
                   "आती है।"),
    "hook": "आयु = संयोग (शरीर · इन्द्रिय · सत्त्व · आत्मा); नाम: धारि · जीवित · नित्यग · अनुबन्ध।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 42 defines life (āyus) as a union. Which four things does it unite?",
            ("Body, sense faculties, mind and self",
             "These are the four members of the compound शरीर-इन्द्रिय-सत्त्व-आत्म."),
            [("Breath, blood, bone and marrow",
              "None of these is named in the verse."),
             ("Earth, water, fire and air",
              "The verse names no elements."),
             ("Food, sleep, exercise and rest",
              "The verse names none of these.")],
            "Life is the union of शरीर, इन्द्रिय, सत्त्व and आत्मा.",
            "Life = union of body, senses, mind, self."),
        match(1, "Match each member of the union to its meaning.",
              [["शरीरम्", "body"], ["इन्द्रियम्", "sense faculties"],
               ["सत्त्वम्", "mind"], ["आत्मा", "self"]],
              "These four are what the union joins.",
              "शरीरम् = body; इन्द्रियम् = sense faculties; सत्त्वम् = mind (here); आत्मा = self."),
        fill(2, "The word for 'union' in the verse is ____ (type it in Devanagari).",
             ["संयोगः", "संयोग", "संयोगो", "सम्योगः"],
             "The first line ends शरीरेन्द्रियसत्त्वात्मसंयोगः: the union of the four.",
             "संयोगः is formed from सम् + √युज् ('to join'). The verse defines life as this joining, not as any one of the four alone.",
             "संयोगः = union, joining."),
        mcq("discriminate", 3, "Which is the right split of शरीरेन्द्रिय?",
            ("शरीर + इन्द्रिय", "अ + इ join as ए, so शरीर + इन्द्रिय is written शरीरेन्द्रिय."),
            [("शरीरे + न्द्रिय", "न्द्रिय is not a word."),
             ("शरीर + एन्द्रिय", "The second word begins with इ, not ए."),
             ("शरी + रेन्द्रिय", "Neither part is a word.")],
            "शरीरेन्द्रिय = शरीर ('body') + इन्द्रिय ('sense faculties').",
            "अ + इ → ए: शरीर + इन्द्रिय = शरीरेन्द्रिय."),
        multi("apply", 4, "Which of these does the verse give as other names (synonyms) of life?",
              [("धारि", "Right: dhāri is the first synonym."),
               ("नित्यगः", "Right: nityaga is a synonym."),
               ("अनुबन्धः", "Right: anubandha is a synonym."),
               ("शरीरम्", "The body is one member of the union, not a name for life."),
               ("इन्द्रियम्", "The senses are one member of the union, not a name for life.")],
              [0, 1, 2],
              "Four synonyms are given (dhāri, jīvita, nityaga, anubandha); body and senses are members of the union.",
              "पर्याय (synonyms) of life: धारि, जीवित, नित्यग, अनुबन्ध."),
        mcq("transfer", 5,
            "An invented line defines a boat-crew as the union of captain, oarsmen, drummer and boat. By the pattern of verse 42, what is the boat-crew?",
            ("The union of all four, not any one of them",
             "As life is the union of the four members, the crew is their joining."),
            [("The captain alone", "One member alone is not the union."),
             ("The boat alone", "One member alone is not the union."),
             ("Any one of the four, whichever you choose",
              "The definition requires all four together.")],
            "A definition by saṃyoga names the joining of all members.",
            "Definition by saṃyoga = all the members together.",
            teaches="When a verse defines something as a saṃyoga of several parts, no single part is the thing; the joining of all is."),
    ],
}

# --------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "तस्यायुषः पुण्यतमो वेदः",
    "question": "How do the knowers of the Vedas regard Āyurveda, and what will now be taught?",
    "rule": ("The Veda (science) of that life is held by the knowers of the "
             "Vedas to be the most holy; what is beneficial to human beings "
             "in both worlds will now be taught."),
    "limits": ("Medium confidence. The verse does not say which two worlds "
               "are meant (this world and the next is the usual reading) "
               "nor what exactly will be taught; यत् is neuter, so it does "
               "not agree with the masculine वेदः."),
    "explain_hi": ("पिछले श्लोकों में आयु की परिभाषा आई; अब ‘उस आयु का वेद’ "
                   "यानी आयुर्वेद वेदज्ञों द्वारा ‘पुण्यतम’ माना गया है। "
                   "‘पुण्यतमः’ में ‘-तम’ अतिशय का प्रत्यय है: सबसे अधिक पुण्य। "
                   "‘मतः’ का अर्थ ‘माना गया’ है, यानी यह वेदज्ञों का मत है। "
                   "दूसरी पंक्ति में आगे का वचन है: जो मनुष्यों के लिए ‘दोनों "
                   "लोकों में’ हितकर है, वह कहा जाएगा। ‘लोकयोः’ में ‘-योः’ "
                   "द्विवचन का रूप है (दो)।"),
    "hook": "आयु का वेद = वेदज्ञों के मत में पुण्यतम · आगे: जो दोनों लोकों में मनुष्यों का हित करे, वही कहा जाएगा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 43 says Āyurveda is regarded as the most holy. By whom?",
            ("By the knowers of the Vedas",
             "The phrase वेदविदां मतः says it is the view of the Veda-knowers."),
            [("By the kings of the earth", "The verse names no kings."),
             ("By the Aśvins alone", "The Aśvins are not mentioned in this verse."),
             ("By Indra alone", "Indra is not mentioned in this verse.")],
            "वेदविदां मतः: regarded by those who know the Vedas.",
            "The holiness of Āyurveda is stated as the view of the Veda-knowers."),
        match(1, "Match each word of the verse to its meaning.",
              [["पुण्यतमः", "most holy"], ["वेदविदाम्", "of the knowers of the Vedas"],
               ["मनुष्याणाम्", "of human beings"], ["उभयोः", "of both"]],
              "These words give who regards it, and for whom the teaching is.",
              "पुण्यतमः = most holy; वेदविदाम् = of the knowers of the Vedas; मनुष्याणाम् = of human beings; उभयोः = of both."),
        fill(2, "The word for 'most holy' in the verse is ____ (type it in Devanagari).",
             ["पुण्यतमः", "पुण्यतमो", "पुण्यतम"],
             "The first line has पुण्यतमो वेदः: the most holy Veda.",
             "पुण्यतमः = पुण्य + तम. The ending -तम makes a superlative: 'most'.",
             "पुण्य + -तम = most holy."),
        mcq("discriminate", 3, "Which is the right split of यन्मनुष्याणाम्?",
            ("यत् + मनुष्याणाम्", "A final त् before the nasal म becomes न्, so यत् + मनुष्याणाम् is written यन्मनुष्याणाम्."),
            [("यन् + मनुष्याणाम्", "यन् is not a word."),
             ("य + न्मनुष्याणाम्", "न्मनुष्याणाम् is not a word."),
             ("यम् + अनुष्याणाम्", "अनुष्याणाम् is not a word.")],
            "यन्मनुष्याणाम् = यत् ('which') + मनुष्याणाम् ('of human beings').",
            "त् + म → न्म: यत् + मनुष्याणाम् = यन्मनुष्याणाम्."),
        mcq("apply", 4,
            "A student writes: 'Verse 43 states as plain fact that Āyurveda is the holiest science.' What does the verse actually say?",
            ("That the knowers of the Vedas regard it as most holy",
             "मतः, 'regarded', and वेदविदाम्, 'of the Veda-knowers', make it their view."),
            [("That Brahmā himself declared it the holiest",
              "Brahmā is not named in this verse."),
             ("That it is more holy than the Vedas themselves",
              "The verse compares nothing with the Vedas."),
             ("That nobody holds any view about it",
              "मतः says a view is held.")],
            "The verse reports a view (मतः) of the Veda-knowers.",
            "मतः = regarded; the holiness is attributed to the Veda-knowers' view."),
        mcq("transfer", 5,
            "An invented phrase reads पादयोरुभयोर्हितम् (पाद = foot). The ending -योः is dual, as in लोकयोरुभयोः. What does the phrase mean?",
            ("Beneficial to both feet",
             "-योः with उभयोः makes it 'of both' two things, here both feet."),
            [("Beneficial to one foot only", "उभयोः means 'both', not 'one'."),
             ("Beneficial to many feet", "A dual ending names two, not many."),
             ("Harmful to both feet", "हितम् means beneficial, not harmful.")],
            "A noun in dual -योः together with उभयोः names exactly two things.",
            "लोकयोरुभयोः = of/in both worlds; पादयोरुभयोः = of both feet.",
            teaches="The pairing of dual -योः with उभयोः carries over to any pair of things: it reads 'both'."),
    ],
}

# --------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "सर्वदा सर्वभावानां सामान्यम्",
    "question": "What do commonality (sāmānya) and distinctiveness (viśeṣa) cause?",
    "rule": ("Commonality is always the cause of increase of all entities; "
             "distinctiveness is the cause of decrease; the operation "
             "(pravṛtti) belongs to both."),
    "limits": ("Medium confidence. pravṛttir ubhayasya tu is terse: it is "
               "read as 'both are operative' or 'the application is of "
               "both'. Do not build more on it than that. The terms "
               "are defined in the next verse."),
    "explain_hi": ("यहाँ से सामान्य-विशेष आदि की चर्चा शुरू होती है। ‘सामान्य’ (समानता) "
                   "सदा सब भावों की वृद्धि का कारण है और ‘विशेष’ (भिन्नता) "
                   "ह्रास का कारण। अन्तिम चरण ‘प्रवृत्तिरुभयस्य तु’ संक्षिप्त है: "
                   "प्रवृत्ति (व्यवहार में प्रयोग) दोनों की होती है। इस श्लोक में "
                   "सामान्य और विशेष की परिभाषा नहीं है, वह अगले श्लोक में आती है।"),
    "hook": "सामान्य → वृद्धि का कारण · विशेष → ह्रास का हेतु · प्रवृत्ति दोनों की।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 44 pairs sāmānya (commonality) with viśeṣa (distinctiveness). Which would you expect to be named the cause of increase?",
            ("Sāmānya", "The verse says सामान्यं वृद्धिकारणम्."),
            [("Viśeṣa", "Viśeṣa is named as the cause of decrease."),
             ("Both, equally", "The two are given opposite effects."),
             ("Neither", "Each is given an effect.")],
            "Sāmānya is the cause of increase; viśeṣa the cause of decrease.",
            "सामान्यं वृद्धिकारणम्; विशेषो ह्रासहेतुः."),
        match(1, "Match each word of the verse to its meaning.",
              [["सर्वदा", "always"], ["सर्वभावानाम्", "of all entities"],
               ["वृद्धिकारणम्", "cause of increase"], ["ह्रासहेतुः", "cause of decrease"]],
              "These words give the two effects and their scope.",
              "सर्वदा = always; सर्वभावानाम् = of all entities; वृद्धिकारणम् = cause of increase; ह्रासहेतुः = cause of decrease."),
        fill(2, "In ह्रासहेतुः the first part is the word for 'decrease', ____ (type it in Devanagari).",
             ["ह्रासः", "ह्रास", "ह्रासो"],
             "ह्रासहेतुः = ह्रास + हेतुः: the cause of decrease.",
             "ह्रास is 'decrease'; the compound ह्रासहेतुः joins it to हेतुः ('cause'). It mirrors वृद्धिकारणम्, 'cause of increase'.",
             "ह्रास = decrease; वृद्धि = increase."),
        mcq("discriminate", 3, "Which is the right split of ह्रासहेतुर्विशेषश्च?",
            ("ह्रासहेतुः + विशेषः + च", "A visarga before the voiced व becomes र्, and one before च becomes श्."),
            [("ह्रासहेतु + र्विशेषश्च", "र्विशेषश्च is not a word."),
             ("ह्रासहेतुः + विशेषः + श्च", "The word is च; the श् comes from the visarga before it."),
             ("ह्रासहेतुर् + विशेषः + च", "ह्रासहेतुर् is not a word; the word ends in a visarga.")],
            "ह्रासहेतुर्विशेषश्च = ह्रासहेतुः + विशेषः + च.",
            "विसर्ग → र् (before voiced); विसर्ग + च → श्च."),
        multi("apply", 4, "Which statements does verse 44 make?",
              [("Sāmānya is always a cause of increase of all entities", "Right: सर्वदा सर्वभावानां सामान्यं वृद्धिकारणम्."),
               ("Viśeṣa is a cause of decrease", "Right: विशेषो ह्रासहेतुः."),
               ("The operation (pravṛtti) belongs to both", "Right: प्रवृत्तिरुभयस्य."),
               ("Sāmānya is the cause of decrease", "It is the cause of increase."),
               ("Viśeṣa is the cause of increase", "It is the cause of decrease.")],
              [0, 1, 2],
              "Three statements follow from the verse; two swap the effects.",
              "सामान्य → वृद्धि; विशेष → ह्रास; प्रवृत्ति दोनों की।"),
        mcq("transfer", 5,
            "An invented compound reads तेजोवृद्धिकारणम् (तेजस् = brightness). By the pattern of वृद्धिकारणम्, what does it name?",
            ("The cause of increase of brightness",
             "X-वृद्धि-कारणम् = the cause of increase of X."),
            [("The increase caused by brightness",
              "Here the cause is what is named last (कारणम्), not तेजः."),
             ("The cause of decrease of brightness", "वृद्धि is increase, not decrease."),
             ("Brightness itself", "The compound ends in कारणम्, 'cause'.")],
            "In X-वृद्धि-कारणम् the last member is the thing named: a cause; what comes before says 'of the increase of X'.",
            "…वृद्धिकारणम् = cause of the increase of ….",
            teaches="You can read any compound of the type X-वृद्धि-कारणम् as 'the cause of the increase of X'."),
    ],
}

# --------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "सामान्यमेकत्वकरम्",
    "question": "How does the verse define commonality and distinctiveness?",
    "rule": ("Commonality produces oneness (ekatva) and is sameness of "
             "purpose (tulyārthatā); distinctiveness produces separateness "
             "(pṛthaktva) and is its opposite (viparyaya)."),
    "limits": ("tulyārthatā is read as 'sameness of effect or purpose'; "
               "artha could also be 'object' or 'meaning'. The verse does "
               "not give examples."),
    "explain_hi": ("यह श्लोक पिछले श्लोक के दो शब्दों की परिभाषा देता है। सामान्य "
                   "एकत्व उत्पन्न करता है और वस्तुतः ‘तुल्यार्थता’ है, यानी "
                   "समान प्रयोजन या प्रभाव। विशेष पृथक्त्व उत्पन्न करता है और "
                   "उसका ‘विपर्यय’ (विपरीत) है। ‘-ता’ प्रत्यय भाव-वाचक संज्ञा "
                   "बनाता है: तुल्यार्थ + ता = तुल्यार्थता, ‘तुल्य अर्थ होने "
                   "की स्थिति’।"),
    "hook": "सामान्य = एकत्वकर · तुल्यार्थता | विशेष = पृथक्त्वकृत् · विपर्यय।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Sāmānya (commonality) and viśeṣa (distinctiveness) are opposites. Which one would you expect to produce separateness?",
            ("Viśeṣa", "The verse says विशेषस्तु पृथक्त्वकृत्."),
            [("Sāmānya", "Sāmānya produces oneness."),
             ("Both of them", "They are given opposite effects."),
             ("Neither of them", "Each is given an effect.")],
            "Viśeṣa produces separateness (pṛthaktva); sāmānya produces oneness (ekatva).",
            "सामान्य → एकत्व; विशेष → पृथक्त्व."),
        match(1, "Match each word of the verse to its meaning.",
              [["एकत्वकरम्", "producing oneness"], ["पृथक्त्वकृत्", "producing separateness"],
               ["तुल्यार्थता", "sameness of purpose"], ["विपर्ययः", "the opposite"]],
              "These four words define the pair.",
              "एकत्वकरम् = producing oneness; पृथक्त्वकृत् = producing separateness; तुल्यार्थता = sameness of purpose; विपर्ययः = the opposite."),
        fill(2, "The verse calls distinctiveness the opposite of commonality. The word for 'opposite' is ____ (type it in Devanagari).",
             ["विपर्ययः", "विपर्यय", "विपर्ययो"],
             "The last words are विशेषस्तु विपर्ययः: distinctiveness is the opposite.",
             "विपर्ययः is the opposite, the reverse. It tells you viśeṣa is defined by reversing sāmānya.",
             "विपर्ययः = the opposite."),
        mcq("discriminate", 3, "Which is the right split of विशेषस्तु?",
            ("विशेषः + तु", "A visarga before त becomes स्, so विशेषः + तु is written विशेषस्तु."),
            [("विशेष + स्तु", "स्तु is not a word."),
             ("विशेषस् + तु", "विशेषस् is not a word; the word ends in a visarga."),
             ("विशेषः + स्तु", "स्तु is not a word.")],
            "विशेषस्तु = विशेषः + तु ('but').",
            "विसर्ग + त → स्त: विशेषः + तु = विशेषस्तु."),
        mcq("apply", 4,
            "Two herbs have the same effect on the body. Which of the two principles in verse 45 does this match?",
            ("Sāmānya, the sameness of effect (tulyārthatā)",
             "तुल्यार्थता is sameness of effect or purpose, which is how the verse defines sāmānya."),
            [("Viśeṣa, because the herbs differ", "The herbs are alike in effect, so this is not viśeṣa."),
             ("Viśeṣa, because there are two herbs", "Viśeṣa is separateness of kind, not a count."),
             ("Neither; the verse is only about words", "The verse defines both principles.")],
            "Sameness of effect = sāmānya.",
            "सामान्यं तुल्यार्थता: likeness of effect or purpose."),
        mcq("transfer", 5,
            "An invented word समवेगता (सम = equal, वेग = speed) is built like तुल्यार्थता. What does it mean?",
            ("The state of having equal speed",
             "The ending -ता makes an abstract noun: 'the state of being …'."),
            [("A person who has equal speed", "-ता names a state, not a person."),
             ("The opposite of speed", "The word contains सम, 'equal', not 'opposite'."),
             ("Speed itself", "-ता adds the sense 'state of equal …'.")],
            "तुल्यार्थ + ता = the state of having the same purpose; सम-वेग + ता = the state of equal speed.",
            "-ता = the state or quality of being ….",
            teaches="The ending -ता turns a descriptive compound into a noun for the state; you can read many such words from their parts."),
    ],
}

# --------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "सत्त्वमात्मा शरीरं च",
    "question": "What does the verse compare to a tripod, and what rests on it?",
    "rule": ("Mind (sattva), self and body are like a tripod; the world of "
             "beings stands by their union, and everything is established "
             "in it."),
    "limits": ("तत्र ('in it') can refer to the union or to the living "
               "being; the verse does not decide. The tripod is a simile "
               "only: it does not say what happens if one member is missing."),
    "explain_hi": ("श्लोक ४२ में आयु चार का संयोग थी; यहाँ तीन का उल्लेख है: "
                   "सत्त्व (मन), आत्मा और शरीर, जो त्रिदण्ड (तीन डण्डों की "
                   "तिपाई) जैसे हैं। ‘त्रिदण्डवत्’ में ‘-वत्’ का अर्थ ‘जैसा’ है। "
                   "‘संयोगात्’ (संयोग से) में ‘-आत्’ कारण बताता है: लोक इनके "
                   "संयोग से टिकता है। ‘तत्र सर्वं प्रतिष्ठितम्’ का भाव है कि "
                   "सब कुछ उसी में स्थित है।"),
    "hook": "मन · आत्मा · शरीर = त्रिदण्ड (तिपाई); संयोग से लोक टिके, उसी में सब प्रतिष्ठित।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 46 compares three things to a tripod. Which three?",
            ("Mind, self and body",
             "The first line names सत्त्वम्, आत्मा and शरीरम्."),
            [("Birth, youth and old age", "These are not named in the verse."),
             ("Earth, water and fire", "These are not named in the verse."),
             ("Sun, moon and stars", "These are not named in the verse.")],
            "सत्त्व, आत्मा and शरीर form the triad.",
            "The triad is mind, self, body."),
        match(1, "Match each word of the verse to its meaning.",
              [["सत्त्वम्", "mind"], ["आत्मा", "self"],
               ["शरीरम्", "body"], ["संयोगात्", "by union"]],
              "These words give the three members and what holds them.",
              "सत्त्वम् = mind; आत्मा = self; शरीरम् = body; संयोगात् = by union."),
        fill(2, "The word for 'like a tripod' is ____ (type it in Devanagari).",
             ["त्रिदण्डवत्", "त्रिदण्डवत"],
             "The first line has त्रयमेतत्त्रिदण्डवत्: this triad is like a tripod.",
             "त्रिदण्डवत् = त्रिदण्ड ('tripod') + वत् ('like'). The ending -वत् here makes the word mean 'like …'.",
             "त्रिदण्ड + -वत् = like a tripod."),
        mcq("discriminate", 3, "Which is the right split of त्रयमेतत्त्रिदण्डवत्?",
            ("त्रयम् + एतत् + त्रिदण्डवत्", "A final म् joins directly to the following vowel, and एतत् ends in त् before the त्र of त्रिदण्डवत्."),
            [("त्रय + मेतत् + त्रिदण्डवत्", "मेतत् is not a word."),
             ("त्रयमे + तत् + त्रिदण्डवत्", "त्रयमे is not a word."),
             ("त्रयम् + एत + त्रिदण्डवत्", "The word is एतत् ('this'); the extra त् belongs to it.")],
            "त्रयमेतत्त्रिदण्डवत् = त्रयम् ('triad') + एतत् ('this') + त्रिदण्डवत् ('like a tripod').",
            "म् + vowel join without change: त्रयम् + एतत् = त्रयमेतत्."),
        mcq("apply", 4,
            "A student says the verse makes the body alone the support of the world. Which word in the verse corrects this?",
            ("संयोगात्: the world stands by the union of all three",
             "संयोगात् = 'by union', and the union is of mind, self and body."),
            [("शरीरम्: because it is named last in the list",
              "Being named in a list does not make it the sole support."),
             ("लोकः: because it is the subject of the sentence",
              "लोकः is what stands; it does not say which member alone stands."),
            ("नित्यः: the body is eternal", "नित्यः is not in this verse.")],
            "The support is the union (संयोगात्) of the triad, not one member alone.",
            "The world stands by the union (संयोगात्) of the three."),
        mcq("transfer", 5,
            "An invented line reads गृहं स्तम्भसंयोगात्तिष्ठति (गृह = house, स्तम्भ = pillar). By the pattern of लोकस्तिष्ठति संयोगात्, what does it say?",
            ("The house stands by the union of pillars",
             "-आत् on संयोग gives 'by / through the union', as in the verse."),
            [("The house destroys the pillars", "तिष्ठति means 'stands', not 'destroys'."),
             ("The pillars stand by the house alone", "The house stands by the pillars' union, not the other way round."),
             ("The house stood in the past", "तिष्ठति is present: 'stands'.")],
            "The ablative -आत् names the means or support: standing by union.",
            "X तिष्ठति Y-संयोगात् = X stands by the union of Y.",
            teaches="The ending -आत् on a noun like संयोग names what something stands on or by; you can read new sentences of this kind."),
    ],
}

# --------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "स पुमांश्चेतनं तच्च",
    "question": "What is the union of mind, self and body called, and for whose sake was this Veda revealed?",
    "rule": ("That union is the person (puruṣa) and the sentient being, and "
             "is regarded as the subject (adhikaraṇa) of this Veda; for its "
             "sake this Veda has been revealed."),
    "limits": ("स ('that') is taken to refer back to the union of verse 46; "
               "the verse itself does not repeat the three names. adhikaraṇa "
               "is rendered 'subject' but may also be 'locus' of treatment."),
    "explain_hi": ("यह श्लोक पिछले श्लोक का ‘संयोग’ आगे बढ़ाता है: वही (मन, "
                   "आत्मा और शरीर का संयोग) पुरुष है, वही चेतन है और वही इस "
                   "वेद का अधिकरण (विषय) माना गया है। ‘पुमान्’ पुरुष का रूप है "
                   "और ‘तदर्थम्’ का अर्थ है ‘उसी के लिए’; इसलिए आयुर्वेद इसी "
                   "संयोग के लिए प्रकाशित हुआ। ‘स’ पुल्लिंग और ‘तत्’ नपुंसक "
                   "है, फिर भी तीनों का संकेत एक ही संयोग की ओर है।"),
    "hook": "वही संयोग = पुमान् · चेतन · अधिकरण; इसी के लिए यह वेद प्रकाशित (तदर्थं हि संप्रकाशितः)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 46 spoke of the union of mind, self and body. In the first words of verse 47, स पुमान्, what is that union called?",
            ("The person (puruṣa)",
             "पुमान् is the person, the one the union makes."),
            [("A god", "No god is named."),
             ("A disease", "No disease is named."),
             ("A medicine", "No medicine is named.")],
            "The union is called the person, the sentient being and the subject of this Veda.",
            "स पुमान् = that (union) is the person."),
        match(1, "Match each word of the verse to its meaning.",
              [["पुमान्", "person"], ["चेतनम्", "sentient being"],
               ["अधिकरणम्", "subject (locus of treatment)"], ["तदर्थम्", "for its sake"]],
              "These words say what the union is and what the Veda is for.",
              "पुमान् = person; चेतनम् = sentient being; अधिकरणम् = subject; तदर्थम् = for its sake."),
        fill(2, "The last word of the verse, meaning 'revealed', is ____ (type it in Devanagari).",
             ["संप्रकाशितः", "सम्प्रकाशितः", "संप्रकाशितो", "सम्प्रकाशितो"],
             "वेदो ऽयं संप्रकाशितः: this Veda has been revealed.",
             "संप्रकाशितः is the causative past participle of √काश् with सम् and प्र: 'made known, revealed'. वेदः (masculine) is its subject.",
             "संप्रकाशितः = revealed, made known."),
        mcq("discriminate", 3, "Which is the right split of तच्चाधिकरणम्?",
            ("तत् + च + अधिकरणम्", "त् + च joins as च्च, and च + अ gives चा, so तत् + च + अधिकरणम् is written तच्चाधिकरणम्."),
            [("तच् + चा + धिकरणम्", "धिकरणम् is not a word."),
             ("तत् + चा + अधिकरणम्", "चा is not a word; the word is च."),
             ("तत् + च + आधिकरणम्", "The word begins with अ, not आ.")],
            "तच्चाधिकरणम् = तत् ('that') + च ('and') + अधिकरणम् ('subject').",
            "त् + च → च्च; अ + अ → आ."),
        mcq("apply", 4,
            "For whom, according to verse 47, was this Veda revealed?",
            ("For the union of mind, self and body, the person",
             "तदर्थं refers back to that union, called puruṣa."),
            [("For the herbs of the mountains", "No herbs are named in this verse."),
             ("For the gods alone", "The verse names no gods."),
             ("For the sages' own fame", "Fame is not mentioned here (verse 39 named it among deities).")],
            "This Veda was revealed for the sake of that union.",
            "तदर्थम् = for its sake: the union called puruṣa."),
        mcq("transfer", 5,
            "An invented word शिष्यार्थम् is built like तदर्थम् (तत् + अर्थम्). What does it mean?",
            ("For the sake of the student",
             "X-अर्थम् is the form 'for the sake of X'."),
            [("Away from the student", "-अर्थम् does not mean 'away from'."),
             ("The student himself", "It is a 'for the sake of' word, not the student."),
             ("After the student", "-अर्थम् does not mean 'after'.")],
            "X-अर्थम् = for the sake of X.",
            "तद्-अर्थम् = for its sake; शिष्य-अर्थम् = for the student's sake.",
            teaches="The ending -अर्थम् after a word X reads 'for the sake of X'; you can read new words of this type."),
    ],
}

# --------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "खादीन्यात्मा मनः कालः",
    "question": "What does the verse list as the summary of substances (dravya), and what makes a substance sentient?",
    "rule": ("The summary of substances: space and the rest (kha-ādīni), "
             "self, mind, time and the directions. A substance with sense "
             "faculties is sentient; one without them is non-sentient."),
    "limits": ("The verse says only 'kha and the rest'; the names of the "
               "five elements are not given in it. Sentient/non-sentient is "
               "stated only in terms of having or lacking sense faculties."),
    "explain_hi": ("यहाँ द्रव्य का संग्रह है: ख (आकाश) आदि, आत्मा, मन, काल और "
                   "दिशाएँ। ‘खादीनि’ का अर्थ ‘ख आदि’ है; ख के बाद के नाम श्लोक में "
                   "नहीं दिए गए हैं, केवल ‘आदि’ कहा गया है। दूसरी पंक्ति कसौटी "
                   "देती है: इन्द्रिय-सहित (सेन्द्रिय) द्रव्य चेतन है और इन्द्रिय-"
                   "रहित (निरिन्द्रिय) द्रव्य अचेतन। ‘स-’ का अर्थ ‘सहित’ और ‘निः-’ "
                   "का ‘रहित’ है।"),
    "hook": "द्रव्य-संग्रह: खादि · आत्मा · मनः · कालः · दिशः | सेन्द्रिय = चेतन, निरिन्द्रिय = अचेतन।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 48 gives a summary of substances (dravya). Which of these is named in it?",
            ("Time (काल)", "कालः is named in the first line."),
            [("Disease (रोग)", "No disease is named in this verse."),
             ("Medicine (औषध)", "No medicine is named in this verse."),
             ("Memory (स्मृति)", "Memory was named among the deities in verse 39, not here.")],
            "The summary names kha and the rest, self, mind, time and the directions.",
            "द्रव्यसंग्रह = kha-ādi, ātmā, manas, kāla, diś."),
        match(1, "Match each word of the verse to its meaning.",
              [["आत्मा", "self"], ["मनः", "mind"],
               ["कालः", "time"], ["दिशः", "directions"]],
              "These words are four of the items in the summary.",
              "आत्मा = self; मनः = mind; कालः = time; दिशः = directions."),
        fill(2, "A substance with sense faculties is चेतन; one without them is ____ (type it in Devanagari).",
             ["अचेतनम्", "अचेतन", "अचेतनं"],
             "The verse ends निरिन्द्रियमचेतनम्: without senses is non-sentient.",
             "अचेतनम् = अ + चेतनम्: the prefix अ- negates, so 'not sentient'.",
             "अचेतन = non-sentient."),
        mcq("discriminate", 3, "Which is the right split of खादीन्यात्मा?",
            ("खादीनि + आत्मा", "A final इ before a different vowel becomes य्, so खादीनि + आत्मा is written खादीन्यात्मा."),
            [("खादीन्य + आत्मा", "खादीन्य is not a word."),
             ("खा + दीन्यात्मा", "दीन्यात्मा is not a word."),
             ("खादि + न्यात्मा", "न्यात्मा is not a word.")],
            "खादीन्यात्मा = खादीनि ('kha and the rest') + आत्मा ('self').",
            "इ + आ → य्+आ: खादीनि + आत्मा = खादीन्यात्मा."),
        multi("apply", 4, "Which of these are named in the verse as substances?",
              [("आत्मा", "Right: ātmā is named."),
               ("कालः", "Right: kāla is named."),
               ("दिशः", "Right: diśaḥ are named."),
               ("औषधम्", "No medicine is named in this verse."),
               ("रोगः", "No disease is named in this verse.")],
              [0, 1, 2],
              "Self, time and directions are named; medicine and disease are not.",
              "द्रव्यसंग्रह: खादि, आत्मा, मनः, कालः, दिशः."),
        mcq("transfer", 5,
            "By the pattern of सेन्द्रियम् and निरिन्द्रियम्, what does the invented word निष्पत्रम् (पत्र = leaf) mean?",
            ("Without leaves",
             "निः- gives 'without', as निः + इन्द्रियम् gave 'without senses'."),
            [("With leaves", "That would be the स- form, सपत्रम्."),
             ("Many leaves", "निः- does not mean 'many'."),
             ("Only a leaf", "निः- does not mean 'only'.")],
            "स- = with; निः- = without.",
            "स-X = with X; निः-X = without X.",
            teaches="The prefixes स- ('with') and निः- ('without') let you read pairs like सपत्रम् / निष्पत्रम् for any noun."),
    ],
}

# --------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "सार्था गुर्वादयो बुद्धिः",
    "question": "What does the verse call guṇa (qualities), and how does it describe karma (action)?",
    "rule": ("Qualities (guṇa): those together with the sense-objects, those "
             "beginning with guru (heavy), buddhi, those ending with effort "
             "(prayatna), and those beginning with para (priority). Action "
             "(karma) is movement (ceṣṭita) beginning with effort."),
    "limits": ("Medium confidence. The first line is a compressed list; "
               "whether prayatnāntāḥ is a separate group or goes with "
               "buddhiḥ is construed differently, and the verse does not "
               "spell out the members. Only the groupings named in the "
               "verse are used here."),
    "explain_hi": ("पहली पंक्ति गुणों की सूची है और बहुत संक्षिप्त है: अर्थों "
                   "(इन्द्रिय-विषयों) सहित, ‘गुरु आदि’, बुद्धि, ‘प्रयत्न तक’ "
                   "और ‘पर आदि’। इनके सारे नाम श्लोक में नहीं दिए गए; ‘आदि’ का "
                   "अर्थ ‘से आरम्भ होने वाले’ है और ‘अन्त’ का ‘पर समाप्त होने "
                   "वाले’। ‘प्रयत्न तक’ वाला भाग किस समूह से जुड़ता है, इस पर "
                   "पाठकों में भेद है। दूसरी पंक्ति कर्म बताती है: प्रयत्न से "
                   "आरम्भ होने वाली चेष्टा।"),
    "hook": "गुण: सार्थ · गुर्वादि · बुद्धि · प्रयत्नान्त · परादि | कर्म = प्रयत्नादि चेष्टित।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 49 defines two terms: guṇa (qualities) and karma (action). Which of them is described as movement (ceṣṭita) beginning with effort?",
            ("Karma", "The second line says प्रयत्नादि कर्म चेष्टितम्."),
            [("Guṇa", "The qualities are listed in the first line, not described as movement."),
             ("Both", "Only karma is called a movement here."),
             ("Neither", "Karma is described this way.")],
            "Karma is movement beginning with effort; guṇas are the listed qualities.",
            "कर्म = प्रयत्न से आरम्भ होने वाली चेष्टा."),
        match(1, "Match each word of the verse to its meaning.",
              [["गुणाः", "qualities"], ["कर्म", "action"],
               ["चेष्टितम्", "movement"], ["प्रयत्नादि", "beginning with effort"]],
              "These words carry the two definitions.",
              "गुणाः = qualities; कर्म = action; चेष्टितम् = movement; प्रयत्नादि = beginning with effort."),
        fill(2, "The word for 'are declared' in the verse is ____ (type it in Devanagari).",
             ["प्रोक्ताः", "प्रोक्ता"],
             "The first sentence ends गुणाः प्रोक्ताः: these are declared to be qualities.",
             "प्रोक्ताः = प्र + उक्ताः, from √वच्: 'declared'. The same root appeared in उक्तम् and उच्यते.",
             "प्रोक्ताः = declared (√वच्)."),
        mcq("discriminate", 3, "Which is the right split of गुर्वादयः?",
            ("गुरु + आदयः", "A final उ before a different vowel becomes व्, so गुरु + आदयः is written गुर्वादयः."),
            [("गुर् + वादयः", "वादयः is not a word here."),
             ("गु + र्वादयः", "र्वादयः is not a word."),
             ("गुरो + आदयः", "ओ + आ would give a different form.")],
            "गुर्वादयः = गुरु ('heavy') + आदयः ('and the rest').",
            "उ + आ → व्+आ: गुरु + आदयः = गुर्वादयः."),
        mcq("apply", 4,
            "In the phrase प्रयत्नादि कर्म चेष्टितम्, which word says that action begins with effort?",
            ("प्रयत्नादि: 'beginning with effort'",
             "आदि means 'beginning with' or 'and the rest'."),
            [("प्रयत्नान्ताः: 'ending with effort'",
              "That word is in the first line and means 'ending with effort', a group of qualities."),
             ("परादयः: 'beginning with para'", "That word names another group of qualities."),
             ("गुणाः: 'qualities'", "That word names the qualities, not action.")],
            "प्रयत्नादि means beginning with effort; प्रयत्नान्ताः means ending with effort.",
            "आदि = beginning with; अन्त = ending with.",),
        mcq("transfer", 5,
            "An invented phrase reads बीजादयः फलान्ताः (बीज = seed, फल = fruit). By the pattern of गुर्वादयः and प्रयत्नान्ताः, what does it describe?",
            ("A series beginning with seed and ending with fruit",
             "आदि = beginning with; अन्त = ending with."),
            [("A series beginning with fruit and ending with seed", "The order is reversed."),
             ("A series that contains only seed and fruit", "आदि means more follow after the first."),
             ("A series with no seed in it", "बीज is the first member.")],
            "X-आदि = beginning with X; Y-अन्त = ending with Y.",
            "X-आदयः Y-अन्ताः = a series from X to Y.",
            teaches="The endings -आदि and -अन्त let you read where a series starts and where it ends, even with new words."),
    ],
}

# --------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "समवायो ऽपृथग्भावः",
    "question": "What is inherence (samavāya), and why is it called eternal?",
    "rule": ("Samavāya is the inseparable existence (aprthag-bhāva) of "
             "earth and the rest with their qualities. It is eternal, for "
             "wherever there is a substance, a quality is not absent."),
    "limits": ("aniyataḥ is literally 'not fixed'; here it is read as "
               "'absent'. The verse gives no example beyond earth and "
               "does not define 'inherence' further."),
    "explain_hi": ("समवाय वह अपृथक्-भाव है जो पृथ्वी आदि का अपने गुणों के साथ "
                   "है, यानी ऐसा सम्बन्ध जो अलग नहीं किया जा सकता। ‘अपृथक्’ "
                   "में ‘अ-’ निषेध है: पृथक् नहीं। दूसरी पंक्ति कारण देती है "
                   "कि वह नित्य क्यों है: जहाँ द्रव्य है, वहाँ गुण ‘अनियत’ "
                   "(अनुपस्थित) नहीं होता। ‘न … अनियतः’ में दो निषेध मिलकर "
                   "‘सदा उपस्थित’ का भाव देते हैं।"),
    "hook": "समवाय = अपृथग्भाव (द्रव्य–गुण का अलग न होना) · नित्य, क्योंकि जहाँ द्रव्य वहाँ गुण।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Samavāya is described as an inseparable relation. Between what does verse 50 say it holds?",
            ("Earth and the rest, and their qualities",
             "भूम्यादीनां गुणैः: earth and the rest with their qualities."),
            [("A teacher and his student", "No teacher is named in this verse."),
             ("Two diseases", "No disease is named in this verse."),
             ("A medicine and its price", "Nothing of the kind is in the verse.")],
            "Samavāya joins substances (earth and the rest) with their qualities.",
            "Samavāya = inseparable existence of substances with their qualities."),
        match(1, "Match each word of the verse to its meaning.",
              [["समवायः", "inherence"], ["अपृथग्भावः", "inseparable existence"],
               ["नित्यः", "eternal"], ["गुणः", "quality"]],
              "These words carry the definition and the reason.",
              "समवायः = inherence; अपृथग्भावः = inseparable existence; नित्यः = eternal; गुणः = quality."),
        fill(2, "The verse's word for 'inseparable existence' is ____ (type it in Devanagari, with or without the ऽ sign).",
             ["अपृथग्भावः", "अपृथग्भावो", "ऽपृथग्भावः", "ऽपृथग्भावो", "अपृथग्भाव"],
             "The first line has समवायो ऽपृथग्भावो: samavāya is aprthag-bhāva.",
             "अपृथग्भावः = अपृथक् + भावः: 'not-separate existence'. The अ- negates पृथक् ('separate').",
             "अपृथक् = not separate; अपृथग्भाव = inseparable existence."),
        mcq("discriminate", 3, "Which is the right split of समवायो ऽपृथग्भावः?",
            ("समवायः + अपृथग्भावः", "अः + अ joins as ओ with ऽ marking the dropped अ, so समवायः + अपृथग्भावः is written समवायो ऽपृथग्भावः."),
            [("समवायः + पृथग्भावः", "That would mean 'separate existence', the opposite; the ऽ sign shows an अ was dropped."),
             ("समवा + योऽपृथग्भावः", "योऽपृथग्भावः is not a word."),
             ("समवायोऽ + पृथग्भावः", "The sign ऽ is not a word.")],
            "समवायो ऽपृथग्भावः = समवायः ('inherence') + अपृथग्भावः ('inseparable existence').",
            "अः + अ → ओ ऽ (ऽ marks the hidden अ)."),
        mcq("apply", 4,
            "A student says: 'Earth can exist without its qualities, so samavāya is not eternal.' What does the verse say against this?",
            ("Where there is a substance, quality is never absent (न तत्रानियतो गुणः)",
             "The second line gives this as the reason for its being eternal."),
            [("Qualities are rare and appear only sometimes",
              "The verse says the opposite: never absent."),
             ("Earth is not a substance",
              "भूमि is the example of the substances the verse names."),
             ("Nothing is said about eternity",
              "स नित्यः says it is eternal.")],
            "The verse gives the reason: no substance without its qualities.",
            "यत्र द्रव्यं न तत्रानियतो गुणः = where there is substance, quality is not absent."),
        mcq("transfer", 5,
            "An invented line: where there is fire, heat (उष्णता) is न अनियत ('not absent'). By the pattern of verse 50, what does it mean?",
            ("Wherever there is fire, heat is present",
             "'Not absent' means present: the same logic as न तत्रानियतो गुणः."),
            [("Heat is sometimes absent where fire is", "That would contradict 'not absent'."),
             ("Fire is absent where heat is", "The line speaks of heat where fire is."),
             ("Heat exists only far from fire", "Nothing in the line says this.")],
            "Two negatives (not … not fixed/absent) give 'always present'.",
            "यत्र X तत्र न अनियतः Y = wherever X is, Y is present.",
            teaches="The pattern 'where X, there Y is not absent' states that one thing is always present where the other is; you can read it for new pairs."),
    ],
}

NOTES_HI = {
    "41": "पाठ में ‘दुखम्’ छपा है; ‘दुःखम्’ अपेक्षित है, क्योंकि स्रोत-टिप्पणी के अनुसार विसर्ग के साथ छन्द नियमित (पथ्या) बनता है। संधि: आयुः + तस्य → आयुस्तस्य (विसर्ग त से पहले स्); यत्र + उक्तम् → यत्रोक्तम् (अ + उ → ओ); आयुः + वेदः → आयुर्वेदः (घोष से पहले र्)। ‘हिताहितम्’ पहली बार आयु का विशेषण है, दूसरी बार ‘उसके लिए क्या हितकर/अहितकर’; दोनों के बीच ‘तस्य’ ही अर्थ बाँटता है।",
    "42": "संधि: शरीर + इन्द्रिय → शरीरेन्द्रिय (अ + इ → ए); सत्त्व + आत्म → सत्त्वात्म (अ + आ → आ); संयोगः + धारि → संयोगो धारि (विसर्ग → ओ घोष से पहले); नित्यगः + च → नित्यगश्च (विसर्ग + च → श्); पर्यायैः + आयुः → पर्यायैरायुः और आयुः + उच्यते → आयुरुच्यते (स्वर से पहले र्)। ‘नित्यग’ का अर्थ ‘सदा चलने वाला’ या ‘सदा साथ रहने वाला’ दोनों माना जाता है; ‘अनुबन्ध’ = निरन्तरता। पाठभेद डेटा में नहीं हैं।",
    "43": "विश्वास: मध्यम। ‘यत्’ नपुंसक है और ‘वेदः’ पुल्लिंग, इसलिए ‘यत्’ को ‘जो (विषय)’ पढ़ना ठीक बैठता है, ‘वेद’ के सम्बन्धी के रूप में नहीं। ‘लोकयोरुभयोः’ सप्तमी और षष्ठी दोनों पढ़ा जा सकता है (‘दोनों लोकों में/के’)। संधि: तस्य + आयुषः → तस्यायुषः; पुण्यतमः + वेदः → पुण्यतमो वेदः; यत् + मनुष्याणाम् → यन्मनुष्याणाम्; लोकयोः + उभयोः → लोकयोरुभयोः, फिर उभयोः + हितम् → उभयोर्हितम्। पाठभेद डेटा में नहीं हैं।",
    "44": "विश्वास: मध्यम। ‘प्रवृत्तिरुभयस्य तु’ को दो तरह पढ़ा जाता है: ‘दोनों क्रियाशील हैं’ या ‘प्रयोग दोनों का है’; अक्षरशः अनुवाद रखा गया है; केवल ‘प्रवृत्ति दोनों की’ एक विकल्प में लिया गया है, उसका और अर्थ नहीं टिकाया गया। संधि: ह्रासहेतुः + विशेषः → ह्रासहेतुर्विशेषः; विशेषः + च → विशेषश्च; प्रवृत्तिः + उभयस्य → प्रवृत्तिरुभयस्य। ‘सर्वभावानाम्’ को डेटा कर्मधारय कहता है; ‘सब भावों का’ अर्थ स्पष्ट है। पाठभेद डेटा में नहीं हैं।",
    "45": "‘तुल्यार्थता’ का ‘अर्थ’ प्रयोजन या प्रभाव है (वस्तु या अर्थ भी हो सकता है); यही एक जगह है जहाँ दो अर्थ सम्भव हैं। संधि: विशेषः + तु → विशेषस्तु (विसर्ग + त → स्); तुल्य + अर्थता → तुल्यार्थता (अ + अ → आ); सामान्यम् + एकत्वकरम् में म् स्वर से जुड़ता है। ‘विशेषस्तु’ दो बार आया है, दोनों बार ‘विशेषः तु’। पाठभेद डेटा में नहीं हैं।",
    "46": "‘तत्र’ संयोग की ओर संकेत कर सकता है या ‘लोक’ की ओर; श्लोक निर्णय नहीं देता, इसलिए कोई प्रश्न इस पर नहीं टिका। संधि: सत्त्वम् + आत्मा → सत्त्वमात्मा; त्रयम् + एतत् → त्रयमेतत्; लोकः + तिष्ठति → लोकस्तिष्ठति (विसर्ग + त → स्); संयोगात् + तत्र → संयोगात्तत्र। ‘त्रिदण्डवत्’ में ‘-वत्’ ‘जैसा’ के अर्थ में अव्यय है (डेटा: ind.)। पाठभेद डेटा में नहीं हैं।",
    "47": "‘स पुमान्’ में ‘स’ पुल्लिंग है और ‘तत् चेतनम्’, ‘तत् अधिकरणम्’ नपुंसक; सब पिछले श्लोक के संयोग को ही दिखाते हैं। संधि: पुमान् + चेतनम् → पुमांश्चेतनम् (न् + च → ंश्); तत् + च → तच्च (त् + च → च्च); च + अधिकरणम् → चाधिकरणम् (अ + अ → आ); वेदस्य + अस्य → वेदस्यास्य; वेदः + अयम् → वेदो ऽयम्; तत् + अर्थम् → तदर्थम् (स्वर से पहले त् → द्)। ‘अधिकरण’ को ‘विषय’ या ‘आश्रय’ दोनों पढ़ा जा सकता है। पाठभेद डेटा में नहीं हैं।",
    "48": "‘खादि + आत्मा’ होता तो खाद्यात्मा बनता; श्लोक में खादीनि (नपुंसक बहुवचन) है, इसलिए खादीनि + आत्मा → खादीन्यात्मा। ख के बाद के नाम श्लोक में नहीं हैं; नोट्स में पाँच भूत कहे गए हैं, पर श्लोक उन्हें नहीं गिनाता। अन्य संधि: कालः + दिशः → कालो दिशः; दिशः + च → दिशश्च; स + इन्द्रियम् → सेन्द्रियम् (अ + इ → ए); निः + इन्द्रियम् → निरिन्द्रियम्। पाठभेद डेटा में नहीं हैं।",
    "49": "विश्वास: मध्यम। पहली पंक्ति बहुत संक्षिप्त सूची है, और ‘प्रयत्नान्ताः’ बुद्धि के साथ एक समूह है या अलग, इस पर पाठक-भेद है; इसलिए प्रश्न केवल ‘आदि’/‘अन्त’ और ‘कर्म = प्रयत्नादि चेष्टित’ पर टिके हैं, सूची के सदस्यों पर नहीं। संधि: गुरु + आदयः → गुर्वादयः (उ + आ → व्+आ); प्रयत्न + अन्ताः → प्रयत्नान्ताः; पर + आदयः → परादयः; चेष्टितम् + उच्यते → चेष्टितमुच्यते। पाठभेद डेटा में नहीं हैं।",
    "50": "‘अपृथग्भावः’ की जगह ‘पृथग्भावः’ पढ़ने पर अर्थ उलट जाएगा; ऽ चिह्न बताता है कि अ छिपा है। ‘अनियतः’ का शाब्दिक अर्थ ‘नियत नहीं’ है; यहाँ ‘अनुपस्थित’। संधि: समवायः + अपृथग्भावः → समवायो ऽपृथग्भावः; अपृथक् + भावः → अपृथग्भावः (क् → ग् घोष से पहले); भूमि + आदीनाम् → भूम्यादीनाम्; गुणैः + मतः → गुणैर्मतः; तत्र + अनियतः → तत्रानियतः। पाठभेद डेटा में नहीं हैं।",
}

AIDS = {
    "41": {
        "seesaw": "हित ↔ अहित, सुख ↔ दुःख: आयु के चार रूप दो जोड़ों में, और फिर ‘उसके लिए हित ↔ अहित’।",
        "frame": "क्या कहा जाए: आयु के हित-अहित, सुख-दुःख, उसके लिए क्या हितकर/अहितकर, मान, और आयु स्वयं · कहाँ: जिसमें ये कहे गए हों · नाम: आयुर्वेद।",
        "sandhi": "आयुः + तस्य → आयुस्तस्य (विसर्ग त से पहले स्) · यत्र + उक्तम् → यत्रोक्तम् (अ + उ → ओ) · आयुः + वेदः → आयुर्वेदः (घोष से पहले र्)।",
        "anchors": "आयुर्वेद = आयुः + वेद (आयु का ज्ञान) · हित ← हितकारी · मान = माप (मानदण्ड, परिमाण)।",
        "chunks": "हिताहितं सुखं | दुःखमायुः | तस्य हिताहितम् ‖ मानं च | तच्च | यत्रोक्तम् | आयुर्वेदः स उच्यते। (छपा: ‘दुखम्’।)",
    },
    "42": {
        "frame": "क्या: आयु · कैसे: संयोग · किनका: शरीर, इन्द्रिय, सत्त्व, आत्मा · दूसरे नाम: धारि, जीवित, नित्यग, अनुबन्ध।",
        "diagram": {"groups": [
            {"label": "संयोग", "items": ["शरीर", "इन्द्रिय", "सत्त्व", "आत्म"]},
            {"label": "पर्याय", "items": ["धारि", "जीवितम्", "नित्यगः", "अनुबन्धः"]}]},
        "letters": "श-इ-स-आ: शरीर · इन्द्रिय · सत्त्व · आत्मा | धा-जी-नि-अ: धारि · जीवित · नित्यग · अनुबन्ध।",
        "pegs": "चार पहियों की गाड़ी (मेरा बनाया चित्र): शरीर = ढाँचा, इन्द्रिय = खिड़कियाँ, सत्त्व = चालक, आत्मा = सवारी; चारों जुड़ें तभी गाड़ी चले = आयु।",
        "sandhi": "शरीर + इन्द्रिय → शरीरेन्द्रिय (अ + इ → ए) · सत्त्व + आत्म → सत्त्वात्म (अ + आ → आ) · नित्यगः + च → नित्यगश्च (विसर्ग + च → श्)।",
        "anchors": "संयोग ← सम् + √युज् (जोड़ना) · जीवित ← √जीव् (जीना) · पर्याय = समानार्थक शब्द।",
        "chunks": "शरीरेन्द्रियसत्त्वात्म | संयोगो धारि जीवितम् ‖ नित्यगश्चानुबन्धश्च | पर्यायैरायुरुच्यते।",
    },
    "43": {
        "frame": "किसका वेद: उस आयु का · किसके मत में: वेदविदों के · कैसा: पुण्यतम · आगे: जो मनुष्यों का दोनों लोकों में हित करे।",
        "chain": "आयु → उसका वेद → वेदविदों ने पुण्यतम माना → आगे वही कहा जाएगा जो दोनों लोकों में हितकर है।",
        "pegs": "पुण्यतम = सबसे ऊँची मीनार की चोटी (मेरा बनाया चित्र): ‘-तम’ = सबसे ऊपर।",
        "sandhi": "तस्य + आयुषः → तस्यायुषः (अ + आ → आ) · पुण्यतमः + वेदः → पुण्यतमो वेदः (विसर्ग → ओ) · यत् + मनुष्याणाम् → यन्मनुष्याणाम् (त् + म → न्म)।",
        "anchors": "वेदविद् = वेद + विद् (वेद जानने वाला) · उभय = दोनों।",
        "chunks": "तस्यायुषः | पुण्यतमो | वेदो वेदविदां मतः ‖ वक्ष्यते | यन्मनुष्याणां | लोकयोरुभयोर्हितम्।",
    },
    "44": {
        "seesaw": "सामान्य ↔ विशेष: सामान्य = वृद्धि का कारण ↔ विशेष = ह्रास का हेतु (प्रवृत्ति दोनों की)।",
        "frame": "कब: सदा · किसका: सब भावों का · क्या: सामान्य → वृद्धि, विशेष → ह्रास · प्रवृत्ति: दोनों की।",
        "pegs": "वृद्धि = सीढ़ी पर चढ़ना, ह्रास = सीढ़ी से उतरना (मेरा बनाया चित्र); सामान्य ऊपर ले जाता है, विशेष नीचे।",
        "sandhi": "ह्रासहेतुः + विशेषः → ह्रासहेतुर्विशेषः (घोष से पहले र्) · विशेषः + च → विशेषश्च (विसर्ग + च → श्) · प्रवृत्तिः + उभयस्य → प्रवृत्तिरुभयस्य (स्वर से पहले र्)।",
        "anchors": "कारण · हेतु = कारण (दोनों समान अर्थ) · भाव = पदार्थ/अवस्था · वृद्धि ↔ ह्रास (बढ़ना ↔ घटना)।",
        "chunks": "सर्वदा | सर्वभावानां | सामान्यं वृद्धिकारणम् ‖ ह्रासहेतुर्विशेषश्च | प्रवृत्तिरुभयस्य तु।",
    },
    "45": {
        "seesaw": "सामान्य ↔ विशेष: एकत्वकरम् ↔ पृथक्त्वकृत् · तुल्यार्थता ↔ विपर्ययः।",
        "frame": "सामान्य: एकत्व करता है, तुल्यार्थता है · विशेष: पृथक्त्व करता है, उसका विपर्यय है।",
        "letters": "ए-पृ: एकत्व (सामान्य) · पृथक्त्व (विशेष) | तु-वि: तुल्यार्थता · विपर्यय।",
        "sandhi": "विशेषः + तु → विशेषस्तु (विसर्ग + त → स्त) · तुल्य + अर्थता → तुल्यार्थता (अ + अ → आ) · सामान्यम् + एकत्वकरम् → सामान्यमेकत्वकरम्।",
        "anchors": "एकत्व ← एक (एक होना) · पृथक्त्व ← पृथक् (अलग) · विपर्यय = उलटा।",
        "contrast": "तुल्यार्थता (सामान्य: समान प्रयोजन) ↔ विपर्ययः (विशेष: उसका उलटा) · एकत्वकरम् ↔ पृथक्त्वकृत्।",
        "chunks": "सामान्यमेकत्वकरं | विशेषस्तु पृथक्त्वकृत् ‖ तुल्यार्थता हि सामान्यं | विशेषस्तु विपर्ययः।",
    },
    "46": {
        "frame": "कौन तीन: सत्त्व, आत्मा, शरीर · उपमा: त्रिदण्ड · परिणाम: संयोग से लोक टिके, उसी में सब प्रतिष्ठित।",
        "pegs": "तिपाई (मेरा बनाया चित्र): तीन पाए = मन, आत्मा, शरीर; ऊपर रखा सब कुछ = लोक; तीनों जुड़े हों तब तिपाई खड़ी रहे।",
        "story": "तीन डण्डे बाँधकर तिपाई बनती है → वैसे ही मन, आत्मा, शरीर जुड़ें → उनके संयोग से लोक टिके → उसी में सब कुछ प्रतिष्ठित।",
        "sandhi": "त्रयम् + एतत् → त्रयमेतत् · लोकः + तिष्ठति → लोकस्तिष्ठति (विसर्ग + त → स्त) · संयोगात् + तत्र → संयोगात्तत्र।",
        "anchors": "त्रिदण्ड = त्रि (तीन) + दण्ड (डण्डा) · प्रतिष्ठित ← प्रति + √स्था (टिका हुआ) · संयोग ← सम् + √युज्।",
        "chunks": "सत्त्वमात्मा शरीरं च | त्रयमेतत्त्रिदण्डवत् ‖ लोकस्तिष्ठति संयोगात् | तत्र सर्वं प्रतिष्ठितम्।",
    },
    "47": {
        "frame": "कौन: वही संयोग (पिछले श्लोक का) · क्या: पुमान्, चेतन, अधिकरण · किसलिए: इसी के लिए यह वेद प्रकाशित।",
        "chain": "संयोग (मन-आत्मा-शरीर) → पुमान् → चेतन → इस वेद का अधिकरण → उसी के लिए वेद प्रकाशित।",
        "pegs": "अधिकरण = मंच (मेरा बनाया चित्र): जिस मंच पर नाटक खेला जाए; आयुर्वेद का मंच यही संयोग है।",
        "sandhi": "पुमान् + चेतनम् → पुमांश्चेतनम् (न् + च → ंश्) · तत् + च → तच्च · वेदः + अयम् → वेदो ऽयम् (अः + अ → ओ ऽ) · तत् + अर्थम् → तदर्थम् (स्वर से पहले त् → द्)।",
        "anchors": "तदर्थम् = तत् + अर्थम् (उसके लिए) · प्रकाशित ← प्र + √काश् (चमकना, प्रकट होना) · चेतन ← √चित् (जानना)।",
        "chunks": "स पुमांश्चेतनं तच्च | तच्चाधिकरणं स्मृतम् ‖ वेदस्यास्य तदर्थं हि | वेदो ऽयं संप्रकाशितः।",
    },
    "48": {
        "frame": "क्या: द्रव्य का संग्रह · सदस्य: ख आदि, आत्मा, मन, काल, दिशाएँ · कसौटी: इन्द्रिय-सहित = चेतन, इन्द्रिय-रहित = अचेतन।",
        "diagram": {"groups": [
            {"label": "द्रव्यसंग्रह", "items": ["खादीनि", "आत्मा", "मनः", "कालः", "दिशः"]},
            {"label": "कसौटी", "items": ["सेन्द्रियं चेतनम्", "निरिन्द्रियम् अचेतनम्"]}]},
        "letters": "ख-आ-म-का-दि: खादि · आत्मा · मनः · कालः · दिशः।",
        "seesaw": "सेन्द्रिय ↔ निरिन्द्रिय · चेतन ↔ अचेतन: जिसके इन्द्रिय हैं वह चेतन, जिसके नहीं वह अचेतन।",
        "sandhi": "खादीनि + आत्मा → खादीन्यात्मा (इ + आ → य्+आ) · कालः + दिशः → कालो दिशः · स + इन्द्रियम् → सेन्द्रियम् (अ + इ → ए) · निः + इन्द्रियम् → निरिन्द्रियम्।",
        "anchors": "खादि = ख (आकाश) + आदि · सेन्द्रिय = स (सहित) + इन्द्रिय · निरिन्द्रिय = निः (रहित) + इन्द्रिय · अचेतन = अ + चेतन।",
        "chunks": "खादीन्यात्मा मनः कालो | दिशश्च द्रव्यसंग्रहः ‖ सेन्द्रियं चेतनं द्रव्यं | निरिन्द्रियमचेतनम्।",
    },
    "49": {
        "frame": "गुण: सार्थ · गुर्वादि · बुद्धि · प्रयत्नान्त · परादि · कर्म: प्रयत्न से आरम्भ होने वाली चेष्टा।",
        "contrast": "प्रयत्नान्ताः (प्रयत्न पर समाप्त, गुणों की सूची में) ↔ प्रयत्नादि (प्रयत्न से आरम्भ, कर्म के लिए): ‘अन्त’ और ‘आदि’ का फ़र्क।",
        "letters": "सा-गु-बु-प्र-प: सार्थ · गुर्वादि · बुद्धि · प्रयत्नान्त · परादि।",
        "sandhi": "गुरु + आदयः → गुर्वादयः (उ + आ → व्+आ) · प्रयत्न + अन्ताः → प्रयत्नान्ताः · पर + आदयः → परादयः · चेष्टितम् + उच्यते → चेष्टितमुच्यते।",
        "anchors": "प्रयत्न = प्र + यत्न (कोशिश) · चेष्टित ← √चेष्ट् (हिलना-डुलना) · कर्म = क्रिया (√कृ)।",
        "chunks": "सार्था गुर्वादयो बुद्धिः | प्रयत्नान्ताः परादयः ‖ गुणाः प्रोक्ताः | प्रयत्नादि कर्म चेष्टितमुच्यते।",
    },
    "50": {
        "frame": "क्या: समवाय · क्या है: अपृथग्भाव · किनका: भूमि आदि और उनके गुणों का · कैसा: नित्य · कारण: जहाँ द्रव्य वहाँ गुण।",
        "story": "मिट्टी हो तो उसका गुण साथ है → गुण को मिट्टी से अलग नहीं किया जा सकता → इसलिए यह सम्बन्ध नित्य कहा गया।",
        "pegs": "गुँथा हुआ धागा (मेरा बनाया चित्र): द्रव्य और गुण ऐसे गुँथे हैं कि एक को खींचो तो दूसरा साथ आए।",
        "sandhi": "समवायः + अपृथग्भावः → समवायो ऽपृथग्भावः (अः + अ → ओ ऽ) · अपृथक् + भावः → अपृथग्भावः (क् → ग्) · गुणैः + मतः → गुणैर्मतः · भूमि + आदीनाम् → भूम्यादीनाम् (इ + आ → य्+आ)।",
        "contrast": "अपृथग्भावः (अलग न होना) ↔ पृथग्भावः (अलग होना): शुरू का अ- निषेध। और न … अनियतः = अनुपस्थित नहीं, यानी सदा उपस्थित।",
        "anchors": "समवाय ← सम् + अव + √इ (साथ जुड़ा रहना) · अपृथक् = अ + पृथक् · नित्य = सदा।",
        "chunks": "समवायो ऽपृथग्भावो | भूम्यादीनां गुणैर्मतः ‖ स नित्यो यत्र हि द्रव्यं | न तत्रानियतो गुणः।",
    },
}

IMAGE_SPECS = {
    ("42", "diagram"): {
        "file": "union-42.svg",
        "alt": "Two columns: the union of four (body, sense faculties, mind, self) and the four synonyms of life (dhāri, jīvita, nityaga, anubandha)",
        "type": "split",
        "title": "आयु = संयोग",
        "cols": [["संयोग (चार)", ["शरीर", "इन्द्रिय", "सत्त्व", "आत्म"]],
                 ["पर्याय (चार)", ["धारि", "जीवितम्", "नित्यगः", "अनुबन्धः"]]],
    },
    ("45", "seesaw"): {
        "file": "common-special-45.svg",
        "alt": "A two-column table: commonality produces oneness and is sameness of purpose; distinctiveness produces separateness and is its opposite",
        "type": "table",
        "title": "सामान्य ↔ विशेष",
        "heads": ["सामान्य", "विशेष"],
        "rows": [["एकत्वकरम्", "पृथक्त्वकृत्"], ["तुल्यार्थता", "विपर्ययः"]],
    },
    ("48", "diagram"): {
        "file": "dravya-48.svg",
        "alt": "Two columns: the items of the summary of substances (kha and the rest, self, mind, time, directions) and the test of sentience (with senses: sentient; without senses: non-sentient)",
        "type": "split",
        "title": "द्रव्यसंग्रह",
        "cols": [["संग्रह", ["खादीनि", "आत्मा", "मनः", "कालः", "दिशः"]],
                 ["कसौटी", ["सेन्द्रियं चेतनम्", "निरिन्द्रियम् अचेतनम्"]]],
    },
}
