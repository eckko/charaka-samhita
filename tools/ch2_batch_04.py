from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "दधित्थबिल्वचाङ्गेरीतक्रदाडिमसाधिता",
    "question": "What does gruel cooked with wood-apple, bilva, cāṅgerī, buttermilk and pomegranate do?",
    "rule": ("Peyā (thin gruel) cooked with wood-apple, bilva, cāṅgerī, "
             "buttermilk and pomegranate is digestive and binding; where "
             "Vāta is present, the peyā made with the five roots."),
    "limits": ("The subject (the gruel) is understood from the verses before "
               "this one. The verse does not say which five roots make the "
               "pañcamūla; it gives no amount or timing."),
    "explain_hi": ("यह वाक्य पिछले श्लोकों से चले आ रहे विषय (पेया, यानी पतली, पी जाने वाली "
                   "यवागू) पर चलता है। पहली पंक्ति में पाँच वस्तुएँ हैं: दधित्थ, बिल्व, "
                   "चाङ्गेरी, तक्र और दाडिम; इनके साथ ‘साधिता’ (पकाई हुई) पेया "
                   "‘पाचनी’ और ‘ग्राहिणी’ कही गई है। दूसरी पंक्ति में ‘सवाते’ "
                   "(वात के होने पर) के लिए ‘पाञ्चमूलिकी’ पेया बताई गई है। "
                   "पाँच मूल कौन से हैं, यह इस श्लोक में नहीं लिखा।"),
    "hook": "दधित्थ-बिल्व-चाङ्गेरी-तक्र-दाडिम से पकी पेया = पाचनी + ग्राहिणी; वात हो तो पाँच मूल की।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Gruel cooked with wood-apple, bilva, cāṅgerī, buttermilk and pomegranate is called what in verse 19?",
            ("Digestive (पाचनी) and binding (ग्राहिणी)",
             "These are the two words the verse gives for it."),
            [("Oleating (स्नेहनी)", "This word is not in verse 19."),
             ("Worm-destroying (क्रिमिघ्नी)", "This word is not in verse 19."),
             ("Thirst-removing (पिपासाघ्नी)", "This word is not in verse 19.")],
            "पाचनी ग्राहिणी, पेया: the gruel is called digestive and binding.",
            "The first gruel group of verse 19 is digestive and binding."),
        match(1, "Match each ingredient of the first line to its meaning.",
              [["दधित्थ", "wood-apple"], ["बिल्व", "bilva fruit"],
               ["तक्र", "buttermilk"], ["दाडिम", "pomegranate"]],
              "These are four of the five things the gruel is cooked with.",
              "दधित्थ = wood-apple; बिल्व = bilva; तक्र = buttermilk; दाडिम = pomegranate."),
        fill(2, "The word for 'thin gruel' in the verse is ____ (type it in Devanagari).",
             ["पेया", "पेयां", "पेयाम्"],
             "The verse says पेया for the thin gruel.",
             "In verses 19-22 the gruel is called पेया (thin, to be drunk); verse 23 uses the word यवागू (thick gruel).",
             "पेया = thin gruel."),
        mcq("discriminate", 3,
            "In सवाते, what does the beginning स- add to वाते (in Vāta)?",
            ("'With': the whole word means when Vāta is present",
             "स- in this joined word means 'with, accompanied by', so सवाते is 'where Vāta is present'."),
            [("'Without': the whole word means when Vāta is absent",
              "Absence would need a negative such as अ-, not स-."),
             ("'Against': the whole word means opposing Vāta",
              "स- does not mean 'against'."),
             ("'From': the whole word means from Vāta",
              "The ending -ए is 'in, when', not 'from'.")],
            "सवाते = स + वाते, a joined word in the locative: 'in the case accompanied by Vāta'.",
            "स- at the start of a joined word = 'with'."),
        multi("apply", 4, "Which of these is named in verse 19 itself?",
              [("तक्र", "Right: buttermilk is in the first line."),
               ("दाडिम", "Right: pomegranate is in the first line."),
               ("बिल्व", "Right: bilva is in the first line."),
               ("मधु", "Honey appears in verse 24, not here."),
               ("सर्पिः", "Ghee appears in verse 26, not here.")],
              [0, 1, 2],
              "The first line names wood-apple, bilva, cāṅgerī, buttermilk and pomegranate.",
              "Verse 19 names buttermilk, pomegranate and bilva; honey and ghee come later."),
        mcq("transfer", 5,
            "An invented line says बिल्वतक्रसाधिता पेया पाचनी. By the frame of verse 19, what does it say?",
            ("Gruel cooked with bilva and buttermilk is digestive",
             "'Ingredients + साधिता' = cooked with them; पाचनी = digestive."),
            [("Gruel without bilva and buttermilk is digestive",
              "साधिता says 'cooked with', not 'without'."),
             ("Bilva and buttermilk are cooked in gruel to bind it",
              "The word is पाचनी (digestive), not ग्राहिणी (binding)."),
             ("Digestive gruel is a name for buttermilk",
              "The line describes a gruel; it does not rename buttermilk.")],
            "The sentence has the same frame as the first line of verse 19: ingredients + साधिता + पेया + effect.",
            "Ingredients + साधिता + पेया + effect = 'gruel cooked with these has this effect'.",
            teaches="साधिता agrees with the feminine पेया and the joined ingredient word before it means 'cooked with these'."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "शालपर्णीबलाविल्वैः पृश्निपर्ण्या च साधिता",
    "question": "For whom is the gruel cooked with śālaparṇī, balā, bilva and pṛśniparṇī, soured with pomegranate, beneficial?",
    "rule": ("Peyā cooked with śālaparṇī, balā, bilva and pṛśniparṇī and "
             "soured with pomegranate is beneficial for those with diarrhoea "
             "due to Pitta and Kapha."),
    "limits": ("The subject (the gruel) continues from earlier verses. "
               "पित्तश्लेष्मातिसारिणाम् may also be read as diarrhoea "
               "involving Pitta and Kapha; the sense is the same. The verse "
               "does not identify the plants or give amounts."),
    "explain_hi": ("इस श्लोक में पेया चार वस्तुओं के साथ पकती है: शालपर्णी, बला, बिल्व "
                   "और पृश्निपर्णी; और ‘दाडिमाम्ला’ यानी अनार से खट्टी की जाती है। "
                   "‘हिता’ का अर्थ ‘हितकर’ है और ‘पित्तश्लेष्मातिसारिणाम्’ षष्ठी "
                   "बहुवचन है: ‘पित्त और कफ से हुए अतिसार वालों के लिए’। "
                   "‘विल्वैः’ तृतीया बहुवचन है (बहुवचन) और "
                   "‘पृश्निपर्ण्या’ तृतीया एकवचन (एक पौधे के साथ)।"),
    "hook": "शालपर्णी-बला-बिल्व-पृश्निपर्णी + अनार की खटाई = पित्त-कफ के अतिसार में हितकर पेया।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 20 calls the gruel cooked with śālaparṇī, balā, bilva and pṛśniparṇī beneficial for whom?",
            ("Those with diarrhoea due to Pitta and Kapha",
             "पित्तश्लेष्मातिसारिणाम् = of those with Pitta-and-Kapha diarrhoea."),
            [("Those with bloody diarrhoea", "Bloody diarrhoea (रक्तातिसार) is in the next verse, 21."),
             ("Those with painful urination", "Painful urination (मूत्रकृच्छ्र) is in verse 22."),
             ("Those with worms", "Worms (क्रिमि) are in verse 23.")],
            "The last word of the verse names the sufferers: those with diarrhoea from Pitta and Kapha.",
            "Verse 20: the gruel is beneficial in Pitta-Kapha diarrhoea."),
        match(1, "Match each word of verse 20 to its meaning.",
              [["साधिता", "cooked"], ["हिता", "beneficial"],
               ["दाडिमाम्ला", "soured with pomegranate"],
               ["अतिसारिणाम्", "of those with diarrhoea"]],
              "These four words carry the sentence.",
              "साधिता = cooked; हिता = beneficial; दाडिमाम्ला = soured with pomegranate; अतिसारिणाम् = of those with diarrhoea."),
        fill(2, "The sour ingredient that gives the gruel its sourness is ____ (type it in Devanagari).",
             ["दाडिम", "दाडिमम्", "दाडिमं"],
             "दाडिमाम्ला = दाडिम (pomegranate) + अम्ला (sour).",
             "A joined word ending in अम्ला names what makes something sour; here the gruel is soured with pomegranate.",
             "दाडिमाम्ला = soured with pomegranate."),
        mcq("discriminate", 3,
            "विल्वैः and पृश्निपर्ण्या both mean 'with'. What does each ending show?",
            ("विल्वैः is instrumental plural; पृश्निपर्ण्या is instrumental singular",
             "Both are instrumental, 'with'; -ऐः is plural and -ण्या singular."),
            [("Both are singular", "विल्वैः ends in -ऐः, which is plural."),
             ("विल्वैः is singular; पृश्निपर्ण्या is plural", "The numbers are the other way round."),
             ("Both are genitive plural, 'of'", "The genitive plural in this verse is अतिसारिणाम्.")],
            "The group शालपर्णी-बला-विल्वैः takes one plural ending at its end; पृश्निपर्ण्या stands alone with a singular ending.",
            "-ऐः = instrumental plural; -या on a feminine word = instrumental singular."),
        multi("apply", 4, "Which of these are named in verse 20 itself?",
              [("शालपर्णी", "Right: first in the verse."),
               ("बला", "Right: second in the verse."),
               ("पृश्निपर्णी", "Right: named after bilva."),
               ("तक्र", "Buttermilk is in verse 19, not here."),
               ("ह्रीवेर", "Hrīvera is in verse 21, not here.")],
              [0, 1, 2],
              "The verse names śālaparṇī, balā, bilva and pṛśniparṇī; buttermilk and hrīvera belong to other verses.",
              "Verse 20 names śālaparṇī, balā, bilva, pṛśniparṇī and pomegranate."),
        mcq("transfer", 5,
            "An invented line says बलाविल्वसाधिता पेया हिता वातातिसारिणाम्. By the frame of verse 20, what does it say?",
            ("Gruel cooked with balā and bilva is beneficial for those with Vāta diarrhoea",
             "'-साधिता' = cooked with; 'हिता' = beneficial; '-इणाम्' names the sufferers."),
            [("Gruel cooked with balā and bilva is harmful for those with Vāta diarrhoea",
              "हिता means beneficial, not harmful."),
             ("Gruel is cooked by those with Vāta diarrhoea",
              "वातातिसारिणाम् is genitive plural: 'of/for those with', not the cooks."),
             ("Vāta diarrhoea is cooked with balā and bilva",
              "साधिता agrees with पेया (the gruel), not with the disease.")],
            "Same frame as verse 20: ingredients + साधिता + पेया + हिता + genitive plural of the sufferers.",
            "Genitive plural in -इणाम् after हिता = 'beneficial for those with ...'.",
            teaches="Joined word ending in -अतिसारिणाम् (genitive plural) names the people the remedy is for, after हिता."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "पयस्यर्धोदके च्छागे",
    "question": "What does gruel in goat's milk with half water and with hrīvera, utpala and dry ginger do?",
    "rule": ("Peyā in goat's milk mixed with half water, with hrīvera, utpala "
             "and dry ginger, and also cooked with pṛśniparṇī, destroys "
             "diarrhoea with blood."),
    "limits": ("The gruel is understood from earlier verses. 'Half water' "
               "could also describe the milk itself; the sense is the same. "
               "The verse does not identify utpala (several plants have "
               "that name) and gives no amounts."),
    "explain_hi": ("इस श्लोक में पेया बकरी (छाग) के दूध में पकती है, जिसमें आधा जल मिला है "
                   "(‘अर्धोदके’)। साथ में ह्रीवेर, उत्पल और नागर (सोंठ) हैं, और "
                   "पृश्निपर्णी से भी साधिता। फल: ‘रक्तातिसारघ्नी’, यानी रक्त वाले "
                   "अतिसार को नष्ट करने वाली। सन्धि: ‘पयसि + अर्धोदके’ का ‘इ’ ‘य्’ बनता है "
                   "(पयस्यर्धोदके) और ‘ह्रीवेर + उत्पल’ का ‘अ + उ’ मिलकर ‘ओ’ (ह्रीवेरोत्पल-) "
                   "बनता है। ‘च्छागे’ में छ दोहरा होकर च्छ हुआ है।"),
    "hook": "बकरी का दूध (आधा जल) + ह्रीवेर-उत्पल-सोंठ + पृश्निपर्णी = रक्तातिसार-नाशक पेया।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 21 calls the gruel in goat's milk with half water 'रक्तातिसारघ्नी'. What does it destroy?",
            ("Diarrhoea with blood",
             "रक्त + अतिसार + घ्नी = destroying diarrhoea with blood."),
            [("Diarrhoea due to Pitta and Kapha", "That is verse 20, not this verse."),
             ("Painful urination", "That is verse 22."),
             ("Thirst", "Thirst is in verse 24.")],
            "रक्तातिसारघ्नी ends in -घ्नी, 'destroying'; the thing destroyed is bloody diarrhoea.",
            "Verse 21: goat's-milk gruel destroys diarrhoea with blood."),
        match(1, "Match each word of verse 21 to its meaning.",
              [["अर्धोदके", "having half water"], ["नागरैः", "with dry ginger"],
               ["साधिता", "cooked"], ["रक्तातिसारघ्नी", "destroying bloody diarrhoea"]],
              "These words carry the sentence.",
              "अर्धोदके = having half water; नागरैः = with dry ginger; साधिता = cooked; रक्तातिसारघ्नी = destroying bloody diarrhoea."),
        fill(2, "The word for 'milk' in the first line is ____ (type it in Devanagari, as in 'पयस्यर्धोदके').",
             ["पयः", "पयसि", "पयस्", "पय", "पयस"],
             "The milk word is पयः; in the verse it is पयसि, 'in milk'.",
             "पयः is the milk word; the locative पयसि 'in milk' joins to अर्धोदके by sandhi: इ becomes य् before a vowel.",
             "पयः = milk; पयसि = in milk."),
        mcq("discriminate", 3, "Which is the right split of ह्रीवेरोत्पलनागरैः?",
            ("ह्रीवेर + उत्पल + नागरैः",
             "अ + उ joins to ओ, so ह्रीवेर + उत्पल is written ह्रीवेरोत्पल."),
            [("ह्रीवेर + त्पल + नागरैः", "त्पल is not a word."),
             ("ह्रीवेरो + पल + नागरैः", "There is no word पल in the verse's list."),
             ("ह्रीवेरः + उत्पल + नागरैः", "अः before a vowel other than अ drops the visarga and leaves a gap; it does not make ओ.")],
            "Three ingredients are joined: ह्रीवेर, उत्पल and नागरैः.",
            "अ + उ → ओ: ह्रीवेर + उत्पल = ह्रीवेरोत्पल."),
        multi("apply", 4, "Which of these are named in verse 21 itself?",
              [("ह्रीवेर", "Right: first of the three joined ingredients."),
               ("उत्पल", "Right: second of the three."),
               ("नागर", "Right: dry ginger ends the group."),
               ("बिल्व", "Bilva is in verses 19-20, not here."),
               ("मरिच", "Pepper is in verse 23, not here.")],
              [0, 1, 2],
              "Verse 21 names hrīvera, utpala and dry ginger (and pṛśniparṇī in line 2).",
              "Verse 21 names ह्रीवेर, उत्पल and नागर."),
        mcq("transfer", 5,
            "An invented gruel is called ज्वरघ्नी. By the pattern of रक्तातिसारघ्नी, what does ज्वरघ्नी say? (ज्वर = fever)",
            ("It destroys fever",
             "X + घ्नी = destroying X, so ज्वर + घ्नी = fever-destroying."),
            [("It causes fever", "-घ्नी means destroying, not causing."),
             ("It is made with fever", "The pattern names what is destroyed, not an ingredient."),
             ("It is cooked in fever", "The pattern names what is destroyed, not a vessel or place.")],
            "In रक्तातिसारघ्नी the thing destroyed (bloody diarrhoea) comes before -घ्नी.",
            "X + -घ्नी = destroying X.",
            teaches="A feminine joined word ending in -घ्नी describes a gruel as 'destroying' whatever comes before it."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "दद्यात् सातिविषां पेयां",
    "question": "Which gruel does the verse prescribe when āma is present, and which in painful urination?",
    "rule": ("In the case with āma, give peyā with ativiṣā, with a sour "
             "ingredient and with dry ginger; in painful urination, peyā "
             "cooked with śvadaṃṣṭrā and kaṇṭakārī and with phāṇita."),
    "limits": ("Āma (undigested matter) is only glossed in the data, not "
               "defined by the verse. The verse does not say which sour "
               "ingredient. The edition records a variant 'peyām āme' for "
               "'peyāṃ sāme', so the first condition could be read two ways."),
    "explain_hi": ("इस श्लोक में ‘दद्यात्’ (देनी चाहिए) एक बार आता है और दोनों आधों पर लगता है। "
                   "पहला आधा: ‘सामे’ (आम की अवस्था में) अतिविषा, खटाई और सोंठ वाली पेया। "
                   "दूसरा आधा: ‘मूत्रकृच्छ्रे’ (कष्ट से मूत्र में) श्वदंष्ट्रा और "
                   "कण्टकारी से पकी और फाणित वाली पेया। खटाई कौन सी है, यह श्लोक "
                   "नहीं बताता। संस्करण में पाठान्तर ‘पेयामामे’ भी दर्ज है, इसलिए "
                   "पहली स्थिति ‘सामे’ या ‘आमे’ दोनों पढ़ी जा सकती है।"),
    "hook": "दद्यात्: आम में अतिविषा-खटाई-सोंठ वाली पेया; मूत्रकृच्छ्र में श्वदंष्ट्रा-कण्टकारी-फाणित वाली।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 22 gives gruel for two conditions. Which two?",
            ("The condition with āma, and painful urination",
             "सामे = when āma is present; मूत्रकृच्छ्रे = in painful urination."),
            [("Bloody diarrhoea and worms", "These are in verses 21 and 23."),
             ("Thirst and poison", "These are in verse 24."),
             ("Cough and hiccup", "These are in verse 27.")],
            "The two conditions are named by the two locative words सामे and मूत्रकृच्छ्रे.",
            "Verse 22: āma and painful urination."),
        match(1, "Match each word of verse 22 to its meaning.",
              [["दद्यात्", "one should give"], ["सामे", "when āma is present"],
               ["मूत्रकृच्छ्रे", "in painful urination"], ["सफाणिताम्", "with phāṇita"]],
              "Each word is one part of the instruction.",
              "दद्यात् = one should give; सामे = when āma is present; मूत्रकृच्छ्रे = in painful urination; सफाणिताम् = with phāṇita."),
        fill(2, "The verb meaning 'one should give' is ____ (type it in Devanagari).",
             ["दद्यात्", "दद्यात"],
             "दद्यात् is the third person singular optative of √दा, 'one should give'.",
             "One optative verb serves both halves of the verse: दद्यात् governs the first gruel and, by understanding, the second.",
             "दद्यात् = one should give; it serves both halves."),
        mcq("discriminate", 3, "Which is the right split of सामे?",
            ("स + आमे",
             "अ + आ joins to आ, so स ('with') + आमे ('in āma') is written सामे."),
            [("सा + मे", "Neither सा nor मे fits the sense 'when āma is present'."),
             ("सः + आमे", "A visarga there would give स आमे, not सामे."),
             ("सम् + आमे", "सम् before आमे would be written समामे.")],
            "सामे is a joined word: 'when āma is present'.",
            "सामे = स + आमे."),
        multi("apply", 4, "Which of these go into the gruel for painful urination in verse 22?",
              [("श्वदंष्ट्रा", "Right: the gruel is cooked with it."),
               ("कण्टकारी", "Right: the gruel is cooked with it."),
               ("फाणित", "Right: the gruel is with phāṇita."),
               ("अतिविषा", "Ativiṣā belongs to the gruel for the āma condition."),
               ("नागर", "Dry ginger belongs to the gruel for the āma condition.")],
              [0, 1, 2],
              "The second line gives the painful-urination gruel; ativiṣā and dry ginger are in the first line.",
              "Painful urination: श्वदंष्ट्रा, कण्टकारी, फाणित."),
        mcq("transfer", 5,
            "An invented word सज्वरे follows the pattern of सामे. What does it mean? (ज्वर = fever)",
            ("When fever is present",
             "स + ज्वरे = in the case with fever, as सामे is 'with āma'."),
            [("When fever is absent", "स- means 'with', not 'without'."),
             ("From fever", "The ending -ए is 'in, when', not 'from'."),
             ("Fever destroyer", "-ए here is a locative, not a destroyer word like -घ्नी.")],
            "सामे and सवाते (verse 19) are built the same way: स- + noun in the locative.",
            "स- + locative noun = 'when X is present'.",
            teaches="A joined word स- + locative names the condition under which the remedy is given."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "विडङ्गपिप्पलीमूलशिग्रुभिर्मरिचेन च",
    "question": "What does the yavāgū cooked in buttermilk with viḍaṅga, pepper and the other ingredients do?",
    "rule": ("A yavāgū (thick gruel) cooked in buttermilk with viḍaṅga, "
             "pippalī root, śigru and pepper, together with suvarcikā, "
             "would be worm-destroying."),
    "limits": ("Whether pippalī and mūla are one item (pippalī root) or two "
               "is a reading choice, so no count is taken. The verse leaves "
               "suvarcikā unidentified. The edition records Gaṅgādhara's "
               "remark that buttermilk is to be understood in place of water."),
    "explain_hi": ("इस श्लोक में ‘यवागू’ (गाढ़ी यवागू) शब्द आता है। यवागू तक्र "
                   "(छाछ) में पकाई जाती है (‘तक्रसिद्धा’), और विडङ्ग, पिप्पलीमूल, शिग्रु, "
                   "मरिच तथा सुवर्चिका के साथ ‘क्रिमिघ्नी’, यानी कृमि को नष्ट करने "
                   "वाली, होनी चाहिए (‘स्यात्’ = विधिलिङ्, ‘would be’)। सन्धि: शिग्रुभिः + मरिचेन में "
                   "‘इः’ के विसर्ग का ‘र्’ बना (शिग्रुभिर्मरिचेन)। टीका में गङ्गाधर "
                   "का मत दर्ज है कि यहाँ जल की जगह तक्र समझना चाहिए।"),
    "hook": "तक्र में पकी यवागू + विडङ्ग-पिप्पलीमूल-शिग्रु-मरिच + सुवर्चिका = कृमिनाशक।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is the yavāgū of verse 23, cooked in buttermilk with viḍaṅga, pepper and others, called?",
            ("Worm-destroying (क्रिमिघ्नी)",
             "क्रिमिघ्नी = क्रिमि (worms) + घ्नी (destroying)."),
            [("Thirst-removing (पिपासाघ्नी)", "That belongs to verse 24."),
             ("Nourishing (बृंहणी)", "That belongs to verse 25."),
             ("Oleating (स्नेहनी)", "That belongs to verse 26.")],
            "The last line gives the effect: क्रिमिघ्नी, worm-destroying.",
            "Verse 23: the buttermilk-cooked yavāgū is worm-destroying."),
        match(1, "Match each word of verse 23 to its meaning.",
              [["तक्रसिद्धा", "cooked in buttermilk"], ["यवागूः", "thick gruel"],
               ["क्रिमिघ्नी", "worm-destroying"], ["मरिचेन", "with pepper"]],
              "These four words carry the sentence.",
              "तक्रसिद्धा = cooked in buttermilk; यवागूः = thick gruel; क्रिमिघ्नी = worm-destroying; मरिचेन = with pepper."),
        fill(2, "The word for 'thick gruel' in this verse is ____ (type it in Devanagari).",
             ["यवागूः", "यवागू", "यवागूं", "यवागूम्"],
             "The verse says यवागूः.",
             "Verses 19-22 used पेया (thin gruel); this verse uses यवागू (thick gruel), the word the data glosses 'thick gruel'.",
             "यवागू = thick gruel."),
        mcq("discriminate", 3, "Which is the right split of शिग्रुभिर्मरिचेन?",
            ("शिग्रुभिः + मरिचेन",
             "A visarga after इ becomes र् before a voiced sound (म), so शिग्रुभिः + मरिचेन is written शिग्रुभिर्मरिचेन."),
            [("शिग्रुभो + मरिचेन", "A visarga becomes ओ only after अ, not after इ."),
             ("शिग्रुभि + रमरिचेन", "रमरिचेन is not a word."),
             ("शिग्रुभिः + अरिचेन", "अरिचेन is not the word in the verse; the word is मरिचेन, 'with pepper'.")],
            "शिग्रुभिः is the instrumental plural 'with śigrus'; मरिचेन is 'with pepper'.",
            "इः + voiced sound → इर्: शिग्रुभिः + मरिचेन = शिग्रुभिर्मरिचेन."),
        multi("apply", 4, "Which of these are named in verse 23 itself?",
              [("विडङ्ग", "Right: first in the verse."),
               ("शिग्रु", "Right: it is in the first line."),
               ("मरिच", "Right: pepper ends the first line."),
               ("मधु", "Honey is in verse 24, not here."),
               ("दाडिम", "Pomegranate is in verses 19-20, not here.")],
              [0, 1, 2],
              "Verse 23 names viḍaṅga, śigru and pepper among its ingredients.",
              "Verse 23 names विडङ्ग, शिग्रु and मरिच; honey and pomegranate belong elsewhere."),
        mcq("transfer", 5,
            "An invented phrase is क्षीरसिद्धा यवागूः. By the pattern of तक्रसिद्धा, what does it describe? (क्षीर = milk)",
            ("A thick gruel cooked in milk",
             "X + सिद्धा = cooked in X, agreeing with the feminine यवागूः."),
            [("A thick gruel without milk", "सिद्धा means 'cooked', not 'without'."),
             ("Milk cooked in thick gruel", "The gruel is what is cooked, in the milk."),
             ("A thin gruel for those who are cooked", "यवागू is the gruel; there is no person in the phrase.")],
            "तक्रसिद्धा यवागूः and क्षीरसिद्धा यवागूः have the same build; only the liquid changes.",
            "Liquid + सिद्धा + यवागूः = a thick gruel cooked in that liquid.",
            teaches="Liquid + सिद्धा (feminine) names what the gruel is cooked in; the same build appears in मदिरासिद्धा (verse 27)."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "मृद्वीकासारिवालजपिप्पलीमधुनागरैः",
    "question": "Which two effects does verse 24 name, and with which ingredients?",
    "rule": ("The yavāgū made with grapes, sārivā, parched rice, long pepper, "
             "honey and dry ginger removes thirst; the one cooked with "
             "somarājī destroys poison."),
    "limits": ("The edition prints सारिवालज with a short a; the data flags "
               "that a long ā (सारिवालाज, lāja = parched rice) may be "
               "intended. The verse does not identify somarājī or sārivā "
               "and gives no amounts. 'यवागू' is understood from earlier verses."),
    "explain_hi": ("इस श्लोक में दो फल हैं, जो ‘च’ से जुड़े हैं। पहला: मृद्वीका (द्राक्षा), "
                   "सारिवा, लाज (खील), पिप्पली, मधु और नागर (सोंठ) वाली यवागू "
                   "‘पिपासाघ्नी’ है, यानी प्यास शान्त करती है। दूसरा: सोमराजी के साथ "
                   "पकी हुई ‘विषघ्नी’ है, यानी विष का नाश करने वाली। छपे पाठ में ‘सारिवालज’ "
                   "है; सन्धि के हिसाब से ‘सारिवालाज’ होना चाहिए था, इसलिए संस्करण की "
                   "सम्भावित भूल दर्ज है। सोमराजी की पहचान श्लोक नहीं देता।"),
    "hook": "द्राक्षा-सारिवा-खील-पिप्पली-मधु-सोंठ = प्यास-नाशक; सोमराजी से पकी = विष-नाशक।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 24 names two effects of its two gruels. Which pair?",
            ("Thirst-removing and poison-destroying",
             "पिपासाघ्नी and विषघ्नी, joined by च."),
            [("Worm-destroying and thirst-removing", "Worm-destroying is verse 23."),
             ("Nourishing and reducing", "These are the two effects of verse 25."),
             ("Oleating and drying", "These are the two effects of verse 26.")],
            "पिपासाघ्नी, विषघ्नी च: thirst-removing and poison-destroying.",
            "Verse 24: one gruel removes thirst; the somarājī one destroys poison."),
        match(1, "Match each word of verse 24 to its meaning.",
              [["पिपासाघ्नी", "thirst-removing"], ["विषघ्नी", "poison-destroying"],
               ["मधु", "honey"], ["मृद्वीका", "grapes (raisins)"]],
              "Two effect words and two ingredients.",
              "पिपासाघ्नी = thirst-removing; विषघ्नी = poison-destroying; मधु = honey; मृद्वीका = grapes."),
        fill(2, "Inside पिपासाघ्नी, the word for 'thirst' is ____ (type it in Devanagari).",
             ["पिपासा"],
             "पिपासा + घ्नी = thirst + destroying.",
             "The first part of a -घ्नी word names what is removed: पिपासा (thirst), as विष (poison) in विषघ्नी.",
             "पिपासाघ्नी = पिपासा + घ्नी."),
        mcq("discriminate", 3,
            "Which ingredient does verse 24 tie to the poison-destroying gruel, not to the thirst-removing one?",
            ("सोमराजी",
             "सोमराजीविपाचिता: cooked with somarājī, and that gruel is विषघ्नी."),
            [("मधु", "Honey is in the thirst-removing group."),
             ("नागर", "Dry ginger is in the thirst-removing group."),
             ("मृद्वीका", "Grapes are in the thirst-removing group.")],
            "The first line lists the thirst-removing ingredients; the second line gives सोमराजी for the poison-destroying gruel.",
            "सोमराजी → विषघ्नी; मृद्वीका ... नागर → पिपासाघ्नी."),
        multi("apply", 4, "Which of these are named for the thirst-removing gruel in verse 24?",
              [("मृद्वीका", "Right: first in the list."),
               ("मधु", "Right: honey is in the list."),
               ("नागर", "Right: dry ginger ends the list."),
               ("सोमराजी", "Somarājī belongs to the poison-destroying gruel."),
               ("तक्र", "Buttermilk is in verse 23, not here.")],
              [0, 1, 2],
              "The first line lists the thirst-removing ingredients; somarājī is in the second line.",
              "Thirst-removing: मृद्वीका, मधु, नागर and the others of the first line."),
        mcq("transfer", 5,
            "An invented line says कासघ्नी च मरिचविपाचिता, like सोमराजीविपाचिता. What does it say? (मरिच = pepper, कास = cough)",
            ("And the one cooked with pepper destroys cough",
             "X + विपाचिता = cooked with X, and च adds a second effect, as in verse 24."),
            [("And the one cooked with cough destroys pepper",
              "The roles are reversed: pepper is the ingredient, cough the thing destroyed."),
             ("And the one without pepper destroys cough", "विपाचिता says 'cooked with', not 'without'."),
             ("And pepper is cooked by cough", "मरिचविपाचिता describes the gruel, not pepper.")],
            "Verse 24 joins two gruels with च; each has an ingredient + विपाचिता and an effect ending in -घ्नी.",
            "X + विपाचिता = cooked with X; च joins a second gruel and its effect.",
            teaches="च joins a second gruel to the first; ingredient + विपाचिता names what it is cooked with, and -घ्नी names the effect."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "सिद्धा वराहनिर्यूहे यवागूर्बृंहणी मता",
    "question": "Which yavāgū does the verse call nourishing, and which reducing?",
    "rule": ("A yavāgū cooked in boar broth is considered nourishing "
             "(बृंहणी); that of roasted gavedhukā, with honey, is "
             "reducing (कर्शनीया)."),
    "limits": ("In the second line the word यवागू is understood from the "
               "first. The verse does not identify gavedhukā and does not "
               "say how either effect arises; निर्यूह is read as decoction or "
               "broth."),
    "explain_hi": ("पहली पंक्ति: वराह (सूअर) के निर्यूह (क्वाथ/शोरबे) में पकाई गई यवागू "
                   "‘बृंहणी’ मानी गई है, यानी पुष्ट करने वाली। दूसरी पंक्ति में यवागू शब्द "
                   "अनकहा चला आता है: भुने हुए गवेधुक की, मधु सहित, यवागू ‘कर्शनीया’ "
                   "है, यानी दुबला करने वाली। इस तरह एक ही श्लोक में दो उलटे गुण हैं: "
                   "बृंहण ↔ कर्शन। सन्धि: यवागूः + बृंहणी में ऊः का विसर्ग ‘र्’ बनता है।"),
    "hook": "वराह-शोरबे की यवागू = बृंहणी (पुष्टि); भुना गवेधुक + मधु = कर्शनीया (दुबला)।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which yavāgū does verse 25 call nourishing (बृंहणी)?",
            ("The one cooked in boar broth",
             "सिद्धा वराहनिर्यूहे यवागूर्बृंहणी: cooked in boar broth, it is nourishing."),
            [("The one of roasted gavedhukā with honey", "That one is reducing (कर्शनीया)."),
             ("The one cooked in buttermilk", "Buttermilk is in verse 23, not here."),
             ("The one with ghee and sesame", "That one is oleating and is in verse 26.")],
            "The first line gives the nourishing gruel: the boar-broth one.",
            "Verse 25: boar-broth yavāgū = nourishing."),
        match(1, "Match each word of verse 25 to its meaning.",
              [["बृंहणी", "nourishing"], ["कर्शनीया", "reducing"],
               ["समाक्षिका", "with honey"], ["निर्यूह", "decoction or broth"]],
              "The two effect words and two helpers.",
              "बृंहणी = nourishing; कर्शनीया = reducing; समाक्षिका = with honey; निर्यूह = broth."),
        fill(2, "The word for 'with honey' in the second line is ____ (type it in Devanagari).",
             ["समाक्षिका"],
             "स + माक्षिका: स- ('with') + माक्षिका (honey) gives समाक्षिका.",
             "A joined word with स- at the front and a feminine ending names a gruel 'with' that thing, as सवाते and सामे name conditions 'with' something.",
             "समाक्षिका = with honey."),
        mcq("discriminate", 3, "Which is the right split of यवागूर्बृंहणी?",
            ("यवागूः + बृंहणी",
             "A visarga after ऊ becomes र् before a voiced sound (ब), so यवागूः + बृंहणी is written यवागूर्बृंहणी."),
            [("यवागू + र्बृंहणी", "र्बृंहणी is not a word."),
             ("यवागूः + अबृंहणी", "That would be written यवागूरबृंहणी and would mean 'not nourishing'."),
             ("यवागुः + बृंहणी", "The word यवागू has a long ऊ, not a short उ.")],
            "यवागूः is the gruel; बृंहणी is its effect, 'nourishing'.",
            "ऊः + voiced sound → ऊर्: यवागूः + बृंहणी = यवागूर्बृंहणी."),
        mcq("apply", 4,
            "Which yavāgū does verse 25 call reducing (कर्शनीया)?",
            ("The yavāgū of roasted gavedhukā, with honey",
             "भृष्टानां गवेधुकानां कर्शनीया समाक्षिका: roasted gavedhukā, with honey, is reducing."),
            [("The yavāgū cooked in boar broth", "That one is nourishing, not reducing."),
             ("Either one, since both are in the verse", "The two have opposite effects in the verse."),
             ("The yavāgū cooked in buttermilk", "Buttermilk is not in verse 25.")],
            "The second line names the reducing gruel.",
            "Reducing: roasted gavedhukā with honey."),
        mcq("transfer", 5,
            "An invented line says सिद्धा मेषनिर्यूहे यवागूः. By the pattern of वराहनिर्यूहे, what does it say? (मेष = ram)",
            ("A yavāgū cooked in a broth of ram",
             "The ending -ए on the compound is 'in', and सिद्धा is 'cooked', agreeing with यवागूः."),
            [("A yavāgū cooked without any ram broth", "निर्यूहे names the broth the gruel is cooked in."),
             ("A ram cooked in a broth of yavāgū", "The gruel is what is cooked, in the broth."),
             ("A yavāgū that makes the ram a broth", "No verb of making is in the line; सिद्धा means 'cooked'.")],
            "Verse 25 line 1: सिद्धा + (animal)निर्यूहे + यवागूः. Only the animal changes.",
            "सिद्धा + X-निर्यूहे = cooked in a broth of X.",
            teaches="Animal + निर्यूहे (locative) names the broth in which the gruel is cooked."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "सर्पिष्मती बहुतिला स्नेहनी लवणान्विता",
    "question": "Which yavāgū does the verse call oleating, and which drying?",
    "rule": ("The one with ghee, much sesame and salt is oleating "
             "(स्नेहनी); that of śyāmāka millet in a decoction of kuśa and "
             "āmalaka is drying (विरुक्षणी)."),
    "limits": ("यवागू is understood from earlier verses. The source has a "
               "stray '&' before a word (removed); check the word division. "
               "कुशामलक is read as two ingredients but could be one name. "
               "The verse says nothing more about oleating or drying."),
    "explain_hi": ("पहली पंक्ति में तीन विशेषण यवागू के हैं: ‘सर्पिष्मती’ (घी वाली), "
                   "‘बहुतिला’ (बहुत तिल वाली) और ‘लवणान्विता’ (नमक सहित); फल: "
                   "‘स्नेहनी’, यानी चिकना करने वाली। दूसरी पंक्ति: कुश और आमलक के "
                   "निर्यूह में पकी श्यामाक की यवागू ‘विरुक्षणी’ है, यानी रूखा करने वाली। "
                   "यह श्लोक का जोड़ा है: स्नेहनी ↔ विरुक्षणी। सन्धि: लवण + अन्विता = "
                   "लवणान्विता (अ + अ → आ)। छापे में एक अवांछित ‘&’ चिह्न का संकेत है; "
                   "शब्द-विभाग जाँच लेना चाहिए।"),
    "hook": "घी-तिल-नमक वाली = स्नेहनी (चिकना); श्यामाक + कुश-आमलक का क्वाथ = विरुक्षणी (रूखा)।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which yavāgū does verse 26 call oleating (स्नेहनी)?",
            ("The one with ghee, much sesame and salt",
             "सर्पिष्मती बहुतिला स्नेहनी लवणान्विता: ghee, much sesame and salt make it oleating."),
            [("The one of śyāmāka in kuśa-āmalaka decoction", "That one is drying (विरुक्षणी)."),
             ("The one cooked in boar broth", "That one is nourishing and belongs to verse 25."),
             ("The one cooked in buttermilk with viḍaṅga", "That one is worm-destroying and belongs to verse 23.")],
            "The first line gives the oleating gruel.",
            "Verse 26: ghee + sesame + salt = oleating."),
        match(1, "Match each word of verse 26 to its meaning.",
              [["स्नेहनी", "oleating"], ["विरुक्षणी", "drying"],
               ["सर्पिष्मती", "with ghee"], ["बहुतिला", "with much sesame"]],
              "Two effect words and two ingredient words.",
              "स्नेहनी = oleating; विरुक्षणी = drying; सर्पिष्मती = with ghee; बहुतिला = with much sesame."),
        fill(2, "The millet named in the drying gruel is ____ (type it in Devanagari).",
             ["श्यामाक", "श्यामाकानां", "श्यामाकानाम्", "श्यामाका"],
             "The second line says श्यामाकानां, 'of śyāmāka (millet)'.",
             "श्यामाकानां is the genitive plural of श्यामाक: 'of śyāmāka', the grain whose gruel is drying.",
             "श्यामाक = millet; its gruel is drying here."),
        mcq("discriminate", 3, "Which is the right split of लवणान्विता?",
            ("लवण + अन्विता",
             "अ + अ joins to आ, so लवण ('salt') + अन्विता ('accompanied') is written लवणान्विता."),
            [("लवणः + अन्विता", "A visarga after अ before अ would be written लवणोऽन्विता."),
             ("लवणा + न्विता", "न्विता is not a word."),
             ("लवण + नन्विता", "नन्विता is not a word.")],
            "लवणान्विता = 'accompanied by salt'.",
            "अ + अ → आ: लवण + अन्विता = लवणान्विता."),
        multi("apply", 4, "Which of these make the oleating gruel in verse 26?",
              [("घी", "Right: सर्पिष्मती, with ghee."),
               ("तिल", "Right: बहुतिला, with much sesame."),
               ("नमक", "Right: लवणान्विता, accompanied by salt."),
               ("श्यामाक", "Śyāmāka belongs to the drying gruel."),
               ("आमलक", "Āmalaka belongs to the drying gruel.")],
              [0, 1, 2],
              "Line 1 gives the oleating ingredients; line 2 gives the drying gruel.",
              "Oleating: ghee, sesame, salt. Drying: śyāmāka in kuśa-āmalaka decoction."),
        mcq("transfer", 5,
            "An invented word बहुघृता follows the pattern of बहुतिला. What does it describe? (घृत = ghee)",
            ("A gruel with much ghee",
             "बहु- + noun in a joined word = 'having much X'."),
            [("A gruel with no ghee", "बहु- means 'much', not 'none'."),
             ("A gruel cooked in a decoction of ghee", "That meaning would need a locative like -निर्यूहे."),
             ("A gruel that destroys ghee", "Destroying would need -घ्नी.")],
            "बहुतिला = with much sesame; बहुघृता = with much ghee.",
            "बहु- + noun (feminine) = 'with much X'.",
            teaches="बहु- + noun in a feminine joined word describes a gruel 'with much' of that thing."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "दशमूलीशृता कासहिक्काश्वासकफापहा",
    "question": "What does the yavāgū cooked with the ten roots remove, and what does the madirā one remove?",
    "rule": ("The one cooked with the ten roots removes cough, hiccup, "
             "breathlessness and Kapha; the one in yamaka cooked with "
             "madirā removes pain of the pakvāśaya (lower gut)."),
    "limits": ("यवागू is understood from earlier verses. The data does not "
               "define yamaka and says that the syntax of 'yamake "
               "madirāsiddhā' could be taken differently. The verse does "
               "not list the ten roots."),
    "explain_hi": ("पहली पंक्ति: दशमूल के साथ ‘शृता’ (पकी हुई) यवागू खाँसी (कास), "
                   "हिचकी (हिक्का), श्वास और कफ को दूर करती है (‘-अपहा’ = दूर करने "
                   "वाली)। दूसरी पंक्ति: ‘यमक’ में ‘मदिरासिद्धा’ (मदिरा के साथ पकी) "
                   "पक्वाशय की पीड़ा दूर करती है। यमक क्या है, यह पाठ नहीं बताता और उस "
                   "पद का वाक्य-विन्यास दूसरी तरह भी पढ़ा जा सकता है। सन्धि: कफ + अपहा = "
                   "कफापहा; रुजा + अपहा = रुजापहा (अ/आ + अ → आ)।"),
    "hook": "दशमूल की यवागू = कास-हिक्का-श्वास-कफ हर; यमक में मदिरा से पकी = पक्वाशय-शूल हर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does the yavāgū cooked with madirā remove, in line 2 of verse 27?",
            ("Pain of the pakvāśaya (lower gut)",
             "पक्वाशयरुजापहा: removing pain of the lower gut."),
            [("Cough and hiccup", "Those belong to the ten-roots gruel in line 1."),
             ("Thirst", "Thirst is in verse 24."),
             ("Worms", "Worms are in verse 23.")],
            "The second line pairs madirā with pakvāśaya pain.",
            "Verse 27 line 2: madirā-cooked gruel removes lower-gut pain."),
        match(1, "Match each word of verse 27 to its meaning.",
              [["कास", "cough"], ["हिक्का", "hiccup"],
               ["श्वास", "breathlessness"], ["मदिरा", "spirituous drink"]],
              "Three conditions of line 1 and one cooking substance of line 2.",
              "कास = cough; हिक्का = hiccup; श्वास = breathlessness; मदिरा = spirituous drink."),
        fill(2, "The part of the body whose pain the second gruel removes is the ____ (type the Devanagari word before रुजा).",
             ["पक्वाशय"],
             "पक्वाशयरुजापहा = पक्वाशय + रुजा + अपहा, 'removing pain of the pakvāśaya'.",
             "The data glosses पक्वाशय as the lower gut; रुजा is 'pain'.",
             "पक्वाशय = lower gut."),
        mcq("discriminate", 3, "Which is the right split of कफापहा?",
            ("कफ + अपहा",
             "अ + अ joins to आ, so कफ + अपहा is written कफापहा ('removing Kapha')."),
            [("कफा + पहा", "पहा is not a word."),
             ("कफः + अपहा", "A visarga after अ before अ would be written कफोऽपहा."),
             ("कफे + अपहा", "ए + अ is written कफेऽपहा; the word here is कफ.")],
            "कफ is the last item of the first compound; अपहा means 'removing'.",
            "अ + अ → आ: कफ + अपहा = कफापहा."),
        multi("apply", 4, "Which does the ten-roots yavāgū of verse 27 remove?",
              [("कास", "Right: cough."),
               ("हिक्का", "Right: hiccup."),
               ("श्वास", "Right: breathlessness."),
               ("पक्वाशय की पीड़ा", "That belongs to the madirā gruel."),
               ("पिपासा", "Thirst is in verse 24.")],
              [0, 1, 2],
              "Line 1 names cough, hiccup, breathlessness and Kapha.",
              "Ten roots: cough, hiccup, breathlessness, Kapha."),
        mcq("transfer", 5,
            "An invented compound is ज्वरतृष्णापहा, like कासहिक्काश्वासकफापहा. What does it say? (ज्वर = fever, तृष्णा = thirst)",
            ("Removing fever and thirst",
             "A string of nouns + अपहा = removing all of them."),
            [("Removing only fever", "तृष्णा is also in the compound and is removed."),
             ("Removing neither", "अपहा means 'removing'."),
             ("Bringing fever and thirst", "अपहा is 'removing', not 'bringing'.")],
            "In the verse four conditions come before अपहा and all are removed.",
            "N1 + N2 + ... + अपहा = removing all of N1, N2 ...",
            teaches="Nouns joined before अपहा are all removed; ā/a + a joins to ā (तृष्णा + अपहा = तृष्णापहा)."),
    ],
}

NOTES_HI = {
    "19": "‘दधित्थबिल्वचाङ्गेरीतक्रदाडिमसाधिता’ को एक समास पढ़ा गया है (पाँच वस्तुएँ + साधिता)। ‘सवाते’ = स + वाते, बहुव्रीहि सप्तमी एकवचन ‘वात के होने पर’। ‘पाञ्चमूलिकी’ में पाँच मूल कौन से हैं, श्लोक में अनिर्दिष्ट है। विषय (पेया) पिछले श्लोकों से चला आता है। पाठभेद या पाठ-दोष इस श्लोक में दर्ज नहीं हैं।",
    "20": "‘विल्वैः’ वही है जो बिल्व है; छपे पाठ में ‘विल्व’ है। ‘दाडिमाम्ला’ = दाडिम + अम्ला (अ + अ → आ); ‘पित्तश्लेष्मातिसारिणाम्’ = पित्त + श्लेष्म + अतिसारिणाम्; ‘पृश्निपर्ण्या’ = पृश्निपर्णी + आ (ई → य्)। टिप्पणी: समास का अर्थ ‘पित्त और कफ से जुड़ा अतिसार’ भी लिया जा सकता है; भाव समान है।",
    "21": "‘च्छागे’ में छ का द्वित्व वैकल्पिक सन्धि है (दीर्घ ‘ए’ के बाद), मूल शब्द ‘छागे’ है; ‘पयस्यर्धोदके’ = पयसि + अर्धोदके (इ → य्) और अर्ध + उदके (अ + उ → ओ)। ‘अर्धोदके’ दूध का विशेषण भी हो सकता है, भाव वही। ‘उत्पल’ अनिर्दिष्ट पौधा है (कई पौधे इस नाम से हैं)।",
    "22": "‘दद्यात्’ दोनों आधों पर लगता है; दूसरे आधे में ‘साधिताम्’ अनकहा समझा गया है। संस्करण में पाठान्तर ‘पेयामामे’ दर्ज है (‘पेयां सामे’ की जगह)। ‘साम्लाम्’ में कौन सी खटाई है, श्लोक नहीं बताता। ‘सामे’ = स + आमे, बहुव्रीहि सप्तमी: ‘आम होने पर’।",
    "23": "‘शिग्रुभिर्मरिचेन’ = शिग्रुभिः + मरिचेन (इः + घोष → इर्)। ‘पिप्पलीमूल’ एक वस्तु (पिप्पली की जड़) भी पढ़ी जा सकती है और दो भी, इसलिए गिनती नहीं ली गई। ‘क्रिमिघ्नी’ में ‘क्रिमि’ की वर्तनी पाठ के अनुसार है (प्रचलित ‘कृमि’)। गङ्गाधर के मत में यहाँ जल की जगह तक्र समझा जाए। ‘सुवर्चिका’ की पहचान अनिश्चित है।",
    "24": "छपा पाठ ‘-सारिवालज-’ है; सन्धि के अनुसार ‘सारिवा + लाज’ में ‘सारिवालाज’ होना चाहिए, इसलिए सम्भावित भूल दर्ज है (छन्द अप्रभावित)। ‘च’ दोनों वाक्य-खण्डों को जोड़ता है। सोमराजी और सारिवा नाम के रूप में ही रखे गए हैं।",
    "25": "‘यवागूर्बृंहणी’ = यवागूः + बृंहणी (ऊः + घोष → ऊर्)। दूसरी पंक्ति में ‘यवागू’ अनकहा समझा गया है। ‘निर्यूह’ = क्वाथ/शोरबा। ‘गवेधुक’ की पहचान श्लोक में नहीं है। ‘मता’ (मानी गई) का क्रिया-रूप: ‘मन्’ धातु का भूतकालिक कृदन्त, स्त्रीलिङ्ग।",
    "26": "स्रोत में एक अवांछित ‘&’ चिह्न का संकेत मिला और हटाया गया; शब्द-विभाग जाँच लेना चाहिए। ‘कुशामलक’ को कुश + आमलक पढ़ा गया है (अ + आ → आ), पर यह एक नाम भी हो सकता है। ‘लवणान्विता’ = लवण + अन्विता (अ + अ → आ)। ‘सर्पिष्मती’ और ‘बहुतिला’ स्त्रीलिङ्ग विशेषण हैं, यवागू के।",
    "27": "‘कासहिक्काश्वासकफापहा’ = कास + हिक्का + श्वास + कफ + अपहा (अ + अ → आ); अन्तिम पद ‘कफ’ है। ‘यमके’ का अर्थ पाठ में परिभाषित नहीं है और ‘यमके मदिरासिद्धा’ का अन्वय दूसरी तरह भी लिया जा सकता है। ‘पक्वाशयरुजापहा’ में रुजा + अपहा = रुजापहा।",
}

AIDS = {
    "19": {
        "frame": "क्या: पेया (पतली) · किसके साथ पकी: दधित्थ, बिल्व, चाङ्गेरी, तक्र, दाडिम · गुण: पाचनी, ग्राहिणी · वात हो तो: पाञ्चमूलिकी।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["दधित्थबिल्वचाङ्गेरीतक्रदाडिमसाधिता"]},
            {"label": "दूसरी पंक्ति",
             "items": ["पाचनी", "ग्राहिणी", "पेया", "सवाते", "पाञ्चमूलिकी"]}]},
        "letters": "द-बि-चा-त-दा: दधित्थ, बिल्व, चाङ्गेरी, तक्र, दाडिम।",
        "pegs": "मेरा बनाया चित्र: एक हाँडी में कैथ, बेल का फल, खट्टी पत्ती, छाछ का लोटा और अनार; ऊपर लिखा ‘पाचन + पकड़’। (केवल याद के लिए।)",
        "chunks": "दधित्थबिल्वचाङ्गेरी | तक्रदाडिमसाधिता ‖ पाचनी ग्राहिणी | पेया सवाते पाञ्चमूलिकी।",
    },
    "20": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["शालपर्णीबलाविल्वैः", "पृश्निपर्ण्या", "च", "साधिता"]},
            {"label": "दूसरी पंक्ति",
             "items": ["दाडिमाम्ला", "हिता", "पेया", "पित्तश्लेष्मातिसारिणाम्"]}]},
        "frame": "क्या: पेया · किसके साथ: शालपर्णी, बला, बिल्व, पृश्निपर्णी · खटाई: अनार · किसके लिए: पित्त-कफ के अतिसार वालों के लिए, हितकर।",
        "sandhi": "अ + अ → आ: दाडिम + अम्ला → दाडिमाम्ला · अ + अ → आ: श्लेष्म + अतिसारिणाम् → श्लेष्मातिसारिणाम् · ई → य् (स्वर से पहले): पृश्निपर्णी + आ → पृश्निपर्ण्या।",
        "contrast": "विल्वैः (तृतीया बहुवचन) ↔ पृश्निपर्ण्या (तृतीया एकवचन)।",
        "chunks": "शालपर्णीबलाविल्वैः | पृश्निपर्ण्या च साधिता ‖ दाडिमाम्ला हिता पेया | पित्तश्लेष्मातिसारिणाम्।",
    },
    "21": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["पयस्यर्धोदके", "च्छागे", "ह्रीवेरोत्पलनागरैः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["पेया", "रक्तातिसारघ्नी", "पृश्निपर्ण्या", "च", "साधिता"]}]},
        "frame": "किसमें: बकरी का दूध (आधा जल) · किसके साथ: ह्रीवेर, उत्पल, सोंठ; और पृश्निपर्णी · फल: रक्तातिसार-नाशक।",
        "sandhi": "इ → य् (स्वर से पहले): पयसि + अर्धोदके → पयस्यर्धोदके · अ + उ → ओ: अर्ध + उदके → अर्धोदके; ह्रीवेर + उत्पल → ह्रीवेरोत्पल · छ का द्वित्व (वैकल्पिक): छागे → च्छागे।",
        "pegs": "मेरा बनाया चित्र: बकरी, आधा भरा जल का घड़ा और दूध का कटोरा; पास में तीन पुड़ियाँ (ह्रीवेर, उत्पल, सोंठ)। (केवल याद के लिए।)",
        "chunks": "पयस्यर्धोदके च्छागे | ह्रीवेरोत्पलनागरैः ‖ पेया रक्तातिसारघ्नी | पृश्निपर्ण्या च साधिता।",
    },
    "22": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति (आम)",
             "items": ["दद्यात्", "सातिविषां", "पेयां", "सामे", "साम्लां", "सनागराम्"]},
            {"label": "दूसरी पंक्ति (मूत्रकृच्छ्र)",
             "items": ["श्वदंष्ट्राकण्टकारीभ्यां", "मूत्रकृच्छ्रे", "सफाणिताम्"]}]},
        "frame": "क्या: पेया, ‘दद्यात्’ (देनी चाहिए) · आम में: अतिविषा, खटाई, सोंठ · मूत्रकृच्छ्र में: श्वदंष्ट्रा, कण्टकारी, फाणित।",
        "sandhi": "अ + आ → आ: स + आमे → सामे · स- = ‘के साथ’: सातिविषाम्, साम्लाम्, सनागराम्, सफाणिताम्।",
        "chunks": "दद्यात् सातिविषां पेयां | सामे साम्लां सनागराम् ‖ श्वदंष्ट्राकण्टकारीभ्यां | मूत्रकृच्छ्रे सफाणिताम्।",
    },
    "23": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["विडङ्गपिप्पलीमूलशिग्रुभिर्मरिचेन", "च"]},
            {"label": "दूसरी पंक्ति",
             "items": ["तक्रसिद्धा", "यवागूः", "स्यात्", "क्रिमिघ्नी", "ससुवर्चिका"]}]},
        "frame": "क्या: यवागू (गाढ़ी) · किसमें पकी: तक्र · किसके साथ: विडङ्ग, पिप्पलीमूल, शिग्रु, मरिच, सुवर्चिका · फल: क्रिमिघ्नी।",
        "sandhi": "इः + घोष → इर्: शिग्रुभिः + मरिचेन → शिग्रुभिर्मरिचेन · स- = ‘के साथ’: स + सुवर्चिका → ससुवर्चिका।",
        "chunks": "विडङ्गपिप्पलीमूलशिग्रुभिर्मरिचेन च ‖ तक्रसिद्धा यवागूः स्यात् | क्रिमिघ्नी ससुवर्चिका।",
        "pegs": "मेरा बनाया चित्र: छाछ की हाँडी में विडङ्ग, पिप्पली, शिग्रु, मरिच और कृमि भागते हुए। (केवल याद के लिए।)",
    },
    "24": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["मृद्वीकासारिवालजपिप्पलीमधुनागरैः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["पिपासाघ्नी", "विषघ्नी", "च", "सोमराजीविपाचिता"]}]},
        "contrast": "पिपासाघ्नी: मृद्वीका, सारिवा, लाज (पाठ संदिग्ध), पिप्पली, मधु, नागर ↔ विषघ्नी: सोमराजी।",
        "letters": "मृ-सा-पि-म-ना: मृद्वीका, सारिवा, पिप्पली, मधु, नागर (पहले अक्षर; लाज छोड़ा गया क्योंकि पाठ वहाँ संदिग्ध है)।",
        "chunks": "मृद्वीकासारिवालज | पिप्पलीमधुनागरैः ‖ पिपासाघ्नी विषघ्नी च | सोमराजीविपाचिता।",
    },
    "25": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["सिद्धा", "वराहनिर्यूहे", "यवागूर्बृंहणी", "मता"]},
            {"label": "दूसरी पंक्ति",
             "items": ["गवेधुकानां", "भृष्टानां", "कर्शनीया", "समाक्षिका"]}]},
        "seesaw": "बृंहणी (पुष्टि करने वाली, वराह-निर्यूह में पकी) ↔ कर्शनीया (दुबला करने वाली, भुने गवेधुक की, मधु सहित)।",
        "sandhi": "ऊः + घोष → ऊर्: यवागूः + बृंहणी → यवागूर्बृंहणी · स- = ‘के साथ’: स + माक्षिका → समाक्षिका।",
        "pegs": "मेरा बनाया चित्र: एक पलड़े में सूअर का शोरबा, दूसरे में भुना गवेधुक और शहद। (केवल याद के लिए।)",
        "chunks": "सिद्धा वराहनिर्यूहे | यवागूर्बृंहणी मता ‖ गवेधुकानां भृष्टानां | कर्शनीया समाक्षिका।",
    },
    "26": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["सर्पिष्मती", "बहुतिला", "स्नेहनी", "लवणान्विता"]},
            {"label": "दूसरी पंक्ति",
             "items": ["कुशामलकनिर्यूहे", "श्यामाकानां", "विरुक्षणी"]}]},
        "seesaw": "स्नेहनी (चिकना करने वाली: घी, बहुत तिल, नमक) ↔ विरुक्षणी (रूखा करने वाली: श्यामाक, कुश-आमलक का निर्यूह)।",
        "sandhi": "अ + अ → आ: लवण + अन्विता → लवणान्विता · अ + आ → आ: कुश + आमलक → कुशामलक (दो नाम पढ़े गए)।",
        "chunks": "सर्पिष्मती बहुतिला | स्नेहनी लवणान्विता ‖ कुशामलकनिर्यूहे | श्यामाकानां विरुक्षणी।",
    },
    "27": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["दशमूलीशृता", "कासहिक्काश्वासकफापहा"]},
            {"label": "दूसरी पंक्ति",
             "items": ["यमके", "मदिरासिद्धा", "पक्वाशयरुजापहा"]}]},
        "frame": "पहली: दशमूल में पकी → कास, हिक्का, श्वास, कफ दूर · दूसरी: यमक में, मदिरा से पकी → पक्वाशय की पीड़ा दूर।",
        "sandhi": "अ + अ → आ: कफ + अपहा → कफापहा · आ + अ → आ: रुजा + अपहा → रुजापहा।",
        "chunks": "दशमूलीशृता | कासहिक्काश्वासकफापहा ‖ यमके मदिरासिद्धा | पक्वाशयरुजापहा।",
    },
}

IMAGE_SPECS = {
    ("22", "diagram"): {
        "file": "ch2-peya-22.svg",
        "alt": "Table of verse 22: in the condition with aama, gruel with ativisha, a sour ingredient and dry ginger; in painful urination, gruel with shvadamshtra and kantakari and with phanita.",
        "type": "table",
        "title": "दो स्थितियाँ, दो पेया",
        "heads": ["स्थिति", "पेया"],
        "rows": [["सामे (आम)", "सातिविषां · साम्लां · सनागराम्"],
                 ["मूत्रकृच्छ्रे", "श्वदंष्ट्रा · कण्टकारी · सफाणिताम्"]],
    },
    ("24", "contrast"): {
        "file": "ch2-yavagu-24.svg",
        "alt": "Two columns from verse 24: thirst-removing gruel with grapes, sarivaa, parched rice (reading doubtful), long pepper, honey and dry ginger; poison-destroying gruel with somaraji.",
        "type": "split",
        "title": "प्यास और विष",
        "cols": [["पिपासाघ्नी", ["मृद्वीका", "सारिवा", "लाज (पाठ संदिग्ध)", "पिप्पली", "मधु", "नागर"]],
                 ["विषघ्नी", ["सोमराजी"]]],
    },
    ("26", "seesaw"): {
        "file": "ch2-yavagu-26.svg",
        "alt": "Two columns from verse 26: oleating gruel with ghee, much sesame and salt; drying gruel of shyamaka in a decoction of kusha and amalaka.",
        "type": "split",
        "title": "स्नेहनी और विरुक्षणी",
        "cols": [["स्नेहनी", ["सर्पिष्मती (घी)", "बहुतिला (तिल)", "लवणान्विता (नमक)"]],
                 ["विरुक्षणी", ["श्यामाकानां", "कुशामलकनिर्यूहे"]]],
    },
}
