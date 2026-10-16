from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}

# ---------------------------------------------------------------- unit 100
AUTHORED["100"] = {
    "title": "अविमूत्रं सतिक्तं स्यात्",
    "question": "What does verse 100 say about sheep's urine and goat's urine?",
    "rule": ("Sheep's urine (अविमूत्रम्): slightly bitter, unctuous, not "
             "antagonistic to Pitta. Goat's (आजम्): astringent and sweet, "
             "wholesome, destroys the doṣas. पित्ताविरोधि = पित्त + अविरोधि."),
    "limits": ("Sheep's urine is only said to be not antagonistic to Pitta; "
               "the verse does not say it pacifies Pitta. 'Wholesome' and "
               "'destroys the doṣas' are said of the goat's urine only."),
    "explain_hi": ("मूत्रों की पशु-वार सूची यहाँ से शुरू होती है। पहले भेड़ का "
                   "मूत्र: ‘सतिक्त’ यानी थोड़ा तिक्त, स्निग्ध, और पित्त का "
                   "अविरोधी (पित्त के विपरीत नहीं)। फिर बकरी का (आजम्): "
                   "कषाय और मधुर रस वाला, पथ्य, और दोषों का नाश करने वाला। "
                   "‘पित्ताविरोधि’ में पित्त + अविरोधि का अ + अ → आ हुआ है, और "
                   "‘अ-’ निषेध है: विरोधी नहीं।"),
    "hook": "भेड़: थोड़ा तिक्त, स्निग्ध, पित्त-अविरोधी · बकरी: कषाय-मधुर, पथ्य, दोषनाशक।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 100 starts the list of urines animal by animal. Whose urine does it describe first?",
            ("The sheep's (अवि)", "अविमूत्रं opens the verse: sheep's urine."),
            [("The goat's", "The goat comes second, after the sheep."),
             ("The cow's", "The cow's urine comes in the next verse."),
             ("The horse's", "The horse comes later in the series.")],
            "अविमूत्रम् = अवि (sheep) + मूत्रम् (urine); the goat's follows as आजम्.",
            "Verse 100: first the sheep's urine, then the goat's."),
        match(1, "Match each word of verse 100 to its meaning.",
              [["अविमूत्रम्", "sheep's urine"], ["आजम्", "goat's urine"],
               ["सतिक्तम्", "slightly bitter"],
               ["कषायमधुरम्", "astringent and sweet"]],
              "These four words carry the two animals and their tastes.",
              "अविमूत्रम् = sheep's urine; आजम् = goat's; सतिक्तम् = slightly bitter; कषायमधुरम् = astringent and sweet."),
        fill(2, "The goat's urine is astringent, sweet and ____ (wholesome; type the Devanagari word).",
             ["पथ्यं", "पथ्यम्"],
             "The verse calls the goat's urine पथ्यं, wholesome.",
             "पथ्य means suitable or wholesome; here it is said of the goat's urine, not of the sheep's.",
             "पथ्यम् = wholesome (said of the goat's urine)."),
        mcq("discriminate", 3, "Which is the right split of पित्ताविरोधि?",
            ("पित्त + अविरोधि", "अ + अ gives आ, so पित्त + अविरोधि is written पित्ताविरोधि."),
            [("पित्त + विरोधि", "That would be written पित्तविरोधि and mean the opposite: antagonistic to Pitta."),
             ("पित्ता + विरोधि", "The long आ comes from the join of two अ; पित्ता is not a word here."),
             ("पित्ति + अविरोधि", "The word is पित्त; the final vowel is अ.")],
            "पित्ताविरोधि = पित्त + अविरोधि: not antagonistic to Pitta.",
            "पित्ताविरोधि = पित्त + अविरोधि; the अ- of अविरोधि negates."),
        multi("apply", 4, "Which of these does verse 100 say of the sheep's urine?",
              [("Slightly bitter", "Right: सतिक्तम्."),
               ("Unctuous", "Right: स्निग्धम्."),
               ("Not antagonistic to Pitta", "Right: पित्ताविरोधि."),
               ("Astringent and sweet", "That is the goat's urine, कषायमधुरम्."),
               ("Destroys the doṣas", "That is said of the goat's urine, दोषान्निहन्ति.")],
              [0, 1, 2],
              "The first half of the verse is about the sheep; the second half, from आजम्, is about the goat.",
              "Sheep: सतिक्त, स्निग्ध, पित्ताविरोधि. Goat: कषायमधुर, पथ्य, दोषनाशक."),
        mcq("transfer", 5,
            "A new line calls a food कफाविरोधि. What does it say?",
            ("It does not oppose Kapha", "The अ- in अविरोधि negates, as in पित्ताविरोधि."),
            [("It opposes Kapha", "That would be कफविरोधि, without the negating अ."),
             ("It destroys Kapha", "Not opposing is not the same as destroying."),
             ("It increases Kapha", "The word only says it is not an opponent; it does not say it increases anything.")],
            "कफ + अविरोधि → कफाविरोधि, just as पित्त + अविरोधि → पित्ताविरोधि.",
            "Noun + अविरोधि = not antagonistic to that noun.",
            teaches="The same word-pattern works for any doṣa: noun + अविरोधि means not antagonistic to it."),
    ],
}

# ---------------------------------------------------------------- unit 101
AUTHORED["101"] = {
    "title": "गव्यं समधुरं किंचित्",
    "question": "What does verse 101 say about cow's urine?",
    "rule": ("Cow's urine (गव्यम्): sweet (समधुर; slightly sweet if किंचित् goes with it), destroys the doṣas, "
             "removes worms and kuṣṭha; drunk, relieves itching; beneficial "
             "in udara caused by the doṣas."),
    "limits": ("किंचित् may go with समधुरं ('slightly sweet') or with "
               "दोषघ्नं; सम्यक् may go with पीतं or with हितम्. This card does "
               "not rest any question on those two choices."),
    "explain_hi": ("अब गाय का मूत्र (गव्यम्)। वह मधुर (शायद थोड़ा मधुर) रस वाला और दोषनाशक है; "
                   "‘क्रिमिकुष्ठनुत्’ का अर्थ है कृमि और कुष्ठ को दूर करने "
                   "वाला। पीने पर खुजली (कण्डू) को शान्त करता है, और दोष "
                   "से उत्पन्न उदर रोग में हितकर है। ‘किंचित्’ और ‘सम्यक्’ "
                   "किस शब्द के साथ जुड़ें, इसमें दो पाठ सम्भव हैं (पाठ-टिप्पणी)। "
                   "संधि: किंचित् + दोषघ्नं → किंचिद्दोषघ्नं; सम्यक् + दोषोदरे → "
                   "सम्यग्दोषोदरे।"),
    "hook": "गाय: मधुर, दोषघ्न, कृमि-कुष्ठनाशक; पीने पर खुजली शान्त, दोषज उदर में हित।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 101 begins गव्यं. Whose urine does it describe?",
            ("The cow's", "गव्यम् is the adjective 'of the cow': cow's urine."),
            [("The sheep's", "The sheep's urine was in verse 100."),
             ("The elephant's", "The elephant is named in a later verse."),
             ("The horse's", "The horse is named in a later verse.")],
            "गव्यं = of the cow; the verse describes cow's urine.",
            "गव्यम् = cow's (urine)."),
        match(1, "Match each word of verse 101 to its meaning.",
              [["गव्यम्", "cow's urine"], ["कण्डूम्", "itching"],
               ["पीतम्", "when drunk"], ["क्रिमि", "worms"]],
              "These words carry what the verse says cow's urine does.",
              "गव्यम् = cow's; कण्डूम् = itching; पीतम् = when drunk; क्रिमि = worms."),
        fill(2, "Cow's urine removes worms and ____ (type the Devanagari word for the skin disease named in क्रिमिकुष्ठनुत्).",
             ["कुष्ठ", "कुष्ठम्", "कुष्ठं"],
             "क्रिमिकुष्ठनुत् = removing worms and kuṣṭha.",
             "क्रिमि-कुष्ठ-नुत् is a compound: worms + kuṣṭha + remover.",
             "क्रिमिकुष्ठनुत् = remover of worms and kuṣṭha."),
        mcq("discriminate", 3,
            "Why is it written सम्यग्दोषोदरे and not सम्यक्दोषोदरे?",
            ("A final क् becomes ग् before a voiced sound like द",
             "सम्यक् + दोषोदरे: क् is voiceless, द is voiced, so क् turns into ग्."),
            [("A final क् becomes ख् before द", "ख् is not the voiced partner of क्; that is ग्."),
             ("The क् is dropped before द", "The letter is not dropped; it is changed to ग्."),
             ("It is a misprint for सम्यक्", "It is a regular sandhi change, not a misprint.")],
            "सम्यक् + दोषोदरे → सम्यग्दोषोदरे (क् → ग् before the voiced द). Likewise किंचित् + दोषघ्नं → किंचिद्दोषघ्नं (त् → द्).",
            "Final voiceless stop + voiced sound → voiced stop (क् → ग्, त् → द्)."),
        multi("apply", 4, "Which of these does verse 101 say about cow's urine?",
              [("It relieves itching when drunk", "Right: कण्डूं शमयेत् पीतम्."),
               ("It removes worms and kuṣṭha", "Right: क्रिमिकुष्ठनुत्."),
               ("It is beneficial in udara caused by the doṣas", "Right: दोषोदरे हितम्."),
               ("It removes poison", "The verse does not mention poison."),
               ("It is salty", "The verse calls it sweet, not salty.")],
              [0, 1, 2],
              "The verse gives three effects (itching, worms with kuṣṭha, doṣa-udara) and says it is sweet.",
              "Cow's urine: sweet, doṣa-destroying; removes worms and kuṣṭha; relieves itching; good in doṣa-udara."),
        mcq("transfer", 5,
            "A new text has a disease called कफ + उदरे joined by sandhi. Which is the joined form?",
            ("कफोदरे", "अ + उ gives ओ, as in दोष + उदरे → दोषोदरे."),
            [("कफूदरे", "ऊ comes from उ + उ, not from अ + उ."),
             ("कफौदरे", "औ comes from अ + औ, not from अ + उ."),
             ("कफुदरे", "The final अ of कफ cannot vanish without a trace; the join gives ओ.")],
            "अ + उ → ओ, the same join as दोष + उदरे → दोषोदरे.",
            "Word ending in अ + word beginning with उ → ओ.",
            teaches="You can join any अ-ending word to उदर: -अ + उ → ओ."),
    ],
}

# ---------------------------------------------------------------- unit 102
AUTHORED["102"] = {
    "title": "अर्शःशोफोदरघ्नं तु",
    "question": "What does verse 102 say of buffalo's urine, and where does the elephant's begin?",
    "rule": ("Buffalo's urine (माहिषम्): destroys piles, swelling and udara; "
             "alkaline (सक्षार); laxative (सर). Elephant's (हास्तिकम्): salty "
             "(लवण), beneficial for those with worms and kuṣṭha."),
    "limits": ("The elephant's urine continues in verse 103; this verse gives "
               "only its taste and one use. क्रिमिकुष्ठिनाम् may be read as "
               "krimin + kuṣṭhin or as one compound in -in; the sense is the same."),
    "explain_hi": ("भैंस का मूत्र (माहिषम्): अर्श, शोफ और उदर का नाशक, "
                   "‘सक्षार’ यानी क्षार वाला, और ‘सर’ यानी मल को सरकाने वाला। "
                   "फिर हाथी का मूत्र (हास्तिकम्): लवण रस वाला, और कृमि तथा "
                   "कुष्ठ के रोगियों के लिए हितकर। हाथी का वर्णन अगले श्लोक की "
                   "पहली पंक्ति में चलता है। पशु का नाम वृद्धि वाले रूप में है: "
                   "महिष → माहिष, हस्ति → हास्तिक, अज → आज: ‘उस पशु का’।"),
    "hook": "भैंस: अर्श-शोफ-उदरनाशक, क्षार, सर · हाथी: लवण, कृमि-कुष्ठ में हित (आगे श्लोक १०३)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 102, which two animals' urines are described?",
            ("The buffalo's and the elephant's", "माहिषम् and हास्तिकम् name them."),
            [("The sheep's and the goat's", "Those were in verse 100."),
             ("The cow's and the buffalo's", "The cow's was in verse 101; the elephant, not the cow, pairs with the buffalo here."),
             ("The camel's and the horse's", "The camel and horse come in later verses.")],
            "माहिषम् = of the buffalo; हास्तिकम् = of the elephant.",
            "Verse 102: buffalo, then elephant."),
        match(1, "Match each word of verse 102 to its meaning.",
              [["माहिषम्", "buffalo's"], ["हास्तिकम्", "elephant's"],
               ["सक्षारम्", "alkaline"], ["लवणम्", "salty"]],
              "Two animals and two tastes.",
              "माहिषम् = buffalo's; हास्तिकम् = elephant's; सक्षारम् = alkaline; लवणम् = salty."),
        fill(2, "The elephant's urine is said to be ____ (type the Devanagari word for 'salty').",
             ["लवणं", "लवणम्"],
             "The verse says हास्तिकं लवणं मूत्रम्.",
             "लवण is the salty taste; it is the elephant's urine that is called so here.",
             "लवणम् = salty, said of the elephant's urine."),
        mcq("discriminate", 3,
            "Which word in the second line of verse 102 names the animal whose urine is now described?",
            ("हास्तिकम्", "It means 'of the elephant' and starts the new description."),
            [("लवणम्", "It names a taste, not an animal."),
             ("हितम्", "It means 'beneficial', not an animal."),
             ("क्रिमिकुष्ठिनाम्", "It names the patients, not an animal.")],
            "The animal is named by हास्तिकम्; the other words tell its taste, use and patients.",
            "हास्तिकम् names the elephant; माहिषम् names the buffalo."),
        multi("apply", 4, "Which of these does verse 102 say of the buffalo's urine?",
              [("It destroys piles, swelling and udara", "Right: अर्शःशोफोदरघ्नम्."),
               ("It is alkaline", "Right: सक्षारम्."),
               ("It is laxative", "Right: सरम्."),
               ("It is salty", "Salty is said of the elephant's urine."),
               ("It is beneficial for those with worms and kuṣṭha", "That is said of the elephant's urine.")],
              [0, 1, 2],
              "The first line and a half is about the buffalo; from हास्तिकम् on, about the elephant.",
              "Buffalo: destroys piles, swelling, udara; alkaline; laxative."),
        mcq("transfer", 5,
            "A new line begins सैंहं मूत्रं. Following the pattern of माहिषं and आजं, whose urine is it?",
            ("The lion's (सिंह)", "The pattern: the animal's name with its first vowel strengthened (vṛddhi), as सिंह → सैंह."),
            [("Of lion cubs", "Nothing in the word marks cubs."),
             ("The horse's", "The horse is named by वाजि- in verse 104."),
             ("A king's", "The pattern names animals, not people.")],
            "महिष → माहिष, अज → आज, हस्तिन् → हास्तिक: 'of that animal'. So सिंह → सैंह means 'of the lion'.",
            "Animal name with first vowel strengthened = 'of that animal'.",
            teaches="Adjectives like माहिष, आज, हास्तिक are 'of the animal'; the pattern lets you guess the animal behind a new word."),
    ],
}

# ---------------------------------------------------------------- unit 103
AUTHORED["103"] = {
    "title": "प्रशस्तं बद्धविण्मूत्र",
    "question": "What does verse 103 add, and what does it say of the camel's urine?",
    "rule": ("103a (commended in retention of faeces and urine, poison, "
             "Kapha diseases and piles) is read as continuing the elephant's "
             "urine. Camel's (औष्ट्रम्): slightly bitter; destroys dyspnoea, cough and piles."),
    "limits": ("103a could grammatically open the camel's description; this "
               "card follows the edition's note and the translations in "
               "reading it with the elephant. No question here depends on "
               "that choice. श्लेष्मामय may also be 'Kapha and āma' (less likely)."),
    "explain_hi": ("यह श्लोक पिछले वाक्य का शेष है: पहली पंक्ति ‘प्रशस्तम्’ "
                   "(सराहनीय) में बँधे मल-मूत्र, विष, कफज रोगों और अर्श का नाम "
                   "है, और पाठ-टिप्पणी के अनुसार इसे हाथी के मूत्र से जोड़ा गया है। फिर ऊँट का "
                   "मूत्र (औष्ट्रम्): थोड़ा तिक्त, श्वास और कास का नाशक, और "
                   "अर्श का नाशक। संधि: च + औष्ट्रम् → चौष्ट्रम् (अ + औ → औ), और "
                   "अर्शः + घ्नम् → अर्शोघ्नम् (विसर्ग → ओ, घोष ‘घ’ से पहले)।"),
    "hook": "(हाथी, आगे) बँधा मल-मूत्र, विष, कफ-रोग, अर्श में प्रशस्त · ऊँट: थोड़ा तिक्त, श्वास-कास-अर्श नाशक।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which of these animals is named in verse 103?",
            ("The camel", "चौष्ट्रम् = च + औष्ट्रम्, 'of the camel'."),
            [("The horse", "The horse is named in verse 104."),
             ("The cow", "The cow was in verse 101."),
             ("The sheep", "The sheep was in verse 100.")],
            "औष्ट्रम् (inside चौष्ट्रम्) is the adjective 'of the camel'.",
            "Verse 103 names the camel (औष्ट्रम्)."),
        match(1, "Match each word of verse 103 to its meaning.",
              [["श्वास", "dyspnoea"], ["कास", "cough"], ["अर्श", "piles"],
               ["विष", "poison"]],
              "These four disease and harm words appear in the verse.",
              "श्वास = dyspnoea; कास = cough; अर्श = piles; विष = poison."),
        fill(2, "The camel's urine destroys श्वास, कास and ____ (type the Devanagari word for piles, as in अर्शोघ्नम्).",
             ["अर्श", "अर्शः", "अर्शस्", "अर्शम्", "अर्शं"],
             "The verse says श्वासकासघ्नमर्शोघ्नम्: it destroys dyspnoea, cough and piles.",
             "अर्शोघ्नम् is अर्शः + घ्नम्: destroyer of piles.",
             "अर्शोघ्नम् = destroying piles."),
        mcq("discriminate", 3, "Which is the right split of चौष्ट्रम्?",
            ("च + औष्ट्रम्", "अ + औ gives औ, so च + औष्ट्रम् is written चौष्ट्रम्."),
            [("च + उष्ट्रम्", "अ + उ would give चोष्ट्रम्, with ओ, not औ."),
             ("चौ + ष्ट्रम्", "ष्ट्रम् is not a word."),
             ("चो + औष्ट्रम्", "No ओ stands at the end of the first word.")],
            "चौष्ट्रम् = च ('and') + औष्ट्रम् ('camel's').",
            "च + औष्ट्रम् → चौष्ट्रम् (अ + औ → औ)."),
        mcq("apply", 4,
            "A patient has cough and breathlessness. Which urine does verse 103 name for it?",
            ("The camel's", "श्वासकासघ्नम् औष्ट्रम्: it destroys dyspnoea and cough."),
            [("The goat's", "The goat's urine (verse 100) is called wholesome, with no mention of cough."),
             ("The cow's", "Verse 101 names itching, worms, kuṣṭha and udara."),
             ("The buffalo's", "Verse 102 names piles, swelling and udara.")],
            "In verse 103 only the camel's urine is said to destroy dyspnoea and cough.",
            "Camel's urine: श्वास and कास nāśaka."),
        mcq("transfer", 5,
            "A new text joins यथा + औषधम्. Which is the written form?",
            ("यथौषधम्", "आ + औ gives औ, as अ + औ does in च + औष्ट्रम्."),
            [("यथाषधम्", "That drops the औ; the join keeps an औ."),
             ("यथोषधम्", "ओ would come from आ + उ or आ + ओ, not from आ + औ."),
             ("यथैषधम्", "ऐ would come from आ + ए or आ + ऐ.")],
            "अ/आ + औ → औ.",
            "अ/आ at the end of a word + औ at the start of the next → औ.",
            teaches="The च + औष्ट्रम् join is one case of a general rule: अ/आ + औ → औ."),
    ],
}

# ---------------------------------------------------------------- unit 104
AUTHORED["104"] = {
    "title": "वाजिनां तिक्तकटुकं",
    "question": "What does verse 104 say of horses' urine and donkey's urine?",
    "rule": ("Horses' (वाजिनाम्, urine understood): bitter and pungent; "
             "removes kuṣṭha, wounds, poison. Donkey's (खरमूत्रम्): "
             "destroys epilepsy, insanity and graha."),
    "limits": ("'Urine' is not written with वाजिनाम्; it is understood "
               "from the context. ग्रह means seizure by malevolent beings, "
               "or a class of disorders, according to commentators."),
    "explain_hi": ("घोड़ों का (मूत्र; शब्द ‘मूत्रम्’ पीछे से जोड़ा जाता है): तिक्त "
                   "और कटु, तथा कुष्ठ, व्रण (घाव) और विष को दूर करने वाला। "
                   "गधे का मूत्र: अपस्मार (मृगी), उन्माद और ग्रह (बाधा) का "
                   "नाशक। ‘अपह’ और ‘विनाशन’ दोनों का अर्थ ‘दूर/नष्ट करने वाला’ है। "
                   "संधि: विष + अपहम् → विषापहम् (अ + अ → आ)।"),
    "hook": "घोड़ा: तिक्त-कटु, कुष्ठ-व्रण-विष हर · गधा: अपस्मार-उन्माद-ग्रह नाशक।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which two animals does verse 104 name?",
            ("The horse and the donkey", "वाजिनाम् = of horses; खरमूत्रम् = donkey's urine."),
            [("The camel and the elephant", "Those were in verses 102-103."),
             ("The sheep and the goat", "Those were in verse 100."),
             ("The cow and the buffalo", "Those were in verses 101-102.")],
            "The verse names horses (वाजिनाम्) and the donkey (खर-).",
            "Verse 104: horses, donkey."),
        match(1, "Match each word of verse 104 to its meaning.",
              [["तिक्तकटुकम्", "bitter and pungent"], ["व्रण", "wound"],
               ["अपस्मार", "epilepsy"], ["उन्माद", "insanity"]],
              "Taste and conditions named in the verse.",
              "तिक्तकटुकम् = bitter and pungent; व्रण = wound; अपस्मार = epilepsy; उन्माद = insanity."),
        fill(2, "Horses' urine removes kuṣṭha, ____ (type the Devanagari word for 'wound') and poison.",
             ["व्रण", "व्रणः", "व्रणम्", "व्रणं"],
             "कुष्ठव्रणविषापहम् = removing kuṣṭha, wounds and poison.",
             "The compound lists three things the horses' urine removes; the middle one is व्रण.",
             "कुष्ठ-व्रण-विष-अपहम् = remover of kuṣṭha, wounds, poison."),
        mcq("discriminate", 3,
            "वाजिनां has no noun with it. Which word is understood, as the edition notes?",
            ("मूत्रम् (urine)", "The verses are about urines; the next half names खरमूत्रम् in the same pattern."),
            [("क्षीरम् (milk)", "Milks are announced for later, in verse 105."),
             ("रोगः (disease)", "The verse says what the substance does, not what disease is."),
             ("वृक्षः (tree)", "No tree is under discussion.")],
            "वाजिनाम् means 'of horses'; the word 'urine' is supplied from the context.",
            "वाजिनाम् (मूत्रम्) = horses' urine."),
        multi("apply", 4, "Which of these does verse 104 say of the donkey's urine?",
              [("It destroys epilepsy", "Right: अपस्मार."),
               ("It destroys insanity", "Right: उन्माद."),
               ("It destroys graha (possession)", "Right: ग्रह."),
               ("It removes kuṣṭha", "That is said of horses' urine."),
               ("It removes wounds", "That is said of horses' urine.")],
              [0, 1, 2],
              "The first line is horses; the second line is the donkey.",
              "Donkey: epilepsy, insanity, graha. Horses: bitter-pungent; kuṣṭha, wounds, poison."),
        mcq("transfer", 5,
            "A new line calls a drink ज्वरापहम्. Following विषापहम्, what does it say?",
            ("It removes fever", "-अपह is 'removing', as in विषापहम्."),
            [("It causes fever", "-अपह means removing, not causing."),
             ("It is made from fever", "The first part names what is removed."),
             ("It is a drink for fever and cough together", "The word names only fever, and as a remover.")],
            "ज्वर + अपहम् → ज्वरापहम्, as विष + अपहम् → विषापहम्: remover of fever.",
            "Noun + अपह / विनाशन / घ्न = remover of that noun.",
            teaches="Words ending in अपह, विनाशन, घ्न mean 'removing'; the first part names what is removed."),
    ],
}

# ---------------------------------------------------------------- unit 105
AUTHORED["105"] = {
    "title": "इतीहोक्तानि मूत्राणि",
    "question": "How does verse 105 close the urines and open the next topic?",
    "rule": ("The urines have been described here (इति) according to potency "
             "and use. Next (अतः) the milks will be described, with their "
             "action (कर्म) and qualities (गुणाः)."),
    "limits": ("यथासामर्थ्ययोगतः may also be read 'as far as their potency "
               "allows them to be used' or 'by power and combination'. "
               "The verse says what follows, not how many milks."),
    "explain_hi": ("यह संक्रमण-श्लोक है: ‘इति’ से मूत्रों का वर्णन पूरा होता है "
                   "(यथासामर्थ्य-योगतः: सामर्थ्य और प्रयोग के अनुसार), और "
                   "‘अतः’ से दूधों (क्षीराणि) का वर्णन आरम्भ होने की घोषणा है। "
                   "दूधों के कर्म और गुण दोनों कहे जाएँगे। ‘वक्ष्यन्ते’ भविष्यत्-"
                   "काल में है, कर्मवाच्य के अर्थ में। संधि: इति + इह + उक्तानि → "
                   "इतीहोक्तानि (इ + इ → ई; अ + उ → ओ), च + एषाम् → चैषाम् "
                   "(अ + ए → ऐ)।"),
    "hook": "इति = मूत्र समाप्त · अतः = अब क्षीर; कर्म और गुण दोनों कहे जाएँगे।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 105 says urines have been described and something else will follow. What follows?",
            ("The milks (क्षीराणि)", "अतः क्षीराणि वक्ष्यन्ते: next the milks will be described."),
            [("The salts", "The verse names milks, not salts."),
             ("The fruits", "The verse names milks, not fruits."),
             ("The diseases", "The verse names milks, not diseases.")],
            "क्षीराणि वक्ष्यन्ते = the milks will be described.",
            "After the urines come the milks."),
        match(1, "Match each word of verse 105 to its meaning.",
              [["मूत्राणि", "urines"], ["क्षीराणि", "milks"],
               ["कर्म", "action"], ["गुणाः", "qualities"]],
              "Two topics and the two things said about the new topic.",
              "मूत्राणि = urines; क्षीराणि = milks; कर्म = action; गुणाः = qualities."),
        fill(2, "अतः ____ वक्ष्यन्ते: the topic announced as coming next (type the Devanagari word for 'milks').",
             ["क्षीराणि", "क्षीर", "क्षीरम्"],
             "The verse announces क्षीराणि, the milks.",
             "क्षीराणि is the plural of क्षीर: the milks of the different animals will be described in turn.",
             "क्षीराणि = milks."),
        mcq("discriminate", 3, "Which is the right split of इतीहोक्तानि?",
            ("इति + इह + उक्तानि", "इ + इ gives ई and अ + उ gives ओ: इतीहोक्तानि."),
            [("इति + हो + उक्तानि", "There is no word हो here."),
             ("इती + होक्तानि", "होक्तानि is not a word."),
             ("इत + ईहोक्तानि", "इत and ईहोक्तानि are not words here.")],
            "इतीहोक्तानि = इति ('thus') + इह ('here') + उक्तानि ('described').",
            "इति + इह + उक्तानि → इतीहोक्तानि."),
        mcq("apply", 4,
            "Which words of verse 105 show that it shifts from the urines to a new topic?",
            ("इति for the urines, and अतः for the milks", "इति closes what was said; अतः begins the next topic."),
            [("अथ and अतः together", "अथ does not occur in this verse."),
             ("ये and च", "These are small linking words; they do not mark the shift."),
             ("कर्म and गुणाः", "They say what will be told of the milks, not that the topic changes.")],
            "इति marks the end of the urines; अतः (hereafter) opens the milks.",
            "इति = closing; अतः = on to the next topic."),
        mcq("transfer", 5,
            "A new text joins रस + एषाम् (meaning: of these tastes). Which written form follows the rule of च + एषाम् → चैषाम्?",
            ("रसैषाम्", "अ + ए gives ऐ."),
            [("रसेषाम्", "That is the result of अ + इ, not of अ + ए."),
             ("रसोषाम्", "ओ is the result of अ + उ."),
             ("रसाषाम्", "आ is the result of अ + अ.")],
            "अ + ए → ऐ, the same as in च + एषाम् → चैषाम्.",
            "Word ending in अ + एषाम् → ऐ-joined form.",
            teaches="You can apply the join अ + ए → ऐ to any new word."),
    ],
}

# ---------------------------------------------------------------- unit 106
AUTHORED["106"] = {
    "title": "अविक्षीरमजाक्षीरं",
    "question": "Which milks does verse 106 list, and in what order?",
    "rule": ("Sheep's, goat's, cow's and buffalo's milk (line 1); then that "
             "of she-camels, she-elephants, the mare, and likewise of "
             "woman (line 2)."),
    "limits": ("The verse only names the milks; it says nothing yet of "
               "their qualities, which come in the next verses. The edition "
               "notes that this list parallels the earlier urines, but "
               "the verse itself does not say so."),
    "explain_hi": ("दूधों की सूची: पहली पंक्ति में भेड़, बकरी, गाय और भैंस का "
                   "दूध; दूसरी में ऊँटनियों, हथिनियों, घोड़ी और स्त्री का। "
                   "पहले चार नाम ‘पशु + क्षीरम्’ वाले समास हैं (अविक्षीरम्, "
                   "अजाक्षीरम्, गोक्षीरम्) या विशेषण (माहिषम्); बाद के चार षष्ठी "
                   "में हैं (उष्ट्रीणाम्, नागीनाम्, वडवायाः, स्त्रियाः), यानी "
                   "‘किसका (दूध)’। संधि: स्त्रियाः + तथा → स्त्रियास्तथा।"),
    "hook": "भेड़ · बकरी · गाय · भैंस | ऊँटनी · हथिनी · घोड़ी · स्त्री।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 106 is a list. What is being listed?",
            ("Milks of different females", "अविक्षीरम्, अजाक्षीरम्, गोक्षीरम् and the genitives that follow name milks."),
            [("Urines of different animals", "Urines ended in verse 105; this list is of क्षीर."),
             ("Diseases and their cures", "No disease is named in this verse."),
             ("Names of sages", "The names here are of animals and woman, not sages.")],
            "After verse 105 announced the milks, this verse names them.",
            "Verse 106 lists milks."),
        order(1, "Put these milks in the order of verse 106.",
              ["अविक्षीरम्", "अजाक्षीरम्", "गोक्षीरम्", "माहिषम्"],
              "The first line runs sheep, goat, cow, buffalo.",
              "अविक्षीर → अजाक्षीर → गोक्षीर → माहिष."),
        fill(2, "The last milk in the list is that of ____ (type the Devanagari word for 'of woman').",
             ["स्त्रियाः", "स्त्रिया", "स्त्री", "स्त्रियास्"],
             "Line 2 ends with स्त्रियास्तथा, i.e. स्त्रियाः + तथा: 'of woman, likewise'.",
             "स्त्रियाः is the genitive singular of स्त्री (woman).",
             "स्त्रियाः = of woman."),
        mcq("discriminate", 3, "Which of these milks is NOT named in verse 106?",
            ("The donkey's", "Verse 106 does not name the donkey."),
            [("The mare's", "Named: वडवायाः."),
             ("The she-elephants'", "Named: नागीनाम्."),
             ("The woman's", "Named: स्त्रियाः.")],
            "The mare, she-elephants and woman are in the list; the donkey is not.",
            "Milks named: sheep, goat, cow, buffalo, she-camels, she-elephants, mare, woman."),
        mcq("apply", 4, "Which is the right split of स्त्रियास्तथा?",
            ("स्त्रियाः + तथा", "A visarga before त becomes स्: स्त्रियाः + तथा → स्त्रियास्तथा."),
            [("स्त्रिया + स्तथा", "स्तथा is not a word."),
             ("स्त्री + आस्तथा", "आस्तथा is not a word."),
             ("स्त्रियास् + तथा", "The ending is a visarga that became स् by the join, not a stand-alone स्.")],
            "स्त्रियास्तथा = स्त्रियाः ('of woman') + तथा ('likewise').",
            "Visarga + त → स् + त."),
        mcq("transfer", 5,
            "A new line reads सिंहीनां क्षीरम् (सिंही = lioness), like उष्ट्रीणाम् and नागीनाम्. Whose milk is it?",
            ("Of lionesses (several females)", "A feminine noun in -ई plus -नाम् is a genitive plural, as in उष्ट्रीणाम्: 'of she-camels'."),
            [("Of one lion", "The ending is feminine plural, not male singular."),
             ("Of one lioness", "The -नाम् ending is plural, not singular."),
             ("Of lion cubs", "Nothing in the ending marks young ones.")],
            "उष्ट्रीणाम् = of she-camels, नागीनाम् = of she-elephants: feminine plural 'of the females'.",
            "Feminine -ई noun + नाम् / णाम् = 'of the females' (plural).",
            teaches="A feminine noun in -ई plus -नाम् (-णाम् after र/ष) is a genitive plural: सिंही (lioness) → सिंहीनाम् 'of lionesses'."),
    ],
}

# ---------------------------------------------------------------- unit 107
AUTHORED["107"] = {
    "title": "प्रायशो मधुरं स्निग्धं",
    "question": "What general qualities does verse 107 give milk?",
    "rule": ("Milk is generally (प्रायशः) sweet, unctuous, cold and stanya; "
             "it is nourishing (प्रीणन), bulk-building (बृंहण), aphrodisiac "
             "(वृष्य), good for the intellect (मेध्य), strengthening (बल्य) "
             "and invigorating the mind (मनस्कर)."),
    "limits": ("स्तन्य is taken here as promoting breast-milk; it could also "
               "be read 'like breast-milk' or 'breast-milk'. प्रायशः says "
               "'generally' and hedges the four qualities (sweet, unctuous, cold, stanya). "
               "The sentence continues in verse 108."),
    "explain_hi": ("अब सभी दूधों के सामान्य गुण। ‘प्रायशः’ का अर्थ है ‘प्रायः, "
                   "अधिकतर’: यानी यह चार गुणों (मधुर, स्निग्ध, शीत, स्तन्य) के साथ है; "
                   "आगे के कर्म इसके दायरे में स्पष्ट नहीं गिने गए। दूध मधुर, स्निग्ध, शीत और स्तन्य माना गया है। "
                   "फिर कर्म गिनाए जाते हैं: प्रीणन (तृप्ति), बृंहण (पुष्टि), "
                   "वृष्य, मेध्य (बुद्धि के लिए), बल्य (बल देने वाला) और "
                   "मनस्कर (मन को बल देने वाला)। वाक्य श्लोक १०८ में चलता है। "
                   "संधि: प्रायशः + मधुरं → प्रायशो मधुरं; पयः + मतम् → पयो मतम्।"),
    "hook": "प्रायः मधुर-स्निग्ध-शीत-स्तन्य; प्रीणन, बृंहण, वृष्य, मेध्य, बल्य, मनस्कर।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 107 says milk is प्रायशः sweet. What does प्रायशः tell you?",
            ("Generally, not always", "प्रायशः means 'generally' or 'mostly'."),
            [("Always without exception", "That would need a word like सर्वदा; प्रायशः is weaker."),
             ("Never", "The verse gives sweetness as a general quality of milk."),
             ("Only for cow's milk", "The verse speaks of milk in general (पयः).")],
            "प्रायशः hedges the list: milk is generally so described.",
            "प्रायशः = generally."),
        match(1, "Match each word of verse 107 to its meaning.",
              [["मधुरम्", "sweet"], ["स्निग्धम्", "unctuous"],
               ["शीतम्", "cold"], ["बल्यम्", "strengthening"]],
              "Taste, texture, temperature and one action word of the verse.",
              "मधुरम् = sweet; स्निग्धम् = unctuous; शीतम् = cold; बल्यम् = strengthening."),
        fill(2, "Milk is generally sweet, unctuous and ____ (type the Devanagari word for 'cold').",
             ["शीतं", "शीतम्"],
             "The verse says मधुरं स्निग्धं शीतम्.",
             "शीत is cold; it is the third of the general qualities named at the start.",
             "शीतम् = cold."),
        mcq("discriminate", 3, "Which is the right split of प्रायशो मधुरं?",
            ("प्रायशः + मधुरं", "A visarga before a voiced sound like म becomes ो after अ: प्रायशः + मधुरं → प्रायशो मधुरं."),
            [("प्रायश + उ मधुरं", "There is no word उ here."),
             ("प्रायशा + मधुरं", "No such word; the visarga after अ becomes ो, not आ."),
             ("प्रायश + मधुरं", "That would be written प्रायशमधुरं, with no ो.")],
            "प्रायशो मधुरं = प्रायशः ('generally') + मधुरं ('sweet').",
            "अः + voiced sound → ो."),
        mcq("apply", 4,
            "A student wants one word from verse 107 for 'good for the intellect'. Which is it?",
            ("मेध्यम्", "मेध्य = promoting intellect."),
            [("वृष्यम्", "वृष्य is 'aphrodisiac'."),
             ("बल्यम्", "बल्य is 'strengthening'."),
             ("बृंहणम्", "बृंहण is 'building bulk'.")],
            "मेध्यम् names the intellect-promoting action.",
            "मेध्य = good for the intellect."),
        mcq("transfer", 5,
            "A new text says the fruits of a tree are प्रायशः sweet. Is a sour fruit from it a contradiction?",
            ("No, because प्रायशः means generally", "A general statement allows exceptions."),
            [("Yes, because it says all are sweet", "प्रायशः does not say all."),
             ("Yes, because sweet and sour cannot share a tree", "The text only says generally."),
             ("It cannot be judged", "The word प्रायशः settles it: the statement is general.")],
            "प्रायशः marks a general statement, as in प्रायशो मधुरम्.",
            "प्रायशः = generally, so exceptions are not contradictions.",
            teaches="When a text uses प्रायशः, read its list as the usual case, not a rule without exceptions."),
    ],
}

# ---------------------------------------------------------------- unit 108
AUTHORED["108"] = {
    "title": "जीवनीयं श्रमहरं",
    "question": "What further effects of milk does verse 108 list?",
    "rule": ("Continuing verse 107, milk is vitalizing (जीवनीय), removes "
             "fatigue, destroys dyspnoea and cough, destroys śoṇitapitta "
             "(bleeding disorder), and heals (unites) what is injured."),
    "limits": ("The verse names no subject; milk is understood from verse "
               "107. सन्धानं विहतस्य may mean joining what is injured or "
               "broken. शोणितपित्त is the bleeding disorder, also called रक्तपित्त."),
    "explain_hi": ("यह श्लोक १०७ का वाक्य आगे बढ़ाता है; इसमें दूध का नाम नहीं "
                   "आता, वह पिछले श्लोक से समझ लिया जाता है। दूध जीवनीय है, "
                   "श्रम (थकान) हरता है, श्वास और कास का नाश करता है, "
                   "शोणितपित्त (रक्तस्राव का रोग) को नष्ट करता है और चोट खाए (विहत) "
                   "को जोड़ने वाला है। संधि: सम् + धानम् → सन्धानम् (म् दन्त्य ‘ध’ के साथ "
                   "दन्त्य न् लिखा गया)।"),
    "hook": "जीवनीय · थकान हर · श्वास-कास नाश · शोणितपित्त नाश · चोट को जोड़े।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 108 has no word for milk. Where does its subject come from?",
            ("From verse 107, which it continues", "The sentence runs on: milk is understood."),
            [("From verse 106's list of animals", "That list names the milks, but the sentence being continued is verse 107."),
             ("It is the reader's choice", "The grammar continues verse 107; the subject is fixed."),
             ("From the next verse, 109", "A subject is understood from what came before, here verse 107.")],
            "Verses 107-109 form one sentence about milk.",
            "Verse 108 continues the description of milk from verse 107."),
        match(1, "Match each word of verse 108 to its meaning.",
              [["जीवनीयम्", "vitalizing"], ["श्रमहरम्", "removing fatigue"],
               ["शोणितपित्तम्", "bleeding disorder"],
               ["सन्धानम्", "uniting, healing"]],
              "Four of the effects named in the verse.",
              "जीवनीयम् = vitalizing; श्रमहरम् = removing fatigue; शोणितपित्तम् = bleeding disorder; सन्धानम् = uniting."),
        fill(2, "The verse says milk destroys श्वास and ____ (type the Devanagari word for 'cough').",
             ["कास", "कासः", "कासम्", "कासं"],
             "श्वासकासनिबर्हणम् = destroying dyspnoea and cough.",
             "निबर्हण means destroying; the two things destroyed are श्वास and कास.",
             "श्वासकासनिबर्हणम् = destroyer of dyspnoea and cough."),
        mcq("discriminate", 3,
            "सम् + धानम् is written सन्धानम्. Which change happened?",
            ("म् became न् before the dental ध", "A nasal before a dental stop takes the dental nasal न्."),
            [("म् became ण् before ध", "ण् is the nasal of the retroflex group, not the dental ध."),
             ("म् became ङ् before ध", "ङ् is the nasal of the velar group."),
             ("म् stayed the same", "It changed to न्.")],
            "सम् + धानम् → सन्धानम्: म् → न् before ध.",
            "म् before a dental stop → न्."),
        multi("apply", 4, "A person has fatigue and cough. Which words of verse 108 apply?",
              [("श्रमहरम्", "Right: removes fatigue."),
               ("श्वासकासनिबर्हणम्", "Right: destroys dyspnoea and cough."),
               ("सन्धानं विहतस्य", "This is about healing an injury."),
               ("शीतम्", "शीत belongs to verse 107, not to this verse.")],
              [0, 1],
              "Fatigue is covered by श्रमहरम्; cough by श्वासकासनिबर्हणम्.",
              "श्रमहर → fatigue; श्वासकासनिबर्हण → dyspnoea and cough."),
        mcq("transfer", 5,
            "A new line calls a drink तापहरं. Following श्रमहरं, what does it say?",
            ("It removes heat", "-हर is 'removing', as in श्रमहरम्."),
            [("It causes heat", "-हर means taking away, not causing."),
             ("It is made of heat", "The first part names what is removed."),
             ("It is hot", "The word says the drink removes heat.")],
            "श्रम + हरम् = remover of fatigue; ताप + हरम् = remover of heat.",
            "Noun + हर = remover of that noun.",
            teaches="-हर, like -घ्न and -अपह, makes a 'remover' word: the first part is what is removed."),
    ],
}

# ---------------------------------------------------------------- unit 109
AUTHORED["109"] = {
    "title": "सर्वप्राणभृतां सात्म्यं",
    "question": "What does verse 109 add to the description of milk?",
    "rule": ("Milk is congenial (सात्म्य) to all living beings, both "
             "pacifying (शमन) and purifying (शोधन), removes thirst, "
             "stimulates digestion, and is best for the wasted and injured."),
    "limits": ("The printed text has ‘सर्वप्राणाभृतां’; the usual compound is "
               "प्राणभृत् ('living being'), and the edition marks the long आ "
               "as a possible slip. क्षीणक्षत may be read as one condition "
               "('wasting due to chest injury'). The sentence ends here."),
    "explain_hi": ("वाक्य का अन्तिम भाग। दूध सब प्राणियों के लिए सात्म्य "
                   "(आदत से अनुकूल) कहा गया है; शमन और शोधन दोनों करता है "
                   "(दो प्रकार की चिकित्सा: शान्त करना और बाहर निकालना); "
                   "प्यास मिटाता है, दीपनीय है, और क्षीण तथा क्षत में श्रेष्ठ है। "
                   "‘क्षीणक्षत’ को दो दशाओं के रूप में (क्षीण और क्षत) या एक "
                   "दशा के रूप में पढ़ा जा सकता है। प्राणभृत् के प्राण में पाठ "
                   "में आकार दिखता है, जो सम्भवतः लिपि-चूक है।"),
    "hook": "सब प्राणियों को सात्म्य · शमन और शोधन · प्यास हर, दीपनीय · क्षीण-क्षत में श्रेष्ठ।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 109 calls milk सात्म्य. Whom does it say milk is congenial to?",
            ("All living beings", "सर्वप्राणभृताम् = of all living beings."),
            [("Only the sick", "The verse says all living beings."),
             ("Only children", "The verse does not limit it to children."),
             ("Only humans", "प्राणभृत् includes all breathing beings, not only humans.")],
            "सात्म्यं सर्वप्राणभृताम्: congenial to all living beings.",
            "Milk is सात्म्य to all living beings."),
        match(1, "Match each word of verse 109 to its meaning.",
              [["शमनम्", "pacifying"], ["शोधनम्", "purifying"],
               ["तृष्णाघ्नम्", "removing thirst"],
               ["दीपनीयम्", "stimulating digestion"]],
              "Four effects named in the verse.",
              "शमनम् = pacifying; शोधनम् = purifying; तृष्णाघ्नम् = removing thirst; दीपनीयम् = stimulating digestion."),
        fill(2, "तृष्णाघ्नम् means removing ____ (type the Devanagari word for 'thirst').",
             ["तृष्णा", "तृष्णाम्", "तृष्णां", "तृषा"],
             "तृष्णाघ्नम् = तृष्णा + घ्नम्: destroyer of thirst.",
             "घ्न is the 'destroying' ending, as in दोषघ्नम् and अर्शोघ्नम् earlier; the first part, तृष्णा, is what is destroyed.",
             "तृष्णाघ्नम् = removing thirst."),
        mcq("discriminate", 3,
            "Verse 109 says milk is both शमनं and शोधनं. How does the edition's note take them?",
            ("Two kinds of therapy: pacifying and purifying",
             "शमन is palliative (calming), शोधन is evacuative (cleansing out), per the note."),
            [("Two kinds of milk", "They are actions of milk, not kinds of milk."),
             ("Two diseases", "They describe what milk does, not what it treats."),
             ("Two animals", "No animals are named in this verse.")],
            "शमनम् and शोधनम् are the two actions: pacifying and purifying.",
            "शमन = pacify, शोधन = purify."),
        multi("apply", 4, "Which of these does verse 109 say of milk?",
              [("It is congenial to all living beings", "Right: सात्म्यं सर्वप्राणभृताम्."),
               ("It removes thirst", "Right: तृष्णाघ्नम्."),
               ("It stimulates digestion", "Right: दीपनीयम्."),
               ("It increases thirst", "The verse says तृष्णाघ्न: it removes thirst."),
               ("It is harmful for the wasted", "The verse calls it best (श्रेष्ठम्) for the wasted and injured.")],
              [0, 1, 2],
              "The verse gives positive effects only.",
              "Milk: सात्म्य, शमन and शोधन, तृष्णाघ्न, दीपनीय, श्रेष्ठ in क्षीण and क्षत."),
        mcq("transfer", 5,
            "A new text calls a decoction कासघ्नं ज्वरघ्नं च. What does it claim?",
            ("It removes cough and fever", "-घ्न means destroying, as in तृष्णाघ्नम्."),
            [("It causes cough and fever", "-घ्न means destroying, not causing."),
             ("It is made from cough and fever", "The first part names what is destroyed."),
             ("It is a food for the weak", "Nothing in the words says this.")],
            "कास + घ्नम् and ज्वर + घ्नम् are destroyers of cough and fever, like तृष्णा + घ्नम्.",
            "Noun + घ्न = destroying that noun.",
            teaches="-घ्न makes a 'destroyer of X' word; you can read any new word that ends in it."),
    ],
}

NOTES_HI = {
    "100": "‘पित्ताविरोधि’ = पित्त + अविरोधि (अ + अ → आ; ‘अ-’ निषेध)। ‘सतिक्तम्’ में ‘स-’ का भाव ‘थोड़ा’ है (पाठ-टिप्पणी: सतिक्त = तिक्तता सहित)। ‘दोषान्निहन्ति’ में ‘दोषान्’ + ‘निहन्ति’ बिना परिवर्तन के सटे हैं। इस श्लोक के पाठ में कोई पाठभेद नहीं दिया गया।",
    "101": "विश्वास: मध्यम। ‘किंचित्’ ‘समधुरं’ के साथ (थोड़ा मधुर) भी जुड़ सकता है और ‘दोषघ्नं’ के साथ (थोड़ा दोषनाशक) भी; शब्द-क्रम बाद वाले की ओर, भाव और समानान्तर (सतिक्तं) पहले की ओर जाते हैं। ‘सम्यक्’ ‘पीतम्’ से (भली-भाँति पिया) या ‘हितम्’ से (भली-भाँति हितकर) जुड़ सकता है। संधियाँ जाँची: किंचित् + दोषघ्नं → किंचिद्दोषघ्नं; सम्यक् + दोषोदरे → सम्यग्दोषोदरे।",
    "102": "‘क्रिमिकुष्ठिनाम्’ को ‘क्रिमिन् + कुष्ठिन्’ या ‘क्रिमिकुष्ठ + इन्’ दोनों तरह समझा जा सकता है; अर्थ वही रहता है। हाथी के मूत्र का वर्णन १०३ की पहली पंक्ति में चलता है। ‘सर’ का अर्थ यहाँ मल को सरकाने वाला (रेचक) लिया गया है।",
    "103": "विश्वास: मध्यम। पंक्ति १०३अ को हाथी के मूत्र से जोड़ा गया है (१०२ब से चलती हुई); व्याकरण से यह ऊँट के वर्णन का आरम्भ भी पढ़ी जा सकती है, पर १०३ब में अपना कर्ता (औष्ट्रम्) है। ‘श्लेष्मामय’ = कफ-रोग (या ‘कफ और आम’, कम सम्भव)। संधि: च + औष्ट्रम् → चौष्ट्रम्; अर्शः + घ्नम् → अर्शोघ्नम्।",
    "104": "‘वाजिनाम्’ के साथ ‘मूत्रम्’ समझा जाता है। ‘ग्रह’ का अर्थ दुष्ट सत्त्वों द्वारा पकड़ (‘बाधा’) है; टीकाकार इसे रोग-वर्ग भी मानते हैं। संधि: विष + अपहम् → विषापहम् (अ + अ → आ)। ‘खरमूत्रमपस्मार…’ में म् + अ बिना परिवर्तन के सटे हैं।",
    "105": "‘यथासामर्थ्ययोगतः’ को ‘जहाँ तक सामर्थ्य उपयोग की अनुमति दे’ या ‘शक्ति और संयोग के अनुसार’ भी पढ़ा जा सकता है। ‘वक्ष्यन्ते’ पाठ में भविष्यत् (कर्मवाच्य के अर्थ में) है। संधियाँ: इति + इह + उक्तानि → इतीहोक्तानि; च + एषाम् → चैषाम्; गुणाः + च → गुणाश्च (विसर्ग → श् च से पहले)।",
    "106": "आठ दूधों की सूची; टिप्पणी इसे पहले के मूत्रों के समानान्तर कहती है (श्लोक में ऐसा नहीं कहा गया)। ‘अजाक्षीरम्’ में ‘अजा’ स्त्रीलिंग रूप है। संधि: स्त्रियाः + तथा → स्त्रियास्तथा; उष्ट्रीणाम् + अथ → उष्ट्रीणामथ (म् + अ सटे हैं)। पाठभेद कोई नहीं।",
    "107": "विश्वास: मध्यम। ‘स्तन्य’ को यहाँ ‘स्तन्य (दूध) बढ़ाने वाला’ लिया गया है; ‘माँ के दूध जैसा’ या केवल ‘स्तन्य’ भी पढ़ा जा सकता है। ‘मनस्कर’ का शब्दार्थ ‘मन करने वाला’ है। संधियाँ: प्रायशः + मधुरं → प्रायशो मधुरं; पयः + मतम् → पयो मतम्। वाक्य श्लोक १०८ में चलता है।",
    "108": "यह श्लोक १०७ का वाक्य जारी रखता है; कर्ता (दूध) पीछे से समझा जाता है। ‘शोणितपित्त’ = रक्तपित्त। ‘सन्धानं विहतस्य’: चोट खाए या टूटे हुए को जोड़ने वाला। संधि: सम् + धानम् → सन्धानम्।",
    "109": "विश्वास: मध्यम। पाठ में ‘सर्वप्राणाभृतां’ छपा है; सामान्य समास ‘प्राणभृत्’ (दीर्घ ‘आ’ अनियमित) है। छन्द दोनों को सह लेता है। ‘शमन/शोधन’ चिकित्सा के दो प्रकार हैं (शान्त करने वाला और निकालने वाला)। ‘क्षीणक्षत’ को ‘क्षीण और क्षत’ या ‘उरःक्षतजन्य क्षय’ पढ़ा जा सकता है।",
}

AIDS = {
    "100": {
        "diagram": {"groups": [
            {"label": "भेड़",
             "items": ["अविमूत्रं", "सतिक्तं", "स्निग्धं", "पित्ताविरोधि"]},
            {"label": "बकरी",
             "items": ["आजं", "कषायमधुरं", "पथ्यं", "दोषान्निहन्ति"]}]},
        "contrast": "भेड़ (अवि): थोड़ा तिक्त, स्निग्ध, पित्त का विरोधी नहीं ↔ बकरी (आज): कषाय-मधुर, पथ्य, दोषनाशक। ध्यान दें: ‘पथ्य’ और ‘दोषनाश’ बकरी के लिए कहे गए हैं।",
        "sandhi": "अ + अ → आ: पित्त + अविरोधि → पित्ताविरोधि। ‘अ-’ निषेध है, इसलिए अर्थ ‘पित्त का विरोधी नहीं’।",
        "anchors": "अवि = भेड़ (श्लोक १०६ में अविक्षीरम्) · आज ← अज (बकरी) · पथ्य = हितकर, अनुकूल (श्लोक में ‘पथ्यं’ बकरी के मूत्र के लिए)।",
        "chunks": "अविमूत्रं सतिक्तं स्यात् | स्निग्धं पित्ताविरोधि च ‖ आजं कषायमधुरं | पथ्यं दोषान्निहन्ति च।",
    },
    "101": {
        "frame": "कौन: गाय का मूत्र · गुण: मधुर, दोषघ्न · काम: कृमि-कुष्ठ दूर, खुजली शान्त (पीने पर), दोषज उदर में हित।",
        "diagram": {"groups": [
            {"label": "गुण",
             "items": ["गव्यं", "समधुरं", "किंचिद्दोषघ्नं", "क्रिमिकुष्ठनुत्"]},
            {"label": "प्रयोग",
             "items": ["कण्डूं", "शमयेत्", "पीतं", "सम्यग्दोषोदरे", "हितम्"]}]},
        "pegs": "मेरा बनाया चित्र: गाय के पास मटका, ऊपर खुजली खुजाता बन्दर और कीड़ा-कृमि; पीने पर खुजली शान्त, कीड़े बाहर।",
        "sandhi": "क् → ग् (घोष द से पहले): सम्यक् + दोषोदरे → सम्यग्दोषोदरे; त् → द् (वही नियम): किंचित् + दोषघ्नं → किंचिद्दोषघ्नं। अ + उ → ओ: दोष + उदरे → दोषोदरे।",
        "chunks": "गव्यं समधुरं | किंचिद्दोषघ्नं | क्रिमिकुष्ठनुत् ‖ कण्डूं च शमयेत् पीतं | सम्यग्दोषोदरे हितम्।",
    },
    "102": {
        "diagram": {"groups": [
            {"label": "भैंस",
             "items": ["अर्शःशोफोदरघ्नं", "सक्षारं", "माहिषं", "सरम्"]},
            {"label": "हाथी",
             "items": ["हास्तिकं", "लवणं", "मूत्रं", "हितं", "क्रिमिकुष्ठिनाम्"]}]},
        "anchors": "माहिष ← महिष (भैंसा), हास्तिक ← हस्तिन् (हाथी), आज ← अज (बकरी), गव्य ← गो: पशु के नाम का ‘उसका’ वाला रूप। लवण = नमकीन (लवण = नमक)।",
        "contrast": "भैंस (क्षार, सर; अर्श-शोफ-उदर का नाश) ↔ हाथी (लवण; कृमि-कुष्ठ वालों के लिए हित)। हाथी का वर्णन श्लोक १०३ की पहली पंक्ति में चलता है।",
        "chunks": "अर्शःशोफोदरघ्नं तु | सक्षारं माहिषं सरम् ‖ हास्तिकं लवणं मूत्रं | हितं तु क्रिमिकुष्ठिनाम्।",
    },
    "103": {
        "frame": "पहली पंक्ति: पिछले वाक्य का शेष (हाथी के मूत्र के प्रयोग) · दूसरी पंक्ति: ऊँट का मूत्र: थोड़ा तिक्त, श्वास-कास-अर्श नाशक।",
        "diagram": {"groups": [
            {"label": "प्रशस्त (पिछला वाक्य)",
             "items": ["प्रशस्तं", "बद्धविण्मूत्रविषश्लेष्मामयार्शसाम्"]},
            {"label": "ऊँट",
             "items": ["सतिक्तं", "श्वासकासघ्नमर्शोघ्नं", "चौष्ट्रमुच्यते"]}]},
        "sandhi": "अ + औ → औ: च + औष्ट्रम् → चौष्ट्रम्। अः + घ → ओ घ: अर्शः + घ्नम् → अर्शोघ्नम्।",
        "anchors": "ऊँट: उष्ट्र → औष्ट्र (‘ऊँट का’) · श्वास = साँस की तकलीफ़ · कास = खाँसी · अर्श = बवासीर।",
        "chunks": "प्रशस्तं बद्धविण्मूत्र | विषश्लेष्मामयार्शसाम् ‖ सतिक्तं श्वासकासघ्नम् | अर्शोघ्नं चौष्ट्रमुच्यते।",
    },
    "104": {
        "diagram": {"groups": [
            {"label": "घोड़ा",
             "items": ["वाजिनां", "तिक्तकटुकं", "कुष्ठव्रणविषापहम्"]},
            {"label": "गधा",
             "items": ["खरमूत्रम्", "अपस्मारोन्मादग्रहविनाशनम्"]}]},
        "contrast": "घोड़ा: त्वचा-घाव-विष (कुष्ठ, व्रण, विष) ↔ गधा: मन-बाधा के रोग (अपस्मार, उन्माद, ग्रह)। यह मेरा याद करने का वर्गीकरण है, श्लोक का नहीं।",
        "sandhi": "अ + अ → आ: विष + अपहम् → विषापहम्।",
        "anchors": "अपह और विनाशन = दूर करने/नष्ट करने वाला · वाजिन् = घोड़ा · खर = गधा · व्रण = घाव।",
        "chunks": "वाजिनां तिक्तकटुकं | कुष्ठव्रणविषापहम् ‖ खरमूत्रम् | अपस्मारोन्मादग्रहविनाशनम्।",
    },
    "105": {
        "frame": "क्या पूरा हुआ: मूत्र · कैसे: सामर्थ्य और प्रयोग के अनुसार · अब क्या: क्षीर, उनके कर्म और गुण।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["इति", "इह", "उक्तानि", "मूत्राणि", "यथासामर्थ्ययोगतः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["अतः", "क्षीराणि", "वक्ष्यन्ते", "कर्म", "गुणाः"]}]},
        "sandhi": "इ + इ → ई, अ + उ → ओ: इति + इह + उक्तानि → इतीहोक्तानि। अ + ए → ऐ: च + एषाम् → चैषाम्।",
        "anchors": "अतः = इसलिए/अब से · वक्ष्यन्ते ← √वच् (कहना) · कर्म = क्रिया/प्रभाव · गुण = विशेषता।",
        "chunks": "इतीहोक्तानि मूत्राणि | यथासामर्थ्ययोगतः ‖ अतः क्षीराणि वक्ष्यन्ते | कर्म चैषां गुणाश्च ये।",
    },
    "106": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["अविक्षीरं", "अजाक्षीरं", "गोक्षीरं", "माहिषं"]},
            {"label": "दूसरी पंक्ति",
             "items": ["उष्ट्रीणां", "नागीनां", "वडवायाः", "स्त्रियाः"]}]},
        "letters": "अ-अ-गो-मा | उ-ना-व-स्त्री: भेड़, बकरी, गाय, भैंस | ऊँटनी, हथिनी, घोड़ी, स्त्री।",
        "pegs": "मेरा बनाया चित्र: आठ दूध के प्याले एक कतार में, पहले चार घर के पशुओं के, फिर ऊँटनी, हथिनी, घोड़ी और अन्त में स्त्री का प्याला।",
        "sandhi": "विसर्ग + त → स् त: स्त्रियाः + तथा → स्त्रियास्तथा।",
        "anchors": "क्षीर = दूध · उष्ट्री ← उष्ट्र (ऊँट) · नागी ← नाग (हाथी) · वडवा = घोड़ी।",
        "chunks": "अविक्षीरमजाक्षीरं | गोक्षीरं माहिषं च यत् ‖ उष्ट्रीणामथ नागीनां | वडवायाः स्त्रियास्तथा।",
    },
    "107": {
        "frame": "विषय: दूध (पयः) · कितना: प्रायशः (अधिकतर) · क्या: मधुर, स्निग्ध, शीत, स्तन्य और कर्म: प्रीणन से मनस्कर तक।",
        "diagram": {"groups": [
            {"label": "सामान्य गुण",
             "items": ["प्रायशः", "मधुरं", "स्निग्धं", "शीतं", "स्तन्यं", "पयः मतम्"]},
            {"label": "कर्म",
             "items": ["प्रीणनं", "बृंहणं", "वृष्यं", "मेध्यं", "बल्यं", "मनस्करम्"]}]},
        "letters": "प्री-बृं-वृ-मे-ब-म: प्रीणन, बृंहण, वृष्य, मेध्य, बल्य, मनस्कर (कर्मों के पहले अक्षर)।",
        "sandhi": "अः + घोष → ो: प्रायशः + मधुरं → प्रायशो मधुरं; पयः + मतम् → पयो मतम्।",
        "anchors": "मेध्य ← मेधा (बुद्धि) · बल्य ← बल · बृंहण ← बृंह् (बढ़ाना) · प्रीणन ← प्रीति (तृप्ति)।",
        "chunks": "प्रायशो मधुरं स्निग्धं | शीतं स्तन्यं पयो मतम् ‖ प्रीणनं बृंहणं वृष्यं | मेध्यं बल्यं मनस्करम्।",
    },
    "108": {
        "frame": "विषय: दूध (श्लोक १०७ से) · क्या करता है: जीवन देता है, थकान हरता है, श्वास-कास और रक्तपित्त का नाश, चोट को जोड़ना।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["जीवनीयं", "श्रमहरं", "श्वासकासनिबर्हणम्"]},
            {"label": "दूसरी पंक्ति",
             "items": ["हन्ति", "शोणितपित्तं", "सन्धानं", "विहतस्य"]}]},
        "sandhi": "म् दन्त्य ध के मेल में दन्त्य नासिक्य न् लिखा जाता है: सम् + धानम् → सन्धानम्।",
        "anchors": "जीवनीय ← जीवन · श्रम = थकान · हर ← √हृ (हरना) · निबर्हण = नाश · शोणित = रक्त · सन्धान = जोड़ना (सम् + धा)।",
        "chunks": "जीवनीयं श्रमहरं | श्वासकासनिबर्हणम् ‖ हन्ति शोणितपित्तं च | सन्धानं विहतस्य च।",
    },
    "109": {
        "seesaw": "शमन ↔ शोधन: शमन = शान्त करने वाली चिकित्सा, शोधन = बाहर निकालने वाली चिकित्सा (पाठ-टिप्पणी)।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["सर्वप्राणाभृतां", "सात्म्यं", "शमनं", "शोधनं", "तथा"]},
            {"label": "दूसरी पंक्ति",
             "items": ["तृष्णाघ्नं", "दीपनीयं", "श्रेष्ठं", "क्षीणक्षतेषु"]}]},
        "anchors": "सात्म्य ← आत्मा/अभ्यास से अनुकूल · तृष्णा = प्यास · घ्न ← √हन् (नाश) · दीपनीय ← दीप (पाचन-अग्नि को जगाना)।",
        "pegs": "मेरा बनाया चित्र: एक तराजू के एक पलड़े में दूध का प्याला और दूसरे में पानी की बूँद; प्यास हरने वाला और दुबले-चोटिल के लिए श्रेष्ठ।",
        "chunks": "सर्वप्राणाभृतां सात्म्यं | शमनं शोधनं तथा ‖ तृष्णाघ्नं दीपनीयं च | श्रेष्ठं क्षीणक्षतेषु च।",
    },
}

IMAGE_SPECS = {
    ("106", "diagram"): {
        "file": "milks-106.svg",
        "alt": "Two columns listing the eight milks of verse 106: sheep, goat, cow, buffalo in the first line; she-camels, she-elephants, mare, woman in the second",
        "type": "split",
        "title": "श्लोक १०६: आठ दूध",
        "cols": [["पहली पंक्ति", ["अविक्षीरं", "अजाक्षीरं", "गोक्षीरं", "माहिषं"]],
                 ["दूसरी पंक्ति", ["उष्ट्रीणां", "नागीनां", "वडवायाः", "स्त्रियाः"]]],
    },
    ("100", "diagram"): {
        "file": "urine-100.svg",
        "alt": "A table with two rows: sheep's urine (slightly bitter, unctuous, not antagonistic to Pitta) and goat's urine (astringent and sweet, wholesome, destroys the doshas)",
        "type": "table",
        "title": "श्लोक १००: भेड़ और बकरी का मूत्र",
        "heads": ["पशु", "गुण"],
        "rows": [["भेड़ (अवि)", "सतिक्त · स्निग्ध · पित्ताविरोधि"],
                 ["बकरी (आज)", "कषायमधुर · पथ्य · दोषनाशक"]],
    },
}
