"""Hand-written study content for units 1-10 of Charaka Samhita Su. 1.

Each entry belongs to the unit with the same number in
sutrasthana1_verses.json. Everything a human wrote (explanations, hooks,
questions) lives here; the generator only adds data from the verse file.
"""

_turn = [0]


def _place(right, wrongs):
    """Put the right option in a rotating position so answers are spread."""
    n = len(wrongs) + 1
    pos = _turn[0] % n
    _turn[0] += 1
    items = list(wrongs)
    items.insert(pos, right)
    return items, pos


def mcq(role, rung, q, right, wrongs, explain, rule, teaches=None,
        hint=None):
    """right and each wrong are (text, why) pairs."""
    items, pos = _place(right, wrongs)
    out = {"role": role, "rung": rung, "kind": "mcq", "q": q,
           "options": [t for t, _ in items], "answer": pos,
           "optionExplain": [("Right: " if i == pos else "") + w
                             for i, (_, w) in enumerate(items)],
           "explain": explain, "rule": rule}
    if teaches:
        out["teaches"] = teaches
    if hint:
        out["hint"] = hint
    return out


def match(rung, q, pairs, explain, rule, role="warmup"):
    return {"role": role, "rung": rung, "kind": "match", "q": q,
            "pairs": pairs, "explain": explain, "rule": rule}


def order(rung, q, items, explain, rule, role="warmup"):
    return {"role": role, "rung": rung, "kind": "order", "q": q,
            "items": items, "explain": explain, "rule": rule}


def fill(rung, q, accept, explain, teaches, rule, role="extend"):
    return {"role": role, "rung": rung, "kind": "fill", "q": q,
            "accept": accept, "explain": explain, "teaches": teaches,
            "rule": rule}


def multi(role, rung, q, options, answers, explain, rule):
    """options are (text, why) pairs; answers are the right indexes."""
    return {"role": role, "rung": rung, "kind": "multi", "q": q,
            "options": [t for t, _ in options], "answers": answers,
            "optionExplain": [w for _, w in options],
            "explain": explain, "rule": rule}


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो दीर्घञ्जीवितीयम्",
    "section": "अध्याय का आरम्भ",
    "question": "How does the chapter announce itself, and what is it called?",
    "rule": ("अथातो … अध्यायं व्याख्यास्यामः = 'Now, therefore, we shall "
             "expound the chapter called Dīrghañjīvitīya.' अथ + अतः = "
             "अथातः. The chapter is named after the first words of verse 3, "
             "दीर्घं जीवितम्, plus the ending -ईय."),
    "limits": ("Taking the name from verse 3 is the usual explanation of "
               "the compound; the sentence itself only names the chapter."),
    "explain_hi": ("यह अध्याय का आरम्भ-वाक्य है; इसी साँचे में सूत्रस्थान के "
                   "अध्याय खुलते हैं। ‘अथ’ आरम्भ का सूचक है, ‘अतः’ का अर्थ "
                   "‘इस कारण से’ है। ‘व्याख्यास्यामः’ उत्तम पुरुष बहुवचन है, "
                   "यानी ‘हम खोलकर समझाएँगे’। अध्याय का नाम ‘दीर्घञ्जीवितीय’ "
                   "अगले श्लोक के पहले शब्दों ‘दीर्घं जीवितम्’ से बना है।"),
    "hook": ("अथ – अतः – व्याख्यास्यामः: ‘अब – इसलिए – हम समझाएँगे’। "
             "नाम = पहले शब्द (दीर्घं जीवितम्) + ईय।"),
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The sentence अथातो दीर्घञ्जीवितीयमध्यायं व्याख्यास्यामः opens a chapter. What does it announce?",
            ("A chapter on long life will now be expounded",
             "It names the chapter, and says it will be explained."),
            [("A king's order for a journey",
              "Nothing here concerns a king or a journey."),
             ("A list of diseases and their cures",
              "No disease is named in this sentence."),
             ("A prayer to Brahmā",
              "No god is addressed; the sentence introduces a chapter.")],
            "अध्यायं (chapter) and व्याख्यास्यामः (we shall expound) show that a chapter is being introduced.",
            "The opening sentence names the chapter and promises to explain it."),
        match(1, "Match each word of the opening sentence to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["अध्यायम्", "chapter"],
               ["व्याख्यास्यामः", "we shall expound"]],
              "These four words carry the whole announcement.",
              "अथ = now; अतः = therefore; अध्यायम् = chapter; व्याख्यास्यामः = we shall expound."),
        fill(2, "The word for 'chapter' in the sentence is ____ (type it in Devanagari).",
             ["अध्यायम्", "अध्यायं"],
             "The sentence says अध्यायम् for 'chapter'.",
             "अध्यायम् ends in -म्, the accusative: the chapter is what is being expounded, the object of the verb.",
             "अध्यायम् = chapter, the thing expounded."),
        mcq("discriminate", 3, "Which is the right split of अथातः?",
            ("अथ + अतः", "अ + अ gives आ, so अथ + अतः is written अथातः."),
            [("अथा + तः", "There is no word तः here."),
             ("अथ + आतः", "आतः is not a word in this sentence."),
             ("अ + थातः", "थातः is not a word.")],
            "अथातः is अथ ('now') + अतः ('therefore') joined by sandhi.",
            "अथातः = अथ + अतः."),
        mcq("apply", 4,
            "व्याख्यास्यामः ends in -मः. Who is speaking, and how many?",
            ("We, the teachers: first person plural",
             "-मः marks 'we', and the future sense gives 'we shall'."),
            [("He, one teacher: third person singular",
              "The third person singular would end in -ति."),
             ("You, the students: second person plural",
              "The second person plural would end in -थ."),
             ("They, the sages: third person plural",
              "The third person plural would end in -न्ति.")],
            "व्याख्यास्यामः is the first person plural future: 'we shall expound'.",
            "-मः on a verb = 'we'."),
        mcq("transfer", 5,
            "Another chapter opens अथातो मात्राशितीयमध्यायं व्याख्यास्यामः. What is the same as here, and what changes?",
            ("Only the chapter name changes; the frame stays",
             "Chapters of this part share the frame अथातो … अध्यायं व्याख्यास्यामः."),
            [("Everything changes, since each chapter opens in its own way",
              "The frame is shared; only the name sits in the middle."),
             ("Only व्याख्यास्यामः stays; the other words change",
              "अथातः and अध्यायम् stay too."),
             ("The speaker changes to 'I'",
              "व्याख्यास्यामः stays 'we shall expound'.")],
            "The name in the middle (here मात्राशितीयम्) is the only part that changes.",
            "The opening frame is shared; the title sits in the middle.",
            teaches="Once you know the frame, you can read any chapter title by looking at the word before अध्यायम्."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "इति ह स्माह भगवानात्रेयः",
    "section": "अध्याय का आरम्भ",
    "question": "Whose words are the opening sentence, and how does the text say so?",
    "rule": ("इति ह स्माह भगवान् आत्रेयः = 'Thus, indeed, said the venerable "
             "Ātreya.' इति closes the opening sentence as a quotation, so "
             "'we shall expound' is Ātreya's own statement."),
    "limits": ("The line gives the teaching to Ātreya; it does not say who "
               "wrote it down."),
    "explain_hi": ("‘इति’ पिछले वाक्य को उद्धरण की तरह बन्द करता है: ‘हम "
                   "व्याख्या करेंगे’ कहने वाले आत्रेय हैं। ‘ह’ और ‘स्म’ "
                   "निपात हैं, जो इस परम्परागत कथन-शैली में आते हैं। "
                   "‘आह’ का अर्थ ‘कहा’ है। ‘भगवान्’ आदर का विशेषण है और "
                   "‘आत्रेयः’ अत्रि के वंश का नाम है।"),
    "hook": ("इति = उद्धरण बन्द · ह स्म = परम्परागत शैली · आह = कहा। "
             "वक्ता: भगवान् + आत्रेय।"),
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In इति ह स्माह भगवानात्रेयः, who is named as the speaker?",
            ("Ātreya", "आत्रेयः is the last word, in the nominative: he is the one who spoke."),
            [("Bharadvāja", "Bharadvāja is named in the next verse, not here."),
             ("Indra", "Indra is named in the next verse, not here."),
             ("Prajāpati", "Prajāpati comes later in the story.")],
            "The speaker is भगवान् आत्रेयः, the venerable Ātreya.",
            "इति ह स्माह भगवानात्रेयः = 'Thus said the venerable Ātreya.'"),
        match(1, "Match each word of the line to its meaning.",
              [["इति", "thus"], ["ह", "indeed"], ["आह", "said"],
               ["भगवान्", "the venerable"]],
              "These words make up a fixed attribution formula.",
              "इति = thus; ह = indeed; आह = said; भगवान् = the venerable."),
        fill(2, "The verb meaning 'said' is ____ (type it in Devanagari).",
             ["आह"],
             "The verb of the line is आह, joined to स्म as स्माह.",
             "आह is a past form of the root √अह्: 'he said'. It tells you one speaker, in the past.",
             "आह = he said."),
        mcq("discriminate", 3, "Which is the right split of स्माह?",
            ("स्म + आह", "म् + आ joins as मा, so स्म + आह is written स्माह."),
            [("स्मा + ह", "ह is a separate word earlier in the line."),
             ("स + माह", "माह is not a word."),
             ("स्म + अह", "The verb is आह, with a long आ.")],
            "स्माह is the particle स्म followed by the verb आह.",
            "स्माह = स्म + आह."),
        mcq("apply", 4,
            "Whose words are 'we shall expound' in the opening sentence, and what shows it?",
            ("Ātreya's; इति closes the sentence as his quoted words",
             "इति marks the end of a quotation and the next line names the speaker."),
            [("The compiler's own; the text speaks in its own voice",
              "इति ह स्माह hands the words to Ātreya."),
             ("Indra's; he is named next",
              "Indra is not the speaker of this line."),
             ("Bharadvāja's; he is the seeker of verse 3",
              "Bharadvāja appears only after this line.")],
            "इति … आह ties the opening sentence to Ātreya.",
            "इति closes a quotation; आह names its speaker."),
        mcq("transfer", 5,
            "Many chapters repeat this second line after a new title. What does it tell you about such a chapter?",
            ("The teaching is again given as Ātreya's",
             "The same formula hands the new chapter to the same speaker."),
            [("The speaker has changed to the new title's sage",
              "The formula names Ātreya, not a new speaker."),
             ("It is a later addition by the compiler",
              "Nothing in the line says it was added later."),
             ("It marks the chapter as written in verse",
              "The line says who spoke, not what form the chapter takes.")],
            "The repeated line works as a signature: it keeps Ātreya as the voice of the teaching.",
            "A repeated इति ह स्माह भगवानात्रेयः = the same voice again.",
            teaches="A repeated formula is a signature: it tells you whose teaching you are reading."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "दीर्घं जीवितमन्विच्छन्",
    "section": "भरद्वाज की खोज",
    "question": "Who goes to whom, and what does he want?",
    "rule": ("दीर्घं जीवितम् अन्विच्छन् भरद्वाजः इन्द्रम् उपागमत् = Seeking a "
             "long life, Bharadvāja approached Indra, having understood that "
             "he was fit to give refuge."),
    "limits": ("The verse gives Bharadvāja's aim and his choice of Indra; "
               "how Indra came to hold the science is told in the next "
               "verses."),
    "explain_hi": ("कथा यहीं से शुरू होती है। भरद्वाज उग्र तप वाले ऋषि हैं और "
                   "उनकी चाह ‘दीर्घ जीवन’ है; इसी से अध्याय का नाम बना। वे "
                   "इन्द्र के पास जाते हैं, क्योंकि उन्होंने इन्द्र को "
                   "‘शरण्य’ (शरण देने योग्य) जाना। ‘बुद्ध्वा’ (जानकर) पहले "
                   "होने वाली क्रिया है और ‘उपागमत्’ (गए) बाद की; दोनों का "
                   "कर्ता भरद्वाज है।"),
    "hook": ("चाह: दीर्घ जीवन · कौन: भरद्वाज · किसके पास: इन्द्र "
             "(अमरों के ईश्वर) · क्यों: शरण्य जानकर।"),
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Bharadvāja wants a long life and goes to a god for help. Whom do you expect him to approach?",
            ("Indra, lord of the immortals",
             "The verse names Indra, with the title अमरेश्वरम्."),
            [("Brahmā", "Brahmā taught earlier; the verse does not send Bharadvāja to him."),
             ("Yama", "Yama is not mentioned in this verse."),
             ("Agni", "Agni is not mentioned in this verse.")],
            "Bharadvāja approached Indra, the lord of the immortals.",
            "Bharadvāja goes to Indra for a long life."),
        match(1, "Match each word of the verse to its meaning.",
              [["दीर्घम्", "long"], ["जीवितम्", "life"],
               ["उग्रतपाः", "of severe austerity"],
               ["शरण्यम्", "fit to give refuge"]],
              "These words give what Bharadvāja wants and what he is like.",
              "दीर्घम् = long; जीवितम् = life; उग्रतपाः = of severe austerity; शरण्यम् = fit to give refuge."),
        fill(2, "The word for 'having understood' is ____ (type it in Devanagari).",
             ["बुद्ध्वा"],
             "बुद्ध्वा comes from the root √बुध्, 'to understand'.",
             "बुद्ध्वा is a 'having done' word (the -त्वा type): it names an action finished before the main verb. He understood, then he approached.",
             "बुद्ध्वा = having understood (before उपागमत्)."),
        mcq("discriminate", 3, "Which is the right split of अमरेश्वरम्?",
            ("अमर + ईश्वरम्", "अ + ई joins as ए, so अमर + ईश्वरम् is written अमरेश्वरम्."),
            [("अमरे + श्वरम्", "श्वरम् is not a word."),
             ("अम + रेश्वरम्", "Neither part is a word."),
             ("अमर + ऐश्वरम्", "The second word begins with ई, not ऐ.")],
            "अमरेश्वरम् = अमर (immortal) + ईश्वरम् (lord): the lord of the immortals.",
            "अमरेश्वरम् = अमर + ईश्वरम्."),
        mcq("apply", 4,
            "A reader says Indra went to Bharadvāja. Which word in the verse shows this is wrong?",
            ("इन्द्रम्: its ending -म् marks Indra as the one approached",
             "For a masculine name in -अ, -म् is the accusative: the one approached."),
            [("इन्द्रम्: its ending -म् marks Indra as the doer",
              "-म् on such a name marks the one approached, not the doer."),
             ("भरद्वाज: it is an accusative, so Bharadvāja is approached",
              "भरद्वाज is the doer; its -ः is dropped by sandhi before उपागमत्."),
             ("उपागमत् is future: nothing has happened yet",
              "उपागमत् is a past form: he approached.")],
            "इन्द्रम् (-म्) is the object of उपागमत्; भरद्वाजः is the doer (its -ः disappears by sandhi before उपागमत्).",
            "Masculine name in -अ: doer -ः (or -ो / dropped, by sandhi), the one approached -म्."),
        mcq("transfer", 5,
            "An invented line reads वसिष्ठो वरुणमुपागमत्. By the same pattern, who goes to whom?",
            ("Vasiṣṭha goes to Varuṇa",
             "वसिष्ठो is वसिष्ठः joined by sandhi: the doer; वरुणम् (-म्) is the one approached."),
            [("Varuṇa goes to Vasiṣṭha", "That would need the endings the other way round."),
             ("Vasiṣṭha and Varuṇa go together", "Nothing joins them as doers."),
             ("Neither goes anywhere",
              "उपागमत् says that a going took place.")],
            "The pattern of verse 3 carries over to any name with the same endings.",
            "Doer name (-ः / -ो) + object name (-म्) + उपागमत् = the first goes to the second.",
            teaches="For masculine names in -अ you can read who goes to whom from the endings: -ः (or -ो) for the doer, -म् for the one approached."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "ब्रह्मणा हि यथाप्रोक्तम्",
    "section": "आयुर्वेद की परम्परा",
    "question": "Through whom did Āyurveda pass from Brahmā to the Aśvins?",
    "rule": ("ब्रह्मा → प्रजापति → अश्विनौ. Prajāpati received Āyurveda "
             "whole, as Brahmā had proclaimed it; then the two Aśvins "
             "received it from him."),
    "limits": ("The printed text reads पजापतिः; प्रजापतिः is the expected "
               "name (see the note). The verb जग्राह has to be supplied "
               "again for the Aśvins."),
    "explain_hi": ("परम्परा की पहली कड़ियाँ: ब्रह्मा ने कहा, प्रजापति ने उसे "
                   "सम्पूर्ण रूप से ग्रहण किया, फिर अश्विनीकुमारों ने "
                   "उनसे (ग्रहण किया)। ‘निखिलेन’ का अर्थ ‘पूरा का पूरा’ और "
                   "‘आदौ’ का ‘सबसे पहले’ है। ‘जग्राह’ एक ही बार आया है; "
                   "‘अश्विनौ’ के साथ उसे दोबारा जोड़कर पढ़ना पड़ता है।"),
    "hook": "ब्रह्मा कहें → प्रजापति ग्रहण करें → अश्विनौ उनसे लें।",
    "core": False,
    "requires": [],
    "questions": [
        mcq("pretest", 0,
            "Brahmā proclaimed Āyurveda. Who do you expect received it first?",
            ("Prajāpati", "The verse names Prajāpati as the first receiver."),
            [("Indra", "Indra comes later, in verse 5."),
             ("The Aśvins", "They receive it from Prajāpati, so they come second."),
             ("Bharadvāja", "Bharadvāja comes at the end of the chain.")],
            "Prajāpati received it first, then the Aśvins.",
            "Brahmā → Prajāpati → the Aśvins."),
        order(1, "Put the three in the order the knowledge passed, starting with the one who proclaimed it.",
              ["ब्रह्मा", "प्रजापति", "अश्विनौ"],
              "Each one receives from the one before.",
              "ब्रह्मा → प्रजापति → अश्विनौ."),
        fill(2, "The word meaning 'in its entirety' is ____ (type it in Devanagari).",
             ["निखिलेन"],
             "निखिलेन means 'entirely'.",
             "निखिलेन ends in -एन, the instrumental, used like an adverb: 'by the whole', so 'completely'.",
             "निखिलेन = in its entirety."),
        mcq("discriminate", 3, "Which is the right split of निखिलेनादौ?",
            ("निखिलेन + आदौ", "अ + आ joins as आ, so निखिलेन + आदौ is written निखिलेनादौ."),
            [("निखिले + नादौ", "नादौ is not a word."),
             ("निखिलेना + दौ", "दौ is not a word."),
             ("निखिलेन + अदौ", "The second word is आदौ, 'in the beginning'.")],
            "निखिलेनादौ = निखिलेन ('entirely') + आदौ ('at first').",
            "निखिलेनादौ = निखिलेन + आदौ."),
        mcq("apply", 4,
            "जग्राह appears once, yet the Aśvins also receive. What lets us read it that way?",
            ("The verb is understood again for अश्विनौ",
             "अश्विनौ has no verb of its own, so जग्राह is carried over to it."),
            [("अश्विनौ is itself a verb meaning 'received'",
              "अश्विनौ is a name, in the dual."),
             ("ब्रह्मणा is the doer of both",
              "ब्रह्मणा names who proclaimed, not who received."),
             ("The verse is incomplete and cannot be read",
              "It reads fully once the verb is carried over.")],
            "Sanskrit often leaves a verb out when the same one fits again; here जग्राह is understood again, in the dual, for the two Aśvins.",
            "A verb can be understood again for a second doer."),
        mcq("transfer", 5,
            "An invented line reads वसिष्ठेन यथोक्तं ज्ञानं शिष्यो जग्राह. Who spoke, and who received?",
            ("Vasiṣṭha spoke; the pupil received",
             "वसिष्ठेन (-एन) names who spoke; शिष्यः is the doer of जग्राह."),
            [("The pupil spoke; Vasiṣṭha received", "The endings are the other way round."),
             ("Vasiṣṭha both spoke and received", "शिष्यः is the one who received."),
             ("Nobody spoke", "यथोक्तम् says it was spoken.")],
            "The same pattern as ब्रह्मणा यथाप्रोक्तम् … जग्राह: -एन/-णा names the speaker.",
            "The speaker ends in -एन/-णा; the receiver is the doer of जग्राह.",
            teaches="An -एन / -णा name before a 'spoken' word is the speaker."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "अश्विभ्यां भगवाञ्छक्रः",
    "section": "आयुर्वेद की परम्परा",
    "question": "How did Āyurveda reach Indra, and why does Bharadvāja go to him?",
    "rule": ("अश्विभ्याम् शक्रः प्रतिपेदे केवलम् = Śakra (Indra) received it "
             "whole from the Aśvins; ऋषिप्रोक्तः भरद्वाजः तस्मात् शक्रम् "
             "उपागमत् = told by the sages, Bharadvāja therefore went to "
             "Śakra."),
    "limits": ("ऋषिप्रोक्तः is read as 'told (asked) by the sages'; the "
               "verse does not say what they told him."),
    "explain_hi": ("परम्परा की अगली कड़ी: अश्विनीकुमारों से शक्र (इन्द्र) को "
                   "आयुर्वेद पूरा मिला। फिर कारण जुड़ता है: इन्द्र के पास "
                   "ज्ञान था, ‘तस्मात्’ (इसीलिए) भरद्वाज उनके पास गए। "
                   "‘ऋषिप्रोक्तः’ का अर्थ ‘ऋषियों द्वारा कहा गया’ है। "
                   "‘भगवान्’ यहाँ इन्द्र का आदरसूचक विशेषण है।"),
    "hook": ("ब्रह्मा → प्रजापति → अश्विनौ → शक्र; और शक्र के पास गए भरद्वाज।"),
    "core": True,
    "requires": ["su1-004"],
    "questions": [
        mcq("pretest", 0,
            "From whom did Indra (Śakra) receive Āyurveda?",
            ("The Aśvins", "अश्विभ्याम् gives the Aśvins as the source."),
            [("Brahmā directly", "Brahmā comes before Prajāpati in the chain."),
             ("Prajāpati", "Prajāpati gave it to the Aśvins, not to Indra."),
             ("Bharadvāja", "Bharadvāja comes to Indra to receive it.")],
            "Indra received it from the Aśvins.",
            "The Aśvins → Śakra (Indra)."),
        match(1, "Match each word of the verse to its meaning.",
              [["अश्विभ्याम्", "from the Aśvins"], ["भगवान्", "the venerable"],
               ["शक्रः", "Śakra (Indra)"], ["केवलम्", "wholly"]],
              "These words carry the handing over from the Aśvins to Indra.",
              "अश्विभ्याम् = from the Aśvins; शक्रः = Śakra (Indra); केवलम् = wholly."),
        fill(2, "In this verse the word meaning 'therefore' is ____ (type it in Devanagari).",
             ["तस्मात्", "तस्माच्"],
             "तस्मात् gives the reason: Indra had the science, so Bharadvāja went to him.",
             "तस्मात् is the -आत् form of तद् ('that'): 'from that', so 'for that reason'.",
             "तस्मात् = therefore."),
        mcq("discriminate", 3, "Which is the right split of तस्माच्छक्रमुपागमत्?",
            ("तस्मात् + शक्रम् + उपागमत्",
             "त् + श् joins as च्छ्, and म् + उ as मु; the three words come back."),
            [("तस्मा + च्छक्रम् + उपागमत्", "च्छक्रम् is not a word."),
             ("तस्मात् + छक्रम् + उपागमत्", "The name is शक्र, not छक्र."),
             ("तस्मात् + शक्रम् + पागमत्", "The verb is उपागमत्, with उ.")],
            "तस्माच्छक्रमुपागमत् = तस्मात् ('therefore') + शक्रम् ('Śakra') + उपागमत् ('approached').",
            "तस्माच्छक्रमुपागमत् = तस्मात् + शक्रम् + उपागमत्."),
        mcq("apply", 4,
            "Which line gives the order of transmission in verses 4 and 5?",
            ("Brahmā → Prajāpati → the Aśvins → Śakra",
             "Each receives from the one before, as verses 4 and 5 say."),
            [("Brahmā → the Aśvins → Prajāpati → Śakra", "Prajāpati comes before the Aśvins."),
             ("Prajāpati → Brahmā → Śakra → the Aśvins", "Brahmā is the first, not the second."),
             ("Brahmā → Prajāpati → Śakra → the Aśvins", "Śakra receives from the Aśvins, not before them.")],
            "The chain of verses 4 and 5 is Brahmā, Prajāpati, the Aśvins, Śakra.",
            "ब्रह्मा → प्रजापति → अश्विनौ → शक्र."),
        mcq("transfer", 5,
            "ऋषिप्रोक्तः means 'told (asked) by the sages'. By the same pattern, what does गुरुप्रोक्तः mean?",
            ("Told by the teacher",
             "The first member names the one who tells; the second is 'told'."),
            [("Telling the teacher", "The teacher is the one who tells, not the one told."),
             ("The teacher who tells", "The compound describes what was told."),
             ("The teacher and the told", "It is not a pair; the first member says by whom.")],
            "A first member like ऋषि- or गुरु- names the one by whom something was told.",
            "X-प्रोक्तः = told by X.",
            teaches="In X-प्रोक्तः the first member names the speaker, as in ब्रह्मणा प्रोक्तम् (verse 4)."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "विघ्नभूता यदा रोगाः",
    "section": "रोगों का आना, ऋषियों का सम्मेलन",
    "question": "What happened to embodied beings, and what did it block?",
    "rule": ("When diseases appeared they became obstacles to the embodied "
             "beings' austerity, fasting, study, celibacy, vows and life. "
             "The sentence begins with यदा and is completed by तदा in "
             "verse 7."),
    "limits": ("The long compound is read as separate items; brahmacarya "
               "and vrata could also be one ('the vow of celibacy'). The "
               "sentence is not complete until verse 7."),
    "explain_hi": ("कथा का दूसरा चरण: रोग उत्पन्न होते हैं। ‘विघ्नभूताः’ का "
                   "अर्थ ‘बाधा बने हुए’ और ‘प्रादुर्भूताः’ का ‘प्रकट हुए’ "
                   "है। दूसरी पंक्ति का लम्बा समास बताता है कि किन-किन "
                   "में बाधा आई: तप, उपवास, अध्ययन, ब्रह्मचर्य, व्रत और "
                   "आयु में। अन्त की ‘-आयुषाम्’ षष्ठी है: ‘इनकी’। वाक्य "
                   "‘यदा’ से शुरू होकर श्लोक ७ के ‘तदा’ पर पूरा होता है।"),
    "hook": "यदा (जब) रोग आए → तदा (तब, श्लोक ७) ऋषि जुटे।",
    "core": False,
    "requires": [],
    "questions": [
        mcq("pretest", 0,
            "The verse speaks of diseases as विघ्नभूताः. Which meaning of विघ्न do you expect?",
            ("Obstacle", "विघ्न means an obstacle or hindrance."),
            [("Medicine", "Medicine would be the opposite of what the verse says."),
             ("Sage", "The sages come in the next verse."),
             ("Teacher", "No teacher is meant here.")],
            "Diseases became obstacles (विघ्न) to the practices named in the second line.",
            "विघ्न = obstacle."),
        match(1, "Match each word of the verse to its meaning.",
              [["विघ्नभूताः", "having become obstacles"],
               ["प्रादुर्भूताः", "arose, appeared"],
               ["शरीरिणाम्", "of embodied beings"], ["यदा", "when"]],
              "These words tell what happened and to whom.",
              "विघ्नभूताः = having become obstacles; प्रादुर्भूताः = arose; शरीरिणाम् = of embodied beings; यदा = when."),
        fill(2, "The word for 'of embodied beings' is ____ (type it in Devanagari).",
             ["शरीरिणाम्"],
             "शरीरिणाम् names those who have a body.",
             "-णाम् is the genitive plural, 'of ...'. शरीरिन् means 'one who has a body', so शरीरिणाम् is 'of the embodied'.",
             "शरीरिणाम् = of embodied beings."),
        mcq("discriminate", 3, "Which is the right split of प्रादुर्भूताः?",
            ("प्रादुः + भूताः", "A visarga before the voiced भ becomes र्, so प्रादुः + भूताः is written प्रादुर्भूताः."),
            [("प्रादुर् + अभूताः", "There is no अ in front of भूताः."),
             ("प्रादु + र्भूताः", "र्भूताः is not a word."),
             ("प्र + आदुर्भूताः", "आदुर्भूताः is not a word.")],
            "प्रादुर्भूताः = प्रादुः ('into view') + भूताः ('become'): they came into being.",
            "प्रादुर्भूताः = प्रादुः + भूताः."),
        mcq("apply", 4,
            "The second line ends in -आयुषाम्, a genitive plural. On the usual reading, what does that say about the list?",
            ("These are the things the diseases got in the way of",
             "'Of austerity ... and life': the genitive links the list to the obstacles."),
            [("These are the diseases themselves", "The diseases are रोगाः in the first line."),
             ("These are the people who study", "The people are शरीरिणाम्."),
             ("These are the sages who gather", "The sages gather in verse 7.")],
            "The list in the genitive names what the obstacles are for: practices and life itself.",
            "The genitive list = what was obstructed."),
        mcq("transfer", 5,
            "A sentence begins यदा रोगाः प्रादुर्भूताः. Which word would begin the clause that completes it?",
            ("तदा", "यदा … तदा is the matching pair: 'when ... then'."),
            [("कदा", "कदा asks 'when?'; it does not answer यदा."),
             ("यथा", "यथा pairs with तथा, 'as ... so'."),
             ("तथा", "तथा means 'so, likewise', not 'then'.")],
            "यदा 'when' is answered by तदा 'then'; verse 7 begins with तदा.",
            "यदा … तदा = when … then.",
            teaches="Sanskrit pairs words like यदा–तदा and यथा–तथा; seeing one tells you which will answer it."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "तदा भूतेष्वनुक्रोशम्",
    "section": "रोगों का आना, ऋषियों का सम्मेलन",
    "question": "Who gathered, where, and moved by what?",
    "rule": ("तदा … = Then, putting compassion for living beings foremost, "
             "great sages of virtuous deeds assembled on an auspicious "
             "slope of the Himālaya."),
    "limits": ("पार्श्वे is read as the 'slope' or side of the mountain; the "
               "verse names no peak beyond the Himālaya. The sages' names "
               "follow in the next verses."),
    "explain_hi": ("यदा–तदा का दूसरा आधा: रोग आए (श्लोक ६), तब ऋषि जुटे। "
                   "प्रेरणा ‘अनुक्रोश’ (करुणा) है; ‘पुरस्कृत्य’ का अर्थ "
                   "‘आगे रखकर’ है, यानी करुणा उनके कार्य का पहला कारण "
                   "है। ‘भूतेषु’ सप्तमी है: प्राणियों के प्रति। स्थान "
                   "हिमालय का शुभ पार्श्व है। ‘समेताः’ का अर्थ ‘इकट्ठे हुए’ "
                   "और ‘महर्षयः’ महा + ऋषयः है।"),
    "hook": "रोग → करुणा आगे → ऋषि हिमालय पर: यदा (६) → तदा (७)।",
    "core": True,
    "requires": ["su1-006"],
    "questions": [
        mcq("pretest", 0,
            "Diseases have appeared. What do you expect moved the great sages to assemble?",
            ("Compassion for living beings", "The verse says they put compassion first."),
            [("A command from Indra", "No command is mentioned."),
             ("A wish for royal gifts", "Nothing of the kind is said."),
             ("A plan to hold a sacrifice", "No sacrifice is mentioned.")],
            "They assembled out of compassion (अनुक्रोश) for living beings.",
            "अनुक्रोश = compassion, the reason they gathered."),
        match(1, "Match each word of the verse to its meaning.",
              [["अनुक्रोशम्", "compassion"], ["पुरस्कृत्य", "putting foremost"],
               ["समेताः", "assembled"], ["शुभे", "auspicious"]],
              "These words say why and how the sages met.",
              "अनुक्रोशम् = compassion; पुरस्कृत्य = putting foremost; समेताः = assembled; शुभे = auspicious."),
        fill(2, "The word for 'great sages' is ____ (type it in Devanagari).",
             ["महर्षयः"],
             "महर्षयः are the doers of the assembling.",
             "महर्षयः = महा + ऋषयः, and -अयः is the nominative plural: the sages are the subject.",
             "महर्षयः = great sages (the subject)."),
        mcq("discriminate", 3, "Which is the right split of भूतेष्वनुक्रोशम्?",
            ("भूतेषु + अनुक्रोशम्", "उ before a different vowel becomes व्, so भूतेषु + अनुक्रोशम् is written भूतेष्वनुक्रोशम्."),
            [("भूतेष्व + अनुक्रोशम्", "भूतेष्व is not a word."),
             ("भूतेषु + वनुक्रोशम्", "वनुक्रोशम् is not a word."),
             ("भूते + षु अनुक्रोशम्", "षु is only an ending, not a word.")],
            "भूतेष्वनुक्रोशम् = भूतेषु ('for beings') + अनुक्रोशम् ('compassion').",
            "भूतेष्वनुक्रोशम् = भूतेषु + अनुक्रोशम्."),
        mcq("apply", 4,
            "भूतेषु ends in -षु, the locative plural. How does it relate to the compassion?",
            ("It is felt toward the beings", "The locative gives the one at whom the feeling is directed."),
            [("It is felt by the beings", "The doer would end differently."),
             ("It comes from the beings", "'From' would need the ablative.")],
            "भूतेषु + अनुक्रोशम् = compassion toward living beings.",
            "Locative of the object of a feeling = 'toward' (the locative itself means 'in, among')."),
        mcq("transfer", 5,
            "In verse 3, बुद्ध्वा named an earlier act (having understood). By the same pattern, what is true of पुरस्कृत्य?",
            ("It names an earlier act, and its doer is the sages",
             "-त्य ends a 'having done' word, as -त्वा does, with the same doer as the main sentence."),
            [("It is a noun naming a place", "The place is पार्श्वे."),
             ("It is a verb in the future tense", "It does not end like a future."),
             ("It names what Indra did", "Indra is not in this verse.")],
            "बुद्ध्वा and पुरस्कृत्य are the same kind of word: an earlier act by the same doer.",
            "-त्वा / -त्य words = 'having done', with the sentence's own doer.",
            teaches="-त्वा and -त्य both mean 'having done'; -त्य is used when a prefix comes before the root (पुरस्-कृ)."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "अङ्गिरा जमदग्निश्च",
    "section": "एकत्र हुए ऋषि",
    "question": "Which sages does verse 8 name, in what order?",
    "rule": ("अङ्गिरा, जमदग्नि, वसिष्ठ, कश्यप, भृगु | आत्रेय, गौतम, साङ्ख्य, "
             "पुलस्त्य, नारद, असित."),
    "limits": ("साङ्ख्य may be a personal name or a title ('the Sāṅkhya "
               "teacher'), and गौतमः साङ्ख्यः might be one person; this "
               "card reads them as two names."),
    "explain_hi": ("यहाँ से जुटे हुए ऋषियों की सूची शुरू होती है, जो आगे के "
                   "श्लोकों में चलती है। पहली पंक्ति में पाँच नाम हैं और "
                   "दूसरी में छह। ‘नारदो ऽसितः’ का अर्थ नारदः + असितः है; "
                   "ऽ चिह्न बताता है कि असितः का आरम्भिक ‘अ’ लुप्त हुआ है। "
                   "पूर्ण सूची के लिए अगले श्लोक देखें।"),
    "hook": "पहली पंक्ति: अ-ज-व-क-भृ · दूसरी: आ-गौ-सा-पु-ना-अ (पहले अक्षरों से)।",
    "core": False,
    "requires": ["su1-007"],
    "questions": [
        mcq("pretest", 0,
            "Verse 8 begins a list of sages. Which of these names do you expect in it?",
            ("वसिष्ठ", "Vasiṣṭha is one of the sages of the list."),
            [("इन्द्र", "Indra is a god, not one of the gathered sages."),
             ("प्रजापति", "Prajāpati is a god in the chain of verse 4."),
             ("अश्विनौ", "The Aśvins are the twin gods of verse 4.")],
            "The list names sages; the gods of the chain (Brahmā, Prajāpati, the Aśvins, Indra) are not in it.",
            "Verse 8 lists sages, not gods."),
        order(1, "Put these four names in the order of verse 8.",
              ["जमदग्निः", "वसिष्ठः", "कश्यपः", "भृगुः"],
              "These four follow अङ्गिरा in the first line.",
              "जमदग्नि → वसिष्ठ → कश्यप → भृगु."),
        fill(2, "In the first line the name after कश्यपः is ____ (type it in Devanagari).",
             ["भृगुः", "भृगु"],
             "भृगुः closes the first line.",
             "भृगुः is the last name of the first line; the second line opens with आत्रेयः.",
             "Line 1 ends with भृगुः; line 2 begins with आत्रेयः."),
        mcq("discriminate", 3, "Which gives the two words of नारदो ऽसितः before sandhi?",
            ("नारदः + असितः", "-ः before अ becomes ो, and ऽ marks the dropped अ."),
            [("नारदो + असितः", "The original ending is -ः; ो comes from the join."),
             ("नारदः + सितः", "The name is असित, with its अ."),
             ("नार + दोऽसितः", "दोऽसितः is not a word.")],
            "नारदो ऽसितः = नारदः + असितः: two names.",
            "नारदो ऽसितः = नारदः + असितः."),
        mcq("apply", 4, "Taking साङ्ख्यः as a separate name, which comes right after गौतमः in verse 8?",
            ("साङ्ख्यः", "The second line runs आत्रेयः, गौतमः, साङ्ख्यः."),
            [("पुलस्त्यः", "पुलस्त्यः comes after साङ्ख्यः."),
             ("नारदः", "नारदः comes near the end of the line."),
             ("असितः", "असितः is the last name.")],
            "आत्रेयः → गौतमः → साङ्ख्यः → पुलस्त्यः → नारदः → असितः.",
            "After गौतमः comes साङ्ख्यः."),
        mcq("transfer", 5,
            "आत्रेयः appears in the second line of this verse. Where did you meet the same name earlier in the chapter?",
            ("In the opening formula इति ह स्माह भगवानात्रेयः",
             "Line 2 of the chapter names Ātreya as the speaker."),
            [("In verse 3, as the one who approached Indra", "Verse 3 names Bharadvāja."),
             ("In verse 4, as the first receiver", "Verse 4 names Prajāpati."),
             ("In verse 6, as a disease", "Verse 6 names diseases, not people.")],
            "The same name occurs again; the verse does not say whether it is the same person.",
            "आत्रेयः: the speaker named in line 2 and a name in verse 8 (same name; same person is not stated).",
            teaches="A name can recur in a text; check where else you have met it before deciding it is new."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "अगस्त्यो वामदेवश्च",
    "section": "एकत्र हुए ऋषि",
    "question": "Which sages does verse 9 add to the list?",
    "rule": ("अगस्त्य, वामदेव, मार्कण्डेय और आश्वलायन, पारिक्षि, भिक्षु आत्रेय, "
             "भरद्वाज, कपिञ्जल."),
    "limits": ("The edition notes the variant कपिष्ठलः for कपिञ्जलः. "
               "भिक्षुरात्रेयः is read as one person, Bhikṣu Ātreya, though "
               "it could be two names."),
    "explain_hi": ("सूची आगे बढ़ती है। ‘मार्कण्डेयाश्वलायनौ’ द्विवचन का "
                   "द्वन्द्व है: दो नाम एक शब्द में, अन्त में ‘-औ’। "
                   "‘भिक्षुरात्रेयः’ = भिक्षुः + आत्रेयः; इसे यहाँ एक "
                   "व्यक्ति (भिक्षु आत्रेय) पढ़ा गया है। ‘भरद्वाज’ वही नाम "
                   "है जो श्लोक ३ में आया था। ‘कपिञ्जलः’ का पाठभेद "
                   "‘कपिष्ठलः’ है (पाठ-टिप्पणी देखें)।"),
    "hook": "अगस्त्य · वामदेव · मार्कण्डेय–आश्वलायन | पारिक्षि · भिक्षु आत्रेय · भरद्वाज · कपिञ्जल (अ-वा-मा-आ | पा-भि-भ-क)।",
    "core": False,
    "requires": ["su1-008"],
    "questions": [
        mcq("pretest", 0,
            "One name in verse 9 is a sage you met in verse 3. Which do you expect?",
            ("भरद्वाजः", "Bharadvāja, who approached Indra in verse 3, is named again."),
            [("इन्द्रः", "Indra is a god, not one of the sages."),
             ("प्रजापतिः", "Prajāpati is a god in the chain of verse 4."),
             ("शक्रः", "Śakra is another name of Indra.")],
            "भरद्वाजः appears in the list.",
            "भरद्वाजः is in verse 3 and again in the list of verse 9."),
        match(1, "Match each Devanagari name to its Latin spelling.",
              [["अगस्त्यः", "Agastya"], ["वामदेवः", "Vāmadeva"],
               ["पारिक्षिः", "Pārikṣi"], ["कपिञ्जलः", "Kapiñjala"]],
              "Reading the names in Devanagari is the point of this card.",
              "अगस्त्यः = Agastya; वामदेवः = Vāmadeva; पारिक्षिः = Pārikṣi; कपिञ्जलः = Kapiñjala."),
        fill(2, "The ending -औ on a name like मार्कण्डेयाश्वलायनौ shows that it names ____ sages (type the number).",
             ["2", "२", "two", "Two", "दो", "द्वि"],
             "-औ is the dual ending: two items in one word.",
             "On names in -अ, -औ marks the dual. मार्कण्डेयाश्वलायनौ joins two names, Mārkaṇḍeya and Āśvalāyana. (Do not confuse आदौ in verse 4: that is the locative singular of आदि.)",
             "On names in -अ, -औ = two."),
        mcq("discriminate", 3, "Which is the right split of मार्कण्डेयाश्वलायनौ?",
            ("मार्कण्डेय + आश्वलायनौ", "-अ + आ- merge into आ, so मार्कण्डेय + आश्वलायनौ is written मार्कण्डेयाश्वलायनौ."),
            [("मार्कण्डेया + श्वलायनौ", "श्वलायनौ is not a name."),
             ("मार्कण्डे + याश्वलायनौ", "याश्वलायनौ is not a name."),
             ("मार्कण्डेय + अश्वलायनौ", "Sandhi alone cannot tell अ + अ from अ + आ here, but the sage's name is आश्वलायन, with a long आ.")],
            "मार्कण्डेयाश्वलायनौ = मार्कण्डेय + आश्वलायनौ: two sages.",
            "मार्कण्डेयाश्वलायनौ = मार्कण्डेय + आश्वलायनौ."),
        mcq("apply", 4,
            "A copy has कपिष्ठलः where this edition has कपिञ्जलः. What kind of difference is this?",
            ("A variant reading of the same name, recorded in the notes",
             "The edition itself lists कपिष्ठलः as a variant."),
            [("A different sage in the list", "Nothing in the text adds another name here."),
             ("A change caused by sandhi", "Sandhi changes letters only where two words meet; this difference is inside the name."),
             ("A mistake made by the edition", "The edition records both readings.")],
            "Variant readings of a name are noted, not silently corrected.",
            "कपिञ्जलः / कपिष्ठलः = two readings of the name in the text."),
        mcq("transfer", 5,
            "A new line reads वसिष्ठभरद्वाजौ. How many sages does it name, and why?",
            ("Two, because -औ is the dual ending",
             "The dual joins वसिष्ठ and भरद्वाज in one word."),
            [("One, because it is a single compound name", "-औ would not appear on a single name like that."),
             ("Three, because the word is long", "Length does not count names."),
             ("It cannot be told", "The ending tells you.")],
            "The dual ending -औ works with any pair of names in -अ.",
            "Name + name + -औ = two sages.",
            teaches="You can count the items in a dual compound from the ending, even for names you have not met."),
    ],
}

# --------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "विश्वामित्राश्मरथ्यौ च",
    "section": "एकत्र हुए ऋषि",
    "question": "Who else is named in verse 10, and which readings are uncertain?",
    "rule": ("Viśvāmitra and Āśmarathya, Cyavana the Bhārgava, Abhijit, "
             "Gārgya, Śāṇḍilya and Kauṇḍilya, Vārkṣi, Devala and Gālava."),
    "limits": ("A word space may be missing in …कौण्डिल्यौवार्क्षिः…; the "
               "edition notes the variant कौण्डिन्य; भार्गवश्च्यवनः is read "
               "as one person (it could be two); आश्मरथ्य could also be "
               "अश्मरथ्य."),
    "explain_hi": ("सूची का यह भाग तीन जोड़ों में बँटा है, जो द्विवचन (-औ) में "
                   "हैं: विश्वामित्र–आश्मरथ्य, शाण्डिल्य–कौण्डिल्य, "
                   "देवल–गालव। बीच में एकवचन नाम हैं: भार्गव च्यवन, "
                   "अभिजित्, गार्ग्य, वार्क्षि। पाठ में एक जगह शब्द-विराम "
                   "छूटा हुआ दिखता है; इसी कारण यह कार्ड ‘मध्यम विश्वास’ का "
                   "है (पाठ-टिप्पणी देखें)।"),
    "hook": "तीन जोड़े (-औ): विश्वामित्र–आश्मरथ्य · शाण्डिल्य–कौण्डिल्य · देवल–गालव; बीच में च्यवन, अभिजित्, गार्ग्य, वार्क्षि।",
    "core": False,
    "requires": ["su1-009"],
    "questions": [
        mcq("pretest", 0,
            "विश्वामित्राश्मरथ्यौ ends in -औ, like मार्कण्डेयाश्वलायनौ in verse 9. How many sages do you expect it to name?",
            ("Two", "On names in -अ, -औ marks a pair (the dual)."),
            [("One", "A single name would not take -औ here."),
             ("Three", "-औ is for two, not three."),
             ("Four", "-औ is for two, not four.")],
            "विश्वामित्राश्मरथ्यौ names two sages: Viśvāmitra and Āśmarathya.",
            "-औ = two sages."),
        match(1, "Match each Devanagari name to its Latin spelling.",
              [["च्यवनः", "Cyavana"], ["गार्ग्यः", "Gārgya"],
               ["वार्क्षिः", "Vārkṣi"], ["गालवः", "Gālava"]],
              "Reading these names in Devanagari is the point of this card.",
              "च्यवनः = Cyavana; गार्ग्यः = Gārgya; वार्क्षिः = Vārkṣi; गालवः = Gālava."),
        fill(2, "Complete the last pair of the verse: देवल और ____ (type the name in Devanagari).",
             ["गालव", "गालवः"],
             "देवलगालवौ is the last pair of the verse.",
             "देवलगालवौ is a dual compound of देवल and गालव, and it closes the verse.",
             "देवलगालवौ = देवल + गालव."),
        mcq("discriminate", 3, "Which is the right split of भार्गवश्च्यवनः?",
            ("भार्गवः + च्यवनः", "A visarga before च becomes श्, so भार्गवः + च्यवनः is written भार्गवश्च्यवनः."),
            [("भार्गव + श्च्यवनः", "श्च्यवनः is not a name."),
             ("भार्गवः + श्यवनः", "The name is च्यवन, with च."),
             ("भार्गवश् + च्यवनः", "श् is not a word-ending that stands on its own.")],
            "भार्गवश्च्यवनः = भार्गवः ('the Bhārgava') + च्यवनः (Cyavana).",
            "भार्गवश्च्यवनः = भार्गवः + च्यवनः."),
        multi("apply", 4, "Which of these are dual pairs in verse 10?",
              [("विश्वामित्राश्मरथ्यौ", "Right: -औ names Viśvāmitra and Āśmarathya."),
               ("गार्ग्यः", "A single name, with -ः."),
               ("शाण्डिल्यकौण्डिल्यौ", "Right: -औ names Śāṇḍilya and Kauṇḍilya."),
               ("देवलगालवौ", "Right: -औ names Devala and Gālava."),
               ("अभिजित्", "A single name.")],
              [0, 2, 3],
              "Three words end in -औ and name pairs; the other two are single names.",
              "विश्वामित्राश्मरथ्यौ, शाण्डिल्यकौण्डिल्यौ, देवलगालवौ are pairs."),
        mcq("transfer", 5,
            "In another book you find कौण्डिन्य where verse 10 has कौण्डिल्य. What should you conclude?",
            ("Likely the same name spelt differently; check the note",
             "The edition itself records कौण्डिन्य as a variant of this name."),
            [("A different sage, for certain", "The edition's own note shows both spellings occur for this name."),
             ("The other book is wrong", "Neither spelling can be called wrong without evidence."),
             ("Nothing can be said about it", "Variants are recorded precisely so you can compare.")],
            "Variant spellings of names are common; compare notes before deciding.",
            "Same name, two spellings: check the variant note first.",
            teaches="A name spelt differently in another source may be a variant; the edition's note is the first place to look."),
    ],
}


NOTES_HI = {
    "1": "‘दीर्घञ्जीवितीयम्’ अलुक् समास है: पहले पद ‘दीर्घम्’ की विभक्ति बनी रहती है और अन्त में ‘-ईय’ जुड़ता है।",
    "2": "‘ह’ और ‘स्म’ निपात हैं; पूरा ‘इति ह स्माह’ कथन की परम्परागत शैली है।",
    "3": "‘उग्रतपाः’ का विसर्ग ‘बुद्ध्वा’ के घोष ‘ब्’ से पहले लुप्त हुआ है (उग्रतपा बुद्ध्वा)। ‘बुद्ध्वा शरण्यम्’ का अर्थ है ‘उन्हें शरण देने योग्य जानकर’।",
    "4": "पाठ में ‘पजापतिः’ छपा है; ‘प्रजापतिः’ अपेक्षित है (ब्रह्मा → प्रजापति → अश्विनौ), यहाँ ‘र्’ छूटा लगता है। छन्द नहीं बदलता। यह सुझाव एक ही स्रोत (SARIT) पर आधारित है; दूसरा पाठ-साक्ष्य अभी नहीं देखा गया। ‘यथाप्रोक्तम्’ को क्रियाविशेषण (‘ठीक जैसा कहा गया’) भी पढ़ा जा सकता है; ‘ततः’ का अर्थ ‘उनसे’ या केवल ‘तब’ हो सकता है।",
    "5": "‘केवलम्’ को ‘पूरा (आयुर्वेद)’ विशेषण या ‘पूर्णतः’ क्रियाविशेषण पढ़ा जा सकता है। ‘ऋषिप्रोक्तः’ का भाव ‘ऋषियों द्वारा कहा/प्रेरित’ है। ‘तस्मात्’ का अर्थ ‘इसलिए’ है।",
    "6": "‘ब्रह्मचर्यव्रत’ को एक पद (‘ब्रह्मचर्य का व्रत’) भी माना जा सकता है। ‘शरीरिणाम्’ को ‘प्रादुर्भूताः’ के साथ (‘देहधारियों में प्रकट हुए’) या समास के साथ पढ़ा जा सकता है। वाक्य श्लोक ७ में पूरा होता है।",
    "7": "यह वाक्य श्लोक ६ से चला आता है; ऋषियों के नाम श्लोक ८ से आगे हैं। ‘पार्श्व’ का अर्थ बगल या ढलान है।",
    "8": "‘साङ्ख्यः’ व्यक्ति का नाम भी हो सकता है और ‘साङ्ख्य-आचार्य’ भी; ‘गौतमः साङ्ख्यः’ को एक व्यक्ति भी पढ़ा जा सकता है। यह कार्ड इन्हें दो नाम मानता है। ‘अङ्गिराः’ का विसर्ग ‘ज’ से पहले लुप्त हुआ है।",
    "9": "पाठभेद: ‘कपिञ्जलः’ की जगह ‘कपिष्ठलः’। ‘भिक्षुरात्रेयः’ को एक व्यक्ति (भिक्षु आत्रेय) माना गया है; दो नाम भी पढ़े जा सकते हैं। ‘पारिक्षि’ की जगह ‘पारीक्षि’ वर्तनी सम्भव है (स्रोत के पाठभेदों में नहीं दी गई)।",
    "10": "विश्वास: मध्यम। (१) ‘शाण्डिल्यकौण्डिल्यौवार्क्षिः’ में शब्द-विराम छूटा हो सकता है (शाण्डिल्यकौण्डिल्यौ वार्क्षिः); इससे पाठ नहीं बदलता। (२) पाठभेद: ‘कौण्डिन्यौ’। (३) ‘भार्गवश्च्यवनः’ को एक व्यक्ति माना गया है; दो नाम भी हो सकते हैं। (४) ‘आश्मरथ्य’ को ‘अश्मरथ्य’ भी पढ़ा जा सकता है (सम्भावित, स्रोत के पाठभेदों में नहीं)।",
}
