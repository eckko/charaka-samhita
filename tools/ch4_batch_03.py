from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}
NOTES_HI = {}
AIDS = {}
IMAGE_SPECS = {}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "तृप्तिघ्न से विषघ्न तक: छह वर्ग",
    "question": "How many drug names does each class of unit 11 list, and what are the six class labels?",
    "rule": ("Unit 11 gives six classes (11-16 of the 50), each of ten drug names closed by a label "
             "ending -ghna (removing): tṛpti, arśas, kuṣṭha, kaṇḍū, krimi, viṣa. "
             "The frame is daśemāni X bhavanti; the unit ends iti ṣaṭkaḥ kaṣāyavargaḥ."),
    "limits": ("The unit names ten drugs per class and a label; it gives no dose and no effect beyond "
               "the literal label. Some name boundaries are uncertain (gāgara, nalada, suvahā, "
               "sūkṣma-elā), and some names recur across classes. The edition prints this text in parentheses."),
    "explain_hi": ("यह गद्य-इकाई पचास महाकषायों में से छह वर्ग (११ से १६) देती है। हर वर्ग का ढाँचा एक-सा है: दस नाम गिनाकर "
                   "‘इति दशेमानि X भवन्ति’, यानी ‘ये दस X हैं’। छह नाम ये हैं: तृप्तिघ्न, अर्शोघ्न, कुष्ठघ्न, कण्डूघ्न, "
                   "क्रिमिघ्न और विषघ्न। ‘-घ्न’ का शाब्दिक अर्थ ‘हटाने वाला’ है (तृप्ति-हटाने वाला, अर्श-हटाने वाला आदि); "
                   "इससे आगे का कोई असर यह पाठ नहीं कहता। अन्त में ‘इति षट्कः कषायवर्गः’ (छह का कषाय-वर्ग) सूची बन्द करता है। "
                   "कुछ नाम एक से अधिक वर्गों में आते हैं, जैसे विडङ्ग; मूल पाठ में वैसा ही है।"),
    "hook": "दस-दस नाम × छह वर्ग: तृप्ति, अर्श, कुष्ठ, कण्डू, क्रिमि, विष: सब ‘-घ्न’ (हटाने वाले)।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In unit 11, how many drug names does each class list, going by the frame दशेमानि?",
            ("Ten",
             "दश = ten; इमानि = these. Each class is introduced as 'these ten'."),
            [("Six", "Six is the number of classes in the unit (षट्कः), not the number of names in one class."),
             ("Five", "Nothing in unit 11 gives five for the names of a class."),
             ("Twelve", "The frame says दश, ten, for every class.")],
            "दशेमानि = दश + इमानि, 'these ten'. The same frame opens the closing of every class in the unit.",
            "Frame: दशेमानि X भवन्ति = these ten are X."),
        match(1, "Match each class label of unit 11 to its literal meaning.",
              [["तृप्तिघ्नानि", "satiety-removing"],
               ["कुष्ठघ्नानि", "kuṣṭha-removing"],
               ["क्रिमिघ्नानि", "worm-removing"],
               ["विषघ्नानि", "poison-removing"]],
              "Each label is a noun plus -घ्नानि, 'removing'; the noun says what is removed.",
              "तृप्ति = satiety; कुष्ठ = kuṣṭha; क्रिमि = worm; विष = poison; -घ्न = removing."),
        fill(2, "The unit closes with इति ____ कषायवर्गः, meaning a set of six. Type the missing word in Devanagari.",
             ["षट्कः", "षट्क"],
             "The closing formula reads इति षट्कः कषायवर्गः.",
             "षट्कः is षष् (six) plus the suffix -क: 'a set of six'. It counts the classes of this unit, not the drugs.",
             "षट्कः = a set of six; it counts the classes.",
             ),
        mcq("discriminate", 3, "Which is the right split of दशेमानि?",
            ("दश + इमानि",
             "अ + इ joins to ए: दश + इमानि gives दशेमानि."),
            [("दशे + मानि", "मानि is not a word here."),
             ("दश + एमानि", "एमानि is not a word; the pronoun is इमानि."),
             ("दशः + इमानि", "With a visarga the words would stay apart: दश इमानि.")],
            "दशेमानि = दश ('ten') + इमानि ('these').",
            "अ + इ → ए: दश + इमानि → दशेमानि."),
        multi("apply", 4, "Which of these does unit 11 say?",
              [("It gives six classes, each introduced as ten names", "Right: six labels, each with दशेमानि."),
               ("Every class label ends in -घ्नानि, removing", "Right: तृप्तिघ्नानि to विषघ्नानि all end so."),
               ("The last class of the unit is विषघ्नानि", "Right: the sixth label is विषघ्नानि."),
               ("It gives a dose for each drug", "No dose is named anywhere in the unit."),
               ("It says the first class cures fever", "The first label is tṛpti-ghna; fever is not mentioned.")],
              [0, 1, 2],
              "The structure is: ten names, a -ghna label, six times, then the closing formula.",
              "Unit 11: six classes of ten names; labels in -ghna; no dose."),
        mcq("transfer", 5,
            "A made-up closing reads इति दशेमानि ज्वरघ्नानि भवन्ति (ज्वर = fever). Following the frame of unit 11, what does it say?",
            ("These ten are fever-removing",
             "ज्वर + घ्नानि, like विष + घ्नानि 'poison-removing': the label names what is removed."),
            [("These ten are fever-causing", "-घ्न means removing, not causing."),
             ("These ten are fevers", "The label describes the drugs; it does not say the drugs are fevers."),
             ("These ten are fever-measuring", "Nothing in -घ्न means measuring.")],
            "The pattern is दशेमानि X-घ्नानि भवन्ति: 'these ten are X-removing'. Only X changes.",
            "X-घ्नानि = removing X.",
            teaches="Any label of the form X-घ्न in these lists reads as 'removing X'."),
    ],
}

NOTES_HI["11"] = ("संधियाँ जाँची: दश + इमानि → दशेमानि (अ + इ → ए); दशेमानि + अर्शोघ्नानि → दशेमान्यर्शोघ्नानि (इ → य् असमान स्वर से पहले); "
                  "‘इति’ सूची के अन्त को बन्द करता है। इकाई ८ में ‘अर्शोघ्नः’ की जगह ‘ऽर्शोघ्रः’ छपा था और सुधारा गया; यहाँ ‘अर्शोघ्नानि’ ठीक छपा है। "
                  "इस इकाई में पाठभेद या पाठ-दोष का कोई संकेत नहीं। टिप्पणी के अनुसार नाम केवल बाँटे गए हैं, पहचाने नहीं गए; "
                  "सीमा-सम्बन्धी शंका: गागर (पहला नाम, असामान्य शब्द), नलद, सुवहा, सूक्ष्मैला (सूक्ष्मा + एला भी सम्भव)। "
                  "‘तृप्ति’ को ‘तृप्ति/संतोष’ दोनों पढ़ सकते हैं। संस्करण में यह पाठ कोष्ठक में छपा है (प्रक्षिप्त या वैकल्पिक हो सकता है)।")

AIDS["11"] = {
    "frame": "बनावट: दस नाम · इति दशेमानि X भवन्ति (ये दस X हैं) · यह ६ बार · अन्त में इति षट्कः कषायवर्गः। वर्ग ११ से १६।",
    "chain": {"steps": [
        "वर्ग ११: तृप्तिघ्नानि",
        "वर्ग १२: अर्शोघ्नानि",
        "वर्ग १३: कुष्ठघ्नानि",
        "वर्ग १४: कण्डूघ्नानि",
        "वर्ग १५: क्रिमिघ्नानि",
        "वर्ग १६: विषघ्नानि"]},
    "sandhi": "अ + इ → ए: दश + इमानि → दशेमानि। इ → य् (असमान स्वर से पहले): दशेमानि + अर्शोघ्नानि → दशेमान्यर्शोघ्नानि।",
    "anchors": "-घ्न = हटाने वाला (हन्-धातु से) · तृप्तिघ्न = तृप्ति + घ्न · षट्कः = षष् (छह) + क · कषायवर्ग = कषाय का वर्ग (समूह)।",
}

IMAGE_SPECS[("11", "chain")] = {
    "file": "ch4-classes-11.svg",
    "alt": "A chain of six boxes in the order of unit 11: class 11 tṛptighna, 12 arśoghna, 13 kuṣṭhaghna, 14 kaṇḍūghna, 15 krimighna, 16 viṣaghna",
    "type": "chain",
    "title": "इकाई ११: छह वर्ग (११–१६)",
    "steps": ["वर्ग ११: तृप्तिघ्नानि", "वर्ग १२: अर्शोघ्नानि", "वर्ग १३: कुष्ठघ्नानि",
              "वर्ग १४: कण्डूघ्नानि", "वर्ग १५: क्रिमिघ्नानि", "वर्ग १६: विषघ्नानि"],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "स्तन्य और शुक्र के चार वर्ग",
    "question": "Which four class labels does unit 12 give, and what two pairs of words do they combine?",
    "rule": ("Unit 12 gives four classes (17-20 of the 50), each of ten names: stanyajanana, stanyaśodhana, "
             "śukrajanana, śukraśodhana. Each joins milk (stanya) or semen (śukra) with producing (janana) "
             "or purifying (śodhana). The first list is of roots (mūlāni)."),
    "limits": ("The unit gives names and labels only, no dose and no effect beyond the literal label. "
               "Boundaries are kept as the data splits them (kat-tṛṇa, vṛddha-ruhā, kadamba-niryāsa "
               "are each taken as one name). The edition prints the text in parentheses."),
    "explain_hi": ("यह गद्य-इकाई वर्ग १७ से २० देती है; कुल चार वर्ग, हर में दस नाम। चारों नाम दो-दो के जोड़े से बने हैं: "
                   "स्तन्य (दूध) या शुक्र के साथ जनन (पैदा करने वाला) या शोधन (शुद्ध करने वाला)। इस तरह स्तन्यजनन, "
                   "स्तन्यशोधन, शुक्रजनन और शुक्रशोधन। पहली सूची के अन्त में ‘मूलानि’ (जड़ें) आता है, यानी वहाँ दस नामों की "
                   "जड़ें गिनी गई हैं। अन्त में ‘इति चतुष्कः कषायवर्गः’ चार का समूह बताकर बन्द करता है। "
                   "श्लोक कोई खुराक या असर नहीं बताता; केवल नाम और वर्ग-नाम हैं।"),
    "hook": "चार वर्ग: दूध-पैदा, दूध-शुद्ध, शुक्र-पैदा, शुक्र-शुद्ध (जनन / शोधन); पहली सूची जड़ों की।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The unit closes with इति चतुष्कः कषायवर्गः. How many classes does unit 12 contain?",
            ("Four",
             "चतुष्कः = a set of four; it counts the classes, as षट्कः counted six in unit 11."),
            [("Ten", "Ten is the number of names in each class, not of classes."),
             ("Six", "Six was the count in unit 11."),
             ("Two", "Two is the number of substances (milk, semen), not of classes.")],
            "चतुष्कः is the closing count of classes; the four labels are stanyajanana, stanyaśodhana, śukrajanana, śukraśodhana.",
            "चतुष्कः = a set of four classes."),
        match(1, "Match each class label of unit 12 to its literal meaning.",
              [["स्तन्यजननानि", "milk-producing"],
               ["स्तन्यशोधनानि", "milk-purifying"],
               ["शुक्रजननानि", "semen-producing"],
               ["शुक्रशोधनानि", "semen-purifying"]],
              "Each label joins स्तन्य or शुक्र with जनन or शोधन.",
              "स्तन्य = milk; शुक्र = semen; जनन = producing; शोधन = purifying."),
        fill(2, "The first list ends with the plural word for roots, ____ (type it in Devanagari).",
             ["मूलानि", "मूलानीति"],
             "The first class ends ...कत्तृणमूलानीति दशेमानि: the word is मूलानि, joined to इति.",
             "मूलानि is neuter plural, 'roots': the list names the roots of the plants, not the plants whole.",
             "मूलानि = roots (neuter plural); इति closes the list.",
             ),
        mcq("discriminate", 3, "What separates the label स्तन्यजननानि from स्तन्यशोधनानि?",
            ("Only the last part: जनन, producing, against शोधन, purifying; both concern milk",
             "The first part स्तन्य is the same in both."),
            [("The first is about milk and the second about semen", "Both begin with स्तन्य, milk; semen is शुक्र."),
             ("The first has ten names and the second has nine", "Every class is introduced with दशेमानि, ten."),
             ("The first is for emesis and the second for purgation", "Neither label names emesis or purgation.")],
            "The two labels share स्तन्य and differ in जनन against शोधन.",
            "जनन = producing; शोधन = purifying; the first part names the substance."),
        multi("apply", 4, "Which of these does unit 12 say?",
              [("Two classes concern milk (stanya)", "Right: stanyajanana and stanyaśodhana."),
               ("Two classes concern semen (śukra)", "Right: śukrajanana and śukraśodhana."),
               ("The first class is stanyajanana, milk-producing", "Right: it stands first, and its list is of roots."),
               ("The unit gives a dose for each drug", "No dose is named."),
               ("The unit has five classes", "It closes with चतुष्कः, four.")],
              [0, 1, 2],
              "Four labels: two for milk, two for semen, in the order janana, śodhana, janana, śodhana.",
              "Unit 12: four classes, two for milk and two for semen; no dose."),
        mcq("transfer", 5,
            "A made-up closing reads इति दशेमानि रक्तजननानि भवन्ति (रक्त = blood). Following unit 12, what does it say?",
            ("These ten are blood-producing",
             "रक्त + जननानि: the same pattern as स्तन्य + जननानि, milk-producing."),
            [("These ten are blood-purifying", "Purifying is शोधन, not जनन."),
             ("These ten are blood-removing", "Removing is -घ्न, as in unit 11, not जनन."),
             ("These ten are blood", "The label describes the drugs; it does not call them blood.")],
            "Y-जननानि means producing Y; Y-शोधनानि means purifying Y. Only the first part changes.",
            "Y-जनन = producing Y; Y-शोधन = purifying Y.",
            teaches="Two label endings now read at sight: -जनन for producing and -शोधन for purifying."),
    ],
}

NOTES_HI["12"] = ("संधियाँ जाँची: वसुक + उशीराणि → वसुकोशीराणि (अ + उ → ओ); उशीराणि + इति → उशीराणीति (इ + इ → ई); "
                  "इक्षुकाण्ड + इक्षु + इक्षुरक → इक्षुकाण्डेक्ष्विक्षुरक (अ + इ → ए; उ + इ → वि)। ‘सारिवा इति’ और ‘कुलिङ्गा इति’ में ‘इति’ अलग छपा है। "
                  "पाठभेद या पाठ-दोष का संकेत नहीं। टिप्पणी के अनुसार पहली सूची में दस नामों के बाद ‘मूलानि’ है; ‘कत्तृण’ को कत् + तृण भी बाँटा जा सकता है; "
                  "‘गुन्द्रा’ और ‘इत्कट’ को दो नाम मानने से दस होते हैं। ‘वृद्धरुहा’ और ‘कदम्बनिर्यास’ एक-एक नाम माने गए (अन्यथा ग्यारह होते)। "
                  "संस्करण में यह पाठ कोष्ठक में छपा है।")

AIDS["12"] = {
    "frame": "चार वर्ग (१७–२०), हर में दस नाम · स्तन्य + जनन / शोधन · शुक्र + जनन / शोधन · पहली सूची: जड़ें (मूलानि) · अन्त: इति चतुष्कः कषायवर्गः।",
    "contrast": "जनन (पैदा करने वाला) ↔ शोधन (शुद्ध करने वाला), यह भेद दोनों पदार्थों पर लागू: स्तन्य के दो वर्ग और शुक्र के दो वर्ग; चार = २ × २।",
    "sandhi": "अ + उ → ओ: वसुक + उशीराणि → वसुकोशीराणि। इ + इ → ई: उशीराणि + इति → उशीराणीति। अ + इ → ए: इक्षुकाण्ड + इक्षु → इक्षुकाण्डेक्षु।",
    "anchors": "जनन = जन् (पैदा होना) से, ‘पैदा करने वाला’ · शोधन = शुद्ध करने वाला · चतुष्कः = चतुर् (चार) + क · मूलानि = जड़ें (नपुंसक बहुवचन)।",
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "सात वर्ग: स्नेहोपग से शिरोविरेचनोपग तक",
    "question": "Which seven class labels does unit 13 give, and what does the ending -upaga add to each treatment name?",
    "rule": ("Unit 13 gives seven classes (21-27 of the 50) of ten names, each ending -upaga (adjunct to, going "
             "along with) a treatment: oleation, sweating, emesis, purgation, decoction enema, oil enema, "
             "head-purging. It closes iti saptakaḥ kaṣāyavargaḥ."),
    "limits": ("The verse names the treatments and gives no method, dose or effect. The glosses of āsthāpana as "
               "decoction enema and anuvāsana as oil enema are standard, not drawn from this text. Two printed "
               "slips are flagged in the notes; several names recur across classes."),
    "explain_hi": ("यह गद्य-इकाई वर्ग २१ से २७ देती है: सात वर्ग, हर में दस नाम। हर वर्ग-नाम एक उपचार-नाम के साथ ‘-उपग’ जोड़कर बना है; "
                   "‘उपग’ का शाब्दिक भाव है ‘साथ चलने वाला, सहायक’। क्रम से: स्नेहन, स्वेदन, वमन, विरेचन, आस्थापन, अनुवासन और "
                   "शिरोविरेचन के उपग। आस्थापन (काढ़े की बस्ति) और अनुवासन (तेल की बस्ति) के ये अर्थ मानक हैं, इस पाठ से नहीं लिए गए। "
                   "‘स्नेह + उपगानि → स्नेहोपगानि’ में अ + उ मिलकर ओ बनता है। अन्त में ‘इति सप्तकः कषायवर्गः’ सात का समूह बताता है। "
                   "कोई खुराक या विधि यहाँ नहीं दी गई।"),
    "hook": "सात उपग-वर्ग: स्नेह, स्वेद, वमन, विरेचन, आस्थापन, अनुवासन, शिरोविरेचन; सब ‘-उपग’ = सहायक।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The last class of unit 13 is शिरोविरेचनोपगानि. Going by the card, what is it an adjunct to?",
            ("Head-purging",
             "शिरोविरेचन = head-purging; -उपग = adjunct to, going along with."),
            [("The oil enema", "The oil enema is अनुवासन, the sixth class."),
             ("Sweating", "Sweating is स्वेद, the second class."),
             ("Emesis", "Emesis is वमन, the third class.")],
            "The last label joins शिरोविरेचन with -उपगानि. The unit closes with सप्तकः, seven.",
            "शिरोविरेचन-उपग = adjunct to head-purging."),
        order(1, "Put these five class labels in the order they stand in unit 13.",
              ["वमनोपगानि", "विरेचनोपगानि", "आस्थापनोपगानि", "अनुवासनोपगानि", "शिरोविरेचनोपगानि"],
              "The seven classes run from oleation to head-purging; these five are the last five.",
              "वमन → विरेचन → आस्थापन → अनुवासन → शिरोविरेचन."),
        fill(2, "The unit closes with इति ____ कषायवर्गः, meaning a set of seven. Type the missing word in Devanagari.",
             ["सप्तकः", "सप्तक"],
             "The closing formula reads इति सप्तकः कषायवर्गः.",
             "सप्तकः is सप्तन् (seven) plus -क: a set of seven. It counts the classes of this unit.",
             "सप्तकः = a set of seven classes.",
             ),
        mcq("discriminate", 3, "Which is the right split of स्नेहोपगानि?",
            ("स्नेह + उपगानि",
             "अ + उ joins to ओ: स्नेह + उपगानि gives स्नेहोपगानि."),
            [("स्नेहो + पगानि", "पगानि is not a word here."),
             ("स्नेहः + उपगानि", "With a visarga the words would stay apart: स्नेह उपगानि."),
             ("स्नेह + ओपगानि", "ओपगानि is not a word; the second part is उपगानि.")],
            "स्नेहोपगानि = स्नेह ('oleation') + उपगानि ('adjuncts to').",
            "अ + उ → ओ: स्नेह + उपगानि → स्नेहोपगानि."),
        multi("apply", 4, "Which of these does unit 13 say?",
              [("It gives seven classes of ten names", "Right: classes 21-27, closed by सप्तकः."),
               ("Both enemas, āsthāpana and anuvāsana, have a class", "Right: आस्थापनोपगानि and अनुवासनोपगानि."),
               ("The last class is an adjunct to head-purging", "Right: शिरोविरेचनोपगानि."),
               ("It gives a dose for each drug", "No dose is named."),
               ("It has five classes", "The closing word is सप्तकः, seven.")],
              [0, 1, 2],
              "Seven treatments, seven classes, in the order oleation to head-purging.",
              "Unit 13: seven -upaga classes; no dose."),
        mcq("transfer", 5,
            "A made-up label अञ्जनोपगानि (अञ्जन = collyrium) appears. Following unit 13, what does it mean?",
            ("Adjuncts to collyrium",
             "अञ्जन + उपगानि, like स्नेह + उपगानि 'adjuncts to oleation'."),
            [("Removing collyrium", "Removing is -घ्न from unit 11, not -उपग."),
             ("Producing collyrium", "Producing is -जनन from unit 12, not -उपग."),
             ("Ten kinds of collyrium", "The label names a treatment the drugs go along with; it does not count kinds.")],
            "The pattern is X-उपग: adjunct to, going along with X. The ending -उपग says the drugs go along with the treatment X.",
            "X-उपग = adjunct to X.",
            teaches="The ending -उपग now reads as adjunct to the treatment named before it."),
    ],
}

NOTES_HI["13"] = ("संधियाँ जाँची: स्नेह, स्वेद, वमन, विरेचन, आस्थापन, अनुवासन, शिरोविरेचन + उपगानि → …ोपगानि (अ + उ → ओ); "
                  "दशेमानि + आस्थापनोपगानि → दशेमान्यास्थापनोपगानि और दशेमानि + अनुवासनोपगानि → दशेमान्यनुवासनोपगानि (इ → य्); "
                  "शोभाञ्जनकैरण्डार्क = शोभाञ्जनक + एरण्ड + अर्क (अ + ए → ऐ; अ + अ → आ), वैकल्पिक बँटवारा शोभाञ्जन + कैरण्ड नहीं लिया गया। "
                  "पाठ-दोष (text_flags): ‘क्षीरकालोली’ सम्भवतः ‘क्षीरकाकोली’ की टंकण-भूल है (का → ला), और ‘विडङ्गशिग्रु’ में विडङ्ग का अन्तिम -अ छूटा है। "
                  "टिप्पणी: ‘मधु’ और ‘मधुक’ तीसरे वर्ग में दो नाम हैं (पहचान नहीं दी गई); वत्सकफल, मदनफल, अपामार्गतण्डुल जैसे यौगिक एक-एक नाम माने गए। "
                  "संस्करण में यह पाठ कोष्ठक में छपा है।")

AIDS["13"] = {
    "frame": "सात वर्ग (२१–२७), हर में दस नाम · हर वर्ग का नाम = उपचार + उपग (सहायक) · अन्त: इति सप्तकः कषायवर्गः।",
    "diagram": {"groups": [
        {"label": "सात वर्गों के छपे नाम (क्रम से)",
         "items": ["स्नेहोपगानि", "स्वेदोपगानि", "वमनोपगानि", "विरेचनोपगानि",
                   "आस्थापनोपगानि", "अनुवासनोपगानि", "शिरोविरेचनोपगानि"]}]},
    "sandhi": "अ + उ → ओ: स्नेह + उपगानि → स्नेहोपगानि। इ → य्: दशेमानि + आस्थापनोपगानि → दशेमान्यास्थापनोपगानि।",
    "anchors": "उपग = उप (पास) + ग (जाने वाला) · स्नेहन = चिकना करना · स्वेदन = पसीना लाना · वमन = उल्टी · विरेचन = दस्त · शिरोविरेचन = सिर का शोधन · सप्तकः = सात का समूह।",
}

IMAGE_SPECS[("13", "diagram")] = {
    "file": "ch4-upaga-13.svg",
    "alt": "Table of unit 13 with seven rows, each a class label and the treatment it is an adjunct to: oleation, sweating, emesis, purgation, decoction enema, oil enema, head-purging",
    "type": "table",
    "title": "इकाई १३: सात उपग-वर्ग",
    "heads": ["वर्ग-नाम", "किसके सहायक"],
    "rows": [["स्नेहोपगानि", "स्नेहन (चिकनाई)"],
             ["स्वेदोपगानि", "स्वेदन (पसीना)"],
             ["वमनोपगानि", "वमन (उल्टी)"],
             ["विरेचनोपगानि", "विरेचन (दस्त)"],
             ["आस्थापनोपगानि", "आस्थापन (काढ़े की बस्ति)"],
             ["अनुवासनोपगानि", "अनुवासन (तेल की बस्ति)"],
             ["शिरोविरेचनोपगानि", "शिरोविरेचन (सिर-शोधन)"]],
}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "छर्दि, तृष्णा, हिक्का: तीन निग्रहण-वर्ग",
    "question": "Which three class labels does unit 14 give, and what does the ending -nigrahaṇa say?",
    "rule": ("Unit 14 gives three classes (28-30 of the 50) of ten names: chardi-, tṛṣṇā- and "
             "hikkā-nigrahaṇa, read literally as vomiting-checking, thirst-checking, hiccup-checking. "
             "It closes iti trikaḥ kaṣāyavargaḥ, a set of three."),
    "limits": ("The unit gives names and labels, no dose and no effect beyond the literal label. "
               "Two printed slips are flagged in the notes; amla-badara is taken as one name (otherwise "
               "eleven). Commentators may read nigrahaṇa a little differently."),
    "explain_hi": ("यह गद्य-इकाई वर्ग २८ से ३० देती है: तीन वर्ग, हर में दस नाम। तीनों नाम ‘निग्रहण’ पर खत्म होते हैं, जिसका आँकड़े में "
                   "अर्थ ‘रोकने वाला’ है: छर्दि-निग्रहण (उल्टी रोकने वाले), तृष्णा-निग्रहण (प्यास रोकने वाले) और "
                   "हिक्का-निग्रहण (हिचकी रोकने वाले)। ढाँचा पहले जैसा है: ‘दशेमानि X भवन्ति’। अन्त में ‘इति त्रिकः कषायवर्गः’ "
                   "तीन का समूह बताकर बन्द करता है। इससे आगे कोई खुराक या विशेष असर नहीं बताया गया।"),
    "hook": "तीन वर्ग: उल्टी, प्यास, हिचकी; सबके नाम ‘निग्रहण’ (रोकने वाले) पर खत्म।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Unit 14 has a class labelled हिक्कानिग्रहणानि. What does the label say about it?",
            ("It is hiccup-checking",
             "हिक्का = hiccup; निग्रहण = checking."),
            [("It is hiccup-causing", "निग्रहण is checking, not causing."),
             ("It is thirst-checking", "Thirst is तृष्णा, the second class."),
             ("It is vomiting-checking", "Vomiting is छर्दि, the first class.")],
            "हिक्कानिग्रहणानि = हिक्का + निग्रहणानि: the thing checked, then the checking.",
            "हिक्का-निग्रहण = hiccup-checking."),
        order(1, "Put the three class labels of unit 14 in the order they stand.",
              ["छर्दिनिग्रहणानि", "तृष्णानिग्रहणानि", "हिक्कानिग्रहणानि"],
              "The unit runs vomiting, thirst, hiccup.",
              "छर्दि → तृष्णा → हिक्का."),
        fill(2, "The unit closes with इति ____ कषायवर्गः, meaning a set of three. Type the missing word in Devanagari.",
             ["त्रिकः", "त्रिक"],
             "The closing formula reads इति त्रिकः कषायवर्गः.",
             "त्रिकः is त्रि (three) plus -क: a set of three. It counts the classes of this unit.",
             "त्रिकः = a set of three classes.",
             ),
        mcq("discriminate", 3, "How does the label हिक्कानिग्रहणानि differ from छर्दिनिग्रहणानि?",
            ("Only the first part: हिक्का, hiccup, against छर्दि, vomiting; both end in checking",
             "The common part is -निग्रहणानि."),
            [("Only the last part: one checks and the other produces", "Both end in -निग्रहणानि, checking."),
             ("The first has twelve names and the second ten", "Every class is introduced as दश, ten."),
             ("The first concerns thirst", "Thirst is तृष्णा; हिक्का is hiccup.")],
            "The two labels share -निग्रहणानि and differ only in the condition named first.",
            "X-निग्रहण: the first part names the condition checked."),
        multi("apply", 4, "Which of these does unit 14 say?",
              [("It gives three classes of ten names", "Right: classes 28-30, closed by त्रिकः."),
               ("Each class label ends in -निग्रहणानि, checking", "Right: all three do."),
               ("The conditions named are vomiting, thirst and hiccup", "Right: छर्दि, तृष्णा, हिक्का."),
               ("It gives a dose for each drug", "No dose is named."),
               ("It has five classes", "The closing word is त्रिकः, three.")],
              [0, 1, 2],
              "Three labels, all of the form condition + checking, closed by त्रिकः.",
              "Unit 14: three nigrahaṇa classes; no dose."),
        mcq("transfer", 5,
            "A made-up closing reads इति दशेमानि कासनिग्रहणानि भवन्ति (कास = cough). Following unit 14, what does it say?",
            ("These ten are cough-checking",
             "कास + निग्रहणानि, like हिक्का + निग्रहणानि 'hiccup-checking'."),
            [("These ten are cough-causing", "निग्रहण is checking, not causing."),
             ("These ten are coughs", "The label describes the drugs; it does not call them coughs."),
             ("These ten are cough-measuring", "Nothing in निग्रहण means measuring.")],
            "The pattern is X-निग्रहणानि: checking X. Only X changes.",
            "X-निग्रहण = checking X.",
            teaches="The ending -निग्रहण reads as checking whatever condition stands before it."),
    ],
}

NOTES_HI["14"] = ("संधियाँ जाँची: दश + इमानि → दशेमानि (अ + इ → ए); त्रिकः = त्रि + क (तद्धित -क), ‘इति’ सूची के अन्त पर। "
                  "पाठ-दोष (text_flags): (१) ‘कुलीरशृङ्ग्या इति’ में अन्त का -आ सम्भवतः -अ होना चाहिए (कुलीरशृङ्ग्यः + इति → कुलीरशृङ्ग्य इति); "
                  "(२) ‘यवयष्टिकोशीर’ में सम्भवतः ‘यवषषष्टिकोशीर’ चाहिए (ष → य की भूल), इसे यव, षष्टिक, उशीर पढ़ा गया; वर्ग फिर भी दस रहता है। "
                  "टिप्पणी: ‘अम्लबदर’ एक नाम माना गया (दो मानने पर ग्यारह)। ‘निग्रहण’ का अर्थ ‘रोकने वाला’ शाब्दिक रूप में है। "
                  "संस्करण में यह पाठ कोष्ठक में छपा है।")

AIDS["14"] = {
    "frame": "तीन वर्ग (२८–३०), हर में दस नाम · उल्टी (छर्दि), प्यास (तृष्णा), हिचकी (हिक्का) + निग्रहण (रोकने वाला) · अन्त: इति त्रिकः कषायवर्गः।",
    "chain": {"steps": [
        "वर्ग २८: छर्दिनिग्रहणानि (उल्टी रोकने वाले)",
        "वर्ग २९: तृष्णानिग्रहणानि (प्यास रोकने वाले)",
        "वर्ग ३०: हिक्कानिग्रहणानि (हिचकी रोकने वाले)"]},
    "sandhi": "अ + इ → ए: दश + इमानि → दशेमानि। त्रिकः = त्रि + क: तीन का समूह।",
    "anchors": "निग्रहण = नि + ग्रह् (पकड़ना, रोकना) · छर्दि = उल्टी · तृष्णा = प्यास · हिक्का = हिचकी · त्रिकः = त्रि (तीन) + क।",
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "पुरीष और मूत्र के पाँच वर्ग",
    "question": "Which five class labels does unit 15 give, and which of them concern faeces and which urine?",
    "rule": ("Unit 15 gives five classes (31-35 of the 50): purīṣa-saṃgrahaṇīya and purīṣa-virajanīya (faeces), then "
             "mūtra-saṃgrahaṇīya, mūtra-virajanīya and mūtra-virecanīya (urine). It closes iti pañcakaḥ kaṣāyavargaḥ."),
    "limits": ("The unit names drugs and labels only: no dose, no effect beyond the literal label. Class 32 is "
               "uncertain: its printed run splits into eleven names, ten only on another reading. Virajanīya "
               "is read cleansing; its exact sense is not stated."),
    "explain_hi": ("यह गद्य-इकाई वर्ग ३१ से ३५ देती है: पाँच वर्ग। पहले दो मल (पुरीष) से जुड़े हैं: संग्रहणीय (बाँधने/रोकने वाले) और "
                   "विरजनीय (शुद्ध करने वाले, पढ़ा गया)। अगले तीन मूत्र से जुड़े हैं: संग्रहणीय, विरजनीय और विरेचनीय (निकालने वाले)। "
                   "ढाँचा ‘दशेमानि X भवन्ति’ वही है और अन्त में ‘इति पञ्चकः कषायवर्गः’ पाँच का समूह बताता है। "
                   "दूसरे वर्ग (पुरीषविरजनीय) की सूची में छपे नाम-समूह की सीमा अनिश्चित है, इसलिए उसकी गिनती पर कोई प्रश्न नहीं बनाया गया। "
                   "यहाँ भी कोई खुराक या असर नहीं बताया गया।"),
    "hook": "पाँच वर्ग: मल के दो (बाँधने, शुद्ध करने), मूत्र के तीन (बाँधने, शुद्ध करने, निकालने)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The labels of unit 15 begin with पुरीष- or मूत्र-. What do these two first parts mean?",
            ("Faeces and urine",
             "पुरीष = faeces; मूत्र = urine."),
            [("Milk and semen", "Milk and semen (स्तन्य, शुक्र) are the substances of unit 12."),
             ("Thirst and vomiting", "Thirst and vomiting (तृष्णा, छर्दि) are conditions in unit 14."),
             ("Blood and sweat", "Neither is named in the labels of unit 15.")],
            "The first part of each label names the substance concerned.",
            "पुरीष = faeces; मूत्र = urine."),
        match(1, "Match each class label of unit 15 to its literal meaning.",
              [["पुरीषसंग्रहणीयानि", "faeces-binding"],
               ["पुरीषविरजनीयानि", "faeces-cleansing"],
               ["मूत्रसंग्रहणीयानि", "urine-binding"],
               ["मूत्रविरेचनीयानि", "urine-purging"]],
              "Each label is the substance plus a quality word: binding, cleansing or purging.",
              "संग्रहणीय = binding; विरजनीय = cleansing; विरेचनीय = purging."),
        fill(2, "The unit closes with इति ____ कषायवर्गः, meaning a set of five. Type the missing word in Devanagari.",
             ["पञ्चकः", "पञ्चक"],
             "The closing formula reads इति पञ्चकः कषायवर्गः.",
             "पञ्चकः is पञ्चन् (five) plus -क: a set of five. It counts the classes of this unit.",
             "पञ्चकः = a set of five classes.",
             ),
        mcq("discriminate", 3, "How do मूत्रसंग्रहणीयानि and मूत्रविरेचनीयानि differ?",
            ("Both concern urine; the first is binding, the second purging",
             "The first part मूत्र is common; संग्रहणीय and विरेचनीय differ."),
            [("The first concerns urine and the second faeces", "Both begin with मूत्र, urine."),
             ("The first has ten names and the second twelve", "Every class is introduced as दश, ten."),
             ("The first is a class of drugs and the second is not", "Both are classes, introduced by दशेमानि.")],
            "Same substance, different quality word: binding against purging.",
            "संग्रहणीय = binding; विरेचनीय = purging."),
        multi("apply", 4, "Which of these does unit 15 say?",
              [("It gives five classes", "Right: classes 31-35, closed by पञ्चकः."),
               ("The first two classes concern faeces", "Right: पुरीषसंग्रहणीय and पुरीषविरजनीय."),
               ("The last three classes concern urine", "Right: मूत्र- in the third, fourth and fifth labels."),
               ("It gives a dose for each drug", "No dose is named."),
               ("It has a class for hiccup", "Hiccup is the class हिक्कानिग्रहण of unit 14, not here.")],
              [0, 1, 2],
              "Two faeces labels first, then three urine labels, closed by पञ्चकः.",
              "Unit 15: five classes, two for faeces and three for urine; no dose."),
        mcq("transfer", 5,
            "A made-up closing reads इति दशेमानि स्वेदसंग्रहणीयानि भवन्ति (स्वेद = sweat). Following unit 15, what does it say?",
            ("These ten are sweat-binding",
             "स्वेद + संग्रहणीयानि, like पुरीष + संग्रहणीयानि 'faeces-binding'."),
            [("These ten are sweat-purging", "Purging is विरेचनीय, not संग्रहणीय."),
             ("These ten are sweat-producing", "Producing is -जनन from unit 12."),
             ("These ten are sweat", "The label describes the drugs; it does not call them sweat.")],
            "The pattern is X-संग्रहणीयानि: binding X. Only X changes.",
            "X-संग्रहणीय = binding X.",
            teaches="The ending -संग्रहणीय reads as binding the substance named before it."),
    ],
}

NOTES_HI["15"] = ("संधियाँ जाँची: दश + इमानि → दशेमानि (अ + इ → ए); पद्मकेशराणि + इति → पद्मकेशराणीति (इ + इ → ई); "
                  "प्रियङ्ग्वनन्ताम्रास्थि = प्रियङ्गु + अनन्ता + आम्र + अस्थि (उ → व् असमान स्वर से पहले; आ + अ → आ)। "
                  "‘सोमवल्का इति’ में ‘इति’ अलग छपा है। इस इकाई में पाठभेद या पाठ-दोष (text_flags) नहीं दिया गया। "
                  "टिप्पणी: दूसरे वर्ग का छपा समूह ‘जम्बुशल्लकीत्वक्कच्छुरा…तिलकणा’ सीमा/पाठ की अनसुलझी शंका है: जैसा बाँटा गया उसमें ग्यारह नाम बनते हैं, "
                  "‘त्वक्’ को ‘शल्लकी’ के साथ लेने पर दस, और ‘तिल’, ‘कणा’ अलग लेने पर बारह। इसलिए इस वर्ग की गिनती पर प्रश्न नहीं रखा। "
                  "‘विरजनीय’ को ‘शुद्ध करने वाला’ पढ़ा गया (वि-रञ्ज्, शाब्दिक ‘रंग हटाना’); सटीक अर्थ मूल में नहीं। संस्करण में यह पाठ कोष्ठक में छपा है।")

AIDS["15"] = {
    "frame": "पाँच वर्ग (३१–३५), हर में दस नाम · पुरीष (मल): संग्रहणीय, विरजनीय · मूत्र: संग्रहणीय, विरजनीय, विरेचनीय · अन्त: इति पञ्चकः कषायवर्गः।",
    "contrast": "पुरीष ↔ मूत्र: मल के दो वर्ग (बाँधने वाले, शुद्ध करने वाले) और मूत्र के तीन (बाँधने वाले, शुद्ध करने वाले, निकालने वाले)। मूत्र में तीसरा विरेचनीय है।",
    "sandhi": "अ + इ → ए: दश + इमानि → दशेमानि। इ + इ → ई: पद्मकेशराणि + इति → पद्मकेशराणीति।",
    "anchors": "संग्रहणीय = सम् + ग्रह् (इकट्ठा पकड़ना, बाँधना) · विरजनीय = वि + रञ्ज् (रंग हटाना; पढ़ा गया ‘शुद्ध करने वाला’) · विरेचनीय = निकालने/शुद्ध करने वाला · पुरीष = मल · मूत्र = पेशाब।",
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "कास से श्रम तक: पाँच -हर वर्ग",
    "question": "Which five class labels does unit 16 give, and what does the ending -hara add?",
    "rule": ("Unit 16 gives five classes (36-40 of the 50) of ten names, each ending -hara (removing): kāsa, "
             "śvāsa, śvayathu, jvara and śrama, read as cough, breathlessness, swelling, fever and fatigue. "
             "It closes iti pañcakaḥ kaṣāyavargaḥ."),
    "limits": ("The unit gives names and labels, no dose and no effect beyond the literal label. The name tāmalakī "
               "appears in two classes and parūṣaka/paruṣaka are spelt differently; whether they name the "
               "same drug is not decided. The edition prints the text in parentheses."),
    "explain_hi": ("यह गद्य-इकाई वर्ग ३६ से ४० देती है: पाँच वर्ग, हर में दस नाम। हर वर्ग-नाम ‘-हर’ (हरने वाला) पर खत्म होता है: "
                   "कासहर (खाँसी), श्वासहर (साँस की तकलीफ़), श्वयथुहर (सूजन), ज्वरहर (बुखार) और श्रमहर (थकान)। "
                   "यहाँ ‘तामलकी’ नाम दो वर्गों (पहले और दूसरे) में आता है, और ‘परूषक’/‘परुषक’ दो वर्तनियों में छपा है; "
                   "ये एक ही औषध हैं या नहीं, यह पाठ से तय नहीं होता। छपा रूप ‘तामलक्य इति’ में ‘इति’ अलग है; सामान्य नियम से यह "
                   "-अः + स्वर (अ से भिन्न) का रूप लगता है, जहाँ विसर्ग गिरता है और स्वर अलग रहते हैं। कोई खुराक या असर श्लोक नहीं देता।"),
    "hook": "पाँच वर्ग: खाँसी, साँस, सूजन, बुखार, थकान; सबके नाम ‘-हर’ (हरने वाले) पर खत्म।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Unit 16 has a class labelled श्रमहराणि. Going by the card, what does the label say?",
            ("Fatigue-removing",
             "श्रम = fatigue; हर = removing."),
            [("Fever-removing", "Fever is ज्वर, the fourth class."),
             ("Cough-removing", "Cough is कास, the first class."),
             ("Swelling-removing", "Swelling is श्वयथु, the third class.")],
            "श्रमहराणि = श्रम + हराणि: the thing removed, then the removing.",
            "श्रम-हर = fatigue-removing."),
        order(1, "Put the five class labels of unit 16 in the order they stand.",
              ["कासहराणि", "श्वासहराणि", "श्वयथुहराणि", "ज्वरहराणि", "श्रमहराणि"],
              "The unit runs cough, breathlessness, swelling, fever, fatigue.",
              "कास → श्वास → श्वयथु → ज्वर → श्रम."),
        fill(2, "In the label कासहराणि the last part, meaning removing, is ____ (Devanagari, plural as printed).",
             ["हराणि", "हर"],
             "कासहराणि = कास + हराणि.",
             "हराणि is neuter plural of हर, removing, agreeing with the ten names (neuter, दशेमानि).",
             "-हर = removing; it ends all five labels of unit 16.",
             ),
        mcq("discriminate", 3, "In the printed तामलक्य इति the word इति stands apart. What explains this?",
            ("After -यः (that is, अः) before a vowel other than अ the visarga drops and the vowels stay apart",
             "तामलक्यः + इति gives तामलक्य इति; the data's note on the typo in unit 14 treats the same pattern."),
            [("अ + इ always joins to ए", "That rule joins दश + इमानि; here the word ends in a visarga, which drops instead."),
             ("The visarga turns to ओ before इ", "ओ comes from अः before a voiced consonant, not before a vowel."),
             ("इति is always printed apart", "In this unit इति is joined elsewhere, as in बिभीतकानीति.")],
            "The visarga is not printed, but the open gap fits the rule: -अः + a vowel other than अ drops the visarga and leaves the vowels apart.",
            "-अः + vowel (not अ) → visarga drops, no joining."),
        multi("apply", 4, "Which of these does unit 16 say?",
              [("It gives five classes of ten names", "Right: classes 36-40, closed by पञ्चकः."),
               ("Each class label ends in -हराणि, removing", "Right: all five do."),
               ("The name tāmalakī appears in both the cough class and the breathlessness class", "Right: तामलकी is in the first and second classes."),
               ("It gives a dose for each drug", "No dose is named."),
               ("It has a class for hiccup", "Hiccup is in unit 14, not here.")],
              [0, 1, 2],
              "Five labels of the form condition + removing, closed by पञ्चकः.",
              "Unit 16: five -hara classes; no dose."),
        mcq("transfer", 5,
            "A made-up closing reads इति दशेमानि शोकहराणि भवन्ति (शोक = grief). Following unit 16, what does it say?",
            ("These ten are grief-removing",
             "शोक + हराणि, like कास + हराणि 'cough-removing'."),
            [("These ten are grief-causing", "-हर means removing, not causing."),
             ("These ten are grief", "The label describes the drugs; it does not call them grief."),
             ("These ten are grief-checking", "Checking is -निग्रहण from unit 14, not -हर.")],
            "The pattern is X-हराणि: removing X. Only X changes.",
            "X-हर = removing X.",
            teaches="The ending -हर reads as removing the condition named before it."),
    ],
}

NOTES_HI["16"] = ("संधियाँ जाँची: दश + इमानि → दशेमानि (अ + इ → ए); ‘तामलक्य इति’ और अन्य जगह ‘…ानीति’ (इ + इ → ई); "
                  "‘इति’ कहीं जुड़ा और कहीं अलग छपा है। इस इकाई में पाठभेद या पाठ-दोष (text_flags) नहीं दिया गया "
                  "(पर इकाई १४ का एक पाठ-दोष इसी ‘तामलक्य इति’ रूप से तुलना करता है)। "
                  "टिप्पणी: ‘शालपर्णी’ और ‘पृश्निपर्णी’ हर एक नाम हैं; ‘तामलकी’ वर्ग १ और २ में, ‘शृङ्गी’ वर्ग १ में आता है (कुलीरशृङ्गी इकाई १४ में); "
                  "वही औषध है या नहीं, तय नहीं। ‘परूषक’ (वर्ग ४) और ‘परुषक’ (वर्ग ५) अलग वर्तनी हैं, पहचान तय नहीं। संस्करण में यह पाठ कोष्ठक में छपा है।")

AIDS["16"] = {
    "frame": "पाँच वर्ग (३६–४०), हर में दस नाम · रोग/स्थिति + हर (हरने वाला): खाँसी, साँस, सूजन, बुखार, थकान · अन्त: इति पञ्चकः कषायवर्गः।",
    "diagram": {"groups": [
        {"label": "पाँच वर्गों के छपे नाम (क्रम से)",
         "items": ["कासहराणि", "श्वासहराणि", "श्वयथुहराणि", "ज्वरहराणि", "श्रमहराणि"]}]},
    "sandhi": "अः + स्वर (अ से भिन्न): विसर्ग गिरता है, स्वर अलग रहते हैं: तामलक्यः + इति → तामलक्य इति (छपा रूप)। अ + इ → ए: दश + इमानि → दशेमानि।",
    "anchors": "हर = हरने वाला (हृ-धातु) · कास = खाँसी · श्वास = साँस · श्वयथु = सूजन · ज्वर = बुखार · श्रम = थकान · पञ्चकः = पाँच का समूह।",
}

IMAGE_SPECS[("16", "diagram")] = {
    "file": "ch4-hara-16.svg",
    "alt": "Table of unit 16 with five rows, each a class label and what it removes: cough, breathlessness, swelling, fever, fatigue",
    "type": "table",
    "title": "इकाई १६: पाँच -हर वर्ग (३६–४०)",
    "heads": ["वर्ग-नाम", "क्या हरने वाले"],
    "rows": [["कासहराणि", "खाँसी हरने वाले"],
             ["श्वासहराणि", "साँस की तकलीफ़ हरने वाले"],
             ["श्वयथुहराणि", "सूजन हरने वाले"],
             ["ज्वरहराणि", "बुखार हरने वाले"],
             ["श्रमहराणि", "थकान हरने वाले"]],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "दाह से शूल तक: पाँच प्रशमन-वर्ग",
    "question": "Which five class labels does unit 17 give, and which two name a pair of opposites?",
    "rule": ("Unit 17 gives five classes (41-45 of the 50) of ten names, each ending -praśamana (soothing): "
             "dāha (burning), śīta (cold), udarda, aṅgamarda (body-ache) and śūla (pain). "
             "It closes iti pañcakaḥ kaṣāyavargaḥ."),
    "limits": ("The unit gives names and labels, no dose, no effect beyond the literal label. Class 43 has "
               "aśvakarṇa twice as printed (likely a doubled word), so it shows eleven names; this is not "
               "resolved here. Udarda is left untranslated in the data."),
    "explain_hi": ("यह गद्य-इकाई वर्ग ४१ से ४५ देती है: पाँच वर्ग, हर में दस नाम (तीसरे वर्ग में छपा रूप ग्यारह दिखाता है, नीचे देखें)। "
                   "हर नाम ‘-प्रशमन’ (शान्त करने वाला) पर खत्म होता है: दाहप्रशमन (जलन), शीतप्रशमन (ठण्ड), उदर्दप्रशमन, "
                   "अङ्गमर्दप्रशमन (अंगों की पीड़ा) और शूलप्रशमन (पीड़ा)। पहले दो नामों में दाह और शीत एक जोड़ा बनाते हैं: जलन ↔ ठण्ड। "
                   "‘उदर्द’ का अर्थ आँकड़े में नहीं दिया गया, इसलिए इसे नाम की तरह ही रखा गया है। तीसरे वर्ग में ‘अश्वकर्ण’ दो बार छपा है; "
                   "यह दोहराव जैसा लगता है, पर यहाँ तय नहीं किया गया। कोई खुराक या असर नहीं बताया गया।"),
    "hook": "पाँच वर्ग: जलन, ठण्ड, उदर्द, अङ्गमर्द, शूल; सबके नाम ‘-प्रशमन’ (शान्त करने वाले) पर खत्म।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Unit 17 has a class labelled शीतप्रशमनानि. Going by the card, what does the label say?",
            ("Cold-soothing",
             "शीत = cold; प्रशमन = soothing."),
            [("Cold-causing", "प्रशमन is soothing, not causing."),
             ("Burning-soothing", "Burning is दाह, the first class."),
             ("Pain-soothing", "Pain is शूल, the last class.")],
            "शीतप्रशमनानि = शीत + प्रशमनानि: what is soothed, then the soothing.",
            "शीत-प्रशमन = cold-soothing."),
        match(1, "Match each class label of unit 17 to its literal meaning.",
              [["दाहप्रशमनानि", "burning-soothing"],
               ["शीतप्रशमनानि", "cold-soothing"],
               ["अङ्गमर्दप्रशमनानि", "body-ache-soothing"],
               ["शूलप्रशमनानि", "pain-soothing"]],
              "Each label is a condition plus -प्रशमनानि, soothing.",
              "दाह = burning; शीत = cold; अङ्गमर्द = body-ache; शूल = pain; प्रशमन = soothing."),
        fill(2, "In the label शीतप्रशमनानि the last part, meaning soothing, is ____ (Devanagari, plural as printed).",
             ["प्रशमनानि", "प्रशमन"],
             "शीतप्रशमनानि = शीत + प्रशमनानि.",
             "प्रशमनानि is neuter plural, agreeing with the ten names (दशेमानि).",
             "-प्रशमन = soothing; it ends all five labels of unit 17.",
             ),
        mcq("discriminate", 3, "Which is the right split of दशेमान्युदर्दप्रशमनानि?",
            ("दशेमानि + उदर्दप्रशमनानि",
             "इ before an unlike vowel becomes य् and the vowel joins it: इ + उ gives यु."),
            [("दशेमान् + युदर्दप्रशमनानि", "युदर्द is not the name; the class is उदर्द."),
             ("दशेमाना + उदर्दप्रशमनानि", "दशेमाना is not a form; the word is दशेमानि."),
             ("दशे + मान्युदर्दप्रशमनानि", "मान्युदर्दप्रशमनानि is not a word.")],
            "दशेमान्युदर्दप्रशमनानि = दशेमानि ('these ten') + उदर्दप्रशमनानि (the label).",
            "इ + असमान स्वर → य् + स्वर: दशेमानि + उदर्द… → दशेमान्युदर्द…."),
        multi("apply", 4, "Which of these does unit 17 say?",
              [("It gives five classes", "Right: classes 41-45, closed by पञ्चकः."),
               ("The first class is burning-soothing and the second cold-soothing", "Right: दाहप्रशमन then शीतप्रशमन."),
               ("The last class is pain-soothing", "Right: शूलप्रशमनानि."),
               ("It gives a dose for each drug", "No dose is named."),
               ("It has a class for fever", "Fever is ज्वरहराणि in unit 16, not here.")],
              [0, 1, 2],
              "Five labels of the form condition + soothing, from burning to pain.",
              "Unit 17: five -praśamana classes; no dose."),
        mcq("transfer", 5,
            "A made-up closing reads इति दशेमानि तृषाप्रशमनानि भवन्ति (तृषा = thirst). Following unit 17, what does it say?",
            ("These ten are thirst-soothing",
             "तृषा + प्रशमनानि, like शीत + प्रशमनानि 'cold-soothing'."),
            [("These ten are thirst-causing", "प्रशमन is soothing, not causing."),
             ("These ten are thirst", "The label describes the drugs; it does not call them thirst."),
             ("These ten are thirst-measuring", "Nothing in प्रशमन means measuring.")],
            "The pattern is X-प्रशमनानि: soothing X. Only X changes.",
            "X-प्रशमन = soothing X.",
            teaches="The ending -प्रशमन reads as soothing the condition named before it."),
    ],
}

NOTES_HI["17"] = ("संधियाँ जाँची: दश + इमानि → दशेमानि (अ + इ → ए); दशेमानि + उदर्द… → दशेमान्युदर्द… और दशेमानि + अङ्गमर्द… → दशेमान्यङ्गमर्द… (इ → य्); "
                  "कण्टकारिका + एरण्ड → कण्टकारिकैरण्ड (अ + ए → ऐ)। पाठ-दोष (text_flags): तीसरे वर्ग में ‘अश्वकर्ण’ दो बार छपा है "
                  "(सम्भवतः द्वित्व-भूल); जैसा छपा है उसमें ग्यारह नाम बनते हैं, एक हटाने पर दस। यहाँ तय नहीं किया गया और गिनती पर प्रश्न नहीं रखा। "
                  "टिप्पणी: ‘विदारीगन्धा’ एक नाम माना गया (दो मानने पर ग्यारह); ‘ह्रिबेर’ छोटी इ से छपा है, उसे वैसा ही रखा। "
                  "‘उदर्द’ का अर्थ आँकड़े में नहीं दिया। संस्करण में यह पाठ कोष्ठक में छपा है।")

AIDS["17"] = {
    "frame": "पाँच वर्ग (४१–४५), हर में दस नाम · स्थिति + प्रशमन (शान्त करने वाला): जलन, ठण्ड, उदर्द, अङ्गमर्द, शूल · अन्त: इति पञ्चकः कषायवर्गः।",
    "seesaw": "दाह (जलन) ↔ शीत (ठण्ड): पहले दो वर्गों के नाम इसी जोड़े से बने हैं; दोनों ‘-प्रशमन’ (शान्त करने वाले) हैं।",
    "sandhi": "इ → य् असमान स्वर से पहले: दशेमानि + उदर्द… → दशेमान्युदर्द…; दशेमानि + अङ्गमर्द… → दशेमान्यङ्गमर्द…।",
    "anchors": "प्रशमन = प्र + शम् (शान्त होना) का भाव, शान्त करने वाला · दाह = जलन · शीत = ठण्ड · अङ्गमर्द = अङ्ग + मर्द (शरीर की पीड़ा) · शूल = तीव्र पीड़ा।",
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "शोणित से वयः तक: पाँच स्थापन-वर्ग",
    "question": "Which five class labels does unit 18 give, and which classes close the fifty?",
    "rule": ("Unit 18 gives the last five classes (46-50 of the 50), each of ten names, each ending -sthāpana: "
             "śoṇita (blood), vedanā (pain), saṃjñā (consciousness), prajā (progeny), vayas (age). "
             "It closes iti pañcakaḥ kaṣāyavargaḥ."),
    "limits": ("The unit gives names and labels, no dose and no effect beyond the literal label; sthāpana is "
               "rendered stabilizing in some labels and establishing in others. Two printed slips are flagged in "
               "the notes (gairikarpiyaṅgu, śatavīrya). The edition prints the text in parentheses."),
    "explain_hi": ("यह गद्य-इकाई वर्ग ४६ से ५० देती है, यानी पचास वर्गों की सूची की अन्तिम इकाई; पाँच वर्ग, हर में दस नाम। हर नाम "
                   "‘-स्थापन’ (स्थिर/स्थापित करने वाला) पर खत्म होता है: शोणितस्थापन (रक्त), वेदनास्थापन (पीड़ा), संज्ञास्थापन (चेतना), "
                   "प्रजास्थापन (सन्तान) और वयःस्थापन (आयु)। चौथे और पाँचवें वर्ग की सूचियों में छपा ‘ऽ’ चिह्न (अवग्रह) बताता है कि "
                   "आ के बाद आने वाला अगला नाम ‘अ’ से शुरू होता है, जैसे ‘सहस्रवीर्या ऽमोघा’ = सहस्रवीर्या, अमोघा। "
                   "वयःस्थापन में ‘वयः’ का विसर्ग छपा है। कोई खुराक या विशेष असर नहीं बताया गया।"),
    "hook": "अन्तिम पाँच वर्ग: रक्त, पीड़ा, चेतना, सन्तान, आयु; सबके नाम ‘-स्थापन’। ‘ऽ’ = छूटा हुआ ‘अ’।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which label is the last class of unit 18, and so the last of the fifty?",
            ("वयःस्थापनानि, age-stabilizing",
             "The fifth label is वयः-स्थापन, with वयस् meaning age."),
            [("शोणितस्थापनानि, blood-stabilizing", "This is the first class of the unit."),
             ("वेदनास्थापनानि, pain-stabilizing", "This is the second class."),
             ("प्रजास्थापनानि, progeny-establishing", "This is the fourth class, not the last.")],
            "The unit runs शोणित, वेदना, संज्ञा, प्रजा, वयः; the footnote numbers in the edition count 46 to 50.",
            "Unit 18 = classes 46-50; the last is वयःस्थापन."),
        order(1, "Put the five class labels of unit 18 in the order they stand.",
              ["शोणितस्थापनानि", "वेदनास्थापनानि", "संज्ञास्थापनानि", "प्रजास्थापनानि", "वयःस्थापनानि"],
              "The unit runs blood, pain, consciousness, progeny, age.",
              "शोणित → वेदना → संज्ञा → प्रजा → वयः."),
        fill(2, "All five labels of unit 18 end in ____, meaning stabilizing or establishing (Devanagari, plural as printed).",
             ["स्थापनानि", "स्थापन"],
             "Each label is a noun plus -स्थापनानि.",
             "स्थापनानि is neuter plural, agreeing with the ten names (दशेमानि).",
             "-स्थापन = stabilizing, establishing; it ends all five labels of unit 18.",
             ),
        mcq("discriminate", 3, "In सहस्रवीर्या ऽमोघा, what does the sign ऽ stand for?",
            ("The initial अ of the name अमोघा, dropped after the final आ",
             "The data reads ऽमोघा as अमोघा, a name beginning with अ."),
            [("A long आ added to the end of the word", "The sign marks a dropped अ at the start of the next name."),
             ("A visarga after सहस्रवीर्या", "The sign is the avagraha, not a visarga."),
             ("The word इति closing the list", "इति is printed separately at the end of each list.")],
            "The avagraha ऽ shows an अ that has merged after a preceding long vowel; the second name is अमोघा.",
            "ऽ (avagraha) = a dropped initial अ."),
        multi("apply", 4, "Which of these does unit 18 say?",
              [("It gives five classes, which close the list of fifty", "Right: classes 46-50."),
               ("The first class is शोणितस्थापनानि, blood-stabilizing", "Right: it stands first."),
               ("The sign ऽ appears in the lists of the fourth and fifth classes", "Right: ऽमोघा, ऽव्यथा, ऽरिष्टा in the fourth; अमृता ऽभया in the fifth."),
               ("It gives a dose for each drug", "No dose is named."),
               ("It has a class for fever", "Fever is ज्वरहराणि in unit 16, not here.")],
              [0, 1, 2],
              "Five labels of the form substance or condition + stabilizing, with ऽ in the last two lists.",
              "Unit 18: five -sthāpana classes; last of the fifty; no dose."),
        mcq("transfer", 5,
            "A made-up closing reads इति दशेमानि स्वरस्थापनानि भवन्ति (स्वर = voice). Following unit 18, what does it say?",
            ("These ten are voice-stabilizing",
             "स्वर + स्थापनानि, like वयः + स्थापनानि 'age-stabilizing'."),
            [("These ten are voice-removing", "Removing is -घ्न or -हर, not -स्थापन."),
             ("These ten are voice-soothing", "Soothing is -प्रशमन from unit 17."),
             ("These ten are voice", "The label describes the drugs; it does not call them voice.")],
            "The pattern is X-स्थापनानि: stabilizing, establishing X. Only X changes.",
            "X-स्थापन = stabilizing X.",
            teaches="The ending -स्थापन reads as stabilizing or establishing what stands before it."),
    ],
}

NOTES_HI["18"] = ("संधियाँ जाँची: दश + इमानि → दशेमानि (अ + इ → ए); अवग्रह ‘ऽ’: ‘…वीर्या ऽमोघा ऽव्यथा…ऽरिष्टा’ और ‘अमृता ऽभया’ में आ के बाद अगला नाम अ से शुरू होता है "
                  "(टिप्पणी के अनुसार ये अ-आदि नाम हैं); वयः + स्थापनानि → वयःस्थापनानि (विसर्ग छपा)। पाठ-दोष (text_flags): "
                  "(१) ‘शतवीर्यसहस्रवीर्या’ में सम्भवतः ‘शतवीर्या’ का दीर्घ आ छूटा है, पर समास के आरम्भ में ह्रस्व भी सम्भव है; "
                  "(२) ‘गैरिकर्पियङ्गु’ सम्भवतः ‘गैरिक-प्रियङ्गु’ की उलटफेर है (सम्भावित पर पक्का नहीं)। "
                  "टिप्पणी: ‘अशोकरोहिणी’ एक नाम माना गया; ‘मोचरस’ वर्ग १ और २ दोनों में आता है। इसलिए इन वर्गों के नामों पर प्रश्न नहीं रखे। "
                  "संस्करण में यह पाठ कोष्ठक में छपा है।")

AIDS["18"] = {
    "frame": "अन्तिम पाँच वर्ग (४६–५०), हर में दस नाम · शोणित, वेदना, संज्ञा, प्रजा, वयः + स्थापन · ‘ऽ’ = छूटा हुआ अ · अन्त: इति पञ्चकः कषायवर्गः।",
    "chain": {"steps": [
        "वर्ग ४६: शोणितस्थापनानि",
        "वर्ग ४७: वेदनास्थापनानि",
        "वर्ग ४८: संज्ञास्थापनानि",
        "वर्ग ४९: प्रजास्थापनानि",
        "वर्ग ५०: वयःस्थापनानि"]},
    "sandhi": "अवग्रह ऽ: सहस्रवीर्या ऽमोघा = सहस्रवीर्या + अमोघा (अ का लोप दिखाने वाला चिह्न); अमृता ऽभया = अमृता + अभया। अ + इ → ए: दश + इमानि → दशेमानि।",
    "anchors": "स्थापन = स्था (ठहरना) का णिजन्त भाव, स्थिर करना · शोणित = रक्त · वेदना = पीड़ा · संज्ञा = चेतना · प्रजा = सन्तान · वयस् = आयु (यहाँ विसर्ग के साथ वयः)।",
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "इति पञ्चकषायशतान्यभिसमस्य",
    "question": "What does unit 19 say has been set forth, after summing up the five hundred kaṣāyas, and for what purpose?",
    "rule": ("Having summed up the five hundred kaṣāyas, fifty great kaṣāyas (mahākaṣāya) have been set forth, "
             "for characterization (lakṣaṇa) and illustration (udāharaṇa) of the great kaṣāyas as well. "
             "One sentence, no verse."),
    "limits": ("The sentence does not say how the five hundred are made up, nor define lakṣaṇa and udāharaṇa "
               "further. Abhisamasya is read as having summed up; the ca after mahatām is slightly redundant."),
    "explain_hi": ("यह एक ही वाक्य की गद्य-इकाई है और पचास वर्गों की सूची को समेटती है। ‘इति पञ्चकषायशतान्यभिसमस्य’ का अर्थ है "
                   "‘इस प्रकार पाँच सौ कषायों को समेटकर’ (अभिसमस्य = एकत्र करके)। फिर कहा गया है कि ‘पञ्चाशन्महाकषायाः’, यानी "
                   "पचास महाकषाय ‘व्याख्याताः’ (बताए गए) हैं। प्रयोजन ‘लक्षणोदाहरणार्थम्’ है: लक्षण (पहचान) और उदाहरण (दृष्टान्त) के लिए, "
                   "और ‘महतां च कषायाणाम्’ से बड़े कषायों के लिए भी। वाक्य यह नहीं बताता कि पाँच सौ किस तरह बने, और न लक्षण-उदाहरण की और व्याख्या करता है।"),
    "hook": "५०० कषाय समेटकर → ५० महाकषाय बताए: लक्षण + उदाहरण के लिए।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Unit 19 says fifty great kaṣāyas have been set forth. For what purpose?",
            ("For characterization and illustration (लक्षणोदाहरणार्थम्)",
             "लक्षण = characterization; उदाहरण = illustration; अर्थम् = for the sake of."),
            [("To give the dose of each drug", "No dose is mentioned in the sentence."),
             ("To name the physician who tested them", "No physician is named."),
             ("To list the diseases the drugs cure", "No disease is named in this sentence.")],
            "The purpose word is लक्षणोदाहरणार्थम्, 'for characterization and illustration'.",
            "Purpose of the fifty: lakṣaṇa and udāharaṇa."),
        match(1, "Match each word of unit 19 to its meaning.",
              [["पञ्चाशत्", "fifty"],
               ["शतानि", "hundreds"],
               ["लक्षण", "characterization"],
               ["उदाहरण", "illustration"]],
              "These four words carry the numbers and the purpose.",
              "पञ्चाशत् = fifty; शतानि = hundreds; लक्षण = characterization; उदाहरण = illustration."),
        fill(2, "The word for having summed up, ending the first clause, is ____ (type it in Devanagari).",
             ["अभिसमस्य"],
             "The first clause ends ...शतान्यभिसमस्य.",
             "अभिसमस्य is an absolutive: an action finished before the main verb, 'having summed up'.",
             "अभिसमस्य = having summed up; it comes before the main clause.",
             ),
        mcq("discriminate", 3, "Which is the right split of पञ्चाशन्महाकषायाः?",
            ("पञ्चाशत् + महाकषायाः",
             "त् before म becomes न्, so पञ्चाशत् + महाकषायाः is written पञ्चाशन्महाकषायाः."),
            [("पञ्चाशः + महाकषायाः", "With a visarga the words would stay apart."),
             ("पञ्चा + शन्महाकषायाः", "शन्महाकषायाः is not a word."),
             ("पञ्चाश + न्महाकषायाः", "न्महाकषायाः is not a word.")],
            "पञ्चाशन्महाकषायाः = पञ्चाशत् ('fifty') + महाकषायाः ('great kaṣāyas').",
            "त् + म → न्म: पञ्चाशत् + महा… → पञ्चाशन्महा…."),
        multi("apply", 4, "Which of these does unit 19 say?",
              [("The five hundred kaṣāyas have been summed up", "Right: पञ्चकषायशतान्यभिसमस्य."),
               ("Fifty great kaṣāyas have been set forth", "Right: पञ्चाशन्महाकषायाः ... व्याख्याताः."),
               ("The purpose is characterization and illustration", "Right: लक्षणोदाहरणार्थम्."),
               ("The sentence names the drugs of each great kaṣāya", "No drug is named in this unit."),
               ("The sentence gives the dose", "No dose is named.")],
              [0, 1, 2],
              "One sentence: a sum-up, a number, a purpose.",
              "Unit 19: five hundred summed up; fifty set forth; for lakṣaṇa and udāharaṇa."),
        mcq("transfer", 5,
            "A made-up word पठनार्थम् is built like लक्षणोदाहरणार्थम् (पठन = reading). What does it mean?",
            ("For the sake of reading",
             "X-अर्थम् = for the sake of X."),
            [("By means of reading", "-अर्थम् gives purpose, not means."),
             ("Because of the reader's age", "Nothing in the word mentions the reader."),
             ("After reading", "-अर्थम् does not mark time.")],
            "The word ends in -अर्थम्, 'for the sake of'. Only the first part changes: पठन = reading.",
            "X-अर्थम् = for the sake of X.",
            teaches="A word ending in -अर्थम् states the purpose, as in लक्षणोदाहरणार्थम्."),
    ],
}

NOTES_HI["19"] = ("संधियाँ जाँची: पञ्चकषायशतानि + अभिसमस्य → पञ्चकषायशतान्यभिसमस्य (इ → य्); पञ्चाशत् + महाकषायाः → पञ्चाशन्महाकषायाः (त् → न् म से पहले); "
                  "लक्षण + उदाहरण → लक्षणोदाहरण (अ + उ → ओ); उदाहरण + अर्थम् → उदाहरणार्थम् (अ + अ → आ)। पाठभेद या पाठ-दोष नहीं दिया गया। "
                  "टिप्पणी के अनुसार ‘अभिसमस्य’ को अभि-सम्-√अस् का ल्यप्-रूप (उपसर्ग-सहित, ‘समेटकर’) माना गया है; ‘महतां च कषायाणाम्’ में ‘च’ कुछ फालतू-सा है। "
                  "‘पञ्चाशत्’ आँकड़े में स्त्रीलिंग एकवचन है, जबकि ‘महाकषायाः’ पुल्लिंग बहुवचन है; इन संख्या-शब्दों में ऐसा मेल सामान्य है।")

AIDS["19"] = {
    "frame": "पहले ५०० कषाय समेटे (अभिसमस्य) → फिर ५० महाकषाय बताए (व्याख्याताः) → प्रयोजन: लक्षण (पहचान) + उदाहरण, महान् कषायों के भी लिए।",
    "sandhi": "त् → न् (म से पहले): पञ्चाशत् + महाकषायाः → पञ्चाशन्महाकषायाः। अ + उ → ओ: लक्षण + उदाहरण → लक्षणोदाहरण। अ + अ → आ: उदाहरण + अर्थम् → उदाहरणार्थम्।",
    "anchors": "अभिसमस्य = अभि + सम् + अस्य (समेटकर) · पञ्चाशत् = पाँच दहाई = पचास · लक्षण = पहचान का चिह्न · उदाहरण = दृष्टान्त · अर्थम् = के लिए।",
    "chunks": "इति पञ्चकषायशतान्यभिसमस्य | पञ्चाशन्महाकषाया महतां च कषायाणां | लक्षणोदाहरणार्थं व्याख्याता भवन्ति।",
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "नहि विस्तरस्य प्रमाणमस्ति",
    "question": "What two reasons does unit 20 give, and what does it conclude about how the kaṣāyas were taught?",
    "rule": ("There is no limit to elaboration (vistara), and excessive brevity (atisaṃkṣepa) does not serve "
             "the capability of the dull-witted; therefore the kaṣāyas are taught neither with excessive "
             "brevity nor with excessive elaboration. The subject is understood from the previous unit."),
    "limits": ("The subject of upadiṣṭāḥ is not printed; it is taken from unit 19. Sāmarthyāya upakalpate is "
               "read serves for capability; another reading is does not suffice to produce competence."),
    "explain_hi": ("यह गद्य-इकाई पिछली इकाई (१९) की बात का कारण देती है; ‘उपदिष्टाः’ का कर्ता छपा नहीं, पिछली इकाई से लिया गया है। "
                   "पहला कारण: ‘नहि विस्तरस्य प्रमाणमस्ति’, यानी विस्तार की कोई सीमा नहीं। दूसरा: ‘न चाप्यतिसंक्षेपः … सामर्थ्याय "
                   "उपकल्पते’, यानी अत्यन्त संक्षेप भी अल्पबुद्धि वालों की सामर्थ्य के काम नहीं आता (दूसरा सम्भव अर्थ: सामर्थ्य पैदा नहीं करता)। "
                   "इसलिए (तस्मात्) उपदेश ‘अनतिसंक्षेपेण अनतिविस्तरेण’, यानी न बहुत संक्षेप से और न बहुत विस्तार से, किया गया। "
                   "‘अन्-अति-’ का अर्थ है ‘अति नहीं’, अर्थात् अधिकता नहीं।"),
    "hook": "विस्तार की सीमा नहीं + अति-संक्षेप कमज़ोर बुद्धि के काम नहीं → इसलिए न अति-संक्षेप, न अति-विस्तार।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Unit 20 opens नहि विस्तरस्य प्रमाणमस्ति. What is said to have no limit?",
            ("Elaboration (विस्तर)",
             "विस्तरस्य = of elaboration; प्रमाणम् = limit, measure; नहि ... अस्ति = there is no ..."),
            [("The number of drugs", "No drug or number is mentioned in this unit."),
             ("The length of life", "Life is not mentioned in this unit."),
             ("The skill of the physician", "No physician is mentioned in this unit.")],
            "विस्तरस्य प्रमाणं नास्ति: of elaboration there is no limit.",
            "विस्तर = elaboration; प्रमाण = limit; नहि ... अस्ति = there is no."),
        match(1, "Match each word of unit 20 to its meaning.",
              [["विस्तर", "elaboration"],
               ["संक्षेप", "brevity"],
               ["अल्पबुद्धि", "dull-witted"],
               ["प्रमाण", "limit, measure"]],
              "These four words carry the two reasons.",
              "विस्तर = elaboration; संक्षेप = brevity; अल्पबुद्धि = dull-witted (small-minded); प्रमाण = limit."),
        fill(2, "In the first clause the word for limit or measure is ____ (type it in Devanagari).",
             ["प्रमाणम्", "प्रमाणं"],
             "The clause reads नहि विस्तरस्य प्रमाणमस्ति.",
             "प्रमाणम् is neuter nominative singular, the subject of अस्ति: the limit is not.",
             "प्रमाण = limit, measure; it is the subject of अस्ति."),
        mcq("discriminate", 3, "Which is the right split of चोपदिष्टाः?",
            ("च + उपदिष्टाः",
             "अ + उ joins to ओ: च + उपदिष्टाः gives चोपदिष्टाः."),
            [("चो + पदिष्टाः", "पदिष्टाः is not a word here."),
             ("चः + उपदिष्टाः", "With a visarga the words would stay apart: च उपदिष्टाः."),
             ("चा + उपदिष्टाः", "चा is not the word; the particle is च.")],
            "चोपदिष्टाः = च ('and') + उपदिष्टाः ('taught').",
            "अ + उ → ओ: च + उपदिष्टाः → चोपदिष्टाः."),
        multi("apply", 4, "Which of these does unit 20 say?",
              [("There is no limit to elaboration", "Right: नहि विस्तरस्य प्रमाणमस्ति."),
               ("Excessive brevity does not serve the capability of the dull-witted", "Right: न चाप्यतिसंक्षेपोऽल्पबुद्धीनां ..."),
               ("The kaṣāyas are taught neither too briefly nor too elaborately", "Right: अनतिसंक्षेपेणानतिविस्तरेण चोपदिष्टाः."),
               ("Elaboration is better than brevity for everyone", "The unit says elaboration has no limit; it does not rank it above brevity."),
               ("The unit gives the dose of each drug", "No dose is named.")],
              [0, 1, 2],
              "Two reasons, then the conclusion marked by तस्मात्, therefore.",
              "Unit 20: no limit to elaboration; too little brevity helps no one; so taught in the middle."),
        mcq("transfer", 5,
            "A made-up word अनतिदीर्घेण (दीर्घ = long) is built like अनतिसंक्षेपेण. What does it mean?",
            ("Without excessive length",
             "अन् + अति + दीर्घ: not excessive length, as अनतिविस्तर is without excessive elaboration."),
            [("With excessive length", "अन्- negates अति-; the sense is not excessive."),
             ("Without any length at all", "अनति- negates the excess only, not the quality."),
             ("Of excessive length", "That would drop the negation अन्.")],
            "The pattern is अनति-X: not excessive X. Only X changes.",
            "अनति-X = without excessive X.",
            teaches="The prefix अनति- means not too much; it can be put on any quality, as in unit 20."),
    ],
}

NOTES_HI["20"] = ("संधियाँ जाँची: न + च + अपि + अतिसंक्षेपः → न चाप्यतिसंक्षेपः (च + अपि → चापि, अ + अ → आ; अपि + अति… → अप्यति…, इ → य्); अतिसंक्षेपः + अल्पबुद्धीनाम् → अतिसंक्षेपोऽल्पबुद्धीनाम् "
                  "(अः + अ → ओऽ, अवग्रह); सामर्थ्याय + उपकल्पते → सामर्थ्यायोपकल्पते (अ + उ → ओ); तस्मात् + अनतिसंक्षेपेण → तस्मादनतिसंक्षेपेण (त् → द्); "
                  "अनतिसंक्षेपेण + अनतिविस्तरेण → अनतिसंक्षेपेणानतिविस्तरेण (अ + अ → आ); च + उपदिष्टाः → चोपदिष्टाः (अ + उ → ओ)। "
                  "पाठभेद या पाठ-दोष नहीं दिया गया। टिप्पणी: ‘उपदिष्टाः’ (पु. बहुवचन) का कर्ता पिछली इकाई से लिया गया है; "
                  "‘सामर्थ्यायोपकल्पते’ का वैकल्पिक अर्थ ‘सामर्थ्य उत्पन्न करने को पर्याप्त नहीं होता’ भी सम्भव है। ‘अल्पबुद्धि’ बहुव्रीहि है।")

AIDS["20"] = {
    "frame": "कारण १: विस्तार की सीमा नहीं · कारण २: अति-संक्षेप अल्पबुद्धि की सामर्थ्य के काम का नहीं · निष्कर्ष (तस्मात्): न अति-संक्षेप, न अति-विस्तार से उपदेश।",
    "seesaw": "अति-विस्तार ↔ अति-संक्षेप: दोनों छोर इसी इकाई में हैं; उपदेश बीच में रखा गया है।",
    "sandhi": "अः + अ → ओऽ: अतिसंक्षेपः + अल्पबुद्धीनाम् → अतिसंक्षेपोऽल्पबुद्धीनाम्। अ + उ → ओ: च + उपदिष्टाः → चोपदिष्टाः। त् → द्: तस्मात् + अनति… → तस्मादनति…।",
    "anchors": "अनतिसंक्षेपेण = अन् + अति + संक्षेप (अति-संक्षेप नहीं) · अल्पबुद्धि = अल्प (थोड़ी) + बुद्धि · प्रमाण = सीमा, माप · तस्मात् = इसलिए।",
    "chunks": "नहि विस्तरस्य प्रमाणमस्ति | न चाप्यतिसंक्षेपोऽल्पबुद्धीनां सामर्थ्यायोपकल्पते | तस्मादनतिसंक्षेपेणानतिविस्तरेण चोपदिष्टाः।",
}
