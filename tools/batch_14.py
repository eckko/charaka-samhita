from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}
NOTES_HI = {}
AIDS = {}

# --------------------------------------------------------------- unit 130
AUTHORED["130"] = {
    "title": "त्यक्तधर्मस्य पापस्य",
    "question": "What does the verse say happens to a man who merely talks with such a physician?",
    "rule": ("This verse finishes the sentence begun in 129: the four genitives "
             "(त्यक्तधर्मस्य, पापस्य, मृत्युभूतस्य, दुर्मतेः) describe the ignorant "
             "giver, resumed by तस्य. Even talking with him makes a man नरकपाती, "
             "'one who falls into hell'."),
    "limits": ("The verse does not say that talking with him is itself a crime, "
               "only that it is said to lead a man to hell. It is a strong "
               "warning in the style of the text, not a rule of treatment."),
    "explain_hi": ("यह श्लोक पिछले श्लोक का वाक्य पूरा करता है: ‘यः … प्रयच्छति’ (जो औषध "
                   "देता है) का उत्तर यहाँ ‘तस्य’ (उसके) में आता है। चार षष्ठी-शब्द "
                   "उसी बिना जाने औषध देने वाले का वर्णन करते हैं: धर्म छोड़ने वाला, "
                   "पापी, मृत्यु-रूप, दुर्बुद्धि। कहा गया है कि उससे बात करना भी "
                   "मनुष्य को ‘नरकपाती’ (नरक में गिरने वाला) बना देता है। यह कठोर "
                   "चेतावनी है, जो आगे के श्लोकों की निन्दा की भूमिका बनाती है।"),
    "hook": "यः (129) → तस्य (130): धर्मत्यागी, पापी, मृत्यु-रूप, दुर्मति; बात करना भी नरक की ओर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 129, यः introduces the man who gives medicine without knowing it. Which word of verse 130 picks that 'he' up again?",
            ("तस्य", "तस्य means 'of him' and refers back to the giver."),
            [("नरः", "नरः is the man who talks with him, a different person."),
             ("स्यात्", "स्यात् is a verb ('would be'), not a person."),
             ("अपि", "अपि means 'even'; it names no one.")],
            "तस्य picks up यः: the whole of 129-130 is one sentence.",
            "यः in 129 is answered by तस्य in 130."),
        match(1, "Match each description of the giver to its meaning.",
              [["त्यक्तधर्मस्य", "who has abandoned dharma"], ["पापस्य", "sinful"],
               ["मृत्युभूतस्य", "who is death itself"], ["दुर्मतेः", "evil-minded"]],
              "All four describe the same person, the ignorant giver of medicine.",
              "त्यक्तधर्म = abandoned dharma; पाप = sinful; मृत्युभूत = death itself; दुर्मति = evil-minded."),
        fill(2, "संभाषणादपि = संभाषणात् + ____ (type the word meaning 'even' in Devanagari).",
             ["अपि"],
             "अपि means 'even': even from talking with him.",
             "A final त् becomes द् before a vowel: संभाषणात् + अपि is written संभाषणादपि.",
             "संभाषणादपि = संभाषणात् + अपि, 'even from conversing'.",
             role="extend"),
        mcq("discriminate", 3, "Which is the right split of स्यात्तस्य?",
            ("स्यात् + तस्य", "The verb स्यात् ('would be') is followed by तस्य ('of him'); त् + त् simply stand together."),
            [("स्या + त्तस्य", "त्तस्य is not a word."),
             ("स्यात्त + स्य", "Neither piece is a word here."),
             ("स्यात् + अस्य", "That would be written स्यादस्य, with द्.")],
            "स्यात्तस्य = स्यात् + तस्य.",
            "स्यात्तस्य = स्यात् + तस्य."),
        multi("apply", 4, "Which of these describe the bad physician of verses 129-130?",
              [("पापस्य", "Right: 'sinful' describes him."),
               ("नरः", "This is the man who talks with him, not the physician."),
               ("दुर्मतेः", "Right: 'evil-minded' describes him."),
               ("संभाषणात्", "This is the act of talking, not a description of him."),
               ("मृत्युभूतस्य", "Right: 'who is death itself' describes him.")],
              [0, 2, 4],
              "The words in the 'of him' form describe the giver; नरः and संभाषणात् belong to the man who talks.",
              "The -स्य / -तेः words describe the giver."),
        mcq("transfer", 5,
            "A new line reads क्रूरस्य लुब्धस्य तस्य सेवनादपि नरो दुःखी स्यात्. Whom do क्रूरस्य and लुब्धस्य describe?",
            ("तस्य, the person served",
             "They end like तस्य ('of him') and describe the same person."),
            [("नरः, the man who serves",
              "नरः has a different ending; it is the man who suffers."),
             ("सेवनात्, the act of serving", "सेवनात् names an act, not a person."),
             ("दुःखी, the unhappy one", "दुःखी is the result, said of the man.")],
            "Describing words stand in the same form as the person they describe: -स्य ... -स्य ... तस्य.",
            "Words in the same ending as तस्य describe him.",
            teaches="You can find whom a string of describing words refers to by matching its ending to the person-word (तस्य) that closes it."),
    ],
}
NOTES_HI["130"] = ("यह श्लोक 129 से चला आता है (यः … तस्य)। ‘संभाषणादपि’ = संभाषणात् + अपि (अघोष त् स्वर से पहले ‘द्’ बनता है)। "
                   "‘स्यात्तस्य’ में स्यात् + तस्य बिना बदलाव जुड़े हैं। ‘नरो’ में नरः का विसर्ग घोष ‘न’ से पहले ‘ओ’ बना है। "
                   "स्रोत में पाठभेद या पाठ-दोष नहीं दिया गया।")
AIDS["130"] = {
    "frame": "कौन: बिना जाना औषध देने वाला (यः → तस्य) · क्या: उससे बात भी · फल: मनुष्य नरकपाती।",
    "sandhi": "त् + स्वर → द्: संभाषणात् + अपि → संभाषणादपि · विसर्ग (अः) + घोष → ओ: नरः + नरकपाती → नरो नरकपाती।",
    "contrast": "यः (129, ‘जो’) और तस्य (130, ‘उसका’): एक ही व्यक्ति, एक ही वाक्य के दो श्लोक।",
    "anchors": "संभाषण ← सम् + भाष (बोलना): ‘मिलकर बात करना’ · नरकपाती = नरक + पाती (गिरने वाला)।",
    "chunks": "त्यक्तधर्मस्य पापस्य | मृत्युभूतस्य दुर्मतेः ‖ नरो नरकपाती स्यात् | तस्य संभाषणादपि।",
}

# --------------------------------------------------------------- unit 131
AUTHORED["131"] = {
    "title": "वरमाशीविषविषं",
    "question": "What three things does verse 131 call better than something to be named in the next verse?",
    "rule": ("वरम् = 'better'. Better to drink snake venom, or molten copper, "
             "or to swallow iron balls heated in fierce fire. The 'than what' "
             "comes in 132: the sentence is not finished here."),
    "limits": ("The verse names only the three harsh things; what they are "
               "preferred to is said in 132. The source writes वा ऽपि with an "
               "avagraha, where plain sandhi would give वापि."),
    "explain_hi": ("श्लोक ‘वरम्’ (बेहतर) से खुलता है और तीन कठोर बातें गिनाता है: "
                   "साँप का विष पी लेना, खौलता हुआ ताँबा पी लेना, या आग में तपे "
                   "लोहे के गोले निगल लेना। ‘पीतम्’ विष और ताँबे के साथ जुड़ता है, "
                   "‘भक्षिताः’ लोहे के गोलों के साथ। ‘किसकी तुलना में बेहतर’ यह बात "
                   "श्लोक १३२ में पूरी होती है, इसलिए दोनों श्लोक एक वाक्य हैं।"),
    "hook": "वरम् (बेहतर): विष पीना · ताँबा पीना · लोहे के गोले निगलना — पर किससे बेहतर? 132 में।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The verse opens with the word वरम्. What does it announce?",
            ("A comparison: the following things are called better",
             "वरम् means 'better': what follows is preferred to something."),
            [("A command to the student", "वरम् is not a verb of command."),
             ("A question put to the sages", "Nothing here is a question."),
             ("A list of medicines", "The items named are harsh things, not medicines.")],
            "वरम् sets up a comparison: A is better (than B).",
            "वरम् = better; a comparison follows."),
        match(1, "Match each word to its meaning.",
              [["आशीविषविषम्", "snake's venom"], ["ताम्रम्", "copper"],
               ["अयोगुडाः", "iron balls"], ["क्वथितम्", "boiled, molten"]],
              "These are the harsh things named in the verse.",
              "आशीविषविषम् = snake's venom; ताम्रम् = copper; अयोगुडाः = iron balls; क्वथितम् = boiled, molten."),
        fill(2, "The word for 'drunk' that goes with the venom and the copper is ____ (type it in Devanagari).",
             ["पीतम्", "पीतं"],
             "पीतम् is 'drunk'.",
             "पीतम् is a past participle in the neuter singular, so it goes with the neuter singular nouns (the venom and the copper).",
             "पीतम् = drunk; it agrees with the venom and the copper.",
             role="extend"),
        mcq("discriminate", 3,
            "भक्षिता वा in the second line has a long -आ ending, though the iron balls are plural. What explains it?",
            ("The visarga of -आः drops before the voiced sound भ् / व्",
             "-आः + a voiced consonant gives -आ: सन्तप्ताः भक्षिताः → सन्तप्ता भक्षिता."),
            [("The word is a singular feminine noun", "The data reads it as masculine plural, agreeing with अयोगुडाः."),
             ("It is a dual form", "The dual of such a word would end in -औ."),
             ("The poet left the ending out by mistake", "This is regular sandhi, not a mistake.")],
            "सन्तप्ताः and भक्षिताः lose their visarga before a voiced sound, leaving -आ.",
            "-आः before a voiced consonant → -आ."),
        order(4, "Put the three things in the order of the verse.",
              ["आशीविषविषम्", "ताम्रम्", "अयोगुडाः"],
              "The venom comes first, the copper next, the iron balls last.",
              "Venom, then copper, then iron balls.", role="apply"),
        mcq("transfer", 5,
            "A speaker begins a new line with वरं मौनम् (invented) and then pauses. What do you expect next?",
            ("Something that silence is preferred to",
             "वरम् starts a comparison, so the thing that is worse still has to be named."),
            [("A prayer to Indra", "Nothing in वरम् points to a prayer."),
             ("A list of medicines", "वरम् starts a comparison, not a list of medicines."),
             ("The end of the chapter", "वरम् opens a sentence, it does not close one.")],
            "As in 131 → 132, वरम् leaves the 'worse' side to be supplied.",
            "वरम् A ... : the worse alternative follows.",
            teaches="When a sentence opens with वरम्, look ahead for the alternative it is being preferred to."),
    ],
}
NOTES_HI["131"] = ("‘वरम् … न तु’ (131-132) एक वाक्य है। ‘पीतम्’ आशीविषविषम् और ताम्रम् के साथ, ‘भक्षिताः’ अयोगुडाः के साथ जुड़ता है। "
                   "‘सन्तप्ता भक्षिता वा’ में आः का विसर्ग घोष (भ्, व्) से पहले लुप्त हुआ है। स्रोत में ‘वा ऽप्ययोगुडाः’ अवग्रह के साथ छपा है; "
                   "सामान्य सन्धि से ‘वाप्ययोगुडाः’ होता। ‘क्वथितम्’ का शाब्दिक अर्थ ‘उबाला हुआ’ है, यहाँ ‘पिघला/खौलता’।")
AIDS["131"] = {
    "diagram": {"groups": [
        {"label": "पहली पंक्ति",
         "items": ["वरम्", "आशीविषविषम्", "क्वथितं ताम्रम्"]},
        {"label": "दूसरी पंक्ति",
         "items": ["अत्यग्निसन्तप्ताः", "भक्षिताः", "अयोगुडाः"]}]},
    "pegs": "मेरा बनाया चित्र: साँप का फन, खौलती कड़ाही, लाल दहकते लोहे के गोले: तीन ‘कठोर’ चित्र, जिन्हें 132 के काम से कम बुरा कहा गया है।",
    "sandhi": "-आः + घोष → -आ: सन्तप्ताः भक्षिताः → सन्तप्ता भक्षिता · इ + असवर्ण स्वर → य्: अपि + अयोगुडाः → अप्ययोगुडाः (वा के बाद अ का ऽ)।",
    "chunks": "वरमाशीविषविषं | क्वथितं ताम्रमेव वा ‖ पीतमत्यग्निसन्तप्ता | भक्षिता वा ऽप्ययोगुडाः।",
}

# --------------------------------------------------------------- unit 132
AUTHORED["132"] = {
    "title": "नतु श्रुतवतां वेशं",
    "question": "What does verse 132 say is not better, after the harsh things of 131?",
    "rule": ("न तु = 'but not'. It completes 131: not better (is it) for one who "
             "wears the garb of the learned to have taken food, drink or money "
             "from a disease-afflicted person who came to him for refuge."),
    "limits": ("The verse is about a pretender who only wears the learned "
               "man's garb. The text has वेशं; वेषं "
               "('garb') is the usual spelling, so वेशं may be a spelling variant."),
    "explain_hi": ("यह श्लोक १३१ का उत्तरार्ध है: ‘वरम् … न तु’। विष पीना भी बेहतर है, "
                   "किन्तु विद्वानों का वेश धारण करने वाले (बिना योग्यता के) व्यक्ति के "
                   "द्वारा शरण में आए रोगी से अन्न, पान या धन लेना बेहतर नहीं। "
                   "‘बिभ्रता’ तृतीया में है: ‘धारण करने वाले के द्वारा’, यानी जिसने "
                   "लिया। ‘शरणागतात्’ और ‘रोगपीडितात्’ पञ्चमी में हैं: जिससे लिया गया। "
                   "‘वेशम्’ सम्भवतः ‘वेषम्’ की वर्तनी-भिन्नता है।"),
    "hook": "विष पीना बेहतर, पर न तु: विद्वान का वेश पहनकर शरणागत रोगी से अन्न, पान या धन लेना नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 131 said what is better. The word न तु at the start of 132 does what?",
            ("It rules out the opposite: taking food, drink or money this way is not better",
             "न तु = 'but not': the second half of the comparison."),
            [("It repeats that the venom is better", "न तु turns to something else."),
             ("It starts a new, unrelated topic", "The two verses form one sentence."),
             ("It asks the patient a question", "Nothing here is a question.")],
            "न तु completes the comparison: A is better, but not B.",
            "वरम् ... न तु = better ..., but not ...."),
        match(1, "Match each word to its meaning.",
              [["अन्नम्", "food"], ["पानम्", "drink"], ["वित्तम्", "wealth, money"],
               ["रोगपीडितात्", "from one afflicted by disease"]],
              "The three things taken, and the one they are taken from.",
              "अन्नम् = food; पानम् = drink; वित्तम् = money; रोगपीडितात् = from one afflicted by disease."),
        fill(2, "नतु = न + ____ (type the second word, meaning 'but', in Devanagari).",
             ["तु"],
             "The source writes नतु as one token; it is न + तु.",
             "नतु is न ('not') + तु ('but'), the pair that finishes the comparison begun by वरम्.",
             "नतु = न + तु = 'but not'.",
             role="extend"),
        mcq("discriminate", 3, "Which word names the person who takes the food, drink or money?",
            ("बिभ्रता, 'by one wearing' the garb",
             "It is the 'by' form; the wearer of the learned man's garb is the one who took."),
            [("शरणागतात्", "This is the person it was taken from (the refugee)."),
             ("रोगपीडितात्", "This is also the patient it was taken from."),
             ("श्रुतवताम्", "This means 'of the learned': the people whose garb is copied.")],
            "बिभ्रता (by the wearer) is the taker; the two -आत् words are the patient.",
            "बिभ्रता is a 'by' form of बिभ्रत्; the -आत् words are 'from' forms."),
        multi("apply", 4, "Which three things does the verse say are taken from the patient?",
              [("अन्नम्", "Right: food."),
               ("औषधम्", "Medicine is not among the things named in this verse."),
               ("पानम्", "Right: drink."),
               ("वित्तम्", "Right: money."),
               ("वेशम्", "The garb is worn by the taker, not taken from the patient.")],
              [0, 2, 3],
              "Food, drink and money are taken; the garb is worn.",
              "अन्नम्, पानम्, वित्तम् are what is taken."),
        mcq("transfer", 5,
            "In a new line धनुर्बिभ्रता वीरेण शत्रुर्जितः (invented), who carries the bow?",
            ("वीर, the hero",
             "बिभ्रता (carrying) and वीरेण (by the hero) are both 'by' forms, so बिभ्रता describes वीरेण, as it names the taker in 132."),
            [("शत्रु, the enemy", "The enemy was defeated; he is not the carrier."),
             ("धनुः, the bow itself", "The bow is what is carried."),
             ("No one is named", "वीरेण names him.")],
            "बिभ्रता agrees with the 'by' word: whoever it describes does the carrying.",
            "बिभ्रता + 'by' person = the one who carries.",
            teaches="A describing word in the 'by' case (here बिभ्रता) agrees with the 'by' person and names the doer, as in 132."),
    ],
}
NOTES_HI["132"] = ("पाठ-संकेत: ‘वेशं’ सम्भवतः ‘वेषं’ (वेश/पोशाक) की वर्तनी-भिन्नता है; हस्तलेखों में वेश और वेष प्रायः मिल जाते हैं। "
                   "‘नतु’ स्रोत में एक शब्द के रूप में है, पढ़ें न + तु। ‘गृहीतम्’ भावे-प्रयोग है, जैसे श्लोक १३१ में ‘पीतम्’। "
                   "‘शरणागतात्’ = शरण + आगतात् (अ + आ → आ)। ‘गृहीतमन्नम्’ = गृहीतम् + अन्नम्।")
AIDS["132"] = {
    "frame": "कौन: विद्वान का वेश धारण करने वाला · किससे: शरण में आए रोगी से · क्या लिया: अन्न, पान या धन · निर्णय: यह बेहतर नहीं।",
    "contrast": "131: वरम् (बेहतर: विष, ताँबा, लोहे के गोले) ↔ 132: न तु (बेहतर नहीं: रोगी से लेना)।",
    "sandhi": "अ + आ → आ: शरण + आगतात् → शरणागतात् · म् + अ: गृहीतम् + अन्नम् → गृहीतमन्नम्।",
    "chunks": "नतु श्रुतवतां वेशं | बिभ्रता शरणागतात् ‖ गृहीतमन्नं पानं वा | वित्तं वा रोगपीडितात्।",
}

# --------------------------------------------------------------- unit 133
AUTHORED["133"] = {
    "title": "भिषग्बुभूषुर्मतिमान्",
    "question": "What should a wise person who wishes to become a physician strive for, and why?",
    "rule": ("अतः = 'therefore'. A wise person who wishes to become a physician "
             "should make the utmost effort towards perfecting his own qualities, "
             "so that he may be a life-giver (प्राणदः) to people."),
    "limits": ("The verse gives the aim (own qualities) and the purpose (giving "
               "life), not a list of the qualities. भिषग्बुभूषुः can also be "
               "read 'a physician wishing to prosper'."),
    "explain_hi": ("निन्दा के बाद यहाँ सीख आती है: ‘अतः’ (इसलिए) बुद्धिमान, वैद्य बनने "
                   "का इच्छुक व्यक्ति अपने गुणों की सम्पन्नता में परम प्रयत्न करे। "
                   "लक्ष्य दिया गया है: ‘यथा प्राणदः स्यात् नृणाम्’, जिससे वह लोगों को "
                   "प्राण देने वाला हो। ‘बुभूषुः’ इच्छार्थक रूप है: ‘होना चाहने वाला’। "
                   "कुछ लोग इसे ‘समृद्धि चाहने वाला वैद्य’ भी पढ़ते हैं।"),
    "hook": "अतः · वैद्य बनने का इच्छुक · अपने गुणों में परम प्रयत्न · ताकि प्राणदाता बने।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "According to verse 133, in what should an aspiring physician make the utmost effort?",
            ("Perfecting his own qualities",
             "स्वगुणसम्पदि = in the accomplishment of his own qualities."),
            [("Collecting fees from patients", "Verse 132 condemned taking money from the pretender's patients; no such aim is given."),
             ("Defeating other physicians", "Nothing in the verse speaks of rivals."),
             ("Finding a king as patron", "No patron or king is mentioned.")],
            "The effort is directed at his own qualities.",
            "Effort goes into स्वगुणसम्पद्, one's own qualities."),
        match(1, "Match each word to its meaning.",
              [["भिषक्", "a physician"], ["बुभूषुः", "wishing to be"],
               ["मतिमान्", "intelligent"], ["प्राणदः", "giver of life"]],
              "Four words that carry the verse.",
              "भिषक् = physician; बुभूषुः = wishing to be; मतिमान् = intelligent; प्राणदः = giver of life."),
        fill(2, "The verse says he should make the utmost ____ (type the Devanagari word for 'effort', with or without the ending).",
             ["प्रयत्नम्", "प्रयत्नं", "प्रयत्न"],
             "प्रयत्नम् means 'effort'.",
             "प्रयत्नम् is the object of आतिष्ठेत् ('should undertake'), qualified by परम् ('utmost').",
             "परं प्रयत्नम् = utmost effort.",
             role="extend"),
        mcq("discriminate", 3, "Which word of the verse gives the purpose 'so that'?",
            ("यथा", "यथा with स्यात् ('may be') means 'so that he may be'."),
            [("अतः", "अतः means 'therefore': it points back to the reason, not forward to the purpose."),
             ("परम्", "परम् means 'utmost' and qualifies the effort."),
             ("सम्पदि", "सम्पदि means 'in the perfecting'; it names the field in which the effort is made.")],
            "अतः gives the reason from before; यथा gives the aim that follows.",
            "अतः = therefore (reason); यथा = so that (purpose)."),
        mcq("apply", 4,
            "A student who wishes to be a physician puts all his effort into earning, none into his own qualities. Which advice of 133 does he ignore?",
            ("Making the utmost effort at the perfection of his own qualities",
             "That is the effort the verse asks for."),
            [("Refusing to take any medicine", "That is not what this verse says."),
             ("Avoiding all conversation with patients", "Nothing like this is said here."),
             ("Waiting until others approve of him", "No approval is mentioned in this verse.")],
            "He ignores the verse's main advice: effort at his own qualities.",
            "The aim is one's own qualities, not income."),
        mcq("transfer", 5,
            "A new word जिजीविषुः is built like बुभूषुः. What does it most likely mean?",
            ("Wishing to live",
             "The wish-form ending -षु (after a doubled syllable) means 'wishing to', so जिजीविषुः = wishing to live."),
            [("One who has lived", "Past action would not use this wish-ending."),
             ("One who gives life", "That is the sense of प्राणदः, a different word."),
             ("One who is afraid of life", "Nothing in the form suggests fear.")],
            "बुभूषुः = wishing to be; जिजीविषुः = wishing to live.",
            "Doubled syllable + -षु = 'wishing to ...'.",
            teaches="You can read a new wish-word by comparing it with बुभूषुः."),
    ],
}
NOTES_HI["133"] = ("‘भिषग्बुभूषुः’ को ‘वैद्य बनने का इच्छुक’ पढ़ा गया है; वैकल्पिक पाठ ‘समृद्धि चाहने वाला वैद्य’ भी सम्भव है (बुभूषु = उन्नति चाहने वाला)। "
                   "सन्धि: भिषक् + बुभूषुः → भिषग्बुभूषुः (क् → ग्, घोष ब् से पहले); बुभूषुः + मतिमान् → बुभूषुर्मतिमान् (विसर्ग → र्); "
                   "स्यात् + यथा → स्याद्यथा (त् → द्, घोष य् से पहले)।")
AIDS["133"] = {
    "frame": "कौन: बुद्धिमान, वैद्य बनने का इच्छुक · क्या करे: अपने गुणों में परम प्रयत्न · क्यों: ताकि प्राणदाता बने।",
    "story": "एक बुद्धिमान युवक वैद्य बनना चाहता है → दूसरों की निन्दा देखकर पहले अपने गुण सँवारता है → ताकि लोगों के लिए प्राणदाता बने।",
    "anchors": "प्राणद = प्राण + द (देने वाला), जैसे अन्नद, धनद · मतिमान् = मति (बुद्धि) + मान् (वाला) · बुभूषु ← √भू (होना) की इच्छा।",
    "sandhi": "क् + घोष → ग्: भिषक् + बुभूषुः → भिषग्बुभूषुः · विसर्ग → र् (घोष से पहले): बुभूषुः + मतिमान् → बुभूषुर्मतिमान् · त् + य → द्य: स्यात् + यथा → स्याद्यथा।",
    "chunks": "भिषग्बुभूषुर्मतिमान् | अतः स्वगुणसम्पदि ‖ परं प्रयत्नमातिष्ठेत् | प्राणदः स्याद्यथा नृणाम्।",
}

# --------------------------------------------------------------- unit 134
AUTHORED["134"] = {
    "title": "तदेव युक्तं भैषज्यं",
    "question": "By what test does the verse judge a medicine and a physician?",
    "rule": ("That alone is proper medicine which conduces to health "
             "(यदारोग्याय कल्पते); that one alone is the best of physicians "
             "who frees (patients) from diseases. The test is the result."),
    "limits": ("The verse gives the test, not the method: it does not say "
               "how the physician frees the patient. भैषज्य can mean medicine "
               "or treatment; the patient is only implied."),
    "explain_hi": ("यहाँ कसौटी परिणाम है। पहली पंक्ति: ‘वही भैषज्य युक्त (उचित) है जो "
                   "आरोग्य के लिए समर्थ हो’ (यत् … तत्)। दूसरी पंक्ति: ‘वही वैद्यों में "
                   "श्रेष्ठ है जो रोगों से छुड़ा दे’ (यः … सः)। दोनों में ‘एव’ (ही) "
                   "जोर देता है। कैसे छुड़ाया जाए, यह श्लोक नहीं बताता; रोगी का शब्द भी "
                   "अनकहा है। ‘भैषज्य’ का अर्थ औषध भी हो सकता है और चिकित्सा भी।"),
    "hook": "यत् … तत्: जो आरोग्य करे वही औषध; यः … सः: जो रोगों से छुड़ाए वही श्रेष्ठ वैद्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "According to verse 134, what makes a medicine proper (युक्त)?",
            ("That it conduces to health",
             "यदारोग्याय कल्पते = which is capable of bringing about health."),
            [("That it is costly", "Cost is never mentioned."),
             ("That a famous physician gives it", "Fame plays no part in the test."),
             ("That it tastes strong", "The test is its effect on health, not its taste.")],
            "The test is whether it conduces to health.",
            "Proper medicine = the one that conduces to health."),
        match(1, "Match each word to its meaning.",
              [["तत्", "that"], ["युक्तम्", "proper"], ["आरोग्याय", "for health"],
               ["कल्पते", "conduces"]],
              "The words of the first line.",
              "तत् = that; युक्तम् = proper; आरोग्याय = for health; कल्पते = conduces."),
        fill(2, "सः भिषजां ____, meaning he is the best of physicians (type the Devanagari word for 'best', with or without the ending).",
             ["श्रेष्ठः", "श्रेष्ठो", "श्रेष्ठ"],
             "श्रेष्ठः means 'the best'.",
             "श्रेष्ठः is nominative singular, agreeing with सः; the visarga becomes ओ before the voiced र् of रोगेभ्यः (श्रेष्ठो रोगेभ्यः).",
             "श्रेष्ठो = श्रेष्ठः (best).",
             role="extend"),
        mcq("discriminate", 3,
            "Verse 132 mentioned someone who wears the garb of the learned. By the test in 134, which marks the best physician?",
            ("Freeing people from diseases",
             "The test of 134 is the result for the patient."),
            [("Wearing the garb of the learned", "134 never names the garb as a test."),
             ("Taking food, drink and money from patients", "132 rejects this."),
             ("Speaking well to patients", "The verse's test is freeing from disease.")],
            "The verse's test is freeing people from disease, not the garb.",
            "Best physician = he who frees from disease (the garb is not the test)."),
        multi("apply", 4, "Which statements follow from verse 134?",
              [("A medicine that does not conduce to health is not 'proper' by this test",
                "Right: only the one that conduces to health is called proper."),
               ("The best physician is the one who frees people from diseases",
                "Right: this is the verse's own statement."),
               ("A medicine is proper if it is expensive", "Cost is not a test in the verse."),
               ("The verse says the physician frees people by diet alone", "The verse does not say how.")],
              [0, 1],
              "Both tests are about results: health for the medicine, freedom from disease for the physician.",
              "Proper medicine → health; best physician → freedom from disease."),
        mcq("transfer", 5,
            "A new line reads तदेव शस्त्रं यद्रणे जयाय कल्पते (invented). By the same rule, what makes a weapon proper?",
            ("That it conduces to victory in battle",
             "यत् … तत् with कल्पते + 'for ...' says: that which serves the end is the proper one."),
            [("That it is made of gold", "The rule is about serving the end, not material."),
             ("That a king owns it", "Ownership is not the test."),
             ("That it is lighter than others", "Weight is not mentioned.")],
            "'तदेव X यत् Y-आय कल्पते' = that alone is the proper X which serves Y.",
            "तदेव ... यत् ... कल्पते = that alone is proper which serves the end.",
            teaches="The pattern तदेव X यत् ...-आय कल्पते lets you read any 'that alone is proper which serves such-and-such' line."),
    ],
}
NOTES_HI["134"] = ("सन्धि: तद् रूप ‘तत् + एव’ → तदेव; ‘यत् + आरोग्याय’ → यदारोग्याय (त् → द्, स्वर से पहले); ‘स च + एव’ में च + एव → चैव (अ + ए → ऐ); "
                   "‘श्रेष्ठः’, ‘रोगेभ्यः’ के विसर्ग घोष से पहले ‘ओ’ बने (श्रेष्ठो रोगेभ्यो)। ‘भैषज्य’ औषध और चिकित्सा, दोनों हो सकता है। "
                   "‘प्रमोचयेत्’ का कर्म (रोगी) अनकहा है। स्रोत में पाठभेद नहीं दिया गया।")
AIDS["134"] = {
    "frame": "कसौटी: परिणाम · औषध: जो आरोग्य करे · वैद्य: जो रोगों से छुड़ाए · जोर: ‘एव’ (ही)।",
    "contrast": "यत् … तत् (पंक्ति १: औषध की कसौटी) और यः … सः (पंक्ति २: वैद्य की कसौटी): जोड़ी में कही गई दो कसौटियाँ।",
    "story": "मेरी बनाई कहानी: दो वैद्य: एक के वस्त्र और ग्रन्थ भव्य हैं पर रोगी वैसे ही रहते हैं; दूसरे के रोगी रोग से मुक्त होते हैं। श्लोक के अनुसार श्रेष्ठ दूसरा है।",
    "sandhi": "त् + स्वर → द्: तत् + एव → तदेव · यत् + आरोग्याय → यदारोग्याय · अ + ए → ऐ: च + एव → चैव।",
    "chunks": "तदेव युक्तं भैषज्यं | यदारोग्याय कल्पते ‖ स चैव भिषजां श्रेष्ठो | रोगेभ्यो यः प्रमोचयेत्।",
}

# --------------------------------------------------------------- unit 135
AUTHORED["135"] = {
    "title": "सम्यक्प्रयोगं सर्वेषां",
    "question": "What does the verse say success proclaims?",
    "rule": ("सिद्धिः (success) proclaims (आख्याति) two things: the correct "
             "application of all procedures, and the best physician, endowed "
             "with all the qualities (भिषक्तमम्)."),
    "limits": ("The verse does not define सिद्धि; it only says what success "
               "shows. कर्म is taken as therapeutic procedures; the second "
               "statement is joined to the first by च."),
    "explain_hi": ("कसौटी की बात यहाँ आगे बढ़ती है: ‘सिद्धि’ (सफलता) दो बातें प्रकट करती है। "
                   "पहली, सभी कर्मों (चिकित्सा-क्रियाओं) का सम्यक् प्रयोग हुआ। दूसरी, "
                   "सभी गुणों से युक्त श्रेष्ठ वैद्य कौन है। ‘आख्याति’ का अर्थ ‘कहती है, "
                   "प्रकट करती है’ है, इसलिए सफलता गवाह की तरह है। ‘भिषक्तमम्’ में ‘-तम’ "
                   "श्रेष्ठता-सूचक है: ‘सबसे अच्छा वैद्य’।"),
    "hook": "सिद्धि बोलती है: ‘प्रयोग सही था’ और ‘यह वैद्य गुणयुक्त, सबसे श्रेष्ठ है’।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In verse 135, what proclaims (आख्याति) the correct application of all procedures?",
            ("सिद्धिः, success", "सिद्धिः is the subject of आख्याति in both lines."),
            [("श्रद्धा, trust", "Trust appears in verse 129, not as the proclaimer here."),
             ("धनम्, wealth", "Wealth is not mentioned in 135."),
             ("कीर्तिः, fame", "Fame is not mentioned in 135.")],
            "सिद्धिः is the subject: success proclaims.",
            "सिद्धिः आख्याति = success proclaims."),
        match(1, "Match each word to its meaning.",
              [["सिद्धिः", "success"], ["आख्याति", "proclaims"],
               ["कर्मणाम्", "of procedures, actions"], ["भिषक्तमम्", "the best physician"]],
              "The four key words.",
              "सिद्धिः = success; आख्याति = proclaims; कर्मणाम् = of procedures; भिषक्तमम् = the best physician."),
        fill(2, "भिषक्तमम् = भिषक् + ____: type the ending that means 'most' (it makes 'best') in Devanagari.",
             ["तमम्", "तमं", "तम"],
             "-तम is the ending of the superlative: भिषक् + तमम् = the best physician.",
             "-तम added to a word means 'the most ...': भिषक्तम = the most physician-like, the best physician.",
             "भिषक् + तम = best physician.",
             role="extend"),
        mcq("discriminate", 3, "Which is the right split of सिद्धिराख्याति?",
            ("सिद्धिः + आख्याति", "A visarga before a vowel becomes र्, so सिद्धिः + आख्याति is written सिद्धिराख्याति."),
            [("सिद्धि + राख्याति", "राख्याति is not a word."),
             ("सिद्धिः + ख्याति", "The verb is आख्याति, with आ."),
             ("सिद्धी + आख्याति", "That would give सिद्ध्याख्याति.")],
            "सिद्धिराख्याति = सिद्धिः + आख्याति.",
            "सिद्धिः + आख्याति → सिद्धिराख्याति."),
        mcq("apply", 4,
            "A physician's procedures, done correctly, lead to success again and again. By verse 135, what does that success do?",
            ("It proclaims the correct application of his procedures",
             "सिद्धिः आख्याति सम्यक्प्रयोगम्."),
            [("It makes his procedures correct afterwards", "Success proclaims; it does not cause the correctness."),
             ("It proves he took money from patients", "135 says nothing about money."),
             ("It shows that no medicine was needed", "Nothing like this is said.")],
            "Success shows that the application was correct.",
            "सिद्धि shows सम्यक्प्रयोग."),
        mcq("transfer", 5,
            "A new line reads समृद्धिर्गृहस्थस्य यत्नमाख्याति (invented). By the same sense of आख्याति, what does the prosperity do?",
            ("It shows the householder's effort",
             "आख्याति = proclaims, shows: the result speaks for what lies behind it."),
            [("It hides the effort", "आख्याति means to proclaim, not to hide."),
             ("It causes the effort", "The effect proclaims the cause, not the reverse."),
             ("It ends the effort", "Nothing about ending is said.")],
            "A result can 'proclaim' its cause, as success proclaims correct practice.",
            "result + आख्याति + cause = the result shows the cause.",
            teaches="You can read a result-word as a witness to its cause whenever आख्याति joins them."),
    ],
}
NOTES_HI["135"] = ("‘आख्याति’ (आ + √ख्या, ‘प्रकट करती है’) दोनों पंक्तियों में आया है; दूसरी पंक्ति का ‘च’ दोनों कथनों को जोड़ता है। "
                   "सन्धि: सिद्धिः + आख्याति → सिद्धिराख्याति (विसर्ग → र्, स्वर से पहले); सर्वैः + च → सर्वैश्च (विसर्ग → श्, च से पहले); "
                   "गुणैः + युक्तम् → गुणैर्युक्तम् (विसर्ग → र्, घोष य् से पहले)। ‘कर्म’ यहाँ चिकित्सा-क्रियाएँ हैं।")
AIDS["135"] = {
    "frame": "कौन बोलता है: सिद्धि (सफलता) · क्या कहती है: (१) कर्मों का सम्यक् प्रयोग, (२) सर्वगुणयुक्त श्रेष्ठ वैद्य।",
    "chain": "सिद्धि → आख्याति (प्रकट) → (१) सर्व कर्मों का सम्यक् प्रयोग, (२) सर्वगुणयुक्त भिषक्तम।",
    "diagram": {"groups": [
        {"label": "पंक्ति १",
         "items": ["सम्यक्प्रयोगम्", "सर्वेषाम्", "सिद्धिः आख्याति", "कर्मणाम्"]},
        {"label": "पंक्ति २",
         "items": ["सिद्धिः आख्याति", "सर्वैः गुणैः युक्तम्", "भिषक्तमम्"]}]},
    "anchors": "भिषक्तमम् ← भिषक् + तम (सबसे): जैसे श्रेष्ठतम, उत्तमतम · आख्याति ← आ + √ख्या: व्याख्यास्यामः (अध्याय का पहला वाक्य, इकाई 1) से जुड़ा मूल।",
    "sandhi": "विसर्ग → र् (स्वर से पहले): सिद्धिः + आख्याति → सिद्धिराख्याति · विसर्ग → श् (च से पहले): सर्वैः + च → सर्वैश्च · विसर्ग → र् (घोष से पहले): गुणैः + युक्तम् → गुणैर्युक्तम्।",
    "chunks": "सम्यक्प्रयोगं सर्वेषां | सिद्धिराख्याति कर्मणाम् ‖ सिद्धिराख्याति सर्वैश्च | गुणैर्युक्तं भिषक्तमम्।",
}

# --------------------------------------------------------------- unit 136
AUTHORED["136"] = {
    "title": "आयुर्वेदागमो हेतुः",
    "question": "Which topics does the first part of the closing list name?",
    "rule": ("A list of topics, each in the naming (nominative) form: the coming "
             "of Āyurveda; its cause; the propagation of the received teaching; "
             "the approval of composing treatises; the definition of Āyurveda."),
    "limits": ("The list has no verb and runs to verse 140. हेतुरागमस्य can be "
               "read 'the cause of the coming' or as two items. आगम means both "
               "'arrival' and 'received teaching'."),
    "explain_hi": ("यहाँ से अध्याय के विषयों की सूची शुरू होती है, जो श्लोक १४० तक चलती "
                   "है। सूची में क्रियापद नहीं; हर विषय अपना नाम (प्रथमा) लेकर आता है: "
                   "आयुर्वेद का आगमन, उसका हेतु, आगम का प्रवर्तन, सूत्रण (ग्रन्थ-रचना) "
                   "का अभ्यनुज्ञान, और आयुर्वेद का निर्णय। ‘आगम’ का अर्थ ‘आना’ भी है "
                   "और ‘प्राप्त परम्परागत ज्ञान’ भी। ‘हेतुरागमस्य’ को ‘आगमन का हेतु’ भी "
                   "पढ़ा जा सकता है।"),
    "hook": "सूची शुरू: आगम · हेतु · प्रवर्तन · सूत्रण का अभ्यनुज्ञान · निर्णय (आगे श्लोक 140 तक)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 136 has no verb, only a string of nouns. What kind of passage is it?",
            ("A list of topics whose closing statement comes later",
             "Nouns without a verb are items of a list; the closing statement is in verse 140."),
            [("A story about the sages", "No person or event is narrated."),
             ("An order given to the student", "There is no verb of command."),
             ("A prayer", "No god is addressed.")],
            "A run of nouns with no verb is a list; look ahead for what completes it.",
            "A verbless run of nouns = list of topics."),
        match(1, "Match each word to its meaning.",
              [["आगमः", "coming, arrival"], ["प्रवर्तनम्", "propagation"],
               ["अभ्यनुज्ञानम्", "approval"], ["निर्णयः", "definition, determination"]],
              "Four of the five topics.",
              "आगमः = coming; प्रवर्तनम् = propagation; अभ्यनुज्ञानम् = approval; निर्णयः = definition."),
        fill(2, "आयुर्वेदागमः = आयुर्वेद + ____ (type the second word, 'coming', in Devanagari).",
             ["आगमः", "आगमो", "आगम"],
             "आगमः is the second member.",
             "आयुर्वेद + आगमः: अ + आ → आ, giving आयुर्वेदागमः (and the visarga becomes ओ before the voiced ह of हेतुः).",
             "आयुर्वेदागमः = आयुर्वेद + आगमः.",
             role="extend"),
        mcq("discriminate", 3, "आगमस्य can carry two senses. Which two?",
            ("Arrival, and the received (traditional) teaching",
             "आगम means both: 'coming' and the teaching that came down."),
            [("Arrival, and departure", "Departure is not a sense of आगम."),
             ("Teaching, and the student", "आगम does not mean the student."),
             ("Cause, and effect", "Those are हेतु and कार्य, different words.")],
            "आगम = what has come: both the arrival and the teaching received.",
            "आगम = arrival / received teaching."),
        order(4, "Put the five topics in the order of the verse.",
              ["आयुर्वेदस्य आगमः", "हेतुः", "आगमस्य प्रवर्तनम्",
               "सूत्रणस्य अभ्यनुज्ञानम्", "आयुर्वेदस्य निर्णयः"],
              "Coming, cause, propagation, approval of composition, definition.",
              "आगम → हेतु → प्रवर्तन → अभ्यनुज्ञान → निर्णय.", role="apply"),
        mcq("transfer", 5,
            "A teacher announces: विषयाः शब्दः, अर्थः, प्रयोगः, निर्णयः (invented). What is this line?",
            ("A list of topics (nouns with no verb)",
             "Nouns in a row without a verb are a list, as in 136."),
            [("A complete command to the class", "There is no verb, so there is no command."),
             ("A single compound word", "The items are separate words."),
             ("A question to the class", "Nothing here is a question.")],
            "As in 136 → 140, read a verbless row of nouns as a list and look for a summing-up line, if any.",
            "Verbless nouns in a row = a list.",
            teaches="When you meet a row of naming-form nouns with no verb, treat it as a list of topics and look ahead for a sentence that sums it up, if there is one."),
    ],
}
NOTES_HI["136"] = ("विश्वास मध्यम। सूची श्लोक १४० तक चलती है, इसलिए इसे अकेले श्लोक की तरह न पढ़ें। ‘हेतुरागमस्य’ के दो पाठ सम्भव हैं: "
                   "‘आगमन का हेतु’ या ‘हेतु’ और ‘आगम का प्रवर्तन’ अलग विषय। ‘सूत्रणस्याभ्यनुज्ञानम्’ = सूत्रणस्य + अभ्यनुज्ञानम् (अ + अ → आ); "
                   "‘हेतुरागमस्य’ = हेतुः + आगमस्य (विसर्ग → र्)। ‘सूत्रण’ = ग्रन्थ को सूत्र-रूप में रचना।")
AIDS["136"] = {
    "diagram": {"groups": [
        {"label": "पंक्ति १",
         "items": ["आयुर्वेदागमः", "हेतुः", "आगमस्य प्रवर्तनम्"]},
        {"label": "पंक्ति २",
         "items": ["सूत्रणस्य", "अभ्यनुज्ञानम्", "आयुर्वेदस्य निर्णयः"]}]},
    "letters": "आ-हे-प्र | सू-अ-नि (आगम, हेतु, प्रवर्तन | सूत्रण, अभ्यनुज्ञान, निर्णय)।",
    "anchors": "आगम ← आ + √गम् (आना) · प्रवर्तन ← प्र + √वृत् (चलाना) · अभ्यनुज्ञान ← अभि + अनु + √ज्ञा (अनुमति) · निर्णय ← निर् + √नी (तय करना)।",
    "sandhi": "विसर्ग → र् (स्वर से पहले): हेतुः + आगमस्य → हेतुरागमस्य · अ + अ → आ: सूत्रणस्य + अभ्यनुज्ञानम् → सूत्रणस्याभ्यनुज्ञानम्।",
    "chunks": "आयुर्वेदागमो हेतुः | आगमस्य प्रवर्तनम् ‖ सूत्रणस्याभ्यनुज्ञानम् | आयुर्वेदस्य निर्णयः।",
}

# --------------------------------------------------------------- unit 137
AUTHORED["137"] = {
    "title": "संपूर्णं कारणं कार्यम्",
    "question": "Which further topics does verse 137 add to the list?",
    "rule": ("The list goes on: the complete cause, the effect, the purpose of "
             "Āyurveda; the causes (of disease), the doṣas, medicine; and "
             "'in brief' (संग्रहेण)."),
    "limits": ("संपूर्णं कारणम् is just 'the complete cause' in the verse; the "
               "reading as the six categories is the chapter's, not the verse's. "
               "संग्रहेण may qualify only भेषजम् or the whole list."),
    "explain_hi": ("सूची आगे बढ़ती है: सम्पूर्ण कारण, कार्य, आयुर्वेद का प्रयोजन; फिर "
                   "हेतु (रोगों के कारण), दोष और भेषज। अन्त में ‘संग्रहेण’ (संक्षेप में) "
                   "है; वह केवल ‘भेषज’ के साथ भी जुड़ सकता है और पूरी सूची के साथ भी। "
                   "‘संपूर्णं कारणम्’ श्लोक में केवल ‘पूरा कारण’ है; उसे छह पदार्थों से "
                   "जोड़ना अध्याय का सन्दर्भ है, श्लोक का नहीं।"),
    "hook": "सूची जारी: पूरा कारण · कार्य · प्रयोजन | हेतु · दोष · भेषज — संक्षेप में।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which item of verse 137 names the purpose of Āyurveda?",
            ("आयुर्वेदप्रयोजनम्", "प्रयोजनम् means 'purpose'; the compound is 'purpose of Āyurveda'."),
            [("दोषाः", "दोषाः are the doṣas."),
             ("भेषजम्", "भेषजम् is medicine."),
             ("हेतवः", "हेतवः are causes (of disease).")],
            "आयुर्वेदप्रयोजनम् = the purpose of Āyurveda.",
            "प्रयोजनम् = purpose."),
        match(1, "Match each word to its meaning.",
              [["कारणम्", "cause"], ["कार्यम्", "effect"], ["दोषाः", "doṣas"],
               ["भेषजम्", "medicine"]],
              "Four of the items of the list.",
              "कारणम् = cause; कार्यम् = effect; दोषाः = doṣas; भेषजम् = medicine."),
        fill(2, "In हेतवश्चैव the small emphatic word after च is ____ (type it in Devanagari; it means indeed, alone).",
             ["एव"],
             "हेतवश्चैव = हेतवः + च + एव.",
             "च + एव joins into चैव (अ + ए → ऐ), and the visarga of हेतवः becomes श् before च.",
             "हेतवश्चैव = हेतवः + च + एव.",
             role="extend"),
        mcq("discriminate", 3,
            "136 had हेतुः and 137 has हेतवः. How do they differ?",
            ("हेतुः is singular 'the cause'; हेतवः is plural 'causes'",
             "Both are the naming form of the same noun; only the number differs."),
            [("हेतुः is plural; हेतवः is singular", "It is the other way round."),
             ("हेतुः is dual; हेतवः is singular", "Neither is dual."),
             ("They are two unrelated words", "They are one noun in two numbers.")],
            "हेतुः (136) is the one cause; हेतवः (137) are causes.",
            "-उः singular / -अवः plural for words like हेतु."),
        multi("apply", 4, "Which are named in the second line of verse 137?",
              [("हेतवः", "Right: the causes."),
               ("रसाः", "रसाः belongs to the next verse."),
               ("दोषाः", "Right: the doṣas."),
               ("कारणम्", "कारणम् is in the first line."),
               ("भेषजम्", "Right: medicine.")],
              [0, 2, 4],
              "Line 2: हेतवः, दोषाः, भेषजम् and then संग्रहेण (in brief).",
              "Line 2 names causes, doṣas, medicine."),
        mcq("transfer", 5,
            "A new line joins two words with च: पुत्रः + च. How is it written as one word?",
            ("पुत्रश्च",
             "A visarga before च becomes श्, as in हेतवः + च → हेतवश्च."),
            [("पुत्रच", "The visarga does not simply vanish before च."),
             ("पुत्रोच", "ओ appears before voiced sounds, not before च."),
             ("पुत्रस्च", "स् appears before त्, not before च.")],
            "Visarga + च → श्च, the same rule as हेतवश्च and दोषाश्च.",
            "visarga + च → श्च.",
            teaches="You can join any word ending in a visarga with च by changing the visarga to श्."),
    ],
}
NOTES_HI["137"] = ("विश्वास मध्यम। ‘संपूर्णं कारणम्’ को अध्याय में छह पदार्थों (सामान्य आदि) से जोड़ा जाता है, पर श्लोक में केवल ‘पूरा कारण’ है। "
                   "‘संग्रहेण’ केवल ‘भेषजम्’ का विशेषण भी हो सकता है और पूरी सूची का भी। सन्धि: हेतवः + च → हेतवश्च; दोषाः + च → दोषाश्च "
                   "(विसर्ग → श्, च से पहले); च + एव → चैव (अ + ए → ऐ); कार्यम् + आयुर्वेद → कार्यमायुर्वेद…।")
AIDS["137"] = {
    "diagram": {"groups": [
        {"label": "पंक्ति १",
         "items": ["संपूर्णं कारणम्", "कार्यम्", "आयुर्वेदप्रयोजनम्"]},
        {"label": "पंक्ति २",
         "items": ["हेतवः", "दोषाः", "भेषजम्", "संग्रहेण"]}]},
    "letters": "सं-का-का-आ | हे-दो-भे-सं (संपूर्ण कारण, कार्य, आयुर्वेदप्रयोजन | हेतु, दोष, भेषज, संग्रह)।",
    "sandhi": "विसर्ग → श् (च से पहले): हेतवः + च → हेतवश्च; दोषाः + च → दोषाश्च · अ + ए → ऐ: च + एव → चैव · म् + स्वर: कार्यम् + आयुर्वेद… → कार्यमायुर्वेद…।",
    "chunks": "संपूर्णं कारणं कार्यम् | आयुर्वेदप्रयोजनम् ‖ हेतवश्चैव दोषाश्च | भेषजं संग्रहेण च।",
}

# --------------------------------------------------------------- unit 138
AUTHORED["138"] = {
    "title": "रसाः सप्रत्ययद्रव्याः",
    "question": "Which further topics does verse 138 add to the list?",
    "rule": ("The list goes on: the tastes (रसाः) together with their "
             "underlying substances; the threefold classification of "
             "substances; the root-plants, the fruit-plants, the fats and "
             "the salts."),
    "limits": ("The verse only names the topics. 'Threefold' is not spelled "
               "out here, and प्रत्यय is read as 'cause, basis'; it could "
               "also be rendered 'condition'."),
    "explain_hi": ("सूची में अगले विषय आते हैं: रस (स्वाद) अपने आधारभूत द्रव्यों के साथ "
                   "(‘सप्रत्ययद्रव्याः’, यानी उन आधार-रूप द्रव्यों सहित जो उनके प्रत्यय हैं), "
                   "द्रव्यों का त्रिविध संग्रह, फिर मूलिनी (जड़ वाली), फलिनी (फल वाली), "
                   "स्नेह (चिकनाई) और लवण। ‘स-’ यहाँ ‘सहित’ का अर्थ देता है। श्लोक केवल "
                   "विषयों के नाम गिनाता है; ‘त्रिविध’ के तीन भेद यहाँ नहीं बताए गए।"),
    "hook": "रस + उनके द्रव्य · द्रव्य के तीन संग्रह · मूलिनी · फलिनी · स्नेह · लवण।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which of these is named in verse 138?",
            ("मूलिन्यः, the root-plants",
             "मूलिन्यः is in the second line."),
            [("क्षीराणि, the milks", "क्षीराणि comes in the next verse."),
             ("मूत्रम्, urine", "मूत्रम् comes in the next verse."),
             ("वैद्यापवादः, censure of physicians", "That comes at the very end, in verse 140.")],
            "138 names tastes, classes of substances, root-plants, fruit-plants, fats and salts.",
            "138 includes मूलिन्यः."),
        match(1, "Match each word to its meaning.",
              [["रसाः", "tastes"], ["मूलिन्यः", "root-plants"],
               ["फलिन्यः", "fruit-plants"], ["स्नेहाः", "fats, oils"]],
              "Four of the topics named.",
              "रसाः = tastes; मूलिन्यः = root-plants; फलिन्यः = fruit-plants; स्नेहाः = fats."),
        fill(2, "The verse speaks of a ____-fold classification of substances, त्रिविधः (type the number).",
             ["3", "३", "three", "Three", "तीन", "त्रि"],
             "त्रि- means three.",
             "त्रिविधः = three kinds; the verse says the classification is threefold but does not list the three here.",
             "त्रिविध = threefold.",
             role="extend"),
        mcq("discriminate", 3, "In सप्रत्ययद्रव्याः, what does the opening स- add?",
            ("'Together with': the tastes with their underlying substances",
             "स- here means 'with', giving 'with their underlying substances'."),
            [("'Without': tastes with no underlying substances", "स- does not mean 'without'."),
             ("'Six': six underlying substances", "The count 'six' would be षष्-."),
             ("'Not': tastes that are not substances", "'Not' would be अ-.")],
            "सप्रत्ययद्रव्याः = tastes together with their underlying substances.",
            "स- = with."),
        order(4, "Put the four plant and substance classes in the order of the second line.",
              ["मूलिन्यः", "फलिन्यः", "स्नेहाः", "लवणानि"],
              "Root-plants, fruit-plants, fats, salts.",
              "मूलिनी → फलिनी → स्नेह → लवण.", role="apply"),
        mcq("transfer", 5,
            "In a new line, सपत्रा लता (invented) is used of a creeper. How do you read सपत्रा?",
            ("With leaves, as in the form 'स- = with'",
             "सपत्रा = स + पत्रा, built like सप्रत्यय-: it means 'having leaves'."),
            [("Without leaves", "That would need अ- or निः-."),
             ("Leaves of six kinds", "स- is not the number six."),
             ("A creeper of salt", "Nothing suggests salt.")],
            "स- + noun = 'having / together with' that noun.",
            "स + X = together with X.",
            teaches="The opening स- turns a noun into 'together with it', so you can read new words like सपत्र."),
    ],
}
NOTES_HI["138"] = ("विश्वास मध्यम। ‘सप्रत्ययद्रव्याः’ बहुव्रीहि है: ‘प्रत्यय’ (कारण/आधार) रूप द्रव्यों सहित; ‘प्रत्यय’ को ‘कारण’ या ‘परिस्थिति’ भी लिया जा सकता है। "
                   "सन्धि: द्रव्याः + त्रिविधः → द्रव्यास्त्रिविधः (विसर्ग → स्, त् से पहले); मूलिन्यः + च → मूलिन्यश्च; फलिन्यः + च → फलिन्यश्च; "
                   "स्नेहाः + च → स्नेहाश्च (विसर्ग → श्, च से पहले); त्रिविधः → त्रिविधो (घोष द् से पहले ओ)।")
AIDS["138"] = {
    "diagram": {"groups": [
        {"label": "पंक्ति १",
         "items": ["रसाः", "सप्रत्ययद्रव्याः", "त्रिविधः", "द्रव्यसंग्रहः"]},
        {"label": "पंक्ति २",
         "items": ["मूलिन्यः", "फलिन्यः", "स्नेहाः", "लवणानि"]}]},
    "letters": "र-स-त्रि-द्र | मू-फ-स्ने-ल (रस, सप्रत्ययद्रव्य, त्रिविध, द्रव्यसंग्रह | मूलिनी, फलिनी, स्नेह, लवण)।",
    "pegs": "मेरा बनाया चित्र: जीभ (रस) → चार टोकरियाँ: जड़ें (मूलिनी), फल (फलिनी), घी का दीया (स्नेह), नमक की डली (लवण)।",
    "anchors": "मूलिनी ← मूल (जड़) · फलिनी ← फल · स्नेह = चिकनाई (तेल, घी) · लवण = नमक।",
    "sandhi": "विसर्ग → स् (त् से पहले): द्रव्याः + त्रिविधः → द्रव्यास्त्रिविधः · विसर्ग → श् (च से पहले): मूलिन्यः + च → मूलिन्यश्च।",
    "chunks": "रसाः सप्रत्ययद्रव्याः | त्रिविधो द्रव्यसंग्रहः ‖ मूलिन्यश्च फलिन्यश्च | स्नेहाश्च लवणानि च।",
}

# --------------------------------------------------------------- unit 139
AUTHORED["139"] = {
    "title": "मूत्रं क्षीराणि वृक्षाश्च",
    "question": "Which further topics does verse 139 add, and what are the six trees defined by?",
    "rule": ("The list goes on: urine; the milks; the six trees whose useful "
             "parts are latex and bark (क्षीरत्वगाश्रयाः); the actions of all "
             "these; and the merits and faults of proper and improper use."),
    "limits": ("The verse names no tree. योगायोगगुणागुणाः can be read as "
               "'merits and faults of proper and improper use' or as a "
               "four-item list (proper use, improper use, merits, faults)."),
    "explain_hi": ("सूची में आगे: मूत्र, क्षीर (दूध), और ‘षड् वृक्षाः’, छह वृक्ष, जिनके "
                   "काम के अंग क्षीर (दूध-रस) और त्वचा (छाल) हैं (क्षीरत्वगाश्रयाः)। फिर "
                   "इन सबके कर्म, और ‘योगायोगगुणागुणाः’। इसका एक पाठ है: योग (उचित प्रयोग) "
                   "और अयोग (अनुचित प्रयोग) के गुण और अगुण (दोष); दूसरा पाठ चार अलग "
                   "विषय। श्लोक में किसी वृक्ष का नाम नहीं आया।"),
    "hook": "मूत्र · क्षीर · छह वृक्ष (क्षीर-त्वक्) · सबके कर्म · योग–अयोग के गुण–अगुण।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "By which useful parts does verse 139 describe the six trees?",
            ("Latex (क्षीर) and bark (त्वक्)",
             "क्षीरत्वगाश्रयाः = those whose seat of use is latex and bark."),
            [("Roots and fruits", "Those belong to the plants of verse 138 (मूलिनी, फलिनी)."),
             ("Leaves and flowers", "Leaves and flowers are not mentioned."),
             ("Wood and seed", "Wood and seed are not mentioned.")],
            "The six trees are defined by latex and bark.",
            "षड् वृक्षाः = क्षीर + त्वक् as आश्रय."),
        match(1, "Match each word to its meaning.",
              [["मूत्रम्", "urine"], ["क्षीराणि", "milks"], ["वृक्षाः", "trees"],
               ["कर्माणि", "actions"]],
              "Four of the topics of the verse.",
              "मूत्रम् = urine; क्षीराणि = milks; वृक्षाः = trees; कर्माणि = actions."),
        fill(2, "In क्षीरत्वगाश्रयाः the word for 'bark' is ____ (type its base form in Devanagari).",
             ["त्वक्", "त्वग्", "त्वच्", "त्वच", "त्वक", "त्वचा"],
             "त्वक् / त्वच् means bark (skin).",
             "क्षीर-त्वक्-आश्रयाः: the क् becomes ग् before the vowel आ, giving त्वगाश्रयाः.",
             "त्वक् = bark.",
             role="extend"),
        mcq("discriminate", 3, "In the pair योग / अयोग, what does अयोग stand for?",
            ("Improper application",
             "अ- reverses योग, 'proper application', giving 'improper application'."),
            [("Proper application", "That is योग itself."),
             ("A medicine", "Neither word names a medicine."),
             ("Success", "सिद्धि is the word for success (verse 135).")],
            "योग = proper use; अयोग = improper use.",
            "अयोग = the reverse of योग."),
        multi("apply", 4, "Which are named in verse 139?",
              [("लवणानि", "Salts are in verse 138."),
               ("मूत्रम्", "Right: urine."),
               ("स्नेहाः", "Fats are in verse 138."),
               ("क्षीराणि", "Right: the milks."),
               ("वृक्षाः", "Right: the six trees.")],
              [1, 3, 4],
              "Urine, milks and the six trees are in 139; salts and fats are in 138.",
              "139: मूत्र, क्षीर, वृक्ष; 138: स्नेह, लवण."),
        mcq("transfer", 5,
            "Following the pair गुण / अगुण, what does a new word अलवण most likely mean?",
            ("Without salt, not salty",
             "अ- reverses or negates, so अलवण = without salt."),
            [("Full of salt", "अ- does not mean 'full of'."),
             ("A kind of salt", "अ- turns the sense to its opposite."),
             ("A fruit", "Nothing in the word suggests fruit.")],
            "अ- + word = the opposite or lack of it.",
            "अ + X = not X.",
            teaches="The negative अ- before a consonant lets you read a new word like अलवण from the word it reverses."),
    ],
}
NOTES_HI["139"] = ("विश्वास मध्यम। ‘योगायोगगुणागुणाः’ के दो विग्रह सम्भव हैं: (१) योग और अयोग के गुण–अगुण, (२) चार पदों का द्वन्द्व। "
                   "‘क्षीरत्वगाश्रयाः’ = क्षीर + त्वक् + आश्रयाः (क् → ग्, स्वर से पहले)। ‘षड्’ = षट् का ‘ड्’ रूप (ट् → ड्, घोष य् से पहले)। "
                   "‘चैषाम्’ = च + एषाम् (अ + ए → ऐ)। ‘मूत्रम्’ एकवचन में है; श्लोक में मूत्र के प्रकार नहीं गिनाए गए। श्लोक ११९ के ‘दिष्टपयस्त्वचः’ से इसका मेल है।")
AIDS["139"] = {
    "diagram": {"groups": [
        {"label": "पंक्ति १",
         "items": ["मूत्रम्", "क्षीराणि", "वृक्षाः षड्", "क्षीरत्वगाश्रयाः"]},
        {"label": "पंक्ति २",
         "items": ["कर्माणि एषां सर्वेषाम्", "योगायोगगुणागुणाः"]}]},
    "letters": "मू-क्षी-वृ-क्षी | क-यो (मूत्र, क्षीर, वृक्ष, क्षीर-त्वक् | कर्म, योग–अयोग)।",
    "seesaw": "एक पाठ के अनुसार: योग ↔ अयोग (उचित प्रयोग ↔ अनुचित प्रयोग) · गुण ↔ अगुण (गुण ↔ दोष): अ- उलटा कर देता है।",
    "anchors": "क्षीर = दूध / वृक्ष का दूध-रस · त्वक् = छाल (त्वचा) · आश्रय = जिसमें टिका हो (काम का अंग)।",
    "chunks": "मूत्रं क्षीराणि वृक्षाश्च | षड् ये क्षीरत्वगाश्रयाः ‖ कर्माणि चैषां सर्वेषां | योगायोगगुणागुणाः।",
}

# --------------------------------------------------------------- unit 140
AUTHORED["140"] = {
    "title": "वैद्यापवादो यत्रस्थाः",
    "question": "How does verse 140 close the list begun in verse 136?",
    "rule": ("The last items: the censure of physicians, and (the passage) in "
             "which all physicians' qualities are found. Then the summary: "
             "सर्वमेतत् समाख्यातम्, all this has been fully explained in the "
             "first chapter by the great sage."),
    "limits": ("यत्रस्थाः is cryptic: '(the section) where the qualities "
               "stand' or '(the physician) in whom they reside'. पूर्वाध्याये "
               "is read as 'in the first chapter'. The sage is not named here."),
    "explain_hi": ("सूची यहाँ समाप्त होती है: अन्तिम विषय हैं वैद्य की निन्दा "
                   "(‘वैद्यापवादः’) और वह प्रसंग जिसमें वैद्यों के सभी गुण स्थित हैं "
                   "(‘यत्रस्थाः’, जिसके दो पाठ हैं: वह खण्ड, या वह वैद्य)। फिर सार-वाक्य: "
                   "‘सर्वमेतत् समाख्यातम्’, यह सब पहले अध्याय में महर्षि ने भली-भाँति "
                   "कह दिया है। महर्षि का नाम श्लोक में नहीं दिया गया; समाख्यातम् "
                   "भूतकालिक कृदन्त है, यानी बात कही जा चुकी।"),
    "hook": "अन्त: वैद्य की निन्दा · सब वैद्य-गुण | सार: ‘सर्वमेतत् समाख्यातम्’ — पहले अध्याय में महर्षि द्वारा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "How does verse 140 end the list that began in verse 136?",
            ("It says that all this has been fully explained in the earlier ('first') chapter",
             "सर्वमेतत् समाख्यातं पूर्वाध्याये = all this has been fully explained in the earlier ('first') chapter."),
            [("It adds a new list of diseases", "It closes the list; it adds none."),
             ("It asks the sages to explain more", "Nothing is asked."),
             ("It names the writer of the chapter", "The sage is called only महर्षिणा, 'by the great sage', not named.")],
            "The closing sentence sums the list up: सर्वमेतत् समाख्यातम्.",
            "140 closes the list with a summary sentence."),
        match(1, "Match each word to its meaning.",
              [["वैद्यापवादः", "censure of physicians"], ["गुणाः", "qualities"],
               ["समाख्यातम्", "has been fully explained"], ["महर्षिणा", "by the great sage"]],
              "The key words of the closing verse.",
              "वैद्यापवादः = censure of physicians; गुणाः = qualities; समाख्यातम् = fully explained; महर्षिणा = by the great sage."),
        fill(2, "वैद्यापवादः = वैद्य + ____ (type the second word, meaning 'censure', in Devanagari).",
             ["अपवादः", "अपवादो", "अपवाद"],
             "अपवादः is 'censure'.",
             "वैद्य + अपवादः: अ + अ → आ, giving वैद्यापवादः; the visarga becomes ओ before the voiced य of यत्रस्थाः.",
             "वैद्यापवादः = वैद्य + अपवादः.",
             role="extend"),
        mcq("discriminate", 3, "What does the verse itself say about the 'great sage'?",
            ("He is called only the great sage; no personal name is given here",
             "The verse says महर्षिणा and nothing more."),
            [("It names him Indra", "Indra is not mentioned in 140."),
             ("It names him Bharadvāja", "Bharadvāja is not mentioned in 140."),
             ("It says several sages spoke", "महर्षिणा is singular.")],
            "The sage is unnamed in this verse.",
            "महर्षिणा = by the great sage (unnamed)."),
        mcq("apply", 4,
            "समाख्यातम् is a past participle. What does it tell you about the topics of the list?",
            ("They have already been explained",
             "A past participle states a finished action: 'has been explained'."),
            [("They will be explained later", "That would need a future form."),
             ("They are being asked about now", "Nothing here is a question."),
             ("They must not be explained", "Nothing here forbids it.")],
            "समाख्यातम् = has been fully explained: the topics are already covered.",
            "Past participle = a finished action."),
        mcq("transfer", 5,
            "A new text lists topics and closes सर्वमेतद् उक्तं द्वितीयेऽध्याये (invented). What does the ending tell you?",
            ("The listed topics were treated in the second chapter",
             "As in 140, the closing line points back to where the listed topics were dealt with."),
            [("They will be treated in a later chapter", "उक्तम् is a past participle: already said."),
             ("The topics are all rejected", "Nothing in the ending says so."),
             ("The topics are still unnamed", "The list has just named them.")],
            "A closing 'all this has been said in chapter X' sends you back to that chapter.",
            "सर्वमेतत् ... उक्तम्/समाख्यातम् + chapter = the summary points back.",
            teaches="When a list ends with 'all this was said in chapter X', treat it as a table of contents pointing back."),
    ],
}
NOTES_HI["140"] = ("विश्वास मध्यम। ‘यत्रस्थाः’ के दो पाठ सम्भव हैं: ‘(वह प्रसंग) जिसमें वैद्यों के सभी गुण स्थित हैं’ या ‘(वह वैद्य) जिसमें सभी गुण रहते हैं’; "
                   "समीक्षक के अनुसार टीकाकार दूसरा पाठ भी लेते हैं, जिसे चक्रपाणि से मिलाना शेष है। ‘पूर्वाध्याये’ का अर्थ ‘प्रथम अध्याय में’ एक व्याख्या है। "
                   "‘महर्षि’ का नाम श्लोक में नहीं है। सन्धि: वैद्य + अपवादः → वैद्यापवादः (अ + अ → आ); अपवादः + यत्र → अपवादो यत्र; "
                   "सर्वम् + एतत् → सर्वमेतत्; पूर्व + अध्याये → पूर्वाध्याये।")
AIDS["140"] = {
    "frame": "सूची का अन्त: वैद्य की निन्दा · सब वैद्य-गुण | सार-वाक्य: यह सब पहले अध्याय में, महर्षि द्वारा, भली-भाँति कहा जा चुका।",
    "anchors": "समाख्यातम् ← सम् + आ + √ख्या (आख्याति, श्लोक 135 का ही मूल) · अपवाद = निन्दा · महर्षि = महा + ऋषि।",
    "sandhi": "अ + अ → आ: वैद्य + अपवादः → वैद्यापवादः; पूर्व + अध्याये → पूर्वाध्याये · विसर्ग → ओ (घोष से पहले): अपवादः + यत्र → अपवादो यत्र · म् + स्वर: सर्वम् + एतत् → सर्वमेतत्।",
    "chunks": "वैद्यापवादो यत्रस्थाः | सर्वे च भिषजां गुणाः ‖ सर्वमेतत् समाख्यातं | पूर्वाध्याये महर्षिणा।",
}
