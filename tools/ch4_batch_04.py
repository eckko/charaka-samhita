from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}


def _g(label, line):
    """A diagram group made of the printed words of one line, in order."""
    return {"label": label, "items": line.split()}


# --------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "नैतानि भगवन् पञ्च कषायशतानि पूर्यन्ते",
    "question": "Who objects in unit 21, to whom, and what is his reason?",
    "rule": ("एवंवादिनं भगवन्तमात्रेयमग्निवेश उवाच … तानि तानि ह्येवाङ्गान्युपप्लवन्ते = "
             "Agniveśa says to Ātreya: these five hundred kaṣāyas are not completed, for "
             "those very members (aṅga) recur in those various great kaṣāyas."),
    "limits": ("This unit only states the objection; Ātreya's reply begins in unit 22. The last "
               "token महाकषायेष्वति is printed with अति; the data suggests इति (end of the "
               "quotation) was meant. The word अङ्ग is rendered 'member' and not explained "
               "further."),
    "explain_hi": ("यहाँ अग्निवेश अपनी शंका रखते हैं। ‘एवंवादिनम्’ का अर्थ ‘ऐसा कहने वाले’ है, "
                   "और ‘उवाच’ का अर्थ ‘कहा’। अग्निवेश कहते हैं: ‘भगवन्! ये पाँच सौ कषाय पूरे "
                   "नहीं होते’ (‘न … पूर्यन्ते’)। कारण वे यह देते हैं कि ‘वे-वे ही अङ्ग’ "
                   "(अवयव) उन-उन महाकषायों में बार-बार आ जाते हैं। ‘तानि तानि’ और ‘तेषु तेषु’ "
                   "में शब्द का दोहराव ‘उन-उन (अलग-अलग)’ का भाव देता है। ‘उपप्लवन्ते’ का "
                   "शाब्दिक अर्थ ‘ऊपर तैरते हैं’ है, यहाँ ‘बार-बार आते हैं’। यह इकाई प्रश्न "
                   "मात्र है; उत्तर अगली इकाई से शुरू होता है।"),
    "hook": "अग्निवेश की शंका: पाँच सौ कषाय पूरे नहीं होते, क्योंकि वे-वे ही अङ्ग उन-उन महाकषायों में बार-बार आते हैं।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In unit 21, who speaks to whom?",
            ("Agniveśa speaks to Ātreya",
             "अग्निवेश उवाच: Agniveśa is the speaker, and Ātreya is addressed as भगवन्."),
            [("Ātreya speaks to Agniveśa",
              "That is unit 22; here Ātreya is the one spoken to (भगवन्तमात्रेयम्, accusative)."),
             ("Ātreya speaks to the whole assembly of sages",
              "No assembly is named; the unit has one speaker and one listener."),
             ("The narrator speaks about both without quoting them",
              "The unit quotes Agniveśa's words directly (the quotation marker is doubtful, see the note).")],
            "अग्निवेशः is the subject of उवाच, and Ātreya is in the accusative as the one addressed.",
            "X-म् (accusative) + Y उवाच = Y said to X."),
        match(1, "Match each word of Agniveśa's sentence to its meaning.",
              [["न", "not"], ["एतानि", "these"],
               ["कषायशतानि", "hundreds of kaṣāyas"],
               ["पूर्यन्ते", "are filled up, are completed"]],
              "These words make up the objection 'these hundreds are not completed'.",
              "न = not; एतानि = these; कषायशतानि = hundreds of kaṣāyas; पूर्यन्ते = are completed."),
        fill(2, "The verb meaning 'are completed' in Agniveśa's sentence is ____ (type it in Devanagari).",
             ["पूर्यन्ते"],
             "Agniveśa says नैतानि … पूर्यन्ते: these are not completed.",
             "पूर्यन्ते is third person plural present passive of √पॄ: 'they are filled up'. With न it denies that the five hundred reach completion.",
             "पूर्यन्ते = are filled up, completed; न … पूर्यन्ते = are not completed."),
        mcq("discriminate", 3, "Which is the right split of नैतानि?",
            ("न + एतानि: अ + ए joins as ऐ",
             "न ends in अ and एतानि begins with ए; अ + ए gives ऐ, so नैतानि."),
            [("ना + एतानि", "The negative is न, with short अ."),
             ("नै + तानि", "नै is not a word; तानि is not the word here."),
             ("न + तानि", "That would lose the ए of एतानि.")],
            "नैतानि = न (not) + एतानि (these).",
            "अ + ए → ऐ: न + एतानि → नैतानि."),
        multi("apply", 4, "Which statements does unit 21 itself make?",
              [("Agniveśa addresses Ātreya as भगवन्", "Right: भगवन्! is a vocative in his sentence."),
               ("The five hundred kaṣāyas are not completed", "Right: नैतानि … पूर्यन्ते."),
               ("The reason given is that the same members recur in the great kaṣāyas",
                "Right: तानि तानि ह्येवाङ्गान्युपप्लवन्ते तेषु तेषु महाकषायेषु."),
               ("Ātreya agrees with him", "Ātreya's reply begins only in unit 22."),
               ("There are fifty great kaṣāyas", "The number fifty is not stated in this unit.")],
              [0, 1, 2],
              "The unit gives the address, the objection and its reason; Ātreya's reply and the number fifty are elsewhere.",
              "Unit 21: objection (not completed) + reason (same members recur)."),
        mcq("transfer", 5,
            "An invented phrase: तानि तानि फलानि. By the pattern of तेषु तेषु, what does it mean?",
            ("Those various fruits, each one in turn",
             "A repeated word, as in तानि तानि and तेषु तेषु, gives 'those various / each of those'."),
            [("Only one fruit",
              "The plural -आनि and the doubling point to many, not one."),
             ("No fruits at all",
              "There is no negative न in the phrase."),
             ("Fruits of fifty kinds",
              "No number is stated in the phrase.")],
            "Doubling a word gives 'those and those', i.e. 'those various': तानि तानि फलानि = those various fruits.",
            "Doubled word = 'each / the various'.",
            teaches="Repeating a pronoun, as in तानि तानि or तेषु तेषु, spreads it over many items: 'those various ones'."),
    ],
}

# --------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "तमुवाच भगवानात्रेयः",
    "question": "How does Ātreya begin his answer, and what does he say about Agniveśa's way of looking?",
    "rule": ("तमुवाच भगवानात्रेयः --- नैतदेवं बुद्धिमता द्रष्टव्यमग्निवेश = The venerable "
             "Ātreya said to him: an intelligent person should not look at this in this "
             "way, Agniveśa."),
    "limits": ("This unit gives only the first words of the reply: a rejection of that "
               "way of looking. It does not yet say what the right way is, nor name "
               "any number."),
    "explain_hi": ("यह आत्रेय के उत्तर का आरम्भ है। ‘तम्’ (उनसे) और ‘उवाच’ (कहा) बताते हैं कि "
                   "वे अग्निवेश से बोल रहे हैं, और अन्त में ‘अग्निवेश’ सम्बोधन है। मुख्य वाक्य: "
                   "‘न एतत् एवं बुद्धिमता द्रष्टव्यम्’: बुद्धिमान् को इसे इस प्रकार नहीं देखना "
                   "चाहिए। ‘बुद्धिमता’ तृतीया है (बुद्धिमान् के द्वारा) और ‘द्रष्टव्यम्’ "
                   "विधि-कृदन्त (gerundive) है, ‘देखा जाना चाहिए’; दोनों मिलकर ‘बुद्धिमान् को "
                   "देखना चाहिए’ का भाव देते हैं। इस इकाई में सही दृष्टि नहीं बताई गई, केवल इस दृष्टि का निषेध है।"),
    "hook": "आत्रेय: बुद्धिमान् को इसे ऐसे नहीं देखना चाहिए, अग्निवेश (न + एतत् + एवम्; बुद्धिमता + द्रष्टव्यम्)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In unit 22, who is speaking, and who is addressed by name?",
            ("Ātreya speaks; Agniveśa is addressed",
             "भगवानात्रेयः is the subject of उवाच, and अग्निवेश at the end is the vocative."),
            [("Agniveśa speaks; Ātreya is addressed",
              "That was unit 21; here the speaker is Ātreya."),
             ("Ātreya speaks; no one is addressed by name",
              "अग्निवेश is a vocative at the end of the unit."),
             ("A third sage speaks to both",
              "No third person is named.")],
            "Ātreya replies to Agniveśa, whom he names at the end.",
            "तम् उवाच X = X said to him; the final vocative names the listener."),
        match(1, "Match each word of unit 22 to its meaning.",
              [["तम्", "to him"], ["उवाच", "said"],
               ["बुद्धिमता", "by an intelligent person"],
               ["द्रष्टव्यम्", "to be seen, to be regarded"]],
              "These words say who is addressed, what is done and by whom.",
              "तम् = to him; उवाच = said; बुद्धिमता = by an intelligent person; द्रष्टव्यम् = to be seen."),
        fill(2, "Ātreya calls his listener by the vocative ____ (type the name in Devanagari).",
             ["अग्निवेश"],
             "The unit ends with अग्निवेश, the vocative.",
             "A vocative has no case ending here: अग्निवेश (not अग्निवेशः) is the form used to call him.",
             "अग्निवेश = 'O Agniveśa', the vocative without visarga."),
        mcq("discriminate", 3, "Which is the right split of नैतदेवं?",
            ("न + एतत् + एवम्",
             "न + एतत् gives नैतत् (अ + ए → ऐ); the final त् of एतत् becomes द् before the vowel ए, giving नैतदेवम्."),
            [("ना + एतद् + एवम्", "The negative is न, with short अ."),
             ("नै + तदेवम्", "नै and तदेवम् are not the words used here."),
             ("न + एतम् + एवम्", "The word is एतत् ('this', neuter), not एतम्.")],
            "नैतदेवं is न (not) + एतत् (this) + एवम् (in this way).",
            "अ + ए → ऐ; त् + vowel → द्: न + एतत् + एवम् → नैतदेवम्."),
        mcq("apply", 4,
            "What does Ātreya say an intelligent person should not do?",
            ("Look at this in this way",
             "नैतदेवं बुद्धिमता द्रष्टव्यम् = this is not to be regarded thus by the intelligent."),
            [("Ask any further question",
              "Nothing in the unit forbids asking questions."),
             ("Prepare a purgative",
              "No purgative or preparation is mentioned in this unit."),
             ("Praise the great kaṣāyas",
              "The unit says nothing about praising them.")],
            "द्रष्टव्यम् with न: 'is not to be seen' in this way.",
            "न + द्रष्टव्यम् = should not be looked at (in this way)."),
        mcq("transfer", 5,
            "An invented sentence: नैतदेवं वैद्येन कर्तव्यम्. By the pattern of बुद्धिमता द्रष्टव्यम्, what does it say?",
            ("A physician should not do this in this way",
             "The agent in the instrumental (वैद्येन) + a word in -तव्य = 'should be done by'; न negates it."),
            [("A physician has done this in this way",
              "-तव्य words express what should be done, not what has been done."),
             ("This should be done by no physician but by a patient",
              "No patient is mentioned in the sentence."),
             ("This is a physician's rule for doing it in this way",
              "The न makes it a prohibition, not a rule to do it.")],
            "Instrumental of the person + gerundive = 'X should do / see it'; with न it becomes 'should not'.",
            "Instrumental + gerundive (-तव्य) = what X should do.",
            teaches="An agent in the instrumental plus a word ending in -तव्य, as in बुद्धिमता द्रष्टव्यम्, says what that person should do (or, with न, should not)."),
    ],
}

# --------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "यतो यावन्ति यैर्द्रव्यैः",
    "question": "What does verse 23 say has been stated in brief, and what comes with it?",
    "rule": ("यतो यावन्ति यैर्द्रव्यैर्विरेचनशतानि षट् उक्तानि संग्रहेणेह तथैवैषां षडाश्रयाः = "
             "From which source, as many as, and with which substances, six hundred "
             "purgatives have been stated here in brief; and likewise their six bases."),
    "limits": ("The verse names no source, no substance and no base; it only recalls "
               "them. यतः can also mean 'because'; here it is taken as 'from which "
               "(source)'. The six bases are left uninterpreted in the data."),
    "explain_hi": ("यह अध्याय के श्लोक-सारांश का पहला श्लोक है; इससे पहले ‘तत्र श्लोकाः’ "
                   "(इस विषय में ये श्लोक हैं) आता है। श्लोक कहता है कि छह सौ विरेचन, "
                   "जिस (स्रोत) से, जितने और जिन द्रव्यों से बनते हैं, यहाँ ‘संक्षेप से’ "
                   "(संग्रहेण) कहे गए हैं, और वैसे ही इनके छह आश्रय भी। ‘यावन्ति’ का "
                   "अर्थ ‘जितने’ है और ‘उक्तानि’ ‘कहे गए’। ‘षडाश्रयाः’ = षट् + आश्रयाः, "
                   "यानी ‘छह आधार’; श्लोक उनके नाम नहीं देता (नाम पहले की इकाई ५ में आए हैं)।"),
    "hook": "छह सौ विरेचन संक्षेप में कहे गए (यतः, यावन्ति, यैर्द्रव्यैः) और उनके छह आश्रय भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 23 says that six hundred purgatives have been stated. In what manner?",
            ("In brief (संग्रहेण)",
             "संग्रहेणेह = संग्रहेण + इह: 'in brief, here'."),
            [("In great detail, one by one",
              "The word is संग्रहेण, 'in summary'; detail is not claimed."),
             ("With doses for each",
              "No dose is mentioned in the verse."),
             ("By one drug alone",
              "The verse says 'with which substances', plural (द्रव्यैः).")],
            "The verse says the six hundred are stated संग्रहेण, in brief.",
            "संग्रहेण = in brief; उक्तानि = stated."),
        match(1, "Match each word of verse 23 to its meaning.",
              [["षट्", "six"], ["उक्तानि", "stated"],
               ["संग्रहेण", "in brief, by summary"],
               ["आश्रयाः", "bases, supports"]],
              "These words carry the verse's claim: six hundred stated in brief, and six bases.",
              "षट् = six; उक्तानि = stated; संग्रहेण = in brief; आश्रयाः = bases."),
        fill(2, "The word meaning 'in brief' (instrumental case) in verse 23 is ____ (type it in Devanagari).",
             ["संग्रहेण"],
             "The verse has संग्रहेणेह, which is संग्रहेण + इह.",
             "संग्रहेण is an instrumental singular: 'by way of summary', i.e. 'in brief'.",
             "संग्रहेण = in brief (instrumental of संग्रह, 'summary')."),
        mcq("discriminate", 3, "Which is the right split of संग्रहेणेह?",
            ("संग्रहेण + इह: अ + इ joins as ए",
             "संग्रहेण ends in अ and इह begins with इ; अ + इ gives ए, so संग्रहेणेह."),
            [("संग्रहेणे + ह", "ह alone is not a word here; the word is इह."),
             ("संग्रहेण + एह", "एह is not the word; it is इह, 'here'."),
             ("संग्रह + इणेह", "इणेह is not a word.")],
            "संग्रहेणेह is संग्रहेण (in brief) + इह (here).",
            "अ + इ → ए: संग्रहेण + इह → संग्रहेणेह."),
        multi("apply", 4, "Which statements does verse 23 itself make?",
              [("Six hundred purgatives have been stated", "Right: षट् … विरेचनशतानि उक्तानि."),
               ("They have been stated in brief, here", "Right: संग्रहेणेह."),
               ("Their six bases are also mentioned", "Right: तथैवैषां षडाश्रयाः."),
               ("The verse lists the six bases", "It only says 'six bases'; no names are given."),
               ("The verse gives the dose of each purgative", "No dose appears in the verse.")],
              [0, 1, 2],
              "The verse recalls the number, the manner and the six bases, without listing them.",
              "Verse 23: 600 purgatives stated in brief + their six bases."),
        mcq("transfer", 5,
            "An invented phrase: यावन्ति द्रव्याणि उक्तानि. By the pattern of यावन्ति … शतानि उक्तानि, what does it say?",
            ("As many substances as have been stated",
             "यावन्ति means 'as many', and agrees with the plural द्रव्याणि; उक्तानि = stated."),
            [("Only one substance was stated",
              "यावन्ति and द्रव्याणि are plural."),
             ("Substances that were never stated",
              "उक्तानि means 'stated', not 'not stated'."),
             ("How few substances there are",
              "यावन्ति asks 'how many / as many', not 'how few'.")],
            "यावन्ति + plural noun + उक्तानि = 'as many as were stated'.",
            "यावन्ति = as many / how many (neuter plural).",
            teaches="यावन्ति is a neuter plural 'as many (as)'; it agrees with the plural noun it counts, as in यावन्ति … शतानि."),
    ],
}

# --------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "रसा लवणवर्ज्याश्च कषाय इति संज्ञिताः",
    "question": "Which tastes are called 'kaṣāya' in verse 24, and what follows from this?",
    "rule": ("रसा लवणवर्ज्याश्च कषाय इति संज्ञिताः तस्मात् पञ्चविधा योनिः कषायाणामुदाहृता = "
             "The tastes (rasa) excluding salt are termed 'kaṣāya'; therefore the source "
             "(yoni) of the kaṣāyas is declared fivefold."),
    "limits": ("The verse does not list the tastes; unit 6 names the five sources. "
               "Here कषाय is a class-name, not the astringent taste alone (the "
               "data's note). Why salt is left out is not said."),
    "explain_hi": ("यह श्लोक बताता है कि ‘कषाय’ नाम किन्हें दिया गया: नमक (लवण) को छोड़कर बाकी "
                   "रस ‘कषाय’ कहे गए हैं (‘कषाय इति संज्ञिताः’)। यहाँ ‘कषाय’ वर्ग का नाम है, "
                   "केवल कसैला स्वाद नहीं। इसी से (‘तस्मात्’ = इसलिए) कषायों की योनि "
                   "(उत्पत्ति-स्रोत) ‘पञ्चविध’ यानी पाँच प्रकार की बताई गई है। पाँच स्रोतों के नाम "
                   "(मधुर, अम्ल, कटु, तिक्त, कषाय) इस श्लोक में नहीं हैं; वे इकाई ६ में हैं। "
                   "श्लोक यह भी नहीं बताता कि लवण क्यों छोड़ा गया।"),
    "hook": "लवण को छोड़कर रस = ‘कषाय’ नाम; इसलिए कषायों की योनि पञ्चविध।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 24 calls the tastes 'kaṣāya' with one taste excluded. Which taste is excluded?",
            ("Salt (लवण)",
             "रसा लवणवर्ज्याः = the tastes excluding salt."),
            [("Sweet (मधुर)",
              "Unit 6 names the sweet kaṣāya among the five sources; sweet is not excluded."),
             ("Bitter (तिक्त)",
              "Unit 6 names the bitter kaṣāya among the five sources; it is not excluded."),
             ("Pungent (कटु)",
              "Unit 6 names the pungent kaṣāya among the five sources; it is not excluded.")],
            "लवणवर्ज्याः means 'excluding salt': salt is the taste left out.",
            "X-वर्ज्य = excluding X; लवणवर्ज्याः = excluding salt."),
        match(1, "Match each word of verse 24 to its meaning.",
              [["रसाः", "tastes"], ["लवणवर्ज्याः", "excluding salt"],
               ["संज्ञिताः", "named, termed"], ["योनिः", "source"]],
              "These words give what is named, with what exclusion, and what the result concerns.",
              "रसाः = tastes; लवणवर्ज्याः = excluding salt; संज्ञिताः = named; योनिः = source."),
        fill(2, "The word meaning 'fivefold' in verse 24 is ____ (type it in Devanagari).",
             ["पञ्चविधा"],
             "Line 2 says पञ्चविधा योनिः: the source is fivefold.",
             "पञ्चविधा is पञ्च ('five') + विधा ('kind'), feminine singular to agree with योनिः: 'of five kinds'.",
             "पञ्चविधा = fivefold; it describes the feminine योनिः."),
        mcq("discriminate", 3, "Which is the right split of लवणवर्ज्याश्च?",
            ("लवणवर्ज्याः + च: a visarga before च becomes श्",
             "The word is लवणवर्ज्याः ('excluding salt'), and ः + च is written श्च."),
            [("लवणवर्ज्या + श्च", "श्च is not a word."),
             ("लवण + वर्ज्याश्च", "That would lose the meaning 'excluding salt' as one word."),
             ("लवणवर्ज्य + आश्च", "आश्च is not a word.")],
            "लवणवर्ज्याश्च = लवणवर्ज्याः (excluding salt) + च (and).",
            "Visarga + च → श्च."),
        mcq("apply", 4,
            "What does the word तस्मात् ('therefore') connect in verse 24?",
            ("The naming of tastes as kaṣāya → the fivefold source",
             "तस्मात् draws the conclusion 'the source is fivefold' from the naming in line 1."),
            [("The fifty great kaṣāyas → the six hundred purgatives",
              "These numbers are not in verse 24."),
             ("The six bases → the five preparations",
              "Neither the bases nor the preparations appear in verse 24."),
             ("The word 'kaṣāya' → the taste salt",
              "Salt is excluded in verse 24, not concluded from anything.")],
            "तस्मात् = therefore: because the tastes (excluding salt) are called kaṣāya, the source of kaṣāyas is fivefold.",
            "Line 1 gives the reason; तस्मात् introduces the result in line 2."),
        mcq("transfer", 5,
            "An invented phrase: द्रव्याणि मूलवर्ज्यानि (मूल = root). By the pattern of लवणवर्ज्याः, what does it mean?",
            ("Substances excluding the root",
             "X-वर्ज्य = 'excluding X'; the ending -आनि is neuter plural, agreeing with द्रव्याणि."),
            [("Substances made only of the root",
              "-वर्ज्य means excluding, not consisting of."),
             ("A root excluding all substances",
              "The plural द्रव्याणि is what is described, not मूलम्."),
             ("The root that excludes salt",
              "Salt is not in the phrase.")],
            "Compound ending in -वर्ज्य = 'excluding the first part': मूलवर्ज्यानि = excluding the root.",
            "X-वर्ज्य = excluding X.",
            teaches="A compound ending in -वर्ज्य names what is left out in its first part: लवणवर्ज्याः 'excluding salt', मूलवर्ज्यानि 'excluding the root'."),
    ],
}

# --------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "तथा कल्पनमप्येषामुक्तं पञ्चविधं पुनः",
    "question": "What two numbers does verse 25 give, and for which things?",
    "rule": ("तथा कल्पनमप्येषामुक्तं पञ्चविधं पुनः महतां च कषायाणां पञ्चाशत् परिकीर्तिता = "
             "Likewise the preparation (kalpana) of these is stated as fivefold; and fifty "
             "of the great kaṣāyas are enumerated."),
    "limits": ("The five preparations are not named in this verse (unit 7 names "
               "them, and lists six names under 'five'). पुनः can also be read as "
               "'further'. The verse does not say what the fifty are."),
    "explain_hi": ("यह श्लोक दो संख्याएँ गिनाता है: इन (कषायों) की ‘कल्पना’ (तैयार करने की विधि) "
                   "भी ‘पञ्चविध’ (पाँच प्रकार की) कही गई, और महान् कषायों के ‘पचास’ "
                   "(पञ्चाशत्) वर्ग बताए गए। ‘तथा’ (वैसे ही) पिछले श्लोक की बात को जोड़ता है। "
                   "पाँच कल्पनाओं के नाम इस श्लोक में नहीं हैं; इकाई ७ में पाँच कहकर छह नाम "
                   "आए हैं, और उसे हल नहीं किया गया। ‘पुनः’ का अर्थ ‘फिर’ या ‘और’ हो सकता है।"),
    "hook": "कल्पना (तैयारी) पाँच प्रकार की; महान् कषाय पचास।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "How many great kaṣāyas does verse 25 enumerate?",
            ("Fifty",
             "महतां च कषायाणां पञ्चाशत् = fifty of the great kaṣāyas."),
            [("Five",
              "Five is the number of kinds of preparation, not of great kaṣāyas."),
             ("Five hundred",
              "Five hundred is the number in verse 26, for the other kaṣāyas."),
             ("Six hundred",
              "Six hundred is the number of purgatives in verse 23.")],
            "पञ्चाशत् = fifty, said of the great kaṣāyas.",
            "पञ्चाशत् = fifty."),
        match(1, "Match each word of verse 25 to its meaning.",
              [["कल्पनम्", "preparation"], ["पञ्चविधम्", "fivefold"],
               ["महताम्", "of the great"], ["परिकीर्तिता", "enumerated, declared"]],
              "These words say what is fivefold and what is enumerated.",
              "कल्पनम् = preparation; पञ्चविधम् = fivefold; महताम् = of the great; परिकीर्तिता = enumerated."),
        fill(2, "The number word meaning 'fifty' in verse 25 is ____ (type it in Devanagari).",
             ["पञ्चाशत्", "पञ्चाशत"],
             "Line 2 ends with पञ्चाशत् परिकीर्तिता: fifty are enumerated.",
             "पञ्चाशत् is a feminine noun-number, and परिकीर्तिता is feminine too, so they agree: 'fifty (are) enumerated'.",
             "पञ्चाशत् = fifty; it agrees with the feminine परिकीर्तिता."),
        mcq("discriminate", 3, "Which is the right split of अप्येषाम्?",
            ("अपि + एषाम्: इ + ए joins as ये",
             "अपि ends in इ and एषाम् begins with ए; इ + ए gives ये, so अप्येषाम्."),
            [("अप + येषाम्", "येषाम् would mean 'of which'; the word here is एषाम्, 'of these'."),
             ("अपि + येषाम्", "That would be written अपियेषाम्, with no joining."),
             ("अप्य + एषाम्", "अप्य is not a word.")],
            "अप्येषाम् is अपि (also) + एषाम् (of these).",
            "इ + ए → ये: अपि + एषाम् → अप्येषाम्."),
        mcq("apply", 4,
            "Does verse 25 name the five kinds of preparation?",
            ("No; it only says the preparation is fivefold",
             "The word is पञ्चविधम्; no names appear in the verse."),
            [("Yes; it names all five in line 1",
              "Line 1 contains no preparation names."),
             ("Yes; it names the first two and says 'again'",
              "पुनः is 'again, further', not a name."),
             ("No; it says the preparation is fiftyfold",
              "पञ्चाशत् belongs to the great kaṣāyas, not to the preparation.")],
            "The verse gives the number five for the preparation, with no names.",
            "पञ्चविधम् states a number of kinds; it does not list them."),
        mcq("transfer", 5,
            "An invented phrase: षड्विधं कल्पनम्. By the pattern of पञ्चविधं कल्पनम्, what does it mean?",
            ("A sixfold preparation",
             "A number + विध = 'of that many kinds'; षट् becomes षड् before विध."),
            [("A preparation with six drugs only",
              "-विध counts kinds, not drugs."),
             ("Six preparations were refused",
              "No refusal is expressed."),
             ("A fivefold preparation",
              "The number is षट्, six, not पञ्च.")],
            "संख्या + विध = of that many kinds: पञ्चविध five-fold, षड्विध six-fold.",
            "Number + विध = -fold.",
            teaches="Number + -विध gives '-fold, of that many kinds': पञ्चविधम् 'fivefold', षड्विधम् 'sixfold'."),
    ],
}

# --------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "पञ्च चापि कषायाणां शतान्युक्तानि भागशः",
    "question": "What number of kaṣāyas does verse 26 state, and why only in parts?",
    "rule": ("पञ्च चापि कषायाणां शतान्युक्तानि भागशः लक्षणार्थं प्रमाणं हि विस्तरस्य न विद्यते = "
             "And five hundred of the kaṣāyas have also been stated, part by part, for "
             "characterization; for there is no limit to elaboration."),
    "limits": ("The verse does not say how the five hundred are divided. भागशः "
               "can also be read as 'in divisions'. It gives no list."),
    "explain_hi": ("यह श्लोक कहता है कि ‘पाँच सौ’ कषाय भी ‘भागशः’ (भाग-भाग करके) कहे गए हैं, "
                   "‘लक्षणार्थम्’ (पहचान या नमूने के लिए)। कारण ‘हि’ (क्योंकि) के बाद आता है: "
                   "‘विस्तर की कोई सीमा (प्रमाण) नहीं मिलती’ (‘न विद्यते’)। ‘शतानि’ का अर्थ "
                   "‘सैकड़े’ है, इसलिए ‘पञ्च … शतानि’ = पाँच सौ। ‘च’ और ‘अपि’ दोनों ‘और भी’ का "
                   "भाव देते हैं। श्लोक यह नहीं बताता कि भाग कैसे बँटे हैं।"),
    "hook": "पाँच सौ कषाय भाग-भाग करके, पहचान के लिए, क्योंकि विस्तार की सीमा नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "How many hundreds of kaṣāyas does verse 26 say have been stated?",
            ("Five hundred",
             "पञ्च … शतानि = five hundreds."),
            [("Fifty",
              "Fifty is the number of great kaṣāyas in verse 25."),
             ("Six hundred",
              "Six hundred is the number of purgatives in verse 23."),
             ("Thirty-two",
              "Thirty-two is not mentioned anywhere in this chapter's verses.")],
            "पञ्च शतानि = five hundreds.",
            "पञ्च + शतानि = 500."),
        match(1, "Match each word of verse 26 to its meaning.",
              [["भागशः", "part by part"],
               ["लक्षणार्थम्", "for the purpose of characterization"],
               ["प्रमाणम्", "limit, measure"], ["विस्तरस्य", "of elaboration"]],
              "These words give the manner, the purpose and the reason.",
              "भागशः = part by part; लक्षणार्थम् = for characterization; प्रमाणम् = limit; विस्तरस्य = of elaboration."),
        fill(2, "Complete the end of verse 26: प्रमाणं हि विस्तरस्य न ____ (type the verb in Devanagari).",
             ["विद्यते"],
             "The verse ends न विद्यते: there is no limit.",
             "विद्यते is third person singular present (passive/middle) of √विद्: 'is found, exists'. With न it says no limit exists.",
             "न विद्यते = does not exist; there is no limit."),
        mcq("discriminate", 3, "Which is the right split of चापि?",
            ("च + अपि: अ + अ joins as आ",
             "च ends in अ and अपि begins with अ; अ + अ gives आ, so चापि."),
            [("चा + पि", "पि is not a word here."),
             ("च + आपि", "The word is अपि, with short अ."),
             ("चाप + इ", "इ alone is not a word here.")],
            "चापि is च (and) + अपि (also).",
            "अ + अ → आ: च + अपि → चापि."),
        multi("apply", 4, "Which statements does verse 26 itself make?",
              [("Five hundred kaṣāyas are stated", "Right: पञ्च … कषायाणां शतानि उक्तानि."),
               ("They are stated part by part, for characterization", "Right: भागशः लक्षणार्थम्."),
               ("The reason is that elaboration has no limit", "Right: प्रमाणं हि विस्तरस्य न विद्यते."),
               ("Each of the five hundred is described with its dose", "No dose appears in the verse."),
               ("There are exactly fifty great kaṣāyas among them", "The number fifty is in verse 25, not here.")],
              [0, 1, 2],
              "The verse gives the number, the manner and the reason; dose and the number fifty are not in it.",
              "Verse 26: 500 kaṣāyas, in parts, for characterization, because elaboration has no limit."),
        mcq("transfer", 5,
            "An invented sentence: ज्ञानस्य प्रमाणं न विद्यते. By the pattern of विस्तरस्य प्रमाणं न विद्यते, what does it say?",
            ("There is no limit to knowledge",
             "Genitive + प्रमाणं न विद्यते = no limit of that thing is found."),
            [("Knowledge is the limit of everything",
              "The sentence denies a limit with न; it does not make knowledge a limit."),
             ("Knowledge has a fixed measure",
              "न विद्यते denies that a measure exists."),
             ("The limit gives knowledge to no one",
              "ज्ञानस्य is a genitive, 'of knowledge', not a receiver.")],
            "प्रमाणं न विद्यते = no limit exists; the genitive names what has no limit.",
            "Genitive + प्रमाणं न विद्यते = there is no limit of that.",
            teaches="The frame 'genitive + प्रमाणं न विद्यते' says that the thing named in the genitive has no limit."),
    ],
}

# --------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "न चालमतिसंक्षेपः सामर्थ्यायोपकल्पते",
    "question": "What does verse 27 say about excessive brevity, and what does it conclude for the exposition?",
    "rule": ("न चालमतिसंक्षेपः सामर्थ्यायोपकल्पते अल्पबुद्धेरयं तस्मान्नातिसंक्षेपविस्तरः = "
             "Nor does excessive brevity suffice for capability; therefore, for one of "
             "little intelligence, this exposition is not too brief and not too elaborate."),
    "limits": ("The compound नातिसंक्षेपविस्तरः is doubtful in the data (the "
               "reading 'neither too brief nor too elaborate' follows unit 20). The "
               "subject 'this exposition' is understood, not printed. न … अलम् is "
               "taken as 'does not suffice'."),
    "explain_hi": ("पहली पंक्ति: ‘अतिसंक्षेप’ (बहुत अधिक संक्षिप्त होना) ‘सामर्थ्य’ के लिए ‘अलम्’ "
                   "(पर्याप्त) नहीं होता, यानी ज्ञान की क्षमता नहीं बनाता। दूसरी पंक्ति: "
                   "‘इसलिए’ (तस्मात्) अल्पबुद्धि वाले के लिए यह (वर्णन) न बहुत संक्षिप्त है, न बहुत "
                   "विस्तृत। यही भाव गद्य इकाई २० में भी है। ‘अयम्’ का संज्ञा-पद ‘वर्णन’ श्लोक में "
                   "नहीं छपा, उसे समझ लिया गया है। ‘अल्पबुद्धेः’ षष्ठी एकवचन है: ‘अल्प बुद्धि वाले का/के लिए’।"),
    "hook": "बहुत संक्षेप सामर्थ्य नहीं देता; इसलिए अल्पबुद्धि के लिए यह वर्णन न अति-संक्षिप्त, न अति-विस्तृत।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 27 say excessive brevity does not do?",
            ("It does not suffice to serve capability",
             "न … अलम् … सामर्थ्याय उपकल्पते: it does not suffice for capability."),
            [("It does not shorten the chapter",
              "The verse says nothing about shortening the chapter."),
             ("It does not name the purgatives",
              "Naming purgatives is not in this verse."),
             ("It does not reach fifty classes",
              "The number fifty is not stated in this verse.")],
            "अतिसंक्षेपः is the subject: excessive brevity does not suffice for capability.",
            "न अलम् उपकल्पते = does not suffice."),
        match(1, "Match each word of verse 27 to its meaning.",
              [["अतिसंक्षेपः", "excessive brevity"],
               ["सामर्थ्याय", "for capability"],
               ["अल्पबुद्धेः", "of one of little intelligence"],
               ["तस्मात्", "therefore"]],
              "These words carry the argument: brevity, what it fails to give, for whom, and the conclusion.",
              "अतिसंक्षेपः = excessive brevity; सामर्थ्याय = for capability; अल्पबुद्धेः = of little intelligence; तस्मात् = therefore."),
        fill(2, "The word meaning 'therefore' in verse 27 is ____ (type it in Devanagari, as the card shows it).",
             ["तस्मात्"],
             "Line 2 has तस्मान्नातिसंक्षेपविस्तरः, which begins with तस्मात्.",
             "तस्मात् is an ablative form used as an adverb: 'for that reason, therefore'. It draws the conclusion from line 1.",
             "तस्मात् = therefore; it introduces the conclusion."),
        mcq("discriminate", 3, "Which is the right split of सामर्थ्यायोपकल्पते?",
            ("सामर्थ्याय + उपकल्पते: अ + उ joins as ओ",
             "सामर्थ्याय ends in अ (-य) and उपकल्पते begins with उ; अ + उ gives ओ, so सामर्थ्यायोपकल्पते."),
            [("सामर्थ्यायो + पकल्पते", "पकल्पते is not a word; the verb is उपकल्पते."),
             ("सामर्थ्य + आयोपकल्पते", "आयोपकल्पते is not a word."),
             ("सामर्थ्याय + अपकल्पते", "The verb is उपकल्पते, with the prefix उप.")],
            "सामर्थ्यायोपकल्पते is सामर्थ्याय (for capability) + उपकल्पते (serves).",
            "अ + उ → ओ: सामर्थ्याय + उपकल्पते → सामर्थ्यायोपकल्पते."),
        mcq("apply", 4,
            "How does verse 27 reach its conclusion about the exposition?",
            ("Excessive brevity does not suffice, so the exposition is kept neither too brief nor too elaborate",
             "Line 1 gives the reason; तस्मात् in line 2 draws the conclusion for one of little intelligence."),
            [("The exposition is as brief as possible, so that it is easily learnt",
              "The verse says excessive brevity does not suffice."),
             ("The exposition is very long, so that nothing is missed",
              "The verse also says it is not too elaborate."),
             ("The exposition is for the learned alone, who need no detail",
              "The verse speaks of one of little intelligence, not the learned.")],
            "The verse argues from the failure of excessive brevity to the middle way.",
            "Reason (brevity fails) → तस्मात् → neither extreme."),
        mcq("transfer", 5,
            "An invented phrase: अल्पबलस्य रोगिणः (बल = strength). By the pattern of अल्पबुद्धेः, what does it mean?",
            ("Of a patient of little strength",
             "A compound beginning with अल्प- and describing a person means 'one of little …'; the genitive says 'of'."),
            [("Of a patient who has no strength at all",
              "अल्प means 'little', not 'none'."),
             ("Of a strength that has little patients",
              "रोगिणः, the patient, is what अल्पबलस्य describes."),
             ("Of a great and strong patient",
              "अल्प- reverses 'great'; it says 'little'.")],
            "अल्प + noun, used of a person = one of little … (here strength): अल्पबलस्य रोगिणः.",
            "अल्प-X in the genitive = of one of little X.",
            teaches="A compound beginning with अल्प-, describing a person, as in अल्पबुद्धेः, means 'of one with little …'."),
    ],
}

# --------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "मन्दानां व्यवहाराय बुधानां बुद्धिवृद्धये",
    "question": "For whom, and for what purposes, is this group of fifty set forth in verse 28?",
    "rule": ("मन्दानां व्यवहाराय बुधानां बुद्धिवृद्धये पञ्चाशत्को ह्ययं वर्गः कषायाणामुदाहृतः = "
             "For the practical use of the dull and the growth of the intellect of the "
             "wise: for this group of fifty kaṣāyas has been set forth."),
    "limits": ("मन्द is taken as 'dull, slow (in understanding)' and व्यवहार as "
               "'practical use'; the verse gives no further definition. हि is read as "
               "'for' (explaining), or as emphasis."),
    "explain_hi": ("यह श्लोक दो उद्देश्य जोड़ी में रखता है: ‘मन्दानाम्’ (धीमे लोगों) के "
                   "‘व्यवहार’ (प्रयोग/उपयोग) के लिए, और ‘बुधानाम्’ (बुद्धिमानों) की बुद्धि की "
                   "वृद्धि के लिए। ‘हि’ (क्योंकि) के बाद कारण आता है: कषायों का यह ‘पचास का वर्ग’ "
                   "(पञ्चाशत्को वर्गः) कहा गया है। ‘व्यवहाराय’ और ‘वृद्धये’ चतुर्थी (तादर्थ्य, "
                   "‘के लिए’) हैं। ‘मन्द’ और ‘बुध’ दो विपरीत सिरे हैं, और दोनों के लिए एक ही वर्ग "
                   "उपयोगी बताया गया है।"),
    "hook": "मन्द → व्यवहार के लिए; बुध → बुद्धि की वृद्धि के लिए; दोनों के लिए पचास का वर्ग।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 28 sets forth a group of fifty kaṣāyas. What two purposes does it give?",
            ("Practical use for the dull, and growth of the intellect of the wise",
             "मन्दानां व्यवहाराय and बुधानां बुद्धिवृद्धये."),
            [("Growth of intellect for the dull, and practical use for the wise",
              "The verse pairs the dull with practical use and the wise with growth of intellect."),
             ("Practical use for physicians, and praise for the teacher",
              "Neither physicians nor a teacher are mentioned in this verse."),
             ("Brevity for the dull, and detail for the wise",
              "The verse speaks of use and growth of intellect, not of brevity and detail.")],
            "Each group of people has its own purpose: dull → व्यवहार; wise → बुद्धिवृद्धि.",
            "मन्दानां + व्यवहाराय; बुधानां + बुद्धिवृद्धये."),
        match(1, "Match each word of verse 28 to its meaning.",
              [["मन्दानाम्", "of the dull, slow"], ["बुधानाम्", "of the wise"],
               ["व्यवहाराय", "for practical use"],
               ["बुद्धिवृद्धये", "for the growth of intellect"]],
              "These four words are the two pairs of the verse.",
              "मन्दानाम् = of the dull; बुधानाम् = of the wise; व्यवहाराय = for practical use; बुद्धिवृद्धये = for growth of intellect."),
        fill(2, "The word meaning 'group, class' in verse 28 is ____ (type it with its visarga in Devanagari).",
             ["वर्गः", "वर्ग"],
             "Line 2 says अयं वर्गः: this group.",
             "वर्गः is the nominative singular of वर्ग, 'group, class'; here it is the 'group of fifty' kaṣāyas.",
             "वर्गः = group, class."),
        mcq("discriminate", 3, "Which is the right split of ह्ययं?",
            ("हि + अयम्: इ + अ becomes य",
             "हि ends in इ and अयम् begins with अ; इ + अ gives य, so ह्ययम्, written ह्ययं."),
            [("ह्य + अयम्", "ह्य is not a word here."),
             ("हि + ययम्", "ययम् is not a word."),
             ("हे + अयम्", "The word is हि, with short इ.")],
            "ह्ययं is हि (for) + अयम् (this).",
            "इ + अ → य: हि + अयम् → ह्ययम्."),
        multi("apply", 4, "Which statements does verse 28 itself make?",
              [("The group is of fifty kaṣāyas", "Right: पञ्चाशत्को वर्गः कषायाणाम्."),
               ("It is for the practical use of the dull", "Right: मन्दानां व्यवहाराय."),
               ("It is for the growth of the intellect of the wise", "Right: बुधानां बुद्धिवृद्धये."),
               ("It is only for the wise", "The verse also names the dull."),
               ("It is for the dull to forget", "The verse says nothing of forgetting.")],
              [0, 1, 2],
              "The verse names the group of fifty and both purposes; it excludes neither the dull nor the wise.",
              "Verse 28: a group of fifty, for the dull (use) and the wise (growth of intellect)."),
        mcq("transfer", 5,
            "An invented phrase: रोगिणां सुखाय (सुख = comfort). By the pattern of मन्दानां व्यवहाराय, what does it mean?",
            ("For the comfort of the sick",
             "Genitive plural + dative = 'for the … of those people'."),
            [("From the comfort of the sick",
              "'From' would need the ablative, not the dative -आय."),
             ("The sick who give comfort",
              "The dative सुखाय names a purpose, not a doer."),
             ("Without comfort for the sick",
              "No negative is expressed.")],
            "Genitive plural of people + dative of the purpose = 'for the (purpose) of those people'.",
            "Genitive + dative (-आय / -ये) = for the … of them.",
            teaches="A dative like व्यवहाराय or सुखाय names the purpose, and the genitive before it names whose purpose it is."),
    ],
}

# --------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "तेषां कर्मसु बाह्येषु योगमाभ्यन्तरेषु च",
    "question": "Whom does verse 29 call 'the best of physicians', and what must he know?",
    "rule": ("तेषां कर्मसु बाह्येषु योगमाभ्यन्तरेषु च संयोगं च प्रयोगं च यो वेद स भिषग्वरः = "
             "He who knows, in the external and internal actions of these, their application "
             "(yoga), combination (saṃyoga) and administration (prayoga) is the best of "
             "physicians."),
    "limits": ("The verse does not explain how yoga, saṃyoga and prayoga differ; the "
               "data keeps their plain senses and notes that commentators may differ. "
               "'These' (तेषाम्) refers to the kaṣāyas of the preceding verses."),
    "explain_hi": ("यह अन्तिम श्लोक वैद्य की पहचान देता है। जो उन (कषायों) के ‘बाह्य’ और "
                   "‘आभ्यन्तर’ कर्मों में तीन बातें जानता है, वह ‘भिषग्वर’ (श्रेष्ठ वैद्य) है: "
                   "‘योग’ (प्रयोग-योग/उपयोग), ‘संयोग’ (मेल) और ‘प्रयोग’ (देना)। ‘योगम्’ का "
                   "अन्वय बाह्य और आभ्यन्तर दोनों कर्मों के साथ लिया गया है। ‘यः … सः’ "
                   "का जोड़ा ‘जो … वह’ का भाव देता है। तीनों शब्दों का भेद श्लोक नहीं समझाता; "
                   "यहाँ उनके सीधे अर्थ ही रखे हैं।"),
    "hook": "जो उन कषायों के बाह्य-आभ्यन्तर कर्मों में योग, संयोग और प्रयोग जानता है, वही श्रेष्ठ वैद्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Whom does verse 29 call भिषग्वरः, 'the best of physicians'?",
            ("The one who knows yoga, saṃyoga and prayoga in their external and internal actions",
             "यो वेद स भिषग्वरः: the one who knows these is the best of physicians."),
            [("The one who has learned all six hundred purgatives by heart",
              "The verse names knowing yoga, saṃyoga and prayoga, not memorising a number."),
             ("The one who prefers the shortest teaching",
              "Brevity is not mentioned in this verse."),
             ("The one who treats only the dull",
              "The dull are mentioned in verse 28, not in this test of a physician.")],
            "The verse's condition is knowledge of three things in two kinds of action.",
            "यः … वेद सः भिषग्वरः = he who knows is the best of physicians."),
        match(1, "Match each word of verse 29 to its meaning.",
              [["योगम्", "application, use"], ["संयोगम्", "combination"],
               ["प्रयोगम्", "administration, employment"],
               ["भिषग्वरः", "best of physicians"]],
              "The first three are what must be known; the last is who knows them.",
              "योगम् = application; संयोगम् = combination; प्रयोगम् = administration; भिषग्वरः = best of physicians."),
        fill(2, "The verb meaning 'knows' in verse 29 is ____ (type it in Devanagari).",
             ["वेद"],
             "Line 2 says यो वेद: who knows.",
             "वेद is third person singular of √विद् (perfect form, present sense): 'he knows'. It is the verb of the relative clause यः … वेद.",
             "वेद = he knows."),
        mcq("discriminate", 3, "Which is the right split of योगमाभ्यन्तरेषु?",
            ("योगम् + आभ्यन्तरेषु",
             "योगम् is the accusative 'application'; its final म् joins the vowel आ of आभ्यन्तरेषु."),
            [("योग + माभ्यन्तरेषु", "माभ्यन्तरेषु is not a word."),
             ("योगा + भ्यन्तरेषु", "भ्यन्तरेषु is not a word."),
             ("योगम् + भ्यन्तरेषु", "That would lose the आ of आभ्यन्तरेषु, 'internal'.")],
            "योगमाभ्यन्तरेषु is योगम् (application) + आभ्यन्तरेषु (in internal ones).",
            "म् + vowel: योगम् + आभ्यन्तरेषु → योगमाभ्यन्तरेषु."),
        order(4, "Put the three things the physician must know in the order of verse 29.",
              ["योगम्", "संयोगम्", "प्रयोगम्"],
              "The verse names application first, then combination, then administration.",
              "योगम् → संयोगम् → प्रयोगम्.", role="apply"),
        mcq("transfer", 5,
            "An invented sentence: यो द्रव्यं वेद स कुशलः (कुशल = skilled). By the pattern of यो वेद स भिषग्वरः, who is skilled?",
            ("He who knows the substance",
             "यः … सः pairs 'who' with 'he': whoever knows the substance (द्रव्यम्) is skilled."),
            [("He who does not know the substance",
              "वेद, 'knows', is not negated."),
             ("The substance itself",
              "द्रव्यम् is what is known; the skilled one is the knower."),
             ("Everyone, whether he knows or not",
              "The यः-clause limits it to the one who knows.")],
            "यः … वेद सः X = he who knows is X.",
            "यः + verb … सः + title = 'he who … is …'.",
            teaches="The pair यः … सः means 'he who … that one …'; it names the condition first and the title after, as in यो वेद स भिषग्वरः."),
    ],
}


NOTES_HI = {
    "21": ("पाठ-संकेत (text_flag): अन्तिम शब्द ‘महाकषायेष्वति’ छपा है, पर ‘अति’ से स्पष्ट अन्वय नहीं "
           "बनता; आँकड़ों में ‘महाकषायेष्विति’ (इति = उद्धरण का अन्त) सुझाया गया है और विभाजन उसी पर किया "
           "गया है। यदि ‘अति’ रखें तो वह ‘उपप्लवन्ते’ से ‘अत्यन्त’ जुड़ सकता है, पर स्थिति अटपटी है। स्रोत "
           "में एक भटका ‘&’ हटाया गया था, इसलिए शब्द-विभाजन मूल से जाँचा नहीं जा सका। सन्धि: अग्निवेशः + उवाच → "
           "अग्निवेश उवाच (अः + अ के अलावा कोई स्वर → विसर्ग लुप्त); न + एतानि → नैतानि (अ + ए → ऐ); हि + एव → ह्येव; "
           "ह्येव + अङ्गानि → ह्येवाङ्गानि; अङ्गानि + उपप्लवन्ते → अङ्गान्युपप्लवन्ते (इ + उ → ्यु)।"),
    "22": ("पाठ-संशय नहीं है। ‘तमुवाच’ = तम् + उवाच; ‘नैतदेवं’ = न + एतत् + एवम् (अ + ए → ऐ; एतत् का त् "
           "स्वर से पहले द् होता है)। ‘बुद्धिमता’ तृतीया एकवचन है, और ‘द्रष्टव्यम्’ √दृश् का विधि-कृदन्त "
           "(‘देखना चाहिए’) है। ‘भगवानात्रेयः’ = भगवान् + आत्रेयः। ‘एवं’ का अर्थ ‘इस प्रकार’ है; यह किस "
           "प्रकार की ओर संकेत करता है, यह अगली बातों से स्पष्ट होता है, इस इकाई से नहीं।"),
    "23": ("पाठ-संशय नहीं है। पहले ‘तत्र श्लोकाः’ (यहाँ, इस विषय में, श्लोक) लगा है। ‘यतः’ का अर्थ "
           "‘जिस (स्रोत) से’ लिया गया; ‘क्योंकि’ भी हो सकता है। ‘उक्तानि’ नपुंसक बहुवचन है और "
           "‘विरेचनशतानि’ से मेल खाता है। ‘षडाश्रयाः’ = षट् + आश्रयाः (ट् + स्वर → ड्); इसे ‘छह आश्रय’ "
           "ही कहा गया है, उनके नाम श्लोक में नहीं हैं। ‘यैर्द्रव्यैः’ = यैः + द्रव्यैः (ऐः + घोष → ऐर्)। "
           "‘संग्रहेणेह’ = संग्रहेण + इह (अ + इ → ए); ‘तथैवैषाम्’ = तथा + एव + एषाम् (आ + ए → ऐ; अ + ए → ऐ)।"),
    "24": ("पाठ-संकेत: स्रोत में एक भटका ‘&’ हटाया गया था; टोकन ठीक पढ़ते हैं और छन्द (१६+१६) बैठता है, "
           "इसलिए शब्द-विभाजन की कोई समस्या नहीं दिखी। ‘कषाय’ यहाँ वर्ग का नाम है, केवल कसैला स्वाद नहीं। "
           "‘लवणवर्ज्याः’ को ‘जिनमें लवण छोड़ा गया’ पढ़ा गया है (तत्पुरुष)। ‘रसा’ = रसाः (आः + घोष: विसर्ग "
           "लुप्त); ‘लवणवर्ज्याश्च’ = लवणवर्ज्याः + च (विसर्ग + च → श्च); ‘कषाय इति’ = कषायः + इति "
           "(अः + इ: विसर्ग लुप्त); ‘कषायाणामुदाहृता’ = कषायाणाम् + उदाहृता।"),
    "25": ("पाठ-संशय नहीं है। ‘कल्पन’ का अर्थ ‘तैयार करने की विधि’ लिया गया; इस श्लोक में पाँच नाम नहीं हैं। "
           "‘पुनः’ का अर्थ ‘फिर’ या ‘और’ भी हो सकता है। ‘परिकीर्तिता’ स्त्रीलिङ्ग है और ‘पञ्चाशत्’ (स्त्रीलिङ्ग) "
           "से मेल खाता है। सन्धि: कल्पनम् + अपि + एषाम् + उक्तम् → कल्पनमप्येषामुक्तम् (अपि + एषाम्: इ + ए → "
           "्ये; एषाम् + उक्तम्: म् + उ जुड़ता है)।"),
    "26": ("पाठ-संशय नहीं है। ‘भागशः’ का अर्थ ‘भाग-भाग करके’ लिया गया, ‘विभागों में’ भी हो सकता है। "
           "‘लक्षणार्थम्’ = लक्षण + अर्थम् (‘पहचान के लिए’), क्रिया-विशेषण। ‘चापि’ = च + अपि (अ + अ → आ); "
           "‘शतान्युक्तानि’ = शतानि + उक्तानि (इ + उ → ्यु)। ‘पञ्च … शतानि’ में ‘पाँच सौ’ का अर्थ संख्या-वाचक शब्द "
           "से ही आता है। पाँच सौ किन वर्गों में बँटे हैं, यह श्लोक नहीं बताता।"),
    "27": ("दो संशय डेटा में हैं। (१) ‘न … अलम्’ को ‘पर्याप्त नहीं होता’ पढ़ा गया है। (२) ‘नातिसंक्षेपविस्तरः’ "
           "का समास-विश्लेषण अनिश्चित है; इसे ‘न अति-संक्षेप, न अति-विस्तार’ पढ़ा गया है, जैसे गद्य इकाई २० के "
           "‘अनतिसंक्षेपेणानतिविस्तरेण’ में। ‘अयम्’ का संज्ञा-पद छपा नहीं है। सन्धि: न + च + अलम् + अति… → "
           "नचालमति… ; सामर्थ्याय + उपकल्पते → सामर्थ्यायोपकल्पते (अ + उ → ओ); अल्पबुद्धेः + अयम् → "
           "अल्पबुद्धेरयम् (एः + स्वर → एर्); तस्मात् + न → तस्मान्न, न + अति → नाति।"),
    "28": ("पाठ-संशय नहीं है। ‘मन्द’ को ‘धीमा/मन्दबुद्धि’ और ‘व्यवहार’ को ‘प्रयोग/उपयोग’ पढ़ा गया है; "
           "‘हि’ कारण-वाचक या बल देने वाला हो सकता है। ‘पञ्चाशत्को ह्ययं’ में दो सन्धियाँ हैं: "
           "पञ्चाशत्कः + हि → पञ्चाशत्को हि (अः + घोष → ओ), और हि + अयम् → ह्ययम् (इ + अ → य)। "
           "‘कषायाणामुदाहृतः’ = कषायाणाम् + उदाहृतः। ‘मन्दानां’ और ‘बुधानां’ दोनों षष्ठी बहुवचन हैं, जो "
           "‘व्यवहाराय’ और ‘बुद्धिवृद्धये’ (चतुर्थी) के साथ जोड़ी बनाते हैं।"),
    "29": ("पाठ-संशय नहीं है। ‘योगम्’ का अन्वय बाह्य और आभ्यन्तर दोनों कर्मों के साथ लिया गया; शब्दों "
           "का सूक्ष्म भेद (योग/संयोग/प्रयोग) टीकाकारों में भिन्न हो सकता है। ‘भिषग्वरः’ का अर्थ "
           "‘वैद्यों में श्रेष्ठ’ या ‘उत्तम वैद्य’ दोनों हो सकता है। सन्धि: योगम् + आभ्यन्तरेषु → "
           "योगमाभ्यन्तरेषु; यः + वेद → यो वेद (अः + घोष → ओ); सः का विसर्ग व्यंजन से पहले लुप्त: "
           "स भिषग्वरः; भिषज् + वरः → भिषग्वरः (ज् → ग् घोष व्यंजन से पहले)।"),
}


AIDS = {
    "21": {
        "diagram": {"groups": [
            _g("वाक्य १", "एवंवादिनं भगवन्तमात्रेयमग्निवेश उवाच"),
            _g("शंका", "नैतानि भगवन् पञ्च कषायशतानि पूर्यन्ते"),
            _g("कारण", "तानि तानि ह्येवाङ्गान्युपप्लवन्ते तेषु तेषु महाकषायेष्वति")]},
        "sandhi": "अग्निवेशः + उवाच → अग्निवेश उवाच (अः + अ के अलावा कोई स्वर → विसर्ग लुप्त) · न + एतानि → नैतानि (अ + ए → ऐ) · हि + एव + अङ्गानि → ह्येवाङ्गानि · अङ्गानि + उपप्लवन्ते → अङ्गान्युपप्लवन्ते (इ + उ → ्यु)।",
        "anchors": "न … पूर्यन्ते = पूरे नहीं होते · तानि तानि / तेषु तेषु = दोहराव: ‘उन-उन’ · उपप्लवन्ते = शाब्दिक ‘ऊपर तैरते हैं’, यहाँ ‘बार-बार आते हैं’ · महाकषायेष्वति में ‘अति’ संदिग्ध (डेटा: ‘इति’ सुझाया)।",
        "chunks": "एवंवादिनं भगवन्तमात्रेयमग्निवेश उवाच ‖ नैतानि भगवन् | पञ्च कषायशतानि पूर्यन्ते ‖ तानि तानि ह्येवाङ्गान्युपप्लवन्ते | तेषु तेषु महाकषायेष्वति।",
    },
    "22": {
        "diagram": {"groups": [
            _g("वाक्य १", "तमुवाच भगवानात्रेयः"),
            _g("उत्तर", "नैतदेवं बुद्धिमता द्रष्टव्यमग्निवेश")]},
        "sandhi": "न + एतत् + एवम् → नैतदेवम् (अ + ए → ऐ; त् + स्वर → द्) · द्रष्टव्यम् + अग्निवेश → द्रष्टव्यमग्निवेश (म् + अ जुड़ता है) · भगवान् + आत्रेयः → भगवानात्रेयः · तम् + उवाच → तमुवाच।",
        "anchors": "बुद्धिमता = तृतीया (बुद्धिमान् के द्वारा) · द्रष्टव्यम् = ‘देखा जाना चाहिए’ · बुद्धिमता + द्रष्टव्यम् = ‘बुद्धिमान् को देखना चाहिए’ · न = ‘नहीं चाहिए’।",
        "chunks": "तमुवाच भगवानात्रेयः ‖ नैतदेवं बुद्धिमता | द्रष्टव्यमग्निवेश।",
    },
    "23": {
        "frame": "क्या: छह सौ विरेचन · कैसे: संक्षेप में कहे गए (संग्रहेण) · किस आधार पर: यतः, यावन्ति, यैर्द्रव्यैः · साथ में: इनके छह आश्रय।",
        "diagram": {"groups": [
            _g("पंक्ति १", "यतो यावन्ति यैर्द्रव्यैर्विरेचनशतानि षट्"),
            _g("पंक्ति २", "उक्तानि संग्रहेणेह तथैवैषां षडाश्रयाः")]},
        "sandhi": "यैः + द्रव्यैः → यैर्द्रव्यैः (विसर्ग + घोष → र्) · द्रव्यैः + विरेचन… → द्रव्यैर्विरेचन… · संग्रहेण + इह → संग्रहेणेह (अ + इ → ए) · तथा + एव + एषाम् → तथैवैषाम् (आ + ए → ऐ, अ + ए → ऐ) · षट् + आश्रयाः → षडाश्रयाः (ट् + स्वर → ड्)।",
        "chunks": "यतो यावन्ति यैर्द्रव्यैः | विरेचनशतानि षट् ‖ उक्तानि संग्रहेणेह | तथैवैषां षडाश्रयाः।",
        "anchors": "यतः = जिस (स्रोत) से · यावन्ति = जितने · यैः द्रव्यैः = जिन द्रव्यों से · संग्रहेण = संक्षेप से · षडाश्रयाः = षट् + आश्रयाः, ‘छह आधार’ (नाम इस श्लोक में नहीं)।",
    },
    "24": {
        "frame": "क्या नाम: लवण को छोड़कर रस → ‘कषाय’ · परिणाम: इसलिए कषायों की योनि (स्रोत) पञ्चविध।",
        "diagram": {"groups": [
            _g("पंक्ति १", "रसा लवणवर्ज्याश्च कषाय इति संज्ञिताः"),
            _g("पंक्ति २", "तस्मात् पञ्चविधा योनिः कषायाणामुदाहृता")]},
        "chain": {"steps": [
            "रस, लवण को छोड़कर",
            "‘कषाय’ नाम से कहे गए",
            "तस्मात् = इसलिए",
            "कषायों की योनि पञ्चविध"]},
        "sandhi": "रसाः + लवण… → रसा लवण… (आः + घोष: विसर्ग लुप्त) · लवणवर्ज्याः + च → लवणवर्ज्याश्च (विसर्ग + च → श्च) · कषायः + इति → कषाय इति (अः + इ: विसर्ग लुप्त) · कषायाणाम् + उदाहृता → कषायाणामुदाहृता।",
        "chunks": "रसा लवणवर्ज्याश्च | कषाय इति संज्ञिताः ‖ तस्मात् पञ्चविधा योनिः | कषायाणामुदाहृता।",
    },
    "25": {
        "frame": "दो संख्याएँ: कल्पना (तैयारी की विधि) पञ्चविध · महान् कषाय पचास (पञ्चाशत्)।",
        "diagram": {"groups": [
            _g("पंक्ति १", "तथा कल्पनमप्येषामुक्तं पञ्चविधं पुनः"),
            _g("पंक्ति २", "महतां च कषायाणां पञ्चाशत् परिकीर्तिता")]},
        "sandhi": "कल्पनम् + अपि → कल्पनमपि · अपि + एषाम् → अप्येषाम् (इ + ए → ्ये) · एषाम् + उक्तम् → एषामुक्तम् (म् + उ जुड़ता है) · बाकी शब्द अलग छपे हैं।",
        "chunks": "तथा कल्पनमप्येषामुक्तं | पञ्चविधं पुनः ‖ महतां च कषायाणां | पञ्चाशत् परिकीर्तिता।",
        "anchors": "पञ्चविधम् = पाँच प्रकार का (नाम इस श्लोक में नहीं) · पञ्चाशत् = पचास, स्त्रीलिङ्ग, ‘परिकीर्तिता’ के साथ मेल · तथा = वैसे ही।",
    },
    "26": {
        "frame": "क्या: पाँच सौ कषाय (शतानि) · कैसे: भाग-भाग करके · किसलिए: लक्षण के लिए · क्यों: विस्तर की सीमा नहीं।",
        "diagram": {"groups": [
            _g("पंक्ति १", "पञ्च चापि कषायाणां शतान्युक्तानि भागशः"),
            _g("पंक्ति २", "लक्षणार्थं प्रमाणं हि विस्तरस्य न विद्यते")]},
        "sandhi": "च + अपि → चापि (अ + अ → आ) · शतानि + उक्तानि → शतान्युक्तानि (इ + उ → ्यु) · बाकी शब्द अलग छपे हैं।",
        "chunks": "पञ्च चापि कषायाणां | शतान्युक्तानि भागशः ‖ लक्षणार्थं | प्रमाणं हि विस्तरस्य न विद्यते।",
        "anchors": "शतानि = सैकड़े (पञ्च शतानि = ५००) · भागशः = भाग-भाग करके · लक्षणार्थम् = पहचान के लिए · प्रमाणम् = सीमा, माप · न विद्यते = नहीं मिलता।",
    },
    "27": {
        "frame": "पंक्ति १: अति-संक्षेप सामर्थ्य के लिए पर्याप्त नहीं · पंक्ति २: इसलिए अल्पबुद्धि के लिए यह वर्णन न अति-संक्षिप्त, न अति-विस्तृत।",
        "diagram": {"groups": [
            _g("पंक्ति १", "न चालमतिसंक्षेपः सामर्थ्यायोपकल्पते"),
            _g("पंक्ति २", "अल्पबुद्धेरयं तस्मान्नातिसंक्षेपविस्तरः")]},
        "sandhi": "च + अलम् + अति… → चालमति… (अ + अ → आ; म् + अ जुड़ता है) · सामर्थ्याय + उपकल्पते → सामर्थ्यायोपकल्पते (अ + उ → ओ) · अल्पबुद्धेः + अयम् → अल्पबुद्धेरयम् (एः + स्वर → एर्) · तस्मात् + न → तस्मान्न · न + अति → नाति।",
        "chunks": "न चालमतिसंक्षेपः | सामर्थ्यायोपकल्पते ‖ अल्पबुद्धेरयं | तस्मान्नातिसंक्षेपविस्तरः।",
        "anchors": "अतिसंक्षेप = बहुत अधिक संक्षेप · सामर्थ्याय = क्षमता के लिए · अल्पबुद्धेः = अल्प बुद्धि वाले का/के लिए · तस्मात् = इसलिए · समास ‘नातिसंक्षेपविस्तरः’ का विश्लेषण अनिश्चित।",
    },
    "28": {
        "frame": "दो जोड़ियाँ: मन्द → व्यवहार के लिए · बुध → बुद्धि की वृद्धि के लिए · कारण: कषायों का यह पचास का वर्ग कहा गया है।",
        "diagram": {"groups": [
            _g("पंक्ति १", "मन्दानां व्यवहाराय बुधानां बुद्धिवृद्धये"),
            _g("पंक्ति २", "पञ्चाशत्को ह्ययं वर्गः कषायाणामुदाहृतः")]},
        "seesaw": "मन्द (धीमे) ↔ बुध (बुद्धिमान्): मन्द के लिए व्यवहार (उपयोग), बुध के लिए बुद्धि की वृद्धि।",
        "sandhi": "पञ्चाशत्कः + हि → पञ्चाशत्को हि (अः + घोष → ओ) · हि + अयम् → ह्ययम् (इ + अ → य) · कषायाणाम् + उदाहृतः → कषायाणामुदाहृतः।",
        "chunks": "मन्दानां व्यवहाराय | बुधानां बुद्धिवृद्धये ‖ पञ्चाशत्को ह्ययं वर्गः | कषायाणामुदाहृतः।",
    },
    "29": {
        "frame": "कौन: जो जानता है (यः वेद) · क्या: योग, संयोग, प्रयोग · कहाँ: उन (कषायों) के बाह्य और आभ्यन्तर कर्मों में · फल: वह श्रेष्ठ वैद्य।",
        "diagram": {"groups": [
            _g("पंक्ति १", "तेषां कर्मसु बाह्येषु योगमाभ्यन्तरेषु च"),
            _g("पंक्ति २", "संयोगं च प्रयोगं च यो वेद स भिषग्वरः")]},
        "chain": {"steps": [
            "योग: प्रयोग-योग (उपयोग)",
            "संयोग: मेल",
            "प्रयोग: देना, व्यवहार में लाना",
            "जो जानता है, वह भिषग्वर"]},
        "sandhi": "योगम् + आभ्यन्तरेषु → योगमाभ्यन्तरेषु (म् + आ जुड़ता है) · यः + वेद → यो वेद (अः + घोष → ओ) · सः + भिषग्वरः → स भिषग्वरः (सः का विसर्ग व्यंजन से पहले लुप्त) · भिषज् + वरः → भिषग्वरः (ज् → ग्)।",
        "chunks": "तेषां कर्मसु बाह्येषु | योगमाभ्यन्तरेषु च ‖ संयोगं च प्रयोगं च | यो वेद स भिषग्वरः।",
    },
}


IMAGE_SPECS = {
    ("28", "seesaw"): {
        "file": "ch4-two-purposes-28.svg",
        "alt": "Table of verse 28 with two rows: the dull (manda) are served with practical use, and the wise (budha) with growth of the intellect.",
        "type": "table",
        "title": "श्लोक २८: दो जोड़ियाँ",
        "heads": ["किसके लिए", "किसलिए"],
        "rows": [["मन्द (धीमे)", "व्यवहार (उपयोग)"],
                 ["बुध (बुद्धिमान्)", "बुद्धि की वृद्धि"]],
    },
    ("29", "chain"): {
        "file": "ch4-best-physician-29.svg",
        "alt": "Chain of four boxes for verse 29: yoga, saṃyoga, prayoga, and the one who knows them is the best of physicians.",
        "type": "chain",
        "title": "श्लोक २९: श्रेष्ठ वैद्य",
        "steps": ["योग: प्रयोग-योग (उपयोग)", "संयोग: मेल",
                  "प्रयोग: देना, व्यवहार में लाना",
                  "जो जानता है, वह भिषग्वर"],
    },
}
