from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "शाकैर्मांसैस्तिलैर्माषैः सिद्धा",
    "question": "What do the two gruels of verse 28 do, one cooked with vegetables, meats, sesame and black gram, the other with the jambu-mango-bilva group?",
    "rule": ("Cooked with vegetables, meats, sesame and black gram, the gruel "
             "expels the stool (वर्चो निरस्यति); cooked with the jambu, mango, "
             "wood-apple, sour and bilva group, it is considered binding "
             "(साङ्ग्राहिकी)."),
    "limits": ("यवागू is understood, not written. No dose is given. The "
               "line-2 compound can be split two ways (stones of jambu and "
               "mango, or jambu and mango stone), and amla may be a separate "
               "sour item or a describing word; the card does not decide."),
    "explain_hi": ("यह श्लोक दो उल्टे असर वाली यवागूएँ एक साथ रखता है। पहली पंक्ति: "
                   "शाक, मांस, तिल और माष के साथ पकाई हुई (यवागू) मल को बाहर "
                   "निकालती है। दूसरी पंक्ति: जामुन, आम की गुठली, कैथ, खट्टे द्रव्य "
                   "और बिल्व के साथ पकाई हुई ‘साङ्ग्राहिकी’ मानी गई है, यानी मल को "
                   "रोकने वाली। ‘शाकैः, मांसैः, तिलैः, माषैः’ तृतीया बहुवचन हैं: "
                   "‘इन-इन के साथ’। ‘सिद्धा’ और ‘साङ्ग्राहिकी’ स्त्रीलिङ्ग हैं, जो बताते "
                   "हैं कि अनकहा कर्ता यवागू (स्त्रीलिङ्ग) है।"),
    "hook": "शाक-मांस-तिल-माष = मल निकाले · जामुन-आम-कैथ-बिल्व = मल रोके।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 28, line 1, a gruel is cooked with vegetables, meats, sesame and black gram. What does it do?",
            ("It expels the stool",
             "The line ends वर्चो निरस्यति: it expels the stool."),
            [("It binds the stool",
              "Binding is the effect of the second-line gruel, साङ्ग्राहिकी."),
             ("It destroys hunger",
              "Destroying hunger is said of the gruel in verse 33."),
             ("It removes cough and hiccup",
              "That is said of the gruel with the ten roots in verse 27.")],
            "वर्चः is the stool and निरस्यति means 'expels': the first gruel clears the stool out.",
            "Vegetables, meats, sesame, black gram: stool expelled."),
        match(1, "Match each ingredient word of line 1 to its meaning.",
              [["शाकैः", "with vegetables"], ["मांसैः", "with meats"],
               ["तिलैः", "with sesame"], ["माषैः", "with black gram"]],
              "The four words are all instrumental plurals: the things the gruel is cooked with.",
              "शाकैः = with vegetables; मांसैः = with meats; तिलैः = with sesame; माषैः = with black gram."),
        fill(2, "The word for 'binding' in line 2 is ____ (type it in Devanagari).",
             ["साङ्ग्राहिकी", "सांग्राहिकी"],
             "Line 2 calls the second gruel साङ्ग्राहिकी, binding.",
             "साङ्ग्राहिकी ends in -ई, feminine, agreeing with the understood word यवागू (feminine). It names the effect: the gruel holds the stool.",
             "साङ्ग्राहिकी = binding."),
        mcq("discriminate", 3, "Which is the right split of वर्चो निरस्यति?",
            ("वर्चः + निरस्यति: the visarga after अ becomes ओ before the voiced न",
             "अः before a voiced consonant gives ओ, so वर्चः + निरस्यति is written वर्चो निरस्यति."),
            [("वर्च + ओ निरस्यति",
              "There is no separate word ओ here."),
             ("वर्चर् + निरस्यति",
              "The visarga becomes र् after other vowels; after short अ it becomes ओ."),
             ("वर्चः + अनिरस्यति",
              "That would give वर्चोऽनिरस्यति, and अनिरस्यति is not the verb in the verse.")],
            "वर्चो निरस्यति is वर्चः (stool, object) + निरस्यति (expels).",
            "अः + voiced consonant → ओ (after अ)."),
        mcq("apply", 4,
            "A gruel is cooked with jambu, mango, wood-apple, a sour item and bilva (the line-2 group). What is it considered?",
            ("Binding (साङ्ग्राहिकी)",
             "Line 2 says this group makes the gruel साङ्ग्राहिकी मता, considered binding."),
            [("Expelling the stool",
              "That is the gruel of line 1, with vegetables, meats, sesame and black gram."),
             ("Aphrodisiac",
              "Being vṛṣya is said of a gruel in verse 32."),
             ("Good for the throat",
              "Being good for the throat is said of a gruel in verse 31.")],
            "मता is 'is considered'; the line 2 gruel is considered binding.",
            "Line 2 group → binding."),
        mcq("transfer", 5,
            "An invented phrase says मुद्गैः सिद्धा (मुद्ग = green gram). By the pattern of शाकैः सिद्धा, what does मुद्गैः tell us?",
            ("The gruel is cooked with green grams",
             "The ending -ऐः (instrumental plural) means 'with', as in शाकैः 'with vegetables'."),
            [("The gruel is cooked in the broth of green gram only",
              "'Broth' would need a word like रसैः; मुद्गैः names the grains themselves."),
             ("Green gram is the effect the gruel has",
              "Effects are named by words like निरस्यति or साङ्ग्राहिकी."),
             ("Green gram is the person who cooks it",
              "The cook is not named; -ऐः marks what it is cooked with.")],
            "A word in -ऐः beside सिद्धा names what the gruel is cooked with.",
            "X-ऐः सिद्धा = cooked with X.",
            teaches="A plural in -ऐः before सिद्धा lists the ingredients 'with' which the gruel is cooked."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "क्षारचित्रकहिङ्ग्वम्लवेतसैर्भेदिनी मता",
    "question": "What do the two gruels of verse 29 do, one cooked with alkali-citraka-asafoetida-amlavetasa, the other with abhayā-pippalī root-dry ginger?",
    "rule": ("With alkali, citraka, asafoetida and amlavetasa the gruel is "
             "considered bhedinī (purgative, loosening); with abhayā, long-"
             "pepper root and dry ginger it is vātānulomanī (moving Vāta in "
             "its proper course)."),
    "limits": ("यवागू is understood, not written. The verse gives no dose and "
               "does not say how the drugs act. The edition records a "
               "variant '-bilvai-' at the end of line 2; the data calls "
               "it a guess that it replaces -viśvair-, so no question rests "
               "on it."),
    "explain_hi": ("पिछले श्लोक की तरह यहाँ भी दो यवागूएँ हैं, पर असर दूसरे हैं। "
                   "क्षार, चित्रक, हींग और अम्लवेतस के साथ पकाई हुई ‘भेदिनी’ मानी गई "
                   "है, यानी भेदन करने वाली (ढीला कर निकालने वाली)। अभया (हरीतकी), "
                   "पिप्पलीमूल और सोंठ (विश्व) के साथ पकाई हुई ‘वातानुलोमनी’ है, "
                   "यानी वात को उसकी ठीक दिशा में चलाने वाली। ‘भेदिनी’ और "
                   "‘वातानुलोमनी’ स्त्रीलिङ्ग हैं, इसलिए अनकहा कर्ता यवागू है। "
                   "सन्धि: हिङ्गु + अम्ल → हिङ्ग्वम्ल; वात + अनुलोमनी → वातानुलोमनी।"),
    "hook": "क्षार-चित्रक-हींग-अम्लवेतस = भेदिनी · अभया-पिप्पलीमूल-सोंठ = वातानुलोमनी।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "A gruel is cooked with alkali, citraka, asafoetida and amlavetasa. What does verse 29 call it?",
            ("Bhedinī: purgative, loosening",
             "Line 1 ends भेदिनी मता: considered bhedinī."),
            [("Sāṅgrāhikī: binding",
              "Binding is the effect of the second gruel of verse 28."),
             ("A remover of the ill effects of ghee",
              "That is said of the gruel cooked in buttermilk in verse 30."),
             ("Vṛṣyā: aphrodisiac",
              "That is said of a gruel in verse 32.")],
            "The first gruel of verse 29 is भेदिनी, considered to loosen and purge.",
            "Alkali, citraka, asafoetida, amlavetasa: bhedinī."),
        match(1, "Match each word of verse 29 to its meaning.",
              [["भेदिनी", "purgative, loosening"],
               ["वातानुलोमनी", "moving Vāta in its proper course"],
               ["हिङ्गु", "asafoetida"],
               ["अभया", "harītakī (chebulic myrobalan)"]],
              "Two of these are effects, two are drugs named in the verse.",
              "भेदिनी = purgative; वातानुलोमनी = moving Vāta in its proper course; हिङ्गु = asafoetida; अभया = harītakī."),
        fill(2, "Type the Devanagari word for dry ginger in the instrumental plural (meaning with dry ginger): ____.",
             ["विश्वैः", "विश्वैर्"],
             "Line 2 names dry ginger as विश्वैः, the last of its three drugs.",
             "विश्वैः ends in -ऐः, the instrumental plural: 'with'. It is the same ending as शाकैः and तिलैः in verse 28.",
             "विश्वैः = with dry ginger."),
        mcq("discriminate", 3, "Which is the right split of वातानुलोमनी?",
            ("वात + अनुलोमनी: अ + अ gives आ",
             "Two short अ-sounds join into long आ, so वात + अनुलोमनी is written वातानुलोमनी."),
            [("वाता + नुलोमनी", "नुलोमनी is not a word."),
             ("वात + आनुलोमनी", "आनुलोमनी is not the word; the word is अनुलोमनी."),
             ("वातः + अनुलोमनी", "That would be written वातोऽनुलोमनी, with ओऽ.")],
            "वातानुलोमनी = वात (Vāta) + अनुलोमनी (moving it along its proper course).",
            "वात + अनुलोमनी = वातानुलोमनी."),
        multi("apply", 4, "Which of these drugs does verse 29 itself name?",
              [("चित्रक", "Right: citraka is in line 1."),
               ("हिङ्गु", "Right: asafoetida is in line 1."),
               ("पिप्पलीमूल", "Right: long-pepper root is in line 2."),
               ("तिल", "Sesame is in verse 28, not here."),
               ("माष", "Black gram is in verse 28, not here.")],
              [0, 1, 2],
              "Citraka, asafoetida and pippalī root are all in verse 29; sesame and black gram belong to verse 28.",
              "Verse 29 names citraka, asafoetida, pippalī root; sesame and māṣa are verse 28."),
        mcq("transfer", 5,
            "The understood subject यवागू is feminine. Which word fills the blank in an invented line ending ____ शृता, saying the gruel kindles appetite (दीपन)?",
            ("दीपनी",
             "A word describing a feminine यवागू ends in -ई or -आ; दीपनी fits, like भेदिनी in line 1."),
            [("दीपनः", "That is masculine and does not agree with यवागू."),
             ("दीपनम्", "That is neuter and does not agree with यवागू."),
             ("दीपी", "That is not a form agreeing with a feminine यवागू.")],
            "The describing words agree with the unwritten feminine subject यवागू.",
            "Feminine subject: describing word in -ई/-आ (भेदिनी, मता, दीपनी).",
            teaches="Words like सिद्धा, मता, भेदिनी all end in feminine forms because the understood subject, यवागू, is feminine."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "तक्रसिद्धा यवागूः स्याद्घृतव्यापत्तिनाशिनी",
    "question": "For which troubles does the verse recommend a gruel cooked in buttermilk, and one cooked with buttermilk and oil-cake?",
    "rule": ("A gruel cooked in buttermilk (तक्र) would remove the ill effects "
             "of ghee; one cooked with buttermilk and oil-cake (पिण्याक) is "
             "recommended in the ill effects of oil."),
    "limits": ("The verse says only which gruel is for which ill effect; it "
               "does not say how the ill effect arises. 'Vyāpad' is "
               "read as a mishap or disorder from improper use. Oil-cake is "
               "the residue left after pressing oil, as the data notes."),
    "explain_hi": ("इस श्लोक में यवागू का नाम पहली पंक्ति में खुलकर आता है: "
                   "‘तक्रसिद्धा यवागूः’। तक्र में पकाई हुई ‘घृतव्यापत्ति’ (घी से "
                   "हुए बिगाड़) को नष्ट करने वाली होगी। तक्र और पिण्याक (तेल "
                   "निकलने के बाद की खली) के साथ पकाई हुई ‘तैलव्यापद्’ (तेल से "
                   "हुए बिगाड़) में प्रशस्त है। ‘तैलव्यापदि’ में -इ सप्तमी है: "
                   "‘में’। सन्धि: स्यात् + घृत… → स्याद्घृत…; यहाँ त् घोष ‘घ’ से "
                   "पहले द् हो गया है।"),
    "hook": "तक्र = घी का बिगाड़ मिटाए · तक्र + खली = तेल के बिगाड़ में प्रशस्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "A gruel is cooked in buttermilk alone. Which trouble does verse 30 say it would remove?",
            ("The ill effects of ghee",
             "Line 1: तक्रसिद्धा यवागूः … घृतव्यापत्तिनाशिनी."),
            [("The ill effects of oil",
              "Oil's ill effects need buttermilk and oil-cake together (line 2)."),
             ("Irregular fever",
              "That is said of the broth gruel in verse 31."),
             ("Intoxication",
              "That is said of the gruel in verse 33.")],
            "घृतव्यापत्ति-नाशिनी = remover of the ill effects of ghee.",
            "Buttermilk-cooked gruel: ghee's ill effects."),
        match(1, "Match each phrase of verse 30 to its meaning.",
              [["तक्रसिद्धा", "cooked in buttermilk"],
               ["नाशिनी", "remover"],
               ["शस्ता", "recommended"],
               ["तक्रपिण्याकसाधिता", "cooked with buttermilk and oil-cake"]],
              "These four phrases carry the verse.",
              "तक्रसिद्धा = cooked in buttermilk; नाशिनी = remover; शस्ता = recommended; तक्रपिण्याकसाधिता = cooked with buttermilk and oil-cake."),
        fill(2, "The word for 'oil-cake' inside तक्रपिण्याकसाधिता is ____ (type it in Devanagari).",
             ["पिण्याक", "पिण्याकः", "पिण्याकम्"],
             "The compound is तक्र + पिण्याक + साधिता: buttermilk and oil-cake, cooked.",
             "In the compound तक्रपिण्याकसाधिता the first two parts are a pair (buttermilk and oil-cake) and साधिता is 'cooked'. The stem is पिण्याक.",
             "पिण्याक = oil-cake, the residue left after pressing oil."),
        mcq("discriminate", 3, "Which is the right split of स्याद्घृतव्यापत्तिनाशिनी?",
            ("स्यात् + घृतव्यापत्तिनाशिनी: त् becomes द् before the voiced घ",
             "A final त् turns into द् before a voiced consonant, so स्यात् + घृत… is written स्याद्घृत…."),
            [("स्या + द्घृतव्यापत्तिनाशिनी", "द्घृत… is not a word."),
             ("स्यः + घृतव्यापत्तिनाशिनी", "The verb is स्यात्, 'would be', not स्यः."),
             ("स्यात् + आघृतव्यापत्तिनाशिनी", "आघृत… is not a word in the verse.")],
            "स्यात् (would be) + घृतव्यापत्तिनाशिनी (remover of ghee's ill effects).",
            "त् → द् before a voiced consonant: स्यात् + घृत → स्याद्घृत."),
        mcq("apply", 4,
            "A gruel is cooked with buttermilk and oil-cake. For which trouble does the verse recommend it?",
            ("The ill effects of oil",
             "Line 2: तैलव्यापदि शस्ता स्यात् तक्रपिण्याकसाधिता."),
            [("The ill effects of ghee",
              "Ghee's ill effects go with the gruel cooked in buttermilk alone."),
             ("Pain in the lower gut",
              "That is said of the madirā gruel in verse 27."),
             ("Hunger",
              "Destroying hunger is said of a gruel in verse 33.")],
            "तैलव्यापदि = in the ill effects of oil; शस्ता = recommended.",
            "Buttermilk + oil-cake gruel: oil's ill effects."),
        mcq("transfer", 5,
            "An invented line ends मधुव्यापदि शस्ता (मधु = honey), built like तैलव्यापदि शस्ता. What does it say?",
            ("(A gruel) is recommended in the ill effects of honey",
             "The ending -इ on व्यापदि is 'in', and शस्ता is 'recommended'."),
            [("(A gruel) removes honey",
              "That would need a word like नाशिनी; शस्ता is 'recommended'."),
             ("(A gruel) is made from the ill effects of honey",
              "-इ marks 'in', not 'made from'."),
             ("Honey is cooked in buttermilk",
              "Nothing here mentions buttermilk or cooking.")],
            "X-व्यापदि शस्ता = recommended in the ill effects of X.",
            "व्यापदि = in the ill effects; शस्ता = recommended.",
            teaches="A locative in -इ before शस्ता names the trouble 'in' which the gruel is recommended."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "गव्यमांसरसैः साम्ला",
    "question": "What do the cow's-meat broth gruel and the barley gruel with long pepper and āmalaka do?",
    "rule": ("Cooked with broths of cow's meat and a sour item, the gruel "
             "destroys irregular fever (विषमज्वर); the barley gruel in yamaka "
             "cooked with long pepper and āmalaka is good for the throat "
             "(कण्ठ्या)."),
    "limits": ("The verse does not define yamaka, so no question rests on it. "
               "'Gavya-māṃsa' literally means cow/ox meat; commentators may "
               "read it differently. Kaṇṭhya is 'good for the throat' (or "
               "the voice); the verse says no more."),
    "explain_hi": ("पहली पंक्ति: गाय के मांस-रस के साथ और खट्टे द्रव्य सहित पकाई हुई "
                   "(यवागू) विषमज्वर का नाश करने वाली है। ‘साम्ला’ = ‘स’ + ‘अम्ला’, "
                   "यानी खट्टे द्रव्य के साथ; ‘स-’ का अर्थ यहाँ ‘सहित’ है। दूसरी "
                   "पंक्ति: जौ की यवागू, पिप्पली और आमलक के साथ पकाई हुई, "
                   "‘कण्ठ्या’ है, कण्ठ के लिए हितकर। ‘यमक’ श्लोक में परिभाषित नहीं "
                   "है, इसलिए उस पर कोई निष्कर्ष नहीं। सन्धि: पिप्पली + आमलकैः → "
                   "पिप्पल्यामलकैः।"),
    "hook": "गाय का मांस-रस + खट्टा = विषमज्वर नाश · जौ + पिप्पली + आमला = कण्ठ्या।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "A gruel is cooked with broths of cow's meat and a sour item. What does the verse say it destroys?",
            ("Irregular fever (विषमज्वर)",
             "Line 1: गव्यमांसरसैः साम्ला विषमज्वरनाशिनी."),
            [("Intoxication",
              "That is said of the gruel with upodikā and curd in verse 33."),
             ("Pain of the seminal passage",
              "That is said of the cock-broth gruel in verse 32."),
             ("The ill effects of ghee",
              "That is said of the buttermilk gruel in verse 30.")],
            "विषमज्वरनाशिनी = destroyer of irregular fever.",
            "Cow's-meat broth plus a sour item: irregular fever destroyed."),
        match(1, "Match each word of verse 31 to its meaning.",
              [["गव्यमांसरसैः", "with broths of bovine meat"],
               ["साम्ला", "with a sour ingredient"],
               ["कण्ठ्या", "good for the throat"],
               ["यवानाम्", "of barley"]],
              "These four phrases carry the verse.",
              "गव्यमांसरसैः = with broths of bovine meat; साम्ला = with a sour ingredient; कण्ठ्या = good for the throat; यवानाम् = of barley."),
        fill(2, "The word for 'good for the throat' is ____ (type it in Devanagari).",
             ["कण्ठ्या"],
             "Line 2 begins with कण्ठ्या.",
             "कण्ठ्या ends in feminine -आ, like सिद्धा and शृता, agreeing with the understood यवागू. It names the effect on the throat.",
             "कण्ठ्या = good for the throat."),
        mcq("discriminate", 3, "Which is the right split of पिप्पल्यामलकैः?",
            ("पिप्पली + आमलकैः: ई + आ becomes या",
             "Final ई before a different vowel turns into य्, so ई + आ gives य् + आ: पिप्पल्यामलकैः."),
            [("पिप्पल + यामलकैः", "यामलकैः is not a word."),
             ("पिप्पलिः + आमलकैः", "That would give पिप्पलिरामलकैः."),
             ("पिप्पली + अमलकैः", "That would be written पिप्पल्यमलकैः; the second word is आमलकैः.")],
            "पिप्पल्यामलकैः = पिप्पली (long pepper) + आमलकैः (with āmalaka).",
            "ई + different vowel → य् + vowel."),
        mcq("apply", 4,
            "The barley gruel that the verse calls good for the throat is cooked with which two items?",
            ("Long pepper and āmalaka",
             "Line 2: पिप्पल्यामलकैः शृता."),
            [("Sesame and black gram",
              "Those belong to the stool-expelling gruel of verse 28."),
             ("Alkali and citraka",
              "Those belong to the purgative gruel of verse 29."),
             ("Ghee and milk",
              "Those belong to the gruel of verse 32.")],
            "The two drugs of the throat gruel are long pepper (पिप्पली) and āmalaka.",
            "Throat gruel: barley, long pepper, āmalaka."),
        mcq("transfer", 5,
            "An invented phrase says सलवणा यवागूः, built like साम्ला. What does सलवणा say about the gruel?",
            ("It is cooked with salt",
             "The prefix स- here means 'with', as साम्ला means 'with a sour item'; लवण is salt."),
            [("It is without salt",
              "'Without' would need अ- or निर्; स- means 'with'."),
             ("It removes salt",
              "Removing would need a word like नाशिनी."),
             ("It is made of salt only",
              "स- does not mean 'only'; it means 'with'.")],
            "स- before a noun gives 'with' (साम्ला = with a sour item).",
            "सX-ā = with X.",
            teaches="A word starting with स- (as साम्ला) describes the gruel as 'with' that item."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "ताम्रचूडरसे सिद्धा",
    "question": "What does the cock-broth gruel remove, and which gruel does the verse call aphrodisiac?",
    "rule": ("A gruel cooked in the broth of the cock removes pain of the "
             "seminal passage (रेतोमार्गरुजापहा); one with split black gram, "
             "cooked with ghee and milk, is vṛṣyā (aphrodisiac, promoting "
             "virility)."),
    "limits": ("The verse gives no dose and does not say how either gruel "
               "acts. 'Tāmracūḍa' (copper-crested) is read as the cock, as "
               "the data glosses it; the word is not explained further. "
               "Retomārga is literally the passage of semen."),
    "explain_hi": ("पहली पंक्ति: ताम्रचूड (मुर्गे) के रस में पकाई हुई (यवागू) शुक्र-"
                   "मार्ग की पीड़ा को दूर करने वाली है। दूसरी पंक्ति: माष की दाल के "
                   "साथ, घी और दूध में पकाई हुई (यवागू) ‘वृष्या’ है, यानी वीर्य बढ़ाने "
                   "वाली। ‘सिद्धा’, ‘वृष्या’ स्त्रीलिङ्ग हैं और यवागू से जुड़ते हैं। सन्धि: "
                   "रेतस् + मार्ग → रेतोमार्ग; रुजा + अपहा → रुजापहा (आ + अ → आ); "
                   "क्षीर + उपसाधिता → क्षीरोपसाधिता (अ + उ → ओ)।"),
    "hook": "मुर्गे का रस = शुक्र-मार्ग की पीड़ा हरे · माष-दाल + घी + दूध = वृष्या।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "A gruel is cooked in the broth of the cock (ताम्रचूड). What does verse 32 say it removes?",
            ("Pain of the seminal passage",
             "Line 1: रेतोमार्गरुजापहा, remover of pain in the seminal passage."),
            [("Intoxication",
              "That is said of the upodikā-and-curd gruel in verse 33."),
             ("The ill effects of oil",
              "That is said of the buttermilk-and-oil-cake gruel in verse 30."),
             ("Irregular fever",
              "That is said of the cow's-meat broth gruel in verse 31.")],
            "रेतोमार्ग-रुजा-अपहा = remover of the pain of the seminal passage.",
            "Cock-broth gruel: pain of the seminal passage removed."),
        match(1, "Match each word of verse 32 to its meaning.",
              [["ताम्रचूडरसे", "in the broth of the cock"],
               ["वृष्या", "aphrodisiac, promoting virility"],
               ["समाषविदला", "with split black gram"],
               ["घृतक्षीर", "ghee and milk"]],
              "These phrases carry the two halves of the verse.",
              "ताम्रचूडरसे = in the cock's broth; वृष्या = aphrodisiac; समाषविदला = with split black gram; घृतक्षीर = ghee and milk."),
        fill(2, "The word for 'aphrodisiac, promoting virility' is ____ (type it in Devanagari).",
             ["वृष्या"],
             "Line 2 says वृष्या for the gruel with split black gram.",
             "वृष्या ends in feminine -आ, agreeing with the understood यवागू. It names the effect: the gruel promotes virility.",
             "वृष्या = aphrodisiac."),
        mcq("discriminate", 3, "Which is the right split of घृतक्षीरोपसाधिता?",
            ("घृतक्षीर + उपसाधिता: अ + उ becomes ओ",
             "Short अ and उ join into ओ, so क्षीर + उपसाधिता is written क्षीरोपसाधिता."),
            [("घृतक्षीरो + पसाधिता", "पसाधिता is not a word."),
             ("घृतक्षीर + ओपसाधिता", "ओपसाधिता is not a word; ओ is made by the joining."),
             ("घृतक्षीरः + उपसाधिता", "That would be written घृतक्षीर उपसाधिता, with no ओ.")],
            "घृत (ghee) + क्षीर (milk) + उपसाधिता (cooked with).",
            "अ + उ → ओ."),
        multi("apply", 4, "Which of these are named in verse 32 itself?",
              [("ताम्रचूडरस", "Right: the cock's broth opens the verse."),
               ("माषविदल", "Right: split black gram is in line 2."),
               ("घृत", "Right: ghee is in line 2."),
               ("दधि", "Curd is in verse 33."),
               ("अपामार्ग", "Apāmārga is in verse 33.")],
              [0, 1, 2],
              "The cock's broth, split māṣa and ghee are all here; curd and apāmārga come in verse 33.",
              "Verse 32: cock broth, split māṣa, ghee, milk. Curd and apāmārga are in verse 33."),
        mcq("transfer", 5,
            "Joining क्षीर and उदक (milk and water, invented) into one word by the same rule as क्षीर + उपसाधिता gives what?",
            ("क्षीरोदक",
             "अ at the end of क्षीर and उ at the start of उदक join into ओ."),
            [("क्षीरौदक", "औ is made from अ + ओ or अ + औ, not from अ + उ."),
             ("क्षीरूदक", "ऊ would come from उ + उ."),
             ("क्षीरुदक", "The joining always makes a new vowel; this leaves उ unchanged.")],
            "अ + उ → ओ, as in क्षीरोपसाधिता.",
            "अ + उ → ओ.",
            teaches="When a word ends in अ and the next starts with उ, they join into ओ."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "उपोदिकादधिभ्यां तु सिद्धा",
    "question": "What does the gruel with upodikā and curd destroy, and what would the one with apāmārga and the godhā's broth destroy?",
    "rule": ("Cooked with upodikā and curd, the gruel destroys intoxication "
             "(मद); cooked with apāmārga, milk and the broth of the godhā "
             "(monitor lizard), it would destroy hunger (क्षुधं हन्यात्)."),
    "limits": ("Upodikā is not explained by the data and no question rests "
               "on its identity. 'Apāmārgakṣīra' could mean milk of the "
               "apāmārga plant rather than apāmārga and milk; the plain "
               "reading is taken. The verse does not say whether the hunger "
               "meant is excessive hunger."),
    "explain_hi": ("पहली पंक्ति: उपोदिका और दही के साथ पकाई हुई (यवागू) मद (नशे) का "
                   "नाश करती है। ‘उपोदिकादधिभ्याम्’ में -भ्याम् द्विवचन है: दो "
                   "वस्तुएँ, उपोदिका और दही। दूसरी पंक्ति: अपामार्ग, दूध और गोधा "
                   "(गोह) के रस के साथ पकाई हुई (यवागू) भूख को नष्ट कर दे। ‘हन्यात्’ "
                   "विधिलिङ् है: ‘नष्ट करे / कर देगी’। ‘क्षुधम्’ द्वितीया है, यानी क्रिया का "
                   "कर्म। सन्धि: हन्यात् + अपामार्ग → हन्यादपामार्ग।"),
    "hook": "उपोदिका + दही = नशा नष्ट · अपामार्ग + दूध + गोधा-रस = भूख नष्ट।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "A gruel is cooked with upodikā and curd. What does verse 33 say it destroys?",
            ("Intoxication (मद)",
             "Line 1: सिद्धा मदविनाशिनी, destroyer of intoxication."),
            [("Hunger",
              "Hunger is destroyed by the apāmārga gruel of line 2."),
             ("Irregular fever",
              "That is said of the cow's-meat gruel in verse 31."),
             ("Cough and hiccup",
              "That is said of the ten-roots gruel in verse 27.")],
            "मद-विनाशिनी = destroyer of intoxication.",
            "Upodikā and curd gruel: intoxication destroyed."),
        match(1, "Match each word of verse 33 to its meaning.",
              [["मदविनाशिनी", "destroying intoxication"],
               ["क्षुधम्", "hunger"],
               ["हन्यात्", "would destroy"],
               ["गोधा", "monitor lizard"]],
              "These words carry the effects and one ingredient.",
              "मदविनाशिनी = destroying intoxication; क्षुधम् = hunger; हन्यात् = would destroy; गोधा = monitor lizard."),
        fill(2, "The word for 'hunger' in line 2 is ____ (type it in Devanagari).",
             ["क्षुधम्", "क्षुधं"],
             "Line 2 begins क्षुधं हन्यात्, 'would destroy hunger'.",
             "क्षुधम् ends in -म्, the accusative: hunger is what is destroyed, the object of हन्यात्.",
             "क्षुधम् = hunger (object of 'would destroy')."),
        mcq("discriminate", 3, "Which is the right split of हन्यादपामार्ग…?",
            ("हन्यात् + अपामार्ग…: त् becomes द् before a vowel",
             "A final त् turns into द् before a vowel as well as before a voiced consonant, so हन्यात् + अपामार्ग is written हन्यादपामार्ग."),
            [("हन्या + दपामार्ग…", "दपामार्ग… is not a word."),
             ("हन्यात् + आपामार्ग…", "आपामार्ग is not the word; the word is अपामार्ग."),
             ("हन्यः + अपामार्ग…", "The verb is हन्यात्, not हन्यः.")],
            "हन्यात् (would destroy) + अपामार्ग… (the next word begins with अपामार्ग).",
            "त् → द् before a vowel."),
        multi("apply", 4, "Which of these are named in line 2 of verse 33?",
              [("अपामार्ग", "Right: apāmārga opens the compound."),
               ("गोधारस", "Right: the broth of the godhā is in the compound."),
               ("क्षीर", "Right: milk is in the line-2 compound."),
               ("दधि", "Curd is in line 1, with upodikā."),
               ("उपोदिका", "Upodikā is in line 1.")],
              [0, 1, 2],
              "Line 2 names apāmārga, milk and godhā's broth; curd and upodikā belong to line 1.",
              "Line 2: apāmārga, milk, godhā-rasa. Line 1: upodikā, curd."),
        mcq("transfer", 5,
            "An invented line says तृषं हन्यात् (तृष् = thirst), built like क्षुधं हन्यात्. What does it say?",
            ("(It) would destroy thirst",
             "तृषम् is the object (what is destroyed) and हन्यात् is 'would destroy', as in क्षुधं हन्यात्."),
            [("Thirst would destroy (it)",
              "Thirst is in the object form, not the subject."),
             ("(It) destroys hunger",
              "The word is तृषम्, thirst, not क्षुधम्."),
             ("Thirst is destroyed by it",
              "Passive meaning would need a different verb form; हन्यात् is active.")],
            "Object in -म् + हन्यात् = 'would destroy that object'.",
            "X-म् हन्यात् = would destroy X.",
            teaches="An object in -म् before हन्यात् names what the gruel 'would destroy'."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "अष्टाविंशतिरित्येता यवाग्वः परिकीर्तिताः",
    "question": "What does the closing verse of the gruel list say about their number, and what does the compendium of remedies rest on?",
    "rule": ("Twenty-eight gruels have been enumerated (अष्टाविंशतिः यवाग्वः "
             "परिकीर्तिताः); the compendium of remedies has been stated, "
             "relying on the five karmas (पञ्चकर्माणि)."),
    "limits": ("The verse does not list the five karmas; the data keeps "
               "'pañcakarma' as written. It is a summary: it names no "
               "gruel and gives no dose. A lead-in 'tatra ślokaḥ' ('here "
               "is the verse') precedes it."),
    "explain_hi": ("यह यवागू-सूची का सारांश-श्लोक है; ‘तत्र श्लोकः’ (इस विषय में श्लोक) "
                   "इसके पहले आता है। पहली पंक्ति: ये अट्ठाईस यवागू कही जा चुकी हैं "
                   "(परिकीर्तिताः)। दूसरी पंक्ति: पाँच कर्मों का आश्रय लेकर औषधों का "
                   "संग्रह (भैषज्यसंग्रह) कहा गया है। पाँच कर्म श्लोक में गिनाए नहीं "
                   "गए। ‘आश्रित्य’ में आ- उपसर्ग है, इसलिए त्वा की जगह -य लगा (छोटे स्वर वाली धातु के बाद त् जुड़कर -त्य दिखता है)। "
                   "सन्धि: अष्टाविंशतिः + इति → अष्टाविंशतिरिति; प्र + उक्तः → प्रोक्तः।"),
    "hook": "२८ यवागू कही जा चुकीं · भैषज्य-संग्रह पाँच कर्मों के आश्रय से कहा गया।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 34 closes the gruel list. How many gruels does it say have been enumerated?",
            ("Twenty-eight",
             "The verse says अष्टाविंशतिः (twenty-eight) यवाग्वः परिकीर्तिताः."),
            [("Twenty-six", "The verse says अष्टाविंशतिः, which is twenty-eight."),
             ("Thirty-two", "The verse says twenty-eight, not thirty-two."),
             ("Eighteen", "The verse says twenty-eight, not eighteen.")],
            "अष्टाविंशतिः means twenty-eight, and यवाग्वः is 'gruels'.",
            "The verse sums up twenty-eight gruels."),
        match(1, "Match each word of verse 34 to its meaning.",
              [["यवाग्वः", "thick gruels"],
               ["परिकीर्तिताः", "have been enumerated"],
               ["पञ्चकर्माणि", "the five karmas"],
               ["भैषज्यसंग्रहः", "compendium of remedies"]],
              "These four words hold the content of the verse.",
              "यवाग्वः = gruels; परिकीर्तिताः = enumerated; पञ्चकर्माणि = the five karmas; भैषज्यसंग्रहः = compendium of remedies."),
        fill(2, "The word for 'the five karmas' (accusative plural) is ____ (type it in Devanagari).",
             ["पञ्चकर्माणि", "पंचकर्माणि"],
             "Line 2 begins with पञ्चकर्माणि, then cāśritya.",
             "पञ्चकर्माणि is पञ्च (five) + कर्म (action) joined as one word, neuter plural in -आणि: what the compendium relies on (आश्रित्य).",
             "पञ्चकर्माणि = the five karmas."),
        mcq("discriminate", 3,
            "Why does आश्रित्य end in -य (written -त्य) and not in -त्वा?",
            ("Because it has the prefix आ- before the root √श्रि",
             "An absolutive from a root with a prefix ends in -य (after a short-vowel root, written -त्य); without a prefix it ends in -त्वा."),
            [("Because it is a plural", "Absolutives do not change for number."),
             ("Because the verse is in the past", "Tense does not choose -य or -त्वा; the prefix does."),
             ("Because it follows the word च", "च is a separate word and does not affect the ending.")],
            "आश्रित्य = आ + श्रि + -य, 'having relied on' (the -य shows as -त्य after the short vowel); the prefix आ- brings -य.",
            "Root with prefix: absolutive in -य; without: -त्वा."),
        multi("apply", 4, "Which of these does verse 34 itself say?",
              [("Twenty-eight gruels have been enumerated", "Right: line 1."),
               ("The compendium of remedies was stated relying on the five karmas", "Right: line 2."),
               ("The five karmas are named one by one here", "The verse says only 'the five karmas'; it lists none."),
               ("Each gruel is given with its dose", "The verse gives no dose."),
               ("The gruels are all for fever", "Verse 34 names no disease at all.")],
              [0, 1],
              "Verse 34 gives the count of gruels and says what the compendium rests on; it names no karma, dose or disease.",
              "Verse 34: 28 gruels, and a compendium resting on the five karmas; nothing more."),
        mcq("transfer", 5,
            "By the rule seen in आश्रित्य, which is the right absolutive (having come) of √गम् with the prefix आ-?",
            ("आगत्य",
             "With a prefix the absolutive takes -य (shown as -त्य here), as in आश्रित्य; आ + गम् gives आगत्य."),
            [("आगत्वा", "-त्वा goes with a root without a prefix."),
             ("आगतम्", "That is a past participle, 'come', not 'having come'."),
             ("आगच्छति", "That is 'he comes', a present form.")],
            "Prefix + root → absolutive in -य.",
            "आ + √गम् → आगत्य.",
            teaches="Absolutives of prefixed roots take -य (shown as -त्य in आश्रित्य, आगत्य); without a prefix the ending is -त्वा."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "पूर्वं मूलफलज्ञानहेतोरुक्तम्",
    "question": "Why does the verse say the earlier medicine is told again?",
    "rule": ("The medicine stated earlier for knowing roots and fruits has "
             "been told again for the sake of knowledge resting on the five "
             "karmas."),
    "limits": ("The verse does not say where the earlier statement is; the "
               "data only suggests it is probably the root and fruit drug "
               "groups of an earlier chapter. It names no medicine and "
               "does not list the five karmas."),
    "explain_hi": ("यह श्लोक एक कारण बताता है: जो औषध पहले मूल और फल के ज्ञान के लिए "
                   "कही गई थी (पूर्वम् उक्तम्), वही अब पाँच कर्मों पर आश्रित ज्ञान के "
                   "लिए फिर से कही गई (कीर्तितं पुनः)। ‘हेतोः’ का अर्थ यहाँ ‘के लिए’ है "
                   "(षष्ठी या पञ्चमी रूप, ‘के प्रयोजन से’ जैसा प्रयोग)। श्लोक यह नहीं बताता "
                   "कि पहले वह कहाँ कही गई थी। सन्धि: हेतोः + तत् → हेतोस्तत्; "
                   "यत् + औषधम् → यदौषधम्।"),
    "hook": "पहले = मूल-फल के ज्ञान के लिए · अब फिर = पाँच कर्मों पर आश्रित ज्ञान के लिए।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "According to verse 35, for what purpose is the medicine told again?",
            ("For knowledge that rests on the five karmas",
             "Line 2: पञ्चकर्माश्रयज्ञानहेतोः … कीर्तितं पुनः."),
            [("For knowing roots and fruits",
              "That was the purpose of the earlier statement."),
             ("For making the gruels",
              "The verse does not mention gruels."),
             ("For fixing the dose",
              "The verse does not mention doses.")],
            "The earlier telling was for roots and fruits; the repeat is for knowledge resting on the five karmas.",
            "Told again for the five-karma knowledge."),
        match(1, "Match each word of verse 35 to its meaning.",
              [["पूर्वम्", "earlier, before"],
               ["पुनः", "again"],
               ["यत्", "which"],
               ["औषधम्", "medicine"]],
              "These four words carry the sense of the earlier and repeated telling.",
              "पूर्वम् = earlier; पुनः = again; यत् = which; औषधम् = medicine."),
        fill(2, "The word for 'again' in line 2 is ____ (type it in Devanagari).",
             ["पुनः", "पुनर्"],
             "Line 2 ends with पुनः.",
             "पुनः is an indeclinable: it does not change. It marks that this medicine had been told before.",
             "पुनः = again."),
        mcq("discriminate", 3, "Which is the right split of हेतोस्तत्?",
            ("हेतोः + तत्: the visarga before त becomes स्",
             "A visarga before a dental त turns into स्, so हेतोः + तत् is written हेतोस्तत्."),
            [("हेतो + स्तत्", "स्तत् is not a word."),
             ("हेतोर् + तत्", "र् appears before voiced sounds or vowels, not before त."),
             ("हेतोः + अतत्", "अतत् is not the word; the word is तत्, 'that'.")],
            "हेतोः (for the sake of) + तत् (that medicine).",
            "Visarga + त → स् + त."),
        multi("apply", 4, "Which statements does verse 35 support?",
              [("The medicine was stated earlier for knowing roots and fruits", "Right: line 1."),
               ("It is told again for knowledge resting on the five karmas", "Right: line 2."),
               ("The verse names the earlier chapter", "No chapter is named."),
               ("The verse lists the five karmas", "The five karmas are not listed here.")],
              [0, 1],
              "The verse names two purposes, earlier and now; it names no chapter and lists no karma.",
              "Earlier: roots and fruits. Now: knowledge based on the five karmas."),
        mcq("transfer", 5,
            "An invented line says औषधज्ञानहेतोर्गुणाः कीर्तिताः. By the pattern of ज्ञानहेतोः, what does औषधज्ञानहेतोः mean?",
            ("For the sake of knowledge of medicines",
             "X-हेतोः is 'for the sake of X'; here X is औषधज्ञान, medicine-knowledge."),
            [("Because medicines are unknown",
              "The word names a purpose for knowledge, not a lack of it."),
             ("For the sake of making medicines",
              "ज्ञान is knowledge, not making."),
             ("After knowing medicines",
              "हेतोः gives a purpose, not a time after.")],
            "X-हेतोः = for the sake of X.",
            "हेतोः = for the sake of.",
            teaches="A word ending in -हेतोः names the purpose: 'for the sake of' what comes before it."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "स्मृतिमान् हेतुयुक्तिज्ञो जितात्मा",
    "question": "What four qualities does the verse give the physician who is fit to treat with combinations of medicines?",
    "rule": ("A physician who is mindful (स्मृतिमान्), knows cause and "
             "rational application, is self-controlled (जितात्मा) and "
             "resourceful (प्रतिपत्तिमान्) is fit to treat by combinations "
             "of medicines."),
    "limits": ("The data's text reads हेतुयुक्तिजो; its text flag calls the final "
               "letters a data-entry error for ज्ञो (the metre and "
               "sense confirm it), and the card follows the flag. 'Hetuyukti' "
               "may be one idea (rational application of cause) or two "
               "(cause and logic); the verse does not decide."),
    "explain_hi": ("यह श्लोक वैद्य के चार गुण गिनाता है: स्मृतिमान् (स्मरण-शक्ति वाला), "
                   "हेतु और युक्ति को जानने वाला, जितात्मा (अपने को वश में रखने वाला), "
                   "प्रतिपत्तिमान् (कर्म में कुशल)। ऐसा वैद्य ‘औषधसंयोगैः’ (औषधों के "
                   "मेल से) चिकित्सा करने के योग्य (अर्हति) है। ‘-मान्’ का अर्थ ‘जिसके पास "
                   "हो’ है। डेटा के पाठ में ‘हेतुयुक्तिजो’ आया है; पाठ-टिप्पणी इसे लेखन-दोष मानकर "
                   "‘हेतुयुक्तिज्ञो’ पढ़ती है। सन्धि: भिषक् + औषध… → भिषगौषध…; "
                   "संयोगैः + चिकित्साम् → संयोगैश्चिकित्साम्।"),
    "hook": "स्मृतिमान् · हेतु-युक्ति का ज्ञाता · जितात्मा · प्रतिपत्तिमान् = औषध-संयोग से चिकित्सा के योग्य वैद्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "According to verse 36, which physician is fit to carry out treatment by combinations of medicines?",
            ("One who is mindful, self-controlled, knows cause and application, and is resourceful",
             "These are the four qualities named in line 1."),
            [("One who owns many drugs",
              "The verse names no wealth or store of drugs."),
             ("One of royal family",
              "The verse names no family or rank."),
             ("One with the most famous teachers",
              "The verse names no teacher.")],
            "The verse sets four personal qualities before the physician may treat.",
            "Mindful, knowing cause and application, self-controlled, resourceful."),
        match(1, "Match each word of verse 36 to its meaning.",
              [["स्मृतिमान्", "mindful, having good memory"],
               ["जितात्मा", "self-controlled"],
               ["प्रतिपत्तिमान्", "skilled in action, resourceful"],
               ["भिषक्", "physician"]],
              "These four words carry the verse.",
              "स्मृतिमान् = mindful; जितात्मा = self-controlled; प्रतिपत्तिमान् = resourceful; भिषक् = physician."),
        fill(2, "The word for 'self-controlled' in line 1 is ____ (type it in Devanagari).",
             ["जितात्मा"],
             "Line 1 has जितात्मा, from जित (conquered) + आत्मा (self).",
             "जितात्मा is जित-आत्मा, a compound meaning one by whom the self has been mastered. It is one of the four qualities.",
             "जितात्मा = self-controlled."),
        mcq("discriminate", 3, "Which is the right split of भिषगौषधसंयोगैः?",
            ("भिषक् + औषधसंयोगैः: क् becomes ग् before a vowel",
             "A final क् turns into ग् before a vowel, so भिषक् + औषध… is written भिषगौषध…."),
            [("भिषग् + गौषध…", "There is no word गौषध…."),
             ("भिषः + औषधसंयोगैः", "भिषः + औषध… would give भिष औषध…, but the word ends in क्, not a visarga."),
             ("भिषगौ + षधसंयोगैः", "षधसंयोगैः is not a word.")],
            "भिषक् (physician) + औषधसंयोगैः (by combinations of medicines).",
            "क् → ग् before a vowel."),
        multi("apply", 4, "Which of these are qualities of the physician named in verse 36?",
              [("स्मृतिमान्", "Right: line 1."),
               ("जितात्मा", "Right: line 1."),
               ("प्रतिपत्तिमान्", "Right: line 1."),
               ("धनवान्", "Wealth is not named."),
               ("राजपूज्यः", "Being honoured by a king is not named.")],
              [0, 1, 2],
              "Line 1 gives mindfulness, self-control and resourcefulness (and knowing cause and application); wealth and royal honour are not named.",
              "Qualities in verse 36: mindful, self-controlled, resourceful, knows cause and application."),
        mcq("transfer", 5,
            "By the pattern of स्मृतिमान् (having memory), what does an invented धृतिमान् mean (धृति = steadiness)?",
            ("One who has steadiness",
             "The ending -मान् means 'having', so धृतिमान् is 'having steadiness'."),
            [("One who lacks steadiness",
              "'Lacking' would use a negative prefix, not -मान्."),
             ("One who destroys steadiness",
              "Destroying would need a word like नाशकः."),
             ("One who is steady in memory only",
              "-मान् adds 'having'; it does not bring in memory.")],
            "-मान् after a noun = 'having that'.",
            "X-मान् = having X.",
            teaches="A noun plus -मान् (स्मृतिमान्, प्रतिपत्तिमान्) names someone who has that quality."),
    ],
}

NOTES_HI = {
    "28": "‘वर्चो निरस्यति’ = वर्चः + निरस्यति (अः + घोष → ओ)। ‘शाकैर्मांसैस्तिलैर्माषैः’ में ऐः का विसर्ग घोष वर्ण से पहले र् बना है (शाकैः + मांसैः → शाकैर्मांसैः, तिलैः + माषैः → तिलैर्माषैः)। ‘जम्ब्वाम्र…’ में जम्बु + आम्र → जम्ब्वाम्र (उ + आ → व् + आ)। पाठ-टिप्पणी के अनुसार लम्बे समास के दो पढ़ने सम्भव हैं: ‘जामुन और आम की गुठलियाँ’ या ‘जामुन, आम की गुठली’; ‘अम्ल’ अलग खट्टा द्रव्य भी हो सकता है और दधित्थ या बिल्व का विशेषण भी। श्लोक में यवागू शब्द नहीं लिखा, पूर्व सन्दर्भ से समझा गया है।",
    "29": "पाठ-भेद: पंक्ति २ के अन्त में सम्पादक ‘-बिल्वै-’ का पाठान्तर दर्ज करता है; सम्भवतः ‘-विश्वैर्’ की जगह, पर यह अनुमान है। ‘हिङ्ग्वम्लवेतसैर्भेदिनी’ में हिङ्गु + अम्ल → हिङ्ग्वम्ल (उ + अ → व् + अ), फिर वेतसैः + भेदिनी → वेतसैर्भेदिनी (विसर्ग → र् घोष से पहले)। ‘वातानुलोमनी’ = वात + अनुलोमनी (अ + अ → आ)। ‘अनुलोमन’ = वात को उसकी स्वाभाविक दिशा में चलाना।",
    "30": "‘स्याद्घृत…’ = स्यात् + घृत… (त् → द् घोष से पहले); ‘स्यात्तक्र…’ में त् के आगे त् होने से स्यात् वैसा ही रहा। ‘व्यापत्ति’ और ‘व्यापद्’ एक ही धातु से बने समानार्थी शब्द हैं (डेटा दोनों का एक अर्थ देता है): बिगाड़ या अनुचित प्रयोग से हुआ विकार। ‘तैलव्यापदि’ सप्तमी एकवचन है। ‘पिण्याक’ = तेल निकलने के बाद की खली (सामान्यतः तिल की), जैसा डेटा के नोट में है। ‘स्यात्’ विधिलिङ् है: ‘हो / होगी’।",
    "31": "‘यमक’ श्लोक में परिभाषित नहीं है; सामान्यतः घी-तेल का मिश्रण माना जाता है, पर यह इस श्लोक का कथन नहीं, इसलिए प्रश्न नहीं बनाया। ‘गव्यमांस’ शब्दशः गाय/बैल का मांस; टीकाकार इसे अलग पढ़ सकते हैं। ‘साम्ला’ = स + अम्ला (बहुव्रीहि: खट्टे सहित)। ‘पिप्पल्यामलकैः’ = पिप्पली + आमलकैः (ई + आ → य् + आ)। ‘यवानाम्’ षष्ठी बहुवचन: जौ की।",
    "32": "‘रेतोमार्ग’ = रेतस् + मार्ग (सकारान्त शब्द का स् घोष से पहले ओ बन गया)। ‘रुजापहा’ = रुजा + अपहा (आ + अ → आ)। ‘क्षीरोपसाधिता’ = क्षीर + उपसाधिता (अ + उ → ओ)। ‘समाषविदला’ बहुव्रीहि है: माष की दाल सहित। ‘ताम्रचूड’ शब्दशः ‘ताँबे जैसी कलगी वाला’, डेटा के अनुसार मुर्गा। श्लोक में कोई पाठभेद या त्रुटि-संकेत नहीं।",
    "33": "टिप्पणी: ‘अपामार्गक्षीर…’ का एक पढ़ना ‘अपामार्ग का दूध (चीक)’ भी हो सकता है; सीधा पढ़ना द्वन्द्व ‘अपामार्ग, दूध और गोधा-रस’ लिया गया है। ‘उपोदिकादधिभ्याम्’ द्विवचन (तृतीया) है: उपोदिका और दही, दो वस्तुएँ। ‘क्षुधं हन्यात्’ शब्दशः ‘भूख को मार दे’; श्लोक नहीं कहता कि यह अत्यधिक भूख के लिए है। ‘हन्यादपामार्ग…’ = हन्यात् + अपामार्ग… (त् → द् स्वर से पहले)।",
    "34": "‘अष्टाविंशतिरित्येता’ = अष्टाविंशतिः + इति + एता (विसर्ग → र् स्वर से पहले; इति + एता → इत्येता, इ + ए → य् + ए)। ‘चाश्रित्य’ = च + आश्रित्य; आश्रित्य में उपसर्ग आ- है, इसलिए पूर्वकालिक कृदन्त -य पर बना (छोटे स्वर के बाद त् जुड़ने से -त्य)। ‘प्रोक्तः’ = प्र + उक्तः (अ + उ → ओ)। पाँच कर्म श्लोक में गिनाए नहीं गए। ‘तत्र श्लोकः’ पंक्तियों से पहले का परिचय है।",
    "35": "‘हेतोः’ षष्ठी या पञ्चमी एकवचन है, पर यहाँ ‘के लिए’ के अर्थ में आया है। ‘यदौषधम्’ = यत् + औषधम् (त् → द् स्वर से पहले); ‘हेतोस्तत्’ = हेतोः + तत् (विसर्ग → स् त से पहले)। ‘पूर्वम्’ किस स्थान की ओर संकेत करता है, यह श्लोक नहीं बताता; डेटा के अनुसार मूल-फल वाले औषध-वर्ग सम्भव हैं।",
    "36": "पाठ-त्रुटि: डेटा के रूप ‘हेतुयुक्तिजो’ को पाठ-टिप्पणी ‘हेतुयुक्तिज्ञो’ (ज्ञ का ‘ज्ञो’) का लेखन-दोष मानती है; छन्द (सोलह अक्षर) और अर्थ दोनों इसे पुष्ट करते हैं। ‘हेतुयुक्ति’ को ‘हेतु और युक्ति’ (द्वन्द्व) भी पढ़ा जा सकता है। ‘भिषगौषध…’ = भिषक् + औषध… (क् → ग् स्वर से पहले); ‘संयोगैश्चिकित्साम्’ = संयोगैः + चिकित्साम् (विसर्ग + च → श्)। ‘ज्ञो जितात्मा’ में अः + घोष → ओ।",
}

AIDS = {
    "28": {
        "diagram": {"groups": [
            {"label": "पंक्ति १",
             "items": ["शाकैः", "मांसैः", "तिलैः", "माषैः", "सिद्धा",
                       "वर्चो", "निरस्यति"]},
            {"label": "पंक्ति २",
             "items": ["जम्बु", "आम्र", "अस्थि", "दधित्थ", "अम्ल",
                       "बिल्वैः", "साङ्ग्राहिकी", "मता"]}]},
        "contrast": "पंक्ति १: शाक-मांस-तिल-माष → मल को निकाले (निरस्यति) ↔ पंक्ति २: जामुन-आम-कैथ-खट्टा-बिल्व → मल को रोके (साङ्ग्राहिकी)।",
        "sandhi": "अः + घोष → ओ (अ के बाद): वर्चः + निरस्यति → वर्चो निरस्यति · विसर्ग → र् (ऐः के बाद, घोष से पहले): शाकैः + मांसैः → शाकैर्मांसैः · उ + आ → व् + आ: जम्बु + आम्र → जम्ब्वाम्र।",
        "chunks": "शाकैर्मांसैस्तिलैर्माषैः | सिद्धा वर्चो निरस्यति ‖ जम्ब्वाम्रास्थिदधित्थाम्लबिल्वैः | साङ्ग्राहिकी मता।",
    },
    "29": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: भेदिनी",
             "items": ["क्षार", "चित्रक", "हिङ्गु", "अम्लवेतसैः", "भेदिनी", "मता"]},
            {"label": "पंक्ति २: वातानुलोमनी",
             "items": ["अभया", "पिप्पलीमूल", "विश्वैः", "वातानुलोमनी"]}]},
        "contrast": "भेदिनी (क्षार, चित्रक, हींग, अम्लवेतस) ↔ वातानुलोमनी (अभया, पिप्पलीमूल, सोंठ): पहली ढीला कर निकाले, दूसरी वात को ठीक दिशा में चलाए।",
        "pegs": "मेरा बनाया चित्र: पहली थाली में चार द्रव्य (क्षार, चित्रक, हींग, अम्लवेतस) और ढीली गाँठ खुलती हुई (भेदिनी); दूसरी थाली में तीन औषध और हवा का सीधा बहता तीर (वातानुलोमनी)।",
        "sandhi": "उ + अ → व् + अ: हिङ्गु + अम्ल → हिङ्ग्वम्ल · विसर्ग → र् (घोष से पहले): वेतसैः + भेदिनी → वेतसैर्भेदिनी · अ + अ → आ: वात + अनुलोमनी → वातानुलोमनी।",
        "chunks": "क्षारचित्रकहिङ्ग्वम्लवेतसैर्भेदिनी मता ‖ अभयापिप्पलीमूलविश्वैर्वातानुलोमनी।",
    },
    "30": {
        "diagram": {"groups": [
            {"label": "तक्र",
             "items": ["तक्रसिद्धा", "यवागूः", "स्यात्", "घृतव्यापत्तिनाशिनी"]},
            {"label": "तक्र + पिण्याक",
             "items": ["तैलव्यापदि", "शस्ता", "स्यात्", "तक्रपिण्याकसाधिता"]}]},
        "contrast": "तक्र में पकी → घी के बिगाड़ को नष्ट करे ↔ तक्र + पिण्याक से पकी → तेल के बिगाड़ में प्रशस्त।",
        "pegs": "मेरा बनाया चित्र: घी का डिब्बा और छाछ का लोटा एक तराज़ू पर; तेल की शीशी और खली की टिकिया दूसरे पर। (केवल याद के लिए, श्लोक का कथन नहीं।)",
        "sandhi": "त् → द् (घोष से पहले): स्यात् + घृतव्यापत्ति… → स्याद्घृतव्यापत्ति… · तैलव्यापदि = तैल + व्यापद् का सप्तमी एकवचन।",
        "chunks": "तक्रसिद्धा यवागूः स्याद् | घृतव्यापत्तिनाशिनी ‖ तैलव्यापदि शस्ता | स्यात्तक्रपिण्याकसाधिता।",
    },
    "31": {
        "diagram": {"groups": [
            {"label": "पंक्ति १",
             "items": ["गव्यमांसरसैः", "साम्ला", "विषमज्वरनाशिनी"]},
            {"label": "पंक्ति २",
             "items": ["कण्ठ्या", "यवानां", "यमके", "पिप्पली", "आमलकैः", "शृता"]}]},
        "contrast": "गाय के मांस-रस + खट्टा → विषमज्वर का नाश ↔ जौ + पिप्पली + आमलक → कण्ठ्या।",
        "pegs": "मेरा बनाया चित्र: एक कटोरी में गर्म रस, ऊपर एक खट्टा द्रव्य, और दूसरी कटोरी में जौ के साथ पिप्पली और आमलक गले पर हाथ फेरते हुए। (केवल याद के लिए।)",
        "sandhi": "ई + आ → य् + आ: पिप्पली + आमलकैः → पिप्पल्यामलकैः · सा + अम्ला: स (सहित) + अम्ला → साम्ला।",
        "chunks": "गव्यमांसरसैः साम्ला | विषमज्वरनाशिनी ‖ कण्ठ्या यवानां यमके | पिप्पल्यामलकैः शृता।",
    },
    "32": {
        "diagram": {"groups": [
            {"label": "पंक्ति १",
             "items": ["ताम्रचूडरसे", "सिद्धा", "रेतस्", "मार्ग", "रुजा", "अपहा"]},
            {"label": "पंक्ति २",
             "items": ["समाषविदला", "वृष्या", "घृत", "क्षीर", "उपसाधिता"]}]},
        "pegs": "मेरा बनाया चित्र: ताँबे जैसी कलगी वाला मुर्गा (ताम्रचूड) एक बर्तन के ऊपर; दूसरे बर्तन में माष-दाल, घी की बूँद और दूध की धार।",
        "puns": "ताम्रचूड = ‘ताँबे जैसी कलगी वाला’ (डेटा का अर्थ): शब्द के अर्थ से याद रखने की मेरी सहायता, श्लोक का अतिरिक्त कथन नहीं।",
        "sandhi": "रेतस् + मार्ग → रेतोमार्ग · आ + अ → आ: रुजा + अपहा → रुजापहा · अ + उ → ओ: क्षीर + उपसाधिता → क्षीरोपसाधिता।",
        "chunks": "ताम्रचूडरसे सिद्धा | रेतोमार्गरुजापहा ‖ समाषविदला वृष्या | घृतक्षीरोपसाधिता।",
    },
    "33": {
        "diagram": {"groups": [
            {"label": "पंक्ति १",
             "items": ["उपोदिका", "दधिभ्याम्", "तु", "सिद्धा", "मदविनाशिनी"]},
            {"label": "पंक्ति २",
             "items": ["क्षुधम्", "हन्यात्", "अपामार्ग", "क्षीर", "गोधारसैः", "शृता"]}]},
        "contrast": "उपोदिका + दही → मद (नशा) नष्ट ↔ अपामार्ग + दूध + गोधा-रस → भूख नष्ट।",
        "pegs": "मेरा बनाया चित्र: एक हाथ में दो वस्तुएँ (उपोदिका और दही) और झूमता प्याला; दूसरे हाथ में गोह का शोरबा और खाली पेट पर ताला।",
        "sandhi": "त् → द् (स्वर से पहले): हन्यात् + अपामार्ग → हन्यादपामार्ग · -भ्याम् = द्विवचन (दो वस्तुएँ): उपोदिका + दधि।",
        "chunks": "उपोदिकादधिभ्यां तु | सिद्धा मदविनाशिनी ‖ क्षुधं हन्यात् | अपामार्गक्षीरगोधारसैः शृता।",
    },
    "34": {
        "diagram": {"groups": [
            {"label": "पंक्ति १",
             "items": ["अष्टाविंशतिः", "इति", "एता", "यवाग्वः", "परिकीर्तिताः"]},
            {"label": "पंक्ति २",
             "items": ["पञ्चकर्माणि", "च", "आश्रित्य", "प्रोक्तः", "भैषज्यसंग्रहः"]}]},
        "frame": "क्या: २८ यवागू गिनाई जा चुकीं · आधार: पाँच कर्म · कथित: भैषज्य का संग्रह।",
        "letters": "अ-य-प-प-आ-प्र-भै: अष्टाविंशति, यवागू, परिकीर्तित, पञ्चकर्म, आश्रित्य, प्रोक्त, भैषज्य।",
        "sandhi": "विसर्ग → र् (इ के बाद, स्वर से पहले): अष्टाविंशतिः + इति → अष्टाविंशतिरिति · इ + ए → य् + ए: इति + एता → इत्येता · अ + उ → ओ: प्र + उक्तः → प्रोक्तः।",
        "chunks": "अष्टाविंशतिरित्येता | यवाग्वः परिकीर्तिताः ‖ पञ्चकर्माणि चाश्रित्य | प्रोक्तो भैषज्यसंग्रहः।",
    },
    "35": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: पहले",
             "items": ["पूर्वम्", "मूलफलज्ञानहेतोः", "उक्तम्", "यत्", "औषधम्"]},
            {"label": "पंक्ति २: अब फिर",
             "items": ["पञ्चकर्माश्रयज्ञानहेतोः", "तत्", "कीर्तितम्", "पुनः"]}]},
        "contrast": "पहले: मूल-फल के ज्ञान के लिए ↔ अब: पाँच कर्मों पर आश्रित ज्ञान के लिए (उसी औषध का पुनः कथन)।",
        "sandhi": "विसर्ग + त → स्त: हेतोः + तत् → हेतोस्तत् · त् → द् (स्वर से पहले): यत् + औषधम् → यदौषधम्।",
        "chunks": "पूर्वं मूलफलज्ञानहेतोः | उक्तं यदौषधम् ‖ पञ्चकर्माश्रयज्ञानहेतोस्तत् | कीर्तितं पुनः।",
    },
    "36": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: चार गुण",
             "items": ["स्मृतिमान्", "हेतुयुक्तिज्ञः", "जितात्मा", "प्रतिपत्तिमान्"]},
            {"label": "पंक्ति २: फल",
             "items": ["भिषक्", "औषधसंयोगैः", "चिकित्साम्", "कर्तुम्", "अर्हति"]}]},
        "letters": "स्म-हे-जि-प्र: स्मृतिमान्, हेतुयुक्ति-ज्ञ, जितात्मा, प्रतिपत्तिमान्।",
        "pegs": "मेरा बनाया चित्र: चार पायों की चौकी, हर पाये पर एक गुण; उस पर बैठा वैद्य औषधों को मिलाता हुआ।",
        "sandhi": "क् → ग् (स्वर से पहले): भिषक् + औषध… → भिषगौषध… · विसर्ग + च → श्च: संयोगैः + चिकित्साम् → संयोगैश्चिकित्साम् · अः + घोष → ओ: ज्ञः + जितात्मा → ज्ञो जितात्मा।",
        "chunks": "स्मृतिमान् हेतुयुक्तिज्ञो | जितात्मा प्रतिपत्तिमान् ‖ भिषगौषधसंयोगैश्चिकित्सां | कर्तुमर्हति।",
    },
}

IMAGE_SPECS = {
    ("30", "contrast"): {
        "file": "ch2-gruel-trouble-30.svg",
        "alt": "Table of verse 30: a gruel cooked in buttermilk removes the ill effects of ghee; a gruel cooked with buttermilk and oil-cake is recommended in the ill effects of oil.",
        "type": "table",
        "title": "श्लोक ३०: यवागू और उसका विकार",
        "heads": ["किसमें पकी", "किस बिगाड़ में"],
        "rows": [["तक्र", "घी का बिगाड़"],
                 ["तक्र + पिण्याक", "तेल का बिगाड़"]],
    },
    ("36", "diagram"): {
        "file": "ch2-physician-36.svg",
        "alt": "Two columns for verse 36: the four qualities of the physician (mindful, knows cause and rational application, self-controlled, resourceful) and the result, fit to treat by combinations of medicines.",
        "type": "split",
        "title": "श्लोक ३६: वैद्य के चार गुण",
        "cols": [["चार गुण", ["स्मृतिमान्", "हेतु-युक्ति का ज्ञाता", "जितात्मा",
                              "प्रतिपत्तिमान्"]],
                 ["फल", ["औषध-संयोग से चिकित्सा के योग्य"]]],
    },
}
