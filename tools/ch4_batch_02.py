from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}
NOTES_HI = {}
AIDS = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातः षड्विरेचनशताश्रितीयम्",
    "question": "How does this chapter announce itself, and what is it called?",
    "rule": ("अथातः षड्विरेचनशताश्रितीयमध्यायं व्याख्यास्यामः = 'Now, therefore, we shall "
             "expound the chapter called Ṣaḍvirecanaśatāśritīya.' The data glosses the title "
             "as 'concerning the six hundred purgatives'."),
    "limits": ("This is only the opening formula: it names the chapter and promises an "
               "exposition, and gives no teaching yet. The data says the exact force of "
               "-आश्रितीय in the title is a little loose, and the edition's footnote has a "
               "variant title षड्विरेचनशतीयम्."),
    "explain_hi": ("यह अध्याय का आरम्भ-वाक्य है, अध्यायों के खुलने का बँधा हुआ साँचा। ‘अथ’ का अर्थ ‘अब’ और "
                   "‘अतः’ का अर्थ ‘इसलिए’ है; दोनों मिलकर ‘अथातः’ बनते हैं। ‘षड्विरेचनशताश्रितीयम्’ अध्याय का नाम है, "
                   "जिसे डेटा ‘छह सौ विरेचनों से सम्बन्धित’ के भाव में लेता है, और ‘अध्यायम्’ द्वितीया एकवचन है, "
                   "यानी वह वस्तु जिसे समझाया जाना है। ‘व्याख्यास्यामः’ उत्तम पुरुष बहुवचन भविष्य है: ‘हम समझाएँगे’। "
                   "इस वाक्य में अभी कोई उपदेश नहीं है।"),
    "hook": "अथ – अतः – व्याख्यास्यामः: ‘अब – इसलिए – हम समझाएँगे’; नाम = छह सौ विरेचनों वाला अध्याय।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The sentence अथातः षड्विरेचनशताश्रितीयमध्यायं व्याख्यास्यामः opens a chapter. What does it announce?",
            ("The chapter Ṣaḍvirecanaśatāśritīya will now be expounded",
             "The title stands before अध्यायम् and व्याख्यास्यामः promises the exposition."),
            [("A royal command to start a journey", "Nothing in the sentence concerns a king or a journey."),
             ("A list of the six hundred formulas with their doses", "No formula and no dose is named in this sentence."),
             ("The names of the six sources of the formulas", "No source is named here; the sentence only introduces the chapter.")],
            "अध्यायम् (chapter) and व्याख्यास्यामः (we shall expound) show that a chapter is being introduced.",
            "The opening sentence names the chapter and promises to explain it."),
        match(1, "Match each word of the opening sentence to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["अध्यायम्", "chapter"],
               ["व्याख्यास्यामः", "we shall expound"]],
              "These four words carry the whole announcement.",
              "अथ = now; अतः = therefore; अध्यायम् = chapter; व्याख्यास्यामः = we shall expound."),
        fill(2, "The first member of the chapter's title means 'six'. Type that word in Devanagari: ____",
             ["षड्", "षट्", "षड", "षट"],
             "The title begins with the word for 'six', which is षट् and is printed षड् before the voiced व.",
             "A final ट् is written ड् before a voiced sound, so षट् + विरेचन is printed षड्विरेचन.",
             "षट् (six) turns to षड् before a voiced letter: षड्विरेचन."),
        mcq("discriminate", 3, "Which is the right split of अथातः?",
            ("अथ + अतः", "अ + अ gives आ, so अथ + अतः is written अथातः."),
            [("अथा + तः", "There is no word तः in this sentence."),
             ("अथ + आतः", "आतः is not a word here."),
             ("अ + थातः", "थातः is not a word.")],
            "अथातः is अथ ('now') + अतः ('therefore') joined by sandhi.",
            "अथातः = अथ + अतः (अ + अ → आ)."),
        multi("apply", 4, "Which of these statements about the opening sentence are right?",
              [("व्याख्यास्यामः is first person plural future: 'we shall expound'",
                "Right: the data labels it first person plural future."),
               ("अध्यायम् is accusative: the chapter is what is to be expounded",
                "Right: the data labels it masculine accusative singular."),
               ("The title is glossed 'concerning the six hundred purgatives'",
                "Right: that is the data's gloss of the title."),
               ("The sentence says who the speaker is",
                "The speaker is named in the next unit, not in this sentence."),
               ("The sentence lists the six hundred purgatives",
                "It only names the chapter; no purgative is listed.")],
              [0, 1, 2],
              "The first three statements are in the sentence or its glosses; the last two are not.",
              "Unit 1: the formula, the title and the promise to expound."),
        mcq("transfer", 5,
            "A made-up chapter opens अथातो दशकषायीयमध्यायं व्याख्यास्यामः. Which word names that chapter?",
            ("दशकषायीयम्", "The title stands just before अध्यायम्, as the long title does here."),
            [("व्याख्यास्यामः", "That is the verb 'we shall expound'."),
             ("अध्यायम्", "That is the word for 'chapter', not its name."),
             ("अथातः", "That is the opening 'now, therefore'.")],
            "In this frame the title sits just before अध्यायम्; the rest of the sentence is the same formula.",
            "The opening frame is shared; the chapter's name stands before अध्यायम्.",
            teaches="Once you know the frame, you can find a chapter's title by looking at the word before अध्यायम्."),
    ],
}

NOTES_HI["1"] = ("संधियाँ जाँची: अथ + अतः → अथातः (अ + अ → आ); षट् + विरेचन → षड्विरेचन (अन्तिम ट् घोष वर्ण व से पहले ड्); "
                 "शत + आश्रितीयम् → शताश्रितीयम् (अ + आ → आ); अन्तिम म् अगले स्वर से सटा है (…ीयमध्यायं), और ‘अध्यायं’ वही "
                 "‘अध्यायम्’ का अनुस्वार वाला छपा रूप है। पाठभेद: संस्करण की पाद-टिप्पणी में नाम का दूसरा पाठ ‘षड्विरेचनशतीयम्’ दिया है। "
                 "डेटा की टिप्पणी: ‘-आश्रितीय’ का सटीक भाव थोड़ा ढीला है। कोई पाठ-दोष नहीं दिया गया।")

AIDS["1"] = {
    "frame": "क्या: अध्याय का आरम्भ-वाक्य · नाम: षड्विरेचनशताश्रितीय · क्रिया: व्याख्यास्यामः (हम समझाएँगे)।",
    "diagram": {"groups": [
        {"label": "वाक्य",
         "items": ["अथातः", "षड्विरेचनशताश्रितीयमध्यायं", "व्याख्यास्यामः"]}]},
    "sandhi": "अ + अ → आ: अथ + अतः → अथातः। घोष वर्ण से पहले ट् → ड्: षट् + विरेचन → षड्विरेचन। अ + आ → आ: शत + आश्रितीयम् → शताश्रितीयम्।",
    "anchors": "षड्विरेचनशताश्रितीयम् = षट् (छह) + विरेचन + शत (सौ) + आश्रितीय: डेटा के अनुसार ‘छह सौ विरेचनों से सम्बन्धित’ · व्याख्यास्यामः = उत्तम पुरुष बहुवचन भविष्य: ‘हम समझाएँगे’।",
    "chunks": "अथातः षड्विरेचनशताश्रितीयमध्यायं | व्याख्यास्यामः।",
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "इति ह स्माह भगवानात्रेयः",
    "question": "Who is said to have spoken, and what is the formula इति ह स्माह?",
    "rule": ("इति ह स्माह भगवानात्रेयः = 'Thus indeed spoke the venerable Ātreya.' "
             "ह स्म with the perfect आह is a stock formula of reported speech; the "
             "speaker भगवान् आत्रेयः is in the nominative."),
    "limits": ("The verse names the speaker and nothing else: no teaching and no "
               "formula yet. It is a unit of its own, a short reporting line, and the "
               "teaching it introduces comes in the units that follow."),
    "explain_hi": ("यह छोटा-सा वाक्य बताता है कि आगे का उपदेश किसने कहा: ‘भगवान् आत्रेय’। "
                   "‘इति ह स्माह’ बँधा हुआ साँचा है, ‘ऐसा निश्चय ही कहा’; डेटा की टिप्पणी के अनुसार ‘स्म’ का आह के साथ "
                   "प्रयोग कथन को आगे रखने का स्थिर रूप है। ‘आह’ लिट् लकार का प्रथम पुरुष एकवचन है (‘उसने कहा’), "
                   "और ‘भगवान् आत्रेयः’ कर्ता है, प्रथमा एकवचन।"),
    "hook": "इति ह स्माह = ‘ऐसा निश्चय ही कहा’; कर्ता = भगवान् आत्रेय।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In इति ह स्माह भगवानात्रेयः, who is the speaker?",
            ("The venerable Ātreya", "भगवान् आत्रेयः is the subject of आह, 'said'."),
            [("The physician who prepares the formulas", "No physician is mentioned in this verse."),
             ("A pupil asking a question", "No pupil and no question appear here."),
             ("The reader of the chapter", "The reader is not named; the speaker is Ātreya.")],
            "आह is the verb 'said' and भगवान् आत्रेयः is its subject.",
            "Unit 2: the speaker is named as भगवान् आत्रेयः."),
        match(1, "Match each word of this unit to its meaning.",
              [["इति", "thus"], ["ह", "indeed"], ["आह", "said"], ["भगवान्", "the venerable"]],
              "The four words give 'Thus indeed said the venerable Ātreya'.",
              "इति = thus; ह = indeed; आह = said; भगवान् = the venerable."),
        fill(2, "The verb meaning 'said' in this unit is ____ (type it in Devanagari, without स्म).",
             ["आह"],
             "The verb is आह, which joins the particle स्म to give स्माह.",
             "आह is third person singular perfect; the speaker stands in the nominative.",
             "आह = he said; the subject stands in the nominative."),
        mcq("discriminate", 3, "Which is the right split of भगवानात्रेयः?",
            ("भगवान् + आत्रेयः", "The final न् of भगवान् stands before the vowel आ and simply joins it."),
            [("भगवा + नात्रेयः", "नात्रेयः is not a word."),
             ("भगवान् + अत्रेयः", "न् + अ would give नत्रेयः; the name here has a long आ."),
             ("भगवानः + आत्रेयः", "भगवान् is the nominative singular; it has no visarga ending.")],
            "भगवानात्रेयः is two words, भगवान् ('the venerable') and आत्रेयः.",
            "भगवानात्रेयः = भगवान् + आत्रेयः."),
        mcq("apply", 4, "What does ह स्म together with the verb आह do in this line?",
            ("It forms a stock formula of reported speech",
             "The data says 'sma' with the perfect आह is a stock formula of reported speech."),
            [("It asks a question", "Nothing in the line is a question."),
             ("It gives a command", "आह is a statement, 'said', not a command."),
             ("It names a second speaker", "Only one speaker, Ātreya, is named.")],
            "इति ह स्माह is the fixed frame of a reported statement; the speaker follows in the nominative.",
            "इति ह स्माह = the stock frame 'thus indeed said'."),
        mcq("transfer", 5,
            "A made-up line reads इति ह स्माह गुरुः. What does it say?",
            ("Thus indeed said the teacher", "The frame is the same as here, with गुरुः as nominative subject."),
            [("Thus indeed the teacher will say", "आह is past, 'said'; it is not a future."),
             ("Thus indeed the teacher asked", "आह means 'said', not 'asked'."),
             ("Thus indeed the teacher listened", "No verb of listening occurs; the verb is आह.")],
            "After इति ह स्माह the speaker follows in the nominative; here गुरुः.",
            "After इति ह स्माह the speaker's name follows in the nominative.",
            teaches="You can find the speaker of any such report by looking for the nominative after आह."),
    ],
}

NOTES_HI["2"] = ("संधियाँ जाँची: स्म + आह → स्माह (अ + आ → आ); भगवान् + आत्रेयः → भगवानात्रेयः (अन्तिम न् अगले स्वर से सट जाता है, कोई परिवर्तन नहीं)। "
                 "डेटा की टिप्पणी: ‘ह स्म आह’ में ‘स्म’ का लिट् ‘आह’ के साथ प्रयोग कथन का बँधा हुआ साँचा है (डेटा में ‘स्म’ का गुण ‘भूतकालिक निपात’ लिखा है)। "
                 "इस श्लोक में कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["2"] = {
    "frame": "क्या कहा: (आगे का उपदेश) · किसने: भगवान् आत्रेय · साँचा: इति ह स्माह = ऐसा निश्चय ही कहा।",
    "diagram": {"groups": [
        {"label": "वाक्य",
         "items": ["इति", "ह", "स्माह", "भगवानात्रेयः"]}]},
    "sandhi": "अ + आ → आ: स्म + आह → स्माह। न् + स्वर: भगवान् + आत्रेयः → भगवानात्रेयः (न् अगले स्वर से सटा)।",
    "anchors": "इति = ऐसा · ह = निश्चय ही · स्म + आह = बँधा साँचा ‘कहा’ · भगवान् आत्रेयः = कर्ता (प्रथमा एकवचन)।",
    "chunks": "इति ह स्माह | भगवानात्रेयः।",
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "इह खलु षड् विरेचनशतानि भवन्ति",
    "question": "What does this summary sentence count, and what is its closing word?",
    "rule": ("इह खलु षड् विरेचनशतानि भवन्ति … इति संग्रहः: six hundred purgatives, six supports, "
             "five sources of kaṣāya, a fivefold preparation, fifty great kaṣāyas, five hundred "
             "kaṣāyas. The verb भवन्ति is understood after the first clause."),
    "limits": ("This is only a count: it names no support, no source and no preparation, and "
               "gives no drug or dose. It does not say how the fifty and the five hundred relate. "
               "The data notes that the verb is understood, not printed, after the first item."),
    "explain_hi": ("यह पूरे अध्याय का संग्रह है, यानी गिनती की संक्षिप्त सूची; अन्त में वाक्य स्वयं ‘इति संग्रहः’ कहता है। "
                   "इसमें छह बातें गिनाई गई हैं: छह सौ विरेचन, विरेचन के छह आश्रय, कषाय की पाँच योनियाँ, कषाय-कल्पना पाँच प्रकार की, "
                   "पचास महाकषाय और पाँच सौ कषाय। ‘भवन्ति’ क्रिया केवल पहले खण्ड में छपी है; बाकी में वह समझी जाती है। "
                   "यहाँ कोई नाम या औषधि नहीं दी गई, केवल संख्याएँ। ‘पञ्चाशन्महाकषायाः’ में पञ्चाशत् का त् म से पहले न् बन गया है।"),
    "hook": "६०० विरेचन · ६ आश्रय · ५ योनि · ५ कल्पना · ५० महाकषाय · ५०० कषाय: ‘इति संग्रहः’।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What kind of sentence is unit 3?",
            ("A summary that counts the chapter's topics and ends with इति संग्रहः",
             "The sentence lists numbers of topics and closes by calling itself the summary."),
            [("A story about the speaker's pupils", "No pupil and no story appear in the sentence."),
             ("A recipe with doses of one formula", "No formula and no dose is given."),
             ("A prayer at the end of the chapter", "It is a count, and it stands near the start of the chapter.")],
            "The sentence gives a number for each topic and ends with 'thus, the summary'.",
            "Unit 3: a counted summary (संग्रहः) of six topics."),
        match(1, "Match each topic of the summary to its number.",
              [["विरेचनशतानि", "six hundred"], ["विरेचनाश्रयाः", "six"],
               ["कषाययोनयः", "five"], ["महाकषायाः", "fifty"], ["कषायशतानि", "five hundred"]],
              "Each topic comes with its number in the sentence.",
              "विरेचनशतानि = 600; विरेचनाश्रयाः = 6; कषाययोनयः = 5; महाकषायाः = 50; कषायशतानि = 500."),
        fill(2, "The word that closes the sentence and names it a 'summary' is ____ (type it in Devanagari).",
             ["संग्रहः", "संग्रह", "सङ्ग्रहः", "सङ्ग्रह"],
             "The sentence ends with इति संग्रहः, 'thus, the summary'.",
             "संग्रहः is nominative singular: it names what the sentence itself is.",
             "इति संग्रहः = 'this is the summary'."),
        mcq("discriminate", 3, "Which is the right split of पञ्चाशन्महाकषायाः?",
            ("पञ्चाशत् + महाकषायाः", "A final त् becomes the nasal न् before the nasal म."),
            [("पञ्चाश + न्महाकषायाः", "न्महाकषायाः is not a word."),
             ("पञ्चाशत् + अहाकषायाः", "There is no word अहाकषायाः; the second word is महाकषायाः."),
             ("पञ्च + आशन्महाकषायाः", "आशन्महाकषायाः is not a word; पञ्चाशत् means 'fifty'.")],
            "पञ्चाशत् ('fifty') + महाकषायाः ('great kaṣāyas') joined by sandhi.",
            "पञ्चाशत् + महा… → पञ्चाशन्महा… (त् → न् before म)."),
        multi("apply", 4, "Which of these things does unit 3 itself say?",
              [("There are six supports of purgation",
                "Right: षड् विरेचनाश्रयाः."),
               ("There are five sources of kaṣāya",
                "Right: पञ्च कषाययोनयः."),
               ("There are fifty great kaṣāyas",
                "Right: पञ्चाशन्महाकषायाः."),
               ("The six supports are milk, root, bark, leaf, flower and fruit",
                "Not in this unit; the supports are named in unit 5."),
               ("Each source of kaṣāya is a taste",
                "Not in this unit; the sources are named in unit 6.")],
              [0, 1, 2],
              "The first three are counts printed here; the supports and sources are named in later units.",
              "Unit 3 counts the topics; naming them comes in the units that follow."),
        mcq("transfer", 5,
            "A made-up sentence reads इह खलु सप्त फलानि भवन्ति, पञ्च पत्राणि, इति संग्रहः. How is पञ्च पत्राणि read?",
            ("There are five leaves, with भवन्ति understood",
             "As in unit 3, the verb is printed once and understood in the later clauses."),
            [("Five leaves, but with no verb at all", "The verb भवन्ति from the first clause carries over."),
             ("Seven leaves, the number being repeated", "The number is पञ्च, five, not सप्त."),
             ("Five fruits instead of seven", "The noun is पत्राणि, leaves, not फलानि.")],
            "The first clause carries the verb; the next clauses give only a number and a noun.",
            "In a counted summary the verb भवन्ति is printed once and understood after it.",
            teaches="You can read a bare 'number + noun' clause in a summary by supplying the verb from the first clause."),
    ],
}

NOTES_HI["3"] = ("संधियाँ जाँची: पञ्चाशत् + महाकषायाः → पञ्चाशन्महाकषायाः (त् → न् नासिक्य म से पहले); ‘षड् विरेचनशतानि’ में षट् का ट् घोष व से पहले ड् है; "
                 "‘पञ्चविधं कषायकल्पनं’ में अन्त के म् का अनुस्वार रूप छपा है। डेटा की टिप्पणी: ‘विरेचनशतानि’ का शाब्दिक अर्थ ‘विरेचनों के सैकड़े’ है "
                 "(यानी छह सौ), और वाक्य अधूरा-सा है: पहले खण्ड के बाद ‘भवन्ति’ आगे के खण्डों में समझा जाता है। कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["3"] = {
    "frame": "क्या: अध्याय का संग्रह (गिनती) · छह बातें · क्रिया ‘भवन्ति’ पहले खण्ड के बाद समझी हुई · नाम और औषधि इस इकाई में नहीं।",
    "diagram": {"groups": [
        {"label": "गिनती का क्रम",
         "items": ["षड् विरेचनशतानि", "षड् विरेचनाश्रयाः", "पञ्च कषाययोनयः", "पञ्चविधं कषायकल्पनं",
                   "पञ्चाशन्महाकषायाः", "पञ्च कषायशतानि", "इति संग्रहः"]}]},
    "pegs": "मेरा बनाया स्मरण-सूत्र (वाक्य का दावा नहीं): विरेचनशतानि छह सौ · आश्रय छह · योनि पाँच · कल्पन पाँच प्रकार · महाकषाय पचास · कषायशतानि पाँच सौ — ‘छह सौ, छह; पाँच, पाँच; पचास, पाँच सौ’।",
    "sandhi": "त् + म → न्म: पञ्चाशत् + महाकषायाः → पञ्चाशन्महाकषायाः। ट् + घोष → ड्: षट् + विरेचन… → षड् विरेचन…।",
    "anchors": "संग्रहः = संक्षिप्त सूची · विरेचनशतानि = विरेचनों के सैकड़े (छह सौ) · योनयः = स्रोत · महाकषायाः = बड़े कषाय (वर्ग)।",
    "chunks": "इह खलु षड् विरेचनशतानि भवन्ति | षड् विरेचनाश्रयाः | पञ्च कषाययोनयः | पञ्चविधं कषायकल्पनं | पञ्चाशन्महाकषायाः | पञ्च कषायशतानि | इति संग्रहः।",
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "षड् विरेचनशतानि, इति यदुक्तम्",
    "question": "What does unit 4 promise, and how does it close the count of six hundred?",
    "rule": ("Unit 4 takes up 'six hundred purgatives' again, promises the detail in the "
             "Kalpa-upaniṣad, and lists drugs with the number of formulations each yields, "
             "ending इति षड्विरेचनशतानि."),
    "limits": ("Names and numbers only: no use, no effect, no dose, no plant identification. The data says "
               "the fruits' 133 and the 110 for śyāmā and trivṛt are inferred from the total 600; no "
               "question rests on either. Which section the Kalpa-upaniṣad is, is not said."),
    "explain_hi": ("यह इकाई ‘छह सौ विरेचन’ वाली बात को फिर उठाती है: यहाँ संक्षेप में गिनाकर विस्तार से ‘कल्पोपनिषद्’ में समझाने का वचन है। "
                   "फिर कई औषधियों के साथ उनके योगों की संख्या दी गई है: जीमूतक में उनतालीस, इक्ष्वाकु में पैंतालीस, धामार्गव साठ प्रकार का, "
                   "कुटज अठारह प्रकार से योग को प्राप्त होता है, चतुरङ्गुल बारह प्रकार से, लोध्र सोलह योगों से युक्त, महावृक्ष बीस योगों से युक्त, "
                   "सप्तला-शङ्खिनी के उनतालीस और दन्ती-द्रवन्ती के अड़तालीस। अन्त में ‘इति षड्विरेचनशतानि’ कहकर कुल छह सौ का निष्कर्ष दिया गया है। "
                   "यह एक लम्बा वाक्य है जिसमें औषधि-नाम और संख्याएँ ही हैं, उपयोग या मात्रा नहीं।"),
    "hook": "‘छह सौ’ का विस्तार कल्पोपनिषद् में; औषधि-दर-औषधि संख्या; अन्त: इति षड्विरेचनशतानि।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does unit 4 say it will do with the phrase 'six hundred purgatives'?",
            ("Cite it here in summary and expound it in detail in the Kalpa-upaniṣad",
             "The unit says it cites the phrase here briefly and explains it in detail in the Kalpa-upaniṣad."),
            [("Drop it, since the matter is settled in unit 3", "The unit takes the phrase up again and promises detail."),
             ("Explain it only by the dose of each drug", "No dose is given anywhere in the unit."),
             ("Replace it with the figure of five hundred", "The unit ends with six hundred, इति षड्विरेचनशतानि.")],
            "The unit says: what was said as 'six hundred purgatives' is cited here and expounded in detail in the Kalpa-upaniṣad.",
            "Unit 4 returns to the six hundred, promises detail, and gives the figures drug by drug."),
        match(1, "Match each drug of unit 4 to the number said of it.",
              [["धामार्गवः", "sixty-fold"], ["कुटजः", "eighteen-fold"],
               ["चतुरङ्गुलः", "twelve-fold"], ["लोध्रम्", "sixteen formulations"],
               ["महावृक्षः", "twenty formulations"]],
              "The unit gives each of these a number: -धा 'fold' or 'with N formulations'.",
              "धामार्गवः 60; कुटजः 18; चतुरङ्गुलः 12; लोध्रम् 16; महावृक्षः 20."),
        fill(2, "The unit closes: इति ____ (the total, one compound word in Devanagari, 'six hundred purgatives').",
             ["षड्विरेचनशतानि", "षड् विरेचनशतानि"],
             "The last words are इति षड्विरेचनशतानि, 'thus, the six hundred purgatives'.",
             "The closing इति repeats the total with which the unit began.",
             "इति + total: the closing repeats the number that the unit explains."),
        mcq("discriminate", 3, "Which is the right split of कुटजस्त्वष्टादशधा?",
            ("कुटजः + तु + अष्टादशधा",
             "The visarga before त is written स्, and the u of तु becomes व् before the vowel अ."),
            [("कुटज + स्तु + अष्टादशधा", "स्तु is not a word here; the particle is तु."),
             ("कुटजः + तु + आष्टादशधा", "The number word is अष्टादश, eighteen, with a short अ."),
             ("कुटजस् + त्व + अष्टादशधा", "त्व is not a word; the particle is तु and its उ turns to व् before the vowel.")],
            "कुटजः ('kuṭaja') + तु ('but') + अष्टादशधा ('eighteen-fold') joined by sandhi.",
            "Visarga + त → स्त; तु + अ → त्व."),
        multi("apply", 4, "Which of these statements about unit 4 are right?",
              [("Caturaṅgula is said to enter into formulation twelve ways",
                "Right: चतुरङ्गुलो द्वादशधा योगमेति."),
               ("Lodhra is said to be joined with sixteen formulations",
                "Right: लोध्रं विधौ षोडशयोगयुक्तम्."),
               ("The unit promises detailed exposition in the Kalpa-upaniṣad",
                "Right: कल्पोपनिषदि व्याख्यास्यामः."),
               ("The unit gives the dose of each drug",
                "No dose is given anywhere in the unit."),
               ("The unit says what each drug does to the body",
                "No effect or use is stated in the unit.")],
              [0, 1, 2],
              "The first three are stated in the unit; no dose or effect appears.",
              "Unit 4 gives names and numbers of formulations only."),
        mcq("transfer", 5,
            "A made-up line reads नवलता पञ्चदशधा योगमेति. By the pattern of कुटजो ऽष्टादशधा योगमेति, how many ways does नवलता enter into formulation?",
            ("Fifteen ways", "पञ्चदश is fifteen, and -धा means '-fold', as अष्टादशधा means eighteen-fold."),
            [("Five ways", "पञ्च alone is five; पञ्चदश is fifteen."),
             ("Fifty ways", "Fifty is पञ्चाश; the word here is पञ्चदश."),
             ("Ten ways", "दश is ten, but पञ्चदश is the compound five + ten, fifteen.")],
            "Number + -धा names the number of ways; the verb योगमेति is the same as in the unit.",
            "Number + धा + योगमेति: 'enters into formulation N ways'.",
            teaches="Read the number in a '-धा' word to learn in how many ways a drug is said to enter formulation."),
    ],
}

NOTES_HI["4"] = ("संधियाँ जाँची: संग्रहेण + उदाहृत्य → संग्रहेणोदाहृत्य (अ + उ → ओ); कुटजः + तु → कुटजस्तु (विसर्ग + त → स्त) और तु + अष्टादशधा → त्वष्टादशधा "
                 "(उ → व् स्वर से पहले); च + अत्र → चात्र (अ + अ → आ); चतुरङ्गुलः + द्वादशधा → चतुरङ्गुलो द्वादशधा (अः + घोष → ओ); "
                 "एकोनचत्वारिंशत् + जीमूतकेषु → …ज्जीमूतकेषु (त् → ज् घोष ज से पहले); सप्तलाशङ्खिन्योः + योगाः → …शङ्खिन्योर्योगाः (ओः + घोष → ओर्)। "
                 "डेटा की टिप्पणियाँ: (१) फलों के लिए ‘त्रयस्त्रिंशद्योगशतम्’ का १३३ पाठ व्याकरण से नहीं, कुल ६०० की जाँच से चुना गया है; (२) ‘श्यामात्रिवृद्योगशतम्’ + "
                 "‘दशापरे’ से ११० अनुमान है; (३) ‘कल्पोपनिषदि’ का कौन-सा खण्ड, पाठ नहीं बताता; (४) ‘विधौ’ अस्पष्ट है; (५) कुछ खण्डों में ‘योगाः’ समझा हुआ है। "
                 "पाठ-स्थिति: संस्करण में यह अंश कोष्ठक में छपा है (प्रक्षिप्त या वैकल्पिक हो सकता है), और स्रोत में एक भटका हुआ ‘&’ था जिसे हटाया गया, शब्द-विभाजन जाँचने योग्य है।")

AIDS["4"] = {
    "frame": "क्या: ‘छह सौ’ का संक्षिप्त उदाहरण और विस्तार का वचन · औषधि → संख्या · अन्त: इति षड्विरेचनशतानि · उपयोग/मात्रा नहीं।",
    "sandhi": "अ + उ → ओ: संग्रहेण + उदाहृत्य → संग्रहेणोदाहृत्य। विसर्ग + त → स्त और उ → व्: कुटजः + तु + अष्टादशधा → कुटजस्त्वष्टादशधा। अः + घोष → ओ: चतुरङ्गुलः + द्वादशधा → चतुरङ्गुलो द्वादशधा। त् + ज → ज्ज: एकोनचत्वारिंशत् + जीमूतकेषु → एकोनचत्वारिंशज्जीमूतकेषु।",
    "anchors": "-धा = ‘-गुना / इतने प्रकार’: षष्टिधा = साठ प्रकार, अष्टादशधा = अठारह प्रकार, द्वादशधा = बारह प्रकार · योगमेति = योग को प्राप्त होता है · योगयुक्तः = योगों से युक्त · कल्पोपनिषदि = ‘कल्प-उपनिषद्’ में (सप्तमी)।",
    "chunks": "षड् विरेचनशतानि इति यदुक्तं | तदिह संग्रहेणोदाहृत्य | विस्तरेण कल्पोपनिषदि व्याख्यास्यामः ‖ … ‖ इति षड्विरेचनशतानि।",
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "षड् विरेचनाश्रयाः",
    "question": "What are the six supports of purgation, and how does the sentence name them?",
    "rule": ("षड् विरेचनाश्रया इति क्षीरमूलत्वक्पत्रपुष्पफलानीति = 'The six supports of purgation are "
             "milk, root, bark, leaf, flower, fruit.' The six names are joined in one compound."),
    "limits": ("Six names only; the sentence gives no drug, no dose and no use. The data renders "
               "क्षीर literally as 'milk' and says the Sanskrit does not state whether it means plant "
               "latex or sap. No question depends on that."),
    "explain_hi": ("यह इकाई, इकाई ३ में गिनाए ‘विरेचन के छह आश्रय’ के नाम बताती है: क्षीर, मूल, त्वक्, पत्र, पुष्प और फल। "
                   "छहों नाम एक ही द्वन्द्व समास में जुड़े हैं: ‘क्षीरमूलत्वक्पत्रपुष्पफलानि’, जिसके अन्त के नपुंसक बहुवचन ‘-आनि’ के बाद ‘इति’ आता है। "
                   "‘क्षीर’ का शाब्दिक अर्थ ‘दूध’ है; वह पौधे का दूधिया रस है या नहीं, यह संस्कृत नहीं बताती। "
                   "‘विरेचनाश्रयाः’ के बाद विसर्ग इति से पहले लुप्त होकर ‘विरेचनाश्रया इति’ छपा है।"),
    "hook": "छह आश्रय: क्षीर · मूल · त्वक् · पत्र · पुष्प · फल।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does unit 5 name?",
            ("The six supports of purgation: milk, root, bark, leaf, flower and fruit",
             "The sentence expands 'six supports' into six names."),
            [("The five tastes of kaṣāya", "The tastes come in unit 6, not here."),
             ("The five preparations of kaṣāya", "The preparations come in unit 7."),
             ("The fifty classes of drugs", "The classes are named from unit 8.")],
            "The supports counted in unit 3 are named here.",
            "Unit 5 names the six supports counted in unit 3."),
        order(1, "Put the six supports in the order the sentence gives them.",
              ["क्षीर", "मूल", "त्वक्", "पत्र", "पुष्प", "फल"],
              "The compound reads milk, root, bark, leaf, flower, fruit.",
              "क्षीर, मूल, त्वक्, पत्र, पुष्प, फल: the order of the compound."),
        fill(2, "In the compound, the support that means 'bark' is ____ (type it in Devanagari).",
             ["त्वक्", "त्वच्", "त्वग्"],
             "The third member of the compound is त्वक्, 'bark'.",
             "The compound joins six bare words and puts the plural ending on the last one.",
             "क्षीर + मूल + त्वक् + पत्र + पुष्प + फलानि: six names, one ending."),
        mcq("discriminate", 3, "Why is the word printed विरेचनाश्रया इति and not विरेचनाश्रयाः इति?",
            ("The visarga after आ drops before the vowel इ",
             "Before a vowel, a visarga that follows आ is dropped."),
            [("The visarga turns to ओ before the vowel इ", "A visarga turns to ओ only after अ and before a voiced consonant."),
             ("The word is a dual, which has no visarga", "The word is nominative plural, 'supports'."),
             ("The two words have been written as one", "The two words are written separately: विरेचनाश्रया and इति.")],
            "विरेचनाश्रयाः + इति → विरेचनाश्रया इति.",
            "आः + vowel → आ + vowel (the visarga drops)."),
        multi("apply", 4, "Which of these are among the six supports named in unit 5?",
              [("मूल", "Right: it is the second member."),
               ("पुष्प", "Right: it is the fifth member."),
               ("फल", "Right: it is the last member."),
               ("बीज", "Not named; the six are क्षीर, मूल, त्वक्, पत्र, पुष्प, फल."),
               ("काण्ड", "Not named in this sentence.")],
              [0, 1, 2],
              "The first three are in the compound; बीज and काण्ड are not among the six.",
              "A listed item belongs only if the sentence names it."),
        mcq("transfer", 5,
            "A made-up line is पञ्च गृहाश्रया इति द्वारभित्तिस्तम्भच्छदपीठानीति. Which part carries the list of items?",
            ("द्वारभित्तिस्तम्भच्छदपीठानि, the long compound before इति",
             "As with the supports in unit 5, the items are joined in one compound with the ending on the last member."),
            [("पञ्च, the number", "That is the count, not the list."),
             ("गृहाश्रयाः, the heading word", "That is the heading, like विरेचनाश्रयाः."),
             ("The word इति alone", "इति only closes the quoted heading and the list.")],
            "The sentence has the same shape as unit 5: number and heading, then इति, then the compound of items.",
            "Heading 'N X', then इति, then one compound of the items.",
            teaches="A long compound after such a heading can be read as the list of items it promises."),
    ],
}

NOTES_HI["5"] = ("संधियाँ जाँची: षट् → षड् (घोष व से पहले); विरेचनाश्रयाः + इति → विरेचनाश्रया इति (आः के बाद स्वर से पहले विसर्ग लुप्त); "
                 "फलानि + इति → फलानीति (इ + इ → ई)। ‘क्षीरमूलत्वक्पत्रपुष्पफलानि’ द्वन्द्व है, विभक्ति केवल अन्तिम पद पर। "
                 "डेटा की टिप्पणी: ‘क्षीर’ का शाब्दिक अर्थ ‘दूध’ है; वह पौधे का दूधिया रस है या नहीं, यह संस्कृत में नहीं कहा गया। "
                 "कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["5"] = {
    "frame": "क्या: विरेचन के छह आश्रय (इकाई ३ की गिनती का नाम-सहित रूप) · एक द्वन्द्व समास · उपयोग/मात्रा नहीं।",
    "diagram": {"groups": [
        {"label": "वाक्य",
         "items": ["षड्", "विरेचनाश्रया", "इति", "क्षीरमूलत्वक्पत्रपुष्पफलानीति"]}]},
    "sandhi": "ट् → ड्: षट् + विरेचन… → षड् विरेचन…। आः + स्वर → आ: विरेचनाश्रयाः + इति → विरेचनाश्रया इति। इ + इ → ई: फलानि + इति → फलानीति।",
    "anchors": "क्षीर-मूल-त्वक्-पत्र-पुष्प-फलानि = दूध, जड़, छाल, पत्ता, फूल, फल (द्वन्द्व; विभक्ति केवल अन्त में) · आश्रय = सहारा / आधार।",
    "chunks": "षड् विरेचनाश्रया इति | क्षीर-मूल-त्वक्-पत्र-पुष्प-फलानीति।",
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "पञ्च कषाययोनयः",
    "question": "What are the five sources of kaṣāya named in unit 6, and what is the last name?",
    "rule": ("पञ्च कषाययोनय इति … तन्त्रे संज्ञा = 'There are five sources of kaṣāya': the sweet, "
             "sour, pungent, bitter and kaṣāya-kaṣāya kaṣāya; such is the technical name in the treatise."),
    "limits": ("Five names only: no drug, no use. The data says the Sanskrit does not explain the "
               "two members of कषायकषायः and commentators differ; it is rendered 'astringent "
               "kaṣāya'. The first four could also read 'kaṣāya of the sweet taste'. No question "
               "rests on these readings."),
    "explain_hi": ("यह इकाई इकाई ३ में गिनाई ‘कषाय की पाँच योनियों’ के नाम देती है: मधुरकषाय, अम्लकषाय, कटुकषाय, तिक्तकषाय और कषायकषाय। "
                   "पहले चार नामों में स्वाद का शब्द (मधुर, अम्ल, कटु, तिक्त) ‘कषाय’ से पहले आता है; पाँचवाँ नाम ‘कषायकषायः’ है, जिसके दोनों खण्ड पाठ में समझाए नहीं गए "
                   "और टीकाकार भिन्न मत रखते हैं, इसलिए डेटा इसे ‘कषाय कषाय’ ही रखकर शाब्दिक अर्थ ‘कषैला कषाय’ देता है। "
                   "अन्त में ‘तन्त्रे संज्ञा’ कहता है कि यह तन्त्र की पारिभाषिक संज्ञा है। "
                   "‘मधुरकषायो ऽम्लकषायः’ में ‘ऽ’ लुप्त हुए अ का चिह्न है।"),
    "hook": "पाँच योनि: मधुर · अम्ल · कटु · तिक्त · कषायकषाय — सब ‘…कषायः’।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does unit 6 list under 'five sources of kaṣāya'?",
            ("Five names: sweet, sour, pungent, bitter and kaṣāya-kaṣāya",
             "The five names are listed, each ending in कषायः."),
            [("Five drugs, each with its dose", "No drug and no dose is named in unit 6."),
             ("Five kinds of preparation such as juice and paste", "Those are the preparations of unit 7."),
             ("Five parts of a plant", "The plant parts are the supports of unit 5.")],
            "The sources counted in unit 3 are named here by taste words.",
            "Unit 6 names the five sources of kaṣāya."),
        match(1, "Match each name to the taste word that begins it.",
              [["मधुरकषायः", "sweet"], ["अम्लकषायः", "sour"],
               ["कटुकषायः", "pungent"], ["तिक्तकषायः", "bitter"]],
              "The first member of each of these four names is a taste word.",
              "मधुर = sweet; अम्ल = sour; कटु = pungent; तिक्त = bitter."),
        fill(2, "In कटुकषायः the part meaning 'pungent' is ____ (type it in Devanagari).",
             ["कटु"],
             "कटुकषायः = कटु ('pungent') + कषायः.",
             "The name is a compound whose first member is the taste and whose last is कषायः.",
             "कटु + कषायः = the pungent kaṣāya."),
        mcq("discriminate", 3, "What does the sign ऽ in मधुरकषायो ऽम्लकषायः show?",
            ("A lost अ: मधुरकषायः + अम्लकषायः → मधुरकषायो ऽम्लकषायः",
             "A visarga after अ turns to ओ before a voiced sound, and the following अ is dropped, marked by ऽ."),
            [("A long vowel औ joins the two names", "The vowel is ओ, and ऽ is a mark, not a vowel."),
             ("A break between two verses", "This is one prose sentence; ऽ is a sandhi mark."),
             ("The number five", "ऽ is not a numeral.")],
            "मधुरकषायः + अम्लकषायः → मधुरकषायो ऽम्लकषायः.",
            "अः + अ → ओ ऽ: the following अ is dropped and marked by ऽ."),
        multi("apply", 4, "Which of these statements about unit 6 are right?",
              [("Four of the five names begin with a taste word",
                "Right: मधुर, अम्ल, कटु, तिक्त."),
               ("The last name is कषायकषायः",
                "Right: it is the fifth name."),
               ("The text calls these a technical name in the treatise (तन्त्रे संज्ञा)",
                "Right: the unit ends with तन्त्रे संज्ञा."),
               ("The unit explains what the two members of कषायकषायः mean",
                "The data says the Sanskrit does not explain them."),
               ("The unit says which drug belongs to each source",
                "No drug is named in the unit.")],
              [0, 1, 2],
              "The first three are in the unit; no meaning for कषायकषायः and no drug is given.",
              "Unit 6 names the five sources and calls them a technical name."),
        mcq("transfer", 5,
            "By the same visarga rule as कटुकषायः + तिक्तकषायः → कटुकषायस्तिक्तकषायः, how are रक्तः and तण्डुलः joined?",
            ("रक्तस्तण्डुलः", "A visarga before त is written स्, giving …स्त…."),
            [("रक्तो तण्डुलः", "ओ is for a voiced sound after अ; त is not voiced."),
             ("रक्तश्तण्डुलः", "श् is for च or छ; before त the visarga is स्."),
             ("रक्तःतण्डुलः", "The visarga is not left bare before त; it becomes स्.")],
            "Visarga + त → स् + त, the same rule as in the unit.",
            "Visarga + त → स्त.",
            teaches="You can predict how a visarga before त is printed, in any compound or phrase."),
    ],
}

NOTES_HI["6"] = ("संधियाँ जाँची: कषाययोनयः + इति → कषाययोनय इति (अः के बाद भिन्न स्वर से पहले विसर्ग लुप्त, हिअटस बना रहता है); "
                 "मधुरकषायः + अम्लकषायः → मधुरकषायो ऽम्लकषायः (अः + अ → ओ और अ का लोप ऽ); कटुकषायः + तिक्तकषायः → कटुकषायस्तिक्तकषायः (विसर्ग + त → स्त); "
                 "कषायकषायः + च → कषायकषायश्च (विसर्ग + च → श्च); च + इति → चेति (अ + इ → ए)। "
                 "डेटा की टिप्पणी: ‘कषायकषाय’ के दोनों खण्ड पाठ में समझाए नहीं गए, टीकाकारों में मतभेद है; ‘मधुरकषाय’ आदि को कर्मधारय (मधुर कषाय) पढ़ा गया है, "
                 "दूसरा पाठ ‘मधुर (रस) से बना कषाय’ भी सम्भव है। कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["6"] = {
    "frame": "क्या: कषाय की पाँच योनियाँ (इकाई ३ की गिनती का नाम-सहित रूप) · चार स्वाद-शब्द + कषायकषाय · अन्त: तन्त्रे संज्ञा।",
    "diagram": {"groups": [
        {"label": "वाक्य",
         "items": ["पञ्च", "कषाययोनय", "इति", "मधुरकषायो", "ऽम्लकषायः", "कटुकषायस्तिक्तकषायः",
                   "कषायकषायश्चेति", "तन्त्रे", "संज्ञा"]}]},
    "sandhi": "अः + अ → ओ ऽ: मधुरकषायः + अम्लकषायः → मधुरकषायो ऽम्लकषायः। विसर्ग + त → स्त: कटुकषायः + तिक्तकषायः → कटुकषायस्तिक्तकषायः। विसर्ग + च → श्च और अ + इ → ए: कषायकषायः + च + इति → कषायकषायश्चेति।",
    "anchors": "मधुर = मीठा · अम्ल = खट्टा · कटु = तीखा · तिक्त = कड़वा · कषायकषाय = ‘कषैला कषाय’ (डेटा का शाब्दिक रूप; टीकाकार भिन्न मत रखते हैं)।",
    "chunks": "पञ्च कषाययोनय इति | मधुरकषायो ऽम्लकषायः | कटुकषायस्तिक्तकषायः | कषायकषायश्चेति | तन्त्रे संज्ञा।",
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "पञ्चविधं कषायकल्पनम्",
    "question": "What does unit 7 list under 'fivefold', and what do you notice about the count?",
    "rule": ("पञ्चविधं कषायकल्पनमिति तद्यथा — स्वरसः, कल्कः, शृतः, शीतः, फाण्टः, कषायः: "
             "the heading says fivefold, yet six names follow."),
    "limits": ("The text says 'five' but prints six names, and the data does not resolve this: the "
               "last, कषाय, may be a general term or a separate item. The five glosses follow "
               "standard meanings. No dose and no method is given."),
    "explain_hi": ("यह इकाई, इकाई ३ की ‘पाँच प्रकार की कषाय-कल्पना’ के नाम गिनाती है, पर नाम छह मिलते हैं: स्वरस, कल्क, शृत, शीत, फाण्ट और कषाय। "
                   "शीर्षक ‘पञ्चविधम्’ (पाँच प्रकार) कहता है, इसलिए गिनती मेल नहीं खाती; डेटा इसे जैसा का तैसा रखता है और सुलझाने का प्रयास नहीं करता। "
                   "पहले पाँच के सामान्य अर्थ ये हैं: स्वरस (निचोड़ा रस), कल्क (लुगदी), शृत (उबाला हुआ), शीत (ठण्डा जलीय निष्कर्ष), फाण्ट (गर्म जलीय निष्कर्ष)। "
                   "छठा ‘कषाय’ सामान्य शब्द भी हो सकता है या अलग प्रकार भी; पाठ स्वयं नहीं बताता।"),
    "hook": "‘पाँच’ कहा, छह नाम छपे: स्वरस · कल्क · शृत · शीत · फाण्ट · कषाय।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The heading of unit 7 says पञ्चविधम्, 'fivefold'. How many names does the list after तद्यथा actually print?",
            ("Six names", "स्वरसः, कल्कः, शृतः, शीतः, फाण्टः and कषायः make six."),
            [("Five names, matching the heading", "The list prints a sixth name, कषायः, after the five."),
             ("Four names", "Four would leave out two of the printed names."),
             ("Ten names", "Ten is the size of the drug groups in later units, not of this list.")],
            "The list after तद्यथा prints six names although the heading says fivefold.",
            "Unit 7: a 'fivefold' heading with six printed names."),
        order(1, "Put the names of unit 7 in the order they are printed.",
              ["स्वरसः", "कल्कः", "शृतः", "शीतः", "फाण्टः", "कषायः"],
              "The list runs स्वरसः, कल्कः, शृतः, शीतः, फाण्टः, कषायः.",
              "The printed order: स्वरस, कल्क, शृत, शीत, फाण्ट, कषाय."),
        fill(2, "The sixth and last name printed after तद्यथा is the plain word ____ (type it in Devanagari).",
             ["कषायः", "कषाय"],
             "The list ends with कषाय, then इति.",
             "The last item is the plain word कषाय, the same word that heads the whole topic.",
             "The list ends कषाय इति."),
        mcq("discriminate", 3, "Which two names does the data gloss as the 'cold infusion' and the 'hot infusion'?",
            ("शीतः and फाण्टः", "शीत is the cold infusion and फाण्ट is the hot infusion."),
            [("कल्कः and शृतः", "कल्क is the paste and शृत the boiled preparation."),
             ("स्वरसः and कल्कः", "स्वरस is the expressed juice and कल्क the paste."),
             ("शृतः and कषायः", "शृत is the boiled preparation; कषाय is not glossed as an infusion.")],
            "The glosses follow the standard meanings: शीत cold, फाण्ट hot.",
            "शीत = cold infusion; फाण्ट = hot infusion."),
        multi("apply", 4, "Which of these statements about unit 7 are right?",
              [("The heading says पञ्चविधम्, fivefold",
                "Right: that is the heading."),
               ("Six names are printed after तद्यथा",
                "Right: from स्वरसः to कषायः."),
               ("The unit does not say which of the six is the extra one",
                "Right: the data says the mismatch is left unresolved."),
               ("The unit states that कषाय is a later insertion",
                "No such statement is made."),
               ("The unit gives how long each preparation is boiled",
                "No method and no time is given.")],
              [0, 1, 2],
              "The first three are what the unit shows; the last two are not in it.",
              "Report a count mismatch as it stands; do not resolve it."),
        mcq("transfer", 5,
            "A made-up line says चतुर्विधं भोजनम्, then prints five names. How should a careful reader treat it, as unit 7 is treated?",
            ("Note that the heading says four and five names are printed, without choosing which is extra",
             "The data treats unit 7 the same way: it records the mismatch and does not resolve it."),
            [("Drop the last name so the count fits", "Nothing in the text allows dropping a printed name."),
             ("Change the heading to five without comment", "That would silently alter the text."),
             ("Treat all five names as one name", "Five printed names are five names.")],
            "Unit 7 prints six names under a heading of five and the mismatch is left standing.",
            "Record a count mismatch plainly; do not guess a fix.",
            teaches="When a heading's count and its list disagree, say so on the card and leave the text as printed."),
    ],
}

NOTES_HI["7"] = ("संधियाँ जाँची: कषायकल्पनम् + इति → कषायकल्पनमिति (म् + इ सटा); तत् + यथा → तद्यथा (त् → द् घोष य से पहले); "
                 "फाण्टः, कषायः आदि के बाद अल्पविराम है और अन्तिम ‘कषाय’ के बाद ‘इति’ आता है। "
                 "डेटा की टिप्पणी: शीर्षक ‘पञ्चविधम्’ के नीचे छह नाम छपे हैं (स्वरस, कल्क, शृत, शीत, फाण्ट, कषाय); यह गिनती का विरोध पाठ में ही है, "
                 "इसे सुलझाया नहीं गया — अन्तिम ‘कषाय’ सामान्य शब्द भी हो सकता है और अलग प्रकार भी। पहले पाँच के अर्थ सामान्य अर्थों के अनुसार दिए गए हैं। "
                 "कोई पाठभेद या पाठ-दोष नहीं दिया गया।")

AIDS["7"] = {
    "frame": "क्या: कषाय-कल्पना के नाम (इकाई ३ की ‘पाँच प्रकार’ गिनती) · शीर्षक: पाँच · छपे नाम: छह · गिनती का विरोध खुला छोड़ा गया।",
    "diagram": {"groups": [
        {"label": "शीर्षक",
         "items": ["पञ्चविधं", "कषायकल्पनमिति", "तद्यथा"]},
        {"label": "छपे नाम",
         "items": ["स्वरसः", "कल्कः", "शृतः", "शीतः", "फाण्टः", "कषाय", "इति"]}]},
    "contrast": "पञ्चविधम् (शीर्षक: पाँच) ↔ छह छपे नाम: गिनती मेल नहीं खाती और पाठ उसे सुलझाता नहीं।",
    "anchors": "स्वरस = निचोड़ा रस · कल्क = लुगदी · शृत = उबाला हुआ · शीत = ठण्डा जलीय निष्कर्ष · फाण्ट = गर्म जलीय निष्कर्ष (सामान्य अर्थ; डेटा के अनुसार)।",
    "sandhi": "म् + स्वर: कषायकल्पनम् + इति → कषायकल्पनमिति। त् + य → द्य: तत् + यथा → तद्यथा।",
    "chunks": "पञ्चविधं कषायकल्पनमिति तद्यथा | स्वरसः कल्कः शृतः | शीतः फाण्टः कषाय इति।",
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "पञ्चाशन्महाकषायाः",
    "question": "What does unit 8 list, and how many classes does each group of the fifty hold?",
    "rule": ("Unit 8 names the fifty great kaṣāya classes in ten groups, each closed by a count and "
             "कषायवर्गः: six, four, six, four, seven, three, five, five, five, five (= 50). It lists no "
             "drug."),
    "limits": ("Class names only (labels given by the text, glossed literally by the data): no drug, "
               "no dose, no claim of what a class does. The printed 'र्शोघ्रः for अर्शोघ्नः is flagged "
               "as a typo in the data, and no question uses it."),
    "explain_hi": ("यह इकाई ‘पचास महाकषाय’ का ढाँचा देती है: दस समूह, हर समूह अन्त में ‘इति … कषायवर्गः’ से बन्द। "
                   "समूहों में वर्ग-नामों की संख्या क्रम से छह, चार, छह, चार, सात, तीन, पाँच, पाँच, पाँच, पाँच है, जिनका योग पचास बैठता है। "
                   "पहला समूह जीवनीय से दीपनीय तक, दूसरा बल्य से हृद्य तक, और पाँचवाँ (सात वर्गों का) स्नेहोपग से शिरोविरेचनोपग तक चलता है। "
                   "इन नामों को डेटा शाब्दिक अर्थ में लेता है (जैसे ‘जीवनीय’ = जीवन देने वाला); इस इकाई में कोई औषधि-नाम नहीं है, औषधियाँ अगली इकाइयों में आएँगी। "
                   "अन्त में कहा गया है कि ये पचास बड़े कषायों के लक्षण और उदाहरण के लिए गिनाए गए हैं।"),
    "hook": "६ · ४ · ६ · ४ · ७ · ३ · ५ · ५ · ५ · ५ = ५० वर्ग; हर समूह ‘इति … कषायवर्गः’ से बन्द।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does the long sentence of unit 8 list?",
            ("Names of classes of kaṣāya, in ten groups, with no drug names",
             "Every item is a class name, and each group closes with a count and कषायवर्गः."),
            [("Ten drug names for each class", "The drug names begin in unit 9."),
             ("The five preparations of kaṣāya", "The preparations are in unit 7."),
             ("The dose of each of fifty formulas", "No dose appears in the unit.")],
            "The unit names the classes only; the ten drugs of each class are given later.",
            "Unit 8: the fifty class names in ten groups."),
        match(1, "Match each group of class names to the number of classes it holds.",
              [["जीवनीय … दीपनीय", "six classes"], ["बल्य … हृद्य", "four classes"],
               ["स्नेहोपग … शिरोविरेचनोपग", "seven classes"],
               ["छर्दिनिग्रहण … हिक्कानिग्रहण", "three classes"]],
              "Each group closes with a count word: षट्कः six, चतुष्कः four, सप्तकः seven, त्रिकः three.",
              "जीवनीय group 6; बल्य group 4; स्नेहोपग group 7; छर्दिनिग्रहण group 3."),
        fill(2, "Each group closes with a count word and कषाय____ (type the word for 'class' in Devanagari).",
             ["वर्गः", "वर्ग"],
             "Each group ends इति … कषायवर्गः, 'a class of kaṣāya'.",
             "कषायवर्गः is a compound: कषाय + वर्गः, 'class of kaṣāya'.",
             "कषाय + वर्गः = a class (group) of kaṣāya."),
        mcq("discriminate", 3, "Which is the right split of स्नेहोपगः?",
            ("स्नेह + उपगः", "अ + उ gives ओ, so स्नेह + उपगः is written स्नेहोपगः."),
            [("स्ने + होपगः", "होपगः is not a word."),
             ("स्नेहो + पगः", "पगः is not a word."),
             ("स्नेहः + उपगः", "A visarga after अ drops before उ, giving स्नेह उपगः, not स्नेहोपगः.")],
            "स्नेहोपगः is स्नेह ('oleation') + उपगः ('going along with'), with अ + उ → ओ.",
            "स्नेह + उपग → स्नेहोपग (अ + उ → ओ)."),
        mcq("apply", 4, "Which group is the largest in unit 8?",
            ("The group beginning with स्नेहोपग, which holds seven classes",
             "Its closing label is सप्तकः, a group of seven."),
            [("The group beginning with जीवनीय", "It is a group of six."),
             ("The group beginning with बल्य", "It is a group of four."),
             ("The group beginning with छर्दिनिग्रहण", "It is a group of three.")],
            "The sizes are 6, 4, 6, 4, 7, 3, 5, 5, 5, 5; the largest is 7.",
            "The स्नेहोपग group is the largest (सप्तकः)."),
        mcq("transfer", 5,
            "A made-up text says there are twelve classes, in groups closed by त्रिकः, चतुष्कः and पञ्चकः. Does it add up?",
            ("Yes: 3 + 4 + 5 = 12", "त्रिकः is three, चतुष्कः four and पञ्चकः five, which total twelve."),
            [("No: it comes to ten", "3 + 4 + 5 is twelve, not ten."),
             ("No: it comes to sixty", "That multiplies the sizes; the group sizes are added."),
             ("It cannot be checked", "The count words give the group sizes, so it can be checked.")],
            "As in unit 8, where 6 + 4 + 6 + 4 + 7 + 3 + 5 + 5 + 5 + 5 = 50, add the group sizes and compare with the stated total.",
            "Add the group sizes and compare with the stated total.",
            teaches="You can check a list of groups against its stated total by adding the sizes given by the count words."),
    ],
}

NOTES_HI["8"] = ("संधियाँ जाँची: जीवनीयः + बृंहणीयः → जीवनीयो बृंहणीयः (अः + घोष → ओ); तृप्तिघ्नः + अर्शोघ्नः → तृप्तिघ्नो ऽर्शोघ्नः (अः + अ → ओ, अ का लोप ऽ); "
                 "स्नेह + उपगः → स्नेहोपगः (अ + उ → ओ); पञ्चाशत् + महाकषायाः → पञ्चाशन्महाकषायाः (त् → न् म से पहले); "
                 "कषायाः + इति → कषाया इति (आः के बाद स्वर से पहले विसर्ग लुप्त; छपा रूप ‘कषायाऽ’)। "
                 "पाठ-दोष (text_flags): ‘ऽर्शोघ्रः’ छपा है, वह ‘ऽर्शोघ्नः’ (अर्शस् + घ्न, ‘अर्श को दूर करने वाला’) होना चाहिए; ‘घ्र’ सम्भवतः ‘घ्न’ की भूल है "
                 "(देवनागरी प्रति में भी यही रूप है, इसलिए संस्करण में हो सकता है); इसे भूल मानकर चिह्नित किया है, किसी प्रश्न में नहीं रखा। "
                 "डेटा की टिप्पणी: समूहों के आकार छपे अनुसार ६+४+६+४+७+३+५+५+५+५ = ५० हैं, जो ‘पञ्चाशत्’ से मेल खाता है; हृद्य का अर्थ ‘मनोहर’ भी हो सकता है, कण्ठ्य का ‘कण्ठ/स्वर के लिए हितकर’, विरजनीय और स्थापन का सटीक अर्थ शब्दों से तय नहीं होता। "
                 "आरम्भ में उद्धरण चिह्न बैकटिक और अन्त में अपोस्ट्रॉफ़ी है (संस्करण के उद्धरण चिह्न)।")

AIDS["8"] = {
    "frame": "क्या: पचास महाकषाय के वर्गों के नाम, दस समूहों में · हर समूह अन्त में ‘इति … कषायवर्गः’ · औषधि-नाम नहीं।",
    "contrast": "समूहों के आकार क्रम से: छह (जीवनीय) · चार (बल्य) · छह (तृप्तिघ्न) · चार (स्तन्यजनन) · सात (स्नेहोपग, सबसे बड़ा) · तीन (छर्दिनिग्रहण, सबसे छोटा) · पाँच · पाँच · पाँच · पाँच = पचास।",
    "sandhi": "अः + घोष → ओ: जीवनीयः + बृंहणीयः → जीवनीयो बृंहणीयः। अ + उ → ओ: स्नेह + उपगः → स्नेहोपगः। त् + म → न्म: पञ्चाशत् + महाकषायाः → पञ्चाशन्महाकषायाः।",
    "anchors": "त्रिकः = तीन का समूह · चतुष्कः = चार का · पञ्चकः = पाँच का · षट्कः = छह का · सप्तकः = सात का · वर्ग = श्रेणी · जीवनीय = जीवन देने वाला · बृंहणीय = पुष्टि बढ़ाने वाला (शाब्दिक, डेटा के अनुसार)।",
    "chunks": "जीवनीयो … दीपनीय इति षट्कः | बल्यो … हृद्य इति चतुष्कः | तृप्तिघ्नो … विषघ्न इति षट्कः | स्तन्यजननः … शुक्रशोधन इति चतुष्कः | स्नेहोपगः … शिरोविरेचनोपग इति सप्तकः | छर्दिनिग्रहणः … हिक्कानिग्रहण इति त्रिकः | पुरीषसंग्रहणीयः … मूत्रविरेचनीय इति पञ्चकः | कासहरः … श्रमहर इति पञ्चकः | दाहप्रशमनः … शूलप्रशमन इति पञ्चकः | शोणितस्थापनः … वयःस्थापन इति पञ्चकः।",
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "जीवनीयादि षट्क वर्ग",
    "question": "What is the frame of each list in unit 9, and which six classes does it hold?",
    "rule": ("Classes 1 to 6 of the fifty: each is a list of drug names closed by 'दशेमानि X भवन्ति' "
             "(these ten are the X). The six X are जीवनीय, बृंहणीय, लेखनीय, भेदनीय, सन्धानीय, दीपनीय; the "
             "unit closes इति षट्कः कषायवर्गः."),
    "limits": ("Names only: no plant identified, no use, no dose. The names are printed run together; "
               "their boundaries, made by a draft and a reviewer, are doubtful in places (भल्लातकास्थि "
               "and हिङ्गुनिर्यासाः each taken as one; वाठ्यायनी flagged). Part of a list across units 9-18."),
    "explain_hi": ("यह इकाई ‘पचास महाकषाय’ की सूची का आरम्भ है: वर्ग १ से ६ (कुल पचास में)। हर वर्ग में दस नाम गिनाकर ‘इति दशेमानि … भवन्ति’ कहा गया है, "
                   "यानी ‘ये दस … हैं’। छह वर्गों के नाम क्रम से जीवनीय, बृंहणीय, लेखनीय, भेदनीय, सन्धानीय और दीपनीय हैं (इकाई ८ में इनके नाम पहले आ चुके हैं), "
                   "और अन्त में ‘इति षट्कः कषायवर्गः’ आता है। कुछ नाम एक से अधिक वर्ग की सूचियों में छपे हैं, जैसे काकोली और क्षीरकाकोली जीवनीय और बृंहणीय दोनों में, "
                   "चित्रक और चिरबिल्व लेखनीय और भेदनीय दोनों में। यहाँ केवल नाम हैं: किसी पौधे की पहचान, उपयोग या मात्रा नहीं।"),
    "hook": "वर्ग १–६: दस-दस नाम, ‘दशेमानि X भवन्ति’; अन्त: षट्कः कषायवर्गः।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Each list in unit 9 ends with इति दशेमानि … भवन्ति. How many drugs does each list claim to hold?",
            ("Ten", "दश is ten, and दशेमानि is दश + इमानि, 'these ten'."),
            [("Six", "Six is the number of classes in the unit, not the size of a list."),
             ("Five", "Five is not stated for any list here."),
             ("Fifty", "Fifty is the total number of classes, not the size of one list.")],
            "Every list is closed by 'these ten are the X'.",
            "Unit 9: each of the six lists claims ten drugs."),
        order(1, "Put the six classes of unit 9 in the order the unit gives them.",
              ["जीवनीयानि", "बृंहणीयानि", "लेखनीयानि", "भेदनीयानि", "सन्धानीयानि", "दीपनीयानि"],
              "The classes run जीवनीय, बृंहणीय, लेखनीय, भेदनीय, सन्धानीय, दीपनीय.",
              "The order of classes 1 to 6: जीवनीय, बृंहणीय, लेखनीय, भेदनीय, सन्धानीय, दीपनीय."),
        fill(2, "The unit ends इति ____ कषायवर्गः. Type the count word for 'group of six' in Devanagari.",
             ["षट्कः", "षट्क"],
             "The closing words are इति षट्कः कषायवर्गः, 'a group of six classes'.",
             "The count word षट्कः closes the group, as in unit 8; here the six lists have just been given.",
             "इति + count word + कषायवर्गः closes a group of classes."),
        mcq("discriminate", 3, "Which pair of names is printed in both the जीवनीय list and the बृंहणीय list?",
            ("काकोली and क्षीरकाकोली", "Both names appear in the first list and again in the second."),
            [("मेदा and महामेदा", "They are printed in the जीवनीय list only."),
             ("क्षीरिणी and पयस्या", "They are printed in the बृंहणीय list only."),
             ("जीवन्ती and मधुक", "They are printed in the जीवनीय list only.")],
            "The same printed name can stand in more than one class; काकोली and क्षीरकाकोली stand in both of the first two.",
            "A name printed in two lists belongs to both classes as printed."),
        mcq("apply", 4, "A list starts पिप्पली, पिप्पलीमूल, चव्य and ends with दशेमानि … भवन्ति. Which class label sits at the end?",
            ("दीपनीयानि", "The sixth list, which begins with पिप्पली, is closed by दशेमानि दीपनीयानि भवन्ति."),
            [("जीवनीयानि", "That is the first list, which begins with जीवक."),
             ("लेखनीयानि", "That is the third list, which begins with मुस्त."),
             ("सन्धानीयानि", "That is the fifth list, which begins with मधुक.")],
            "Each list ends with its class label between दशेमानि and भवन्ति.",
            "The class label stands between दशेमानि and भवन्ति."),
        mcq("transfer", 5,
            "A made-up line is अ आ इ ई उ ऊ ए ऐ ओ औ इति दशेमानि स्वराणि भवन्ति. Which word is the class label?",
            ("स्वराणि", "It stands between दशेमानि and भवन्ति, as जीवनीयानि does in unit 9."),
            [("दशेमानि", "That is the count, 'these ten'."),
             ("भवन्ति", "That is the verb, 'are'."),
             ("इति", "That closes the list of items.")],
            "The shape is the same as in unit 9: items, इति, दशेमानि, label, भवन्ति.",
            "Items + इति + दशेमानि + label + भवन्ति.",
            teaches="You can name the class of any list in this frame by reading the word between दशेमानि and भवन्ति."),
    ],
}

NOTES_HI["9"] = ("संधियाँ जाँची: दश + इमानि → दशेमानि (अ + इ → ए); जीवक + ऋषभकौ → जीवकर्षभकौ (अ + ऋ → अर्); मधुकम् + इति → मधुकमिति (म् सटा); "
                 "अर्क + उरुबुक → अर्कोरुबुक (अ + उ → ओ); पयस्या + ऋष्यगन्धा → पयस्यर्ष्यगन्धा (आ + ऋ → अर्)। "
                 "पाठ-दोष/वैकल्पिक पाठ (text_flags): ‘वाठ्यायनी’ सम्भवतः ‘वाट्यायनी’ है (दोनों देवनागरी प्रति में ठ है); दस की गिनती दोनों में बैठती है। "
                 "सीमाओं के सन्देह (डेटा की टिप्पणी): ‘भल्लातकास्थि’ और ‘हिङ्गुनिर्यासाः’ को एक-एक नाम माना गया है; दूसरी तरह तोड़ने पर बारह होते; "
                 "‘अर्कोरुबुकाग्निमुखी’ में उरुबुक की दीर्घता सन्धि में छिप सकती है। पाठ-स्थिति: संस्करण में यह अंश कोष्ठक में छपा है (प्रक्षिप्त या वैकल्पिक हो सकता है); स्रोत में एक भटका ‘&’ था जिसे हटाया गया; "
                 "सूचियों के बाद १–६ की गिनती के संख्या-चिह्न हटाए गए (वे पचास समूहों को गिनते हैं)।")

AIDS["9"] = {
    "frame": "क्या: वर्ग १–६ (पचास में से) · हर वर्ग: दस नाम + ‘दशेमानि X भवन्ति’ · अन्त: षट्कः कषायवर्गः · केवल नाम।",
    "chain": {"steps": ["जीवनीयानि", "बृंहणीयानि", "लेखनीयानि", "भेदनीयानि", "सन्धानीयानि", "दीपनीयानि"]},
    "sandhi": "अ + इ → ए: दश + इमानि → दशेमानि। अ + ऋ → अर्: जीवक + ऋषभकौ → जीवकर्षभकौ। अ + उ → ओ: अर्क + उरुबुक → अर्कोरुबुक।",
    "anchors": "दशेमानि = दश (दस) + इमानि (ये): ‘ये दस’ · काकोली और क्षीरकाकोली दोनों जीवनीय और बृंहणीय सूचियों में छपे हैं · चित्रक और चिरबिल्व लेखनीय और भेदनीय दोनों में।",
    "chunks": "… इति दशेमानि जीवनीयानि भवन्ति | … दशेमानि बृंहणीयानि भवन्ति | … दशेमानि लेखनीयानि भवन्ति | … दशेमानि भेदनीयानि भवन्ति | … दशेमानि सन्धानीयानि भवन्ति | … दशेमानि दीपनीयानि भवन्ति ‖ इति षट्कः कषायवर्गः।",
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "बल्यादि चतुष्क वर्ग",
    "question": "Which four classes does unit 10 hold, and how does it close?",
    "rule": ("Classes 7 to 10 of the fifty: बल्य, वर्ण्य, कण्ठ्य, हृद्य, each a list of ten names closed "
             "by 'दशेमानि X भवन्ति'. The unit closes इति चतुष्कः कषायवर्गः, a group of four."),
    "limits": ("Names only: no plant identified, no use, no dose. The class labels are glossed "
               "literally by the data; hṛdya can also mean 'pleasing'. पयस्यासितालता can be read "
               "with सिता or असिता; no question rests on it. The unit continues unit 9."),
    "explain_hi": ("यह इकाई इकाई ९ की सूची को आगे बढ़ाती है: वर्ग ७ से १० (कुल पचास में)। चार वर्ग हैं: बल्य, वर्ण्य, कण्ठ्य और हृद्य, "
                   "जिन्हें डेटा शाब्दिक रूप में ‘बल देने वाले’, ‘वर्ण सुधारने वाले’, ‘कण्ठ के लिए हितकर’ और ‘हृदय के लिए हितकर’ लेता है। "
                   "हर वर्ग में दस नाम हैं और अन्त में ‘दशेमानि X भवन्ति’ आता है; पूरी इकाई ‘इति चतुष्कः कषायवर्गः’ (चार का समूह) पर समाप्त होती है, जैसा इकाई ८ में बताया गया था। "
                   "कुछ नाम कई सूचियों में छपे हैं, जैसे मधुक वर्ण्य और कण्ठ्य दोनों में। यहाँ केवल नाम हैं: कोई पहचान, उपयोग या मात्रा नहीं।"),
    "hook": "वर्ग ७–१०: बल्य · वर्ण्य · कण्ठ्य · हृद्य; अन्त: चतुष्कः कषायवर्गः।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does unit 10 continue, and with which closing label does it end?",
            ("The list begun in unit 9; it ends इति चतुष्कः कषायवर्गः",
             "The unit gives classes 7 to 10 and closes a group of four."),
            [("The list of unit 7; it ends इति षट्कः कषायवर्गः", "Unit 7 lists the preparations; the closing label षट्कः belongs to unit 9."),
             ("The summary of unit 3; it ends इति संग्रहः", "The summary is unit 3 and ends differently."),
             ("The speaker line of unit 2; it ends आह", "Unit 2 only names Ātreya as speaker.")],
            "Unit 10 continues the class lists of unit 9 and closes with the group-of-four label.",
            "Unit 10: classes 7 to 10, closing label चतुष्कः."),
        match(1, "Match each class label to the data's literal gloss.",
              [["बल्यानि", "strength-giving"], ["वर्ण्यानि", "complexion-improving"],
               ["कण्ठ्यानि", "good for the throat"], ["हृद्यानि", "good for the heart"]],
              "The data renders the four class labels literally.",
              "बल्य strength-giving; वर्ण्य complexion-improving; कण्ठ्य good for the throat; हृद्य good for the heart."),
        fill(2, "The unit ends इति ____ कषायवर्गः. Type the count word for 'group of four' in Devanagari.",
             ["चतुष्कः", "चतुष्क"],
             "The closing words are इति चतुष्कः कषायवर्गः.",
             "The count word चतुष्कः (four) closes the group, as षट्कः (six) did in unit 9.",
             "इति + count word + कषायवर्गः closes a group of classes."),
        mcq("discriminate", 3, "Which name is printed in both the वर्ण्य list and the कण्ठ्य list of unit 10?",
            ("मधुक", "It stands among the वर्ण्य names and again among the कण्ठ्य names."),
            [("चन्दन", "It is printed in the वर्ण्य list only."),
             ("द्राक्षा", "It is printed in the कण्ठ्य list only."),
             ("दाडिम", "It is printed in the हृद्य list only.")],
            "The same printed name can stand in more than one class.",
            "A name printed in two lists belongs to both classes as printed."),
        mcq("apply", 4, "A list begins चन्दन, तुङ्ग, पद्मक, उशीर and ends with दशेमानि … भवन्ति. Which class label sits at the end?",
            ("वर्ण्यानि", "The second list of the unit, beginning with चन्दन, ends दशेमानि वर्ण्यानि भवन्ति."),
            [("बल्यानि", "That list begins with ऐन्द्री."),
             ("कण्ठ्यानि", "That list begins with सारिवा."),
             ("हृद्यानि", "That list begins with आम्र.")],
            "The label stands between दशेमानि and भवन्ति at the end of each list.",
            "The class label stands between दशेमानि and भवन्ति."),
        mcq("transfer", 5,
            "A made-up text closes three lists with इति त्रिकः वर्गः. By the pattern of चतुष्कः, what does that say?",
            ("The three lists form one group of three", "त्रिकः means a group of three, as चतुष्कः means a group of four."),
            [("Each list holds three names", "The count word counts the lists in the group, not the names in one list."),
             ("The lists hold thirty names in all", "The word gives no total of names."),
             ("The text has three groups", "One closing label closes one group.")],
            "As चतुष्कः closes four lists in unit 10, त्रिकः would close three.",
            "Count word + वर्गः: the group has that many lists.",
            teaches="A closing label like त्रिकः or चतुष्कः counts how many lists the group holds."),
    ],
}

NOTES_HI["10"] = ("संधियाँ जाँची: ऐन्द्री + ऋषभी → ऐन्द्र्यृषभी (ई + स्वर → य्); ऋषभी + अतिरसा → ऋषभ्यतिरसा; अतिरसा + ऋष्यप्रोक्ता → अतिरसर्ष्यप्रोक्ता (आ + ऋ → अर्); "
                  "बला + अतिबला → बलातिबला (आ + अ → आ); सारिवा + इक्षुमूल → सारिवेक्षुमूल (आ + इ → ए); आम्र + आम्रातक → आम्राम्रातक (अ + आ → आ); "
                  "वृक्षाम्ल + अम्लवेतस → वृक्षाम्लाम्लवेतस (अ + अ → आ); मातुलुङ्गानि + इति → मातुलुङ्गानीति (इ + इ → ई)। "
                  "सीमा का सन्देह (डेटा की टिप्पणी): ‘पयस्यासितालता’ को पयस्या + सिता + लता या पयस्या + असिता + लता, दोनों तरह पढ़ा जा सकता है (दोनों से दस बनते हैं); "
                  "‘एक नाम असितालता’ मानने पर नौ रहते। हृद्य का अर्थ ‘मनोहर’ भी हो सकता है। पाठ-स्थिति: संस्करण में यह अंश कोष्ठक में छपा है (प्रक्षिप्त या वैकल्पिक हो सकता है) और "
                  "७–१० की गिनती के संख्या-चिह्न हटाए गए। कोई पाठ-दोष (text_flags) नहीं दिया गया।")

AIDS["10"] = {
    "frame": "क्या: वर्ग ७–१० (पचास में से, इकाई ९ की सूची जारी) · हर वर्ग दस नाम + ‘दशेमानि X भवन्ति’ · अन्त: चतुष्कः कषायवर्गः · केवल नाम।",
    "chain": {"steps": ["बल्यानि", "वर्ण्यानि", "कण्ठ्यानि", "हृद्यानि"]},
    "sandhi": "ई + स्वर → य्: ऐन्द्री + ऋषभी → ऐन्द्र्यृषभी। आ + ऋ → अर्: अतिरसा + ऋष्यप्रोक्ता → अतिरसर्ष्यप्रोक्ता। आ + इ → ए: सारिवा + इक्षुमूल → सारिवेक्षुमूल। अ + आ → आ: आम्र + आम्रातक → आम्राम्रातक।",
    "anchors": "बल्य = बल देने वाला · वर्ण्य = वर्ण सुधारने वाला · कण्ठ्य = कण्ठ के लिए हितकर · हृद्य = हृदय के लिए हितकर (डेटा के शाब्दिक रूप) · मधुक वर्ण्य और कण्ठ्य दोनों सूचियों में छपा है · चतुष्कः = चार का समूह।",
    "chunks": "… इति दशेमानि बल्यानि भवन्ति | … दशेमानि वर्ण्यानि भवन्ति | … दशेमानि कण्ठ्यानि भवन्ति | … दशेमानि हृद्यानि भवन्ति ‖ इति चतुष्कः कषायवर्गः।",
}

IMAGE_SPECS = {
    ("3", "pegs"): {
        "file": "ch4-count-3.svg",
        "alt": "A table of the six counts in the summary of unit 3: six hundred purgatives, six supports of purgation, five sources of kaṣāya, fivefold preparation, fifty great kaṣāyas, five hundred kaṣāyas",
        "type": "table",
        "title": "इकाई ३: संग्रह की गिनती",
        "heads": ["विषय", "संख्या"],
        "rows": [["विरेचनशतानि", "छह सौ"], ["विरेचनाश्रयाः", "छह"], ["कषाययोनयः", "पाँच"],
                 ["कषायकल्पनम्", "पाँच प्रकार"], ["महाकषायाः", "पचास"], ["कषायशतानि", "पाँच सौ"]],
    },
    ("8", "contrast"): {
        "file": "ch4-groups-8.svg",
        "alt": "A table of the ten groups of class names in unit 8 with their sizes: six, four, six, four, seven, three, five, five, five, five, adding up to fifty",
        "type": "table",
        "title": "इकाई ८: दस समूहों के आकार",
        "heads": ["समूह (पहला वर्ग)", "वर्ग"],
        "rows": [["१ जीवनीय", "छह"], ["२ बल्य", "चार"], ["३ तृप्तिघ्न", "छह"], ["४ स्तन्यजनन", "चार"],
                 ["५ स्नेहोपग", "सात"], ["६ छर्दिनिग्रहण", "तीन"], ["७ पुरीषसंग्रहणीय", "पाँच"],
                 ["८ कासहर", "पाँच"], ["९ दाहप्रशमन", "पाँच"], ["१० शोणितस्थापन", "पाँच = कुल पचास"]],
    },
    ("9", "chain"): {
        "file": "ch4-classes-9.svg",
        "alt": "A chain of six boxes in the order of unit 9: jivaniya, brimhaniya, lekhaniya, bhedaniya, sandhaniya, dipaniya",
        "type": "chain",
        "title": "इकाई ९: वर्ग १ से ६ का क्रम",
        "steps": ["जीवनीयानि", "बृंहणीयानि", "लेखनीयानि", "भेदनीयानि", "सन्धानीयानि", "दीपनीयानि"],
    },
}
