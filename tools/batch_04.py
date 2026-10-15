from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "अग्निवेशश्च भेलश्च",
    "question": "Who are the six disciples, and what did they take from the sage?",
    "rule": ("अग्निवेश, भेल, जतूकर्ण, पराशर, हारीत, क्षारपाणि जगृहुः (they received) "
             "तत् मुनेः वचः = Agniveśa, Bhela, Jatūkarṇa, Parāśara, Hārīta and "
             "Kṣārapāṇi received that teaching of the sage."),
    "limits": ("The sage is not named in this verse; the teacher in the "
               "preceding verse is Punarvasu. The edition notes the variant "
               "भेडश्च (Bheḍa) for भेलश्च, a second spelling of the same name."),
    "explain_hi": ("श्लोक ३० में पुनर्वसु ने छह शिष्यों को आयुर्वेद दिया; यहाँ उन्हीं "
                   "छह के नाम हैं: अग्निवेश, भेल, जतूकर्ण, पराशर, हारीत और "
                   "क्षारपाणि। ‘जगृहुः’ का अर्थ ‘उन्होंने ग्रहण किया’ है; श्लोक ४ का "
                   "‘जग्राह’ (उसने ग्रहण किया) इसी धातु का एकवचन रूप है। "
                   "‘तन्मुनेर्वचः’ = तत् + मुनेः + वचः, यानी ‘उन मुनि का वह वचन’। "
                   "पाठ-टिप्पणी में ‘भेल’ का एक पाठभेद ‘भेड’ दर्ज है।"),
    "hook": "छह नाम: अ-भे-ज-प-हा-क्षा · जगृहुः = उन्होंने ग्रहण किया (जग्राह का बहुवचन)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 30 says Punarvasu gave Āyurveda to six disciples. Which of these do you expect among them?",
            ("Agniveśa", "Agniveśa is the first of the six names in verse 31."),
            [("Indra", "Indra is a god of the earlier story, not one of the six."),
             ("Prajāpati", "Prajāpati is in the chain of verse 4, not among the six."),
             ("Brahmā", "Brahmā begins the chain of verse 4; he is not a disciple here.")],
            "The six names of verse 31 begin with Agniveśa.",
            "Verse 31 names the six disciples, beginning with Agniveśa."),
        match(1, "Match each Devanagari name to its Latin spelling.",
              [["अग्निवेशः", "Agniveśa"], ["जतूकर्णः", "Jatūkarṇa"],
               ["पराशरः", "Parāśara"], ["क्षारपाणिः", "Kṣārapāṇi"]],
              "Reading the names in Devanagari is the point of this card.",
              "अग्निवेशः = Agniveśa; जतूकर्णः = Jatūkarṇa; पराशरः = Parāśara; क्षारपाणिः = Kṣārapāṇi."),
        fill(2, "The verb meaning 'they received' is ____ (type it in Devanagari).",
             ["जगृहुः", "जगृहुस्", "जगृहु"],
             "जगृहुः is the verb of the verse; the subject is the six names.",
             "जगृहुः is the plural of जग्राह (verse 4, 'he received'): the same root √ग्रह्, but 'they' instead of 'he'.",
             "जगृहुः = they received (जग्राह = he received)."),
        mcq("discriminate", 3, "Which is the right split of जगृहुस्तन्मुनेर्वचः?",
            ("जगृहुः + तत् + मुनेः + वचः",
             "A visarga before त becomes स्, त् before म becomes न्, and a visarga before the voiced व becomes र्."),
            [("जगृहुस् + तन् + मुनेर् + वचः", "These pieces are not words; they are only the joined sounds."),
             ("जगृहु + स्तन् + मुनेः + वचः", "स्तन् is not a word."),
             ("जगृहुः + मुनेः + वचः", "That drops तत् ('that'), which the joined form still contains.")],
            "जगृहुस्तन्मुनेर्वचः = जगृहुः ('they received') + तत् ('that') + मुनेः ('of the sage') + वचः ('teaching').",
            "जगृहुः + तत् + मुनेः + वचः joins as जगृहुस्तन्मुनेर्वचः."),
        multi("apply", 4,
              "Which of these are among those who received the sage's teaching in verse 31?",
              [("भरद्वाजः", "He is the seeker of verse 3, not one of the six."),
               ("अग्निवेशः", "Right: the first of the six."),
               ("पुनर्वसुः", "He is the teacher of verse 30, not a disciple."),
               ("जतूकर्णः", "Right: the third of the six."),
               ("क्षारपाणिः", "Right: the last of the six.")],
              [1, 3, 4],
              "Verse 31 names exactly the six disciples; Bharadvāja and Punarvasu are named elsewhere.",
              "Only the six names of verse 31 are the receivers here."),
        mcq("transfer", 5,
            "An invented line begins मित्रश्च सोमश्च. What stands before the join in मित्रश्च?",
            ("मित्रः + च", "A visarga before च becomes श्, exactly as in अग्निवेशः + च = अग्निवेशश्च."),
            [("मित्रम् + च", "That would be written मित्रं च, without श्."),
             ("मित्रा + च", "That would be written मित्रा च; there is no visarga to turn into श्."),
             ("मित्र + श्च", "श्च is not a word; the श् comes from the visarga.")],
            "The same pattern as अग्निवेशश्च and भेलश्च: -ः + च gives -श्च.",
            "-श्च at the end of a name = -ः + च ('and').",
            teaches="When a name ends in -श्च, undo it as -ः + च ('and'); this works for any name in -अ."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "बुद्धेर्विशेषस्तत्रासीत्",
    "question": "Where did the six differ, and why did Agniveśa become the first author?",
    "rule": ("बुद्धेः विशेषः तत्र आसीत्, न उपदेशान्तरं मुनेः = the difference lay "
             "in intellect, not in the sage's teaching. यतः (that is why) Agniveśa "
             "first became the author of a treatise."),
    "limits": ("The verse says the difference was in intellect; that it was "
               "Agniveśa's superior intellect is the usual understanding (see the "
               "note). प्रथमम् may be 'first' (adverb) or 'of the first "
               "treatise' (with तन्त्रस्य)."),
    "explain_hi": ("छहों शिष्यों को एक ही उपदेश मिला था; भेद उपदेश में नहीं, बुद्धि में "
                   "था। इसी कारण अग्निवेश सबसे पहले तन्त्र के रचयिता बने। "
                   "‘नोपदेशान्तरम्’ = न + उपदेश + अन्तर: ‘उपदेश में कोई भेद नहीं’। "
                   "‘प्रथमम्’ को यहाँ ‘सबसे पहले’ पढ़ा गया है; ‘पहले तन्त्र का "
                   "कर्ता’ भी पढ़ा जा सकता है। टिप्पणी के अनुसार ‘बुद्धेर्विशेषः’ का "
                   "भाव अग्निवेश की श्रेष्ठ बुद्धि है।"),
    "hook": "उपदेश एक-सा, भेद बुद्धि में → इसीलिए अग्निवेश पहले तन्त्र-कर्ता।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The six disciples got the same teaching. What does the verse give as the difference among them?",
            ("A difference of intellect", "बुद्धेः विशेषः: the distinction lay in intellect."),
            [("A difference in the sage's teaching", "The verse says there was no difference in the teaching."),
             ("A difference of age", "Age is not mentioned."),
             ("A difference of home", "Home is not mentioned.")],
            "The distinction lay in intellect (बुद्धि); the sage's teaching did not differ.",
            "Same teaching, different intellect."),
        match(1, "Match each word of the verse to its meaning.",
              [["बुद्धेः", "of intellect"], ["विशेषः", "distinction"],
               ["उपदेशान्तरम्", "difference in teaching"], ["कर्ता", "author"]],
              "These four words carry the whole argument of the verse.",
              "बुद्धेः = of intellect; विशेषः = distinction; उपदेशान्तरम् = difference in teaching; कर्ता = author."),
        fill(2, "The word meaning 'first' in the second line is ____ (type it in Devanagari).",
             ["प्रथमम्", "प्रथमं"],
             "प्रथमम् tells that Agniveśa came first as author.",
             "प्रथमम् is read as an adverb, 'first'; the other reading, 'of the first treatise', also uses the same word.",
             "प्रथमम् = first."),
        mcq("discriminate", 3, "Which is the right split of नोपदेशान्तरम्?",
            ("न + उपदेशान्तरम्", "अ + उ joins as ओ, so न + उपदेशान्तरम् is written नोपदेशान्तरम्."),
            [("नो + पदेशान्तरम्", "पदेशान्तरम् is not a word."),
             ("नु + उपदेशान्तरम्", "नु is not the negative word here; the negative is न."),
             ("न + पदेशान्तरम्", "The word is उपदेश, with उ.")],
            "नोपदेशान्तरम् = न ('not') + उपदेशान्तरम् ('difference in teaching').",
            "नोपदेशान्तरम् = न + उपदेशान्तरम्."),
        mcq("apply", 4,
            "A reader says the sage taught the six differently. Which words of the verse speak against this?",
            ("नोपदेशान्तरं मुनेः", "न + उपदेशान्तरम् + मुनेः = no difference in the sage's teaching."),
            [("तन्त्रस्य कर्ता", "These words say who became an author, not how the teaching was given."),
             ("प्रथमम्", "This single word says 'first'; it says nothing about the teaching."),
             ("यतो ऽभवत्", "These words say 'that is why he became'; they do not describe the teaching.")],
            "नोपदेशान्तरं मुनेः says that the sage's teaching had no difference.",
            "न + उपदेशान्तरम् = no difference in the teaching."),
        mcq("transfer", 5,
            "By the pattern of नोपदेशान्तरम्, how is न + उदकम् (not water) written when joined?",
            ("नोदकम्", "अ + उ joins as ओ, as in न + उपदेशान्तरम् = नोपदेशान्तरम्."),
            [("नुदकम्", "अ + उ does not give a short उ."),
             ("नौदकम्", "औ comes from अ + ओ or अ + औ, not from अ + उ."),
             ("नाउदकम्", "The two vowels must join; they do not stay apart.")],
            "The rule अ + उ → ओ works in any word, not only here.",
            "अ + उ → ओ.",
            teaches="A word ending in -अ, followed by a word starting with उ, joins as ओ."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "अथ भेलादयश्चक्रुः",
    "question": "What did Bhela and the others do next, and to whom did they recite it?",
    "rule": ("अथ भेलादयः स्वं स्वं तन्त्रं चक्रुः, कृतानि च आत्रेयं सर्षिसङ्घं "
             "श्रावयामासुः (they made hear) = then Bhela and the others each composed his own "
             "treatise and made Ātreya and the assembly of sages hear them."),
    "limits": ("The verse does not list the 'others' again, nor say what the "
               "treatises contained. श्रावयामासुः takes two objects: the works "
               "(कृतानि) and the one made to hear (आत्रेयम्)."),
    "explain_hi": ("अग्निवेश के बाद भेल आदि ने भी अपना-अपना तन्त्र रचा (‘स्वं स्वम्’ = "
                   "अपना-अपना)। फिर उन मेधावी शिष्यों ने अपनी रचनाएँ आत्रेय को "
                   "ऋषि-समूह सहित सुनाईं। ‘श्रावयामासुः’ ‘सुनवाया’ अर्थ वाली प्रेरणार्थक "
                   "क्रिया है; इसलिए ‘किसे सुनाया’ (आत्रेयम्) और ‘क्या सुनाया’ "
                   "(कृतानि) दोनों द्वितीया में हैं। ‘सर्षिसङ्घम्’ = स + ऋषिसङ्घम् "
                   "(ऋषि-समूह के साथ)।"),
    "hook": "रचा (चक्रुः) → सुनाया (श्रावयामासुः): आत्रेय को, ऋषि-समूह सहित।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Agniveśa was the first author (verse 32). What do you expect Bhela and the others did?",
            ("They also composed treatises of their own", "The verse says each composed his own treatise."),
            [("They gave up the science", "Nothing of the kind is said."),
             ("They went to Indra for more teaching", "Indra is not in this verse."),
             ("They left for the Himalaya", "No journey is mentioned.")],
            "Bhela and the others each composed his own treatise.",
            "भेलादयः चक्रुः स्वं स्वं तन्त्रम् = each composed his own treatise."),
        match(1, "Match each word of the verse to its meaning.",
              [["तन्त्रम्", "treatise"], ["स्वं स्वम्", "each his own"],
               ["श्रावयामासुः", "they made hear"], ["सुमेधसः", "highly intelligent"]],
              "These words carry the composing and the reciting.",
              "तन्त्रम् = treatise; स्वं स्वम् = each his own; श्रावयामासुः = they made hear; सुमेधसः = highly intelligent."),
        fill(2, "The word meaning 'treatise' in the first line is ____ (type it in Devanagari).",
             ["तन्त्रम्", "तन्त्रं"],
             "तन्त्रम् is what each of them composed.",
             "तन्त्र is the treatise or science; the same word occurs in verse 29 (तन्त्रोक्तम्) and verse 32 (तन्त्रस्य).",
             "तन्त्रम् = treatise."),
        mcq("discriminate", 3, "Which is the right split of सर्षिसङ्घम्?",
            ("स + ऋषिसङ्घम्", "अ + ऋ joins as अर्, so स + ऋषिसङ्घम् is written सर्षिसङ्घम्."),
            [("सर् + षिसङ्घम्", "षिसङ्घम् is not a word."),
             ("सा + ऋषिसङ्घम्", "The prefix is short स ('with'), not सा."),
             ("सर्ष + इसङ्घम्", "इसङ्घम् is not a word.")],
            "सर्षिसङ्घम् = स ('with') + ऋषिसङ्घम् ('assembly of sages'): together with the assembly of sages.",
            "सर्षिसङ्घम् = स + ऋषिसङ्घम्."),
        mcq("apply", 4,
            "श्रावयामासुः means 'they made hear'. Which word names the one made to hear?",
            ("आत्रेयम्", "It is the person who heard; the works are what was heard."),
            [("कृतानि", "These are the works that were recited, not the hearer."),
             ("सुमेधसः", "These are the doers, the reciters."),
             ("भेलादयः", "These are also the doers, the reciters.")],
            "आत्रेयम् is the hearer; कृतानि is what was heard; both are in the accusative.",
            "With 'made hear', the hearer and the thing heard are both accusative."),
        mcq("transfer", 5,
            "An invented line reads शिष्याः गुरुं श्लोकान् श्रावयामासुः. Who was made to hear?",
            ("The teacher (गुरुम्)", "The one who hears is named in the accusative, as आत्रेयम् is here."),
            [("The pupils (शिष्याः)", "The pupils are the doers, who recited."),
             ("The verses (श्लोकान्)", "The verses are what was heard, not the hearer."),
             ("Nobody", "श्रावयामासुः says that someone was made to hear.")],
            "The same pattern as आत्रेयं … कृतानि श्रावयामासुः: the hearer and the thing heard are both accusative.",
            "Hearer (a person) + thing heard + श्रावयामासुः: the person is the hearer.",
            teaches="After 'made hear', the person is the hearer and the thing is what was heard; sense tells you which is which."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "श्रुत्वा सूत्रणमर्थानाम्",
    "question": "How did the sages react to the recited treatises?",
    "rule": ("ऋषयः सूत्रणं श्रुत्वा प्रहृष्टाः 'यथावत् सूत्रितम्' इति अनुमेनिरे = "
             "having heard the composition, the sages were delighted and "
             "approved, saying: 'It has been properly composed.'"),
    "limits": ("The printed text reads प्रहृष्टास्त ऽनुमेनिरे; the expected "
               "form is प्रहृष्टास्ते ऽनुमेनिरे (see the note). पुण्यकर्मणाम् may "
               "belong to सूत्रणम् (composed by the meritorious) or to "
               "अर्थानाम्."),
    "explain_hi": ("ऋषियों ने रचनाएँ सुनीं, बहुत प्रसन्न हुए और उन्हें मान्यता दी: "
                   "‘ठीक ढंग से सूत्रबद्ध हुआ है’। ‘श्रुत्वा’ ‘सुनकर’ है, पहले की "
                   "क्रिया; ‘अनुमेनिरे’ (उन्होंने अनुमोदन किया) बाद की, और दोनों के "
                   "कर्ता ऋषि हैं। ‘इति’ ऋषियों के कहे शब्दों को बन्द करता है। "
                   "‘पुण्यकर्मणाम्’ को यहाँ रचने वाले शिष्यों के लिए पढ़ा गया है; उसे "
                   "‘अर्थानाम्’ का विशेषण भी माना जा सकता है।"),
    "hook": "सुना (श्रुत्वा) → प्रसन्न (प्रहृष्टाः) → ‘यथावत् सूत्रितम्’ इति कहकर माना (अनुमेनिरे)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The sages heard the treatises recited. What do you expect their reaction was?",
            ("They were delighted and approved", "प्रहृष्टाः and अनुमेनिरे say this."),
            [("They rejected the treatises", "The verse says they approved."),
             ("They asked the authors to rewrite them", "No rewriting is mentioned."),
             ("They left without a word", "They spoke, with the words ending in इति.")],
            "The sages were delighted (प्रहृष्टाः) and approved (अनुमेनिरे).",
            "Heard → delighted → approved."),
        match(1, "Match each word of the verse to its meaning.",
              [["श्रुत्वा", "having heard"], ["प्रहृष्टाः", "delighted"],
               ["अनुमेनिरे", "they approved"], ["यथावत्", "properly"]],
              "These words give what the sages did and how they judged it.",
              "श्रुत्वा = having heard; प्रहृष्टाः = delighted; अनुमेनिरे = they approved; यथावत् = properly."),
        fill(2, "The word that closes the sages' spoken remark is ____ (type it in Devanagari).",
             ["इति"],
             "इति stands right after the remark यथावत्सूत्रितम्.",
             "इति closes a quotation, as it did in verse 2 (इति ह स्माह): the words before it are what the sages said.",
             "इति = closing mark of what was said."),
        mcq("discriminate", 3, "Which is the right split of सूत्रणमर्थानामृषयः?",
            ("सूत्रणम् + अर्थानाम् + ऋषयः",
             "A final म् is simply written together with the vowel that follows (म् + अ gives म)."),
            [("सूत्रण + मर्थानाम् + ऋषयः", "मर्थानाम् is not a word."),
             ("सूत्रणम् + अर्थानामृ + षयः", "षयः is not a word."),
             ("सूत्रणमर्था + नामृषयः", "नामृषयः is not a word.")],
            "सूत्रणमर्थानामृषयः = सूत्रणम् ('composition') + अर्थानाम् ('of the subjects') + ऋषयः ('the sages').",
            "सूत्रणम् + अर्थानाम् + ऋषयः."),
        mcq("apply", 4,
            "श्रुत्वा means 'having heard'. Whose act of hearing is it?",
            ("The sages' (ऋषयः), who then approved", "A 'having done' word shares the doer of the main verb अनुमेनिरे."),
            [("The disciples', who composed the works", "The disciples recited; the sages are the doers of अनुमेनिरे."),
             ("Indra's, from heaven", "Indra is not in this verse."),
             ("Nobody's in particular", "Normally a 'having done' word shares the doer of the main verb.")],
            "श्रुत्वा and अनुमेनिरे have the same doer: the sages heard, then approved.",
            "A 'having done' word shares the doer of the main verb."),
        mcq("transfer", 5,
            "An invented line reads ऋषयो ग्रन्थं दृष्ट्वा प्रहृष्टा अभवन्. Which act came first?",
            ("Seeing the book (दृष्ट्वा)", "A -त्वा / -य word names the earlier act, as श्रुत्वा does here."),
            [("Becoming delighted", "That is the main verb, so it comes after."),
             ("Both together", "A 'having done' word names an act finished before."),
             ("It cannot be told", "The ending tells you.")],
            "दृष्ट्वा is the same kind of word as श्रुत्वा and बुद्ध्वा.",
            "-त्वा word = the earlier act, by the doer of the main verb.",
            teaches="A word ending in -त्वा names an act done before the main verb, by the same doer."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "सर्व एवास्तुवंस्तांश्च",
    "question": "What did all the sages do and say together?",
    "rule": ("सर्वे एव तान् अस्तुवन्; 'साधु, भूतेषु अनुक्रोशः' इति उच्चैः समम् "
             "अब्रुवन् = all of them praised them and said together, loudly: "
             "'Well done! (This is) compassion for living beings.'"),
    "limits": ("The exclamation may also be read '(Your) compassion for beings "
               "is good'. सर्वभूतहितैषिणः may go with the sages (nominative) or "
               "with तान् (accusative)."),
    "explain_hi": ("सब ऋषियों ने उन शिष्यों की प्रशंसा की और एक साथ, ऊँचे स्वर में कहा: "
                   "‘साधु! (यह) प्राणियों पर अनुकम्पा है।’ ‘अनुक्रोश’ वही शब्द है जो "
                   "श्लोक ७ में ऋषियों की प्रेरणा था। ‘सर्व एव’ में ‘सर्वे’ का अन्तिम "
                   "‘ए’ स्वर से पहले ‘अ’ बन गया है (सर्वे + एव)। ‘सर्वभूतहितैषिणः’ = "
                   "सर्व + भूत + हित + एषिणः (सब प्राणियों का हित चाहने वाले)।"),
    "hook": "सब ऋषि: प्रशंसा की (अस्तुवन्) और एक स्वर में कहा ‘साधु! भूतों पर अनुक्रोश’।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The sages approved the treatises. What do you expect they called out together?",
            ("Well done (साधु)", "The verse has them cry साधु, 'well done'."),
            [("A command to stop", "No command is given."),
             ("A complaint about the treatises", "They praised, not complained."),
             ("A prayer for rain", "Rain is not mentioned.")],
            "They praised the authors and called out साधु.",
            "Praise ends with the shout साधु."),
        match(1, "Match each word of the verse to its meaning.",
              [["अस्तुवन्", "they praised"], ["साधु", "well done"],
               ["उच्चैः", "loudly"], ["समम्", "together"]],
              "These words say how the sages praised.",
              "अस्तुवन् = they praised; साधु = well done; उच्चैः = loudly; समम् = together."),
        fill(2, "The word meaning 'loudly' in the second line is ____ (type it in Devanagari).",
             ["उच्चैः", "उच्चैर्", "उच्चै"],
             "उच्चैः is joined to the next word as उच्चैरब्रुवन्.",
             "उच्चैः is an adverb, 'loudly'; before the vowel of अब्रुवन् its visarga becomes र्.",
             "उच्चैः = loudly."),
        mcq("discriminate", 3, "Which is the right split of इत्युच्चैरब्रुवन्?",
            ("इति + उच्चैः + अब्रुवन्",
             "इ + उ becomes य् + उ, and the visarga of उच्चैः becomes र् before the vowel of अब्रुवन्."),
            [("इत्यु + च्चैरब्रुवन्", "च्चैरब्रुवन् is not a word."),
             ("इति + च्चैः + अब्रुवन्", "च्चैः is not a word; the word is उच्चैः."),
             ("इत + उच्चैः + अब्रुवन्", "The word that closes the quotation is इति, ending in -ि, not इत.")],
            "इत्युच्चैरब्रुवन् = इति (closes the quoted words) + उच्चैः (loudly) + अब्रुवन् (they said).",
            "इत्युच्चैरब्रुवन् = इति + उच्चैः + अब्रुवन्."),
        mcq("apply", 4,
            "The first line reads सर्व एव, yet many sages are meant. Why does the verse have सर्व and not सर्वे?",
            ("Final -ए before a vowel turns into अ: सर्वे + एव = सर्व एव",
             "The plural सर्वे loses its ए to अ before the vowel of एव."),
            [("सर्व is singular, so one sage speaks", "The verbs अस्तुवन् and अब्रुवन् are plural."),
             ("सर्व is a different word meaning 'a little'", "सर्व means 'all'."),
             ("It is a mistake in the text", "It is the regular result of sandhi.")],
            "सर्वे + एव → सर्व एव: ए before a vowel becomes अ and the vowel stays apart (सर्वः + एव would also give सर्व एव; the plural verbs and the note decide).",
            "सर्व एव = सर्वे + एव (all, indeed)."),
        mcq("transfer", 5,
            "An invented line reads सर्व आगताः. By the same pattern, how many came, and what is the word before the join?",
            ("All of them; सर्वे + आगताः", "ए before a vowel becomes अ, so सर्वे + आगताः is written सर्व आगताः."),
            [("One only; सर्वः + आगताः", "सर्वः + आगताः would also join as सर्व आगताः, but singular सर्वः cannot agree with plural आगताः, so सर्वे is meant."),
             ("Nobody; सर्व + नागताः", "नागताः is not what is written."),
             ("It cannot be told", "The pattern of सर्व एव shows it.")],
            "A bare -अ before a vowel can hide a plural -ए, as in सर्व एव.",
            "सर्व + vowel can be सर्वे + vowel (all).",
            teaches="Before a vowel, final -ए can shrink to -अ; it may be read as the plural 'all' (सर्वे) when the verbs are plural."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "तं पुण्यं शुश्रुवुः शब्दम्",
    "question": "Who heard the sages' cry, and how did they respond?",
    "rule": ("दिवि स्थिताः देवर्षयः सामराः तं पुण्यं शब्दं शुश्रुवुः, श्रुत्वा परं "
             "मुमुदिरे = the divine sages in heaven, with the gods, heard that holy "
             "utterance and, having heard, rejoiced greatly."),
    "limits": ("The printed परमर्षीणं is a likely slip for परमर्षीणाम् (see the "
               "note). 'Of the supreme sages' is taken with शब्दम्. The verse "
               "does not say how the sound reached heaven."),
    "explain_hi": ("अब दृश्य पृथ्वी से स्वर्ग की ओर जाता है। स्वर्ग (दिवि) में स्थित देवर्षियों "
                   "ने, देवताओं सहित, परम ऋषियों का वह पुण्य शब्द सुना और सुनकर बहुत "
                   "प्रसन्न हुए। ‘शुश्रुवुः’ (उन्होंने सुना) एक पूर्ण क्रिया है, ‘श्रुत्वा’ "
                   "(सुनकर) पहले हुई क्रिया। ‘सामराः’ = स + अमराः (देवताओं के साथ); "
                   "‘देवर्षयः’ = देव + ऋषयः।"),
    "hook": "स्वर्ग में देवर्षि + देवता: सुना (शुश्रुवुः) → सुनकर (श्रुत्वा) बहुत प्रसन्न (मुमुदिरे)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The sages cried साधु aloud. Who do you expect heard it, according to this verse?",
            ("The divine sages in heaven, with the gods", "दिवि स्थिताः देवर्षयः सामराः are the hearers."),
            [("Only the six disciples", "The disciples are not the hearers named here."),
             ("Indra alone", "Indra is not named in this verse; the hearers are plural."),
             ("Nobody heard it", "शुश्रुवुः says that it was heard.")],
            "The divine sages and the gods in heaven heard the holy sound.",
            "Heaven heard the sages' cry."),
        match(1, "Match each word of the verse to its meaning.",
              [["दिवि", "in heaven"], ["देवर्षयः", "divine sages"],
               ["शब्दम्", "sound, utterance"], ["मुमुदिरे", "they rejoiced"]],
              "These words say who heard, where, and how they felt.",
              "दिवि = in heaven; देवर्षयः = divine sages; शब्दम् = sound; मुमुदिरे = they rejoiced."),
        fill(2, "The word meaning 'in heaven' is ____ (type it in Devanagari).",
             ["दिवि"],
             "दिवि tells where the hearers were.",
             "दिवि ends in -इ, the locative: 'in heaven'. The hearers are stationed (स्थिताः) there.",
             "दिवि = in heaven."),
        mcq("discriminate", 3, "Which is the right split of देवर्षयः?",
            ("देव + ऋषयः", "अ + ऋ joins as अर्, so देव + ऋषयः is written देवर्षयः."),
            [("देवर् + षयः", "षयः is not a word."),
             ("देवा + ऋषयः", "The first word is देव, with short अ."),
             ("दे + वर्षयः", "वर्षयः is not a word.")],
            "देवर्षयः = देव ('god') + ऋषयः ('sages'): divine sages.",
            "देवर्षयः = देव + ऋषयः."),
        mcq("apply", 4,
            "सामराः is स + अमराः, 'together with the gods'. Who is with the gods?",
            ("The divine sages standing in heaven", "सामराः agrees with देवर्षयः, in the plural nominative."),
            [("The sages on the Himalaya", "The sages on the Himalaya are the ones who cried out."),
             ("The six disciples", "The disciples are not part of this verse."),
             ("Indra alone", "The word is plural.")],
            "सामराः describes the hearers: the divine sages, accompanied by the gods.",
            "सा- at the start = 'together with'."),
        mcq("transfer", 5,
            "An invented line reads सशिष्यो गुरुरागतः. By the pattern of सामराः, who came?",
            ("The teacher, together with his pupils", "स- at the start means 'together with', as in सामराः."),
            [("The pupils, with the teacher left behind", "The doer is गुरुः, who comes with them."),
             ("The pupils, without a teacher", "स- means 'with', not 'without'."),
             ("Nobody came", "आगतः says that someone came.")],
            "The same pattern as सामराः and सर्षिसङ्घम्: स- = together with.",
            "स + noun = together with the noun.",
            teaches="A word beginning with स- ('with') describes the doer as accompanied by what follows स-."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "अहो साध्विति निर्घोषः",
    "question": "What sound filled the three worlds, and what was it like?",
    "rule": ("'अहो, साधु' इति निर्घोषः नभसि हर्षात् भूतैः उदीरितः त्रीन् लोकान् "
             "अन्ववादयत् = the cry 'Ah, well done!', smooth and deep, raised in "
             "the sky by beings out of joy, made the three worlds resound."),
    "limits": ("The edition notes the variant -नादयत् (अन्वनादयत्, 'made "
               "resound'), nearly the same in sense. भूतैः may mean spirits or "
               "celestial beings rather than creatures in general; the verse does "
               "not say which."),
    "explain_hi": ("भूतों का हर्ष एक घोष बनकर गूँजता है: ‘अहो, साधु!’ यह घोष स्निग्ध "
                   "(कोमल) और गम्भीर था, आकाश में हर्ष से भूतों द्वारा उच्चारित हुआ और "
                   "तीनों लोकों में गूँज उठा। ‘हर्षाद्भूतैः’ = हर्षात् + भूतैः (त् घोष ‘भ’ "
                   "से पहले ‘द्’ बना)। टिप्पणी में पाठभेद ‘-नादयत्’ है, जिसका अर्थ ‘गुँजाया’ "
                   "लगभग वही रहता है। ‘भूतैः’ का अर्थ यहाँ केवल प्राणी नहीं, आकाशीय जीव भी हो "
                   "सकता है।"),
    "hook": "साधु! (३५) → स्वर्ग ने सुना (३६) → आकाश में ‘अहो साधु’ का घोष तीनों लोकों में (३७)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Heaven rejoiced over the sages' praise. What do you expect resounded through the three worlds?",
            ("A cry of praise: 'Ah, well done!'", "The verse gives the cry अहो साधु."),
            [("A cry of grief", "Joy (हर्ष) is the cause named, not grief."),
             ("A royal command", "No ruler is mentioned."),
             ("A thunderclap", "No thunder is mentioned; it is a cry of words.")],
            "The cry अहो साधु resounded through the three worlds.",
            "Joy in heaven becomes a cry of praise."),
        match(1, "Match each word of the verse to its meaning.",
              [["निर्घोषः", "resounding cry"], ["लोकान्", "worlds"],
               ["नभसि", "in the sky"], ["हर्षात्", "out of joy"]],
              "These words say what sounded, where, and why.",
              "निर्घोषः = resounding cry; लोकान् = worlds; नभसि = in the sky; हर्षात् = out of joy."),
        fill(2, "The Sanskrit word for 'three' in the first line (right after लोकान्) is ____ (type it in Devanagari).",
             ["त्रीन्", "त्रीन"],
             "त्रीन् stands with लोकान्: the three worlds.",
             "त्रीन् is the accusative plural of 'three', matching लोकान्: the cry made the three worlds resound.",
             "त्रीन् = three (the three worlds, accusative)."),
        mcq("discriminate", 3, "Which is the right split of हर्षाद्भूतैरुदीरितः?",
            ("हर्षात् + भूतैः + उदीरितः",
             "त् before the voiced भ becomes द्, and the visarga of भूतैः becomes र् before the vowel of उदीरितः."),
            [("हर्षा + द्भूतैः + उदीरितः", "द्भूतैः is not a word."),
             ("हर्षाद् + भूतैर् + उदीरितः", "These pieces carry the joined sounds, not the words."),
             ("हर्षात् + भूतैः + रुदीरितः", "रुदीरितः is not a word; the र् comes from the visarga.")],
            "हर्षाद्भूतैरुदीरितः = हर्षात् ('out of joy') + भूतैः ('by beings') + उदीरितः ('uttered').",
            "हर्षात् + भूतैः + उदीरितः."),
        multi("apply", 4,
              "Which words describe the quality of the cry, not where or why it sounded?",
              [("स्निग्ध", "Right: smooth, soft."),
               ("नभसि", "This tells where: in the sky."),
               ("गम्भीर", "Right: deep."),
               ("हर्षात्", "This tells why: out of joy.")],
              [0, 2],
              "स्निग्धगम्भीरः = smooth and deep; नभसि gives the place, हर्षात् the cause.",
              "Quality of the cry: स्निग्ध and गम्भीर."),
        mcq("transfer", 5,
            "By the pattern हर्षात् + भूतैः = हर्षाद्भूतैः, how is the invented जगत् + भद्रम् written when joined?",
            ("जगद्भद्रम्", "A final त् before a voiced letter like भ becomes द्."),
            [("जगत्भद्रम्", "त् does not stay before a voiced भ."),
             ("जगत्तभद्रम्", "No extra त is added."),
             ("जगध्भद्रम्", "त् becomes द्, not ध्.")],
            "The same sandhi as हर्षाद्भूतैः: त् + voiced consonant → द् + voiced consonant.",
            "त् before a voiced consonant → द्.",
            teaches="A word-final त् turns into द् before a voiced consonant such as भ, ग, ब, द."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "शिवो वायुर्ववौ सर्वा",
    "question": "Which three signs followed the cry?",
    "rule": ("शिवः वायुः ववौ, सर्वाः दिशः भाभिः उन्मीलिताः, सजलाः दिव्याः "
             "कुसुमवृष्टयः निपेतुः = an auspicious wind blew, all directions were "
             "lit with radiance, and heavenly showers of flowers fell with water."),
    "limits": ("शिवः here is the adjective 'auspicious' for the wind, not the "
               "god. उन्मीलिताः ('lit up', literally 'opened') and सजलाः "
               "('with water') are taken as in the translation."),
    "explain_hi": ("घोष के बाद तीन शुभ संकेत आते हैं: मंगलकारी वायु बही (शिवो वायुर्ववौ), "
                   "सब दिशाएँ प्रकाश से जगमगा उठीं (भाभिरुन्मीलिता दिशः), और दिव्य "
                   "पुष्प-वर्षा जल सहित हुई (सजलाः कुसुमवृष्टयः)। यहाँ ‘शिवः’ विशेषण है, "
                   "यानी ‘मंगलकारी’; यह देवता का नाम नहीं। ‘सर्वाः’ का विसर्ग ‘भाभिः’ के "
                   "घोष ‘भ’ से पहले लुप्त हुआ है (सर्वा भाभिः)।"),
    "hook": "तीन संकेत: वायु बही · दिशाएँ जगमगाईं · जल सहित फूल बरसे।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "After the cry resounded, what kind of signs do you expect the verse to describe?",
            ("Auspicious signs: a wind, light and flowers", "The verse names a good wind, lit directions and flowers."),
            [("Signs of coming disease", "Disease is not mentioned here."),
             ("A storm that destroys the Himalaya", "No destruction is mentioned."),
             ("A command from the gods", "The signs are natural events, not commands.")],
            "An auspicious wind blew, the directions were lit, and flowers fell.",
            "Three good signs follow the cry."),
        order(1, "Put the three signs in the order the verse names them.",
              ["वायुः", "दिशः", "कुसुमवृष्टयः"],
              "The wind comes first, then the lit directions, then the showers of flowers.",
              "वायु → दिशः → कुसुमवृष्टयः."),
        fill(2, "The word meaning 'auspicious', which describes the wind, is ____ (type it in Devanagari).",
             ["शिवः", "शिवो", "शिव"],
             "शिवः describes वायुः: the auspicious wind.",
             "शिवः is an ordinary adjective here ('auspicious'), agreeing with वायुः; the verse does not speak of a god.",
             "शिवः = auspicious (of the wind)."),
        mcq("discriminate", 3, "Which is the right split of सजलाश्चैव?",
            ("सजलाः + च + एव", "A visarga before च becomes श्, and च + एव joins as चैव (अ + ए → ऐ)."),
            [("सजला + श्चैव", "श्चैव is not a word."),
             ("सजलाः + श्च + एव", "श्च is not a word; the श् comes from the visarga."),
             ("सजल + आश्चैव", "आश्चैव is not a word.")],
            "सजलाश्चैव = सजलाः ('with water') + च ('and') + एव ('indeed').",
            "सजलाः + च + एव."),
        mcq("apply", 4,
            "On the usual reading, what falls in the last line?",
            ("Heavenly showers of flowers, together with water", "सजलाः = with water; कुसुमवृष्टयः = showers of flowers."),
            [("Heavenly showers of water only", "The showers are of flowers, with water."),
             ("Showers of gems, with water", "Gems are not named."),
             ("Showers of fire", "Fire is not named.")],
            "निपेतुः सजलाः दिव्याः कुसुमवृष्टयः = heavenly showers of flowers fell, with water.",
            "सजलाः = स + जल: with water."),
        mcq("transfer", 5,
            "By the pattern सर्वाः + भाभिः = सर्वा भाभिः, how is the invented बालाः + गच्छन्ति written when joined?",
            ("बाला गच्छन्ति", "A visarga after आ is dropped before a voiced consonant such as ग."),
            [("बालाः गच्छन्ति", "In the joined form the visarga is dropped."),
             ("बालो गच्छन्ति", "ो comes from a visarga after short अ, not after आ."),
             ("बालार् गच्छन्ति", "A visarga after आ does not become र् before a voiced consonant.")],
            "The same pattern as सर्वा भाभिः and उन्मीलिता दिशः: -आः disappears before a voiced consonant.",
            "-आः + voiced consonant → -आ.",
            teaches="After आ, a visarga is dropped before a voiced consonant; after short अ it would become ो."),
    ],
}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "अथाग्निवेशप्रमुखान् विविशुः",
    "question": "Who entered Agniveśa and the others, and what are they called?",
    "rule": ("अथ ज्ञानदेवताः अग्निवेशप्रमुखान् विविशुः = then the deities of "
             "knowledge entered Agniveśa and the others: बुद्धि, सिद्धि, स्मृति, "
             "मेधा, धृति, कीर्ति, क्षमा, दया."),
    "limits": ("क्षमादया is written without a space; it is read as two names, "
               "क्षमा and दया, not 'क्षमा etc.' (see the note). The verse does not "
               "say these deities are persons or powers; it only says they "
               "'entered' the disciples."),
    "explain_hi": ("देवताओं की प्रसन्नता और शुभ संकेतों के बाद शिष्यों में ज्ञान की देवियाँ प्रवेश करती हैं: "
                   "बुद्धि, सिद्धि, स्मृति, मेधा, धृति, कीर्ति, क्षमा और दया। "
                   "‘अग्निवेशप्रमुखान्’ = अग्निवेश जिनमें प्रमुख हैं, यानी वे शिष्य। "
                   "‘विविशुः’ (प्रवेश किया) का कर्म द्वितीया में है। सूची में सब स्त्रीलिंग "
                   "नाम हैं; ‘क्षमादया’ इसीलिए दो नाम पढ़ा गया है, ‘क्षमा आदि’ नहीं।"),
    "hook": "ज्ञान की आठ देवियाँ: बुद्धि · सिद्धि · स्मृति · मेधा · धृति · कीर्ति · क्षमा · दया।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The sages approved the treatises and heaven rejoiced. Who or what do you expect entered the disciples, according to this verse?",
            ("Deities of knowledge", "ज्ञानदेवताः are the ones who entered."),
            [("The diseases of verse 6", "The diseases are not mentioned here."),
             ("The gods Indra and the Aśvins", "They are not the ones who entered the disciples."),
             ("Wild beasts of the Himalaya", "No beasts are named.")],
            "The deities of knowledge entered Agniveśa and the other disciples.",
            "ज्ञानदेवताः entered the disciples."),
        match(1, "Match each name of the list to its meaning.",
              [["बुद्धिः", "intellect"], ["स्मृतिः", "memory"],
               ["धृतिः", "fortitude"], ["दया", "compassion"]],
              "Four of the eight deities, with their usual meanings.",
              "बुद्धिः = intellect; स्मृतिः = memory; धृतिः = fortitude; दया = compassion."),
        fill(2, "The verb meaning 'entered' is ____ (type it in Devanagari).",
             ["विविशुः", "विविशुर्", "विविशु"],
             "विविशुः is the verb of the sentence.",
             "विविशुः is a plural past form of √विश् ('enter'): 'they entered'. Its doers are the deities and its objects are the disciples.",
             "विविशुः = they entered."),
        mcq("discriminate", 3, "Which is the right split of विविशुर्ज्ञानदेवताः?",
            ("विविशुः + ज्ञानदेवताः", "A visarga before the voiced ज becomes र्."),
            [("विविशुर् + ज्ञानदेवताः", "विविशुर् is the joined sound, not the word."),
             ("विविश + उर्ज्ञानदेवताः", "उर्ज्ञानदेवताः is not a word."),
             ("विविशु + र्ज्ञानदेवताः", "र्ज्ञानदेवताः is not a word.")],
            "विविशुर्ज्ञानदेवताः = विविशुः ('they entered') + ज्ञानदेवताः ('deities of knowledge').",
            "विविशुः + ज्ञानदेवताः."),
        multi("apply", 4,
              "Which of these are among the deities named in verse 39?",
              [("मेधा", "Right: retentive intelligence."),
               ("श्रद्धा", "Not named in this verse."),
               ("कीर्तिः", "Right: fame."),
               ("शान्तिः", "Not named in this verse."),
               ("क्षमा", "Right: forbearance.")],
              [0, 2, 4],
              "The verse names बुद्धि, सिद्धि, स्मृति, मेधा, धृति, कीर्ति, क्षमा and दया; श्रद्धा and शान्ति are not in it.",
              "Only the eight names of the verse count."),
        mcq("transfer", 5,
            "By the pattern स्मृतिः + मेधा = स्मृतिर्मेधा, how is the invented मतिः + बलम् written when joined?",
            ("मतिर्बलम्", "A visarga after इ becomes र् before a voiced consonant such as ब."),
            [("मतिबलम्", "The visarga does not simply vanish after इ."),
             ("मतो बलम्", "ो comes from a visarga after short अ, not after इ."),
             ("मतिःबलम्", "In the joined form the visarga must change.")],
            "The same sandhi as स्मृतिर्मेधा and धृतिः कीर्तिः: -इः + voiced consonant → -इर्.",
            "-इः + voiced consonant → -इर्.",
            teaches="After इ or उ, a visarga becomes र् before a voiced consonant."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "तानि चानुमतान्येषाम्",
    "question": "What became of the approved treatises, and for whose benefit?",
    "rule": ("एषां तानि तन्त्राणि परमर्षिभिः अनुमतानि भुवि प्रतिष्ठां लेभिरे = "
             "their treatises, approved by the supreme sages, gained a firm "
             "standing on earth, for the welfare of the multitudes of beings."),
    "limits": ("The edition notes the variant भावाय for भवाय. एषाम् may go "
               "with तन्त्राणि ('their treatises') or with परमर्षिभिः. भवाय is "
               "taken as 'welfare', not 'existence'."),
    "explain_hi": ("अध्याय के इस भाग का निष्कर्ष: शिष्यों के वे तन्त्र, जिन्हें परम ऋषियों ने "
                   "अनुमोदित किया था, पृथ्वी पर प्रतिष्ठित हुए, प्राणि-समूहों के कल्याण के "
                   "लिए। ‘लेभिरे’ (उन्होंने पाया) वही क्रिया है जो श्लोक २९ में ‘परमं "
                   "शर्म लेभिरे’ में आई थी; वहाँ ऋषि कर्ता थे, यहाँ तन्त्र। ‘परमर्षिभिः’ = "
                   "परम + ऋषिभिः, और ‘-भिः’ ‘द्वारा’ का अर्थ देता है। टिप्पणी में ‘भवाय’ के "
                   "स्थान पर ‘भावाय’ पाठभेद है।"),
    "hook": "तन्त्र + परम ऋषियों की स्वीकृति → पृथ्वी पर प्रतिष्ठा, प्राणियों के कल्याण के लिए।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The treatises were approved by the supreme sages. What does the verse say became of them?",
            ("They gained a firm standing on earth", "प्रतिष्ठां भुवि लेभिरे says this."),
            [("They were lost", "The verse speaks of standing, not loss."),
             ("They were kept secret in heaven", "The standing is on earth (भुवि)."),
             ("They were handed over to Indra", "Indra is not in this verse.")],
            "The treatises gained a firm standing on earth.",
            "Approved treatises → a firm standing on earth."),
        match(1, "Match each word of the verse to its meaning.",
              [["तन्त्राणि", "treatises"], ["अनुमतानि", "approved"],
               ["भुवि", "on earth"], ["भूतसङ्घानाम्", "of the multitudes of beings"]],
              "These words say what, how, where and for whom.",
              "तन्त्राणि = treatises; अनुमतानि = approved; भुवि = on earth; भूतसङ्घानाम् = of the multitudes of beings."),
        fill(2, "The word meaning 'on earth' is ____ (type it in Devanagari).",
             ["भुवि"],
             "भुवि tells where the treatises gained their standing.",
             "भुवि ends in -इ, the locative: 'on earth'. It contrasts with दिवि ('in heaven') in verse 36.",
             "भुवि = on earth."),
        mcq("discriminate", 3, "Which is the right split of तानि चानुमतान्येषाम्?",
            ("तानि + च + अनुमतानि + एषाम्",
             "च + अ joins as चा, and the इ of अनुमतानि before ए becomes य्."),
            [("तानि + चानु + मतानि + एषाम्", "चानु and मतानि are not words here."),
             ("ताना + इचानुमतानि + एषाम्", "इचानुमतानि is not a word."),
             ("तानि + च + अनुमतान् + येषाम्", "The word is एषाम् ('of these'), not येषाम्.")],
            "तानि चानुमतान्येषाम् = तानि ('those') + च ('and') + अनुमतानि ('approved') + एषाम् ('of these').",
            "तानि + च + अनुमतानि + एषाम्."),
        mcq("apply", 4,
            "Who approved the treatises, and which word shows it?",
            ("The supreme sages; परमर्षिभिः, with -भिः meaning 'by'",
             "-भिः is the ending for 'by', so the supreme sages are the approvers."),
            [("The disciples; एषाम्", "एषाम् means 'of these', naming the owners of the treatises."),
             ("The earth; भुवि", "भुवि means 'on earth', the place where they stand."),
             ("The beings; भूतसङ्घानाम्", "This means 'of the multitudes of beings', the ones who benefit.")],
            "परमर्षिभिः (-भिः = by) names the approvers: the supreme sages.",
            "-भिः = by (the agent)."),
        mcq("transfer", 5,
            "An invented line reads शिष्याः कीर्तिं लेभिरे. By the pattern प्रतिष्ठां लेभिरे, who obtained what?",
            ("The pupils obtained fame", "शिष्याः (-आः) is the doer; कीर्तिम् (-म्) is what was obtained."),
            [("Fame obtained the pupils", "The endings are the other way round."),
             ("The pupils gave fame", "लेभिरे means 'they obtained', not 'they gave'."),
             ("The pupils lost fame", "लेभिरे means 'they obtained', not 'they lost'.")],
            "The same pattern as प्रतिष्ठां लेभिरे: the thing obtained is accusative (here -म्); the doer is nominative.",
            "Doer (nominative) + thing obtained (accusative) + लेभिरे.",
            teaches="With लेभिरे ('they obtained'), the accusative word (e.g. प्रतिष्ठाम्) is what was obtained; the nominative is who obtained."),
    ],
}


NOTES_HI = {
    "31": ("पाठभेद: ‘भेलश्च’ की जगह ‘भेडश्च’ (भेड); भेल और भेड एक ही नाम की दो वर्तनी "
           "मानी गई हैं। संधि: जगृहुः + तत् → जगृहुस्तत्; तत् + मुनेः → तन्मुनेः; "
           "मुनेः + वचः → मुनेर्वचः। ‘तन्मुनेर्वचः’ को ‘तत् + मुनेः + वचः’ पढ़ा गया है।"),
    "32": ("‘बुद्धेर्विशेषः’ का भाव टिप्पणी में अग्निवेश की श्रेष्ठ बुद्धि बताया गया है। "
           "‘प्रथमम्’ को क्रियाविशेषण (‘सबसे पहले’) या ‘तन्त्रस्य’ के साथ विशेषण "
           "(‘पहले तन्त्र का कर्ता’) पढ़ा जा सकता है। संधि जाँची हैं: बुद्धेः + विशेषः → "
           "बुद्धेर्विशेषः; विशेषः + तत्र → विशेषस्तत्र; न + उपदेशान्तरम् → नोपदेशान्तरम्; "
           "यतः + अभवत् → यतो ऽभवत्।"),
    "33": ("‘कृतानि च’ श्रावयामासुः का कर्म है और ‘आत्रेयम्’ वह व्यक्ति जिसे सुनवाया गया "
           "(प्रेरणार्थक धातु का द्विकर्मक प्रयोग)। ‘सर्षिसङ्घम्’ = स + ऋषिसङ्घम् (अ + ऋ → अर्)। "
           "श्लोक ३० की टिप्पणी पुनर्वसु और आत्रेय को एक मानती है; यह श्लोक केवल "
           "‘आत्रेयम्’ नाम देता है।"),
    "34": ("पाठ में ‘प्रहृष्टास्त ऽनुमेनिरे’ छपा है; अपेक्षित रूप ‘प्रहृष्टास्ते ऽनुमेनिरे’ है "
           "(प्रहृष्टाः + ते, फिर ते + अनुमेनिरे → ते ऽनुमेनिरे), यहाँ ‘ए’ छूटा लगता है। "
           "देवनागरी पाठ में भी वही रूप है। ‘पुण्यकर्मणाम्’ को ‘सूत्रणम्’ के कर्ता (रचने वाले शिष्य) "
           "के लिए पढ़ा गया है; उसे ‘अर्थानाम्’ का विशेषण भी माना जा सकता है।"),
    "35": ("‘सर्व’ = ‘सर्वे’ (स्वर से पहले ‘ए’ → ‘अ’)। ‘साधु भूतेष्वनुक्रोशः’ को ‘साधु! प्राणियों पर "
           "अनुकम्पा है’ या ‘प्राणियों पर (आपकी) अनुकम्पा उत्तम है’ दोनों पढ़ा जा सकता है। "
           "‘सर्वभूतहितैषिणः’ को ऋषियों (प्रथमा) या ‘तान्’ (द्वितीया) के साथ पढ़ा जा सकता है। "
           "संधि: अस्तुवन् + तान् + च → अस्तुवंस्तांश्च; हित + एषिणः → हितैषिणः; इति + उच्चैः → इत्युच्चैः।"),
    "36": ("पाठ में ‘परमर्षीणं’ छपा है; षष्ठी बहुवचन का रूप ‘परमर्षीणाम्’ है, यहाँ दीर्घ ‘आ’ "
           "छूटा लगता है (देवनागरी पाठ में भी वही रूप)। छन्द इससे तय नहीं होता, क्योंकि "
           "अनुस्वार से अक्षर वैसे भी गुरु है। ‘परमर्षीणाम्’ को ‘शब्दम्’ के साथ (परम ऋषियों का शब्द) "
           "पढ़ा गया है। ‘शुश्रुवुः’ और ‘मुमुदिरे’ दोनों परोक्ष भूत के रूप हैं।"),
    "37": ("पाठभेद: ‘अन्ववादयत्’ की जगह ‘-नादयत्’ (अन्वनादयत्, ‘गुँजाया’); टिप्पणी में कहा गया "
           "है कि ‘-नादयत्’ अधिक स्वाभाविक अर्थ देता है, ‘अन्ववादयत्’ सम्भव पर असामान्य। "
           "‘भूतैः’ का अर्थ प्राणी या आकाशीय जीव दोनों हो सकता है। संधि: साधु + इति → साध्विति; "
           "लोकान् + त्रीन् → लोकांस्त्रीन्; हर्षात् + भूतैः → हर्षाद्भूतैः; भूतैः + उदीरितः → भूतैरुदीरितः।"),
    "38": ("‘शिवः’ यहाँ वायु का विशेषण है। ‘सजलाः’ को ‘कुसुमवृष्टयः’ का विशेषण (जल-सहित "
           "पुष्प-वर्षा) पढ़ा गया है। संधि: शिवः + वायुः → शिवो वायुः; वायुः + ववौ → वायुर्ववौ; "
           "सर्वाः + भाभिः → सर्वा भाभिः; उन्मीलिताः + दिशः → उन्मीलिता दिशः; "
           "सजलाः + च + एव → सजलाश्चैव।"),
    "39": ("‘क्षमादया’ दो शब्द (क्षमा, दया) हैं जो बिना रिक्त स्थान के लिखे गए हैं, संधि का "
           "परिवर्तन नहीं; ‘क्षमा + आदयः’ नहीं, क्योंकि सूची के सब नाम स्त्रीलिंग हैं। "
           "संधि: अथ + अग्निवेश… → अथाग्निवेश…; विविशुः + ज्ञानदेवताः → विविशुर्ज्ञानदेवताः; "
           "स्मृतिः + मेधा → स्मृतिर्मेधा। ‘विविशुः’ परोक्ष भूत का बहुवचन रूप है।"),
    "40": ("पाठभेद: ‘भवाय’ की जगह ‘भावाय’; ‘भव’ का अर्थ ‘अस्तित्व’ भी हो सकता है, पर "
           "‘कल्याण’ यहाँ प्रसंग से अधिक ठीक बैठता है। ‘एषाम्’ को ‘तन्त्राणि’ के साथ (इनके तन्त्र) "
           "या ‘परमर्षिभिः’ के साथ (इन परम ऋषियों द्वारा) पढ़ा जा सकता है। संधि: च + अनुमतानि → "
           "चानुमतानि; अनुमतानि + एषाम् → अनुमतान्येषाम्; परम + ऋषिभिः → परमर्षिभिः।"),
}


AIDS = {
    "31": {
        "frame": "कौन: छह शिष्य · क्या: मुनि का वचन · क्रिया: जगृहुः (ग्रहण किया)।",
        "letters": "अ-भे-ज-प-हा-क्षा (अग्निवेश, भेल, जतूकर्ण, पराशर, हारीत, क्षारपाणि)।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["अग्निवेश", "भेल", "जतूकर्ण", "पराशर"]},
            {"label": "दूसरी पंक्ति", "items": ["हारीत", "क्षारपाणि"]}]},
        "sandhi": "विसर्ग + च → श्च: अग्निवेशः + च → अग्निवेशश्च; भेलः + च → भेलश्च। "
                  "जगृहुः + तत् → जगृहुस्तत् (विसर्ग + त → स्त); तत् + मुनेः → तन्मुनेः "
                  "(त् + म → न्म); मुनेः + वचः → मुनेर्वचः (विसर्ग → र् घोष ‘व’ से पहले)।",
        "contrast": "जग्राह (श्लोक ४: एक ने ग्रहण किया) ↔ जगृहुः (यहाँ: छह ने ग्रहण किया) — "
                    "धातु एक (√ग्रह्), वचन अलग।",
        "chunks": "अग्निवेशश्च भेलश्च | जतूकर्णः पराशरः ‖ हारीतः क्षारपाणिश्च | "
                  "जगृहुस्तन्मुनेर्वचः।",
    },
    "32": {
        "frame": "कौन: अग्निवेश · क्या: पहले तन्त्र-कर्ता · क्यों (यतः): बुद्धि की "
                 "विशेषता; उपदेश सबको एक-सा।",
        "seesaw": "बुद्धि का भेद ↔ उपदेश का अभेद: भेद बुद्धि (बुद्धेः) में है, उपदेश "
                  "(मुनेः) में नहीं (न + अन्तरम्)।",
        "chain": "उपदेश एक-सा → बुद्धि में भेद → इसीलिए अग्निवेश पहले तन्त्र-कर्ता।",
        "sandhi": "बुद्धेः + विशेषः → बुद्धेर्विशेषः (विसर्ग → र् घोष ‘व’ से पहले); "
                  "विशेषः + तत्र → विशेषस्तत्र (विसर्ग + त → स्त); न + उपदेशान्तरम् → "
                  "नोपदेशान्तरम् (अ + उ → ओ); यतः + अभवत् → यतो ऽभवत् (विसर्ग → ओ, "
                  "अगले ‘अ’ की जगह ऽ)।",
        "contrast": "‘बुद्धेः विशेषः’ (भेद है) ↔ ‘न उपदेशान्तरम्’ (भेद नहीं): एक ही श्लोक के "
                    "दो पलड़े, दोनों अलग विषयों के बारे में।",
        "chunks": "बुद्धेर्विशेषस्तत्रासीत् | नोपदेशान्तरं मुनेः ‖ तन्त्रस्य कर्ता प्रथमम् | "
                  "अग्निवेशो यतो ऽभवत्।",
    },
    "33": {
        "frame": "कौन: भेल आदि · क्या: अपना-अपना तन्त्र रचा · किसे सुनाया: आत्रेय, "
                 "ऋषि-समूह सहित।",
        "chain": {"steps": ["भेल आदि: अपना अपना तन्त्र रचा",
                            "रचनाएँ तैयार (कृतानि)",
                            "आत्रेय + ऋषि-समूह को सुनाया"]},
        "sandhi": "विसर्ग + च → श्च: भेलादयः + चक्रुः → भेलादयश्चक्रुः। विसर्ग → र् "
                  "(स्वर से पहले): श्रावयामासुः + आत्रेयम् → श्रावयामासुरात्रेयम्। "
                  "अ + ऋ → अर्: स + ऋषिसङ्घम् → सर्षिसङ्घम्।",
        "anchors": "श्रावयामासुः ← √श्रु (सुनना) का प्रेरणार्थक: ‘सुनवाया’ · श्रावयति / "
                   "श्रुत्वा (श्लोक ३४) / शुश्रुवुः (श्लोक ३६) एक ही धातु के परिवार में।",
        "contrast": "चक्रुः (उन्होंने रचा) ↔ श्रावयामासुः (उन्होंने सुनवाया): पहली क्रिया "
                    "का फल दूसरी का कर्म बनता है (कृतानि)।",
        "chunks": "अथ भेलादयश्चक्रुः | स्वं स्वं तन्त्रं कृतानि च ‖ श्रावयामासुरात्रेयं | "
                  "सर्षिसङ्घं सुमेधसः।",
    },
    "34": {
        "frame": "कौन: ऋषि · क्या सुना: अर्थों का सूत्रण · क्या किया: प्रसन्न होकर "
                 "अनुमोदन किया।",
        "chain": "श्रुत्वा (सुनकर) → प्रहृष्टाः (प्रसन्न) → ‘यथावत् सूत्रितम्’ इति → अनुमेनिरे "
                 "(माना)।",
        "pegs": "अनुमेनिरे = मुहर लगाना (मेरा बनाया चित्र): रचना पर ऋषियों की मुहर, और "
                "मुहर के साथ पूरी बात ‘इति’ पर बन्द।",
        "anchors": "अनुमेनिरे ← अनु + √मन् (मानना): अनुमोदन, मान्य · प्रहृष्ट ← प्र + "
                   "√हृष् (हर्ष) · सूत्रण ← सूत्र।",
        "sandhi": "म् + स्वर सीधा जुड़ता है: सूत्रणम् + अर्थानाम् → सूत्रणमर्थानाम्; "
                  "अर्थानाम् + ऋषयः → अर्थानामृषयः। (छपे पाठ ‘प्रहृष्टास्त ऽ…’ में अपेक्षित "
                  "‘प्रहृष्टास्ते ऽ…’: प्रहृष्टाः + ते → प्रहृष्टास्ते।)",
        "contrast": "श्रुत्वा (श्लोक ३४, पहले की क्रिया) और बुद्ध्वा (श्लोक ३): दोनों "
                    "‘-त्वा’ वाले रूप; दोनों के कर्ता मुख्य क्रिया (अनुमेनिरे / उपागमत्) के कर्ता ही हैं।",
        "chunks": "श्रुत्वा सूत्रणमर्थानाम् | ऋषयः पुण्यकर्मणाम् ‖ यथावत्सूत्रितमिति | "
                  "प्रहृष्टास्ते [पाठ: प्रहृष्टास्त] ऽनुमेनिरे।",
    },
    "35": {
        "frame": "कौन: सब ऋषि · क्या किया: प्रशंसा · क्या कहा: ‘साधु! भूतों पर अनुक्रोश’, "
                 "ऊँचे स्वर में, एक साथ।",
        "chain": "सुना (३४) → प्रशंसा की (अस्तुवन्) → एक साथ बोले (अब्रुवन् समम्): साधु।",
        "sandhi": "ए + स्वर → अ + स्वर: सर्वे + एव → सर्व एव। न् + त/च → ं + स्त/श्च: "
                  "अस्तुवन् + तान् + च → अस्तुवंस्तांश्च। अ + ए → ऐ: हित + एषिणः → "
                  "हितैषिणः। इ + उ → यु: इति + उच्चैः → इत्युच्चैः। विसर्ग → र्: "
                  "उच्चैः + अब्रुवन् → उच्चैरब्रुवन्।",
        "anchors": "अनुक्रोश = दया (श्लोक ७ में भी) · हितैषी = हित + एषी (हित चाहने वाला) · "
                   "साधु = भला, ठीक।",
        "contrast": "अनुक्रोश श्लोक ७ में ऋषियों की प्रेरणा था; श्लोक ३५ में वही शब्द उनकी "
                    "प्रशंसा का विषय है। शब्द वही; वही बात है या नहीं, यह श्लोक नहीं कहता।",
        "chunks": "सर्व एवास्तुवंस्तांश्च | सर्वभूतहितैषिणः ‖ साधु भूतेष्वनुक्रोश | "
                  "इत्युच्चैरब्रुवन् समम्।",
    },
    "36": {
        "frame": "कौन: देवर्षि, देवताओं सहित · कहाँ: दिवि (स्वर्ग) · क्या: पुण्य शब्द सुना · "
                 "फल: बहुत प्रसन्न।",
        "chain": "ऋषियों का शब्द (३५) → स्वर्ग में सुना (शुश्रुवुः) → सुनकर प्रसन्न (मुमुदिरे)।",
        "sandhi": "अ + ऋ → अर्: देव + ऋषयः → देवर्षयः; परम + ऋषीणाम् → परमर्षीणाम्। "
                  "स + अमराः → सामराः (अ + अ → आ)।",
        "anchors": "श्रुत्वा / शुश्रुवुः / श्रावयामासुः: तीनों √श्रु (सुनना) के रूप · मुमुदिरे ← "
                   "√मुद् (प्रसन्न होना): मोद।",
        "contrast": "शुश्रुवुः (उन्होंने सुना: मुख्य क्रिया) ↔ श्रुत्वा (सुनकर: पहले की क्रिया): "
                    "धातु एक, पर एक मुख्य क्रिया है और दूसरी उससे पहले की।",
        "chunks": "तं पुण्यं शुश्रुवुः शब्दं | दिवि देवर्षयः स्थिताः ‖ सामराः परमर्षीणां | "
                  "श्रुत्वा मुमुदिरे परम्।",
    },
    "37": {
        "chain": "साधु! (३५) → स्वर्ग में सुना (३६) → आकाश में ‘अहो साधु’ का घोष, तीनों लोकों में (३७)।",
        "frame": "कौन: भूत (प्राणी/आकाशीय जीव) · क्या: ‘अहो, साधु!’ का घोष · कहाँ: नभसि · "
                 "क्यों: हर्ष · असर: तीनों लोक गूँजे।",
        "story": "भूतों के हर्ष से → आकाश में कोमल-गम्भीर घोष उठा → तीनों लोक "
                 "गूँज उठे।",
        "sandhi": "उ + इ → व् + इ: साधु + इति → साध्विति। न् + त → ं + स्त: लोकान् + "
                  "त्रीन् → लोकांस्त्रीन्। त् + भ → द्भ: हर्षात् + भूतैः → हर्षाद्भूतैः। "
                  "विसर्ग → र् (स्वर से पहले): भूतैः + उदीरितः → भूतैरुदीरितः।",
        "anchors": "निर्घोष = निः + घोष (गूँजती आवाज़) · उदीरित ← उत् + √ईर् (उठाना, बोलना) · "
                   "गम्भीर = गहरा।",
        "contrast": "श्लोक ३५ में ऋषियों ने ‘साधु’ कहा; श्लोक ३७ में आकाश में ‘अहो साधु’ गूँजा। "
                    "शब्द साधु दोनों में है; ३५ में ऋषि बोले, ३७ में ‘भूतैः’ (वे कौन, श्लोक नहीं कहता)।",
        "chunks": "अहो साध्विति निर्घोषो | लोकांस्त्रीनन्ववादयत् ‖ नभसि स्निग्धगम्भीरो | "
                  "हर्षाद्भूतैरुदीरितः।",
    },
    "38": {
        "chain": "वायु बही → दिशाएँ जगमगाईं → जल सहित फूल बरसे।",
        "story": "घोष गूँजा → मंगलकारी हवा चली → दिशाएँ प्रकाश से खुल गईं → आकाश से फूलों "
                 "की बौछार, जल की बूँदों सहित।",
        "pegs": "तीन संकेत = हवा का झोंका, दीया, फूलों की बौछार (मेरा बनाया चित्र)।",
        "sandhi": "विसर्ग → ओ (घोष से पहले, अ के बाद): शिवः + वायुः → शिवो वायुः। विसर्ग → "
                  "र्: वायुः + ववौ → वायुर्ववौ। -आः + घोष → -आ: सर्वाः + भाभिः → सर्वा भाभिः; "
                  "उन्मीलिताः + दिशः → उन्मीलिता दिशः। विसर्ग + च → श्च; च + एव → चैव: "
                  "सजलाः + च + एव → सजलाश्चैव।",
        "contrast": "शिवः यहाँ विशेषण है (मंगलकारी वायु), देवता नहीं; सजलाः = स + जल: "
                    "‘जल के साथ’।",
        "chunks": "शिवो वायुर्ववौ सर्वा | भाभिरुन्मीलिता दिशः ‖ निपेतुः सजलाश्चैव | "
                  "दिव्याः कुसुमवृष्टयः।",
    },
    "39": {
        "frame": "कौन: ज्ञानदेवताएँ · किनमें: अग्निवेश आदि शिष्य · क्रिया: विविशुः "
                 "(प्रवेश किया) · सूची: आठ नाम।",
        "diagram": {"groups": [
            {"label": "आठ ज्ञानदेवताएँ",
             "items": ["बुद्धिः", "सिद्धिः", "स्मृतिः", "मेधा", "धृतिः", "कीर्तिः",
                       "क्षमा", "दया"]}]},
        "letters": "बु-सि-स्मृ-मे-धृ-की-क्ष-द (बुद्धि, सिद्धि, स्मृति, मेधा, धृति, कीर्ति, क्षमा, दया)।",
        "sandhi": "अ + अ → आ: अथ + अग्निवेश… → अथाग्निवेश…। विसर्ग → र् (घोष से पहले): "
                  "विविशुः + ज्ञानदेवताः → विविशुर्ज्ञानदेवताः; स्मृतिः + मेधा → स्मृतिर्मेधा।",
        "anchors": "अग्निवेशप्रमुखान् = अग्निवेश + प्रमुख (मुखिया) · विविशुः ← √विश् (प्रवेश): "
                   "प्रवेश · कीर्ति = यश · क्षमा-दया दो अलग नाम।",
        "contrast": "मेधा (धारण करने वाली बुद्धि) ↔ बुद्धिः (समझ): सूची में दोनों अलग नाम हैं। "
                    "‘क्षमादया’ एक शब्द-रूप में दो नाम हैं, ‘क्षमा आदि’ नहीं।",
        "chunks": "अथाग्निवेशप्रमुखान् | विविशुर्ज्ञानदेवताः ‖ बुद्धिः सिद्धिः स्मृतिर्मेधा | "
                  "धृतिः कीर्तिः क्षमादया।",
    },
    "40": {
        "frame": "क्या: अनुमोदित तन्त्र · किसने माना: परम ऋषि · फल: भुवि प्रतिष्ठा · "
                 "किसके लिए: भूतसङ्घों के कल्याण के लिए।",
        "chain": "तन्त्र रचे (३३) → परम ऋषियों ने माना (३४, ४०) → पृथ्वी पर प्रतिष्ठा (४०)।",
        "sandhi": "अ + अ → आ: च + अनुमतानि → चानुमतानि। इ + ए → ये: अनुमतानि + एषाम् → "
                  "अनुमतान्येषाम्। अ + ऋ → अर्: परम + ऋषिभिः → परमर्षिभिः।",
        "anchors": "प्रतिष्ठा ← प्रति + √स्था (टिकना, स्थापित होना) · अनुमत ← अनु + √मन् "
                   "(अनुमेनिरे, श्लोक ३४, वही धातु) · भूतसङ्घ = भूत + सङ्घ (प्राणि-समूह)।",
        "contrast": "लेभिरे (श्लोक २९): ऋषियों ने परम सुख पाया ↔ लेभिरे (श्लोक ४०): तन्त्रों ने "
                    "प्रतिष्ठा पाई। क्रिया वही, कर्ता और फल अलग।",
        "chunks": "तानि चानुमतान्येषां | तन्त्राणि परमर्षिभिः ‖ भवाय भूतसङ्घानां | "
                  "प्रतिष्ठां भुवि लेभिरे।",
    },
}

IMAGE_SPECS = {
    ("31", "diagram"): {
        "file": "disciples-31.svg",
        "alt": "Two columns listing the six disciples of verse 31: four names of the first line (Agniveśa, Bhela, Jatūkarṇa, Parāśara) and two of the second line (Hārīta, Kṣārapāṇi)",
        "type": "split",
        "title": "श्लोक ३१: छह शिष्य",
        "cols": [["पहली पंक्ति", ["अग्निवेश", "भेल", "जतूकर्ण", "पराशर"]],
                 ["दूसरी पंक्ति", ["हारीत", "क्षारपाणि"]]],
    },
    ("33", "chain"): {
        "file": "chain-33.svg",
        "alt": "Three boxes joined by arrows: Bhela and the others compose their own treatises; the works are ready; they are recited to Ātreya with the assembly of sages",
        "type": "chain",
        "title": "श्लोक ३३: रचना से श्रवण तक",
        "steps": ["भेल आदि: अपना अपना तन्त्र रचा",
                  "रचनाएँ तैयार (कृतानि)",
                  "आत्रेय + ऋषि-समूह को सुनाया"],
    },
    ("39", "diagram"): {
        "file": "deities-39.svg",
        "alt": "Two columns listing the eight deities of knowledge in verse 39 in verse order: Intellect, Accomplishment, Memory, Retentive intelligence; then Fortitude, Fame, Forbearance, Compassion",
        "type": "split",
        "title": "श्लोक ३९: आठ ज्ञानदेवताएँ",
        "cols": [["पहली चार", ["बुद्धिः", "सिद्धिः", "स्मृतिः", "मेधा"]],
                 ["अगली चार", ["धृतिः", "कीर्तिः", "क्षमा", "दया"]]],
    },
}
