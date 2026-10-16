"""Units 21-30 of Caraka Su. 1, written by hand (batch 03)."""
from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}
NOTES_HI = {}
AIDS = {}
IMAGE_SPECS = {}

# --------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "सो ऽभिगम्य जयाशीर्भिः",
    "question": "How does Bharadvāja approach Indra before he delivers the sages' message?",
    "rule": ("He approached Indra, greeted him with blessings of victory, and "
             "then humbly spoke the sages' excellent message. The message "
             "itself is in verse 22."),
    "limits": ("The verse only introduces the speech; it does not give its "
               "words. The printed ऋसीणां is a typing slip for ऋषीणाम् (see "
               "the note)."),
    "explain_hi": ("भरद्वाज इन्द्र के पास पहुँचे, विजय के आशीर्वादों से उनका "
                   "अभिनन्दन किया और फिर विनय से ऋषियों का उत्तम वचन कहा। "
                   "‘अभिगम्य’ और ‘अभिनन्द्य’ दोनों ‘करके’ वाले रूप हैं और दोनों में "
                   "उपसर्ग ‘अभि-’ है, इसलिए अन्त में ‘-य’ आता है। ‘विनयात्’ पञ्चमी "
                   "एकवचन है: ‘विनय से’। असली वचन अगले श्लोक में है।"),
    "hook": "पास गए → अभिनन्दन किया → विनय से बोले: अभिगम्य – अभिनन्द्य – प्रोवाच।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Before delivering the sages' message, what does Bharadvāja do to Indra?",
            ("He greets him with blessings of victory",
             "जयाशीर्भिः अभिनन्द्य: he greeted the lord of the gods with blessings of victory."),
            [("He demands the remedy at once",
              "The request comes in verse 22, after the greeting."),
             ("He ignores him and speaks to the other gods",
              "The verse says he approached and greeted Indra."),
             ("He recites the names of the sages",
              "The names were given earlier in the chapter, not here.")],
            "He approaches, greets with blessings of victory, then speaks humbly.",
            "Approach, greet, then speak."),
        match(1, "Match each word of the verse to its meaning.",
              [["अभिगम्य", "having approached"], ["अभिनन्द्य", "having greeted"],
               ["सुरेश्वरम्", "the lord of the gods"], ["प्रोवाच", "he said"]],
              "These words carry the three actions of the verse.",
              "अभिगम्य = having approached; अभिनन्द्य = having greeted; सुरेश्वरम् = lord of the gods; प्रोवाच = he said."),
        fill(2, "The word for out of humility (humbly) is ____ (type it in Devanagari, before sandhi).",
             ["विनयात्", "विनयाद्", "विनयाद"],
             "The verse says विनयाद्धीमान्, that is विनयात् + धीमान्.",
             "विनयात् ends in the ablative -आत्, 'from, out of': he spoke out of humility. Before a voiced letter (ध) the final त् is written द्.",
             "An ablative in -आत् can give the reason or manner: 'out of humility'."),
        mcq("discriminate", 3, "Which is the right split of विनयाद्धीमान्?",
            ("विनयात् + धीमान्", "त् before the voiced ध becomes द्, so विनयात् + धीमान् is written विनयाद्धीमान्."),
            [("विनय + आद्धीमान्", "आद्धीमान् is not a word."),
             ("विनयाद् + हीमान्", "हीमान् is not a word; the second word is धीमान्, the wise one."),
             ("विनयात् + दीमान्", "दीमान् is not a word.")],
            "विनयाद्धीमान् = विनयात् + धीमान्: 'out of humility' + 'the wise one'.",
            "Final त् becomes द् before ध (and before ग, घ, ब, भ, द and vowels)."),
        mcq("apply", 4, "Why is सः written सो in सो ऽभिगम्य?",
            ("Before a following अ, the visarga of सः becomes ओ, and the अ is shown by ऽ",
             "-अः + अ gives -ओ ऽ."),
            [("सो is a different word meaning 'to him'", "It is the same word सः, 'he'."),
             ("The ओ marks a dual", "The ओ here is only a sandhi result, not an ending."),
             ("The ओ marks a call, 'O!'", "A call would be in a different form and context; here it is plain 'he'.")],
            "सः + अभिगम्य → सो ऽभिगम्य: the visarga turns into ओ and the following अ is dropped, marked by ऽ.",
            "-अः before अ gives ओ ऽ."),
        mcq("transfer", 5,
            "A new line says a pupil went up to his teacher using prefix उप- with root गम्, then spoke. Which form means having gone up to?",
            ("उपगम्य", "With a prefix, the 'having done' form ends in -य, as in अभिगम्य."),
            [("उपगत्वा", "-त्वा is used when there is no prefix, as in बुद्ध्वा."),
             ("उपागमत्", "That is a finite past verb, 'approached', not 'having gone up to'."),
             ("उपगन्तव्य", "That is a 'must be approached' form, not 'having approached'.")],
            "Prefix + root + -य is the pattern shown by अभिगम्य and अभिनन्द्य.",
            "Prefix present: 'having done' ends in -य; no prefix: -त्वा.",
            teaches="A prefix on the root tells you to expect a -य form for 'having done'."),
    ],
}
NOTES_HI["21"] = ("पाठ में ‘ऋसीणां’ छपा है (देवनागरी पंक्ति में भी); अपेक्षित ‘ऋषीणाम्’ है "
                  "(षष्ठी बहुवचन, मूर्धन्य ष)। यह टंकण-त्रुटि लगती है। ‘सो ऽभिगम्य’ में "
                  "‘सः’ का विसर्ग अ से पहले ओ बना और अ का लोप ऽ से दिखाया गया। "
                  "‘विनयाद्धीमान्’ = विनयात् + धीमान् (त् घोष ‘ध’ से पहले द् बना)।")
AIDS["21"] = {
    "frame": "कौन: भरद्वाज (धीमान्) · किसके पास: सुरेश्वर (इन्द्र) · कैसे: जय के "
             "आशीर्वाद से अभिनन्दन, फिर विनय से · क्या: ऋषियों का उत्तम वचन (श्लोक २२)।",
    "chain": "अभिगम्य (पास गए) → अभिनन्द्य (अभिनन्दन किया) → प्रोवाच (बोले)।",
    "anchors": "अभिनन्द्य ← अभि + √नन्द् · जयाशीः = जय + आशीः (विजय का आशीर्वाद) · "
               "सुरेश्वर = सुर + ईश्वर (देवों का स्वामी)।",
    "sandhi": "-अः + अ → ओ ऽ: सः + अभिगम्य → सो ऽभिगम्य। अ + ई → ए: सुर + ईश्वरम् → "
              "सुरेश्वरम्। अ + उ → ओ: प्र + उवाच → प्रोवाच। त् → द् (घोष ध से पहले): "
              "विनयात् + धीमान् → विनयाद्धीमान्।",
    "contrast": "अभिगम्य, अभिनन्द्य (उपसर्ग अभि-, अन्त में -य) ↔ बुद्ध्वा (श्लोक ३, "
                "उपसर्ग नहीं, -त्वा)।",
    "chunks": "सो ऽभिगम्य | जयाशीर्भिः | अभिनन्द्य सुरेश्वरम् ‖ प्रोवाच | विनयाद्धीमान् | "
              "ऋषीणां (छपा: ऋसीणां) वाक्यमुत्तमम्।",
}

# --------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "व्याधयो हि समुत्पन्नाः",
    "question": "What does Bharadvāja tell Indra, and what does he ask for?",
    "rule": ("Diseases that terrify all living beings have arisen; therefore "
             "Indra, lord of the immortals, is asked to tell the means of "
             "curing them properly."),
    "limits": ("तत् may be 'therefore' or the pronoun 'that' going with the "
               "means. The verse does not say what the means are; that "
               "begins in the next verses."),
    "explain_hi": ("यह ऋषियों का सन्देश है, जिसे भरद्वाज इन्द्र को सुनाते हैं। पहली "
                   "पंक्ति कारण बताती है: ऐसे रोग उत्पन्न हो गए हैं जो सब प्राणियों "
                   "को भयभीत करते हैं। दूसरी पंक्ति प्रार्थना है: ‘ब्रूहि’ (आज्ञार्थक, "
                   "‘बताइए’) और ‘अमरप्रभो’ सम्बोधन है: ‘हे अमरों के स्वामी’। "
                   "‘शमोपायम्’ = शम (शान्ति) + उपाय।"),
    "hook": "रोग उठे, सब डरे → इसलिए: ब्रूहि मे शमोपायम्, हे अमरप्रभो।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What reason does Bharadvāja give for his request to Indra?",
            ("Diseases that terrify all beings have arisen",
             "व्याधयः समुत्पन्नाः सर्वप्राणिभयङ्कराः says exactly this."),
            [("The sages have lost their vows", "That worry belongs to the earlier verses about the obstacles, not to this verse."),
             ("Indra has not been honoured", "Nothing here complains about honour."),
             ("The gods are asking for medicine", "The request is made on behalf of the sages and living beings.")],
            "The reason is the rise of frightening diseases.",
            "Reason first (diseases), request second (tell the remedy)."),
        match(1, "Match each word to its meaning.",
              [["व्याधयः", "diseases"], ["भयङ्कराः", "causing fear"],
               ["ब्रूहि", "tell!"], ["शमोपायम्", "the means of cure"]],
              "These four words carry the whole sentence.",
              "व्याधयः = diseases; भयङ्कराः = causing fear; ब्रूहि = tell; शमोपायम् = means of cure."),
        fill(2, "The command meaning tell in the second line is ____ (type it in Devanagari).",
             ["ब्रूहि"],
             "The line begins तद्ब्रूहि, that is तत् + ब्रूहि.",
             "ब्रूहि is the command form of the root ब्रू, 'speak': Bharadvāja asks Indra to tell.",
             "ब्रूहि = 'tell!', a command to one person."),
        mcq("discriminate", 3, "Which is the right split of शमोपायम्?",
            ("शम + उपायम्", "अ + उ gives ओ, so शम + उपायम् is written शमोपायम्."),
            [("शमो + पायम्", "पायम् is not the word here; the second word is उपायम्, the means."),
             ("शम + ओपायम्", "ओपायम् is not a word."),
             ("शमि + उपायम्", "इ + उ would give यु, written शम्युपायम्.")],
            "शमोपायम् = शम (calming) + उपाय (means).",
            "अ + उ → ओ."),
        mcq("apply", 4,
            "In verse 18 the form is अमरप्रभुः; here it is अमरप्रभो. What does the ending -ओ show here?",
            ("He is being addressed: 'O lord of the immortals'",
             "The ending -ओ is the form used when calling someone, matching the translation 'O lord'."),
            [("More than one lord", "The verse speaks to one lord, Indra."),
             ("A past action", "It is a noun, not a verb."),
             ("The topic of the sentence, 'he'", "That was the verse 18 form, अमरप्रभुः, the one who will tell.")],
            "In verse 18 he is spoken about (अमरप्रभुः); here he is spoken to (अमरप्रभो).",
            "-उः (spoken about) vs -ओ (spoken to)."),
        mcq("transfer", 5,
            "By the same rule that gives तद्ब्रूहि from तत् + ब्रूहि, how is तत् + गच्छ written?",
            ("तद्गच्छ", "Final त् before a soft stop such as ग becomes द्."),
            [("तत्गच्छ", "Left unchanged, it would break the rule shown by तद्ब्रूहि."),
             ("तट्गच्छ", "The त् does not turn retroflex here."),
             ("तन्गच्छ", "A nasal न् appears only before a nasal letter.")],
            "Final त् before a soft stop such as ग, घ, ब, ध, द is written द्.",
            "त् + soft stop → द्.",
            teaches="Final त् changes to द् before a soft stop such as ग, घ, ब, ध, द."),
    ],
}
NOTES_HI["22"] = ("‘तत्’ को ‘इसलिए’ (अव्यय) या ‘उस उपाय’ के विशेषण के रूप में भी पढ़ा जा सकता है; "
                  "अर्थ लगभग वही रहता है। ‘तद्ब्रूहि’ = तत् + ब्रूहि (त् घोष ‘ब’ से पहले द्)। "
                  "‘शमोपायम्’ = शम + उपायम् (अ + उ → ओ)। ‘अमरप्रभो’ सम्बोधन है।")
AIDS["22"] = {
    "frame": "कौन: भरद्वाज · किससे: इन्द्र (अमरप्रभु) · कारण: रोग जो सब प्राणियों को "
             "डराते हैं · माँग: शान्ति का उपाय, यथावत्।",
    "chain": "रोग उत्पन्न (व्याधयः समुत्पन्नाः) → सबको भय (भयङ्कराः) → इसलिए (तत्) → "
             "बताइए (ब्रूहि) शमोपायम्।",
    "anchors": "भयङ्कर = भय + कर (भय करने वाला) · शम = शान्ति · उपाय = साधन।",
    "sandhi": "त् → द् (घोष ब से पहले): तत् + ब्रूहि → तद्ब्रूहि। अ + उ → ओ: शम + उपायम् → "
              "शमोपायम्।",
    "contrast": "अमरप्रभुः (श्लोक १८, ‘वे स्वामी’) ↔ अमरप्रभो (यहाँ, ‘हे स्वामी’, सम्बोधन)।",
    "chunks": "व्याधयो हि समुत्पन्नाः | सर्वप्राणिभयङ्कराः ‖ तद्ब्रूहि मे | शमोपायं | "
              "यथावदमरप्रभो।",
}

# --------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "तस्मै प्रोवाच भगवान्",
    "question": "Who taught whom, in how many words, and why so few?",
    "rule": ("Indra (Śatakratu) taught Āyurveda to Bharadvāja, the supreme "
             "sage, in few words, having recognised that his intellect was "
             "vast."),
    "limits": ("The verse does not say what the few words were. That few "
               "words sufficed because of his vast intellect is the natural "
               "reading of बुद्ध्वा, not a separate statement."),
    "explain_hi": ("इन्द्र (शतक्रतु) भरद्वाज की विशाल बुद्धि को जानकर उन्हें थोड़े पदों में "
                   "आयुर्वेद सिखाते हैं। ‘तस्मै’ और ‘परमर्षये’ दोनों भरद्वाज के लिए हैं (चतुर्थी)। "
                   "‘बुद्ध्वा’ पहले की क्रिया है: पहले बुद्धि जानी, तब उपदेश दिया। "
                   "‘परमर्षये’ = परम + ऋषये (अ + ऋ → अर्)।"),
    "hook": "बुद्धि विशाल जानी → थोड़े पदों में आयुर्वेद दिया।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Who teaches Āyurveda to whom in this verse?",
            ("Indra teaches Bharadvāja",
             "भगवान् शतक्रतुः is Indra, and तस्मै … परमर्षये is Bharadvāja."),
            [("Bharadvāja teaches Indra", "It is the other way round: Indra is the teacher here."),
             ("Brahmā teaches Prajāpati", "That was in verse 4."),
             ("Indra teaches the six disciples", "The six disciples come much later, from verse 30.")],
            "Indra, called Śatakratu, teaches Bharadvāja.",
            "Indra → Bharadvāja."),
        match(1, "Match each phrase to its meaning.",
              [["तस्मै", "to him"], ["प्रोवाच", "he taught, he spoke"],
               ["पदैरल्पैः", "with few words"], ["विपुलाम्", "vast"]],
              "विपुलाम् describes the intellect (मतिम्).",
              "तस्मै = to him; प्रोवाच = he spoke; पदैरल्पैः = with few words; विपुलाम् = vast."),
        fill(2, "The word meaning having known in the second line is ____ (type it in Devanagari).",
             ["बुद्ध्वा"],
             "The second line has मतिं बुद्ध्वा विपुलाम्: having known the intellect to be vast.",
             "बुद्ध्वा has -त्वा, which marks an action that happens before the main verb: first Indra recognised the intellect, then he taught.",
             "-त्वा on a root with no prefix = 'having done', an earlier action."),
        mcq("discriminate", 3, "Which is the right split of परमर्षये?",
            ("परम + ऋषये", "अ + ऋ gives अर्, so परम + ऋषये is written परमर्षये."),
            [("परमि + ऋषये", "इ + ऋ would give य्, written परम्यृषये."),
             ("परमर + षये", "षये is not a word."),
             ("परमः + ऋषये", "A visarga before ऋ would not give this form.")],
            "परमर्षये = परम (supreme) + ऋषये (to the sage).",
            "अ + ऋ → अर्."),
        mcq("apply", 4, "According to the verse, what did Indra recognise before he taught in few words?",
            ("That Bharadvāja's intellect was vast",
             "मतिं बुद्ध्वा विपुलाम्: having known the intellect to be vast."),
            [("That Bharadvāja was tired", "Nothing about tiredness is said."),
             ("That the other sages had already learned it", "Nothing about other sages is said in this verse."),
             ("That Āyurveda is a short science", "The verse does not say so; the few words are linked to his intellect.")],
            "बुद्ध्वा links the recognition of his vast intellect to the teaching in few words.",
            "Vast intellect recognised → few words enough."),
        mcq("transfer", 5,
            "By the rule that gives परमर्षये from परम + ऋषये, how is देव + ऋषि written?",
            ("देवर्षि", "अ + ऋ gives अर्."),
            [("देवृषि", "The अ would not disappear leaving ऋ alone."),
             ("देवेषि", "अ + ऋ does not give ए."),
             ("देवारषि", "The result is अर्, not आर.")],
            "अ + ऋ → अर् turns देव + ऋषि into देवर्षि, just as महा + ऋषि gives महर्षि.",
            "अ/आ + ऋ → अर्.",
            teaches="You can join any word ending in -अ with a following ऋ-word by writing अर्."),
    ],
}
NOTES_HI["23"] = ("‘तस्मै’ और ‘परमर्षये’ दोनों भरद्वाज के लिए हैं। ‘मतिं बुद्ध्वा विपुलाम्’ में ‘विपुलाम्’ "
                  "मति का विशेषण है। ‘भगवानायुर्वेदम्’ = भगवान् + आयुर्वेदम् (न् स्वर से जुड़ गया)। "
                  "‘परमर्षये’ = परम + ऋषये। ‘पदैरल्पैः’ = पदैः + अल्पैः (विसर्ग स्वर से पहले र्)।")
AIDS["23"] = {
    "frame": "कौन: भगवान् शतक्रतु (इन्द्र) · किसे: परम ऋषि (भरद्वाज) · क्या: आयुर्वेद · "
             "कैसे: थोड़े पदों में, क्योंकि मति विशाल जानी।",
    "chain": "मति विशाल जानी (बुद्ध्वा) → थोड़े पदों में (पदैरल्पैः) → आयुर्वेद का उपदेश (प्रोवाच)।",
    "seesaw": "पदैः अल्पैः (थोड़े शब्द) ↔ मतिं विपुलाम् (विशाल बुद्धि): बुद्धि विशाल हो तो "
              "थोड़े शब्द काफी।",
    "anchors": "शतक्रतु = शत + क्रतु (सौ यज्ञ वाले) · परमर्षि = परम + ऋषि · विपुल = विशाल · "
               "अल्प = थोड़ा।",
    "sandhi": "अ + ऋ → अर्: परम + ऋषये → परमर्षये (वैसे ही महा + ऋषि → महर्षि)। "
              "भगवान् + आयुर्वेदम् → भगवानायुर्वेदम्। विसर्ग → र् (स्वर से पहले): पदैः + अल्पैः → "
              "पदैरल्पैः।",
    "puns": "शतक्रतु ≈ ‘शत-क्रेटू’ (सौ का पिटारा): केवल सुनने की सहायता; अर्थ है ‘सौ यज्ञ’।",
    "chunks": "तस्मै प्रोवाच | भगवान् | आयुर्वेदं शतक्रतुः ‖ पदैरल्पैः | मतिं बुद्ध्वा | "
              "विपुलां परमर्षये।",
}

# --------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "हेतुलिङ्गौषधज्ञानम्",
    "question": "How does verse 24 describe the Āyurveda that Indra taught?",
    "rule": ("Āyurveda is the knowledge of cause (हेतु), sign (लिङ्ग) and "
             "remedy (औषध); the supreme resort of the healthy and the sick; "
             "threefold in its aphorisms, eternal and holy; Brahmā knew it."),
    "limits": ("त्रिसूत्रम् is usually taken as that same triad of cause, "
               "sign and remedy; the verse does not spell it out. "
               "परायणम् is a two-way word: 'resort' or 'devoted to'. "
               "The data marks this verse as medium confidence."),
    "explain_hi": ("यह श्लोक उस आयुर्वेद का वर्णन है जो श्लोक २३ में दिया गया। वह हेतु, लिङ्ग "
                   "(लक्षण) और औषध का ज्ञान है, स्वस्थ और रोगी दोनों का परम आश्रय है, "
                   "त्रिसूत्र, शाश्वत और पुण्य है। ‘त्रिसूत्र’ को सामान्यतः इन्हीं तीन "
                   "(हेतु–लिङ्ग–औषध) से जोड़ा जाता है। सब विशेषण ‘आयुर्वेदम्’ के हैं। "
                   "अन्त में कहा गया कि इसे पितामह (ब्रह्मा) ने जाना था।"),
    "hook": "हेतु–लिङ्ग–औषध: कारण, लक्षण, दवा। स्वस्थ और रोगी का आश्रय; पितामह ने जाना।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The first word of verse 24 names three things whose knowledge Āyurveda is. Which three?",
            ("Cause, sign and remedy",
             "हेतु, लिङ्ग and औषध: cause, sign (symptom) and remedy."),
            [("Gods, sages and kings", "Those are not in the first word."),
             ("Past, present and future", "Time is not mentioned in this verse."),
             ("Body, speech and mind", "None of these three appears in the verse.")],
            "हेतुलिङ्गौषधज्ञानम् = the knowledge of cause, sign and remedy.",
            "हेतु + लिङ्ग + औषध = cause, sign, remedy."),
        match(1, "Match each word to its meaning.",
              [["हेतु", "cause"], ["लिङ्ग", "sign, symptom"],
               ["औषध", "remedy"], ["आतुर", "sick person"]],
              "The first three form the triad of the verse; आतुर is the second of the two people it serves.",
              "हेतु = cause; लिङ्ग = sign; औषध = remedy; आतुर = sick person."),
        fill(2, "Brahmā is called ____ , 'the grandfather', in the last word of the verse (type it in Devanagari).",
             ["पितामहः", "पितामह"],
             "The verse ends बुबुधे यं पितामहः: the Grandfather understood it.",
             "पितामह means grandfather; the translation reads it as a name of Brahmā. It is the subject of बुबुधे, 'understood'.",
             "पितामहः = the Grandfather, here Brahmā."),
        mcq("discriminate", 3, "Which is the right split of लिङ्गौषध (inside the first compound)?",
            ("लिङ्ग + औषध", "अ + औ gives औ, so लिङ्ग + औषध is written लिङ्गौषध."),
            [("लिङ्गौ + षध", "षध is not a word."),
             ("लिङ्गो + औषध", "A word लिङ्गो with this ending is not in the verse."),
             ("लिङ्गः + औषध", "A visarga before औ would leave a gap, not merge the words.")],
            "लिङ्गौषध = लिङ्ग (sign) + औषध (remedy).",
            "अ + औ → औ."),
        multi("apply", 4, "Which of these are said of Āyurveda in verse 24? Pick all that apply.",
              [("शाश्वतम्", "Right: eternal."),
               ("पुण्यम्", "Right: holy."),
               ("स्वस्थातुरपरायणम्", "Right: the supreme resort of the healthy and the sick."),
               ("अनन्तपारम्", "Wrong: this word appears in verse 25, not here."),
               ("प्रजाहितम्", "Wrong: this word appears in verse 27, not here.")],
              [0, 1, 2],
              "The three right words are all in the second line or the first-line compound; the other two come in later verses.",
              "शाश्वतम्, पुण्यम्, स्वस्थातुरपरायणम् are said here."),
        mcq("transfer", 5,
            "By the rule that gives स्वस्थातुर from स्वस्थ + आतुर, how is पुस्तक + आलय written?",
            ("पुस्तकालय", "अ + आ gives आ."),
            [("पुस्तकलय", "That drops the आ instead of lengthening the vowel."),
             ("पुस्तकोलय", "अ + आ does not give ओ."),
             ("पुस्तकैलय", "अ + आ does not give ऐ.")],
            "अ + आ → आ: पुस्तक + आलय = पुस्तकालय, as स्वस्थ + आतुर = स्वस्थातुर.",
            "अ + आ → आ.",
            teaches="Any word ending in -अ joined with a following आ-word merges into a single long आ."),
    ],
}
NOTES_HI["24"] = ("विश्वास: मध्यम। सभी विशेषण (स्वस्थातुरपरायणम्, त्रिसूत्रम्, शाश्वतम्, पुण्यम्) श्लोक २३ के "
                  "‘आयुर्वेदम्’ से जुड़ते हैं; ‘यम्’ भी उसी की ओर संकेत करता है। ‘परायणम्’ को ‘परम आश्रय’ या "
                  "‘(स्वस्थ-रोगी के हित में) लगा हुआ’ पढ़ा जा सकता है। ‘त्रिसूत्रम्’ का सामान्य अर्थ "
                  "हेतु–लिङ्ग–औषध है, पर श्लोक स्वयं ऐसा नहीं कहता। ‘लिङ्गौषध’ = लिङ्ग + औषध (अ + औ → औ); "
                  "‘स्वस्थातुर’ = स्वस्थ + आतुर (अ + आ → आ)।")
AIDS["24"] = {
    "frame": "क्या: आयुर्वेद · किसका ज्ञान: हेतु, लिङ्ग, औषध · किसका आश्रय: स्वस्थ और "
             "आतुर · किसने जाना: पितामह।",
    "chain": "हेतु (कारण) → लिङ्ग (लक्षण) → औषध (दवा): यही त्रय सामान्यतः ‘त्रिसूत्र’ माना "
             "जाता है।",
    "diagram": {"groups": [
        {"label": "ज्ञान", "items": ["हेतु", "लिङ्ग", "औषध", "ज्ञानम्"]},
        {"label": "आश्रय", "items": ["स्वस्थ", "आतुर", "परायणम्"]},
        {"label": "गुण", "items": ["त्रिसूत्रम्", "शाश्वतम्", "पुण्यम्"]},
        {"label": "जाना", "items": ["बुबुधे", "यं", "पितामहः"]}]},
    "letters": "हे-लि-औ: हेतु · लिङ्ग · औषध।",
    "sandhi": "अ + औ → औ: लिङ्ग + औषध → लिङ्गौषध। अ + आ → आ: स्वस्थ + आतुर → स्वस्थातुर।",
    "anchors": "त्रिसूत्र = त्रि + सूत्र (तीन सूत्र) · शाश्वत ← शश्वत् (सदा) · पितामह = पिता "
               "का पिता · आतुर = रोगी।",
    "chunks": "हेतुलिङ्गौषधज्ञानं | स्वस्थातुरपरायणम् ‖ त्रिसूत्रं शाश्वतं पुण्यं | "
              "बुबुधे यं पितामहः।",
}

# --------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "सो ऽनन्तपारं त्रिस्कन्धम्",
    "question": "How did Bharadvāja take in Āyurveda, and how is it described?",
    "rule": ("The sage of great intellect, with his mind fixed on it, quickly "
             "and properly understood the whole of Āyurveda, which is "
             "boundless in extent and has three divisions."),
    "limits": ("त्रिस्कन्धम् is generally taken as the same triad as "
               "त्रिसूत्रम् in verse 24; this verse itself does not name "
               "the three. The subject is not named; it is the sage "
               "(Bharadvāja) from the context."),
    "explain_hi": ("भरद्वाज ने (महामति मुनि) एकाग्र मन से, शीघ्र और यथावत् सम्पूर्ण आयुर्वेद "
                   "समझ लिया। इसे ‘अनन्तपार’ कहा गया है, यानी जिसका दूसरा किनारा अनन्त है, और "
                   "‘त्रिस्कन्ध’, यानी तीन विभाग वाला। ‘अ/अन्’ से बने शब्द (अनन्त, अचिरात्) "
                   "‘नहीं’ का भाव देते हैं। ‘तन्मना’ में विसर्ग का लोप हुआ है।"),
    "hook": "अपार आयुर्वेद, तीन स्कन्ध; एकाग्र मन से भरद्वाज ने शीघ्र पूरा समझा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What did the sage of great intellect do, according to verse 25?",
            ("He understood the whole of Āyurveda quickly and properly",
             "यथावदचिरात् सर्वं बुबुधे: properly, quickly, all, he understood."),
            [("He refused the teaching", "The verse says he understood it."),
             ("He taught it to the six disciples", "That comes in verse 30."),
             ("He wrote it down at once", "Nothing is said about writing.")],
            "He understood the whole of Āyurveda quickly and properly.",
            "बुबुधे = he understood; सर्वम् = the whole."),
        match(1, "Match each word to its meaning.",
              [["अनन्तपारम्", "boundless in extent"], ["त्रिस्कन्धम्", "having three divisions"],
               ["अचिरात्", "quickly"], ["तन्मनाः", "with mind fixed on it"]],
              "Each word adds one detail about the sage or about Āyurveda.",
              "अनन्तपारम् = boundless; त्रिस्कन्धम् = three divisions; अचिरात् = quickly; तन्मनाः = mind fixed on it."),
        fill(2, "The word for the whole (all) in the second line is ____ (type it in Devanagari).",
             ["सर्वम्", "सर्वं"],
             "The second line reads यथावदचिरात् सर्वं बुबुधे.",
             "सर्वम् goes with आयुर्वेदम्: he understood the whole of it, not a part.",
             "सर्वम् = the whole, all."),
        mcq("discriminate", 3, "Why is तन्मना, and not तन्मनाः, written before मुनिः?",
            ("A visarga after आ is dropped before a voiced letter such as म",
             "आः + voiced letter → आ, so तन्मनाः + मुनिः is written तन्मना मुनिः."),
            [("The visarga becomes ओ", "ओ appears after -अः, not after -आः."),
             ("The visarga becomes र्", "र् appears after vowels other than अ and आ."),
             ("It is a different word, तन्मना, meaning 'we'", "It is the same word तन्मनाः, 'with mind fixed on it'.")],
            "तन्मनाः + मुनिः → तन्मना मुनिः: the visarga after आ falls away before a voiced letter.",
            "-आः + voiced letter → -आ."),
        mcq("apply", 4, "What does अनन्तपारम् (far shore endless) say about Āyurveda?",
            ("It is boundless in extent",
             "A shore with no end means no limit to its extent."),
            [("It is very short", "A far shore that has no end is the opposite of short."),
             ("It has only one division", "That contradicts त्रिस्कन्धम्, three divisions."),
             ("It can be learned only slowly", "The verse says the sage understood it quickly.")],
            "अनन्तपार means boundless in extent, yet the sage understood it quickly.",
            "अनन्तपार = boundless."),
        mcq("transfer", 5,
            "A poet calls an ocean अपार. Using the idea of 'not' in अनन्त and अचिरात्, what does it mean?",
            ("Without a far shore, boundless",
             "अ- negates पार, 'far shore': no far shore."),
            [("With a near shore, narrow", "अ- negates; it does not mean 'near'."),
             ("Very deep", "Nothing in the word speaks of depth."),
             ("Very old", "Nothing in the word speaks of age.")],
            "अ-/अन्- means 'not': अनन्त = not-end, अचिरात् = not-long, अपार = not-having-a-far-shore.",
            "अ-/अन्- = not.",
            teaches="The prefix अ-/अन्- reverses the meaning of the word that follows."),
    ],
}
NOTES_HI["25"] = ("‘त्रिस्कन्धम्’ को सामान्यतः श्लोक २४ के ‘त्रिसूत्रम्’ वाले त्रय (हेतु–लिङ्ग–औषध) से जोड़ा जाता है; "
                  "यह इस श्लोक का अपना कथन नहीं है। ‘सो ऽनन्तपारम्’ में सः का विसर्ग अ से पहले ओ बना। "
                  "‘तन्मनाः’ = तत् + मनाः (त् + म → न्म); ‘तन्मना मुनिः’ में आः का विसर्ग घोष म् से पहले लुप्त है। "
                  "‘अचिरात्’ पञ्चमी एकवचन है, ‘शीघ्र’ के अर्थ में।")
AIDS["25"] = {
    "frame": "कौन: महामति मुनि (भरद्वाज) · क्या: सम्पूर्ण आयुर्वेद · कैसे: एकाग्र मन से, "
             "शीघ्र, यथावत्।",
    "chain": "तन्मनाः (एकाग्र मन) → अचिरात् (शीघ्र) → यथावत् सर्वं बुबुधे (ठीक-ठीक सब समझा)।",
    "anchors": "अनन्त = अ/अन् + अन्त (जिसका अन्त नहीं) · अचिरात् = अ + चिर (देर नहीं) · "
               "तन्मनाः = तत् + मनः (उसमें मन)।",
    "sandhi": "-अः + अ → ओ ऽ: सः + अनन्त… → सो ऽनन्त…। त् + म → न्म: तत् + मनाः → तन्मनाः। "
              "-आः + घोष → आ: तन्मनाः + मुनिः → तन्मना मुनिः।",
    "chunks": "सो ऽनन्तपारं | त्रिस्कन्धम् | आयुर्वेदं महामतिः ‖ यथावदचिरात् | सर्वं | "
              "बुबुधे तन्मना मुनिः।",
}

# --------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "तेनायुरमितं लेभे",
    "question": "What did Bharadvāja gain from Āyurveda, and how did he pass it on?",
    "rule": ("By it Bharadvāja obtained an immeasurable life endowed with "
             "happiness, and he told it to the sages adding nothing and "
             "leaving nothing out."),
    "limits": ("The printed सुखानिवितम् is a slip for सुखान्वितम् (see the "
               "note). तत् can be read as the teaching itself. "
               "Data confidence: medium."),
    "explain_hi": ("भरद्वाज ने आयुर्वेद से अमित (अपरिमित) आयु पाई, जो सुख से युक्त थी। फिर उन्होंने "
                   "उसे ऋषियों को ज्यों-का-त्यों बताया: ‘अनधिकम्’ यानी बिना कुछ बढ़ाए और "
                   "‘अनवशेषयन्’ यानी बिना कुछ छोड़े। यह ज्ञान के निष्ठापूर्वक आगे पहुँचाने का "
                   "वर्णन है। ‘तेन’ का अर्थ ‘उसके द्वारा’ (आयुर्वेद से) है।"),
    "hook": "आयु पाई → ऋषियों को बताया: न एक बात जोड़ी, न एक छोड़ी (अनधिकम् – अनवशेषयन्)।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What did Bharadvāja obtain by means of Āyurveda?",
            ("A life of immeasurable length",
             "आयुरमितं लेभे: he obtained an immeasurable life."),
            [("A kingdom", "No kingdom is mentioned."),
             ("The rank of Indra", "The verse does not say he became Indra."),
             ("A treatise in his own name", "No treatise by him is mentioned.")],
            "He gained an immeasurable life, and the sages received the teaching from him.",
            "Bharadvāja: long life gained, teaching passed on."),
        match(1, "Match each word to its meaning.",
              [["अमितम्", "immeasurable"], ["लेभे", "he obtained"],
               ["ऋषिभ्यः", "to the sages"], ["शशंस", "he told"]],
              "These words give the two things Bharadvāja does in the verse.",
              "अमितम् = immeasurable; लेभे = he obtained; ऋषिभ्यः = to the sages; शशंस = he told."),
        fill(2, "The word meaning 'adding nothing' in the second line is ____ (type it in Devanagari).",
             ["अनधिकम्", "अनधिकं"],
             "The line reads ऋषिभ्यो ऽनधिकम् तच्च शशंसानवशेषयन्.",
             "अनधिकम् is अन् + अधिकम्, 'not more': he added nothing of his own.",
             "अनधिकम् = without adding; अनवशेषयन् = without leaving anything out."),
        mcq("discriminate", 3, "Which is the right split of तेनायुरमितम्?",
            ("तेन + आयुः + अमितम्", "अ + आ gives आ; the visarga of आयुः before अ becomes र्."),
            [("तेना + युर + मितम्", "युर and मितम् are not words here."),
             ("ते + नायु + रमितम्", "नायु and रमितम् are not words here."),
             ("तेन + युः + अमितम्", "The second word is आयुः, with a long आ.")],
            "तेनायुरमितम् = तेन ('by it') + आयुः (life) + अमितम् (immeasurable).",
            "अ + आ → आ; -उः + अ → -उर्."),
        mcq("apply", 4, "What do अनधिकम् and अनवशेषयन् together say about how Bharadvāja taught the sages?",
            ("He passed on exactly what he had received",
             "Nothing added and nothing left out means an exact transmission."),
            [("He added his own ideas", "अनधिकम् says he added nothing."),
             ("He left out the hard parts", "अनवशेषयन् says he left nothing out."),
             ("He kept it to himself", "The verse says he told it to the sages.")],
            "Neither more nor less: the teaching is passed on exactly.",
            "अनधिक + अनवशेष = exact transmission."),
        mcq("transfer", 5,
            "By the rule that gives तच्च from तत् + च, how is सत् + चरित्र written?",
            ("सच्चरित्र", "Final त् before च is written च्, giving च्च."),
            [("सतचरित्र", "The त् must change before च."),
             ("सज्जरित्र", "त् before च becomes च्, not ज्."),
             ("सट्चरित्र", "The त् does not turn retroflex here.")],
            "Final त् followed by च becomes च्: तत् + च = तच्च, सत् + चरित्र = सच्चरित्र.",
            "त् + च → च्च.",
            teaches="A word ending in त् before च takes on च, so the sound is doubled."),
    ],
}
NOTES_HI["26"] = ("विश्वास: मध्यम। पाठ में ‘सुखानिवितम्’ छपा है; यह शब्द नहीं है और पंक्ति में १७ अक्षर "
                  "हो जाते हैं (छन्द-चिह्न)। ‘सुखान्वितम्’ (सुख-अन्वितम्, ‘सुख से युक्त’) पढ़ने पर १६ अक्षर "
                  "बैठते हैं। पाठ में ‘अमितम् लेभे’, ‘अनधिकम् तच्च’ में अनुस्वार की जगह म् लिखा है; यह केवल "
                  "लेखन-शैली है। ‘तच्च’ = तत् + च; ‘तत्’ सम्भवतः आयुर्वेद/ज्ञान की ओर संकेत करता है। ‘शशंसानवशेषयन्’ = शशंस + "
                  "अनवशेषयन् (अ + अ → आ)।")
AIDS["26"] = {
    "frame": "कौन: भरद्वाज · क्या पाया: अमित आयु, सुख-युक्त · फिर क्या किया: ऋषियों को "
             "बताया · कैसे: न जोड़ा, न छोड़ा।",
    "chain": "आयु पाई (लेभे) → ऋषियों को बताया (शशंस) → अनधिकम् और अनवशेषयन्।",
    "seesaw": "अनधिकम् (कुछ अधिक नहीं) ↔ अनवशेषयन् (कुछ शेष नहीं छोड़ा): न बढ़ा, न घटा।",
    "sandhi": "अ + आ → आ: तेन + आयुः → तेनायुः। -उः + अ → उर्: आयुः + अमितम् → आयुरमितम्। "
              "-अः + अ → ओ ऽ: ऋषिभ्यः + अनधिकम् → ऋषिभ्यो ऽनधिकम्। त् + च → च्च: तत् + च → "
              "तच्च। अ + अ → आ: शशंस + अनवशेषयन् → शशंसानवशेषयन्।",
    "anchors": "अमित = अ + मित (जो नापा न जा सके) · अनधिक = अन् + अधिक · अवशेष = बचा हुआ · "
               "शशंस ← √शंस् (कहना)।",
    "chunks": "तेनायुरमितं लेभे | भरद्वाजः | सुखान्वितम् (छपा: सुखानिवितम्) ‖ ऋषिभ्यो "
              "ऽनधिकं तच्च | शशंसानवशेषयन्।",
}

# --------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "ऋषयश्च भरद्वाजात्",
    "question": "From whom did the sages receive Āyurveda, and why?",
    "rule": ("The sages received from Bharadvāja the Veda that is beneficial "
             "to people and increases life, because they wished to make "
             "their life long."),
    "limits": ("वर्धनम् can be an adjective, 'increasing', or an agent noun. "
               "The verse does not say how the sages put it to use."),
    "explain_hi": ("ऋषियों ने भरद्वाज से आयुर्वेद ग्रहण किया (जगृहुः)। कारण: वे अपनी आयु दीर्घ "
                   "करना चाहते थे (चिकीर्षन्तः)। इस वेद को ‘प्रजाहित’ (प्रजा के लिए हितकर) और "
                   "‘आयुषः वर्धनम्’ (आयु बढ़ाने वाला) कहा गया है। श्लोक २६ में भरद्वाज ने इसे ऋषियों को "
                   "बताया था; यहाँ ऋषियों की ओर से बात है।"),
    "hook": "ऋषि चाहते थे दीर्घ आयु → भरद्वाज से लिया प्रजाहित, आयु-वर्धक वेद।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "From whom did the sages receive the Veda in this verse?",
            ("From Bharadvāja", "भरद्वाजात् जगृहुः: they received it from Bharadvāja."),
            [("From Indra", "Indra taught Bharadvāja; the sages got it from Bharadvāja."),
             ("From Brahmā", "Brahmā is at the start of the chain, verse 4."),
             ("From Punarvasu", "Punarvasu appears in verse 30.")],
            "The sages took it from Bharadvāja.",
            "ऋषि ← भरद्वाज."),
        order(1, "Put these three in the order the knowledge passed, following verses 23 and 27.",
              ["इन्द्रः", "भरद्वाजः", "ऋषयः"],
              "Indra taught Bharadvāja (verse 23); the sages received it from Bharadvāja (verse 27).",
              "इन्द्र → भरद्वाज → ऋषि."),
        fill(2, "The sages wished to make their ____ life (Devanagari word for 'long', as in the verse).",
             ["दीर्घम्", "दीर्घं"],
             "The second line begins दीर्घमायुश्चिकीर्षन्तः.",
             "दीर्घम् goes with आयुः: a long life is what they wanted.",
             "दीर्घम् आयुः = long life."),
        mcq("discriminate", 3, "Which is the right split of ऋषयश्च?",
            ("ऋषयः + च", "A visarga before च becomes श्, so ऋषयः + च is written ऋषयश्च."),
            [("ऋषय + श्च", "श्च is not a word."),
             ("ऋषयाः + च", "The plural of ऋषि is ऋषयः, not ऋषयाः."),
             ("ऋषयश + च", "ऋषयश is not a word.")],
            "ऋषयश्च = ऋषयः + च: 'and the sages'.",
            "Visarga + च → श्च."),
        mcq("apply", 4, "Why did the sages receive the Āyurveda from Bharadvāja, according to the verse?",
            ("They wished to make their life long",
             "दीर्घमायुश्चिकीर्षन्तः: wishing to make life long."),
            [("Indra ordered them to", "Nothing like that is said here."),
             ("They wished to become rulers of the gods", "The verse names only a wish for long life."),
             ("They wished to compose a new treatise", "The verse does not say so; the treatise appears later.")],
            "The reason is stated in चिकीर्षन्तः: wishing to make (their life) long.",
            "Reason: wish for a long life."),
        mcq("transfer", 5,
            "By the rule that gives भरद्वाजाज्जगृहुः from भरद्वाजात् + जगृहुः, how is सत् + जन written?",
            ("सज्जन", "Final त् before ज is written ज्, giving ज्ज."),
            [("सत्जन", "Left unjoined, it breaks the rule shown here."),
             ("सजन", "The doubled sound ज्ज must stay."),
             ("सन्जन", "A nasal न् appears only before a nasal letter.")],
            "Final त् before ज becomes ज्: भरद्वाजात् + जगृहुः = भरद्वाजाज्जगृहुः, सत् + जन = सज्जन.",
            "त् + ज → ज्ज.",
            teaches="A word ending in त् before ज takes on ज, so the sound is doubled."),
    ],
}
NOTES_HI["27"] = ("‘वर्धनम्’ विशेषण (‘बढ़ाने वाला’) भी हो सकता है और कर्तृवाचक संज्ञा भी। ‘तम्’ और ‘वेदम्’ दोनों "
                  "आयुर्वेद के लिए हैं। ‘ऋषयश्च’ = ऋषयः + च (विसर्ग + च → श्च); ‘भरद्वाजाज्जगृहुः’ = "
                  "भरद्वाजात् + जगृहुः (त् + ज → ज्ज); ‘चिकीर्षन्तो वेदम्’ में विसर्ग घोष ‘व’ से पहले ओ बना। "
                  "‘दीर्घमायुः’ = दीर्घम् + आयुः।")
AIDS["27"] = {
    "frame": "कौन: ऋषि · किससे: भरद्वाज · क्या: प्रजाहित, आयु बढ़ाने वाला वेद · क्यों: दीर्घ "
             "आयु की इच्छा।",
    "chain": "इन्द्र → भरद्वाज (श्लोक २३) → ऋषि (यहाँ, जगृहुः)।",
    "story": "लम्बी आयु चाहने वाले ऋषि भरद्वाज से वह वेद ग्रहण करते हैं जो प्रजा का "
             "हित करता है और आयु बढ़ाता है।",
    "anchors": "प्रजाहित = प्रजा + हित · चिकीर्षन्तः ← √कृ की इच्छा (करना चाहते हुए) · "
               "वर्धन = बढ़ाने वाला (वृद्धि)।",
    "sandhi": "-अः/-उः + च → श्च: ऋषयः + च → ऋषयश्च; आयुः + चिकीर्षन्तः → आयुश्चिकीर्षन्तः। "
              "त् + ज → ज्ज: भरद्वाजात् + जगृहुः → भरद्वाजाज्जगृहुः। -अः + घोष → ओ: चिकीर्षन्तः "
              "+ वेदम् → चिकीर्षन्तो वेदम्।",
    "chunks": "ऋषयश्च | भरद्वाजाज्जगृहुः | तं प्रजाहितम् ‖ दीर्घमायुश्चिकीर्षन्तो | वेदं "
              "वर्धनमायुषः।",
}

# --------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "महर्षयस्ते ददृशुः",
    "question": "What did the great sages see with the eye of knowledge?",
    "rule": ("They saw properly, with the eye of knowledge, commonality "
             "(सामान्य), distinctiveness (विशेष), qualities (गुण), "
             "substances (द्रव्य) and action (कर्म). The sentence goes on "
             "in verse 29."),
    "limits": ("The verse names the items but does not define them. "
               "यथावत् may go with the seeing or with the items ('as they "
               "are'). The printed दड्र्शुः is a slip for ददृशुः (see the "
               "note)."),
    "explain_hi": ("महर्षियों ने ज्ञान-चक्षु से यथावत् पाँच बातें देखीं: सामान्य, विशेष, गुण, द्रव्य "
                   "और कर्म। यह वाक्य अधूरा है और श्लोक २९ में चलता है, जहाँ समवाय जुड़ता है। इस श्लोक में "
                   "इन शब्दों की परिभाषा नहीं दी गई, केवल नाम हैं। ‘महर्षयस्ते’ में विसर्ग ‘त’ से पहले ‘स्’ "
                   "बन गया है।"),
    "hook": "सामान्य – विशेष – गुण – द्रव्य – कर्म (→ समवाय, श्लोक २९)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which item does the list in verse 28 begin with?",
            ("सामान्यम् (commonality)",
             "The second line starts सामान्यं च विशेषं च."),
            [("कर्म (action)", "कर्म comes last in this verse."),
             ("समवायः (inherence)", "समवाय is added in verse 29."),
             ("द्रव्याणि (substances)", "द्रव्याणि comes fourth, not first.")],
            "The list runs सामान्य, विशेष, गुण, द्रव्य, कर्म.",
            "First item: सामान्यम्."),
        order(1, "Put the items in the order of the verse.",
              ["सामान्यम्", "विशेषम्", "गुणान्", "द्रव्याणि", "कर्म"],
              "They follow one another in the second line.",
              "सामान्य → विशेष → गुण → द्रव्य → कर्म."),
        fill(2, "The last item of the list, meaning 'action', is ____ (type it in Devanagari).",
             ["कर्म"],
             "The line ends गुणान् द्रव्याणि कर्म च.",
             "कर्म is the last of the five items in this verse; the sentence continues with one more item in verse 29.",
             "कर्म = action, the fifth item."),
        mcq("discriminate", 3, "Why is महर्षयः + ते written महर्षयस्ते?",
            ("A visarga before त becomes स्",
             "The visarga becomes स् before the dental त."),
            [("A visarga becomes ओ before a voiced letter", "त is not voiced, and ओ follows only -अः before voiced letters."),
             ("A visarga becomes र् before a vowel", "ते begins with a consonant, not a vowel."),
             ("The visarga drops out before any consonant", "Before त it becomes स्.")],
            "Visarga + त → स्त: महर्षयः + ते = महर्षयस्ते.",
            "Visarga + त → स्त."),
        mcq("apply", 4, "The verse ends with कर्म च, but its sentence goes on in verse 29. What does that tell you about the list?",
            ("It is not complete; समवाय follows in verse 29",
             "Verse 29 begins समवायं च: one more item of the same sentence."),
            [("It is complete at five", "Verse 29 adds another item to the same sentence."),
             ("समवाय is a different sentence", "यत् in verse 29 refers back to the whole list, so the sentence continues."),
             ("The list repeats from the start", "Nothing repeats; a new item is added.")],
            "The list continues in the next verse.",
            "Verse 28 + verse 29 = one sentence."),
        mcq("transfer", 5,
            "By the rule that gives महर्षयस्ते from महर्षयः + ते, how is मुनयः + तत्र written?",
            ("मुनयस्तत्र", "A visarga before त becomes स्."),
            [("मुनयोतत्र", "ओ appears only after -अः before a voiced letter."),
             ("मुनयतत्र", "The visarga does not simply vanish before त."),
             ("मुनयरतत्र", "र् appears only before a vowel or a voiced letter.")],
            "Visarga + त → स्त: मुनयः + तत्र = मुनयस्तत्र.",
            "Visarga + त → स्त.",
            teaches="Before a त, a visarga turns into स् and joins the next word."),
    ],
}
NOTES_HI["28"] = ("पाठ में ‘दड्र्शुः’ छपा है (देवनागरी में भी ‘दड्र्शु’); अपेक्षित ‘ददृशुः’ है (श्लोक १७ में "
                  "भी ‘ददृशुः’ आया है); पंक्ति में १५ अक्षर गिने जाते हैं और ‘ददृशुः’ पढ़ने पर १६ हो जाते हैं। "
                  "‘यथावत्’ को ‘ददृशुः’ के साथ (ठीक देखा) या विषयों के साथ (जैसे वे हैं) पढ़ा जा सकता है। "
                  "‘महर्षयस्ते’ = महर्षयः + ते। वाक्य श्लोक २९ तक चलता है।")
AIDS["28"] = {
    "frame": "कौन: महर्षि · कैसे: ज्ञान-चक्षु से, यथावत् · क्या देखा: सामान्य, विशेष, गुण, "
             "द्रव्य, कर्म (समवाय अगले श्लोक में)।",
    "chain": "सामान्य → विशेष → गुण → द्रव्य → कर्म (→ समवाय, श्लोक २९)।",
    "diagram": {"groups": [
        {"label": "कौन", "items": ["महर्षयः", "ते"]},
        {"label": "कैसे", "items": ["यथावत्", "ज्ञानचक्षुषा"]},
        {"label": "क्या", "items": ["सामान्यं", "विशेषं", "गुणान्", "द्रव्याणि", "कर्म"]}]},
    "letters": "सा-वि-गु-द्र-क: सामान्य · विशेष · गुण · द्रव्य · कर्म।",
    "seesaw": "सामान्यम् ↔ विशेषम्: पहली दो वस्तुएँ विपरीत जोड़ी जैसी रखी गई हैं (अर्थ की व्याख्या "
              "इस श्लोक में नहीं)।",
    "sandhi": "-अः + त → स्त: महर्षयः + ते → महर्षयस्ते। -उः + य → उर्य: ददृशुः + यथावत् → "
              "ददृशुर्यथावत्। त् + ज्ञ → ज्ज्ञ: यथावत् + ज्ञानचक्षुषा → यथावज्ज्ञानचक्षुषा।",
    "anchors": "ज्ञानचक्षु = ज्ञान + चक्षु (ज्ञान की आँख) · महर्षि = महा + ऋषि · सामान्य ← "
               "समान।",
    "chunks": "महर्षयस्ते | ददृशुः | यथावज्ज्ञानचक्षुषा ‖ सामान्यं च विशेषं च | "
              "गुणान् द्रव्याणि कर्म च।",
}

# --------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "समवायं च यज्ज्ञात्वा",
    "question": "What is added to the list, and what did the sages gain by knowing it?",
    "rule": ("The list is completed with समवाय (inherence). Having known "
             "these and followed the regimen laid down in the treatise, the "
             "sages obtained the highest well-being and a life that is not "
             "transient."),
    "limits": ("यत् is taken to refer to the whole group of items from "
               "verses 28 and 29. अनित्वरम् is 'not transient', that is "
               "long-lasting; the verse does not say literally eternal."),
    "explain_hi": ("श्लोक २८ की सूची यहाँ पूरी होती है: समवाय। इन सबको जानकर (ज्ञात्वा) और शास्त्र में "
                   "कही विधि पर टिककर (आस्थिताः) ऋषियों ने परम सुख (शर्म) और अनित्वर, यानी "
                   "अस्थायी न रहने वाला, जीवन पाया। ‘ज्ञात्वा’ में उपसर्ग नहीं है, इसलिए ‘-त्वा’ है। "
                   "‘तन्त्रोक्तम्’ = तन्त्र + उक्तम्, ‘शास्त्र में कहा गया’।"),
    "hook": "समवाय जोड़ा → जानो और विधि अपनाओ → परम शर्म + अनित्वर जीवन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which item does verse 29 add to the list begun in verse 28?",
            ("समवायः (inherence)", "The verse opens समवायं च: and inherence."),
            [("गुणः (quality)", "गुण is already in verse 28."),
             ("कर्म (action)", "कर्म is already in verse 28."),
             ("सामान्यम् (commonality)", "सामान्य is already in verse 28.")],
            "समवाय completes the list.",
            "Verse 29 adds समवाय."),
        match(1, "Match each word to its meaning.",
              [["ज्ञात्वा", "having known"], ["विधिम्", "the regimen, the rule"],
               ["लेभिरे", "they obtained"], ["शर्म", "well-being"]],
              "These four words carry the verse's chain: know, follow, obtain.",
              "ज्ञात्वा = having known; विधिम् = regimen; लेभिरे = they obtained; शर्म = well-being."),
        fill(2, "The word meaning 'not transient' in the last line is ____ (type it in Devanagari).",
             ["अनित्वरम्", "अनित्वरं"],
             "The last words are जीवितं चाप्यनित्वरम्.",
             "अनित्वरम् is अन् + इत्वरम्, 'not passing': the life they gained does not fade quickly.",
             "अनित्वर = not transient, long-lasting."),
        mcq("discriminate", 3, "Why does ज्ञात्वा end in -त्वा rather than -य?",
            ("The root ज्ञा here has no prefix",
             "The ‘having done’ form of a root without prefix ends in -त्वा."),
            [("Because the sentence is about the past", "That is not what decides it; the prefix does."),
             ("Because the word is plural", "-त्वा does not mark number."),
             ("Because it is a command", "It is not a command; it means 'having known'.")],
            "No prefix → -त्वा (ज्ञात्वा, बुद्ध्वा); a prefix → -य (अभिनन्द्य).",
            "No prefix: -त्वा. Prefix: -य."),
        multi("apply", 4, "Which two things did the sages obtain, according to this verse? Pick all that apply.",
              [("The highest well-being (शर्म)", "Right: परमं शर्म."),
               ("A life that is not transient", "Right: जीवितं चाप्यनित्वरम्."),
               ("Rulership of the gods", "Wrong: no such gain is mentioned."),
               ("Great wealth", "Wrong: wealth is not mentioned.")],
              [0, 1],
              "The verse names exactly these two gains.",
              "परमं शर्म + अनित्वरं जीवितम्."),
        mcq("transfer", 5,
            "By the rule that gives तन्त्रोक्तम् from तन्त्र + उक्तम्, how is शास्त्र + उक्त written?",
            ("शास्त्रोक्त", "अ + उ gives ओ."),
            [("शास्त्रुक्त", "The अ does not disappear leaving उ."),
             ("शास्त्रौक्त", "अ + उ gives ओ, not औ."),
             ("शास्त्राक्त", "The उ does not become अ.")],
            "अ + उ → ओ: शास्त्र + उक्त = शास्त्रोक्त, like तन्त्र + उक्तम् = तन्त्रोक्तम्.",
            "अ + उ → ओ.",
            teaches="Any word ending in -अ followed by उ merges into ओ."),
    ],
}
NOTES_HI["29"] = ("‘यत्’ (नपुंसक एकवचन) श्लोक २८ और २९ के सभी छह पदार्थों का सामूहिक संकेत माना गया है। "
                  "‘तन्त्र’ = शास्त्र (आयुर्वेद)। ‘अनित्वरम्’ का भाव ‘क्षणिक नहीं’ है, यानी दीर्घकालिक; ‘शाश्वत’ "
                  "नहीं। ‘यज्ज्ञात्वा’ = यत् + ज्ञात्वा; ‘तन्त्रोक्तम्’ = तन्त्र + उक्तम्; "
                  "‘विधिमास्थिताः’ = विधिम् + आस्थिताः; ‘चाप्यनित्वरम्’ = च + अपि + अनित्वरम्।")
AIDS["29"] = {
    "frame": "क्या जोड़ा: समवाय · क्या किया: जाना (ज्ञात्वा) और विधि अपनाई (आस्थिताः) · क्या "
             "पाया: परम शर्म, अनित्वर जीवित।",
    "chain": "ज्ञात्वा (जानकर) → आस्थिताः (विधि पर टिके) → लेभिरे (पाया)।",
    "story": "ऋषियों ने सूची के सभी पदार्थ समझे, शास्त्र की विधि पर चले, और सुख तथा दीर्घ जीवन "
             "पाया।",
    "sandhi": "त् + ज्ञ → ज्ज्ञ: यत् + ज्ञात्वा → यज्ज्ञात्वा। अ + उ → ओ: तन्त्र + उक्तम् → "
              "तन्त्रोक्तम्। म् + आ: विधिम् + आस्थिताः → विधिमास्थिताः। अ + अ → आ: च + अपि → "
              "चापि; इ + अ → य: अपि + अनित्वरम् → अप्यनित्वरम्।",
    "anchors": "तन्त्र = शास्त्र · विधि = नियम · शर्म = सुख · अनित्वर = न + इत्वर (जो क्षणिक "
               "नहीं)।",
    "contrast": "ज्ञात्वा (यहाँ, उपसर्ग नहीं, -त्वा) ↔ अभिनन्द्य (श्लोक २१, उपसर्ग अभि-, -य)।",
    "chunks": "समवायं च | यज्ज्ञात्वा | तन्त्रोक्तं विधिमास्थिताः ‖ लेभिरे परमं शर्म | "
              "जीवितं चाप्यनित्वरम्।",
}

# --------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "अथ मैत्रीपरः पुण्यम्",
    "question": "Who gave Āyurveda to six disciples, and why?",
    "rule": ("Then Punarvasu, devoted to friendliness, gave the holy "
             "Āyurveda to six disciples, out of compassion for all beings. "
             "The disciples are named in the next verse."),
    "limits": ("The verse does not name the disciples or say how Punarvasu "
               "received the teaching. That Punarvasu is Ātreya is stated "
               "in a later unit, not here."),
    "explain_hi": ("अब परम्परा का नया चरण है: पुनर्वसु, जो मैत्री-परायण थे, ने सब प्राणियों पर "
                   "अनुकम्पा से पुण्य आयुर्वेद छह शिष्यों को दिया (दत्तवान्)। इस श्लोक में शिष्यों के "
                   "नाम नहीं हैं; वे अगले श्लोक में आते हैं। ‘षड्भ्यः’ ‘शिष्येभ्यः’ का विशेषण है: "
                   "‘छह को’।"),
    "hook": "पुनर्वसु ने, अनुकम्पा से, पुण्य आयुर्वेद छह शिष्यों को दिया।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Who gave Āyurveda to six disciples in this verse?",
            ("Punarvasu", "पुनर्वसुः … दत्तवान् षड्भ्यः: Punarvasu gave it to six."),
            [("Bharadvāja", "Bharadvāja gave it to the sages, in verses 26 and 27."),
             ("Indra", "Indra taught Bharadvāja, verse 23."),
             ("Agniveśa", "Agniveśa is named as a receiver in the next verse.")],
            "Punarvasu is the giver; six disciples are the receivers.",
            "Punarvasu → six disciples."),
        match(1, "Match each word to its meaning.",
              [["शिष्येभ्यः", "to the disciples"], ["षड्भ्यः", "to six"],
               ["दत्तवान्", "he gave"], ["अनुकम्पया", "out of compassion"]],
              "षड्भ्यः goes with शिष्येभ्यः: 'to the six disciples'.",
              "शिष्येभ्यः = to the disciples; षड्भ्यः = to six; दत्तवान् = he gave; अनुकम्पया = out of compassion."),
        fill(2, "Type the last word of the verse, which means 'out of compassion for all beings' (Devanagari): ____.",
             ["सर्वभूतानुकम्पया"],
             "The verse ends सर्वभूतानुकम्पया: out of compassion for all beings.",
             "अनुकम्पा is compassion; the ending -या means 'by, out of': his reason for giving.",
             "अनुकम्पया = out of compassion, the reason."),
        mcq("discriminate", 3, "Why is शिष्येभ्यः written शिष्येभ्यो before दत्तवान्?",
            ("A visarga after -अ becomes ओ before a voiced consonant such as द",
             "-अः + voiced consonant → ओ."),
            [("The ओ shows a call, 'O disciples'", "This is a sandhi result, not a calling form."),
             ("The ओ marks the dual", "The word means 'to the disciples', plural."),
             ("The visarga becomes र्", "र् follows other vowels, not -अ.")],
            "शिष्येभ्यः + दत्तवान् → शिष्येभ्यो दत्तवान्.",
            "-अः + voiced consonant → ओ."),
        mcq("apply", 4, "What does षड्भ्यः add to शिष्येभ्यः?",
            ("It gives their number, six",
             "षट् is six; षड्भ्यः is 'to six'."),
            [("It names them", "The names come in the next verse."),
             ("It gives their country", "No country is mentioned."),
             ("It says they were gods", "Nothing like that is said.")],
            "षड्भ्यः says six; the names follow in verse 31.",
            "षड्भ्यः = to six."),
        mcq("transfer", 5,
            "By the pattern शिष्येभ्यः + दत्तवान् → शिष्येभ्यो दत्तवान्, how is वृक्षेभ्यः + जलम् written?",
            ("वृक्षेभ्यो जलम्", "-अः before a voiced consonant (ज) becomes ओ."),
            [("वृक्षेभ्यः जलम्", "The visarga does not stay before a voiced letter in joined text."),
             ("वृक्षेभ्यर्जलम्", "र् follows other vowels, not -अ."),
             ("वृक्षेभ्यस्जलम्", "स् appears before त or थ, not before ज.")],
            "-अः + voiced consonant → ओ.",
            "-अः before a voiced consonant → ओ.",
            teaches="Any plural dative in -एभ्यः becomes -एभ्यो before a voiced consonant or अ."),
    ],
}
NOTES_HI["30"] = ("‘पुण्यम्’ आयुर्वेदम् का विशेषण है। ‘पुनर्वसुः’ में ‘पुनः’ अव्यय है जिसका विसर्ग मूलतः र् है, इसलिए "
                  "घोष ‘व’ से पहले र् ही रहा। ‘शिष्येभ्यो दत्तवान्’ में -अः घोष द् से पहले ओ बना। ‘षड्भ्यः’ "
                  "= षष् + भ्यः (ष् → ड् घोष भ् से पहले)। ‘पुण्यमायुर्वेदम्’ = पुण्यम् + आयुर्वेदम्। पुनर्वसु का "
                  "आत्रेय होना यहाँ नहीं, बाद में कहा गया है।")
AIDS["30"] = {
    "frame": "कौन: मैत्रीपर पुनर्वसु · किसे: षड् शिष्य · क्या: पुण्य आयुर्वेद · क्यों: सब "
             "प्राणियों पर अनुकम्पा।",
    "chain": "अनुकम्पा (कारण) → दत्तवान् (दिया) → शिष्येभ्यः षड्भ्यः (छह को)।",
    "pegs": "छह दीपक (मेरा बनाया चित्र): एक दीप से छह दीप जलते हैं, जैसे एक गुरु से छह शिष्य।",
    "sandhi": "-अः + द → ओ: शिष्येभ्यः + दत्तवान् → शिष्येभ्यो दत्तवान्। पुनः + वसुः → "
              "पुनर्वसुः (पुनः का विसर्ग र् है)। षष् + भ्यः → षड्भ्यः। सर्वभूत + अनुकम्पया → "
              "सर्वभूतानुकम्पया।",
    "anchors": "मैत्रीपर = मैत्री + पर (मैत्री में लगा) · अनुकम्पा = दया · दत्तवान् ← √दा "
               "(देना) · षड् = छह।",
    "chunks": "अथ मैत्रीपरः | पुण्यमायुर्वेदं पुनर्वसुः ‖ शिष्येभ्यो दत्तवान् | षड्भ्यः | "
              "सर्वभूतानुकम्पया।",
}
