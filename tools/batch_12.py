from ch1_authored import mcq, match, order, multi
from ch1_authored import fill as _fill


def fill(rung, q, accept, e1, e2, teaches, rule):
    return _fill(rung, q, accept, e1 + " " + e2, teaches, rule)

AUTHORED = {}

# ------------------------------------------------------------- unit 110
AUTHORED["110"] = {
    "title": "पाण्डुरोगे ऽम्लपित्ते च",
    "question": "In which conditions is milk beneficial, and which one does verse 110 stress?",
    "rule": ("A list of locatives, 'in anaemia, acid dyspepsia, wasting, gulma, "
             "udara, diarrhoea, fever, burning, swelling', with swelling "
             "stressed by विशेषतः. The word पथ्यम् that completes it is in verse 111."),
    "limits": ("The verse names no subject and no verb; 'milk is beneficial' is "
               "carried over from verses 107-109 and from पथ्यम् in 111. "
               "The verse gives no reason why each condition is on the list."),
    "explain_hi": ("यह श्लोक दूध के उपयोग की रोग-सूची शुरू करता है; दूध का प्रसंग श्लोक १०७–१०९ से चला आता है। "
                   "सभी रोग सप्तमी विभक्ति में हैं: ‘पाण्डुरोगे’ = पाण्डु रोग में, ‘ज्वरे’ = ज्वर में। "
                   "‘हितकर है’ वाला शब्द पथ्यम् अगले श्लोक (१११) में आता है, इसलिए वाक्य वहीं पूरा होता है। "
                   "‘विशेषतः’ यानी ‘विशेष रूप से’ सूची के अन्तिम रोग श्वयथु (सूजन) पर जोर देता है। "
                   "ध्यान दें: ‘श्वयथौ’ में -औ द्विवचन नहीं है; यह श्वयथु का सप्तमी एकवचन है।"),
    "hook": "पाण्डु · अम्लपित्त · शोष · गुल्म · उदर | अतीसार · ज्वर · दाह · श्वयथु (विशेषतः)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 110 lists conditions and then adds विशेषतः. Which condition does it single out?",
            ("श्वयथु (swelling)", "श्वयथौ च विशेषतः: 'and especially in swelling'."),
            [("ज्वर (fever)", "Fever is in the list, but it is not the one stressed."),
             ("दाह (burning sensation)", "Burning is in the list, but it is not the one stressed."),
             ("अतीसार (diarrhoea)", "Diarrhoea is in the list, but it is not the one stressed.")],
            "विशेषतः stands at the end of the verse, next to श्वयथौ.",
            "श्वयथौ च विशेषतः = and especially in swelling."),
        match(1, "Match each condition named in the verse to its meaning.",
              [["अम्लपित्ते", "in acid dyspepsia"], ["अतीसारे", "in diarrhoea"],
               ["दाहे", "in burning sensation"], ["श्वयथौ", "in swelling"]],
              "Each word is a locative: 'in ...'.",
              "अम्लपित्ते, अतीसारे, दाहे, श्वयथौ are all 'in' (locative) forms."),
        fill(2, "Complete the middle of the list: अतीसारे, ____, दाहे. Type the word for 'in fever'.",
             ["ज्वरे", "ज्वर"],
             "The verse reads अतीसारे ज्वरे दाहे: diarrhoea, fever, burning.",
             "ज्वरे is the locative singular of ज्वर: 'in fever'. The whole list is in this case.",
             "A string of words ending in -ए (locative) reads 'in A, in B, in C'.",
             "ज्वरे = in fever."),
        mcq("discriminate", 3, "Which is the right split of तथोदरे?",
            ("तथा + उदरे", "आ + उ becomes ओ, so तथा + उदरे is written तथोदरे."),
            [("तथ + उदरे", "तथ is not a word here; the word is तथा, 'and also'."),
             ("तथो + दरे", "दरे is not the word; the condition is उदर."),
             ("तथा + ओदरे", "There is no word ओदर.")],
            "तथोदरे = तथा ('and also') + उदरे ('in udara').",
            "आ + उ → ओ: तथा + उदरे = तथोदरे."),
        mcq("apply", 4,
            "श्वयथौ ends in -औ, like the dual names of verse 9. What does it mean here?",
            ("In swelling: locative singular",
             "The data gives m. loc. sg. of श्वयथु; here -औ is not the dual."),
            [("Two swellings: dual", "The meaning is 'in swelling', one condition in a list of locatives."),
             ("Of swelling: genitive", "The genitive would be श्वयथोः."),
             ("By swelling: instrumental", "The instrumental would be श्वयथुना.")],
            "On a word in -उ, -औ can be the locative singular; the list around it settles the case.",
            "-औ is not always dual: श्वयथौ = in swelling."),
        mcq("transfer", 5,
            "A made-up line reads कासे श्वासे ज्वरे च हितम्. What do कासे, श्वासे, ज्वरे tell you?",
            ("Three conditions, each read as 'in ...', for which something is beneficial",
             "Like verse 110, a run of -ए words is a list of 'in ...' conditions."),
            [("Three remedies given by the physician", "The -ए words name conditions, not remedies."),
             ("One condition with three names", "Three words in a row make a list; they are not one name."),
             ("Three people who give the remedy", "-ए here is the 'in' ending, not a person.")],
            "The same list pattern as verse 110: condition words in the locative, then the word for 'beneficial'.",
            "Locative list + 'beneficial' = 'good in these conditions'.",
            teaches="You can read a new list of conditions by its endings: -ए words are 'in this condition', and the word for 'beneficial' comes at the end."),
    ],
}

# ------------------------------------------------------------- unit 111
AUTHORED["111"] = {
    "title": "योनिशुक्रप्रदोषेषु",
    "question": "What further conditions does verse 111 list, and for whom is the remedy wholesome?",
    "rule": ("Disorders of योनि and शुक्र, scanty urine and hard faeces; "
             "पथ्यम् = wholesome, for those with Vāta-Pitta disorders "
             "(वातपित्तविकारिणाम्). This verse finishes the sentence of verse 110."),
    "limits": ("योनिशुक्रप्रदोषेषु may be read 'disorders of yoni and of śukra' or "
               "as 'disorders of yoni-śukra' taken together. "
               "The verse does not name milk; it is understood from the context."),
    "explain_hi": ("श्लोक ११० की सूची यहाँ पूरी होती है। पहले योनि और शुक्र के दोष, फिर "
                   "‘मूत्रेषु अप्रचुरेषु’ (मूत्र कम होने पर) और ‘पुरीषे ग्रथिते’ (मल गाँठदार होने पर) "
                   "आते हैं; ये दोनों ‘जब ... हो’ वाले सप्तमी रूप हैं। "
                   "‘अप्रचुर’ = अ (नहीं) + प्रचुर (बहुत), यानी थोड़ा। "
                   "अन्त में ‘पथ्यम्’ (हितकर) आता है, जो श्लोक ११० की पूरी सूची के लिए है। "
                   "‘वातपित्तविकारिणाम्’ षष्ठी बहुवचन है: ‘वात-पित्त के विकार वालों के लिए’।"),
    "hook": "योनि–शुक्र दोष · मूत्र कम · मल कठिन → पथ्यम् (वात-पित्त विकार वालों के लिए)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The verse ends with the word पथ्यम्. What does it say about the milk?",
            ("It is wholesome, suitable",
             "पथ्य means wholesome; it completes the lists of verses 110 and 111."),
            [("It is harmful", "That would be अपथ्य, not पथ्यम्."),
             ("It is forbidden", "पथ्यम् is a positive word."),
             ("It is costly", "The word says nothing about price.")],
            "पथ्यम् = wholesome. It is the word that all the 'in ...' conditions wait for.",
            "पथ्यम् = wholesome."),
        match(1, "Match each word to its meaning.",
              [["योनि", "female genital tract"], ["शुक्र", "semen"],
               ["मूत्र", "urine"], ["पुरीष", "faeces"]],
              "These four words name the body parts and products in the verse.",
              "योनि = female genital tract; शुक्र = semen; मूत्र = urine; पुरीष = faeces."),
        fill(2, "पुरीषे ____: type the word that completes the phrase for faeces that are knotted and hard.",
             ["ग्रथिते"],
             "पुरीषे ग्रथिते: 'when the faeces are hard'.",
             "ग्रथिते is the locative singular of ग्रथित (knotted, hard). Together with पुरीषे it reads 'when the faeces are hard'.",
             "Two words in the same locative can mean 'when X is Y'.",
             "ग्रथिते = when hard (said of पुरीषे)."),
        mcq("discriminate", 3, "Which is the right split of मूत्रेष्वप्रचुरेषु?",
            ("मूत्रेषु + अप्रचुरेषु", "उ before a different vowel becomes व्, so मूत्रेषु + अप्रचुरेषु is written मूत्रेष्वप्रचुरेषु."),
            [("मूत्रेषु + प्रचुरेषु", "That would give 'plentiful urine' and would not show a व्."),
             ("मूत्रेष्व + अप्रचुरेषु", "The व् belongs to the sandhi; मूत्रेष्व is not a word."),
             ("मूत्रे + षु + अप्रचुरेषु", "-षु is an ending, not a separate word.")],
            "मूत्रेष्वप्रचुरेषु = मूत्रेषु ('in urines') + अप्रचुरेषु ('scanty').",
            "उ + अ → व् + अ: मूत्रेषु + अप्रचुरेषु = मूत्रेष्वप्रचुरेषु."),
        multi("apply", 4, "Which of these does verse 111 itself name?",
              [("Disorders of semen (शुक्र)", "Right: शुक्रप्रदोषेषु."),
               ("Scanty urine", "Right: मूत्रेष्वप्रचुरेषु."),
               ("Hard faeces", "Right: पुरीषे ग्रथिते."),
               ("Fever (ज्वर)", "Fever is in verse 110, not here."),
               ("Anaemia (पाण्डुरोग)", "Anaemia is in verse 110, not here.")],
              [0, 1, 2],
              "Verse 111 names disorders of yoni and śukra, scanty urine and hard faeces; the others are in 110.",
              "111: yoni-śukra disorders, scanty urine, hard faeces."),
        mcq("transfer", 5,
            "A made-up line says ज्वरे शान्ते पथ्यम्. By the pattern of पुरीषे ग्रथिते, what is the best sense?",
            ("Wholesome when the fever has subsided",
             "Two words in the same locative can mean 'when X has become Y'."),
            [("Wholesome in fever and in peace, two separate conditions", "Like पुरीषे ग्रथिते, the second word describes the first; it is not another condition."),
             ("Wholesome for the one who gives the fever", "-ए does not mark a person."),
             ("Wholesome by means of fever", "-ए is not the 'by means of' ending.")],
            "Noun + describing word in the same locative = 'when the noun is so'.",
            "Locative + locative describing it = 'when ...'.",
            teaches="A pair of locatives, noun and describing word, can give a 'when' clause, so you can read a new phrase like ज्वरे शान्ते."),
    ],
}

# ------------------------------------------------------------- unit 112
AUTHORED["112"] = {
    "title": "नस्यालेपावगाहेषु",
    "question": "In which therapies is milk used, and how wide is the statement?",
    "rule": ("In nasya, ālepa, avagāha, vamana, āsthāpana, virecana and snehana, "
             "milk is used everywhere: पयः सर्वत्र युज्यते."),
    "limits": ("सर्वत्र ('everywhere') covers the therapies listed in this verse; "
               "the verse does not say that milk is used in every disease or in every "
               "form, and it does not describe how the therapies are done."),
    "explain_hi": ("पिछले दो श्लोकों में रोग थे; यह श्लोक चिकित्सा-विधियाँ गिनाता है: नस्य, आलेप, अवगाह, "
                   "वमन, आस्थापन, विरेचन और स्नेहन। सभी सप्तमी में हैं, यानी ‘इनमें’। "
                   "कथन यह है: ‘पयः सर्वत्र युज्यते’, दूध का प्रयोग (इन सब में) सब जगह होता है। "
                   "श्लोक ११० में ‘विशेषतः’ एक रोग पर जोर देता था; यहाँ ‘सर्वत्र’ सबको एक-सा गिनता है।"),
    "hook": "नस्य · आलेप · अवगाह · वमन · आस्थापन · विरेचन · स्नेहन: पयः सर्वत्र युज्यते।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does the verse say about the use of milk (पयः) in the therapies it lists?",
            ("It is used everywhere, in all of them", "पयः सर्वत्र युज्यते."),
            [("Only in emesis", "Emesis is one of seven therapies listed, not the only one."),
             ("Never in purgation", "विरेचने is in the list: milk is used there too."),
             ("Only in oleation", "स्नेहने is one of seven; the verse says सर्वत्र.")],
            "सर्वत्र = everywhere. The verse covers all seven therapies.",
            "पयः सर्वत्र युज्यते = milk is used everywhere."),
        match(1, "Match each therapy to its meaning.",
              [["नस्य", "nasal therapy"], ["अवगाह", "immersion bath"],
               ["वमन", "emesis"], ["विरेचन", "purgation"]],
              "Four of the seven therapies named in the verse.",
              "नस्य = nasal therapy; अवगाह = immersion bath; वमन = emesis; विरेचन = purgation."),
        fill(2, "The verse says पयः ____ युज्यते. Type the word that means everywhere.",
             ["सर्वत्र"],
             "The verse ends पयः सर्वत्र युज्यते.",
             "सर्वत्र is सर्व ('all') with the ending -त्र ('in/at'): everywhere.",
             "-त्र added to a pronoun-like word gives 'in/at', so सर्वत्र = in all places, in all cases.",
             "सर्वत्र = everywhere."),
        mcq("discriminate", 3, "Which is the right split of नस्यालेपावगाहेषु?",
            ("नस्य + आलेप + अवगाहेषु", "अ + आ and अ + अ both give आ; the three words are नस्य, आलेप, अवगाह."),
            [("नस्या + आलेप + अवगाहेषु", "नस्या is not the word; it is नस्य."),
             ("नस्य + लेप + आवगाहेषु", "The words are आलेप and अवगाह; they begin with a vowel."),
             ("नस्य + आलेपा + वगाहेषु", "आलेपा and वगाह are not words.")],
            "नस्यालेपावगाहेषु joins three therapies: नस्य, आलेप, अवगाह.",
            "अ + आ → आ and अ + अ → आ: नस्य + आलेप + अवगाह = नस्यालेपावगाह."),
        multi("apply", 4, "Which of these does verse 112 list as therapies where milk is used?",
              [("Nasal therapy (नस्य)", "Right: नस्य is first in the verse."),
               ("Oleation (स्नेहन)", "Right: स्नेहने च."),
               ("Decoction enema (आस्थापन)", "Right: वमनास्थापनेषु."),
               ("Fever (ज्वर)", "Fever is a condition in verse 110, not a therapy."),
               ("Anaemia (पाण्डुरोग)", "Anaemia is a condition in verse 110, not a therapy.")],
              [0, 1, 2],
              "Verse 112 lists therapies; the conditions belong to 110 and 111.",
              "112 = therapies; 110-111 = conditions."),
        mcq("transfer", 5,
            "A made-up line says ज्वरे कासे च, विशेषतः श्वासे. Compared with सर्वत्र in verse 112, what does विशेषतः do?",
            ("It picks out one item (श्वासे) for stress, instead of treating all alike",
             "विशेषतः stresses one item, as in verse 110; सर्वत्र covers all alike."),
            [("It covers all three items alike", "That is what सर्वत्र does, not विशेषतः."),
             ("It removes the last item from the list", "It stresses an item; it does not remove it."),
             ("It means the same as सर्वत्र", "The two words work in opposite ways.")],
            "विशेषतः ('especially') singles out; सर्वत्र ('everywhere') includes all.",
            "विशेषतः = singles out one; सर्वत्र = covers all.",
            teaches="Two small words steer a list: विशेषतः stresses one item, सर्वत्र spreads the statement over all."),
    ],
}

# ------------------------------------------------------------- unit 113
AUTHORED["113"] = {
    "title": "यथाक्रमं क्षीरगुणान्",
    "question": "What does the speaker promise about the qualities of the milks, and where?",
    "rule": ("'I shall describe (वक्ष्यामि) the qualities of the milks, in due order, "
             "each one separately and completely, later (भूयः) in the chapter on food and "
             "drink etc. (अन्नपानादिके अध्याये).'"),
    "limits": ("The verse does not name the chapter's number; which chapter "
               "अन्नपानादिक is, is an identification made from outside this verse. "
               "The promise is about the qualities of each milk, not about milk in general."),
    "explain_hi": ("यहाँ वक्ता वचन देता है कि दूधों के गुण आगे अन्नपान वाले अध्याय में क्रम से, अलग-अलग और पूर्ण रूप से कहे जाएँगे। "
                   "‘यथाक्रमम्’ = क्रम से, ‘पृथक् पृथक्’ = अलग-अलग, ‘अशेषतः’ = पूर्ण रूप से। "
                   "‘वक्ष्यामि’ उत्तम पुरुष एकवचन भविष्य है: ‘मैं कहूँगा’। "
                   "‘अन्नपानादिके अध्याये’ का अर्थ ‘अन्न-पान आदि वाले अध्याय में’ है; "
                   "कौन-सा अध्याय, यह श्लोक सीधे नहीं बताता।"),
    "hook": "क्रम से · अलग-अलग · पूरा | ‘अन्नपान’ अध्याय में फिर | मैं कहूँगा (वक्ष्यामि)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Where does the speaker say the qualities of the milks will be described in full?",
            ("In the chapter that begins with food and drink (अन्नपानादि)",
             "अन्नपानादिके ऽध्याये भूयो वक्ष्यामि: further, in that chapter."),
            [("In the next verse of this chapter", "The verse says भूयः (later, again), pointing to another chapter."),
             ("Nowhere; this is the last mention", "The speaker promises to speak of them again."),
             ("In a chapter on the origin of diseases", "The chapter is described by food and drink (अन्नपान), not diseases.")],
            "The promise points forward to a chapter named by अन्नपानादि.",
            "अन्नपानादिके ऽध्याये = in the chapter (beginning with) food and drink."),
        match(1, "Match each word of the promise to its meaning.",
              [["यथाक्रमम्", "in due order"], ["पृथक् पृथक्", "separately"],
               ["भूयः", "further, again"], ["अशेषतः", "completely"]],
              "These four words say how the promise will be kept.",
              "यथाक्रमम् = in due order; पृथक् पृथक् = separately; भूयः = further, again; अशेषतः = completely."),
        fill(2, "भूयो ____ अशेषतः: type the verb meaning I shall describe (ending in -मि), before sandhi.",
             ["वक्ष्यामि"],
             "The verse has भूयो वक्ष्याम्यशेषतः.",
             "वक्ष्यामि is the first person singular future of √वच्: 'I shall say / describe'.",
             "-स्य- (here -ष्य- after क्) marks the future; -मि marks 'I'.",
             "वक्ष्यामि = I shall describe."),
        mcq("discriminate", 3, "Which is the right split of वक्ष्याम्यशेषतः?",
            ("वक्ष्यामि + अशेषतः", "इ before a different vowel becomes य्, so वक्ष्यामि + अशेषतः is written वक्ष्याम्यशेषतः."),
            [("वक्ष्याम + यशेषतः", "यशेषतः is not a word."),
             ("वक्ष्यामि + शेषतः", "That would drop the अ- of अशेषतः and give a different meaning, 'from the remainder'."),
             ("वक्ष्याम्य + शेषतः", "वक्ष्याम्य is not a verb form.")],
            "वक्ष्याम्यशेषतः = वक्ष्यामि ('I shall describe') + अशेषतः ('completely').",
            "इ + अ → य् + अ: वक्ष्यामि + अशेषतः = वक्ष्याम्यशेषतः."),
        mcq("apply", 4,
            "In verse 1, व्याख्यास्यामः (-मः) meant 'we shall expound'. वक्ष्यामि ends in -मि. Who speaks, and when?",
            ("I, one speaker, about the future", "-मि marks 'I' and the future sense gives 'I shall'."),
            [("We, a group, about the future", "'We' ends in -मः, as in verse 1."),
             ("He, about the past", "'He' would end in -ति and the sense is not past."),
             ("You, about the present", "'You' would end in -सि.")],
            "वक्ष्यामि is first person singular future: 'I shall describe'.",
            "-मि = I; -मः = we."),
        mcq("transfer", 5,
            "A made-up teacher ends a lesson with पृथक् पृथक् भूयो वक्ष्यामि. What is he doing?",
            ("Promising to return to the matter and treat each part separately",
             "भूयः + the future verb is a promise to come back; पृथक् पृथक् means each separately."),
            [("Saying nothing more will be said about it", "भूयः points to more to come."),
             ("Asking his students to explain it separately", "वक्ष्यामि is 'I shall say', not a request."),
             ("Repeating what he said before", "The future verb looks forward, not back.")],
            "The pattern is the same as in verse 113: a short statement now and a fuller one promised later.",
            "भूयः + future verb = a later fuller treatment.",
            teaches="भूयः with a future verb is a promise of a later, fuller treatment of the topic."),
    ],
}

# ------------------------------------------------------------- unit 114
AUTHORED["114"] = {
    "title": "अथापरे त्रयो वृक्षाः",
    "question": "Which three further plants are introduced, and what is promised about them?",
    "rule": ("Three more plants, distinct from the fruit- and root-yielding ones: "
             "स्नुही, अर्क, अश्मन्तक. 'Their action, each separately, is this' "
             "(तेषामिदं कर्म पृथक् पृथक्): the actions come in verse 115."),
    "limits": ("फलमूलिभिः is taken as the fruit- and root-plants listed earlier; "
               "it could also mean 'distinct in fruits and roots'. "
               "What each plant is, is not given here, and अश्मन्तक is of uncertain identity."),
    "explain_hi": ("एक नया वर्ग शुरू होता है: ‘अथ अपरे त्रयो वृक्षाः’, अब तीन और पौधे। "
                   "‘पृथग्ये फलमूलिभिः’ का सामान्य अर्थ है: जो फलिनी और मूलिनी (औषधियों) से भिन्न हैं। "
                   "तीन नाम हैं: स्नुही, अर्क, अश्मन्तक। "
                   "‘तेषामिदं कर्म पृथक् पृथक्’ यानी ‘इनका अपना-अपना कर्म यह है’; वह कर्म अगले श्लोक में आता है। "
                   "इसलिए यह श्लोक भूमिका है, कर्म स्वयं यहाँ नहीं दिए गए।"),
    "hook": "तीन और पौधे: स्नुही · अर्क · अश्मन्तक | हर एक का अलग कर्म (अगले श्लोक में)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Verse 114 introduces a new group of plants. Which three does it name?",
            ("स्नुही, अर्क, अश्मन्तक", "These are the names in स्नुह्यर्काश्मन्तकाः."),
            [("पूतीक, कृष्णगन्धा, तिल्वक", "These come later, in verse 116."),
             ("स्नुही, अर्क, तिल्वक", "तिल्वक is not in this verse."),
             ("अश्मन्तक, पूतीक, कृष्णगन्धा", "Only one of these three is named here.")],
            "The verse names exactly three plants: snuhī, arka, aśmantaka.",
            "114: स्नुही, अर्क, अश्मन्तक."),
        match(1, "Match each word of the verse to its meaning.",
              [["अथ", "now"], ["अपरे", "other"], ["त्रयः", "three"], ["पृथक्", "separately"]],
              "These words carry the introduction of the new group.",
              "अथ = now; अपरे = other; त्रयः = three; पृथक् = separately."),
        fill(2, "Complete the three names: स्नुही, अर्क, ____ (type the third in Devanagari).",
             ["अश्मन्तक", "अश्मन्तकाः", "अश्मन्तकः"],
             "The compound is स्नुह्यर्काश्मन्तकाः.",
             "The compound ends in -आः, the nominative plural: 'snuhī, arka and aśmantaka'.",
             "A compound of names in a list ends with the plural ending that covers all of them.",
             "The three names are स्नुही, अर्क, अश्मन्तक."),
        mcq("discriminate", 3, "Which is the right split of स्नुह्यर्काश्मन्तकाः?",
            ("स्नुही + अर्क + अश्मन्तकाः", "ई before a different vowel becomes य्, and अ + अ gives आ: three names."),
            [("स्नुह्य + अर्का + श्मन्तकाः", "These pieces are not names."),
             ("स्नुहि + यर्क + अश्मन्तकाः", "यर्क is not a name; the name is अर्क."),
             ("स्नुही + अर्का + अश्मन्तकाः", "अर्का is not the name; the name is अर्क and आ comes from joining it with अश्मन्तक.")],
            "स्नुह्यर्काश्मन्तकाः = स्नुही + अर्क + अश्मन्तकाः.",
            "ई + अ → य्, अ + अ → आ: स्नुही + अर्क + अश्मन्तक."),
        multi("apply", 4, "Which statements does verse 114 support?",
              [("Three other plants are being introduced", "Right: अथापरे त्रयो वृक्षाः."),
               ("Each plant has its own action to be told", "Right: तेषामिदं कर्म पृथक् पृथक्."),
               ("All three have exactly the same action", "पृथक् पृथक् says the opposite: each separately."),
               ("The actions are already listed in this verse", "इदं कर्म points ahead; the actions come in verse 115.")],
              [0, 1],
              "The verse introduces three plants and promises their separate actions; it does not state them.",
              "114 = introduction; 115 = the actions."),
        mcq("transfer", 5,
            "A made-up line reads अथापरे द्वौ क्षारौ, तेषामिदं कर्म पृथक् पृथक्. What do you expect next?",
            ("A separate action for each of the two",
             "As in verse 114, पृथक् पृथक् promises each item its own action."),
            [("One action shared by both", "पृथक् पृथक् means separately."),
             ("A list of diseases", "The line promises their action, not a list of diseases."),
             ("Nothing more about them", "इदं कर्म promises that the action follows.")],
            "The same frame as 114: 'now other [number] ...; their action, each separately, is this'.",
            "अथापरे [number] ... तेषामिदं कर्म पृथक् पृथक् = items now, separate actions next.",
            teaches="This opening frame tells you the next verse will give each new item its own action."),
    ],
}

# ------------------------------------------------------------- unit 115
AUTHORED["115"] = {
    "title": "वमने ऽश्मन्तकं विद्यात्",
    "question": "For which therapy is each of the three plants known?",
    "rule": ("अश्मन्तक: emesis (वमने). The latex of स्नुही: purgation (विरेचने). "
             "The latex of अर्क: emesis together with purgation (वमने सविरेचने)."),
    "limits": ("क्षीर here is taken as the milky latex of the plant. For अश्मन्तक the "
               "verse names no part (no क्षीर). Whether सविरेचने means 'both' or "
               "'emesis with some purgation' is read in the first way here."),
    "explain_hi": ("यह तीनों पौधों का कर्म बताने वाला मुख्य श्लोक है। अश्मन्तक वमन में, "
                   "स्नुही का क्षीर (दूध-सा रस) विरेचन में, और अर्क का क्षीर वमन और विरेचन दोनों में। "
                   "‘सविरेचने’ = स (साथ) + विरेचने, यानी ‘विरेचन के साथ’। "
                   "‘विद्यात्’ का अर्थ ‘जानना चाहिए’ और ‘विज्ञेयम्’ का अर्थ ‘जानने योग्य’ है; दोनों एक ही बात कहते हैं। "
                   "तीन पौधे, तीन अलग-अलग कर्म: यही श्लोक ११४ का वादा पूरा करता है।"),
    "hook": "अश्मन्तक → वमन | स्नुही-क्षीर → विरेचन | अर्क-क्षीर → वमन + विरेचन।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which is named for emesis only, with purgation not mentioned for it?",
            ("अश्मन्तक", "वमने ऽश्मन्तकं विद्यात्: aśmantaka is known for emesis."),
            [("The latex of स्नुही", "Snuhī's latex is for purgation."),
             ("The latex of अर्क", "Arka's latex is for emesis together with purgation."),
             ("None of them", "The verse gives a use for each of the three.")],
            "Only aśmantaka is named for emesis without purgation; the other two involve purgation.",
            "अश्मन्तक = emesis; स्नुही = purgation; अर्क = both."),
        order(1, "Put the three plants in the order in which verse 115 names them.",
              ["अश्मन्तक", "स्नुही", "अर्क"],
              "The verse names aśmantaka first, then snuhī, then arka.",
              "Verse order: अश्मन्तक, स्नुही, अर्क."),
        fill(2, "Complete: क्षीरमर्कस्य विज्ञेयं वमने ____ . Type the word for 'together with purgation'.",
             ["सविरेचने"],
             "The verse ends वमने सविरेचने.",
             "सविरेचने = स ('with') + विरेचने ('in purgation'): emesis together with purgation.",
             "स- at the start of a word can mean 'with, together with'.",
             "सविरेचने = together with purgation."),
        mcq("discriminate", 3,
            "In वमने सविरेचने, what does सविरेचने add to वमने?",
            ("'Together with purgation': both therapies", "स- means 'with', so emesis comes together with purgation."),
            [("'Instead of purgation': emesis only", "स- means 'with', not 'instead of'."),
             ("'Without purgation'", "'Without' would need a word like अविरेचने or विना, not स-."),
             ("'After purgation': a later step", "स- means 'together with', not 'after'.")],
            "Arka's latex is the one with the double use.",
            "स + विरेचने = together with purgation."),
        multi("apply", 4, "Which statements about verse 115 are right?",
              [("अश्मन्तक is for emesis", "Right: वमने ऽश्मन्तकं विद्यात्."),
               ("The latex of स्नुही is for purgation", "Right: स्नुहीक्षीरं विरेचने."),
               ("The latex of अर्क is for emesis together with purgation", "Right: क्षीरमर्कस्य ... वमने सविरेचने."),
               ("The latex of स्नुही is for emesis", "The verse puts snuhī under purgation."),
               ("The latex of अर्क is for purgation only", "Arka is for emesis together with purgation, not purgation alone.")],
              [0, 1, 2],
              "The three plants have three different uses: emesis, purgation, and the two together.",
              "अश्मन्तक: वमन; स्नुही: विरेचन; अर्क: वमन + विरेचन."),
        mcq("transfer", 5,
            "A made-up verse reads विरेचने कल्पकं विद्यात्. By the pattern of 115, what does it say about the plant कल्पक?",
            ("It is to be known as used for purgation",
             "'विरेचने X विद्यात्' reads 'know X for purgation', as with snuhī in 115."),
            [("It is to be known as used for emesis", "Emesis would be वमने."),
             ("It is used for both therapies", "Both would need a wording like सविरेचने."),
             ("It is to be avoided", "विद्यात् ('one should know') names a use; it does not forbid.")],
            "The pattern is: therapy in the locative, plant, and 'one should know'.",
            "वमने X विद्यात् = X for emesis; विरेचने X विद्यात् = X for purgation.",
            teaches="You can read a new plant's use from the therapy word in the locative: वमने = emesis, विरेचने = purgation."),
    ],
}

# ------------------------------------------------------------- unit 116
AUTHORED["116"] = {
    "title": "इमांस्त्रीनपरान् वृक्षान्",
    "question": "Which three other trees are named, and what part of them is beneficial?",
    "rule": ("Three more trees whose barks (त्वचः) are beneficial: पूतीक, "
             "कृष्णगन्धा and तिल्वक. They are the 'other' (अपरान्) three, after the "
             "three of verses 114-115."),
    "limits": ("आहुः ('they say') leaves the speaker unnamed. The verse gives "
               "no use for each tree; that begins in verse 117. Identifications of "
               "the plants come from commentaries, not from this text."),
    "explain_hi": ("तीन और वृक्षों की सूची, जिनकी छाल (त्वक्) हितकर है: पूतीक, कृष्णगन्धा और तिल्वक। "
                   "‘अपरान्’ (अन्य) बताता है कि ये पिछले तीन (स्नुही, अर्क, अश्मन्तक) से अलग हैं। "
                   "‘आहुः’ = ‘कहते हैं’, यानी कर्ता अनाम। "
                   "‘येषां हिताः त्वचः’ का अर्थ है ‘जिनकी छालें हितकर हैं’। "
                   "इस श्लोक में उपयोग नहीं दिए गए; वे श्लोक ११७ में हैं।"),
    "hook": "छाल वाले तीन: पूतीक · कृष्णगन्धा · तिल्वक | पहले के तीन वमन/विरेचन वाले।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What do the three trees of verse 116 have in common?",
            ("Their barks are beneficial", "येषां हिताः त्वचः: 'whose barks are beneficial'."),
            [("Their roots are beneficial", "The verse names the bark (त्वचः), not the roots."),
             ("Their fruits are beneficial", "The verse names the bark, not the fruits."),
             ("Their latex is beneficial", "Latex was the part for snuhī and arka in verse 115, not here.")],
            "त्वचः = barks.",
            "116 trees: bark (त्वच्)."),
        match(1, "Match each word of the verse to its meaning.",
              [["अपरान्", "others"], ["हिताः", "beneficial"],
               ["त्वचः", "barks"], ["आहुः", "they say"]],
              "These words carry the sense of the verse.",
              "अपरान् = others; हिताः = beneficial; त्वचः = barks; आहुः = they say."),
        fill(2, "Complete the three names: पूतीक, कृष्णगन्धा, ____ (type the third in Devanagari).",
             ["तिल्वक", "तिल्वकः"],
             "The verse ends तिल्वकश्च तथा तरुः.",
             "The third name is तिल्वक; तथा तरुः adds 'likewise the tree'.",
             "In a list, तथा ('likewise') introduces the last member.",
             "The three bark trees are पूतीक, कृष्णगन्धा, तिल्वक."),
        mcq("discriminate", 3, "Which is the right split of वृक्षानाहुर्येषाम्?",
            ("वृक्षान् + आहुः + येषाम्", "Final न् joins आहुः; the visarga after उ becomes र् before the voiced य."),
            [("वृक्षा + नाहुः + येषाम्", "नाहुः is not a word."),
             ("वृक्षान् + आहु + र्येषाम्", "र्येषाम् is not a word; the र् comes from the visarga of आहुः."),
             ("वृक्षान् + आहुः + र्येषाम्", "The र् belongs to आहुः; the word is येषाम्.")],
            "वृक्षानाहुर्येषाम् = वृक्षान् + आहुः + येषाम् ('the trees; they speak; of which').",
            "उः + voiced letter → उर्: आहुः + येषाम् = आहुर्येषाम्."),
        multi("apply", 4, "Which statements fit verse 116?",
              [("It names Pūtīka, Kṛṣṇagandhā and Tilvaka", "Right: पूतीकः कृष्णगन्धा च तिल्वकश्च."),
               ("The barks of these trees are said to be beneficial", "Right: येषां हिताः त्वचः."),
               ("It says Tilvaka is used for purgation", "That is verse 117, not this verse."),
               ("It says Kṛṣṇagandhā is śigru", "The text gives no such identification; that comes from commentators.")],
              [0, 1],
              "Verse 116 gives the names and the useful part (bark); the uses come in 117.",
              "116 = names + bark; 117 = uses."),
        mcq("transfer", 5,
            "A made-up line reads इमांस्त्रीन् वृक्षानाहुर्येषां हितानि फलानि. What does it tell you about the trees?",
            ("Their fruits are the beneficial part",
             "'येषां हिताः X' names the useful part: here fruits, in verse 116 barks."),
            [("Their barks are the beneficial part", "The made-up line says फलानि, fruits."),
             ("They are harmful trees", "हितानि means beneficial."),
             ("Their roots are the beneficial part", "Only one part, fruits, is named.")],
            "The pattern येषां हिताः + part names what is useful.",
            "येषां हिताः X = whose X are beneficial.",
            teaches="The phrase 'येषां हिताः ...' names the useful part of a plant group, so you can read it for any new plant."),
    ],
}

# ------------------------------------------------------------- unit 117
AUTHORED["117"] = {
    "title": "विरेचने प्रयोक्तव्यः",
    "question": "Which bark-trees are for purgation, and for what is Kṛṣṇagandhā prescribed?",
    "rule": ("Pūtīka and Tilvaka are to be used in purgation (विरेचने); Kṛṣṇagandhā is "
             "prescribed for parīsarpa, swellings and piles (परीसर्प, शोथ, अर्श)."),
    "limits": ("The list for Kṛṣṇagandhā goes on into verse 118. The verse names no other "
               "use for Pūtīka or Tilvaka. प्रयोक्तव्यः is singular though it serves two "
               "subjects; it can agree with the nearer one or with each."),
    "explain_hi": ("छाल वाले तीन वृक्षों के उपयोग यहाँ शुरू होते हैं। पूतीक और तिल्वक विरेचन में प्रयोग किए जाने चाहिए "
                   "(‘प्रयोक्तव्यः’ = प्रयोग करने योग्य)। कृष्णगन्धा के लिए परीसर्प, शोथ और अर्श बताए गए हैं "
                   "(‘उच्यते’ = कहा जाता है)। कृष्णगन्धा की सूची अगले श्लोक में जारी रहती है। "
                   "‘प्रयोक्तव्यः’ एकवचन है पर उसके दो कर्ता हैं; वह पास वाले ‘तिल्वकः’ से भी जुड़ सकता है।"),
    "hook": "पूतीक · तिल्वक → विरेचन | कृष्णगन्धा → परीसर्प · शोथ · अर्श (और आगे)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which two trees does verse 117 name for use in purgation?",
            ("पूतीक and तिल्वक", "विरेचने प्रयोक्तव्यः पूतीकस्तिल्वकस्तथा."),
            [("कृष्णगन्धा and तिल्वक", "Kṛṣṇagandhā is named for parīsarpa, swellings and piles."),
             ("पूतीक and कृष्णगन्धा", "Kṛṣṇagandhā is named for other conditions in this verse."),
             ("स्नुही and अर्क", "These were in verses 114-115, not in this verse.")],
            "Purgation goes with the first two names, Pūtīka and Tilvaka.",
            "117: पूतीक, तिल्वक = purgation."),
        match(1, "Match each word to its meaning.",
              [["विरेचने", "in purgation"], ["शोथेषु", "in swellings"],
               ["अर्शःषु (पाठ में)", "in piles"], ["उच्यते", "is said, is prescribed"]],
              "These words carry the uses named in the verse.",
              "विरेचने = in purgation; शोथेषु = in swellings; अर्शःसु = in piles; उच्यते = is said."),
        fill(2, "Complete: कृष्णगन्धा ____ शोथेष्वर्शःषु चोच्यते. Type the first condition, the one in -ए.",
             ["परीसर्पे", "परिसर्पे"],
             "The verse reads कृष्णगन्धा परीसर्पे शोथेष्वर्शःषु चोच्यते.",
             "परीसर्पे is the locative singular: 'in parīsarpa', a spreading skin disease.",
             "Each use of a tree is a locative: 'in this condition'.",
             "परीसर्पे = in parīsarpa (spreading skin disease)."),
        mcq("discriminate", 3, "Which is the right split of चोच्यते?",
            ("च + उच्यते", "अ + उ becomes ओ, so च + उच्यते is written चोच्यते."),
            [("चो + च्यते", "च्यते is not a verb form here; the verb is उच्यते."),
             ("चा + उच्यते", "The word is च, with short अ."),
             ("च + ओच्यते", "There is no verb ओच्यते.")],
            "चोच्यते = च ('and') + उच्यते ('is said').",
            "अ + उ → ओ: च + उच्यते = चोच्यते."),
        multi("apply", 4, "Which of these does verse 117 itself say?",
              [("Pūtīka is to be used in purgation", "Right: विरेचने प्रयोक्तव्यः पूतीकः."),
               ("Tilvaka is to be used in purgation", "Right: तिल्वकस्तथा."),
               ("Kṛṣṇagandhā is prescribed for parīsarpa", "Right: कृष्णगन्धा परीसर्पे ... उच्यते."),
               ("Tilvaka is for emesis", "The verse puts Tilvaka under purgation."),
               ("Pūtīka is for swellings and piles", "Swellings and piles are listed under Kṛṣṇagandhā.")],
              [0, 1, 2],
              "Purgation goes with Pūtīka and Tilvaka; parīsarpa, swellings and piles with Kṛṣṇagandhā.",
              "117: पूतीक + तिल्वक = विरेचन; कृष्णगन्धा = परीसर्प, शोथ, अर्श."),
        mcq("transfer", 5,
            "A made-up line says क्वाथः पातव्यः, with पातव्यः built like प्रयोक्तव्यः. What does it say of the decoction?",
            ("It is to be drunk", "The -तव्य ending, as in प्रयोक्तव्यः, means 'is to be done'."),
            [("It was drunk", "-तव्य is not a past ending."),
             ("It must not be drunk", "A negative word would be needed."),
             ("It is being drunk now by someone", "-तव्य says 'is to be', not an action in progress.")],
            "The ending -तव्य gives the 'is to be done' sense.",
            "-तव्य = is to be (done).",
            teaches="With the ending -तव्य you can read a new word as 'is to be ...', for example पातव्यः 'is to be drunk'."),
    ],
}

# ------------------------------------------------------------- unit 118
AUTHORED["118"] = {
    "title": "दद्रुविद्रधिगण्डेषु",
    "question": "What else is Kṛṣṇagandhā used for, and what does the verse call the six trees?",
    "rule": ("In ringworm, abscess, gaṇḍa, skin diseases and pustular eruptions "
             "(continuing Kṛṣṇagandhā's uses); and the discerning physician should know "
             "these six trees as purifying (शोधन)."),
    "limits": ("The first half names no subject; it continues Kṛṣṇagandhā from verse 117. "
               "ṣaḍvṛkṣān may be one compound or two words, with the same sense. "
               "गण्ड may mean goitre, glandular swelling or boil."),
    "explain_hi": ("पहली पंक्ति में कर्ता नहीं है; वह श्लोक ११७ के कृष्णगन्धा की सूची को आगे बढ़ाती है: दद्रु, विद्रधि, गण्ड, कुष्ठ और अलजी में। "
                   "दूसरी पंक्ति सार देती है: विचक्षण वैद्य इन छह वृक्षों को ‘शोधन’ (शुद्ध करने वाला, दोषों को बाहर निकालने वाला) जाने। "
                   "छह = श्लोक ११४ के तीन (स्नुही, अर्क, अश्मन्तक) + श्लोक ११६ के तीन (पूतीक, कृष्णगन्धा, तिल्वक)। "
                   "‘षड्वृक्षाञ्छोधनान्’ में न् + श → ञ्छ का संधि-नियम है।"),
    "hook": "कृष्णगन्धा के और रोग: दद्रु · विद्रधि · गण्ड · कुष्ठ · अलजी | छहों वृक्ष = शोधन।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "How does verse 118 describe the six trees at its close?",
            ("As purifying, evacuant (शोधन)", "षड्वृक्षाञ्छोधनान्: the six trees are शोधन."),
            [("As bulk-building (बृंहण)", "बृंहण was a quality of milk in verse 107, not the label of the trees."),
             ("As stimulating digestion (दीपनीय)", "दीपनीय was a quality of milk in verse 109."),
             ("As aphrodisiac (वृष्य)", "वृष्य was a quality of milk in verse 107.")],
            "The six trees are called शोधन, purifying or evacuant.",
            "षड् वृक्षाः = शोधन."),
        match(1, "Match each condition to its meaning.",
              [["दद्रु", "ringworm"], ["विद्रधि", "abscess"],
               ["कुष्ठ", "skin diseases"], ["अलजी", "pustular eruptions"]],
              "These are four of the conditions in the first line.",
              "दद्रु = ringworm; विद्रधि = abscess; कुष्ठ = skin diseases; अलजी = pustular eruptions."),
        fill(2, "विद्याद् ____: type the word that names the physician who should know, as the verse puts it.",
             ["विचक्षणः", "विचक्षण"],
             "The verse ends विद्याद्विचक्षणः.",
             "विचक्षणः is a nominative singular: the one who should know.",
             "विद्यात् ('should know') takes its subject in the nominative: विचक्षणः.",
             "विचक्षणः = the discerning (physician)."),
        mcq("discriminate", 3, "Which is the right split of षड्वृक्षाञ्छोधनान्?",
            ("षड्वृक्षान् + शोधनान्", "न् + श् becomes ञ्छ्, so षड्वृक्षान् + शोधनान् is written षड्वृक्षाञ्छोधनान्."),
            [("षड्वृक्षाञ् + छोधनान्", "छोधन is not a word; the छ् comes from the sandhi."),
             ("षड्वृक्षा + ञ्छोधनान्", "ञ्छोधन is not a word."),
             ("षट् + वृक्षाञ्छोधनान्", "वृक्षाञ्छोधनान् is not a word.")],
            "षड्वृक्षाञ्छोधनान् = षड्वृक्षान् ('six trees') + शोधनान् ('purifying').",
            "न् + श → ञ् + छ: वृक्षान् + शोधनान् = वृक्षाञ्छोधनान्."),
        multi("apply", 4, "Which conditions are listed in verse 118?",
              [("दद्रु (ringworm)", "Right: दद्रुविद्रधिगण्डेषु."),
               ("कुष्ठ (skin diseases)", "Right: कुष्ठेष्वपि."),
               ("अलजी (pustular eruptions)", "Right: अलजीषु च."),
               ("परीसर्प (spreading skin disease)", "Parīsarpa is in verse 117."),
               ("अर्श (piles)", "Piles are in verse 117.")],
              [0, 1, 2],
              "Verse 118 continues the list from 117; parīsarpa, swellings and piles were the first part of it.",
              "117: परीसर्प, शोथ, अर्श; 118: दद्रु, विद्रधि, गण्ड, कुष्ठ, अलजी."),
        mcq("transfer", 5,
            "A made-up verse follows one listing a tree's uses and opens दाहे तृष्णायां च, naming no tree. Where is the tree most likely named?",
            ("Look back at the previous verse for the subject, as 118 does with 117",
             "A verse made only of locatives continues a list begun before it."),
            [("Treat the verse as complete and meaningless", "The subject is understood from the verse before."),
             ("Take the subject from the verse after it", "Verse 118 takes it from the verse before, 117."),
             ("Take 'milk' as the subject by default", "The subject comes from the immediately preceding list, not from a default.")],
            "The same situation as the first line of 118, which names no tree.",
            "Locatives with no subject continue the list before them.",
            teaches="A verse of only 'in ...' words with no subject may continue the list before it."),
    ],
}

# ------------------------------------------------------------- unit 119
AUTHORED["119"] = {
    "title": "इत्युक्ताः फलमूलिन्यः",
    "question": "What does verse 119 do, and which groups does it recall?",
    "rule": ("A summary: 'thus have been stated' the fruit- and root-plants, fats, "
             "salts, urine, milks, and the six trees whose milk and bark are indicated."),
    "limits": ("दिष्टपयस्त्वचः is read as a compound meaning 'whose milk and bark are "
               "indicated'. The verse only recalls what was described; it adds no "
               "new use or property."),
    "explain_hi": ("यह सार-श्लोक है: ‘इति उक्ताः’ = ‘इस प्रकार कहे गए’। जो कुछ पहले कहा गया उसकी सूची: फलिनी–मूलिनी, स्नेह (घी–तेल आदि), "
                   "लवण, मूत्र, क्षीर (दूध) और छह वृक्ष। "
                   "‘ये दिष्टपयस्त्वचः’ का अर्थ है ‘जिनके पय (क्षीर) और त्वचा (छाल) बताए गए हैं’; इनमें तीन के क्षीर और तीन की छाल आते हैं। "
                   "‘इत्युक्ताः’ में इति + उक्ताः का इ + उ → यु संधि है।"),
    "hook": "इति उक्ताः: फलिनी–मूलिनी · स्नेह · लवण · मूत्र · क्षीर · छह वृक्ष।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What kind of verse is verse 119?",
            ("A summary of the groups already described", "इत्युक्ताः = 'thus have been stated', followed by the list."),
            [("The start of a new topic", "इत्युक्ताः looks back; it does not open a new topic."),
             ("A list of diseases and their cures", "The list is of drug groups, not diseases."),
             ("A prayer to end the chapter", "The verse is a list of groups already described.")],
            "इति + उक्ताः closes a section by recalling what has been said.",
            "इत्युक्ताः = thus stated: a recap."),
        order(1, "Put these four groups in the order in which verse 119 names them.",
              ["स्नेहाः", "लवणानि", "मूत्रम्", "क्षीराणि"],
              "The verse names fats, then salts, then urine, then milks.",
              "Verse order: स्नेह, लवण, मूत्र, क्षीर."),
        fill(2, "स्नेहाश्च ____ च: type the word for salts as it stands in the verse.",
             ["लवणानि", "लवण"],
             "The verse reads स्नेहाश्च लवणानि च.",
             "लवणानि is the neuter nominative plural of लवण: 'salts'.",
             "Neuter a-stem nouns make the plural in -आनि: लवण → लवणानि = salts.",
             "लवणानि = salts."),
        mcq("discriminate", 3, "What does ये दिष्टपयस्त्वचः say about the six trees?",
            ("Their milk and bark have been indicated", "दिष्ट-पयस्-त्वचः: whose milk and bark are indicated."),
            [("Their roots and fruits have been indicated", "Roots and fruits belong to the other group, the phalinī and mūlinī plants."),
             ("Their milk and bark are forbidden", "दिष्ट means indicated, not forbidden."),
             ("Their leaves and flowers have been indicated", "The compound names milk and bark.")],
            "Three of the six trees give milk (latex), three give bark.",
            "दिष्टपयस्त्वचः = whose milk and bark are indicated."),
        multi("apply", 4, "Which items does verse 119 name in its summary?",
              [("Fats (स्नेह)", "Right: स्नेहाश्च."),
               ("Salts (लवण)", "Right: लवणानि."),
               ("Urine (मूत्र)", "Right: मूत्रम्."),
               ("Honey (मधु)", "Honey is not named in this verse."),
               ("Blood (रक्त)", "Blood is not named in this verse.")],
              [0, 1, 2],
              "The verse recalls fats, salts and urine among its groups; honey and blood are not in it.",
              "119 names fruit- and root-plants, fats, salts, urine, milks and six trees."),
        mcq("transfer", 5,
            "A made-up author closes a section with इत्युक्तानि धान्यानि शिम्बयः फलानि च. What is the author doing?",
            ("Recalling the groups already described: grains, pulses and fruits",
             "इत्युक्ताः ('thus stated') is the recap marker, as in verse 119."),
            [("Beginning a new list of groups", "इत्युक्ताः looks back, not forward."),
             ("Forbidding those groups", "उक्ताः means 'stated', not forbidden."),
             ("Asking a question about them", "The line is a statement.")],
            "The same device as verse 119: इति + उक्ताः, then the list.",
            "इत्युक्ताः + list = a summary of what has been said.",
            teaches="इत्युक्त- often marks a closing recap, so it can help you spot the end of a section."),
    ],
}

NOTES_HI = {
    "110": "संधि: तथा + उदरे → तथोदरे (आ + उ → ओ); पाण्डुरोगे + अम्लपित्ते → पाण्डुरोगे ऽम्लपित्ते (ए के बाद अ का लोप, ऽ से दिखाया)। ‘श्वयथौ’ में -औ सप्तमी एकवचन है, द्विवचन नहीं। ‘पथ्यम्’ श्लोक १११ में है, इसलिए यह श्लोक वाक्य का पहला अर्धांश है। पाठभेद या पाठ-सन्देह डेटा में नहीं हैं।",
    "111": "संधि: मूत्रेषु + अप्रचुरेषु → मूत्रेष्वप्रचुरेषु (उ + अ → व् + अ)। ‘योनिशुक्रप्रदोषेषु’ को ‘योनि और शुक्र के दोषों में’ या ‘योनि-शुक्र (एक साथ) के दोषों में’ दोनों तरह पढ़ा जा सकता है; यह कार्ड पहला अर्थ मानता है। ‘मूत्रेष्वप्रचुरेषु’ और ‘पुरीषे ग्रथिते’ ‘जब ... हो’ वाले सप्तमी प्रयोग हैं। पाठभेद डेटा में नहीं हैं।",
    "112": "संधि: नस्य + आलेप + अवगाहेषु → नस्यालेपावगाहेषु (अ + आ → आ, अ + अ → आ); वमन + आस्थापनेषु → वमनास्थापनेषु (अ + आ → आ)। ‘सर्वत्र’ का दायरा इसी श्लोक की सात विधियाँ हैं। डेटा में कोई पाठभेद या पाठ-सन्देह नहीं है।",
    "113": "संधि: अन्नपानादिके + अध्याये → अन्नपानादिके ऽध्याये (ए + अ → ए ऽ); वक्ष्यामि + अशेषतः → वक्ष्याम्यशेषतः (इ + अ → य् + अ); एक + एकस्य → एकैकस्य (अ + ए → ऐ)। ‘अन्नपानादिके अध्याये’ कौन-सा अध्याय है, यह पाठ में नहीं लिखा; डेटा की टिप्पणी में बाहर से जोड़ी गई पहचान है। पाठभेद डेटा में नहीं हैं।",
    "114": "विश्वास: मध्यम। ‘फलमूलिभिः’ को पहले बताई फलिनी–मूलिनी औषधियाँ माना गया है; ‘फल और मूल के बारे में अलग’ भी पढ़ा जा सकता है। अश्मन्तक की पहचान अनिश्चित है। संधि: अथ + अपरे → अथापरे; पृथक् + ये → पृथग्ये (क् → ग् घोष ‘य’ से पहले); स्नुही + अर्क + अश्मन्तकाः → स्नुह्यर्काश्मन्तकाः; तेषाम् + इदम् → तेषामिदम्।",
    "115": "‘क्षीर’ यहाँ पौधे का दूध जैसा रस माना गया है। अश्मन्तक के साथ कोई अंग नहीं बताया गया। ‘सविरेचने’ को ‘विरेचन के साथ’ पढ़ा गया है (वमन + विरेचन दोनों)। संधि: वमने + अश्मन्तकम् → वमने ऽश्मन्तकम्; क्षीरम् + अर्कस्य → क्षीरमर्कस्य। डेटा में कोई पाठभेद नहीं है।",
    "116": "‘तथा तरुः’ का शाब्दिक अर्थ ‘उसी प्रकार वृक्ष’ है, यानी तिल्वक भी वृक्ष है। संधि: वृक्षान् + आहुः + येषाम् → वृक्षानाहुर्येषाम् (उः + घोष → उर्); तिल्वकः + च → तिल्वकश्च। ‘अपरान्’ यहाँ पिछले तीन वृक्षों से इन तीनों को अलग करता है। पौधों की पहचान टीकाओं की बात है, पाठ की नहीं। पाठभेद डेटा में नहीं हैं।",
    "117": "पाठ-सन्देह: ‘शोथेष्वर्शःषु’ में ‘र्शःषु’ का ष् सम्भवतः लिपि-सम्बन्धी भूल है; सप्तमी बहुवचन ‘अर्शःसु’ (या ‘अर्शस्सु’) अपेक्षित है, क्योंकि विसर्ग के बाद स् ष् नहीं होता। डेटा इसे संभावित लिपि-भूल बताता है; देवनागरी पाठ में भी ष है। ‘प्रयोक्तव्यः’ एकवचन है पर दो कर्ता हैं (पूतीकः, तिल्वकः)। संधि: च + उच्यते → चोच्यते (अ + उ → ओ)।",
    "118": "‘षड्वृक्षान्’ को एक समास (द्विगु) या दो शब्द (षट् वृक्षान्) दोनों पढ़ सकते हैं; अर्थ वही रहता है। संधि: वृक्षान् + शोधनान् → वृक्षाञ्छोधनान् (न् + श → ञ् + छ); विद्यात् + विचक्षणः → विद्याद्विचक्षणः (त् → द् घोष ‘व’ से पहले)। ‘गण्ड’ का अर्थ गलगण्ड या फोड़ा हो सकता है। पहली पंक्ति में कर्ता नहीं है; वह श्लोक ११७ से चलती है।",
    "119": "विश्वास: मध्यम। ‘दिष्टपयस्त्वचः’ को बहुव्रीहि ‘जिनके पय (क्षीर) और त्वचा बताए गए हैं’ माना गया है; छन्द में यह पाठ ठीक बैठता है। ‘फलमूलिन्यः’ = फलिन्यः + मूलिन्यः। संधि: इति + उक्ताः → इत्युक्ताः (इ + उ → यु); षट् + ये → षड् ये (ट् → ड् घोष ‘य’ से पहले)। डेटा में कोई पाठभेद नहीं है।",
}

AIDS = {
    "110": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["पाण्डुरोगे", "ऽम्लपित्ते", "शोषे", "गुल्मे", "उदरे"]},
            {"label": "दूसरी पंक्ति",
             "items": ["अतीसारे", "ज्वरे", "दाहे", "श्वयथौ (विशेषतः)"]}]},
        "letters": "पहली पंक्ति: पा-अ-शो-गु-उ · दूसरी: अ-ज्व-दा-श्व (रोगों के पहले अक्षर)।",
        "sandhi": "आ + उ → ओ: तथा + उदरे → तथोदरे · ए + अ → ए ऽ (अ छिपा): पाण्डुरोगे + अम्लपित्ते → पाण्डुरोगे ऽम्लपित्ते।",
        "contrast": "श्वयथौ (‘सूजन में’, सप्तमी एकवचन) ≠ मार्कण्डेयाश्वलायनौ (श्लोक ९, द्विवचन): दोनों -औ पर, अर्थ अलग।",
        "chunks": "पाण्डुरोगे | ऽम्लपित्ते च | शोषे | गुल्मे | तथोदरे ‖ अतीसारे | ज्वरे | दाहे | श्वयथौ च | विशेषतः।",
    },
    "111": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["योनिशुक्रप्रदोषेषु", "मूत्रेषु अप्रचुरेषु"]},
            {"label": "दूसरी पंक्ति",
             "items": ["पुरीषे ग्रथिते", "पथ्यम्", "वातपित्तविकारिणाम्"]}]},
        "sandhi": "उ + अ → व् + अ: मूत्रेषु + अप्रचुरेषु → मूत्रेष्वप्रचुरेषु।",
        "anchors": "अप्रचुर = अ (नहीं) + प्रचुर (बहुत) · विकारिणाम् ← विकार (बिगाड़) · पथ्य ← पथ (मार्ग): ‘सही मार्ग का’, हितकर।",
        "chunks": "योनिशुक्रप्रदोषेषु | मूत्रेष्वप्रचुरेषु च ‖ पुरीषे ग्रथिते | पथ्यं | वातपित्तविकारिणाम्।",
    },
    "112": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["नस्य", "आलेप", "अवगाह", "वमन", "आस्थापन"]},
            {"label": "दूसरी पंक्ति",
             "items": ["विरेचन", "स्नेहन", "पयः सर्वत्र युज्यते"]}]},
        "letters": "न-आ-अ-व-आ | वि-स्ने (विधियों के पहले अक्षर), फिर: पयः सर्वत्र।",
        "sandhi": "अ + आ → आ, अ + अ → आ: नस्य + आलेप + अवगाह → नस्यालेपावगाह · वमन + आस्थापनेषु → वमनास्थापनेषु।",
        "anchors": "सर्वत्र ← सर्व + त्र (‘सब जगह’) · स्नेहन ← स्नेह (चिकनाहट) · युज्यते ← √युज् (जोड़ना, प्रयोग): योग, उपयोग।",
        "contrast": "विशेषतः (श्लोक ११०) = एक पर जोर; सर्वत्र (श्लोक ११२) = सब पर एक-सा।",
    },
    "113": {
        "frame": "कौन: वक्ता (‘मैं’) · क्या: दूधों के गुण, क्रम से, अलग-अलग, पूरे · कहाँ: आगे, अन्नपान आदि वाले अध्याय में।",
        "sandhi": "ए + अ → ए ऽ: अन्नपानादिके + अध्याये → अन्नपानादिके ऽध्याये · इ + अ → य्: वक्ष्यामि + अशेषतः → वक्ष्याम्यशेषतः · अ + ए → ऐ: एक + एकस्य → एकैकस्य।",
        "anchors": "यथाक्रमम् ← यथा + क्रम (क्रम के अनुसार) · अशेषतः ← अ + शेष (बचा हुआ नहीं) + -तः · वक्ष्यामि ← √वच् (कहना): वचन, वाक्य।",
        "chunks": "यथाक्रमं | क्षीरगुणान् | एकैकस्य पृथक् पृथक् ‖ अन्नपानादिके ऽध्याये | भूयो वक्ष्याम्यशेषतः।",
    },
    "114": {
        "diagram": {"groups": [
            {"label": "नया वर्ग",
             "items": ["अथापरे त्रयो वृक्षाः", "पृथग्ये फलमूलिभिः", "स्नुह्यर्काश्मन्तकाः",
                       "तेषामिदं कर्म पृथक् पृथक्"]}]},
        "letters": "स्नु – अ – अ (स्नुही, अर्क, अश्मन्तक के पहले अक्षर)।",
        "sandhi": "ई + अ → य्: स्नुही + अर्क → स्नुह्यर्क · अ + अ → आ: अर्क + अश्मन्तक → अर्काश्मन्तक · क् → ग् (घोष य से पहले): पृथक् + ये → पृथग्ये · अथ + अपरे → अथापरे।",
        "contrast": "अपरे (‘अन्य’) = ये तीन पहले की फलिनी–मूलिनी सूची से अलग हैं; श्लोक ११६ में फिर ‘अपरान्’ तीन और के लिए आएगा।",
        "chunks": "अथापरे | त्रयो वृक्षाः | पृथग्ये फलमूलिभिः ‖ स्नुह्यर्काश्मन्तकाः | तेषामिदं कर्म | पृथक् पृथक्।",
    },
    "115": {
        "diagram": {"groups": [
            {"label": "वमने",
             "items": ["अश्मन्तकम्"]},
            {"label": "विरेचने",
             "items": ["स्नुहीक्षीरम्"]},
            {"label": "वमने सविरेचने",
             "items": ["क्षीरमर्कस्य"]}]},
        "letters": "अ-स्नु-अ → व-वि-व+वि (पौधे → काम)।",
        "sandhi": "ए + अ → ए ऽ: वमने + अश्मन्तकम् → वमने ऽश्मन्तकम् · क्षीरम् + अर्कस्य → क्षीरमर्कस्य (म् स्वर से जुड़ा)।",
        "contrast": "‘स’ वाला शब्द: सविरेचने = स (साथ) + विरेचने · अश्मन्तक के साथ क्षीर शब्द नहीं है।",
    },
    "116": {
        "diagram": {"groups": [
            {"label": "छाल वाले तीन",
             "items": ["इमान् त्रीन् अपरान् वृक्षान्", "आहुः", "येषां हिताः त्वचः",
                       "पूतीकः", "कृष्णगन्धा", "तिल्वकः तथा तरुः"]}]},
        "letters": "पू – कृ – ति (पूतीक, कृष्णगन्धा, तिल्वक के पहले अक्षर)।",
        "sandhi": "न् + आ: वृक्षान् + आहुः → वृक्षानाहुः · उः + य → उर्य: आहुः + येषाम् → आहुर्येषाम् · विसर्ग + च → श्च: तिल्वकः + च → तिल्वकश्च।",
        "contrast": "श्लोक ११५: क्षीर (स्नुही, अर्क) ↔ श्लोक ११६: त्वक् (पूतीक, कृष्णगन्धा, तिल्वक)। पहले तीन के बाद ‘अपरान्’ (अन्य) तीन।",
        "anchors": "त्वचः ← त्वच् (‘चमड़ी, छाल’): त्वचा · हिताः ← हित (हितकर): हितैषी।",
    },
    "117": {
        "diagram": {"groups": [
            {"label": "विरेचन",
             "items": ["विरेचने प्रयोक्तव्यः", "पूतीकः", "तिल्वकः तथा"]},
            {"label": "कृष्णगन्धा",
             "items": ["परीसर्पे", "शोथेषु", "अर्शःसु (पाठ में अर्शःषु)", "उच्यते"]}]},
        "letters": "पू-ति → विरेचन · कृ → प-शो-अ (परीसर्प, शोथ, अर्श)।",
        "sandhi": "अ + उ → ओ: च + उच्यते → चोच्यते · पूतीकः + तिल्वकः → पूतीकस्तिल्वकः (विसर्ग → स् त से पहले)।",
        "contrast": "प्रयोक्तव्यः (‘प्रयोग करने योग्य’) ≠ उच्यते (‘कहा जाता है’): पहला विधान है, दूसरा कथन।",
        "chunks": "विरेचने प्रयोक्तव्यः | पूतीकस्तिल्वकस्तथा ‖ कृष्णगन्धा | परीसर्पे | शोथेष्वर्शःषु चोच्यते।",
    },
    "118": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["दद्रु", "विद्रधि", "गण्डेषु", "कुष्ठेषु अपि", "अलजीषु च"]},
            {"label": "दूसरी पंक्ति",
             "items": ["षड् वृक्षान्", "शोधनान् एतान् अपि", "विद्यात् विचक्षणः"]}]},
        "letters": "द-वि-ग-कु-अ → छह वृक्ष: शोधन (रोगों के पहले अक्षर)।",
        "sandhi": "न् + श → ञ्छ: वृक्षान् + शोधनान् → वृक्षाञ्छोधनान् · त् → द् (घोष वि से पहले): विद्यात् + विचक्षणः → विद्याद्विचक्षणः।",
        "anchors": "शोधन ← √शुध् (शुद्ध करना): शुद्धि, शोध · विचक्षणः ← वि + √चक्ष् (देखना, भेद करना): ‘परखने वाला’।",
        "contrast": "तीन (श्लोक ११४) + तीन (श्लोक ११६) = छह वृक्ष: पहले तीन वमन/विरेचन वाले (अश्मन्तक में अंग नहीं बताया), फिर तीन छाल वाले।",
        "chunks": "दद्रुविद्रधिगण्डेषु | कुष्ठेष्वप्यलजीषु च ‖ षड्वृक्षाञ्छोधनान् | एतानपि | विद्याद्विचक्षणः।",
    },
    "119": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["इत्युक्ताः", "फलमूलिन्यः", "स्नेहाः", "लवणानि"]},
            {"label": "दूसरी पंक्ति",
             "items": ["मूत्रं", "क्षीराणि", "वृक्षाश्च षड् ये", "दिष्टपयस्त्वचः"]}]},
        "letters": "फ-स्ने-ल-मू-क्षी-वृ (छह समूहों के पहले अक्षर)।",
        "sandhi": "इ + उ → यु: इति + उक्ताः → इत्युक्ताः · विसर्ग + च → श्च: स्नेहाः + च → स्नेहाश्च · ट् → ड् (घोष य से पहले): षट् + ये → षड् ये।",
        "contrast": "श्लोक ११९ (सार: ‘इति उक्ताः’) ≠ श्लोक ११४ (भूमिका: ‘अथ’ नया वर्ग): एक पीछे देखता है, दूसरा आगे।",
        "chunks": "इत्युक्ताः | फलमूलिन्यः | स्नेहाश्च लवणानि च ‖ मूत्रं क्षीराणि | वृक्षाश्च षड् ये | दिष्टपयस्त्वचः।",
    },
}

IMAGE_SPECS = {
    ("115", "diagram"): {
        "file": "uses-115.svg",
        "alt": "A table of three plants of verse 115 and their use: aśmantaka for emesis, snuhī latex for purgation, arka latex for emesis together with purgation",
        "type": "table",
        "title": "तीन पौधे, तीन कर्म",
        "heads": ["पौधा", "कर्म"],
        "rows": [["अश्मन्तकम्", "वमने"],
                 ["स्नुहीक्षीरम्", "विरेचने"],
                 ["क्षीरमर्कस्य", "वमने सविरेचने"]],
    },
}
