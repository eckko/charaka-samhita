from ch1_authored import mcq, match, order, fill, multi

AUTHORED = {}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "एकादशावशिष्टा याः",
    "question": "How many mūlinīs remain for purgation, and what does the verse turn to next?",
    "rule": ("The eleven that remain are to be used in virecana (purgation). "
             "So the mūlinīs have been described by name and action; now hear "
             "the phalinīs (fruit-drugs)."),
    "limits": ("The verse gives the number eleven, not their names; the count "
               "16 − 3 − 2 comes from verses 78-79. It does not say what "
               "'action' (कर्म) covers beyond the uses just stated."),
    "explain_hi": ("श्लोक ७८ में मूलिनियाँ सोलह गिनी गईं; श्लोक ७९ में तीन को "
                   "वमन में और दो को शिरोविरेचन में रखा गया। १६ − ३ − २ = ११; "
                   "इन्हीं बची हुई ग्यारह को यह श्लोक विरेचन में प्रयोज्य कहता है। "
                   "‘नामकर्मभ्याम्’ का अर्थ है ‘नाम और कर्म से’: नाम गिनाए गए और "
                   "उपयोग बताए गए। अन्त में विषय बदलता है: मूलिनियाँ पूरी हुईं, अब "
                   "‘फलिनीः’ (फल वाली औषधियाँ) सुनो।"),
    "hook": "ग्यारह बचीं → विरेचन; मूलिनी पूरी (नाम + कर्म) → अब फलिनी सुनो।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 79 puts three of the sixteen mūlinīs in emesis and two in head-purgation. How many are left for purgation?",
            ("Eleven (16 − 3 − 2)", "The rest of the sixteen after the five already placed."),
            [("Five", "Five is the number already placed, not the number left."),
             ("Thirteen", "That forgets the two placed in head-purgation."),
             ("Sixteen", "Sixteen is the whole set; five are already placed elsewhere.")],
            "The verse itself says एकादश (eleven) remain for virecana.",
            "16 mūlinīs − 3 (emesis) − 2 (head-purgation) = 11 for purgation."),
        match(1, "Match each word of the verse to its meaning.",
              [["एकादश", "eleven"], ["अवशिष्टाः", "remaining"],
               ["विरेचने", "in purgation"], ["शृणु", "hear"]],
              "These four words carry the verse's two statements.",
              "एकादश = eleven; अवशिष्टाः = remaining; विरेचने = in purgation; शृणु = hear."),
        fill(2, "The last word of verse 80 is a command meaning 'hear'. Type it in Devanagari: ____",
             ["शृणु"],
             "शृणु is the imperative of √श्रु, 'hear'.",
             "फलिनीः शृणु = 'hear the phalinīs': the verse hands over to the next topic.",
             "शृणु = hear (command); it ends the mūlinī section."),
        mcq("discriminate", 3,
            "In मूलिन्यः फलिनीः शृणु, which word is the thing to be heard, the object of शृणु?",
            ("फलिनीः", "It is accusative plural: 'hear the phalinīs'."),
            [("मूलिन्यः", "It is nominative plural, the subject of उक्ताः: 'the mūlinīs have been described'."),
             ("नामकर्मभ्याम्", "It means 'by name and action' and says how the mūlinīs were described."),
             ("शृणु", "It is the verb itself, 'hear', not the thing heard.")],
            "मूलिन्यः are the ones already described; फलिनीः are the ones now to be heard.",
            "Nominative = subject (मूलिन्यः); accusative = object (फलिनीः)."),
        multi("apply", 4, "Which statements does verse 80 make?",
              [("The eleven that remain are to be used in purgation.", "Right: प्रयोज्यास्ता विरेचने."),
               ("The mūlinīs have been described by name and action.", "Right: इत्युक्ता नामकर्मभ्यां मूलिन्यः."),
               ("Now the phalinīs are to be heard.", "Right: फलिनीः शृणु."),
               ("The eleven that remain are for emesis.", "Wrong: they are for virecana (purgation)."),
               ("The phalinīs have already been described.", "Wrong: they are only announced here.")],
              [0, 1, 2],
              "The verse closes the mūlinīs and opens the phalinīs.",
              "Eleven for purgation; mūlinīs done; phalinīs next."),
        mcq("transfer", 5,
            "A new text lists 20 herbs: 5 are sent to bath and 4 to massage. By the method of verse 80, how many remain for drinking?",
            ("Eleven (20 − 5 − 4)", "The remainder after the uses already assigned."),
            [("Nine", "Nine is the size of the two assigned groups together, not the remainder."),
             ("Fifteen", "That subtracts only the bath herbs."),
             ("Sixteen", "That subtracts only the massage herbs.")],
            "As in verses 79-80, the remainder is the total minus the groups already placed.",
            "Remaining = total − the groups already assigned.",
            teaches="When a text assigns some drugs to uses and says the rest remain for one more use, subtract the assigned groups from the total."),
    ],
}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "शङ्खिन्यथ विडङ्गानि",
    "question": "Which fruit-drugs open the list of phalinīs?",
    "rule": ("Begins the list of phalinīs: शङ्खिनी, विडङ्ग, त्रपुष, मदन, "
             "धामार्गव, इक्ष्वाकु, जीमूत, कृतवेधन, and क्लीतक, known to be "
             "twofold: आनूप (marshland) and स्थलज (dry land)."),
    "limits": ("The verse names plants only; it gives no identification and "
               "no use here. The printed द्विदिधं is not a word; द्विविधं "
               "('twofold') is the suggested reading. The list continues in "
               "verses 82-83."),
    "explain_hi": ("‘फलिनीः शृणु’ (श्लोक ८०) के बाद यहाँ फलिनियों की सूची शुरू "
                   "होती है। पहली अर्ध-पंक्ति में शङ्खिनी, विडङ्ग, त्रपुष और मदन हैं; "
                   "दूसरी में धामार्गव, इक्ष्वाकु, जीमूत और कृतवेधन। तीसरी में "
                   "क्लीतक को ‘दो प्रकार’ का कहा गया है: आनूप (जलप्राय भूमि का) "
                   "और स्थलज (सूखी भूमि का)। ‘शङ्खिन्यथ’ में शङ्खिनी + अथ का "
                   "ई, अगले स्वर से पहले ‘य्’ बन गया है। छपा ‘द्विदिधं’ संभवतः "
                   "‘द्विविधं’ है (पाठ-टिप्पणी देखें)।"),
    "hook": "श-वि-त्र-म | धा-इ-जी-कृ | क्लीतक दो: आनूप + स्थलज।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 80 ended with 'now hear the phalinīs'. What kind of text do you expect in verse 81?",
            ("A list of names of fruit-drugs", "Hearing the phalinīs means hearing them named."),
            [("A list of diseases", "Nothing in verse 80 announces diseases."),
             ("The story of a sage", "The story part of the chapter is long over."),
             ("A rule about food", "Verse 80 promises fruit-drugs, not food rules.")],
            "Verse 81 begins naming the phalinīs.",
            "After 'hear the phalinīs', the names follow."),
        match(1, "Match each Devanagari name to its Latin spelling.",
              [["शङ्खिनी", "Śaṅkhinī"], ["मदनानि", "Madana"],
               ["जीमूतम्", "Jīmūta"], ["कृतवेधनम्", "Kṛtavedhana"]],
              "Reading the plant names in Devanagari is the point of this card.",
              "शङ्खिनी = Śaṅkhinī; मदनानि = Madana; जीमूतम् = Jīmūta; कृतवेधनम् = Kṛtavedhana."),
        fill(2, "क्लीतक is said to be of two kinds: आनूप (marshland) and ____ (dry land). Type the second kind in Devanagari.",
             ["स्थलज", "स्थलजम्", "स्थलजं"],
             "स्थलजम् is the dry-land kind of क्लीतक.",
             "The verse gives क्लीतक two kinds: आनूपम् (growing in marshland) and स्थलजम् (growing on dry land).",
             "क्लीतक = आनूप + स्थलज."),
        mcq("discriminate", 3, "Which is the right split of शङ्खिन्यथ?",
            ("शङ्खिनी + अथ", "ई before a different vowel becomes य्: शङ्खिनी + अथ is written शङ्खिन्यथ."),
            [("शङ्खिन्य + थ", "थ is not a word."),
             ("शङ्खिना + अथ", "आ + अ would merge into आ and give शङ्खिनाथ."),
             ("शङ्खिनः + अथ", "That would give शङ्खिनोऽथ, with ओ.")],
            "शङ्खिन्यथ = शङ्खिनी (the plant) + अथ (then).",
            "ई + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which of these are named in verse 81 itself?",
              [("मदनम्", "Right: मदनानि च is in the first half-line."),
               ("हस्तिपर्णी", "Wrong: it comes in verse 82."),
               ("जीमूतम्", "Right: it is in the second half-line."),
               ("कुटजम्", "Wrong: it comes in verse 83."),
               ("त्रपुषम्", "Right: it is in the first half-line.")],
              [0, 2, 4],
              "Three of the five are in verse 81; the others come in the next verses.",
              "81: शङ्खिनी, विडङ्ग, त्रपुष, मदन | धामार्गव, इक्ष्वाकु, जीमूत, कृतवेधन | क्लीतक."),
        mcq("transfer", 5,
            "A new line says अन्नं त्रिविधं स्मृतम्, meaning food is known to be of how many kinds, by the verse-81 pattern?",
            ("Threefold: three kinds of food follow", "Number + विध means '-fold', as in द्विविध, twofold."),
            [("Twofold", "त्रि is three; द्वि would be two."),
             ("Fourfold", "चतुर् would be four."),
             ("Of no kind at all", "विध means a kind or fold; the line names kinds.")],
            "द्विविधं gives 'twofold'; त्रिविधं gives 'threefold' in the same way.",
            "Number + विध = so many kinds.",
            teaches="A number word before -विध tells how many kinds the text will name."),
    ],
}

# ---------------------------------------------------------------- unit 82
AUTHORED["82"] = {
    "title": "प्रकीर्या चोदकीर्या",
    "question": "Which phalinīs does verse 82 add to the list?",
    "rule": ("Continues the phalinīs: प्रकीर्या, उदकीर्या, प्रत्यक्पुष्पा, "
             "अभया, अन्तःकोटरपुष्पी, and the autumnal fruit of हस्तिपर्णी."),
    "limits": ("The verse gives no use here. 'Fruit' is understood with "
               "शारदम् and is not written. The printed तथा ऽभया shows the two "
               "words apart; ordinary sandhi would write तथाभया."),
    "explain_hi": ("सूची आगे बढ़ती है। पहली पंक्ति में प्रकीर्या, उदकीर्या, "
                   "प्रत्यक्पुष्पा और अभया हैं; दूसरी में अन्तःकोटरपुष्पी और "
                   "हस्तिपर्णी का शारद (शरद् ऋतु का) फल। ‘शारदम्’ नपुंसक है, "
                   "इसलिए उसके साथ ‘फलम्’ समझा जाता है, जो शब्द रूप में लिखा नहीं है। "
                   "‘चोदकीर्या’ = च + उदकीर्या, और ‘हस्तिपर्ण्याश्च’ में विसर्ग "
                   "‘च’ से पहले ‘श्’ हो गया है।"),
    "hook": "प्रकीर्या · उदकीर्या · प्रत्यक्पुष्पा · अभया | अन्तःकोटरपुष्पी · हस्तिपर्णी का शारद फल।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 81 began the phalinīs and its list was not finished. What do you expect verse 82 to do?",
            ("Go on naming more phalinīs", "The list continues across verses 81-83."),
            [("Start a list of salts", "The salts come much later, in verses 88-89."),
             ("State the uses of all of them", "The uses begin only in verse 83, line 2."),
             ("Close the chapter", "The chapter goes on for many more verses.")],
            "Verse 82 gives six more phalinīs.",
            "The phalinī list runs on from 81 into 82."),
        match(1, "Match each Devanagari name to its Latin spelling.",
              [["प्रकीर्या", "Prakīryā"], ["उदकीर्या", "Udakīryā"],
               ["अभया", "Abhayā"], ["अन्तःकोटरपुष्पी", "Antaḥkoṭarapuṣpī"]],
              "Reading the plant names in Devanagari is the point of this card.",
              "प्रकीर्या = Prakīryā; उदकीर्या = Udakīryā; अभया = Abhayā; अन्तःकोटरपुष्पी = Antaḥkoṭarapuṣpī."),
        fill(2, "चोदकीर्या is a joined form: च + ____ (type the plant name in Devanagari).",
             ["उदकीर्या"],
             "च + उदकीर्या = चोदकीर्या.",
             "अ + उ → ओ: च + उदकीर्या is written चोदकीर्या.",
             "च + उ… → चो…"),
        mcq("discriminate", 3, "Which is the right split of हस्तिपर्ण्याश्च?",
            ("हस्तिपर्ण्याः + च", "A visarga before च becomes श्, so हस्तिपर्ण्याः + च is written हस्तिपर्ण्याश्च."),
            [("हस्तिपर्ण्या + श्च", "श्च is not a word."),
             ("हस्तिपर्णी + याश्च", "याश्च is not a word."),
             ("हस्तिपर्ण्याः + श्च", "The श् comes from the visarga; it is not a separate word.")],
            "हस्तिपर्ण्याः is genitive: 'of हस्तिपर्णी', and च follows.",
            "Visarga + च → श्च."),
        mcq("apply", 4,
            "A reader sees शारदम् ('autumnal') with no noun after हस्तिपर्ण्याः. What does the card say is understood?",
            ("फलम्, the fruit, so 'the autumnal fruit of हस्तिपर्णी'", "The list is of phalinīs (fruit-drugs), and शारदम् is neuter like फलम्."),
            [("मूलम्, the root", "Roots belong to the mūlinīs, already finished."),
             ("पत्रम्, the leaf", "Nothing in the verses speaks of leaves."),
             ("Nothing is understood; it is a name on its own", "शारदम् is an adjective, 'autumnal', and needs a noun.")],
            "The sentence is about phalinīs, so a fruit is understood.",
            "शारदम् (neuter, 'autumnal') takes फलम् understood."),
        mcq("transfer", 5,
            "A new line joins वचायाः and च. How is it written, by the same rule as हस्तिपर्ण्याश्च?",
            ("वचायाश्च", "The visarga of वचायाः becomes श् before च."),
            [("वचायाःच", "The visarga does not stay before च."),
             ("वचायास्च", "Before च the sound is श्, not स्."),
             ("वचायाच", "The sound श् is not dropped.")],
            "A visarga before च is written श्च, in any word.",
            "-ः + च → श्च.",
            teaches="The rule that turns the visarga into श् before च applies to any word."),
    ],
}

# ---------------------------------------------------------------- unit 83
AUTHORED["83"] = {
    "title": "कम्पिल्लकारग्वधयोः फलम्",
    "question": "What completes the phalinīs here, and what does the repeated second line begin?",
    "rule": ("Line 1 gives the fruit of कम्पिल्लक, आरग्वध and कुटज, completing "
             "the nineteen. Line 2 repeats धामार्गव, इक्ष्वाकु, जीमूत, "
             "कृतवेधन and begins a new sentence about uses."),
    "limits": ("The repeated line (also in verse 81) is read as the start of "
               "a new sentence, not a scribal repeat; that reading rests on "
               "the counts of verses 84-85. The sentence is not finished here: "
               "it ends in verse 84."),
    "explain_hi": ("पहली पंक्ति में कम्पिल्लक और आरग्वध का फल तथा कुटज का फल "
                   "है; ये तीन फलिनियाँ पिछले सोलह में जुड़कर कुल उन्नीस पूरी "
                   "करती हैं। ‘कम्पिल्लकारग्वधयोः’ षष्ठी द्विवचन है: दो नामों का "
                   "द्वन्द्व, ‘दोनों का’। दूसरी पंक्ति श्लोक ८१ की दूसरी पंक्ति की "
                   "पुनरावृत्ति है, पर यहाँ वह सूची का सदस्य नहीं, बल्कि एक नए "
                   "वाक्य का आरम्भ है, जो श्लोक ८४ में पूरा होता है: ‘ये वमन और "
                   "आस्थापन में प्रयोज्य हैं’। गिनती भी इसी पाठ को सही ठहराती है "
                   "(पाठ-टिप्पणी देखें)।"),
    "hook": "पंक्ति १: कम्पिल्लक · आरग्वध · कुटज (१७–१९) | पंक्ति २: वही चार, पर नए वाक्य का आरम्भ → ८४ में पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verses 81-82 gave sixteen phalinīs in all. If the total is nineteen, how many does line 1 of verse 83 add?",
            ("Three", "19 − 16 = 3, and line 1 names three plants."),
            [("One", "One would leave the total at seventeen."),
             ("Two", "Two would leave the total at eighteen."),
             ("Nineteen", "Nineteen is the whole total, not the new part.")],
            "Line 1 names कम्पिल्लक, आरग्वध and कुटज: three more, making nineteen.",
            "16 + 3 = 19 phalinīs."),
        match(1, "Match each word to its meaning.",
              [["फलम्", "fruit"], ["यत्", "which"],
               ["कुटजस्य", "of kuṭaja"],
               ["कम्पिल्लकारग्वधयोः", "of kampillaka and āragvadha"]],
              "The first line is built on the genitive: 'the fruit of ...'.",
              "फलम् = fruit; यत् = which; कुटजस्य = of kuṭaja; कम्पिल्लकारग्वधयोः = of kampillaka and āragvadha."),
        fill(2, "The ending -योः of कम्पिल्लकारग्वधयोः is a genitive dual, so the word names ____ plants (type the number).",
             ["2", "२", "two", "Two", "दो", "द्वि"],
             "-योः here marks the genitive dual: two items.",
             "कम्पिल्लक and आरग्वध are joined in one word with a dual ending: 'of the two'.",
             "-योः = 'of the two'."),
        mcq("discriminate", 3,
            "Line 2 repeats words of verse 81. As the card reads it, what is the difference?",
            ("In 81 they are list members; in 83 they begin a statement of uses", "The same four fruits are first named, then used as the start of a new sentence."),
            [("In 83 they are new phalinīs, numbers 20-23", "The total is nineteen, completed in line 1."),
             ("In 83 they are mūlinīs", "The mūlinīs were finished in verse 80."),
             ("The line in 83 is only a copying error", "The card reads it as genuine: the counts of verses 84-85 need it.")],
            "The repeated line is the opening of a sentence that ends in verse 84.",
            "81 line 2: list members. 83 line 2: subject of the next sentence."),
        mcq("apply", 4,
            "The sentence begun in line 2 of verse 83 has no verb yet. Where does it end?",
            ("In verse 84, where the fruits are said to be used in emesis and āsthāpana", "Verse 84 gives the verb योज्यानि."),
            [("In verse 82, before it starts", "Verse 82 comes before 83 and cannot finish it."),
             ("In verse 83, line 1", "Line 1 is a separate statement about the fruit of three plants."),
             ("It never ends", "Verse 84 completes it.")],
            "Verses 83 (line 2) and 84 form one sentence.",
            "Verse 83 line 2 + verse 84 = one sentence of use."),
        mcq("transfer", 5,
            "12 jars are listed; 4 are repeated as for sale, 3 go as gifts, 5 stay in the shop. Is the repeat a mistake?",
            ("No: 12 − 4 − 3 = 5, so the repeated four are needed in the count", "The repeat starts a new statement, and the counts fit it."),
            [("Yes: a repeated name is always an error", "Counts can show that a repeat is deliberate."),
             ("Yes: the book should list only 8 jars", "That would break the stated 5 for the shop."),
             ("It cannot be told by counting", "Here the counting settles it.")],
            "As in verses 83-85, check the counts before calling a repeated line an error.",
            "A repeat that makes the stated counts work is not a scribal error.",
            teaches="Before deleting a repeated line as a copying error, test whether the counts the text states depend on it."),
    ],
}

# ---------------------------------------------------------------- unit 84
AUTHORED["84"] = {
    "title": "मदनं कुटजं चैव",
    "question": "Where are the eight fruits to be used?",
    "rule": ("मदन, कुटज, त्रपुष and हस्तिपर्णिनी, together with the four of verse "
             "83 line 2, are to be used in emesis (वमन) and in "
             "āsthāpana (decoction enema)."),
    "limits": ("The verse finishes the sentence of verse 83 and says only "
               "where these are used, not how. 'These' (एतानि) covers all "
               "eight fruits named in 83 line 2 and here."),
    "explain_hi": ("यह श्लोक श्लोक ८३ की दूसरी पंक्ति से चले वाक्य को पूरा करता है। "
                   "वहाँ चार फल थे (धामार्गव, इक्ष्वाकु, जीमूत, कृतवेधन); यहाँ चार और "
                   "(मदन, कुटज, त्रपुष, हस्तिपर्णिनी) जुड़ते हैं। ‘एतानि’ इन सभी आठों "
                   "के लिए है। क्रिया ‘योज्यानि’ (प्रयोग करने योग्य) है, और स्थान दो हैं: "
                   "‘वमने’ (वमन में, एकवचन) तथा ‘आस्थापनेषु’ (आस्थापन-बस्तियों में, "
                   "बहुवचन)। ‘योज्यान्यास्थापनेषु’ = योज्यानि + आस्थापनेषु।"),
    "hook": "आठ फल → वमन में और आस्थापन में भी (योज्यानि)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 83 line 2 started a sentence naming four fruits. What do you expect verse 84 to give?",
            ("More names and the verb that says what to do with them", "A sentence needs its verb; the verse supplies it."),
            [("A new chapter title", "A verse in the middle of a chapter does not give a title."),
             ("A list of sages", "The sages came at the start of the chapter."),
             ("The list of salts", "Salts come in verses 88-89.")],
            "Verse 84 adds four names and the verb योज्यानि.",
            "84 completes the sentence begun in 83."),
        match(1, "Match each word to its meaning.",
              [["वमने", "in emesis"], ["आस्थापनेषु", "in decoction enemas"],
               ["योज्यानि", "to be used"], ["एतानि", "these"]],
              "These four words carry the whole statement.",
              "वमने = in emesis; आस्थापनेषु = in āsthāpana enemas; योज्यानि = to be used; एतानि = these."),
        fill(2, "योज्यान्यास्थापनेषु is a joined form: योज्यानि + ____ (type the second word in Devanagari).",
             ["आस्थापनेषु"],
             "योज्यानि + आस्थापनेषु = योज्यान्यास्थापनेषु.",
             "इ before a different vowel becomes य्: योज्यानि + आस्थापनेषु is written योज्यान्यास्थापनेषु.",
             "इ + आ → ्य + आ."),
        mcq("discriminate", 3, "Which is the right split of योज्यान्यास्थापनेषु?",
            ("योज्यानि + आस्थापनेषु", "इ before a different vowel becomes य्; योज्यानि agrees with एतानि."),
            [("योज्यान + यास्थापनेषु", "यास्थापनेषु is not a word."),
             ("योज्यानः + आस्थापनेषु", "A visarga here would not give न्य."),
             ("योज्यानु + आस्थापनेषु", "That would give योज्यान्वास्थापनेषु, with व्.")],
            "योज्यानि is neuter plural, like एतानि.",
            "योज्यानि + आस्थापनेषु = योज्यान्यास्थापनेषु."),
        multi("apply", 4, "Which of these fruits are named in verse 84 itself?",
              [("मदनम्", "Right: first word of the verse."),
               ("जीमूतम्", "Wrong: it is in verse 83, line 2."),
               ("कुटजम्", "Right: second word."),
               ("इक्ष्वाकु", "Wrong: it is in verse 83, line 2."),
               ("हस्तिपर्णिनी", "Right: it ends the first line.")],
              [0, 2, 4],
              "Verse 84 names मदन, कुटज, त्रपुष and हस्तिपर्णिनी; जीमूत and इक्ष्वाकु are in 83.",
              "84 names 4 fruits; the other 4 are in 83 line 2."),
        mcq("transfer", 5,
            "A new line says इमानि पाने नस्ये च योज्यानि. Where are 'these' to be used?",
            ("In both drinking and nasal use", "Two uses are joined by च, as in verse 84."),
            [("Only in drinking", "नस्ये च adds a second use."),
             ("Only in nasal use", "पाने names the first use."),
             ("In neither", "योज्यानि says they are to be used.")],
            "Verse 84 pairs वमने with आस्थापनेषु in the same way.",
            "Use 1 + च + use 2 + योज्यानि = used in both.",
            teaches="Two locative uses joined by च with योज्यानि mean 'to be used in both'."),
    ],
}

# ---------------------------------------------------------------- unit 85
AUTHORED["85"] = {
    "title": "नस्तः प्रच्छर्दने चैव",
    "question": "Which fruit is for the nose, and how many remain for purgation?",
    "rule": ("प्रत्यक्पुष्पा is prescribed for expulsion through the nose; "
             "the ten that remain of the nineteen are stated for virecana "
             "(purgation): 19 − 8 − 1 = 10."),
    "limits": ("The verse names only प्रत्यक्पुष्पा and gives the number ten; "
               "it does not name the ten. नस्तः प्रच्छर्दने could also be "
               "read as one compound."),
    "explain_hi": ("पहली पंक्ति में नाक के रास्ते (नस्तः) निष्कासन के लिए "
                   "प्रत्यक्पुष्पा का विधान है। दूसरी पंक्ति गिनती का हिसाब पूरा करती है: "
                   "उन्नीस फलिनियों में से आठ वमन और आस्थापन में गईं (श्लोक ८३–८४), "
                   "एक नस्य में गई, और ‘दश’ शेष बचीं जो विरेचन में कही गई हैं। "
                   "१९ − ८ − १ = १०। ‘यान्यवशिष्टानि’ = यानि + अवशिष्टानि; "
                   "‘तान्युक्तानि’ = तानि + उक्तानि।"),
    "hook": "१९ − ८ (वमन/आस्थापन) − १ (प्रत्यक्पुष्पा, नस्य) = १० → विरेचन।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The second line says ten remain. Remain after what?",
            ("After the eight of verses 83-84 and the one for the nose", "19 − 8 − 1 = 10."),
            [("After the sixteen mūlinīs", "The mūlinīs are a different group, finished in verse 80."),
             ("After the four snehas", "The snehas begin only in verse 86."),
             ("After the five salts", "The salts come in verses 88-89.")],
            "The ten are the remainder of the nineteen phalinīs.",
            "10 = 19 − 8 − 1."),
        match(1, "Match each word of the verse to its meaning.",
              [["नस्तः", "through the nose"], ["विधीयते", "is prescribed"],
               ["दश", "ten"], ["अवशिष्टानि", "remaining"]],
              "These four words carry the verse's two statements.",
              "नस्तः = through the nose; विधीयते = is prescribed; दश = ten; अवशिष्टानि = remaining."),
        fill(2, "The ten remaining phalinīs are stated for the procedure called ____ (type it in Devanagari).",
             ["विरेचन", "विरेचने", "विरेचनम्", "विरेचनं"],
             "The verse ends: तान्युक्तानि विरेचने.",
             "विरेचने = in purgation: the use of the ten that remain.",
             "The ten remain for विरेचन (purgation)."),
        mcq("discriminate", 3, "Which is the right split of यान्यवशिष्टानि?",
            ("यानि + अवशिष्टानि", "इ before a different vowel becomes य्: यानि + अवशिष्टानि is written यान्यवशिष्टानि."),
            [("यान्य + वशिष्टानि", "वशिष्टानि is not a word."),
             ("यान + यवशिष्टानि", "यवशिष्टानि is not a word."),
             ("यानु + अवशिष्टानि", "That would give यान्ववशिष्टानि, with व्.")],
            "यानि is neuter plural: 'those which'.",
            "यानि + अवशिष्टानि = यान्यवशिष्टानि."),
        multi("apply", 4, "Which statements follow from verses 83-85?",
              [("प्रत्यक्पुष्पा is prescribed for the nose.", "Right: नस्तः प्रच्छर्दने प्रत्यक्पुष्पा विधीयते."),
               ("The ten that remain are stated for purgation.", "Right: दश यान्यवशिष्टानि तान्युक्तानि विरेचने."),
               ("मदन is among the ten left for purgation.", "Wrong: मदन is among the eight of verse 84."),
               ("प्रत्यक्पुष्पा is among the eight of verse 84.", "Wrong: it is not named there; it is the one for the nose."),
               ("The eight of 83-84 are used in emesis and āsthāpana.", "Right: एतानि वमने चैव योज्यान्यास्थापनेषु च.")],
              [0, 1, 4],
              "The nineteen divide into 8 (emesis, āsthāpana), 1 (nose) and 10 (purgation).",
              "19 = 8 + 1 + 10."),
        mcq("transfer", 5,
            "A text lists 24 roots: 9 go to bath, one (bhṛṅga) to the nose, the rest to drinking. How many are for drinking?",
            ("Fourteen (24 − 9 − 1)", "The remainder after both groups assigned."),
            [("Fifteen", "That forgets the one for the nose."),
             ("Ten", "Ten is the size of the two assigned groups together, not the remainder."),
             ("Twenty-three", "That subtracts only the one for the nose and forgets the bath roots.")],
            "As in verse 85, subtract each assigned group, including the single one.",
            "Remaining = total − all assigned groups, even a group of one.",
            teaches="A group of one counts like any other group when you work out how many remain."),
    ],
}

# ---------------------------------------------------------------- unit 86
AUTHORED["86"] = {
    "title": "नामकर्मभिरुक्तानि फलानि",
    "question": "How does the verse close the phalinīs, and which four snehas does it name?",
    "rule": ("The nineteen fruits have been stated by name and action. Sneha "
             "(unctuous substance) is indicated as fourfold: सर्पिः (ghee), "
             "तैलम् (oil), वसा (fat) and मज्जा (marrow)."),
    "limits": ("The verse names the four snehas but does not describe them; "
               "that begins in verse 87. वसा is rendered 'fat' and "
               "सर्पिस्तैलम् can also be read as one compound."),
    "explain_hi": ("पहली पंक्ति फलिनियों का समापन करती है: उन्नीस (‘एकोनविंशति’ = "
                   "एक + ऊन + विंशति, यानी बीस में एक कम) फल नाम और कर्म से कहे गए। "
                   "दूसरी पंक्ति नया विषय खोलती है: स्नेह चार प्रकार का बताया गया है: "
                   "सर्पि (घी), तैल, वसा और मज्जा। ‘सर्पिस्तैलम्’ में सर्पिः का विसर्ग "
                   "‘त’ से पहले ‘स्’ हुआ है, और ‘दिष्टश्चतुर्विधः’ में विसर्ग ‘च’ से पहले ‘श्’।"),
    "hook": "फल १९ पूरे | स्नेह चार: सर्पि · तैल · वसा · मज्जा।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 86 begins 'नामकर्मभिरुक्तानि फलानि'. Which number do you expect it to give for the fruits?",
            ("Nineteen", "The phalinīs counted across verses 81-83 come to nineteen."),
            [("Sixteen", "Sixteen is the number of mūlinīs."),
             ("Eight", "Eight is only the group used in emesis and āsthāpana."),
             ("Ten", "Ten is only the group left for purgation.")],
            "The verse says एकोनविंशतिः: nineteen.",
            "All nineteen fruits are closed off in the first line."),
        match(1, "Match each sneha to its meaning.",
              [["सर्पिः", "ghee"], ["तैलम्", "oil"],
               ["वसा", "fat"], ["मज्जा", "marrow"]],
              "These are the four snehas of the verse.",
              "सर्पिः = ghee; तैलम् = oil; वसा = fat; मज्जा = marrow."),
        fill(2, "In चतुर्विधः, the first part चतुर् means ____ (type the number).",
             ["4", "४", "four", "Four", "चार", "चतुः"],
             "चतुर् = four, विध = fold or kind.",
             "स्नेहो दिष्टश्चतुर्विधः: sneha is indicated as fourfold, and four are named.",
             "चतुर्विध = fourfold."),
        mcq("discriminate", 3, "Why is it written सर्पिस्तैलम् and not सर्पिःतैलम्?",
            ("A visarga before त is written स्", "सर्पिः + तैलम् becomes सर्पिस्तैलम्."),
            [("A visarga becomes र् before any consonant", "Before a voiceless consonant like त it becomes स्, not र्."),
             ("A visarga becomes श् before every letter", "श् appears before च/छ, as in दिष्टश्चतुर्विधः, not before त."),
             ("It is a spelling mistake", "It is the regular sandhi.")],
            "सर्पिः is the word 'ghee'; तैलम् follows it.",
            "Visarga + त → स्त."),
        multi("apply", 4, "Which are among the four snehas named in verse 86?",
              [("सर्पिः", "Right: ghee."),
               ("क्षीरम्", "Wrong: milk is not named here."),
               ("वसा", "Right: fat."),
               ("मधु", "Wrong: honey is not named here."),
               ("मज्जा", "Right: marrow.")],
              [0, 2, 4],
              "सर्पिः, तैलम्, वसा, मज्जा are the four.",
              "Four snehas: ghee, oil, fat, marrow."),
        mcq("transfer", 5,
            "A new text counts एकोनत्रिंशत् herbs. If त्रिंशत् is thirty, how many herbs are meant?",
            ("Twenty-nine", "एकोन- means 'one less than', as in एकोनविंशति = nineteen."),
            [("Thirty-one", "That would be one more than thirty."),
             ("Thirty", "एकोन- takes one away."),
             ("Twenty-one", "That would be a different number word.")],
            "एकोनविंशति = twenty minus one = nineteen; एकोनत्रिंशत् = thirty minus one.",
            "एकोन + N = N − 1.",
            teaches="The prefix एकोन- gives 'one less than' the number that follows."),
    ],
}

# ---------------------------------------------------------------- unit 87
AUTHORED["87"] = {
    "title": "पानाभ्यञ्जनबस्त्यर्थम्",
    "question": "For what are the snehas used, and what effects does the verse give them?",
    "rule": ("By proper application, for drinking, inunction, enema and "
             "nasal use, the snehas are oleating, vitalizing, good for the "
             "complexion, and increase strength and bodily growth."),
    "limits": ("The sentence runs on into verse 88: the subject (the snehas) "
               "comes there. योगतः may mean 'by proper application' or "
               "'in combination with other drugs'."),
    "explain_hi": ("यह श्लोक श्लोक ८६ के चार स्नेहों का वर्णन आगे बढ़ाता है और वाक्य "
                   "श्लोक ८८ में पूरा होता है। पहले उपयोग गिनाए गए हैं: पान, अभ्यंग, "
                   "बस्ति और नस्य, ‘योगतः’ (उचित प्रयोग से)। फिर प्रभाव: स्नेहन करने "
                   "वाले, जीवन देने वाले, वर्ण को उत्तम करने वाले, और बल तथा उपचय "
                   "बढ़ाने वाले। ‘-अर्थम्’ वाले समास का अर्थ ‘के लिए’ होता है। "
                   "‘बलोपचयवर्धनाः’ में बल + उपचय का अ + उ मिलकर ओ हुआ है।"),
    "hook": "उपयोग: पान · अभ्यंग · बस्ति · नस्य | असर: स्नेहन · जीवन · वर्ण्य · बल–उपचय बढ़ाना।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 86 named the four snehas. What do you expect verse 87 to tell about them?",
            ("How they are used and what they do", "The verse gives uses and effects."),
            [("Their prices", "Nothing in these verses speaks of prices."),
             ("Which sages found them", "The sages belong to the early part of the chapter."),
             ("Which plants give them", "The verse speaks of uses, not of source plants.")],
            "Verse 87 gives four uses and four effects.",
            "After naming the snehas, the text gives their uses and effects."),
        match(1, "Match each use to its meaning.",
              [["पान", "drinking"], ["अभ्यञ्जन", "inunction"],
               ["बस्ति", "enema"], ["नस्य", "nasal administration"]],
              "These are the four uses.",
              "पान = drinking; अभ्यञ्जन = inunction; बस्ति = enema; नस्य = nasal administration."),
        fill(2, "बलोपचयवर्धनाः is built from बल + ____ + वर्धनाः (type the middle word in Devanagari).",
             ["उपचय"],
             "बल + उपचय = बलोपचय.",
             "अ + उ → ओ: बल + उपचय is written बलोपचय; the whole word means 'increasing strength and bulk'.",
             "बल + उपचय → बलोपचय."),
        mcq("discriminate", 3, "Which is the right split of बलोपचय?",
            ("बल + उपचय", "अ + उ → ओ, so बल + उपचय is written बलोपचय."),
            [("बलोप + चय", "बलोप is not a word."),
             ("बल + ओपचय", "ओपचय is not a word."),
             ("बलो + उपचय", "ओ would not simply join an उ here.")],
            "बलोपचय = बल (strength) + उपचय (bulk, growth).",
            "बल + उपचय = बलोपचय."),
        multi("apply", 4, "Which effects does verse 87 itself name?",
              [("स्नेहनाः, oleating", "Right: named in line 2."),
               ("वातपित्तकफापहाः, removing Vāta, Pitta, Kapha", "Wrong: that is said in verse 88."),
               ("वर्ण्याः, good for the complexion", "Right: named in line 2."),
               ("दीपनीयतमाः, most stimulating to digestion", "Wrong: that is said of the salts in verse 89."),
               ("जीवनाः, vitalizing", "Right: named in line 2.")],
              [0, 2, 4],
              "Verse 87 gives स्नेहनाः, जीवनाः, वर्ण्याः and बल–उपचय बढ़ाने वाले.",
              "87: oleating, vitalizing, complexion, strength and bulk."),
        mcq("transfer", 5,
            "A new line says स्नानपानार्थम्, built like पानाभ्यञ्जनबस्त्यर्थम्. With स्नान meaning bath and पान meaning drinking, what does it say?",
            ("For bathing and drinking", "Items + -अर्थम् means 'for the purpose of ... '."),
            [("From bathing and drinking", "-अर्थम् means 'for', not 'from'."),
             ("Instead of bathing", "The two items are added together."),
             ("Without drinking", "There is no 'without' in the word.")],
            "The compound lists uses and ends in -अर्थम्, as in verse 87.",
            "Items + -अर्थम् = for the purpose of those items.",
            teaches="A list of nouns joined into one word and ended with -अर्थम् states what something is used for."),
    ],
}

# ---------------------------------------------------------------- unit 88
AUTHORED["88"] = {
    "title": "स्नेहा ह्येते च विहिताः",
    "question": "What do the snehas do to the three doṣas, and which salts open the next list?",
    "rule": ("These snehas are prescribed as removers of Vāta, Pitta and "
             "Kapha. Then the salts begin: सौवर्चल, सैन्धव, विड and औद्भिद "
             "(सैन्धव is rendered 'rock salt' in the translation)."),
    "limits": ("The verse does not say how, nor which sneha for which doṣa. "
               "Line 2 begins a list of salts that is finished in verse 89, "
               "with sea salt making five."),
    "explain_hi": ("श्लोक ८७ के वाक्य का अन्त यहाँ आता है: ये स्नेह वात, पित्त और कफ "
                   "को दूर करने वाले बताए गए हैं। ‘स्नेहा ह्येते’ में स्नेहाः का विसर्ग "
                   "घोष ‘ह’ से पहले लुप्त हुआ है, और हि + एते मिलकर ‘ह्येते’ बना। "
                   "दूसरी पंक्ति से लवणों की सूची शुरू होती है: सौवर्चल, सैन्धव, विड "
                   "और औद्भिद; पाँचवाँ लवण अगले श्लोक में आता है। ‘विडमौद्भिदमेव’ "
                   "में विडम् + औद्भिदम् + एव एक साथ लिखे हैं।"),
    "hook": "स्नेह: वात-पित्त-कफ को दूर करने वाले | लवण (१–४): सौवर्चल · सैन्धव · विड · औद्भिद।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The word वातपित्तकफापहाः ends in अपहाः, 'removers'. What do the snehas of this verse remove?",
            ("Vāta, Pitta and Kapha", "The three doṣas named in the compound."),
            [("Only Vāta", "The compound names all three."),
             ("The salts", "The salts are a separate topic that begins on line 2."),
             ("The sages", "The sages are not in this verse.")],
            "वात-पित्त-कफ-अपहाः = removers of Vāta, Pitta, Kapha.",
            "अपहाः = removers; the three doṣas are the object."),
        match(1, "Match each Devanagari salt to its Latin spelling.",
              [["सौवर्चलम्", "Sauvarcala"], ["सैन्धवम्", "Saindhava"],
               ["विडम्", "Viḍa"], ["औद्भिदम्", "Audbhida"]],
              "Reading the salt names in Devanagari is the point of this card.",
              "सौवर्चलम् = Sauvarcala; सैन्धवम् = Saindhava; विडम् = Viḍa; औद्भिदम् = Audbhida."),
        fill(2, "स्नेहा ह्येते is a joined form of स्नेहाः + हि + ____ (type the last word in Devanagari).",
             ["एते"],
             "हि + एते = ह्येते.",
             "इ before a different vowel becomes य्: हि + एते is written ह्येते. एते means 'these'.",
             "हि + एते → ह्येते."),
        mcq("discriminate", 3,
            "Why does स्नेहाः lose its visarga in स्नेहा ह्येते?",
            ("A visarga after आ drops before a voiced sound such as ह", "स्नेहाः + हि becomes स्नेहा हि."),
            [("It becomes ओ before ह", "ओ comes after अ, not after आ."),
             ("It becomes र् before ह", "र् appears after इ/उ (e.g. सर्पिः + वसा → सर्पिर्वसा), not after आ; after आ the visarga drops."),
             ("It is a printing error", "The loss is regular sandhi.")],
            "स्नेहाः is nominative plural: 'the snehas'.",
            "-आः + voiced sound → -आ."),
        multi("apply", 4, "Which are named as salts in verse 88?",
              [("सौवर्चलम्", "Right: first word of line 2."),
               ("सामुद्रम्", "Wrong: sea salt comes in verse 89."),
               ("विडम्", "Right: it is in line 2."),
               ("मज्जा", "Wrong: marrow is a sneha, from verse 86."),
               ("औद्भिदम्", "Right: it ends line 2.")],
              [0, 2, 4],
              "Verse 88 names four salts; the fifth, sea salt, is in 89.",
              "88: सौवर्चल, सैन्धव, विड, औद्भिद."),
        mcq("transfer", 5,
            "A new line joins हि and आगताः. How is it written, by the rule of ह्येते?",
            ("ह्यागताः", "इ before a different vowel becomes य्."),
            [("हियागताः", "The vowels must join; य् replaces the इ."),
             ("हागताः", "The इ does not simply drop."),
             ("हिआगताः", "Inside a sentence the two vowels are joined.")],
            "ह्येते shows हि + एते → ह्य + एते; the same happens before आ.",
            "हि + vowel → ह्य + vowel.",
            teaches="The rule that turns इ into य् before a different vowel works for हि with any following vowel."),
    ],
}

# ---------------------------------------------------------------- unit 89
AUTHORED["89"] = {
    "title": "सामुद्रेण सहैतानि",
    "question": "What makes the salts five, and which four qualities do they share?",
    "rule": ("With sea salt, the four salts of verse 88 make five. They are "
             "unctuous, hot, sharp and the most stimulating to digestion."),
    "limits": ("The verse gives the qualities of the salts as a group, not "
               "one by one. The source prints स्निघ्दान्युष्णानि; "
               "स्निग्धान्युष्णानि is the word meant. The list of uses "
               "follows in verse 90."),
    "explain_hi": ("सामुद्र (समुद्री) लवण के साथ श्लोक ८८ के चार लवण मिलकर पाँच "
                   "होते हैं। ‘सह’ के साथ तृतीया (‘सामुद्रेण’) का अर्थ है ‘के साथ’। फिर "
                   "इन लवणों के गुण: स्निग्ध, उष्ण, तीक्ष्ण और ‘दीपनीयतम’ (अग्नि को "
                   "सबसे अधिक प्रदीप्त करने वाले)। ‘सहैतानि’ = सह + एतानि "
                   "(अ + ए → ऐ), ‘स्युर्लवणानि’ में स्युः का विसर्ग ‘र्’ हुआ है, और "
                   "‘स्निग्धान्युष्णानि’ में स्निग्धानि + उष्णानि। पाठ में छपा "
                   "‘स्निघ्दान्…’ शायद वर्तनी की भूल है (पाठ-टिप्पणी देखें)।"),
    "hook": "४ + सामुद्र = ५ लवण | गुण: स्निग्ध · उष्ण · तीक्ष्ण · दीपनीयतम।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Verse 88 named four salts, and verse 89 begins 'सामुद्रेण सह'. What does 'together with sea salt' do to the group?",
            ("Adds sea salt as a fifth salt", "The verse says the group, with sea salt, is five."),
            [("Removes one of the four", "सह means 'together with', which adds."),
             ("Makes sea salt a sneha", "Sea salt is called a salt, लवणम्, not a sneha."),
             ("Splits the group into two", "The verse joins, not splits.")],
            "सह + instrumental = 'together with'; so 4 + 1 = 5.",
            "सामुद्रेण सह = together with sea salt."),
        match(1, "Match each quality to its meaning.",
              [["स्निग्धानि", "unctuous"], ["उष्णानि", "hot"],
               ["तीक्ष्णानि", "sharp"], ["दीपनीयतमानि", "most stimulating to digestion"]],
              "These are the four qualities of the salts.",
              "स्निग्ध = unctuous; उष्ण = hot; तीक्ष्ण = sharp; दीपनीयतम = most stimulating to digestion."),
        fill(2, "सहैतानि is a joined form: सह + ____ (type the second word in Devanagari).",
             ["एतानि"],
             "सह + एतानि = सहैतानि.",
             "अ + ए → ऐ: सह + एतानि is written सहैतानि.",
             "सह + एतानि → सहैतानि."),
        mcq("discriminate", 3,
            "In सामुद्रेण सह, what does the ending of सामुद्रेण show?",
            ("The instrumental: 'together with sea salt'", "सह takes the instrumental."),
            [("The genitive: 'of sea salt'", "The genitive would be सामुद्रस्य."),
             ("The locative: 'in sea salt'", "The locative would be सामुद्रे."),
             ("The nominative: 'sea salt is'", "The nominative would be सामुद्रम्.")],
            "-एण ending + सह = 'with'.",
            "सह + instrumental = together with."),
        multi("apply", 4, "Which qualities does verse 89 give to the salts?",
              [("स्निग्धानि", "Right: unctuous."),
               ("शीतानि", "Wrong: the verse says उष्णानि, hot, not cold."),
               ("तीक्ष्णानि", "Right: sharp."),
               ("उष्णानि", "Right: hot."),
               ("वातपित्तकफापहाः", "Wrong: that is said of the snehas in verse 88.")],
              [0, 2, 3],
              "The salts are unctuous, hot, sharp and the most stimulating to digestion.",
              "89: स्निग्ध, उष्ण, तीक्ष्ण, दीपनीयतम."),
        mcq("transfer", 5,
            "A new line says आम्रेण (आम्र = mango) सहैतानि पञ्च फलानि, after four fruits were named. How many fruits are there, and which is the fifth?",
            ("Five; the mango is the fifth", "आम्रेण सह adds the mango to the four, as in verse 89."),
            [("Four; the mango is only a comment", "पञ्च says five."),
             ("Six; the mango is counted twice", "The total is stated as five."),
             ("Five; the mango is among the four", "सह adds a new item to the group.")],
            "Verse 89 does the same: four salts + सामुद्रेण सह = five.",
            "X-instrumental + सह + the group = the group plus X.",
            teaches="सह with an instrumental adds a new item to a named group, and the stated total includes it."),
    ],
}


NOTES_HI = {
    "80": "‘नामकर्मभ्याम्’ तृतीया द्विवचन है (नाम और कर्म)। ‘इत्युक्ता’ = इति + उक्ताः; उक्ताः का विसर्ग ‘न’ से पहले लुप्त है (उक्ता नाम…), और ‘प्रयोज्यास्ता’ में प्रयोज्याः का विसर्ग ‘त’ से पहले ‘स्’ हुआ है। संख्या ११ = १६ − ३ − २ (श्लोक ७८–७९)। पाठभेद डेटा में नहीं हैं।",
    "81": "विश्वास: मध्यम। (१) श्लोक में दो की जगह तीन अर्ध-पंक्तियाँ छपी हैं। (२) छपा ‘द्विदिधम्’ शब्द नहीं है; अर्थ के अनुसार ‘द्विविधम्’ (दो प्रकार का) अपेक्षित है, छन्द नहीं बदलता; यह सुझाव अर्थ और समानान्तर रूपों (त्रिविध/चतुर्विध) पर आधारित है। (३) दूसरी अर्ध-पंक्ति श्लोक ८३ में दोबारा आती है। (४) डेटा में कुछ पौधों के साथ पहचान (जैसे ‘क्लीतक’) लिखी है, पर पाठ पहचान नहीं देता; यह कार्ड उसे नहीं मानता।",
    "82": "‘चोदकीर्या’ = च + उदकीर्या (अ + उ → ओ)। ‘हस्तिपर्ण्याश्च’ = हस्तिपर्ण्याः + च (विसर्ग → श् ‘च’ से पहले)। ‘तथा ऽभया’ पाठ में अलग-अलग छपा है; सामान्य संधि ‘तथाभया’ देती। ‘शारदम्’ के साथ ‘फलम्’ समझा गया है, पाठ में नहीं लिखा। ‘अभया’ को हरीतकी मानना डेटा की टिप्पणी है, पाठ की नहीं।",
    "83": "विश्वास: मध्यम। दूसरी पंक्ति श्लोक ८१ की दूसरी पंक्ति की हूबहू पुनरावृत्ति है। इसे नक़ल की भूल नहीं माना गया, क्योंकि श्लोक ८४–८५ की गिनती (८ + १ + १० = १९) तभी बैठती है जब ये चार फल उपयोग-वाक्य का भी आरम्भ हों। ‘कम्पिल्लकारग्वधयोः’ षष्ठी द्विवचन है; ‘यत्…कुटजस्य च’ का शाब्दिक अर्थ ‘और जो कुटज का (फल)’।",
    "84": "‘योज्यान्यास्थापनेषु’ = योज्यानि + आस्थापनेषु (इ → य् स्वर से पहले)। ‘वमने’ एकवचन, ‘आस्थापनेषु’ बहुवचन है। यह श्लोक श्लोक ८३ की दूसरी पंक्ति से चला वाक्य पूरा करता है; ‘एतानि’ आठों फलों के लिए है। ‘हस्तिपर्णिनी’ को श्लोक ८२ की ‘हस्तिपर्णी’ ही मानना डेटा की टिप्पणी है।",
    "85": "‘नस्तः प्रच्छर्दने’ को एक समास (नस्तःप्रच्छर्दन) भी पढ़ा जा सकता है; भाव ‘नाक से निष्कासन’ है। ‘यान्यवशिष्टानि’ = यानि + अवशिष्टानि; ‘तान्युक्तानि’ = तानि + उक्तानि। गिनती: १९ − ८ − १ = १०। पाठभेद डेटा में नहीं हैं।",
    "86": "‘एकोनविंशतिः’ = एक + ऊन + विंशति (अ + ऊ → ओ): ‘बीस में एक कम’। ‘सर्पिस्तैलम्’ को द्वन्द्व-समास (सर्पिस्-तैलम्) भी पढ़ा जा सकता है; अर्थ वही रहता है। ‘नामकर्मभिरुक्तानि’ में भिः + उक्तानि स्वर से पहले ‘र्’ बना है। ‘दिष्टः’ (√दिश्) का अर्थ ‘निर्दिष्ट, बताया गया’ है।",
    "87": "‘योगतः’ का अर्थ ‘उचित प्रयोग से’ या ‘अन्य द्रव्यों के योग में’, दोनों हो सकता है। वाक्य श्लोक ८८ में पूरा होता है, जहाँ ‘स्नेहाः’ कर्ता आता है। ‘बस्त्यर्थम्’ = बस्ति + अर्थम् (इ → य्)। ‘बलोपचयवर्धनाः’ = बल + उपचय + वर्धनाः (अ + उ → ओ)। पाठभेद डेटा में नहीं हैं।",
    "88": "‘स्नेहा ह्येते’ = स्नेहाः + हि + एते: आ के बाद विसर्ग घोष ‘ह’ से पहले लुप्त; इ → य्। ‘विडमौद्भिदमेव’ में तीन शब्द (विडम् + औद्भिदम् + एव) एक साथ लिखे हैं। सैन्धव की ‘सेंधा नमक’ वाली पहचान डेटा की टिप्पणी है। सूची श्लोक ८९ में पूरी होती है।",
    "89": "छपा ‘स्निघ्दान्युष्णानि’ में ‘घ्द’ वर्तनी की भूल लगती है; अर्थ के अनुसार ‘स्निग्धान्युष्णानि’ अपेक्षित है (श्लोक १००, १०७ में ‘स्निग्धम्’ मिलता है)। यह सुझाव ‘स्निग्ध’ शब्द और श्लोक १००, १०७ के प्रयोग पर आधारित है। ‘सहैतानि’ = सह + एतानि (अ + ए → ऐ); ‘स्युर्लवणानि’ में स्युः का विसर्ग ‘ल’ से पहले ‘र्’ हुआ है। ‘दीपनीयतम’ में ‘-तम’ उत्तमावस्था (सबसे अधिक) का प्रत्यय है।",
}


AIDS = {
    "80": {
        "chunks": "एकादशावशिष्टा याः | प्रयोज्यास्ता विरेचने ‖ इत्युक्ता | नामकर्मभ्यां | मूलिन्यः फलिनीः शृणु।",
        "sandhi": "अ + अ → आ: एकादश + अवशिष्टा → एकादशावशिष्टा · इ + उ → यु: इति + उक्ता → इत्युक्ता · विसर्ग + त → स्त: प्रयोज्याः + ताः → प्रयोज्यास्ताः; फिर ताः का विसर्ग घोष ‘व’ (विरेचने) से पहले लुप्त: ता विरेचने।",
        "seesaw": "मूलिन्यः (जड़ वाली: कही जा चुकीं) ↔ फलिनीः (फल वाली: अब सुनो)। तराजू का पलड़ा पलट रहा है।",
        "anchors": "अवशिष्ट ← अव + √शिष् (बचना): शेष, विशेष, शिष्ट · प्रयोज्य ← प्र + √युज् (लगाना): योग, प्रयोग, योज्य।",
    },
    "81": {
        "letters": "श-वि-त्र-म | धा-इ-जी-कृ | क्ली (शङ्खिनी, विडङ्ग, त्रपुष, मदन | धामार्गव, इक्ष्वाकु, जीमूत, कृतवेधन | क्लीतक)।",
        "diagram": {"groups": [
            {"label": "पहली अर्ध-पंक्ति", "items": ["शङ्खिनी", "विडङ्गानि", "त्रपुषम्", "मदनानि"]},
            {"label": "दूसरी अर्ध-पंक्ति", "items": ["धामार्गवम्", "इक्ष्वाकु", "जीमूतम्", "कृतवेधनम्"]},
            {"label": "तीसरी अर्ध-पंक्ति", "items": ["आनूपम्", "स्थलजम्", "क्लीतकम्"]}]},
        "sandhi": "ई + स्वर → य् + स्वर: शङ्खिनी + अथ → शङ्खिन्यथ · अ + इ → ए: अथ + इक्ष्वाकु → अथेक्ष्वाकु · अ + ए → ऐ: च + एव → चैव।",
        "chunks": "शङ्खिन्यथ | विडङ्गानि | त्रपुषं मदनानि च ‖ धामार्गवमथेक्ष्वाकु | जीमूतं कृतवेधनम् ‖ आनूपं स्थलजं चैव | क्लीतकं द्विविधं स्मृतम्। (छपा ‘द्विदिधं’ = द्विविधं।)",
    },
    "82": {
        "letters": "प्र-उ-प्र-अ | अ-ह (प्रकीर्या, उदकीर्या, प्रत्यक्पुष्पा, अभया | अन्तःकोटरपुष्पी, हस्तिपर्णी)।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति", "items": ["प्रकीर्या", "उदकीर्या", "प्रत्यक्पुष्पा", "अभया"]},
            {"label": "दूसरी पंक्ति", "items": ["अन्तःकोटरपुष्पी", "हस्तिपर्ण्याः", "शारदम्"]}]},
        "puns": "अभया ≈ ‘अ-भय’: बिना डर। (केवल सुनने की सहायता; यह मेरा बनाया हुक है, पौधे के बारे में दावा नहीं।)",
        "sandhi": "अ + उ → ओ: च + उदकीर्या → चोदकीर्या · विसर्ग + च → श्च: हस्तिपर्ण्याः + च → हस्तिपर्ण्याश्च।",
        "chunks": "प्रकीर्या चोदकीर्या | प्रत्यक्पुष्पा तथा अभया ‖ अन्तःकोटरपुष्पी च | हस्तिपर्ण्याश्च शारदम्।",
    },
    "83": {
        "diagram": {"groups": [
            {"label": "पंक्ति १", "items": ["कम्पिल्लकारग्वधयोः", "फलम्", "कुटजस्य"]},
            {"label": "पंक्ति २", "items": ["धामार्गवम्", "इक्ष्वाकु", "जीमूतम्", "कृतवेधनम्"]}]},
        "contrast": "वही पंक्ति दो जगह: श्लोक ८१ में सूची का सदस्य ↔ श्लोक ८३ में नए वाक्य (उपयोग) का आरम्भ, जो श्लोक ८४ में पूरा होता है।",
        "sandhi": "अ + आ → आ: कम्पिल्लक + आरग्वधयोः → कम्पिल्लकारग्वधयोः · अ + इ → ए: अथ + इक्ष्वाकु → अथेक्ष्वाकु।",
        "chunks": "कम्पिल्लकारग्वधयोः | फलं यत् कुटजस्य च ‖ धामार्गवमथेक्ष्वाकु | जीमूतं कृतवेधनम्।",
    },
    "84": {
        "frame": "कौन: आठ फल (८३ के चार + मदन, कुटज, त्रपुष, हस्तिपर्णिनी) · कहाँ: वमन और आस्थापन · विधान: योज्यानि।",
        "diagram": {"groups": [
            {"label": "नाम", "items": ["मदनम्", "कुटजम्", "त्रपुषम्", "हस्तिपर्णिनी"]},
            {"label": "प्रयोग", "items": ["एतानि", "वमने", "योज्यानि", "आस्थापनेषु"]}]},
        "sandhi": "इ + आ → य् + आ: योज्यानि + आस्थापनेषु → योज्यान्यास्थापनेषु · अ + ए → ऐ: च + एव → चैव।",
        "anchors": "योज्य ← √युज् (श्लोक ८०: प्रयोज्य) · वमन ← √वम् (उगलना, उल्टी)।",
        "chunks": "मदनं कुटजं चैव | त्रपुषं हस्तिपर्णिनी ‖ एतानि वमने चैव | योज्यान्यास्थापनेषु च।",
    },
    "85": {
        "chain": {"steps": ["१९ फलिनियाँ", "− ८ (वमन और आस्थापन, ८३–८४)", "− १ (प्रत्यक्पुष्पा, नस्य)", "= १० (विरेचन)"]},
        "frame": "कौन: प्रत्यक्पुष्पा · कहाँ: नाक से निष्कासन · बाकी: दस, विरेचन के लिए।",
        "sandhi": "इ + अ → य् + अ: यानि + अवशिष्टानि → यान्यवशिष्टानि · इ + उ → यु: तानि + उक्तानि → तान्युक्तानि।",
        "contrast": "वमने (श्लोक ८४, उल्टी) ↔ विरेचने (श्लोक ८५, विरेचन)। दोनों सप्तमी एकवचन, पर अलग क्रियाएँ।",
        "chunks": "नस्तः प्रच्छर्दने चैव | प्रत्यक्पुष्पा विधीयते ‖ दश यान्यवशिष्टानि | तान्युक्तानि विरेचने।",
    },
    "86": {
        "letters": "स-त-व-म (सर्पिः, तैलम्, वसा, मज्जा)।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति", "items": ["नामकर्मभिः", "उक्तानि", "फलानि", "एकोनविंशतिः"]},
            {"label": "दूसरी पंक्ति", "items": ["सर्पिः", "तैलम्", "वसा", "मज्जा", "स्नेहः", "चतुर्विधः"]}]},
        "pegs": "चार पैरों वाली मेज़: घी, तेल, वसा, मज्जा चार पाये। (मेरा बनाया चित्र; श्लोक में नहीं।)",
        "sandhi": "विसर्ग + त → स्त: सर्पिः + तैलम् → सर्पिस्तैलम् · विसर्ग + च → श्च: दिष्टः + चतुर्विधः → दिष्टश्चतुर्विधः · अ + ऊ → ओ: एक + ऊन → एकोन।",
        "anchors": "एकोनविंशति = एक + ऊन + विंशति (बीस में एक कम) · चतुर्विध = चतुर् (चार) + विध (प्रकार)।",
        "chunks": "नामकर्मभिरुक्तानि | फलान्येकोनविंशतिः ‖ सर्पिस्तैलं वसा मज्जा | स्नेहो दिष्टश्चतुर्विधः।",
    },
    "87": {
        "frame": "किसलिए: पान, अभ्यंग, बस्ति, नस्य · कैसे: योगतः · असर: स्नेहन, जीवन, वर्ण, बल–उपचय।",
        "diagram": {"groups": [
            {"label": "उपयोग", "items": ["पान", "अभ्यञ्जन", "बस्ति", "नस्य"]},
            {"label": "असर", "items": ["स्नेहनाः", "जीवनाः", "वर्ण्याः", "बलोपचयवर्धनाः"]}]},
        "sandhi": "इ + अ → य् + अ: बस्ति + अर्थम् → बस्त्यर्थम् · अ + उ → ओ: बल + उपचय → बलोपचय।",
        "anchors": "अर्थम् = के लिए (पान-…-अर्थम् = ‘पान आदि के लिए’) · उपचय = वृद्धि, पुष्टि।",
        "chunks": "पानाभ्यञ्जनबस्त्यर्थं | नस्यार्थं चैव योगतः ‖ स्नेहना जीवना वर्ण्या | बलोपचयवर्धनाः।",
    },
    "88": {
        "letters": "सौ-सै-वि-औ (सौवर्चल, सैन्धव, विड, औद्भिद)।",
        "diagram": {"groups": [
            {"label": "पहली पंक्ति", "items": ["स्नेहाः", "एते", "विहिताः", "वातपित्तकफापहाः"]},
            {"label": "दूसरी पंक्ति (लवण)", "items": ["सौवर्चलम्", "सैन्धवम्", "विडम्", "औद्भिदम्"]}]},
        "sandhi": "विसर्ग लुप्त (आः + घोष): स्नेहाः + हि → स्नेहा हि · इ → य्: हि + एते → ह्येते।",
        "chunks": "स्नेहा ह्येते च विहिता | वातपित्तकफापहाः ‖ सौवर्चलं सैन्धवं च | विडमौद्भिदमेव च।",
    },
    "89": {
        "letters": "स्नि-उ-ती-दी (स्निग्ध, उष्ण, तीक्ष्ण, दीपनीयतम)।",
        "diagram": {"groups": [
            {"label": "पाँच लवण (श्लोक ८८ के चार + सामुद्र)", "items": ["सौवर्चल", "सैन्धव", "विड", "औद्भिद", "सामुद्र"]},
            {"label": "चार गुण", "items": ["स्निग्ध", "उष्ण", "तीक्ष्ण", "दीपनीयतम"]}]},
        "sandhi": "अ + ए → ऐ: सह + एतानि → सहैतानि · विसर्ग → र्: स्युः + लवणानि → स्युर्लवणानि · इ + उ → यु: स्निग्धानि + उष्णानि → स्निग्धान्युष्णानि।",
        "anchors": "दीपनीय ← दीपन ← √दीप् (जलना, चमकना): ‘दीया’ जैसा · -तम = सबसे अधिक (दीपनीयतम) · सामुद्र ← समुद्र।",
        "chunks": "सामुद्रेण सहैतानि | पञ्च स्युर्लवणानि च ‖ स्निग्धान्युष्णानि तीक्ष्णानि | दीपनीयतमानि च।",
    },
}


IMAGE_SPECS = {
    ("85", "chain"): {
        "file": "phalini-count.svg",
        "alt": "A four-box chain: 19 phalinīs, minus 8 for emesis and enema, minus 1 for the nose, equals 10 for purgation",
        "type": "chain",
        "title": "फलिनियों की गिनती",
        "steps": ["१९ फलिनियाँ", "− ८ (वमन और आस्थापन, ८३–८४)", "− १ (प्रत्यक्पुष्पा, नस्य)", "= १० (विरेचन)"],
    },
    ("89", "diagram"): {
        "file": "five-salts.svg",
        "alt": "Two columns: the five salts (sauvarcala, saindhava, viḍa, audbhida, sāmudra) and the four qualities (unctuous, hot, sharp, most stimulating to digestion)",
        "type": "split",
        "title": "पाँच लवण · चार गुण",
        "cols": [["पाँच लवण", ["सौवर्चल", "सैन्धव", "विड", "औद्भिद", "सामुद्र"]],
                 ["चार गुण", ["स्निग्ध", "उष्ण", "तीक्ष्ण", "दीपनीयतम"]]],
    },
}
