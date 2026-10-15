from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}

# ---------------------------------------------------------------- unit 90
AUTHORED["90"] = {
    "title": "आलेपनार्थे युज्यन्ते",
    "question": "For which procedures are the salts used, according to the first part of the list?",
    "rule": ("आलेपनार्थे … युज्यन्ते = the salts are used for pastes, in oleation and "
             "sudation, in evacuations of the lower and upper parts, in decoction "
             "enemas and in oil enema. The list goes on in verses 91-92."),
    "limits": ("The verse does not say how each salt is used or which salt suits which "
               "procedure; adhobhāga / ūrdhvabhāga are read as purgation and emesis "
               "only through the edition's note. The list continues in verse 91."),
    "explain_hi": ("पिछले श्लोकों में लवणों के नाम आए; अब उनके प्रयोग गिनाए जा रहे हैं। "
                   "‘आलेपनार्थे’ का अर्थ है ‘लेप के प्रयोजन से’ और ‘युज्यन्ते’ का ‘प्रयोग "
                   "किए जाते हैं’ (बहुवचन, क्योंकि लवण कई हैं)। फिर स्नेहन–स्वेदन की विधि, "
                   "अधोभाग–ऊर्ध्वभाग के शोधन (टिप्पणी के अनुसार विरेचन और वमन), "
                   "निरूह बस्ति और अनुवासन बस्ति आते हैं। यह सूची अगले श्लोक में भी चलती है।"),
    "hook": "लवण के प्रयोग (१): लेप → स्नेहन–स्वेदन → नीचे–ऊपर के शोधन → निरूह → अनुवासन।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verses 88-89 named the salts. What do you expect verse 90 to begin?",
            ("A list of the procedures in which the salts are used",
             "The verse says the salts are used for pastes and in several procedures."),
            [("The names of five more salts", "Verse 89 already closed the set at five."),
             ("The eight urines", "The urines are announced only at the end of verse 92."),
             ("The names of the sages", "The sages were listed in verses 8-13.")],
            "Verse 90 starts the uses of the salts, introduced by आलेपनार्थे … युज्यन्ते.",
            "Verse 90 begins the uses of the salts."),
        match(1, "Match each word of the verse to its meaning.",
              [["आलेपनार्थे", "for the purpose of pastes"],
               ["स्नेहस्वेदविधौ", "in oleation and sudation procedures"],
               ["निरूहेषु", "in decoction enemas"],
               ["अनुवासने", "in oil enema"]],
              "These words name four of the uses in the verse.",
              "आलेपनार्थे = for pastes; स्नेहस्वेदविधौ = in oleation and sudation procedures; निरूहेषु = in decoction enemas; अनुवासने = in oil enema."),
        fill(2, "The word meaning 'likewise' in the first line is ____ (type it in Devanagari).",
             ["तथा"],
             "तथा links the oleation and sudation procedures to the pastes just named.",
             "तथा is an indeclinable meaning 'likewise, and so'; it adds one more item to the list of uses.",
             "तथा = likewise."),
        mcq("discriminate", 3, "Which is the right split of निरूहेष्वनुवासने?",
            ("निरूहेषु + अनुवासने",
             "उ before a different vowel becomes व्, so निरूहेषु + अनुवासने is written निरूहेष्वनुवासने."),
            [("निरूहेष्व + अनुवासने", "निरूहेष्व is not a word."),
             ("निरूहे + ष्वनुवासने", "ष्वनुवासने is not a word."),
             ("निरूहेषु + वनुवासने", "वनुवासने is not a word; the व् comes from the join.")],
            "निरूहेष्वनुवासने = निरूहेषु ('in decoction enemas') + अनुवासने ('in oil enema').",
            "निरूहेष्वनुवासने = निरूहेषु + अनुवासने."),
        multi("apply", 4, "Which of these are named in verse 90 as uses of the salts?",
              [("आलेपन (pastes)", "Right: the verse begins with आलेपनार्थे."),
               ("अनुवासन (oil enema)", "Right: अनुवासने closes the verse."),
               ("निरूह (decoction enema)", "Right: निरूहेषु is in the second line."),
               ("शस्त्रकर्म (surgery)", "Not in this verse; it is not named here."),
               ("अञ्जन (collyrium)", "Not in this verse; it is not named here.")],
              [0, 1, 2],
              "Verse 90 names pastes, oleation and sudation, the two evacuations, decoction enemas and oil enema; surgery and collyrium are not in it.",
              "Check each item against the words of the verse."),
        mcq("transfer", 5,
            "Invented line: क्षारो दन्तधावनार्थे युज्यते (क्षार = ash; दन्तधावन = tooth-cleaning). What does it say?",
            ("The ash is used for the purpose of cleaning teeth",
             "-अर्थे after a noun means 'for the purpose of', as in आलेपनार्थे; युज्यते is 'is used'."),
            [("The ash is used after cleaning teeth", "-अर्थे gives the purpose, not a later time."),
             ("The teeth are cleaned to make ash", "The ash is what is used; the cleaning is its purpose."),
             ("The ash is not to be used for cleaning teeth", "युज्यते says it is used; there is no negative.")],
            "X-अर्थे युज्यते = 'is used for the purpose of X', the pattern of verse 90.",
            "X-अर्थे = for the purpose of X.",
            teaches="A noun + -अर्थे names the purpose; you can read the purpose of any invented use from it."),
    ],
}

# ---------------------------------------------------------------- unit 91
AUTHORED["91"] = {
    "title": "अभ्यञ्जने भोजनार्थे",
    "question": "Which further uses of the salts does verse 91 add?",
    "rule": ("अभ्यञ्जने, भोजनार्थे, शिरसः विरेचने, शस्त्रकर्मणि, वर्त्यर्थम्, "
             "अञ्जन-उत्सादनेषु च = in inunction, in food, in evacuation of the "
             "head, in surgery, for suppositories, in collyrium and unction."),
    "limits": ("The printed चिरेचने is not a word; the sense requires विरेचने "
               "(see the note). The list is still a sentence in progress, "
               "finished in verse 92."),
    "explain_hi": ("लवणों के प्रयोगों की सूची आगे बढ़ती है: अभ्यंग (मालिश), भोजन के लिए, "
                   "सिर के विरेचन में, शस्त्रकर्म में, वर्ति बनाने के लिए, तथा अञ्जन और "
                   "उत्सादन में। छपे पाठ में ‘चिरेचने’ है, जो शब्द नहीं है; अर्थ के अनुसार "
                   "‘विरेचने’ चाहिए (पाठ-टिप्पणी देखें)। ‘शिरसः’ षष्ठी है: ‘सिर के’। "
                   "‘वर्त्यर्थम्’ = वर्ति + अर्थम्, यानी ‘वर्ति के प्रयोजन से’।"),
    "hook": "लवण के प्रयोग (२): अभ्यंग · भोजन · शिरोविरेचन · शस्त्रकर्म · वर्ति · अञ्जन · उत्सादन।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 91 goes on listing uses of the salts. Which of these is named in it?",
            ("In surgical procedures (शस्त्रकर्म)", "शस्त्रकर्मणि is in the second line."),
            [("In decoction enemas (निरूह)", "निरूह was named in verse 90, not here."),
             ("In oil enema (अनुवासन)", "अनुवासन was named in verse 90, not here."),
             ("In the eight urines", "The urines are not a use of the salts; they come after verse 92.")],
            "Verse 91 adds surgery, among other uses; decoction and oil enemas were in verse 90.",
            "Verse 91 adds new uses to the list begun in verse 90."),
        match(1, "Match each word of the verse to its meaning.",
              [["अभ्यञ्जने", "in inunction"], ["भोजनार्थे", "for use in food"],
               ["शस्त्रकर्मणि", "in surgery"], ["वर्त्यर्थम्", "for suppositories (wicks)"]],
              "These words give four of the uses in the verse.",
              "अभ्यञ्जने = in inunction; भोजनार्थे = for use in food; शस्त्रकर्मणि = in surgery; वर्त्यर्थम् = for suppositories."),
        fill(2, "The word for 'of the head' in the first line is ____ (type it in Devanagari).",
             ["शिरसः", "शिरसश्", "शिरसश्च"],
             "शिरसः is the genitive of शिरस्, joined to च as शिरसश्च.",
             "-अः on शिरस् is the genitive singular: 'of the head'. Together with the evacuation word it gives 'evacuation of the head'.",
             "शिरसः = of the head."),
        mcq("discriminate", 3, "Which is the right split of वर्त्यर्थम्?",
            ("वर्ति + अर्थम्",
             "इ before a different vowel becomes य्, so वर्ति + अर्थम् is written वर्त्यर्थम्."),
            [("वर्त्य + अर्थम्", "वर्त्य is not the word; the wick is वर्ति."),
             ("वर्ति + यर्थम्", "यर्थम् is not a word; the य् comes from the join."),
             ("वर्त + इ अर्थम्", "इ is not a word of its own here.")],
            "वर्त्यर्थम् = वर्ति ('suppository, wick') + अर्थम् ('for the purpose of').",
            "वर्त्यर्थम् = वर्ति + अर्थम्."),
        mcq("apply", 4,
            "The printed text reads शिरसश्च चिरेचने, but चिरेचने is not a word. What does the sense require?",
            ("विरेचने: 'in evacuation (of the head)'",
             "The note reads विरेचने, and शिरसः 'of the head' fits it."),
            [("चिरेचने as printed, a correct word", "The note marks चिरेचने as not a word."),
             ("भोजने: 'in food'", "Food was already named just before as भोजनार्थे."),
             ("वर्तने: 'in turning'", "Nothing in the verse or the note suggests it.")],
            "Printed चिरेचने is a slip for विरेचने; the line then reads 'and in evacuation of the head'.",
            "Where a printed word is not a word, read the form the sense and the note require."),
        mcq("transfer", 5,
            "Invented phrase: गुरुश्च शिष्यः. By the pattern of शिरसश्च, which gives गुरुश्च before sandhi?",
            ("गुरुः + च",
             "A visarga before च becomes श्, as in शिरसः + च → शिरसश्च."),
            [("गुरु + श्च", "श्च is not a word; the श् comes from the join."),
             ("गुरुश् + च", "श् does not stand as a word-ending on its own here."),
             ("गुरुः + श", "The second word is च, 'and'.")],
            "The same visarga + च → श्च rule gave भार्गवश्च्यवनः in verse 10.",
            "Visarga + च → श्च.",
            teaches="You can undo a श्च join: the first word ended in a visarga, the second is च."),
    ],
}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "अजीर्णानाहयोर्वाते",
    "question": "In which conditions are the salts used, and what does the verse turn to next?",
    "rule": ("The salts are used in indigestion, distension, Vāta disorders, "
             "gulma, colic and udara. Having described the salts, the speaker "
             "announces the eight urines: मूत्राण्यष्टौ निबोध मे."),
    "limits": ("The verse names no salt for any condition. वाते can be read "
               "'in Vāta (disorders)'. The word for 'salts' appears only "
               "in the second line; before it the list is carried over from "
               "verses 90-91."),
    "explain_hi": ("लवणों के प्रयोगों की सूची यहाँ समाप्त होती है: अजीर्ण, आनाह (पेट का "
                   "फूलना या रुकावट), वात रोग, गुल्म, शूल और उदर में। दूसरी पंक्ति में वक्ता कहता "
                   "है कि लवणों का वर्णन हो चुका (‘उक्तानि लवणानि’), और अब ‘मूत्राणि अष्टौ’, यानी "
                   "आठ मूत्र, मुझसे सुनो (‘निबोध मे’)। इस तरह यह श्लोक एक विषय को बन्द करके "
                   "दूसरा खोलता है।"),
    "hook": "लवण के प्रयोग (३) अजीर्ण–आनाह–वात–गुल्म–शूल–उदर; फिर: ‘आठ मूत्र सुनो’।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 92 closes the talk on salts. What do you expect it to announce next?",
            ("The eight urines", "The second line says 'learn from me the eight urines'."),
            [("A second list of salts", "The salts are said to have been described."),
             ("The roots and fruits", "These came earlier, not after the salts."),
             ("The names of the sages", "The sages were named at the start of the chapter.")],
            "मूत्राण्यष्टौ निबोध मे = 'learn from me the eight urines'.",
            "After the salts come the eight urines."),
        match(1, "Match each word of the verse to its meaning.",
              [["अजीर्ण", "indigestion"], ["आनाह", "distension"],
               ["गुल्मे", "in gulma (abdominal lump)"], ["शूले", "in colic"]],
              "These words name conditions in which the salts are used.",
              "अजीर्ण = indigestion; आनाह = distension; गुल्मे = in gulma; शूले = in colic."),
        fill(2, "The verse says 'learn' with the word ____ (type it in Devanagari).",
             ["निबोध"],
             "निबोध is a command: 'learn, listen'.",
             "निबोध is the second person singular imperative of नि-√बुध्: the speaker tells the hearer to learn. The doer 'you' is not written.",
             "निबोध = learn (a command to one hearer)."),
        mcq("discriminate", 3, "Which is the right split of तथोदरे?",
            ("तथा + उदरे",
             "आ + उ joins as ओ, so तथा + उदरे is written तथोदरे."),
            [("तथो + दरे", "दरे is not a word here."),
             ("तथ + उदरे", "The word is तथा, with a long आ."),
             ("तथा + ओदरे", "ओदरे is not a word; the ओ comes from the join.")],
            "तथोदरे = तथा ('and also') + उदरे ('in udara').",
            "तथोदरे = तथा + उदरे."),
        multi("apply", 4, "Which of these conditions are named in verse 92?",
              [("गुल्म", "Right: गुल्मे is in the first line."),
               ("शूल", "Right: शूले is in the first line."),
               ("उदर", "Right: उदरे ends the first line."),
               ("कुष्ठ", "Not in this verse; it is not named here."),
               ("अर्शस्", "Not in this verse; it is not named here.")],
              [0, 1, 2],
              "The first line names indigestion, distension, Vāta disorders, gulma, colic and udara.",
              "Check each condition against the first line."),
        mcq("transfer", 5,
            "By the pattern of मूत्राणि + अष्टौ → मूत्राण्यष्टौ, how is अग्नि + अत्र joined?",
            ("अग्न्यत्र", "इ before a different vowel becomes य्, so अग्नि + अत्र gives अग्न्यत्र."),
            [("अग्नात्र", "That would drop the इ without a य्; the pattern keeps य्."),
             ("अग्नेत्र", "ए comes from अ + इ, not from इ + अ."),
             ("अग्नि अत्र, with no join", "Within a line the two words are joined, as in मूत्राण्यष्टौ.")],
            "The rule that turned भूतेषु + अनुक्रोशम् into भूतेष्वनुक्रोशम् works the same for इ: इ + vowel → य् + vowel.",
            "इ + a different vowel → य् + that vowel.",
            teaches="Once you know इ → य् before a vowel, you can join or split any such pair."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "मुख्यानि यानि दिष्टानि",
    "question": "How does the list of principal urines begin, and on whose teaching does it rest?",
    "rule": ("सर्वाणि मुख्यानि यानि आत्रेयशासने दिष्टानि = all those taught as "
             "principal in Ātreya's teaching: sheep's, goat's, cow's urine "
             "and that of the buffalo. The list of eight continues in verse 94."),
    "limits": ("The verse gives four of the eight; the other four are in "
               "verse 94. The sentence has no verb here: it runs on into the "
               "next verse. The verse does not say why these are 'principal'."),
    "explain_hi": ("आठ मूत्रों की सूची यहाँ से शुरू होती है। पहली पंक्ति कहती है कि ये वे "
                   "मुख्य मूत्र हैं जो ‘आत्रेय के उपदेश में’ (आत्रेयशासने) बताए गए हैं। फिर चार "
                   "नाम आते हैं: भेड़, बकरी, गाय और भैंस का मूत्र। बाकी चार अगले श्लोक में हैं, "
                   "इसलिए वाक्य यहाँ पूरा नहीं होता। ‘दिष्टानि’ का अर्थ ‘बताए गए’ है और "
                   "‘मुख्यानि’ ‘प्रधान’।"),
    "hook": "आठ में पहले चार: भेड़ · बकरी · गाय · भैंस (शेष चार श्लोक ९४ में)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 93 begins naming the eight urines. Which animal's urine is named in it?",
            ("The goat", "अजामूत्रम् is in the second line."),
            [("The elephant", "The elephant comes in verse 94."),
             ("The camel", "The camel comes in verse 94."),
             ("The donkey", "The donkey comes in verse 94.")],
            "Verse 93 names the sheep, goat, cow and buffalo; the camel, elephant, horse and donkey come after.",
            "Verse 93 names four of the eight urines."),
        match(1, "Match each word of the verse to its meaning.",
              [["अविमूत्रम्", "sheep's urine"], ["अजामूत्रम्", "goat's urine"],
               ["गोमूत्रम्", "cow's urine"], ["माहिषम्", "of the buffalo"]],
              "These are the four animals of this verse.",
              "अविमूत्रम् = sheep's urine; अजामूत्रम् = goat's urine; गोमूत्रम् = cow's urine; माहिषम् = of the buffalo."),
        fill(2, "The word meaning 'principal' in the first line is ____ (type it in Devanagari).",
             ["मुख्यानि"],
             "मुख्यानि is the first word of the verse.",
             "-आनि marks a neuter plural: मुख्यानि goes with the urines (neuter, plural), the things that are 'principal'.",
             "मुख्यानि = principal (neuter plural)."),
        mcq("discriminate", 3, "Which is the right split of सर्वाण्यात्रेयशासने?",
            ("सर्वाणि + आत्रेयशासने",
             "इ before a different vowel becomes य्, so सर्वाणि + आत्रेयशासने is written सर्वाण्यात्रेयशासने."),
            [("सर्वाण्य + आत्रेयशासने", "सर्वाण्य is not a word."),
             ("सर्वाणि + यात्रेयशासने", "यात्रेयशासने is not a word; the य् comes from the join."),
             ("सर्वाण + आत्रेयशासने", "The word is सर्वाणि, the neuter plural of 'all'.")],
            "सर्वाण्यात्रेयशासने = सर्वाणि ('all') + आत्रेयशासने ('in Ātreya's teaching').",
            "सर्वाण्यात्रेयशासने = सर्वाणि + आत्रेयशासने."),
        mcq("apply", 4,
            "What does आत्रेयशासने tell you about where the list of principal urines comes from?",
            ("It is the list taught in Ātreya's teaching",
             "आत्रेय-शासने = 'in Ātreya's teaching'; the list rests on it."),
            [("It is taught in Indra's teaching", "Indra is not named in this verse."),
             ("It is a king's order to the physicians", "Nothing in the verse speaks of a king."),
             ("It is a list the speaker made up himself", "The verse says they are taught in Ātreya's teaching.")],
            "आत्रेयशासने is a locative: 'in the teaching of Ātreya'.",
            "आत्रेयशासने = in Ātreya's teaching."),
        mcq("transfer", 5,
            "Invented: भरद्वाजशासने. By the pattern of आत्रेयशासने, what does it mean?",
            ("In Bharadvāja's teaching",
             "A name + शासने = 'in the teaching of' that person."),
            [("From Bharadvāja's teaching", "-ने (locative) says 'in', not 'from'."),
             ("Bharadvāja is taught", "The name is the teacher, not the one taught."),
             ("Bharadvāja and the teaching", "The two are joined as one compound, not listed as a pair.")],
            "The compound name + शासने follows the same pattern.",
            "X-शासने = in X's teaching.",
            teaches="A teacher's name + शासने = 'in the teaching of that teacher'; the same pattern works with any name."),
    ],
}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "हस्तिमूत्रमथोष्ट्रस्य",
    "question": "Which four urines complete the eight, and what properties are stated for the urines?",
    "rule": ("हस्तिमूत्रम्, उष्ट्रस्य, हयस्य, खरस्य = elephant's, camel's, "
             "horse's and donkey's urine complete the eight. Urine is hot, "
             "sharp, not dry, pungent and has a salty taste."),
    "limits": ("The reading अरूक्षम् ('not dry') rests on the avagraha in "
               "अथो ऽरूक्षम्; without it the sense would be 'and dry'. The edition "
               "follows the avagraha. The properties are stated once for all urines."),
    "explain_hi": ("पिछले श्लोक में चार मूत्र थे; यहाँ बाकी चार आते हैं: हाथी, ऊँट, घोड़ा और गधा। "
                   "इस तरह आठ पूरे होते हैं। दूसरी पंक्ति सब मूत्रों के सामान्य गुण बताती है: उष्ण, तीक्ष्ण, "
                   "अरूक्ष (रूखा नहीं), कटु और लवण से युक्त। ये गुण एक बार, एकवचन में कहे गए हैं और सब "
                   "मूत्रों पर लागू माने गए हैं। ‘अरूक्षम्’ पढ़ने का आधार अवग्रह (ऽ) है; पाठ-टिप्पणी देखें।"),
    "hook": "बाकी चार: हाथी · ऊँट · घोड़ा · गधा। सामान्य गुण: उष्ण, तीक्ष्ण, अरूक्ष, कटु, लवणान्वित।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 93 named sheep, goat, cow and buffalo. Which animal's urine is named in verse 94?",
            ("The camel", "उष्ट्रस्य, 'of the camel', is in the first line."),
            [("The sheep", "The sheep was named in verse 93."),
             ("The goat", "The goat was named in verse 93."),
             ("The buffalo", "The buffalo was named in verse 93.")],
            "Verse 94 names the elephant, camel, horse and donkey.",
            "Verse 94 names the other four of the eight urines."),
        match(1, "Match each word of the verse to its meaning.",
              [["हस्ति", "elephant"], ["उष्ट्र", "camel"], ["हय", "horse"],
               ["खर", "donkey"]],
              "These are the four animals of this verse.",
              "हस्ति = elephant; उष्ट्र = camel; हय = horse; खर = donkey."),
        fill(2, "The word meaning 'pungent' in the second line is ____ (type it in Devanagari).",
             ["कटुकम्", "कटुकं"],
             "कटुकम् is one of the properties of the urines.",
             "The properties in line 2 end in -म्: neuter singular, agreeing with मूत्रम् understood. One word of the list, कटुकम्, is 'pungent'.",
             "कटुकम् = pungent."),
        mcq("discriminate", 3, "Which gives the words of हस्तिमूत्रमथोष्ट्रस्य before sandhi?",
            ("हस्तिमूत्रम् + अथ + उष्ट्रस्य",
             "म् joins the following अ, and अ + उ joins as ओ, so the three words give हस्तिमूत्रमथोष्ट्रस्य."),
            [("हस्तिमूत्र + मथो + ष्ट्रस्य", "मथो and ष्ट्रस्य are not words."),
             ("हस्तिमूत्रम् + अथो + उष्ट्रस्य", "The second word is अथ; the ओ comes from the join with उ."),
             ("हस्तिमूत्रम् + अथ + औष्ट्रस्य", "The camel is उष्ट्र, with a short उ, not औ.")],
            "हस्तिमूत्रमथोष्ट्रस्य = हस्तिमूत्रम् ('elephant's urine') + अथ ('and') + उष्ट्रस्य ('of the camel').",
            "हस्तिमूत्रमथोष्ट्रस्य = हस्तिमूत्रम् + अथ + उष्ट्रस्य."),
        multi("apply", 4, "Which of these properties does the second line state for the urines?",
              [("उष्ण (hot)", "Right: उष्णम् opens the line."),
               ("तीक्ष्ण (sharp)", "Right: तीक्ष्णम् is in the line."),
               ("कटुक (pungent)", "Right: कटुकम् is in the line."),
               ("लवणान्वित (having a salty taste)", "Right: लवणान्वितम् ends the line."),
               ("शीत (cold)", "Not in the line; it is the opposite of उष्ण.")],
              [0, 1, 2, 3],
              "The line gives hot, sharp, pungent and salty (and 'not dry' on the edition's reading).",
              "Check each property against the second line."),
        mcq("transfer", 5,
            "Invented: a teacher lists four oils, then adds उष्णं तीक्ष्णम्, neuter singular, with 'oil' understood. By the pattern of verse 94, what does he mean?",
            ("Every oil listed is hot and sharp",
             "In verse 94 the properties agree with an understood singular noun and apply to every urine listed."),
            [("Only the last oil is hot and sharp", "In verse 94 the properties are not limited to the last animal."),
             ("Only the first oil is hot and sharp", "They are not limited to the first item either."),
             ("The properties belong to none of the oils", "Properties after a list describe the items listed.")],
            "In verse 94 the neuter singular properties agree with an understood noun and describe all items of the list.",
            "Properties after a list, with the noun understood = shared by all.",
            teaches="Properties agreeing with an understood noun, placed after a list, describe every item of the list."),
    ],
}

# ---------------------------------------------------------------- unit 95
AUTHORED["95"] = {
    "title": "मूत्रमुत्सादने युक्तम्",
    "question": "In which procedures is urine said to be suitable?",
    "rule": ("मूत्रम् … युक्तम् = urine is suitable in unction, in pastes, in "
             "decoction enema (āsthāpana) and in purgation. The word युक्तम् "
             "is repeated for each use."),
    "limits": ("The verse does not say which urine suits which procedure. "
               "युक्त is rendered 'suitable, applied'. The list goes on in "
               "verse 96."),
    "explain_hi": ("अब मूत्रों के प्रयोग गिनाए जाते हैं। मूत्र ‘युक्त’ यानी उपयुक्त है "
                   "उत्सादन (उबटन जैसे मलने) में, आलेपों में, आस्थापन (काढ़े की बस्ति) में और "
                   "विरेचन में। ‘युक्तम्’ हर प्रयोग के साथ दोहराया गया है, इसलिए पढ़ते समय हर "
                   "बार ‘मूत्र उपयुक्त है’ जोड़ लें। सप्तमी (-ने, -षु) बताती है कि उपयोग किसमें है।"),
    "hook": "मूत्र युक्त है: उत्सादन · आलेप · आस्थापन · विरेचन (युक्तम् चार बार)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which of these is named in verse 95 as a use of urine?",
            ("Pastes (आलेप)", "आलेपनेषु is in the first line."),
            [("Surgery (शस्त्रकर्म)", "Surgery is not named in this verse."),
             ("Collyrium (अञ्जन)", "Collyrium is not named in this verse."),
             ("Food (भोजन)", "Food is not named in this verse.")],
            "Verse 95 names unction, pastes, decoction enema and purgation.",
            "Verse 95 lists the uses of urine."),
        match(1, "Match each word of the verse to its meaning.",
              [["उत्सादने", "in unction"], ["आलेपनेषु", "in pastes"],
               ["आस्थापने", "in decoction enema"], ["विरेचने", "in purgation"]],
              "These words name the four uses of the verse.",
              "उत्सादने = in unction; आलेपनेषु = in pastes; आस्थापने = in decoction enema; विरेचने = in purgation."),
        fill(2, "The word meaning 'suitable' is repeated in the verse: ____ (type it in Devanagari).",
             ["युक्तम्", "युक्तं"],
             "युक्तम् comes with each of the four uses.",
             "युक्तम् is a past participle of √युज्, neuter singular, agreeing with मूत्रम्: 'urine (is) suitable'.",
             "युक्तम् = suitable."),
        mcq("discriminate", 3, "Which is the right split of युक्तमास्थापने?",
            ("युक्तम् + आस्थापने",
             "म् joins the following आ, so युक्तम् + आस्थापने is written युक्तमास्थापने."),
            [("युक्त + मास्थापने", "मास्थापने is not a word."),
             ("युक्तमा + स्थापने", "स्थापने alone is not the word here."),
             ("युक्तम् + अस्थापने", "The word is आस्थापने, with a long आ.")],
            "युक्तमास्थापने = युक्तम् ('suitable') + आस्थापने ('in decoction enema').",
            "युक्तमास्थापने = युक्तम् + आस्थापने."),
        mcq("apply", 4,
            "In verse 95, which word names the thing that is 'suitable'?",
            ("मूत्रम् (urine)", "मूत्रम् is the subject; युक्तम् describes it."),
            [("उत्सादने (in unction)", "It is a locative: the place of use, not the thing used."),
             ("आलेपनेषु (in pastes)", "It is a locative: the place of use, not the thing used."),
             ("विरेचने (in purgation)", "It is a locative: the place of use, not the thing used.")],
            "मूत्रम् is the subject; the four locatives say where it is suitable.",
            "Subject = मूत्रम्; locatives = uses."),
        mcq("transfer", 5,
            "Invented line: घृतं पाने युक्तं युक्तं च सेचने (घृत = ghee; पान = drinking; सेचन = sprinkling). What does it say?",
            ("Ghee is suitable for drinking and for sprinkling",
             "As in verse 95: the thing is named, then युक्तम् with each locative use."),
            [("Drinking and sprinkling are suitable for making ghee", "Ghee is the thing that is suitable."),
             ("Ghee is suitable for drinking but not for sprinkling", "च joins a second युक्तम्; nothing says 'not'."),
             ("Ghee is drunk and sprinkled by the same person", "The line speaks of suitability, not of a person.")],
            "The pattern of verse 95 carries to any thing and its uses.",
            "Thing + युक्तम् + locative = suitable for that use.",
            teaches="A repeated युक्तम् with locatives lists the uses of the one thing named."),
    ],
}

# ---------------------------------------------------------------- unit 96
AUTHORED["96"] = {
    "title": "स्वेदेष्वपि च तद्युक्तम्",
    "question": "Which further procedures and conditions is the urine said to suit?",
    "rule": ("तत् … युक्तम् = it (the urine) is suitable also in sudation, in "
             "distension and in antidotes, and in abdominal diseases, in "
             "piles, and for patients with gulma, kuṣṭha and kilāsa."),
    "limits": ("The verse does not say how the urine is used in any of these. "
               "तद् is read as the urine of the previous verse. "
               "गुल्मि-कुष्ठि-किलासिषु names persons, not diseases."),
    "explain_hi": ("मूत्र के प्रयोगों की सूची चलती है: स्वेदन में भी, आनाह में और अगद (विष के "
                   "उपचार) में; फिर उदर रोगों में, अर्श में, और गुल्म, कुष्ठ तथा किलास से "
                   "पीड़ित लोगों में। ‘तद्’ का अर्थ ‘वह’, यानी पिछले श्लोक का मूत्र। अन्तिम "
                   "शब्द में ‘-इन्’ वाले रूप (गुल्मी, कुष्ठी, किलासी) ‘उस रोग वाला’ अर्थ देते हैं, "
                   "इसलिए सप्तमी बहुवचन का अर्थ ‘उन रोगियों में’ है।"),
    "hook": "मूत्र ‘तद्’ = वह: स्वेद · आनाह · अगद · उदर · अर्श · गुल्मी–कुष्ठी–किलासी (रोग वाले)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which disease is named in verse 96?",
            ("Kuṣṭha (skin disease)", "कुष्ठ is part of the last compound of the verse."),
            [("Pāṇḍu (anaemia)", "Pāṇḍu comes in verse 98."),
             ("Jvara (fever)", "Fever is not named in this verse."),
             ("Prameha (urinary disorder)", "Prameha is not named in this verse.")],
            "Verse 96 ends with the patients of gulma, kuṣṭha and kilāsa.",
            "Verse 96 names kuṣṭha among its conditions."),
        match(1, "Match each word of the verse to its meaning.",
              [["स्वेदेषु", "in sudation procedures"], ["आनाहेषु", "in distensions"],
               ["अगदेषु", "in antidotes"], ["अर्शःसु", "in piles"]],
              "These words name four of the uses in the verse.",
              "स्वेदेषु = in sudation; आनाहेषु = in distensions; अगदेषु = in antidotes; अर्शःसु = in piles."),
        fill(2, "The word for 'it' (the urine) in the first line is ____ (type it in Devanagari).",
             ["तत्", "तद्"],
             "तद् joins युक्तम् as तद्युक्तम्.",
             "तद् / तत् is the neuter 'it', 'that'. Here it points back to the urine of the last verse; तत् + युक्तम् is written तद्युक्तम्.",
             "तत् = it, that."),
        mcq("discriminate", 3, "Which is the right split of स्वेदेष्वपि?",
            ("स्वेदेषु + अपि",
             "उ before a different vowel becomes व्, so स्वेदेषु + अपि is written स्वेदेष्वपि."),
            [("स्वेदेष्व + पि", "पि is not a word."),
             ("स्वेदे + ष्वपि", "ष्वपि is not a word."),
             ("स्वेदेषु + वपि", "वपि is not a word; the व् comes from the join.")],
            "स्वेदेष्वपि = स्वेदेषु ('in sudation') + अपि ('also').",
            "स्वेदेष्वपि = स्वेदेषु + अपि."),
        multi("apply", 4, "Which of these are named in verse 96 as conditions or uses for the urine?",
              [("आनाह (distension)", "Right: आनाहेषु is in the first line."),
               ("उदर (abdominal diseases)", "Right: उदरेषु begins the second line."),
               ("अर्शस् (piles)", "Right: अर्शःसु is in the second line."),
               ("पाण्डु (anaemia)", "Not in this verse; it is not named here."),
               ("शूल (colic)", "Not in this verse; it is not named here.")],
              [0, 1, 2],
              "Verse 96 names sudation, distension, antidotes, abdominal diseases, piles, and gulma, kuṣṭha and kilāsa patients.",
              "Check each item against the words of the verse."),
        mcq("transfer", 5,
            "If कास means 'cough', what does कासिषु mean, by the pattern of गुल्मिकुष्ठिकिलासिषु?",
            ("Among those who suffer from cough",
             "-इन् names the one who has the thing, and -षु gives 'among, in'."),
            [("In coughs, the diseases themselves", "A disease alone would be कासेषु; -इ names the person."),
             ("For the sake of cough", "-अर्थे would give the purpose; this ending does not."),
             ("From cough", "'From' would need an ablative ending.")],
            "In गुल्मि- the person is meant ('one with gulma'); the same ending on कास gives 'one with cough'.",
            "X-इन् = one who has X; plural locative = among such persons.",
            teaches="An -इन् noun names the one who has the thing, so a locative plural reads 'among those who have it'."),
    ],
}

# ---------------------------------------------------------------- unit 97
AUTHORED["97"] = {
    "title": "तद्युक्तमुपनाहेषु",
    "question": "What are the last uses, and which three properties is the urine declared to have?",
    "rule": ("तत् … युक्तम् = it is suitable in poultices and in affusion; it is "
             "declared stimulating to digestion, destroying poison and "
             "destroying worms."),
    "limits": ("The verse does not name who declares these properties "
               "(उपदिश्यते is passive). It does not say which urine has which "
               "property."),
    "explain_hi": ("उपयोगों की सूची के अन्तिम दो नाम: उपनाह (पुल्टिस की तरह बाँधना) और परिषेक "
                   "(धार डालना)। फिर तीन गुण: दीपनीय (अग्नि को जगाने वाला), विषघ्न (विष का नाश "
                   "करने वाला) और क्रिमिघ्न (कृमियों का नाश करने वाला)। ‘-घ्न’ अन्त में हो तो अर्थ "
                   "‘नाश करने वाला’ होता है। ‘उपदिश्यते’ कर्मवाच्य है, यानी ‘बताया जाता है’, "
                   "कर्ता का नाम नहीं दिया गया।"),
    "hook": "अन्तिम उपयोग: उपनाह · परिषेक। तीन गुण: दीपनीय · विषघ्न · क्रिमिघ्न।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which of these is said of the urine in verse 97?",
            ("It destroys worms", "क्रिमिघ्नम् means 'destroying worms'."),
            [("It breeds worms", "The verse says the opposite."),
             ("It is cooling", "Verse 94 called urines hot; nothing here changes that."),
             ("It increases poison", "विषघ्नम् says it destroys poison.")],
            "Verse 97 declares the urine stimulating to digestion, poison-destroying and worm-destroying.",
            "Verse 97 gives three properties: dīpanīya, viṣaghna, krimighna."),
        match(1, "Match each word of the verse to its meaning.",
              [["उपनाहेषु", "in poultices"], ["परिषेके", "in affusion (pouring)"],
               ["विषघ्नम्", "destroying poison"], ["क्रिमिघ्नम्", "destroying worms"]],
              "These words give the last uses and two of the properties.",
              "उपनाहेषु = in poultices; परिषेके = in affusion; विषघ्नम् = destroying poison; क्रिमिघ्नम् = destroying worms."),
        fill(2, "The verb meaning 'is declared' in the verse is ____ (type it in Devanagari).",
             ["उपदिश्यते", "चोपदिश्यते"],
             "उपदिश्यते is the last word of the verse (with च before it).",
             "उपदिश्यते is a passive: 'is declared, is taught'. The doer is not named.",
             "उपदिश्यते = is declared."),
        mcq("discriminate", 3, "Which is the right split of चोपदिश्यते?",
            ("च + उपदिश्यते",
             "अ + उ joins as ओ, so च + उपदिश्यते is written चोपदिश्यते."),
            [("चो + पदिश्यते", "पदिश्यते is not the verb here."),
             ("च + अपदिश्यते", "The verb begins with उ, not अ."),
             ("चा + उपदिश्यते", "The first word is च, with a short अ.")],
            "चोपदिश्यते = च ('and') + उपदिश्यते ('is declared').",
            "चोपदिश्यते = च + उपदिश्यते."),
        multi("apply", 4, "Which of these are named in verse 97?",
              [("उपनाह (poultices)", "Right: उपनाहेषु is in the first line."),
               ("परिषेक (affusion)", "Right: परिषेके is in the first line."),
               ("दीपनीय (stimulating digestion)", "Right: दीपनीयम् opens the second line."),
               ("शस्त्रकर्म (surgery)", "Not in this verse."),
               ("अनुवासन (oil enema)", "Not in this verse.")],
              [0, 1, 2],
              "The verse names poultices, affusion and the three properties; surgery and oil enema are not in it.",
              "Check each item against the words of the verse."),
        mcq("transfer", 5,
            "Invented: शूलघ्नम्, with शूल = colic. By the pattern of विषघ्नम्, what does it mean?",
            ("Destroying colic",
             "-घ्न at the end of a compound means 'destroying' what the first part names."),
            [("Causing colic", "-घ्न is the opposite of causing."),
             ("Like colic", "'Like' would need a different ending."),
             ("Fond of colic", "The ending does not mean 'fond of'.")],
            "विष-घ्नम् is 'poison-destroying'; शूल-घ्नम् is 'colic-destroying'.",
            "X-घ्नम् = destroying X.",
            teaches="-घ्न at the end of a compound means 'destroying'; you can read विषघ्न, क्रिमिघ्न, and any new X-घ्न."),
    ],
}

# ---------------------------------------------------------------- unit 98
AUTHORED["98"] = {
    "title": "पाण्डुरोगोपसृष्टानाम्",
    "question": "For whom is urine the best relief, and what does it do to Kapha and Vāta when drunk?",
    "rule": ("पाण्डुरोग-उपसृष्टानाम् उत्तमं शर्म = the best relief for those "
             "afflicted with pāṇḍu; drunk, it would pacify Kapha and make "
             "Vāta move in its proper direction. The effect on Pitta is in "
             "verse 99."),
    "limits": ("The printed पाण्डुरोगोपसृष्तानाम् has a misspelt ष्ट "
               "(see the note). शमयेत् and अनुलोमयेत् are optative forms, a "
               "general statement of effect. The sentence runs on into "
               "verse 99."),
    "explain_hi": ("इस श्लोक में मूत्र को पाण्डु रोग से पीड़ितों के लिए ‘उत्तम शर्म’ यानी सबसे "
                   "अच्छा सुखकारक उपाय कहा गया है। फिर पीने पर इसके असर बताए जाते हैं: "
                   "श्लेष्मा (कफ) को शान्त करे और मारुत (वात) को अनुलोम करे, यानी उसे उसकी "
                   "स्वाभाविक दिशा में चलाए। दोनों क्रियाएँ ‘-एत्’ में हैं (शमयेत्, अनुलोमयेत्), जो "
                   "सामान्य कथन का रूप है। पित्त पर असर अगले श्लोक में है, इसलिए वाक्य वहीं पूरा होता है।"),
    "hook": "पाण्डु वालों के लिए उत्तम; पीने पर: कफ शान्त, वात अनुलोम (पित्त → श्लोक ९९)।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "For those afflicted with which disease does verse 98 call urine the best relief?",
            ("Pāṇḍu (anaemia)", "पाण्डुरोग-उपसृष्टानाम् names those afflicted with pāṇḍu."),
            [("Kuṣṭha (skin disease)", "Kuṣṭha was in verse 96, not in this phrase."),
             ("Gulma (abdominal lump)", "Gulma was in verses 92 and 96, not in this phrase."),
             ("Kilāsa (white patches)", "Kilāsa was in verse 96, not in this phrase.")],
            "The first line names pāṇḍu-roga as the disease for which it is the best relief.",
            "Verse 98: best relief for those afflicted with pāṇḍu."),
        match(1, "Match each word of the verse to its meaning.",
              [["उत्तमम्", "the best"], ["शर्म", "relief"],
               ["श्लेष्माणम्", "Kapha"], ["मारुतम्", "Vāta (wind)"]],
              "These words carry the praise and the two effects of the verse.",
              "उत्तमम् = the best; शर्म = relief; श्लेष्माणम् = Kapha; मारुतम् = Vāta."),
        fill(2, "The word meaning 'when drunk' in the second line is ____ (type it in Devanagari).",
             ["पीतम्", "पीतं"],
             "पीतम् comes from √पा, 'to drink'.",
             "पीतम् is a past participle used for the condition: 'when it has been drunk'. It qualifies the urine.",
             "पीतम् = when drunk."),
        mcq("discriminate", 3, "Which is the right split of चानुलोमयेत्?",
            ("च + अनुलोमयेत्",
             "अ + अ joins as आ, so च + अनुलोमयेत् is written चानुलोमयेत्."),
            [("चा + नुलोमयेत्", "नुलोमयेत् is not a word."),
             ("च + आनुलोमयेत्", "The verb begins with a short अ: अनुलोमयेत्."),
             ("चान + उलोमयेत्", "उलोमयेत् is not a word.")],
            "चानुलोमयेत् = च ('and') + अनुलोमयेत् ('would make move in its proper direction').",
            "चानुलोमयेत् = च + अनुलोमयेत्."),
        mcq("apply", 4,
            "According to verse 98, what does the urine do to Kapha and Vāta when drunk?",
            ("Pacifies Kapha and makes Vāta move in its proper direction",
             "शमयेत् goes with श्लेष्माणम् and अनुलोमयेत् with मारुतम्."),
            [("Increases Kapha and stops Vāta", "Both verbs say the opposite."),
             ("Pacifies Vāta and makes Kapha move", "The two verbs go with the other substances."),
             ("Pacifies both and moves neither", "अनुलोमयेत् is said of Vāta.")],
            "The two verbs of the second line each take their own object.",
            "शमयेत् → Kapha; अनुलोमयेत् → Vāta."),
        mcq("transfer", 5,
            "Invented: उष्णं जलं पीतं कफं नाशयेत् (नाशयेत् = would destroy). As in verse 98, how is पीतम् used?",
            ("As 'when drunk', the condition under which the water acts",
             "Like पीतं शमयेत् in verse 98: the participle gives the condition."),
            [("As the doer who drinks", "पीतम् describes the water, not a drinker."),
             ("As a place, 'in the drink'", "It has no locative ending."),
             ("As a command, 'drink!'", "A command would be a verb form, not a participle.")],
            "पीतम् is a participle describing the substance at the time it acts.",
            "पीतम् = when drunk (a condition on the substance).",
            teaches="A past participle can give the condition under which a substance acts."),
    ],
}

# ---------------------------------------------------------------- unit 99
AUTHORED["99"] = {
    "title": "कर्षेत् पित्तमधोभागम्",
    "question": "What does the urine do to Pitta, and what shift of treatment does the verse announce?",
    "rule": ("कर्षेत् पित्तम् अधोभागम् = it would draw Pitta downward. इति … "
             "गुणसंग्रहः सामान्येन उक्तः = the summary of properties has been "
             "stated in general terms; पृथक्त्वेन प्रवक्ष्यते = it will be stated "
             "separately."),
    "limits": ("अस्मिन् may refer to the urine or to the section; the verse does "
               "not decide. The verse promises a separate account but does not "
               "itself give it; the account begins in the next verse."),
    "explain_hi": ("पिछले श्लोक का वाक्य पूरा होता है: मूत्र पित्त को नीचे की ओर खींचता है। "
                   "फिर वक्ता कहता है ‘इति’ यानी ‘इस प्रकार’ गुणों का संग्रह मैंने ‘सामान्य रूप "
                   "से’ (सामान्येन) कह दिया; अब ‘अलग-अलग’ (पृथक्त्वेन) कहा जाएगा। यहाँ "
                   "सामान्य और पृथक् का जोड़ा याद रखें: पहले सबके साझा गुण, फिर एक-एक मूत्र के गुण। "
                   "‘अस्मिन्’ मूत्र के लिए भी पढ़ा जा सकता है और इस प्रकरण के लिए भी।"),
    "hook": "पित्त नीचे खिंचे। सामान्य रूप से कहा (अब तक) ↔ अलग-अलग कहा जाएगा (आगे)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 99 say the urine does to Pitta?",
            ("Draws it downward", "कर्षेत् पित्तम् अधोभागम् = it would draw Pitta downward."),
            [("Draws it upward", "अधोभागम् means downward."),
             ("Increases it", "The verb is कर्षेत्, 'would draw'."),
             ("Leaves it unchanged", "The verb says it draws Pitta.")],
            "The urine draws Pitta downward (अधोभाग).",
            "कर्षेत् पित्तम् अधोभागम् = draws Pitta downward."),
        match(1, "Match each word of the verse to its meaning.",
              [["कर्षेत्", "it would draw"], ["अधोभागम्", "downward"],
               ["सामान्येन", "in general terms"], ["पृथक्त्वेन", "separately"]],
              "These words carry the effect on Pitta and the change of plan.",
              "कर्षेत् = it would draw; अधोभागम् = downward; सामान्येन = in general terms; पृथक्त्वेन = separately."),
        fill(2, "The word meaning 'separately' in the second line is ____ (type it in Devanagari).",
             ["पृथक्त्वेन"],
             "पृथक्त्वेन is the counterpart of सामान्येन.",
             "-एन marks the instrumental, here used as an adverb: 'in a separate way', 'separately'.",
             "पृथक्त्वेन = separately."),
        mcq("discriminate", 3, "Which gives the words of मयोक्तस्तु before sandhi?",
            ("मया + उक्तः + तु",
             "आ + उ joins as ओ, and a visarga before त becomes स्, so मया + उक्तः + तु gives मयोक्तस्तु."),
            [("मयो + क्तः + तु", "क्तः is not a word."),
             ("मया + उक्त + स्तु", "स्तु is not a word; the स् comes from the visarga."),
             ("मय + उक्तः + तु", "मय is not a word here; 'by me' is मया.")],
            "मयोक्तस्तु = मया ('by me') + उक्तः ('stated') + तु ('but').",
            "मयोक्तस्तु = मया + उक्तः + तु."),
        mcq("apply", 4,
            "The speaker says the summary was stated 'in general terms'. What does the verse say will follow?",
            ("An account of each urine separately",
             "पृथक्त्वेन प्रवक्ष्यते = 'it will be stated separately'."),
            [("The same summary again", "The verse promises something different, a separate account."),
             ("The list of the five salts", "The salts were finished in verse 92."),
             ("Nothing more on the urines", "The verse promises a further account.")],
            "After the general summary, a separate account is promised.",
            "सामान्येन → पृथक्त्वेन: general first, then separately."),
        mcq("transfer", 5,
            "A teacher says: सामान्येन फलानि उक्तानि, पृथक्त्वेन प्रवक्ष्ये (प्रवक्ष्ये = I shall tell). What will he do next?",
            ("Describe each fruit one by one",
             "As in verse 99, 'separately' follows a general statement."),
            [("Repeat the general statement", "पृथक्त्वेन promises the opposite of 'in general'."),
             ("Describe only one fruit", "Separately means each in its own turn."),
             ("Stop speaking about fruits", "He says he will tell more.")],
            "The pair सामान्येन / पृथक्त्वेन works the same for any subject.",
            "सामान्येन then पृथक्त्वेन = general first, each one next.",
            teaches="Once a speaker says 'in general terms', the word पृथक्त्वेन signals a one-by-one account to come."),
    ],
}

NOTES_HI = {
    "90": "संधि: ‘अधोभागोर्ध्वभागेषु’ में अधोभाग + ऊर्ध्वभागेषु, अ + ऊ → ओ। ‘निरूहेष्वनुवासने’ में निरूहेषु + अनुवासने, उ → व् (स्वर से पहले)। टिप्पणी: अधोभाग/ऊर्ध्वभाग का अर्थ ‘नीचे/ऊपर का भाग’ है; यहाँ उन मार्गों से शोधन (विरेचन, वमन) लिया गया है। पाठभेद या पाठ-दोष नहीं दिया गया।",
    "91": "पाठ-दोष: छपा ‘चिरेचने’ शब्द नहीं है; अर्थ के अनुसार ‘विरेचने’ चाहिए (‘शिरसश्च विरेचने’ = सिर के विरेचन में)। यह स्रोत में c/v की मुद्रण-भूल लगती है। संधि: शिरसः + च → शिरसश्च (विसर्ग → श्); वर्ति + अर्थम् → वर्त्यर्थम् (इ → य्); अञ्जनोत्सादनेषु = अञ्जन + उत्सादनेषु (अ + उ → ओ)। ‘वर्त्यर्थम्’ को क्रियाविशेषण की तरह (‘वर्ति के लिए’) पढ़ा गया है।",
    "92": "स्रोत में एक अतिरिक्त ‘&’ चिह्न था, जिसे हटा दिया गया; शब्द-विभाजन ‘अजीर्णानाहयोर् वाते’ ठीक है। ‘वाते’ को ‘वात रोगों में’ पढ़ा जा सकता है। ‘अजीर्णानाहयोः’ द्विवचन सप्तमी है (अजीर्ण + आनाह), उसी की संधि ‘अजीर्णानाहयोर्’ है। ‘लवणान्यूर्ध्वम्’ = लवणानि + ऊर्ध्वम् (इ → य्)।",
    "93": "‘सर्वाण्यात्रेयशासने’ = सर्वाणि + आत्रेयशासने (इ → य्)। इस श्लोक में क्रिया नहीं है; वाक्य श्लोक ९४ में चलता है। ‘माहिषं च यत्’ में ‘यत्’ का अन्वय स्पष्ट नहीं है; यहाँ ‘जो (भैंस का मूत्र) है’ के रूप में पढ़ा गया है। ‘आत्रेय’ वही व्यक्ति है या नहीं, श्लोक नहीं बताता।",
    "94": "विश्वास: मध्यम। ‘अथो ऽरूक्षम्’ में अवग्रह के साथ ‘अरूक्षम्’ (रूखा नहीं) बनता है; अवग्रह के बिना ‘अथो रूक्षम्’ (और रूखा) पढ़ा जाता, जिसका अर्थ उलटा होता। छन्द दोनों में वही रहता है; पाठ अवग्रह वाला रखा गया है। ‘हस्तिमूत्रमथोष्ट्रस्य’ में हस्तिमूत्रम् + अथ + उष्ट्रस्य।",
    "95": "‘युक्तम्’ चार बार आया है; इसे ‘उपयुक्त/प्रयुक्त’ दोनों अर्थों में पढ़ा जा सकता है, यहाँ ‘उपयुक्त’ लिया गया। संधि: ‘मूत्रमुत्सादने’ = मूत्रम् + उत्सादने; ‘युक्तमालेपनेषु’ = युक्तम् + आलेपनेषु; ‘चापि’ = च + अपि (अ + अ → आ)।",
    "96": "‘तद्युक्तम्’ में तत् + युक्तम् (त् → द्, घोष य से पहले)। ‘स्वेदेष्वपि’ = स्वेदेषु + अपि (उ → व्)। ‘गुल्मिकुष्ठिकिलासिषु’ एक द्वन्द्व है और रोगी व्यक्तियों के लिए है। ‘आनाहेषु’ रूप में बहुवचन है। पाठभेद या पाठ-दोष नहीं दिया गया।",
    "97": "‘तद्युक्तमुपनाहेषु’ = तत् + युक्तम् + उपनाहेषु। ‘चोपदिश्यते’ = च + उपदिश्यते (अ + उ → ओ)। ‘विषघ्नम्’ और ‘क्रिमिघ्नम्’ उपपद तत्पुरुष हैं (घ्न = नाश करने वाला)। ‘उपदिश्यते’ कर्मवाच्य है, कर्ता नाम से नहीं आता।",
    "98": "पाठ-दोष: छपा ‘पाण्डुरोगोपसृष्तानाम्’ में ‘ष्त’ है; सही रूप ‘उपसृष्टानाम्’ (टवर्ग ष्ट) होना चाहिए, यह प्रविष्टि की भूल लगती है। ‘पाण्डुरोगोपसृष्टानाम्’ = पाण्डुरोग + उपसृष्टानाम् (अ + उ → ओ)। ‘शर्म’ का मूल अर्थ ‘आश्रय, सुख’ है। ‘अनुलोमयेत्’ वात को उसकी स्वाभाविक अनुकूल दिशा में चलाने का भाव है।",
    "99": "‘अस्मिन्’ मूत्र के लिए भी पढ़ा जा सकता है और ‘इस प्रकरण’ के लिए भी; श्लोक तय नहीं करता। ‘प्रवक्ष्यते’ रूप में आत्मनेपद भविष्यत् है, पर अर्थ कर्मवाच्य (‘कहा जाएगा’) है। संधि: ‘पित्तमधोभागमित्यस्मिन्’ में पित्तम् + अधोभागम् + इति + अस्मिन्; ‘मयोक्तस्तु’ = मया + उक्तः + तु।",
}

AIDS = {
    "90": {
        "chain": {"steps": ["आलेपनार्थे: लेप के लिए",
                            "स्नेहस्वेदविधौ: स्नेहन–स्वेदन में",
                            "अधोभाग–ऊर्ध्वभाग: नीचे और ऊपर के शोधन",
                            "निरूहेषु: निरूह बस्ति में",
                            "अनुवासने: अनुवासन बस्ति में"]},
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["आलेपनार्थे", "युज्यन्ते", "स्नेहस्वेदविधौ", "तथा"]},
            {"label": "दूसरी पंक्ति",
             "items": ["अधोभागोर्ध्वभागेषु", "निरूहेषु", "अनुवासने"]}]},
        "sandhi": "अ + ऊ → ओ: अधोभाग + ऊर्ध्वभागेषु → अधोभागोर्ध्वभागेषु · उ + अ → व् + अ: निरूहेषु + अनुवासने → निरूहेष्वनुवासने।",
        "anchors": "आलेपन ← लेप (लगाना) · अर्थे = ‘के प्रयोजन से’ · स्नेह (चिकनाई) + स्वेद (पसीना, सेंक) · अधस् = नीचे, ऊर्ध्व = ऊपर।",
    },
    "91": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["अभ्यञ्जने", "भोजनार्थे", "शिरसः", "विरेचने"]},
            {"label": "दूसरी पंक्ति",
             "items": ["शस्त्रकर्मणि", "वर्त्यर्थम्", "अञ्जन", "उत्सादनेषु"]}]},
        "letters": "अ-भो-शि-वि | श-व-अ-उ (अभ्यञ्जने, भोजनार्थे, शिरसः, विरेचने | शस्त्रकर्मणि, वर्त्यर्थम्, अञ्जन, उत्सादनेषु)।",
        "sandhi": "विसर्ग + च → श्च: शिरसः + च → शिरसश्च (श्लोक १० का भार्गवश्च्यवनः जैसा) · इ + अ → य् + अ: वर्ति + अर्थम् → वर्त्यर्थम् · अ + उ → ओ: अञ्जन + उत्सादनेषु → अञ्जनोत्सादनेषु।",
        "anchors": "अभ्यञ्जन ← अञ्जन (लगाना, चुपड़ना) · शस्त्र (औज़ार) + कर्म (क्रिया) = शस्त्रकर्म · शिरस् = सिर, इसी से ‘शिरोविरेचन’।",
    },
    "92": {
        "chain": {"steps": ["अजीर्ण", "आनाह", "वात (वाते)", "गुल्म", "शूल", "उदर",
                            "फिर: लवण पूरे, अब आठ मूत्र"]},
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["अजीर्णानाहयोः", "वाते", "गुल्मे", "शूले", "तथा", "उदरे"]},
            {"label": "दूसरी पंक्ति",
             "items": ["उक्तानि", "लवणानि", "ऊर्ध्वम्", "मूत्राणि", "अष्टौ", "निबोध", "मे"]}]},
        "sandhi": "आ + उ → ओ: तथा + उदरे → तथोदरे · इ + अ → य् + अ: मूत्राणि + अष्टौ → मूत्राण्यष्टौ · इ + ऊ → य् + ऊ: लवणानि + ऊर्ध्वम् → लवणान्यूर्ध्वम्।",
    },
    "93": {
        "frame": "क्या: मुख्य मूत्र · किसके उपदेश में: आत्रेय के · कौन-से (चार): भेड़, बकरी, गाय, भैंस।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["मुख्यानि", "यानि", "दिष्टानि", "सर्वाणि", "आत्रेयशासने"]},
            {"label": "दूसरी पंक्ति",
             "items": ["अविमूत्रम्", "अजामूत्रम्", "गोमूत्रम्", "माहिषम्", "च", "यत्"]}]},
        "letters": "अ-अ-गो-मा: अवि, अजा, गो, माहिष (भेड़, बकरी, गाय, भैंस)।",
        "pegs": "मेरा बनाया चित्र: एक आँगन में चार पशु पंक्ति में, भेड़, बकरी, गाय, भैंस: और पीछे एक गुरु की पाठशाला (आत्रेयशासने)।",
        "sandhi": "इ + आ → य् + आ: सर्वाणि + आत्रेयशासने → सर्वाण्यात्रेयशासने।",
    },
    "94": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["हस्तिमूत्रम्", "अथ", "उष्ट्रस्य", "हयस्य", "च", "खरस्य", "च"]},
            {"label": "दूसरी पंक्ति",
             "items": ["उष्णम्", "तीक्ष्णम्", "अथो", "अरूक्षम्", "कटुकम्", "लवणान्वितम्"]}]},
        "letters": "ह-उ-ह-ख: हाथी, ऊँट, घोड़ा, गधा। गुण: उ-ती-अ-क-ल (उष्ण, तीक्ष्ण, अरूक्ष, कटुक, लवणान्वित)।",
        "pegs": "मेरा बनाया चित्र: चार बड़े पशु चल रहे हैं: हाथी, ऊँट, घोड़ा, गधा; ऊपर गरम धूप (उष्ण) और तीखी हवा (तीक्ष्ण)।",
        "sandhi": "म् + अ: हस्तिमूत्रम् + अथ → हस्तिमूत्रमथ · अ + उ → ओ: अथ + उष्ट्रस्य → अथोष्ट्रस्य · अवग्रह: अथो + अरूक्षम् → अथो ऽरूक्षम् (अ छिपा)।",
        "contrast": "श्लोक ९३ के चार (भेड़, बकरी, गाय, भैंस) बनाम श्लोक ९४ के चार (हाथी, ऊँट, घोड़ा, गधा): मिलकर आठ।",
    },
    "95": {
        "chain": {"steps": ["उत्सादने (मलने में)", "आलेपनेषु (लेपों में)",
                            "आस्थापने (काढ़े की बस्ति में)", "विरेचने (विरेचन में)"]},
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["मूत्रम्", "उत्सादने", "युक्तम्", "युक्तम्", "आलेपनेषु", "च"]},
            {"label": "दूसरी पंक्ति",
             "items": ["युक्तम्", "आस्थापने", "मूत्रम्", "युक्तम्", "च", "अपि", "विरेचने"]}]},
        "pegs": "मेरा बनाया चित्र: चार दरवाज़ों पर चार बार ‘युक्तम्’ की मुहर: उत्सादन, आलेप, आस्थापन, विरेचन।",
        "sandhi": "म् + उ/आ: मूत्रम् + उत्सादने → मूत्रमुत्सादने · युक्तम् + आलेपनेषु → युक्तमालेपनेषु · युक्तम् + आस्थापने → युक्तमास्थापने · च + अपि → चापि।",
    },
    "96": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["स्वेदेषु", "अपि", "च", "तत्", "युक्तम्", "आनाहेषु", "अगदेषु", "च"]},
            {"label": "दूसरी पंक्ति",
             "items": ["उदरेषु", "अथ", "च", "अर्शःसु", "गुल्मि", "कुष्ठि", "किलासिषु"]}]},
        "letters": "स्वे-आ-अ | उ-अर्-गु-कु-कि (स्वेद, आनाह, अगद | उदर, अर्श, गुल्मी, कुष्ठी, किलासी)।",
        "sandhi": "उ + अ → व् + अ: स्वेदेषु + अपि → स्वेदेष्वपि · तत् + युक्तम् → तद्युक्तम् · तत् + युक्तम् + आनाहेषु + अगदेषु → तद्युक्तमानाहेष्वगदेषु।",
        "anchors": "कास = खाँसी (cough): मेरा उदाहरण, श्लोक में नहीं · -इन् = ‘वाला’: गुल्मिन् = गुल्म वाला।",
        "contrast": "गुल्म, कुष्ठ, किलास = रोग; गुल्मी, कुष्ठी, किलासी (-इन्) = उस रोग वाला रोगी। यहाँ तीनों रोगी के रूप में हैं।",
    },
    "97": {
        "chain": {"steps": ["उपनाहेषु (पुल्टिस में)", "परिषेके (धार डालने में)",
                            "दीपनीयम् (अग्नि-दीपक)", "विषघ्नम् (विष-नाशक)",
                            "क्रिमिघ्नम् (कृमि-नाशक)"]},
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["तत्", "युक्तम्", "उपनाहेषु", "परिषेके", "तथा", "एव", "च"]},
            {"label": "दूसरी पंक्ति",
             "items": ["दीपनीयम्", "विषघ्नम्", "च", "क्रिमिघ्नम्", "च", "उपदिश्यते"]}]},
        "anchors": "-घ्न = नाश करने वाला: विष-घ्न, क्रिमि-घ्न (वैसे ही ‘शत्रुघ्न’ में) · दीपन ← दीप (जलाना): ‘अग्नि को जलाने वाला’।",
        "sandhi": "अ + उ → ओ: च + उपदिश्यते → चोपदिश्यते · तत् + युक्तम् + उपनाहेषु → तद्युक्तमुपनाहेषु · तथा + एव → तथैव (आ + ए → ऐ)।",
    },
    "98": {
        "frame": "किसके लिए: पाण्डु-पीड़ित · क्या: उत्तम शर्म · पीने पर: कफ शान्त, वात अनुलोम (पित्त: श्लोक ९९)।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["पाण्डुरोगोपसृष्टानाम्", "उत्तमम्", "शर्म", "च", "उच्यते"]},
            {"label": "दूसरी पंक्ति",
             "items": ["श्लेष्माणम्", "शमयेत्", "पीतम्", "मारुतम्", "च", "अनुलोमयेत्"]}]},
        "sandhi": "अ + उ → ओ: पाण्डुरोग + उपसृष्टानाम् → पाण्डुरोगोपसृष्टानाम् · च + उच्यते → चोच्यते · च + अनुलोमयेत् → चानुलोमयेत्।",
        "anchors": "अनुलोम ← अनु (साथ) + लोम (बाल): ‘बाल की दिशा में’, यानी स्वाभाविक दिशा में · श्लेष्मा = कफ · मारुत = वायु।",
    },
    "99": {
        "frame": "पित्त: नीचे खिंचे · क्या कहा: गुणों का संग्रह · कैसे: सामान्य रूप से · आगे: अलग-अलग।",
        "seesaw": "सामान्येन (सामान्य रूप से, अब तक कहा) ↔ पृथक्त्वेन (अलग-अलग, आगे कहा जाएगा)।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["कर्षेत्", "पित्तम्", "अधोभागम्", "इति", "अस्मिन्", "गुणसंग्रहः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["सामान्येन", "मया", "उक्तः", "तु", "पृथक्त्वेन", "प्रवक्ष्यते"]}]},
        "sandhi": "आ + उ → ओ, विसर्ग + त → स्त: मया + उक्तः + तु → मयोक्तस्तु · पित्तम् + अधोभागम् + इति + अस्मिन् → पित्तमधोभागमित्यस्मिन् (इ + अ → य्)।",
        "chunks": "कर्षेत् पित्तम् | अधोभागम् | इति ‖ अस्मिन् गुणसंग्रहः | सामान्येन | मया उक्तः तु ‖ पृथक्त्वेन | प्रवक्ष्यते।",
    },
}

IMAGE_SPECS = {
    ("94", "contrast"): {
        "file": "urines-8-split.svg",
        "alt": ("Two columns listing the eight urines: the four of verse 93 (sheep, goat, cow, "
                "buffalo) and the four of verse 94 (elephant, camel, horse, donkey)."),
        "type": "split",
        "title": "आठ मूत्र: चार + चार",
        "cols": [["श्लोक ९३", ["अविमूत्रम्", "अजामूत्रम्", "गोमूत्रम्", "माहिषम्"]],
                 ["श्लोक ९४", ["हस्तिमूत्रम्", "उष्ट्र", "हय", "खर"]]],
    },
    ("99", "seesaw"): {
        "file": "general-separate-99.svg",
        "alt": ("Two columns: in general terms (stated so far) and separately (to be stated next), "
                "the pair of opposites of verse 99."),
        "type": "split",
        "title": "सामान्येन ↔ पृथक्त्वेन",
        "cols": [["सामान्येन", ["सामान्य रूप से", "अब तक कहा"]],
                 ["पृथक्त्वेन", ["अलग-अलग", "आगे कहा जाएगा"]]],
    },
}
