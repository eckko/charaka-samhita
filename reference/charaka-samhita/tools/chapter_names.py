#!/usr/bin/env python3
"""Chapter names for toc.md, taken from the colophon of each chapter.

name_of(chapter) -> (iast_name, how). The colophon reads
"... <sthāna> <name> nāma <ordinal> adhyāyaḥ"; the name is the words
between the sthāna word and "nāma". Sandhi at the end is undone only for
the usual "-o nāma" -> "-aḥ" and "-ir nāma" -> "-iḥ", and a leading
avagraha mark (') is dropped. A few colophons are missing or misspelt;
those names come from the chapter's opening formula "athāto X ...
vyākhyāsyāmaḥ" (OVERRIDES, each says so).
"""
import re

OVERRIDES = {
    # (sthana, adhyaya): (name, how)
    (3, 4): ("trividharogaviśeṣavijñānīyaṃ vimānaṃ", "colophon"),
    (3, 8): ("rogabhiṣagjitīyaṃ vimānaṃ",
             "opening formula (colophon has no name)"),
    (4, 3): ("khuḍḍīkāgarbhāvakrāntiśārīraṃ", "colophon"),
    (4, 4): ("mahatīgarbhāvakrāntiśārīraṃ",
             "colophon (a stray space inside the word removed)"),
    (5, 8): ("avākśirasīyamindriyaṃ",
             "opening formula (colophon spells it avākṇirasīya)"),
    (6, 1): ("rasāyanādhyāyaḥ",
             "colophon; four pādas: abhayāmalakīya, prāṇakāmīya, "
             "karapracitīya, āyurvedasamutthānīya"),
    (6, 2): ("vājīkaraṇādhyāyaḥ",
             "colophon; four pādas: saṃyogaśaramūlīya, āsiktakṣīrika, "
             "māṣaparṇabhṛtīya, pumāñjātabalādika"),
    (6, 8): ("rājayakṣmacikitsitaṃ", "colophon"),
}


def name_of(chapter):
    key = (chapter["sthana"], chapter["adhyaya"])
    if key in OVERRIDES:
        return OVERRIDES[key]
    colophons = [r["text"] for r in chapter["rows"] if r["kind"] == "trailer"]
    for text in colophons:
        text = re.sub(r"\s+", " ", text.replace("&", ""))
        match = re.search(
            r"(?:sthāne|rasāyanādhyāye|vājīkaraṇādhyāye)\s+(.+?)\s*"
            r"nām(?:a|ā|o|au|ai|ṣ)?", text)
        if match:
            name = match.group(1).strip()
            name = re.sub(r"^'", "", name)
            name = re.sub(r"o$", "aḥ", name)
            name = re.sub(r"ir$", "iḥ", name)
            return name, "colophon"
    return "", "none"
