# Word check: charaka-samhita

- tokens: 98096, distinct: 50859
- stray characters / impossible sequences: 180 (stray.tsv)
- rare tokens near a frequent token: 96 (typos.tsv, tier 1 = difference inside the word, tier 2 = at the last akshara; rare = seen <= 2, frequent = seen >= 20)
- verse lines outside 15-17 / 22-23 aksharas: 1882 (metre.tsv)
- compare texts: 0, vocabulary 0

## Akshara counts per part (verse lines)
- part 01: 3711 lines; most common 16:3196, 22:86, 17:43, 15:36, 11:33
- part 06: 10375 lines; most common 16:8386, 22:828, 17:186, 18:173, 19:134
- part 08: 1396 lines; most common 16:922, 22:256, 21:31, 24:31, 17:15
- part 02: 386 lines; most common 16:195, 11:10, 5:8, 4:7, 12:6
- part 03: 480 lines; most common 16:162, 5:13, 21:11, 11:9, 17:9
- part 04: 685 lines; most common 16:375, 22:86, 4:8, 24:8, 15:7
- part 05: 729 lines; most common 16:662, 11:13, 4:11, 17:7, 15:5
- part 07: 726 lines; most common 16:645, 11:13, 4:13, 17:6, 22:6

## First stray rows
- 01.11.P6 unexpected character U+2018 संशयश्चात्र कथं भविष्याम इतश्च्युता नवेति; कुतः पुनः संशय इत
- 01.11.P7 unexpected character U+2019 स्वभावं परनिर्माणं यदृच्छां चापरे जनाः ॥ इति ।’ अतः संशयः---
- 01.11.P11 unexpected character U+002E तत्रातिप्रभावतां दृश्यानाम् अतिमात्रं दर्शनम् अतियोगः, सर्वश
- 01.18.7-2 word starts with a sign/matra/virama ंर्दुः
- 01.30.12a unexpected character U+002E तत्फला बहुधा वा ताः फलन्तीव (आ.ति। महाफलाः ।
- 06.01.1.8b unexpected character U+002E U+2018 ‘वृषतां‘ इति पा-. लाभोपायो हि शस्तानां रसादीनां रसायनम्॥
- 06.01.1.11c unexpected character U+002E च पा-.
- 06.01.1.35b unexpected character U+002E U+2018 U+2019 सेवेरन्नाभयामेते क्षुत्तृष्णोष्णार्दिताश्च ये॥) ‘योगीन्द्रना
- 06.01.P14 unexpected character U+002E प-.
- 06.01.P24 unexpected character U+002E गङ्गाधरस् तुपठित्वाव्याख्याम् अयति. (इति नागबलारसायनम्।)
- 06.01.P35 unexpected character U+002E योगीन्द्रनाथसेनस् तुइत्य् आदि पाठं पठति.
- 06.01.3.39c unexpected character U+002E योगीन्द्रनाथसेनः.
- 06.01.3.46c unexpected character U+002E योगीन्द्रनाथसेन.
- 06.01.3.51c unexpected character U+2018 ‘शित्लाजतु कोष्णे वातहरादिक्वाथे प्रक्षिप्य अथैनं रौद्रे शोष
- 06.01.3.51e unexpected character U+002E U+2019 अनेन विधिना सप्ताहं (सप्तवारान्) तस्य भावना’ इति गङ्गाधरः.
- 06.01.P46 unexpected character U+002E योगीन्द्रनाथसेनः.
- 06.01.4.7 unexpected character U+2018 U+2019 ब्रह्मसुवर्चला नामौषधिर्या हिरण्यक्षीरा पुष्करसदृशपत्रा, आदि
- 06.01.4.46c unexpected character U+002E U+2019 अन्यानि हवींषि च’ इति पा-.
- 06.01.4.53c unexpected character U+002E योगीन्द्रनाथसेनः.
- 06.01.4.55c unexpected character U+002E योगीन्द्रनाथसेनः.

## First typo suspects
- tier 1 06.06.53a प्रभवन्ति (2x) ~ भवन्ति (304x)
- tier 1 04.03.1 व्याध्यास्यामः (1x) ~ व्याख्यास्यामः (138x)
- tier 1 06.06.22b प्रपिबेत् (2x) ~ पिबेत् (201x)
- tier 1 03.08.9 भगवति (2x) ~ भवति (190x)
- tier 1 01.28.42b अप्रयोजयेत् (1x) ~ प्रयोजयेत् (90x)
- tier 1 06.29.100b नियोजयेत् (1x) ~ प्रयोजयेत् (90x)
- tier 1 01.26.84 अपयसा (1x) ~ पयसा (87x)
- tier 1 06.01.4.2 भागवानात्रेयः (2x) ~ भगवानात्रेयः (146x)
- tier 1 06.12.102a प्रकरोति (1x) ~ करोति (70x)
- tier 1 06.07.69b परमम् (1x) ~ परम् (67x)
- tier 1 06.05.137a प्रदद्यात् (1x) ~ दद्यात् (62x)
- tier 1 06.17.14a प्रवर्तेते (1x) ~ प्रवर्तते (47x)
- tier 1 03.06.9 *प्रवर्तते (1x) ~ प्रवर्तते (47x)
- tier 1 03.07.P22 संवर्तते (1x) ~ प्रवर्तते (47x)
- tier 1 04.03.13 व्यावर्तते (1x) ~ प्रवर्तते (47x)
- tier 1 05.07.7b विवर्तते (1x) ~ प्रवर्तते (47x)
- tier 1 01.25.44a संप्रयोजयेत् (2x) ~ प्रयोजयेत् (90x)
- tier 1 06.01.1.5a अभेषजं (1x) ~ भेषजं (43x)
- tier 1 01.06.23a कारेयेत् (1x) ~ कारयेत् (41x)
- tier 1 01.13.74b मारयेत् (1x) ~ कारयेत् (41x)
- tier 1 06.25.102b संप्रशस्यते (1x) ~ प्रशस्यते (41x)
- tier 1 06.01.P30 ससर्पिषा (1x) ~ सर्पिषा (37x)
- tier 1 08.03.P1 दृढबलस्ंपूरिते (1x) ~ दृढबलसंपूरिते (37x)
- tier 1 06.05.168b संदीपनं (1x) ~ दीपनं (36x)
- tier 1 06.15.223a विपादयेत् (1x) ~ विपाचयेत् (36x)
- tier 1 01.27.293b चिशेषेण (1x) ~ विशेषेण (34x)
- tier 1 06.02.1.5b स्त्रीशरीरे (1x) ~ शरीरे (34x)
- tier 1 06.12.55a सचित्रकं (1x) ~ चित्रकं (34x)
- tier 1 02.06.10 विशेषण (1x) ~ विशेषेण (34x)
- tier 1 01.26.71b चापरम् (2x) ~ परम् (67x)